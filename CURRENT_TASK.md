# CURRENT TASK — Project Profile & Transfer Contracts v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-PROFILE-HANDOFF-LIFECYCLE-068`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Objective

Complete the reusable v0.6.0 source architecture before installed acceptance by adding a lightweight Project Profile capability, standardizing handoff cards/receipts and compact engineering status receipts, and unifying project-artifact refresh/lifecycle rules without creating a second control plane.

## Superseded task

`EG-V060-INTEGRATED-ACCEPTANCE-067` is superseded before installed/runtime acceptance. Its Web readiness observation remains historical evidence only; no v0.6.0 runtime verdict was produced.

## In scope

- add one bounded top-level `project-profile` Skill for derived project context/index generation and refresh;
- distinguish Profile vs `AGENTS.md` vs Domain/navigation vs STATUS/TASK vs durable planning;
- standardize Handoff Card + Receipt envelopes and EXECUTE/AUDIT/VERIFY profiles, including test-run mapping;
- add compact Engineering Status Receipt guidance for governance responses;
- add lightweight artifact/authority lifecycle and affected-owner reconciliation rules;
- add explicit continuation anti-churn and same-task PR/workspace reuse rules;
- reduce project `AGENTS.md` template duplication of reusable workflow;
- update routing/composition/plugin docs/acceptance for the new capability.

## Out of scope

- installed Plugin/Web/Codex acceptance;
- runtime/daemon/database/model-router/automatic enforcement;
- project-specific Profile generation for InvestDesk/Gift/Merloom;
- release/merge of PR #26.

## Verification

- source/tree/frontmatter/reference consistency;
- exact intended top-level Skill set;
- no duplicate task/status/domain/planning authority introduced;
- no hardcoded environment-specific runtime values;
- read-only remote source audit on the final semantic candidate;
- PR remains Draft until later integrated acceptance.

## STOP

Stop if the new Profile would become a fourth control file, duplicate Domain Map authority, or if Card/Receipt templates redefine task authority instead of transporting it.
