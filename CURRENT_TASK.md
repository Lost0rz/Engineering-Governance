# CURRENT TASK — Capability Architecture Hardening v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ARCHITECTURE-HARDENING-063`

Task class: `CORRECTIVE`

State: `COMPLETE`

Mode: remote reusable-source architecture hardening before consolidated installed Plugin/runtime acceptance

## Objective

Refine the frozen v0.6.0 seven-Skill architecture so task semantics, Sub Agent orchestration, model selection, cross-context handoff, and independent audit behavior match the intended operating model before integrated acceptance.

The goal is **not** to suppress Sub Agents or high-capability models. The goal is to use them deliberately and effectively: parallelize independent work when useful, select stronger models when judgment demand justifies them, keep execution authority explicit, and separate engineering task purpose from the Web/Local/agent context in which the work happens.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: Task 062 froze a complete architecture candidate; Task 063 completed bounded semantic hardening accepted after the seven-Skill audit.

## Accepted baseline

- Task start literal branch HEAD: `177c685e867747eb8346edcef31272e03df405ea`.
- Prior Task 062 Architecture Delivery / Semantic HEAD: `26fdc590b4c4ef1e25781f7065626fc87fc349cf`.
- Branch: `codex/capability-model-v0.6.0`.
- PR #26 remained OPEN / DRAFT / UNMERGED.
- Published/installed baseline remained Plugin `0.5.5`.
- Installed v0.6.0 integrated acceptance was not run.

## Completed work

### WP11 — Task purpose and lifecycle semantics

- Added optional `TASK_CLASS` guidance without creating a new control authority.
- Distinguished engineering task, Sub Agent execution unit, and execution context.
- Defined same-task continuation across Web/local/session/machine/Sub Agent contexts when objective/authorization is unchanged.
- Defined reconciliation/new-task boundaries for materially distinct engineering purposes such as independent acceptance audit or corrective work.
- Updated Project Governance task template, main Skill, development flow, capability composition, and control-plane semantics.

### WP12 — Positive orchestration and model selection

- Replaced minimum-agent bias with effective-safe-execution semantics.
- Added positive use of safe independent parallel Sub Agent capacity.
- Added `AVAILABLE_PARALLELISM`, dependency/write/integration state, cancellation and supersession semantics.
- Added environment `MODEL_TIER_MAP` for actual model + reasoning effort when material.
- Clarified that HIGH is allowed and should be selected deliberately when judgment demand justifies it.
- Allowed intentional escalation with explicit reason/boundary while continuing to prohibit silent/unreasoned inheritance/escalation.

### WP13 — Context-neutral handoff and independent audit

- Added same-task `TASK_ID` continuity across execution contexts.
- Added optional `SOURCE_CONTEXT`, `TARGET_CONTEXT`, and `AUTHORITY_OBSERVED_BASIS`.
- Added compatible/conflicting/unavailable authority handling instead of stale-intent execution.
- Clarified that Web/local are context labels, not reusable task-purpose definitions.
- Distinguished implementation self-check from independent acceptance.
- Added audit independence basis `SELF_CHECK | FRESH_CONTEXT | SEPARATE_AGENT | HUMAN`.
- Added required-claim coverage and explicit severity-to-boundary disposition semantics.

### WP14 — Acceptance and maintainer alignment

- Updated `references/V060_INTEGRATED_ACCEPTANCE.md` for task/context separation, positive parallelism, model mapping/HIGH/escalation, authority-basis handoff cases, independent audit, required claims, and severity/disposition.
- Updated root `AGENTS.md`, README, verification contract, Skill Engineering quality contract, and upstream conceptual references.
- Preserved the seven-Skill model and no-eighth-Skill rule.

## New architecture freeze

Frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`5ad4f4a4465714f571bce4b9d095d741cd361c03`

The earlier Task 062 semantic candidate `26fdc590b4c4ef1e25781f7065626fc87fc349cf` is historical/superseded for final v0.6.0 acceptance because reusable semantics changed under Task 063.

## Verification result

`V2 remote source-architecture audit: PASS`.

Evidence:

- compare from Task 063 start `177c685e...` to semantic head `5ad4f4a...` contains only governance/Skill Markdown and control files; no runtime/daemon/model-router/workflow implementation was added;
- exactly seven top-level Skill directories remain;
- Project Governance distinguishes task purpose, execution unit, and execution context;
- Orchestrator semantics positively use safe parallel capacity and intentionally allow HIGH model use;
- model tier mapping/escalation semantics remain provider-neutral;
- Handoff preserves same-task authority across contexts and handles authority drift explicitly;
- Evidence Audit now separates self-check from independent acceptance, required-claim coverage from verdict, and severity from boundary disposition;
- Integrated acceptance specification covers the hardened semantics;
- PR #26 is OPEN / DRAFT / UNMERGED / `mergeable=true` at audit time;
- semantic head has no reported commit/check statuses; CI PASS is not claimed.

## Acceptance criteria

All Task 063 source-hardening acceptance criteria are satisfied.

Installed Plugin/Web/Codex routing/runtime acceptance remains explicitly outside this task and has not been run. The accepted next sequence is one consolidated integrated acceptance task against semantic head `5ad4f4a4465714f571bce4b9d095d741cd361c03` (or a proven control-only descendant).

## Handoff / terminal state

Task 063 is complete. PR #26 remains Draft.

Next authorized work should be the consolidated v0.6.0 integrated acceptance task using `references/V060_INTEGRATED_ACCEPTANCE.md`. Reusable defects discovered during installed acceptance return to the remote source flow; do not patch reusable source inside installed Plugin caches.

Control Alignment Gate:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-hardening-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UNCHANGED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
