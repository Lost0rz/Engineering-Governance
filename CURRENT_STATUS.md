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

`plugin-v0.5.3` publishes the accepted `EG-FINAL-PR-HEAD-FREEZE-052` corrective. The active source task refines that model by separating literal Repository HEAD from Delivery / Semantic HEAD for control-only changes and by distinguishing semantic implementation evidence from live repository-host merge gates. The published v0.5.3 release itself remains immutable and is not being republished by this task.

## ChatGPT Plugin state

Owned private ChatGPT Plugin `engineering-governance` is version `0.5.3`.

Its current release remains the published baseline; the active source corrective is not yet a released Plugin version.

## Local Codex installation state

Machine-local v0.5.3 authority reconciliation has been performed outside this repository workflow. This repository task does not rely on those machine-local receipts for reusable-source correctness and does not mutate installed Plugin caches.

## Active development state

Active authorized repository task: `EG-CONTROL-DELIVERY-IDENTITY-055`.

Task branch: `codex/control-delivery-identity-055`.

The corrected reusable-source implementation candidate is:

`FROZEN_IMPLEMENTATION_HEAD = c8a9a4cc1ae99ca1e51f5422a8b2c1afa64c72e4`

This lock is a **Delivery / Semantic HEAD** lock, not a requirement that later control-only Repository HEAD must equal that SHA.

Implemented source now distinguishes:

- `Repository HEAD` from `Delivery / Semantic HEAD`;
- `CONTROL_ONLY_CHANGE` / `CONTROL_ONLY_DRIFT` from `DELIVERY_HEAD_CHANGE`;
- semantic-tree equivalence excluding exactly `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
- authoritative task-content changes from implementation-identity changes;
- semantic CI/test, code-review, and independent-audit evidence from repository-host gate state;
- required checks/reviews, mergeability/conflicts, merge queue, current-base/latest-head rules, and similar host gates as live literal constraints for the identity the repository host governs;
- lazy/batched lifecycle reconciliation from immediate evidence writeback;
- closed workspace lifecycle from later control-only main advances.

Required RED baseline was demonstrated before source modification:

- Scenario A: post-audit control update could invalidate literal exact-head verification;
- Scenario B: workspace closeout lacked an explicit control-only-main non-reopen rule;
- Scenario C: next-task flow could force an intermediate lifecycle control transition;
- Scenario D: real implementation drift remains a required invalidation guard;
- Scenario E: material `CURRENT_TASK.md` content remains authoritative.

The first independent audit identified one Important defect: the initial candidate treated repository-host merge/readiness gates too much like reusable semantic evidence. The bounded corrective now requires live host-gate evaluation and prohibits inferring `HOST_GATE_PASS` from semantic-tree equivalence alone.

The design and implementation plan are retained under `docs/superpowers/specs/` and `docs/superpowers/plans/` for this source task and have been reconciled to the corrected host-gate boundary.

## Current repository state

- Release task `EG-PLUGIN-V0.5.3-RELEASE-053`: **COMPLETE**.
- Published release blocker: **none**.
- Active source task: `EG-CONTROL-DELIVERY-IDENTITY-055`.
- Draft PR: `#18` — open, unmerged.
- Reusable-source corrective: complete at semantic candidate `c8a9a4cc1ae99ca1e51f5422a8b2c1afa64c72e4`.
- Independent re-audit: pending.
- New Plugin release: **not authorized**.

## Next intended milestone

Prove that Repository HEAD advances after `c8a9a4cc1ae99ca1e51f5422a8b2c1afa64c72e4` are control-only, re-audit the corrected contracts and current live repository-host gates, then decide whether PR #18 is safe to merge. Do not create evidence-only control commits after that boundary.
