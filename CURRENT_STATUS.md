# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Published Plugin v0.2.0

- GitHub Release `plugin-v0.2.0` remains the published release.
- Package version: `0.2.0`.
- Exact release/source SHA: `cf2df83e7e6bde39a5cce7f51e47d59e3911d71c`.
- Release asset SHA-256: `99ab0679c5692dd382d515cf39a92c6fb1e9c68ae119c43637b3cec65b19436e`.
- The published v0.2.0 artifact does not include the workspace-lifecycle changes merged after that release or this corrective task.

## Accepted repository main

- Current verified `main`: `1e80848880b902ccf56ffcd70e22b19788b7b8d4`.
- Task `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-039` is closed and merged.
- `project-governance` includes the workspace/worktree lifecycle contract; task 040 corrects four semantic edge cases identified by the post-039 full audit.
- No new top-level Skill, runtime, CLI, daemon, database, hook, installer, or automatic cleanup/remediation capability is added.

## Current task

- Task: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-CORRECTIVE-040`.
- State: `READY_FOR_MERGE`.
- Mode: `BOUNDED_GOVERNANCE_CORRECTIVE`.
- Start baseline: `main` at `1e80848880b902ccf56ffcd70e22b19788b7b8d4`.
- Authorized branch: `codex/project-governance-workspace-lifecycle-corrective-v1`.
- Reviewed corrective HEAD: `1e1affa284d7d3e3bfacfb44f19ee58d5f3778b9`.
- Reviewed tree: `b5e818ea93359ba98ef680d55d9e5796927b6fa7`.
- V0 whole-Skill audit: PASS for the four corrective requirements, code-structure authority alignment, project-governance/domain-navigation/incident-doctor boundaries, path/link presence, bounded startup semantics, and absence of Plugin/runtime/automation scope expansion.
- Final diff versus exact baseline: ahead 10, behind 0; only nine authorized Markdown/control paths changed.

## Next milestone

Create an exact-head PR, independently re-read the PR diff and mergeability/status evidence, merge only if the reviewed head and base remain aligned, then verify merge-tree/content equivalence and close task 040. Plugin publication remains a separate future task.
