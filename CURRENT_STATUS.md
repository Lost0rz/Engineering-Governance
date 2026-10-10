# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Published Plugin

- Latest published Release remains `plugin-v0.4.0`.
- Published source SHA: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- No v0.5 release has been published yet.

## Integrated v0.5 main baseline

PR #17 merged the audited integrated v0.5 + Project Storage Affinity source.

- Audited integrated candidate I1: `ee091fcdbad0e3edcec2b544067021068a0d54b9`.
- PR/control head: `22f8ceaa40adf41c3a18826a2b4f5eb944ebf578`.
- Merge SHA: `4b762490c035ecd0de0caa587c6e8a0e843377f1`.
- Post-merge comparison from I1 changes only root `CURRENT_STATUS.md` and `CURRENT_TASK.md`; merged Plugin payload is exact-I1 equivalent.
- Plugin source version on merged main: `0.5.0`.
- Exactly three top-level Skills remain.
- Global Router remains selection-only.

Accepted integrated capabilities:

1. affected-only Navigation refresh with correct/no-churn, stale-same freshness refresh, unresolved, historical, and strict-read-only boundaries;
2. lightweight evidence-backed non-blocking `CURRENT_STATUS.md / Follow-ups` with explicit Task authorization before repair;
3. Project Storage Affinity derived from canonical project location, with explicit project override and separate machine/runtime + ephemeral scratch classes;
4. Engineering-Governance-only Web/remote construction and local runtime-validation execution split.

## Active closeout

Task: `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`.

State: `ACTIVE_REMOTE_LIFECYCLE_CLOSEOUT`.

Current work is remote branch/PR lifecycle reconciliation only. Terminal merged-PR, obsolete release, completed publisher, and superseded integration-input branches may be removed after their disposition is verified. Unique unresolved historical evidence must be retained or preserved explicitly rather than deleted by age.

## Testing/release boundary

Do not run local Plugin V1 and do not publish v0.5.0 until the remote repository has a clean unique development baseline with no unresolved parallel writer.

## Next milestone

Complete remote branch inventory and closeout, verify zero open PRs and one active development authority (`main`), then close this task as ready for the subsequent v0.5 packaging/release/install-test flow.
