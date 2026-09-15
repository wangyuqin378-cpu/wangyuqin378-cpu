# Validation record — 2026-09-16

This records the profile refresh and checks on the public snapshots. It is not a product release certificate. Dates use Asia/Shanghai unless a linked service displays another timezone.

## Profile and publishing

- The [public profile](https://github.com/wangyuqin378-cpu) was opened without a GitHub login. The English introduction, Chinese entry, three selected projects, four experiments and five recent updates were present.
- Display name, bio and website were saved and checked through GitHub's API. Pins were verified in this order: `jianwei`, `context-continuity`, `prompt-generation-loop`, `codex-resume-manager`.
- Desktop and 390 × 844 responsive layouts were visually inspected in Safari in light and dark modes. Tables wrapped and product images remained readable. This is browser responsive inspection, not a physical-phone test.
- The [City Copy story](https://yuqin.wang/#/project/city) was opened in a browser; its description and three product images loaded. Source code remains private.
- All six existing public repositories received English introductions, Chinese entries and reviewed metadata. Existing visibility and license files were preserved.

## Repository checks

| Repository | Observed result | Remaining boundary |
| --- | --- | --- |
| [Context Continuity](https://github.com/wangyuqin378-cpu/context-continuity) | CLI version/help worked; 130 tests passed, including the checkpoint lifecycle. [Hosted check passed](https://github.com/wangyuqin378-cpu/context-continuity/actions/runs/35004822156). | Fixture-based checks do not establish success with every model or a new live agent session. |
| [Codex Resume Manager](https://github.com/wangyuqin378-cpu/codex-resume-manager) | Dependency installation, type checking, 87 app tests, 20 plugin tests and build passed. [Hosted check passed](https://github.com/wangyuqin378-cpu/codex-resume-manager/actions/runs/35004842722). | Natural usage-limit exhaustion → actual reset → exactly one continuation of the same task was not exercised. Installation reported three existing high-severity dependency findings. |
| [Jianwei](https://github.com/wangyuqin378-cpu/jianwei) | Local backend: 146 tests passed, 17 PostgreSQL tests skipped, build passed; the built local-provider server returned a successful health response. The [hosted iOS job passed](https://github.com/wangyuqin378-cpu/jianwei/actions/runs/35004810733). | That hosted run failed overall: Android SDK setup could not find package `tools`; the backend production dependency audit reported 8 high and 4 moderate findings, including `fast-uri` advisories. Physical-device, widget, content quality and distribution acceptance remain separate. |
| [Prompt Generation Loop](https://github.com/wangyuqin378-cpu/prompt-generation-loop) | Installation instructions, skill entry, relative links and worked input/output examples were reviewed. | A fresh host catalog registration and a live target-model evaluation were not performed; examples remain static. |
| [Just Do It](https://github.com/wangyuqin378-cpu/just-do-it) | Entry files and internal-service dependencies were inspected and documented. | The required internal services were unavailable for a complete workflow run. |
| [Texas Hold’em](https://github.com/wangyuqin378-cpu/texas-holdem) | Dependencies installed; the server served the game page; a Socket.IO room-creation request returned a room ID and game state with a seven-player limit. | Full multiplayer sessions and all poker rules were not accepted. Installation reported 8 existing dependency findings: 1 low, 3 moderate and 4 high. |

Dependency and environment findings above were observed during documentation validation. Application dependencies and runtime code were not changed by this refresh.

## Attribution and daily work

- The profile's [initial human commit](https://github.com/wangyuqin378-cpu/wangyuqin378-cpu/commit/f208c50e294eb8d46d3cda36c20357d19a03ee3c) and the six documentation commits were pushed with the verified GitHub noreply identity; GitHub returned `wangyuqin378-cpu` as the author account.
- Future commit identity was corrected in global Git settings and checked repository overrides. Historical commits were not rewritten.
- Anonymous private contribution counts were enabled and observed on the signed-out profile. No private repository names or work descriptions were added to public updates.
- A separate contribution-calendar API check reported **8 contributions on 2026-09-16** at the time of validation. This is a dated observation, not a daily activity guarantee.
- The local Codex completion rules now cover scoped verification, documentation, commit/push and a returned GitHub link. Deployment/protected repositories use task branches and PRs. Local-only projects still require a separate repository decision.

## Weekly update automation

- [First hosted run](https://github.com/wangyuqin378-cpu/wangyuqin378-cpu/actions/runs/35005014742): passed and published genuine public updates using `github-actions[bot]`.
- [Second manual run](https://github.com/wangyuqin378-cpu/wangyuqin378-cpu/actions/runs/35005127350): passed, reported no new content and skipped the commit.
- Nine automated tests passed locally and in Actions. They cover new content, unchanged file preservation, PR/commit deduplication, API failure preserving prior output, rejecting private sources, bot filtering, latest-five plus weekly history, malformed markers and title escaping.
- Schedule: Sunday **20:30 Asia/Shanghai**, plus manual dispatch. The four public source repositories are an explicit whitelist; the profile repository's bot commits are excluded.

See [maintenance instructions](MAINTENANCE.md) for routine edits and manual runs.
