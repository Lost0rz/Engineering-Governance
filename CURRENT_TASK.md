# CURRENT TASK — Web Candidate Acceptance v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

Task class: `VERIFY`

State: `WAITING_FRESH_WEB_SESSION`

## Objective

Package the frozen v0.6.0 Semantic HEAD as an exact Web Plugin candidate, update the existing personal ChatGPT `engineering-governance` Plugin from 0.5.5 to 0.6.0, and run the Web-side discovery/routing portion of integrated acceptance before any formal GitHub release or PR merge.

## Resume / corrective basis

Packaging precheck exposed stale Agent Handoff request/receipt templates. Corrective task `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` is COMPLETE and aligned those shipped templates with the accepted Card/Receipt contract.

Current frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`d8bdf9da4094a0550d59afe33e02b179582150b2`

## Web candidate evidence

- Source payload identity: frozen Semantic HEAD `d8bdf9da4094a0550d59afe33e02b179582150b2`.
- Exact overlay package: `plugin.json` + changed/new `skills/**` only; 33 entries.
- Overlay Git-blob equivalence: `33/33 PASS` against the frozen source.
- Candidate ZIP SHA-256: `18bb5d7e063524f015e77f8f66feb7df1ac761512819728a38c4c4f3c48cce9e`.
- Web Plugin identity preserved: `plugins_6acb0b9e8b748191a9b89fad47d89517`.
- Web Plugin updated: `0.5.5 -> 0.6.0`.
- Current Web Plugin release: `pluginrel_6acef4a99cac81919f1be1a44f965235`.
- Scope/discoverability unchanged: `USER / PRIVATE`.
- Stored Plugin file surface contains all eight expected Skill trees.
- Platform-managed `.codex-plugin/plugin.json` reports `engineering-governance` version `0.6.0` and `skills: ./skills`.
- Semantic HEAD to current repository control descendant is proven `CONTROL_ONLY_DRIFT`; Delivery identity remains the frozen Semantic HEAD above.

## Current Web routing observation

The Plugin backend/current release is 0.6.0, but this already-open Web conversation still exposes the pre-update three-Skill resource snapshot (`project-governance`, `domain-navigation`, `incident-doctor`) with old descriptions.

Classification:

`CURRENT_CONVERSATION_SKILL_REGISTRY: STALE_PRE_UPDATE_SNAPSHOT`

This does not establish a source/package defect. Web routing/discovery verdict for v0.6.0 remains `UNKNOWN` until a fresh Web conversation/session loads the current Plugin release.

## In scope remaining

- in a fresh Web conversation/session, verify v0.6.0 Plugin discovery exposes the expected eight Skills/current metadata;
- run bounded positive/negative Web routing scenarios from `references/V060_INTEGRATED_ACCEPTANCE.md`;
- record unresolved Web-only or cross-environment acceptance gaps explicitly.

## Out of scope

- formal immutable GitHub `plugin-v0.6.0` release/tag;
- PR #26 merge;
- Local Codex / Mac mini / MacBook Air installation or acceptance;
- installed-cache patching;
- source architecture changes unless a real reusable defect is found and separately authorized.

## STOP conditions

Stop before formal release/merge/local installation if a fresh Web session still cannot discover the 0.6.0 eight-Skill release, Plugin identity/provenance differs from the candidate, or Web routing exposes another reusable source defect.

## Terminal boundary

This task closes only after fresh-session Web discovery/routing evidence is recorded. Formal GitHub release remains a later boundary after required integrated acceptance supports publication.

Control Alignment:

- `RELATED_DOCUMENT`: `references/V060_INTEGRATED_ACCEPTANCE.md`
- `DOCUMENT_ALIGNMENT`: `UNCHANGED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
