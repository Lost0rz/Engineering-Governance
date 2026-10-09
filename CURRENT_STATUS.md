# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Published Plugin v0.2.0

- GitHub Release `plugin-v0.2.0` remains the currently published release.
- Package version: `0.2.0`.
- Exact release/source SHA: `cf2df83e7e6bde39a5cce7f51e47d59e3911d71c`.
- Release asset SHA-256: `99ab0679c5692dd382d515cf39a92c6fb1e9c68ae119c43637b3cec65b19436e`.

## Accepted repository baseline

- Verified pre-release `main`: `fe59b6eb38a40f312f86872248d26f2e151bf07b`.
- Tasks 039/040 added and corrected the reusable `project-governance` workspace/worktree lifecycle contract.
- Exactly three reusable top-level Skills remain: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Plugin v0.3.0 release preparation

- Task: `EG-PLUGIN-V0.3.0-RELEASE-041`.
- State: `READY_FOR_SOURCE_PR`.
- Release-source branch: `codex/plugin-v0.3.0-release-v1`.
- Current reviewed release-source HEAD before control handoff: `20a7787bc67090d5f19be1a8e4c958b3254c11da`.
- Version metadata: `plugin.json` is `0.3.0`.
- Exact diff from start baseline is ahead 3 / behind 0 and contains only `plugin.json`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`; no Skill file changed.
- GitHub currently has no `plugin-v0.3.0` Release and no `refs/tags/plugin-v0.3.0`, so there is no conflicting publication identity.
- Release payload contract remains exactly `plugin.json` + `skills/**` under ZIP root `engineering-governance/`.
- Direct Release/tag/asset creation is unavailable in the current connector; if source PR is accepted, publication may use the task-authorized remote-only publisher branch. That transport must not enter `main`, the source tag, or the ZIP.

## Next milestone

Create and independently inspect the exact release-source PR. If accepted, merge with expected-head protection, lock the resulting merged source SHA, publish `plugin-v0.3.0` from that exact SHA, verify the GitHub-reported asset digest/size and release target, then close task 041.
