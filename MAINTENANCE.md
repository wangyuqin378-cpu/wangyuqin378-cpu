# Maintaining this profile

[Validation record and remaining checks](VALIDATION.md)

## Content

- `README.md` is the English profile; `README.zh-CN.md` is the Chinese entry.
- Keep selected work in this order: Jianwei, City Copy, Context Continuity.
- Label prototypes and incomplete device/distribution checks explicitly.
- See [asset provenance](assets/README.md) before replacing images.
- Public source visibility is separate from a license grant. Do not infer permission from visibility.

## Weekly public updates

[Weekly public updates](https://github.com/wangyuqin378-cpu/wangyuqin378-cpu/actions/workflows/weekly-updates.yml) runs on Sundays at **20:30 Asia/Shanghai** and supports **Run workflow**. GitHub schedules can be delayed; they are not an exact-time delivery guarantee. Inactive public repositories may have scheduled workflows disabled after 60 days; re-enable the workflow in Actions if needed.

Sources are explicitly limited to these public repositories:

- `wangyuqin378-cpu/jianwei`
- `wangyuqin378-cpu/context-continuity`
- `wangyuqin378-cpu/prompt-generation-loop`
- `wangyuqin378-cpu/codex-resume-manager`

The script verifies public visibility before reading each source. It collects published releases (including labeled prereleases), merged pull requests targeting the default branch and non-bot commits reachable from the default branch. PR-associated commits are replaced by their PR entry, including squash/rebase merges. Releases and development changes have separate labels. Commit author dates and release/merge timestamps are retained in `data/updates.json`; displayed dates and week groups use UTC+8.

The fixed initial window starts **2026-08-17 UTC**. Re-reading this window catches missed runs and removes stale duplicates; prior weeks appear in `UPDATES.md`. It intentionally excludes older backfill and the profile bot's own repository. Update titles come directly from public GitHub records and may include documentation work, rather than implying every change is a shipped feature.

All API reads and output validation finish before files are written. On an API failure the job fails without committing and the previous published result stays intact. Generated files use atomic replacement. If content is unchanged, no commit is created. Bot commits do not represent the maker's own work or guarantee contribution-graph activity.

Run checks locally with Python 3.9+:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/update_profile.py
```

The second command can read unauthenticated public endpoints within their rate limit, or use `GH_TOKEN` / `GITHUB_TOKEN` from your environment. Never add a token to the repository. In Actions, the built-in token has only the repository content permission needed to push generated files.

## Completing ordinary project work

Finish the scoped change, run proportionate verification, update necessary documentation, then commit and push only that task's changes to the existing repository. Return the GitHub commit or PR link. Preserve the repository's visibility.

For projects with automatic deployments or branch protection, use a `codex/` task branch and a PR; follow the existing merge and release process. Do not create public repositories for local-only work without a separate decision. Design work, evaluations and documentation can be real contributions when they contain meaningful work. Do not create empty or repetitive commits to fill the graph.

## Platform references

- [Profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [Scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [Contribution attribution](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/troubleshooting-missing-contributions)
