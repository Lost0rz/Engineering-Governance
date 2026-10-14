# CURRENT TASK — Project Profile & Transfer Contracts v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-PROFILE-HANDOFF-LIFECYCLE-068`

Task class: `CORRECTIVE`

State: `COMPLETE`

## Objective

Complete the reusable v0.6.0 source architecture before installed acceptance by adding a lightweight Project Profile capability, standardized handoff cards/receipts and compact engineering status receipts, and unified project-artifact refresh/lifecycle rules without creating a second control plane.

## Completed

- added `project-profile` as a derived context/index Skill with compact template and freshness contract;
- separated Profile vs normative `AGENTS.md` vs detailed Domain/navigation vs STATUS/TASK vs durable planning;
- standardized Handoff Card envelope, mode profiles and EXECUTE/AUDIT/REVIEW/VERIFY receipts;
- mapped normal test-run cards to VERIFY and state-changing test/probe work to EXECUTE;
- added compact human-facing Engineering Status Receipt guidance to Project Governance;
- added affected-owner artifact lifecycle and `NO_SEMANTIC_CHANGE -> NO_WRITE -> NO_COMMIT`;
- added continuation anti-churn and same-task PR/workspace reuse rules;
- reduced project AGENTS template duplication of reusable workflow;
- updated routing/adoption/design/acceptance contracts to the eight-Skill model.

## Architecture freeze

Frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`448661193faa24d6e5dd719ef3840ec40517bb1f`

## Verification

`V2 remote source-architecture audit: PASS`.

- exact eight top-level Skill directories;
- Plugin metadata remains `0.6.0`;
- Project Profile is non-authoritative and does not duplicate detailed Domain routing;
- Card/Receipt contracts preserve `CURRENT_TASK.md` authority and side-effect boundaries;
- artifact lifecycle updates only affected semantic owners;
- source changes are governance/Skill/design/acceptance Markdown/control only;
- no runtime/daemon/database/workflow/model-router/automatic enforcement added;
- PR #26 OPEN / DRAFT / UNMERGED and mergeable/clean at audit time;
- no commit/check status on semantic head, so CI PASS is not claimed.

## Terminal state

Task 068 is complete. Next milestone is the consolidated installed Plugin/Web/Codex acceptance against the frozen semantic identity (or a proven semantic-tree-equivalent control-only descendant).

Control Alignment:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-hardening-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UPDATED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
