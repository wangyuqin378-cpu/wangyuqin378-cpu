import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('updates', Path(__file__).parents[1] / 'scripts/update_profile.py')
u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)
DATE = '2026-09-15T18:30:00Z'

class FakeAPI:
    def __init__(self):
        self.data = {}
        for repo in u.REPOS:
            p = f'/repos/{u.OWNER}/{repo}'
            self.data[p] = {'private': False, 'full_name': f'{u.OWNER}/{repo}', 'default_branch': 'main'}
            self.data[p + '/releases'] = []
            self.data[p + '/pulls'] = []
            self.data[p + '/commits'] = []
        self.prefix = f'/repos/{u.OWNER}/jianwei'
        self.data[self.prefix + '/commits'] = [self.commit('a')]
        self.data[self.prefix + '/commits/a/pulls'] = []
        self.fail = None
    def commit(self, sha, user=None):
        return {'sha': sha, 'author': user or {'login': u.OWNER, 'type': 'User'},
                'html_url': f'https://github.com/{u.OWNER}/jianwei/commit/{sha}',
                'commit': {'message': 'Improve photo discovery\n\nDetails', 'author': {'name': 'Yuqin Wang', 'email': 'maker@example.invalid', 'date': DATE}}}
    def get(self, path):
        if self.fail and self.fail in path:
            raise ConnectionError('simulated API failure')
        return copy.deepcopy(self.data[path.split('?')[0]])
    pages = get

class UpdatesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ['README.md', 'README.zh-CN.md']:
            (self.root / name).write_text('# Profile\n' + u.START + '\nPrevious\n' + u.END + '\nKeep footer\n')
        self.api = FakeAPI()
    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
    def test_new_update_has_original_link_date_and_both_languages(self):
        changed = u.update(self.root, self.api)
        self.assertEqual(len(changed), 4)
        en = (self.root / 'README.md').read_text()
        self.assertIn('2026-09-16', en) # UTC+8 date
        self.assertIn('Development update', en)
        self.assertIn('/commit/a', en)
        self.assertIn('Keep footer', en)
        self.assertIn('开发更新', (self.root / 'README.zh-CN.md').read_text())
        self.assertIn('2026-W38', (self.root / 'UPDATES.md').read_text())
        self.assertEqual(json.loads((self.root / 'data/updates.json').read_text())['events'][0]['date'], DATE)
    def test_no_update_does_not_write(self):
        u.update(self.root, self.api)
        before = self.snapshot()
        mtimes = {p: p.stat().st_mtime_ns for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(u.update(self.root, self.api), [])
        self.assertEqual(before, self.snapshot())
        self.assertTrue(all(p.stat().st_mtime_ns == mtime for p, mtime in mtimes.items()))
    def test_pr_merge_squash_and_rebase_deduplicate(self):
        p = self.api.prefix
        pr = {'number': 5, 'title': 'Improve discovery', 'merged_at': DATE, 'user': {'type': 'User'},
              'base': {'ref': 'main', 'repo': {'full_name': f'{u.OWNER}/jianwei'}},
              'html_url': f'https://github.com/{u.OWNER}/jianwei/pull/5'}
        self.api.data[p + '/pulls'] = [pr]
        self.api.data[p + '/commits'] = [self.api.commit(s) for s in ('a','b','c')]
        for sha in ('a','b','c'):
            self.api.data[p + f'/commits/{sha}/pulls'] = [pr]
        events = u.collect(self.api)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['kind'], 'pr')
    def test_api_failure_preserves_every_output(self):
        u.update(self.root, self.api)
        before = self.snapshot()
        # Fail after another repository has been successfully read.
        self.api.fail = '/context-continuity/releases'
        with self.assertRaises(ConnectionError):
            u.update(self.root, self.api)
        self.assertEqual(before, self.snapshot())
    def test_private_source_aborts_before_publishing(self):
        u.update(self.root, self.api)
        before = self.snapshot()
        self.api.data[self.api.prefix]['private'] = True
        with self.assertRaises(ValueError):
            u.update(self.root, self.api)
        self.assertEqual(before, self.snapshot())
    def test_bot_commit_is_excluded(self):
        self.api.data[self.api.prefix + '/commits'] = [self.api.commit('b', {'login': 'robot[bot]', 'type': 'Bot'})]
        self.assertEqual(u.collect(self.api), [])
    def test_release_and_latest_five_archive(self):
        p = self.api.prefix
        self.api.data[p + '/releases'] = [{'id': n, 'name': f'v{n}', 'draft': False,
            'published_at': DATE, 'html_url': f'https://github.com/{u.OWNER}/jianwei/releases/tag/v{n}'} for n in range(7)]
        u.update(self.root, self.api)
        self.assertEqual((self.root / 'README.md').read_text().count('\n- '), 5)
        self.assertEqual((self.root / 'UPDATES.md').read_text().count('\n- '), 8)
        self.assertIn('**Release**', (self.root / 'UPDATES.md').read_text())
    def test_malformed_markers_preserve_all_output(self):
        (self.root / 'README.zh-CN.md').write_text('No markers')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            u.update(self.root, self.api)
        self.assertEqual(before, self.snapshot())
    def test_titles_cannot_inject_markdown(self):
        s = u.escape('[Click](https://example.invalid)\n<img src=x>')
        self.assertNotIn('\n', s)
        self.assertIn('\\[Click\\]', s)
        self.assertNotIn('<img', s)

if __name__ == '__main__':
    unittest.main()
