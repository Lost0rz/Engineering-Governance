# CURRENT TASK — Handoff Template Contract Corrective v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071`

Task class: `CORRECTIVE`

State: `ACTIVE`

## Trigger

Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` stopped during exact Plugin packaging because the shipped Agent Handoff request/receipt templates were verified stale relative to the accepted `CAPABILITY` + `MODE` Card/Receipt contract.

## Objective

Correct only the stale Agent Handoff templates so the packaged Plugin exposes one consistent transfer schema, then re-freeze the v0.6.0 Semantic HEAD and return to Task 070 Web candidate installation/acceptance.

## In scope

- `skills/agent-handoff/assets/templates/HANDOFF_REQUEST.md`;
- `skills/agent-handoff/assets/templates/HANDOFF_RECEIPT.md`;
- bounded consistency verification against `skills/agent-handoff/SKILL.md` and `references/handoff-contract.md`;
- control/design alignment only if owned semantics change.

## Out of scope

- new Skills or control files;
- changes to routing/authority semantics beyond aligning the stale templates;
- Web Plugin update before the corrected source is frozen;
- formal GitHub release or PR merge.

## Required correction

- replace old `HANDOFF_ID` transport identity with `CARD_ID`;
- include required `CAPABILITY` and preserve `MODE` as the independent side-effect/action dimension;
- make request template match the required Card core and conditional fields;
- make receipt template start with the standard Receipt core and use mode-specific evidence without becoming task authority.

## Verification / acceptance

- both templates match the accepted Handoff contract;
- no old template wording can cause `MODE` to replace Skill routing;
- no mutation authority is created by a Card/Receipt;
- package-facing Agent Handoff assets are internally consistent.

## STOP conditions

Stop and report if template correction exposes a broader contract defect outside this bounded scope.
