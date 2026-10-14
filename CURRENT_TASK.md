# CURRENT TASK — Web Candidate Acceptance v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

Task class: `VERIFY`

State: `ACTIVE`

## Objective

Package the frozen v0.6.0 Semantic HEAD as an exact Web Plugin candidate, update the existing personal ChatGPT `engineering-governance` Plugin from 0.5.5 to 0.6.0, and run the Web-side discovery/routing portion of integrated acceptance before any formal GitHub release or PR merge.

## Resume basis

Packaging precheck exposed stale Agent Handoff request/receipt templates. Corrective task `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` is COMPLETE and aligned those shipped templates with the accepted Card/Receipt contract.

Current frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`d8bdf9da4094a0550d59afe33e02b179582150b2`

Task 071 changed only the two Agent Handoff templates plus control records needed for the corrective transition; the accepted eight-Skill architecture and routing semantics otherwise remain unchanged.

## Authority / identity

- Frozen source / Semantic HEAD: `d8bdf9da4094a0550d59afe33e02b179582150b2`.
- Current PR: #26, branch `codex/capability-model-v0.6.0`.
- Existing Web Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`, current installed version before update `0.5.5`.

## In scope

- build/verify an exact Plugin payload containing only `plugin.json` and `skills/**` from the frozen Semantic HEAD;
- update the existing Web personal Plugin to version `0.6.0` without changing audience/identity;
- verify installed release metadata and exact eight-Skill availability;
- run bounded Web routing/discovery checks from `references/V060_INTEGRATED_ACCEPTANCE.md` that are observable in this environment;
- record unresolved Web-only or cross-environment acceptance gaps explicitly.

## Out of scope

- formal immutable GitHub `plugin-v0.6.0` release/tag;
- PR #26 merge;
- Local Codex / Mac mini / MacBook Air installation or acceptance;
- installed-cache patching;
- source architecture changes unless a real reusable defect is found and separately authorized.

## Verification / acceptance

- package manifest version/name match `engineering-governance` `0.6.0`;
- package contains only `plugin.json` + `skills/**` and the exact eight top-level Skills;
- shipped Agent Handoff templates match the accepted Card/Receipt contract;
- Web Plugin update produces a new current release on the same Plugin identity;
- installed Web surface exposes the expected eight Skills and routing metadata;
- Web routing positive/negative scenarios are checked where the platform surface makes them observable;
- missing/unobservable platform behavior remains `UNKNOWN`, not `PASS`.

## STOP conditions

Stop before formal release/merge/local installation if package provenance differs from the frozen Semantic HEAD, Plugin identity changes unexpectedly, update would delete unknown existing Plugin files outside the intended payload, or Web installation/routing exposes another reusable source defect.

## Terminal boundary

This task may close after the Web candidate is installed and Web-side acceptance evidence is recorded. Formal GitHub release remains a later boundary after the required integrated acceptance decision.
