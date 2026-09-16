#!/usr/bin/env python3
"""Public-only portfolio updates. Fetch completely before touching generated files."""
import argparse
import datetime as dt
import html
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

OWNER = 'wangyuqin378-cpu'
REPOS = ('voice-todo', 'jianwei', 'context-continuity', 'prompt-generation-loop', 'codex-resume-manager')
# Fixed start preserves missed weeks when a scheduled run is delayed or disabled.
SINCE = '2026-08-17T00:00:00Z'
TZ = dt.timezone(dt.timedelta(hours=8))
START, END = '<!-- updates:start -->', '<!-- updates:end -->'


def timestamp(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))


def bot(user, name='', email=''):
    user = user or {}
    return (user.get('type') == 'Bot' or user.get('login', '').lower().endswith('[bot]')
            or '[bot]' in email.lower() or name.lower() in ('github-actions', 'dependabot'))


class GitHub:
    def __init__(self, token=None):
        self.token = token

    def get(self, path):
        # No caller-supplied host: credentials only ever go to api.github.com.
        if not path.startswith('/repos/' + OWNER + '/'):
            raise ValueError('Unexpected API path')
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': OWNER + '-profile',
                   'X-GitHub-Api-Version': '2022-11-28'}
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        request = urllib.request.Request('https://api.github.com' + path, headers=headers)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    return json.load(response)
            except urllib.error.HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                    raise
            except (urllib.error.URLError, TimeoutError):
                if attempt == 2:
                    raise
            time.sleep(2 ** attempt)

    def pages(self, path):
        items = []
        for page in range(1, 101):
            separator = '&' if '?' in path else '?'
            batch = self.get(path + separator + urllib.parse.urlencode({'per_page': 100, 'page': page}))
            if not isinstance(batch, list):
                raise ValueError('Expected an API list')
            items.extend(batch)
            if len(batch) < 100:
                return items
        raise RuntimeError('Pagination limit reached; previous output preserved')


def collect(api):
    events = []
    cutoff = timestamp(SINCE)
    for repo in REPOS:
        prefix = f'/repos/{OWNER}/{repo}'
        info = api.get(prefix)
        if info.get('private') is not False or info.get('full_name') != f'{OWNER}/{repo}':
            raise ValueError(f'{repo}: repository is not the expected public source')
        branch = info['default_branch']

        def event(kind, key, title, date, url):
            if timestamp(date) < cutoff:
                return
            expected = f'https://github.com/{OWNER}/{repo}/'
            if not url.startswith(expected):
                raise ValueError('Unexpected event URL')
            events.append({'id': f'{repo}:{kind}:{key}', 'repo': repo, 'kind': kind,
                           'title': title, 'date': date, 'url': url})

        for release in api.pages(prefix + '/releases'):
            if release['draft'] or not release.get('published_at'):
                continue
            event('release', release['id'], (release.get('name') or release['tag_name']) + (' (prerelease)' if release.get('prerelease') else ''),
                  release['published_at'], release['html_url'])

        pulls = api.pages(prefix + '/pulls?' + urllib.parse.urlencode({'state': 'closed', 'base': branch}))
        merged = {p['number']: p for p in pulls if p.get('merged_at')}
        for p in merged.values():
            if not bot(p.get('user')):
                event('pr', p['number'], p['title'], p['merged_at'], p['html_url'])

        commits = api.pages(prefix + '/commits?' + urllib.parse.urlencode({'sha': branch, 'since': SINCE}))
        for c in commits:
            author = c['commit']['author']
            if bot(c.get('author'), author.get('name', ''), author.get('email', '')):
                continue
            # Includes squash, merge and rebase commits. A PR is represented once.
            associated = api.pages(prefix + f"/commits/{c['sha']}/pulls")
            represented = False
            for p in associated:
                if p.get('merged_at') and p.get('base', {}).get('ref') == branch and p.get('base', {}).get('repo', {}).get('full_name') == info['full_name']:
                    represented = True
                    if not bot(p.get('user')):
                        event('pr', p['number'], p['title'], p['merged_at'], p['html_url'])
            if represented:
                continue
            event('commit', c['sha'], c['commit']['message'].splitlines()[0],
                  author['date'], c['html_url'])
    # Rebuild from the fixed window rather than keeping stale duplicate events.
    unique = {e['id']: e for e in events}
    return sorted(unique.values(), key=lambda e: (timestamp(e['date']), e['id']), reverse=True)


def escape(text):
    text = html.escape(' '.join(text.split()), quote=False)
    return re.sub(r'([\\`*{}\[\]()#+.!_|>~-])', r'\\\1', text)


def line(event, zh=False):
    date = timestamp(event['date']).astimezone(TZ).date().isoformat()
    kind = ('版本发布' if zh else 'Release') if event['kind'] == 'release' else ('开发更新' if zh else 'Development update')
    return f"- {date} · **{kind}** · {event['repo']} — [{escape(event['title'])}]({event['url']})"


def generated(root, events):
    outputs = {}
    for filename, zh in [('README.md', False), ('README.zh-CN.md', True)]:
        original = (root / filename).read_text()
        if original.count(START) != 1 or original.count(END) != 1 or original.index(START) >= original.index(END):
            raise ValueError(f'{filename}: expected one ordered marker pair')
        body = '\n'.join(line(e, zh) for e in events[:5]) or ('暂无公开更新。' if zh else 'No public updates yet.')
        outputs[filename] = original[:original.index(START)] + START + '\n' + body + '\n' + original[original.index(END):]
    archive = '# Public updates / 公开进展\n\nOriginal dates and source links. Weeks and displayed dates use Asia/Shanghai (UTC+8).\nOnly the public repositories listed in [MAINTENANCE.md](MAINTENANCE.md) are included.\n\n'
    week = None
    for e in events:
        iso = timestamp(e['date']).astimezone(TZ).isocalendar()
        group = f'{iso.year}-W{iso.week:02d}'
        if group != week:
            archive += f'## {group}\n\n'
            week = group
        archive += line(e) + '\n\n'
    outputs['UPDATES.md'] = archive
    outputs['data/updates.json'] = json.dumps({'since': SINCE, 'events': events}, ensure_ascii=False, indent=2) + '\n'
    return outputs


def update(root, api):
    # API errors, invalid public sources and malformed markers cannot erase past output.
    outputs = generated(root, collect(api))
    changed = []
    for name, content in outputs.items():
        path = root / name
        if path.exists() and path.read_text() == content:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name + '.tmp')
        temporary.write_text(content)
        temporary.replace(path)
        changed.append(name)
    return changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        changed = update(args.root, GitHub(os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')))
    except Exception as exc:
        print(f'Update failed ({type(exc).__name__}); previous published output is unchanged.', file=sys.stderr)
        return 1
    print('Updated: ' + ', '.join(changed) if changed else 'No new content; no files changed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
