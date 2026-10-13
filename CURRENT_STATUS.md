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

`plugin-v0.5.3` publishes the accepted `EG-FINAL-PR-HEAD-FREEZE-052` corrective:

- finish intended source/control edits before designating the final PR head;
- freeze that head for exact-head CI, review, independent audit, mergeability, and repository-host evidence;
- treat those results as live external evidence for the immutable identity;
- do not create source/control commits solely to record external evidence state;
- if evidence requires a real correction, unfreeze and restart exact-head verification on the corrected head;
- if evidence passes, merge the same frozen head;
- post-merge verification must not create another evidence-only commit loop.

This baseline is now under an authorized follow-up task that will refine the distinction between literal Repository HEAD and Delivery / Semantic HEAD for control-only changes. The published v0.5.3 release itself remains immutable.

## ChatGPT Plugin state

Owned private ChatGPT Plugin `engineering-governance` is version `0.5.3`.

Its current release retains the accepted Final PR-head freeze source. The Plugin identity and audience were preserved during the version update.

## Local Codex installation state

Machine-local v0.5.3 authority reconciliation has been performed outside this repository workflow. This repository task does not rely on those machine-local receipts for reusable-source correctness and does not mutate installed Plugin caches.

## Active development state

Active authorized repository task: `EG-CONTROL-DELIVERY-IDENTITY-055`.

Objective: globally separate control-record changes in `CURRENT_STATUS.md` / `CURRENT_TASK.md` from implementation/delivery identity, while preserving those files as authoritative controls for their owned semantics.

Verified task-start repository baseline before authorization transition: `4f3d5308aa742014cfbb8a72adcdb18d5d7c147d`.

The current source audit has already identified a material semantic conflict: the existing final-head freeze text still treats post-freeze status/task/documentation commits as changing the identity under exact-head verification. The new task must reconcile this with the requested Delivery / Semantic HEAD model before any release.

## Current repository state

- Release task `EG-PLUGIN-V0.5.3-RELEASE-053`: **COMPLETE**.
- Published release blocker: **none**.
- Active source task: `EG-CONTROL-DELIVERY-IDENTITY-055`.
- No new Plugin release is authorized by the active task.

## Next intended milestone

Create the dedicated task branch, capture the supplied design and implementation plan, demonstrate the required RED scenarios against the current contracts, then update only the existing Project Governance rules/templates needed to make the five scenarios consistent.
