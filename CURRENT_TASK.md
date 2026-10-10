# CURRENT TASK — v0.5 + Storage Affinity Integration and Clean Baseline

Task ID: `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`

State: `ACTIVE_REMOTE_LIFECYCLE_CLOSEOUT`

Mode: `POST_MERGE_BRANCH_RECONCILIATION`

Authoritative branch: `main`

## Integrated baseline

- Audited integrated reusable candidate I1: `ee091fcdbad0e3edcec2b544067021068a0d54b9`.
- PR #17 control head B1: `22f8ceaa40adf41c3a18826a2b4f5eb944ebf578`.
- PR #17 merged with exact-head protection.
- Accepted merge/main SHA: `4b762490c035ecd0de0caa587c6e8a0e843377f1`.
- `I1..4b762490` changes only `CURRENT_STATUS.md` and `CURRENT_TASK.md`; merged `plugin.json + skills/**` is payload-equivalent to exact audited I1.

## Post-merge authorization

The user authorized repository closeout before any local Plugin testing.

Classify every remote non-main branch and remove branches only when their disposition is proven terminal/superseded and no unresolved unique authority/evidence requires retention.

Safe deletion classes:

1. branch fully contained in current `main`;
2. branch tied to an already merged/terminal PR and no longer carrying active authority;
3. completed one-shot publisher/release-transport branch after the corresponding release/tag/artifact evidence is durable;
4. superseded v0.5 design/implementation/storage/integration branches after their reusable content is present in merged `main` and any historical design/plan authority needed going forward is preserved in `main`.

Do not delete a branch solely because it is old. If a branch carries unique historical evidence not preserved elsewhere and its disposition is not established, retain it explicitly as frozen/non-writing or preserve that evidence before deletion.

## Closeout verification

Before declaring a clean baseline, verify:

- PR #17 is merged/closed;
- `main` has `plugin.json` version `0.5.0`;
- exactly three top-level Skills remain;
- no open PR remains;
- all remaining non-main branches, if any, have explicit justified retention;
- no remaining branch is an active or write-capable predecessor for the integrated Plugin authority;
- published Plugin remains v0.4.0 until a later release task;
- no local install/runtime mutation has occurred in this task.

## Out of scope

- publishing v0.5.0;
- local install/runtime V1;
- business-project mutation;
- installed Plugin/cache changes.

## Final target

`EG_V0.5_INTEGRATED_MAIN_CLEAN_BASELINE_READY_FOR_INSTALL_TEST`
