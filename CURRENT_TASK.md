# CURRENT TASK — Model Policy Stabilization v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-MODEL-POLICY-STABILIZATION-064`

Task class: `CORRECTIVE`

State: `COMPLETE`

Mode: remote reusable-source model-policy correction before consolidated installed Plugin/runtime acceptance

## Objective

Stabilize v0.6.0 delegated Sub Agent model behavior without suppressing useful Sub Agent parallelism.

Delegated Sub Agents use the execution environment's configured default Sub Agent model and default reasoning setting. Stronger-model routing is disabled until a later explicit user/project policy re-enables it.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: completed narrow correction of Task 063 model-selection semantics; seven-Skill architecture and positive Sub Agent parallelism remain unchanged.

## Accepted baseline

- Task start literal branch HEAD: `f5c998ab72b6a27577a66cc87beb7a4be6570f37`.
- Prior Task 063 Architecture Delivery / Semantic HEAD: `5ad4f4a4465714f571bce4b9d095d741cd361c03`.
- Branch: `codex/capability-model-v0.6.0`.
- PR #26 remained OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance was not run.

## Completed operating policy

```text
SUBAGENT_MODEL_POLICY: DEFAULT_ONLY
SUBAGENT_MODEL: environment configured default
SUBAGENT_REASONING: environment configured default
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

1. Sub Agents remain a throughput/context-isolation capability and safe useful parallelism remains encouraged.
2. All delegated Sub Agents use the environment-configured default Sub Agent model and reasoning setting during stabilization.
3. Current user Codex convention may configure `gpt-6-luna` with `xhigh` reasoning effort; reusable governance keeps this environment-specific rather than hardcoding one universal provider/model.
4. Model identity and reasoning effort are separate; `xhigh` reasoning is not a HIGH-model selection.
5. No automatic or intentional delegated stronger-model escalation is allowed during stabilization.
6. `LOW / STANDARD / HIGH` remain inactive future capability vocabulary only and do not drive current delegated routing.
7. Re-enabling stronger-model/tier routing requires a later explicit user/project decision and governance update.

## Completed work

- Updated `skills/execution-orchestrator/SKILL.md` and `references/execution-contract.md` to `DEFAULT_ONLY`.
- Updated root `AGENTS.md` and README model-policy semantics.
- Updated global routing/development-flow wording so routing remains provider/model neutral and uses delegated-model-policy language rather than active tier routing.
- Updated `references/SKILL_ENGINEERING.md` so intentional stronger-model non-use during stabilization is not treated as under-use while useful safe Sub Agent parallelism remains positively encouraged.
- Updated `references/V060_INTEGRATED_ACCEPTANCE.md` to test environment-default continuity, reasoning/model separation, no stronger-model inheritance/escalation, and positive parallelism.
- Updated both v0.6.0 durable design authorities so Task 062/063 active HIGH-selection semantics are superseded by Task 064 stabilization.

## Architecture freeze

New v0.6.0 Architecture Delivery / Semantic HEAD:

`31d9d94f1f59a3d5b49fb7c614f37ec752cff479`

The prior Task 063 semantic candidate `5ad4f4a4465714f571bce4b9d095d741cd361c03` is historical/superseded for final v0.6.0 acceptance.

## Verification result

`V2 remote source-architecture corrective audit: PASS`.

Evidence:

- Task 064 start-to-semantic-head diff contains only governance/Skill/design/acceptance Markdown/control paths;
- no release workflow/runtime/daemon/database/model-router implementation was added;
- exactly seven top-level Skills remain;
- Plugin metadata remains `0.6.0`;
- active delegated-model policy is `DEFAULT_ONLY`;
- no active reusable rule requires or permits delegated stronger-model escalation during stabilization;
- `xhigh` reasoning is explicitly not a stronger-model tier selection;
- positive safe Sub Agent parallelism remains intact;
- integrated acceptance specification has matching default-model/no-escalation scenarios;
- PR #26 observed OPEN / DRAFT / UNMERGED / `mergeable=true`;
- semantic head has no reported commit/check statuses; CI PASS is not claimed.

## Acceptance criteria

All Task 064 criteria are satisfied.

Installed Plugin/Web/Codex acceptance is explicitly not part of Task 064 and has not been run.

## Handoff / terminal state

Task 064 is complete. PR #26 remains Draft.

Next authorized milestone is one consolidated v0.6.0 integrated acceptance task against semantic head `31d9d94f1f59a3d5b49fb7c614f37ec752cff479` or a proven control-only descendant, using `references/V060_INTEGRATED_ACCEPTANCE.md`.

Do not split acceptance one Skill at a time. Do not patch reusable source inside local installed Plugin acceptance; reusable-source defects return to the remote source flow.

Control Alignment Gate:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-hardening-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UPDATED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
