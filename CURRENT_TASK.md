# CURRENT TASK — Web Candidate Acceptance v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070`

Task class: `VERIFY`

State: `ACTIVE`

## Objective

Package the frozen v0.6.0 Semantic HEAD as an exact Web Plugin candidate, update the existing personal ChatGPT `engineering-governance` Plugin from 0.5.5 to 0.6.0, and run the Web-side discovery/routing portion of integrated acceptance before any formal GitHub release or PR merge.

## Authority / identity

- Frozen source / Semantic HEAD: `7be11aae70c42b075034eb4613a7dc66b242bb80`.
- Current PR: #26, branch `codex/capability-model-v0.6.0`.
- Existing Web Plugin identity: `plugins_6acb0b9e8b748191a9b89fad47d89517`, current version `0.5.5`.

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
- Web Plugin update produces a new current release on the same Plugin identity;
- installed Web surface exposes the expected eight Skills and routing metadata;
- Web routing positive/negative scenarios are checked where the platform surface makes them observable;
- missing/unobservable platform behavior remains `UNKNOWN`, not `PASS`.

## STOP conditions

Stop before formal release/merge/local installation if package provenance differs from the frozen Semantic HEAD, Plugin identity changes unexpectedly, update would delete unknown existing Plugin files outside the intended payload, or Web installation/routing exposes a reusable source defect.

## Terminal boundary

This task may close after the Web candidate is installed and Web-side acceptance evidence is recorded. Formal GitHub release remains a later boundary after the required integrated acceptance decision.
