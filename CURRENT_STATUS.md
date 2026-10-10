# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Published Plugin baseline

- Latest published Release remains `plugin-v0.4.0`.
- Exact published source SHA: `204f74952ce53fb97180e42f537fdf3236d1c48e`.
- Published package version: `0.4.0`.
- No v0.5 release has been published under this task.

## Integrated v0.5 candidate

Exact integrated source candidate:

`I1 = ee091fcdbad0e3edcec2b544067021068a0d54b9`

Integration base after the owner-approved control transition:

`467a92daa1bc6c43a7c874684a607c9a637a4dc9`

Inputs reconciled:

- v0.5 Navigation Refresh + Follow-ups A2: `ecadcf67bf00a5a82cd644cd822ad4d45a76a420`;
- Project Storage Affinity implementation: `c250b9b081a93949f1d000165e64dcaa53610bdb`.

I1 is a fresh integrated candidate rather than a blind merge of either old branch.

## Integrated source audit

`INTEGRATED_SOURCE_AUDIT_I1 = PASS`

- Critical: `0`
- Important: `0`
- Plugin metadata: `0.5.0`
- Top-level Skill count: exactly `3`
- Skills: `project-governance`, `domain-navigation`, `incident-doctor`
- Global Router responsibility: unchanged / selection-only
- Navigation affected-only refresh: preserved
- Navigation current-route no-churn: preserved
- Historical/read-only mutation boundaries: preserved
- Lightweight Follow-up retention and Task authorization boundary: preserved
- Project Storage Affinity: preserved
- Machine/runtime and ephemeral-scratch separation: preserved
- Universal host/volume rule added: `NO`
- New Skill/control/Findings/storage runtime subsystem: `NO`
- Engineering-Governance-only Web/local execution split in root `AGENTS.md`: reconciled

The v0.5 maintainer Plan is retained as historical planning material and explicitly states that its former merge/release/test sequencing is superseded by the active integration task.

## Main freshness

Live `main` was reverified after the source audit and remained:

`467a92daa1bc6c43a7c874684a607c9a637a4dc9`

No Plugin payload or control drift occurred during candidate construction.

## Active task

Task: `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049`.

State: `READY_FOR_EXACT_HEAD_MERGE`.

Mode: `INTEGRATED_SOURCE_AUDIT_ACCEPTED`.

Integration branch:

`codex/v0.5-storage-affinity-integration-v1`

## Next step

Create a control-only receipt after I1, prove that receipt changes only root `CURRENT_STATUS.md` / `CURRENT_TASK.md`, open an exact-head PR to `main`, merge the audited integrated candidate, verify merged main payload, then immediately begin remote lifecycle closeout of terminal historical PR/release/publisher branches.

Do not publish v0.5.0 and do not run local Plugin behavior V1 until the remote repository is reduced to the clean unique baseline (plus only explicitly justified retained historical refs, if any).
