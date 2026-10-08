# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-08.

## Accepted reusable baseline

- Exactly three reusable Skills remain: `project-governance`, `domain-navigation`, and `incident-doctor`.
- Plugin v0.1.0 remains the currently published package.
- DN-001 authority-gate corrective was accepted and merged in PR #7.
- Project Governance canonical-authority/code-structure enhancement was accepted and merged in PR #8.
- Project Governance lifecycle/evidence-identity/workspace-integrity enhancement was independently audited and merged in PR #9.
- Current accepted `main` before this release-control transition: `302dd233036ec77a423fa870d1ca994613d415c4`.

## Release decision

The accumulated accepted changes are now large enough for an overall Plugin minor release rather than a patch-only corrective. The next package version is `0.2.0` and the GitHub Release tag is `plugin-v0.2.0`.

The release payload remains exactly the packaged Plugin surface:

- `plugin.json`
- `skills/**`

under ZIP root `engineering-governance/`.

Root governance controls, maintainer docs/history, examples, Git metadata, caches, secrets, and unrelated repository files are not part of the packaged payload.

## Current task

- Task: `EG-PLUGIN-V0.2.0-RELEASE-038`.
- State: `AUTHORIZED_FOR_RELEASE_PREP_AND_PUBLICATION`.
- Mode: `PLUGIN_RELEASE`.
- Allowed product change: bump `plugin.json` package version `0.1.0 -> 0.2.0`; do not change Skill semantics during release preparation.
- Release must be built from an exact accepted merged source revision and verified by file list plus SHA-256 before publication.

## Next milestone

Prepare and independently verify the exact v0.2.0 payload, merge only the release metadata change, package `engineering-governance-plugin.zip`, publish GitHub Release `plugin-v0.2.0`, and verify the published release target and asset identity.
