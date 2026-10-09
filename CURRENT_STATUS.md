# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-09.

## Published Plugin v0.2.0

- GitHub Release `plugin-v0.2.0` is published and independently verified.
- Release title: `Engineering Governance Plugin v0.2.0`.
- Package version: `0.2.0`.
- Exact release/source SHA: `cf2df83e7e6bde39a5cce7f51e47d59e3911d71c`.
- Release tag `plugin-v0.2.0` resolves directly to that exact commit.
- Release is neither draft nor prerelease.
- Release asset: `engineering-governance-plugin.zip`.
- Published asset size: `36224` bytes.
- Published asset SHA-256: `99ab0679c5692dd382d515cf39a92c6fb1e9c68ae119c43637b3cec65b19436e`.
- The release contains exactly the Plugin payload surface: `plugin.json` plus `skills/**` under root `engineering-governance/`.
- Exactly three reusable Skills are included: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Accepted v0.2.0 capability baseline

The published release includes the accepted reusable changes merged after Plugin v0.1.0:

- Domain Navigation current-task authority gate and bounded/historical snapshot navigation;
- one canonical authority per fact/state/behavior class;
- domain-coherent code structure and anti-redundancy guidance;
- task lifecycle integrity;
- exact evidence/artifact identity binding with proven-equivalence reuse;
- selected task-workspace identity with bounded discovery.

No MCP, hooks, daemon, runtime service, database, telemetry, installer, automatic refactor, or automatic remediation was added.

## Current task

- Task: `EG-PROJECT-GOVERNANCE-WORKSPACE-LIFECYCLE-039`.
- State: `ACTIVE`.
- Mode: `BOUNDED_GOVERNANCE_CHANGE`.
- Start baseline: `main` at `533cefb1dcf07b4fde5a489408fbc8fa6f0e324e`.
- Authorized branch: `codex/project-governance-workspace-lifecycle-v1`.
- Objective: add a reusable workspace/worktree lifecycle and closeout contract to `project-governance`, including bounded pre-task classification, same-authority successor gating, terminal closeout, explicit retention, and non-destructive unique-work handling.

## Next milestone

Implement the accepted workspace lifecycle contract in `project-governance`, update its templates/references consistently, run V0 diff/content/link/scope verification plus a self-audit for contradictions or overreach, then merge only if the exact reviewed branch remains aligned with the authorized baseline and scope.
