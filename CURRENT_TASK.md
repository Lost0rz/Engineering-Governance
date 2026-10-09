# CURRENT TASK — Plugin v0.4.0 Release

Task ID: `EG-PLUGIN-V0.4.0-RELEASE-043`

State: `CLOSED`

Mode: `PLUGIN_RELEASE`

## Outcome

`RELEASED_VERIFIED`

Engineering Governance Plugin v0.4.0 was published from the exact accepted release source without changing Skill/plugin payload semantics during release preparation.

## Exact release identity

- Release/source SHA: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Tag: `plugin-v0.4.0` -> exact commit `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Release title: `Engineering Governance Plugin v0.4.0`.
- Release state: published, non-draft, non-prerelease.
- Asset: `engineering-governance-plugin.zip`.
- Size: `54754` bytes.
- SHA-256: `1d0d791acc167f47ff5d91b523528f53fed027f2bc9eac8d0b938983903a7922`.
- Package entries: `44`.
- Publisher run: `37916223246`, `success`.

## Source provenance

- Governance/routing PR #14 exact head: `3b969e45230923629d23bb0d1a432c1740b4ae3b`.
- PR #14 merge: `879521028a056a9fed4ce6fb9be89a6221eb80bf` with zero file differences from the exact PR head.
- Final audited reusable payload before control-only handoff: `0a00ebf1a5ebe17163431fa099249b8e2fc70a22`.
- Release-source branch started from `879521028a056a9fed4ce6fb9be89a6221eb80bf` and changed only `CURRENT_STATUS.md` and `CURRENT_TASK.md`.
- Release-source PR #15 exact head: `2088b2df13196482ec0cc8bf2b4b937d92b9d851`.
- Final merged release source: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Compare `879521028a056a9fed4ce6fb9be89a6221eb80bf` -> `204f74952ce53fb97180e42f537fdf3236d1c48e`: only `CURRENT_STATUS.md` and `CURRENT_TASK.md`; no `plugin.json` or `skills/**` mutation.

## Package verification

The one-shot publisher:

- confirmed Release/tag identity was unused;
- checked out exact source `204f74952ce53fb97180e42f537fdf3236d1c48e` rather than publisher HEAD;
- verified `plugin.json` version `0.4.0`;
- verified exactly three top-level Skills: `domain-navigation`, `incident-doctor`, `project-governance`;
- verified required routing/adoption/code-structure/workspace-lifecycle assets exist;
- verified the final code-structure guard is independent of edit size;
- verified normal-development workspace lifecycle checkpoints exist;
- rejected symlinks;
- packaged one `engineering-governance/` root containing only `plugin.json` and `skills/**`;
- rejected root controls, `.github`, docs, examples, root references, and transport files;
- produced size `54754`, SHA-256 `1d0d791acc167f47ff5d91b523528f53fed027f2bc9eac8d0b938983903a7922`, and `44` entries;
- published the exact Release.

GitHub Release metadata independently reports the same source SHA, asset name, size, and digest. The tag ref resolves directly to the exact release source. The tagged source has no `.github` publisher workflow.

## Accepted v0.4.0 behavior

- Project/repository engineering defaults to `project-governance`, including simple low-risk work with lightweight procedure.
- `domain-navigation` is conditional for unclear semantic/authority/source routes and reuses accepted maps.
- `incident-doctor` is reactive only when a real blocking failure plus insufficient evidence satisfies its gate.
- code structure is governed during construction by responsibility/Domain/authority/lifecycle/reason-to-change, never by universal line-count or edit-size thresholds;
- canonical authority prevents silent parallel truth/writers;
- task-relevant worktrees are checked at bounded lifecycle transitions so normal development closes debt while evidence is fresh; full historical archaeology is exceptional;
- historical control-parent inequality alone is not current-head drift; explicit locked-head equality remains hard;
- verification effort follows risk, not edit count, using `V0`–`V3` plus separate cadence.

## Workspace / transport disposition

- PR #14: merged / terminal.
- PR #15: merged / terminal.
- Publisher branch `codex/plugin-v0.4.0-publisher-v1`: transport-only and terminal after successful publication. It is not merged to `main` and is not part of the Release/tag/package. The available connector does not provide branch-ref deletion, so no remote branch deletion claim is made.
- Local branches/worktrees/install state: not inspected or claimed by this remote-only task.

## Next authorized milestone

Local reinstall and routing acceptance: synchronize local source/install state to published v0.4.0; install/upgrade all three Skills plus exactly one current managed global routing block; preserve unrelated global rules; verify repeated adoption is idempotent; then run representative real development requests to prove default Project Governance routing, conditional Domain Navigation, reactive Incident Doctor, construction-time structure governance, and bounded worktree lifecycle behavior.
