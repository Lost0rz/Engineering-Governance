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
- The accepted lifecycle semantics cover bounded task-relevant classification, overlapping-authority writer gating, retained write-capability handling, project-defined terminal-event semantics, unique-work preservation, legacy reconciliation, and remote/local evidence boundaries.
- Exactly three reusable top-level Skills remain: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Release decision

The accepted reusable capability added after Plugin v0.2.0 warrants a minor release. The next Plugin version is `0.3.0` with GitHub Release tag `plugin-v0.3.0`.

The release payload remains exactly:

- `plugin.json`
- `skills/**`

under one ZIP root `engineering-governance/`.

## Current task

- Task: `EG-PLUGIN-V0.3.0-RELEASE-041`.
- State: `AUTHORIZED_FOR_RELEASE_PREP_AND_PUBLICATION`.
- Mode: `PLUGIN_RELEASE`.
- Authorized source branch: `codex/plugin-v0.3.0-release-v1`.
- Allowed reusable-source change during release prep: `plugin.json` version `0.2.0 -> 0.3.0` only; Skill semantics are frozen.
- Root controls may record release evidence and lifecycle state.
- Publication transport may use a separate remote-only publisher branch because the current GitHub connector does not expose direct Release/tag/asset creation. That transport branch must not be merged into `main`, must not be the Release target, and must not enter the Plugin ZIP.

## Next milestone

Prepare and audit the exact v0.3.0 release-source diff, merge it, package from the exact merged source SHA, publish `plugin-v0.3.0`, independently verify release target and asset identity, then close task 041. The next step after release is installation/acceptance testing in target projects, not further governance expansion by default.
