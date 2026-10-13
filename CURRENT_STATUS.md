# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Published Plugin release: `plugin-v0.5.3`.

Accepted release source:

`255bd32b1414a9555a7280d6e7562411ed3c7d96`

Published asset:

- `engineering-governance-plugin.zip`
- size: `56926` bytes
- SHA-256: `4bec949b09d5178f205ce07a34fb5e2223b3d52fe492464aa4f661876b9b9aa4`
- package entries: `29`
- exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

The release workflow verified manifest version `0.5.3`, the exact three-Skill boundary, the Final PR-head freeze source, and the 29-file package before publishing the immutable tag/release. Release run `38332704281` completed successfully for frozen source `255bd32b1414a9555a7280d6e7562411ed3c7d96`.

## Final PR-head freeze baseline

`plugin-v0.5.3` publishes the accepted `EG-FINAL-PR-HEAD-FREEZE-052` corrective. The active source task refines that model by separating literal Repository HEAD from Delivery / Semantic HEAD for control-only changes. The published v0.5.3 release itself remains immutable and is not being republished by this task.

## ChatGPT Plugin state

Owned private ChatGPT Plugin `engineering-governance` is version `0.5.3`.

Its current release remains the published baseline; the active source corrective is not yet a released Plugin version.

## Local Codex installation state

Machine-local v0.5.3 authority reconciliation has been performed outside this repository workflow. This repository task does not rely on those machine-local receipts for reusable-source correctness and does not mutate installed Plugin caches.

## Active development state

Active authorized repository task: `EG-CONTROL-DELIVERY-IDENTITY-055`.

Task branch: `codex/control-delivery-identity-055`.

The reusable-source implementation candidate is:

`FROZEN_IMPLEMENTATION_HEAD = 5dcd7b4146da5d8f930ebd1ca04b8d9ee4703b0c`

This lock is a **Delivery / Semantic HEAD** lock, not a requirement that later control-only Repository HEAD must equal that SHA.

Implemented source now distinguishes:

- `Repository HEAD` from `Delivery / Semantic HEAD`;
- `CONTROL_ONLY_CHANGE` / `CONTROL_ONLY_DRIFT` from `DELIVERY_HEAD_CHANGE`;
- semantic-tree equivalence excluding exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
- authoritative task-content changes from implementation-identity changes;
- lazy/batched lifecycle reconciliation from immediate evidence writeback;
- closed workspace lifecycle from later control-only main advances.

Required RED baseline was demonstrated before source modification:

- Scenario A: post-audit control update could invalidate literal exact-head verification;
- Scenario B: workspace closeout lacked an explicit control-only-main non-reopen rule;
- Scenario C: next-task flow could force an intermediate lifecycle control transition;
- Scenario D: real implementation drift remains a required invalidation guard;
- Scenario E: material `CURRENT_TASK.md` content remains authoritative.

The design and implementation plan are retained under `docs/superpowers/specs/` and `docs/superpowers/plans/` for this source task.

## Current repository state

- Release task `EG-PLUGIN-V0.5.3-RELEASE-053`: **COMPLETE**.
- Published release blocker: **none**.
- Active source task: `EG-CONTROL-DELIVERY-IDENTITY-055`.
- Reusable-source construction: implementation candidate prepared.
- New Plugin release: **not authorized**.

## Next intended milestone

Finish cross-contract verification, prove that the control reconciliation after `5dcd7b4146da5d8f930ebd1ca04b8d9ee4703b0c` is `CONTROL_ONLY_DRIFT`, open a Draft PR, and stop for independent source audit. Do not create evidence-only control commits after that boundary.
