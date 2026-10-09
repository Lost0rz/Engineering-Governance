# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Published Plugin v0.2.0

- GitHub Release `plugin-v0.2.0` remains the published release.
- Package version: `0.2.0`.
- Exact release/source SHA: `cf2df83e7e6bde39a5cce7f51e47d59e3911d71c`.
- Release asset SHA-256: `99ab0679c5692dd382d515cf39a92c6fb1e9c68ae119c43637b3cec65b19436e`.
- The published v0.2.0 artifact does not include the workspace-lifecycle changes merged after that release.

## Accepted repository main

- Current verified `main`: `1e80848880b902ccf56ffcd70e22b19788b7b8d4`.
- Task `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-039` is closed and merged.
- `project-governance` includes the workspace/worktree lifecycle contract, but a complete follow-up audit identified four bounded semantic corrections before that contract should be treated as final.
- No new top-level Skill, runtime, CLI, daemon, database, hook, installer, or automatic cleanup/remediation capability is authorized.

## Current task

- Task: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-CORRECTIVE-040`.
- State: `ACTIVE`.
- Mode: `BOUNDED_GOVERNANCE_CORRECTIVE`.
- Start baseline: `main` at `1e80848880b902ccf56ffcd70e22b19788b7b8d4`.
- Authorized branch: `codex/project-governance-workspace-lifecycle-corrective-v1`.
- Objective: correct four lifecycle semantics found by the post-039 full audit: task-relevant workspace scope, overlapping-write-authority granularity, retained write-capable predecessor blocking, and project-defined terminal-event semantics.

## Next milestone

Implement only the four authorized semantic corrections, run V0 whole-Skill consistency and boundary audit, merge only if the exact branch remains aligned, then perform post-merge verification and close task 040. Plugin publication remains a separate future task.
