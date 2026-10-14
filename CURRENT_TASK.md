# CURRENT TASK — Model Policy Stabilization v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-MODEL-POLICY-STABILIZATION-064`

Task class: `CORRECTIVE`

State: `ACTIVE`

Mode: remote reusable-source model-policy correction before consolidated installed Plugin/runtime acceptance

## Objective

Correct the v0.6.0 Execution Orchestrator model policy so Sub Agents remain actively usable for safe parallel work while delegated model selection stays stable during an initial operating period.

During this stabilization period, delegated Sub Agents use the execution environment's configured default Sub Agent model and default reasoning setting. Do not select or escalate a Sub Agent to a stronger model than that configured default. Stronger-model routing can be reconsidered later only through an explicit user/project policy change.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: narrow correction of Task 063 model-selection semantics; seven-Skill architecture and positive Sub Agent parallelism remain unchanged.

## Accepted baseline

- Task start literal branch HEAD: `f5c998ab72b6a27577a66cc87beb7a4be6570f37`.
- Prior hardened Architecture Delivery / Semantic HEAD: `5ad4f4a4465714f571bce4b9d095d741cd361c03`.
- Branch: `codex/capability-model-v0.6.0`.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance has not run.

## User-decided operating policy

1. Sub Agents are still a throughput/context-isolation capability and should be used when independent parallel work is useful.
2. Sub Agents use the environment's configured default Sub Agent model and default reasoning setting during stabilization.
3. Current user Codex convention: default Sub Agent model `gpt-6-luna`, reasoning effort `xhigh`; this is environment configuration, not universal reusable source truth.
4. `xhigh` is a reasoning-effort setting and must not be conflated with selecting a higher model tier.
5. No delegated stronger-model escalation is permitted during stabilization, whether automatic or agent-initiated.
6. Existing `LOW / STANDARD / HIGH` abstractions may remain as future design vocabulary but must not drive active v0.6.0 delegated model routing while `DEFAULT_ONLY` stabilization is in force.
7. Re-enabling stronger model selection requires a later explicit user/project decision.

## In scope

- Update `execution-orchestrator` Skill and execution contract to `DEFAULT_ONLY` delegated model policy.
- Remove/override current wording that encourages intentional HIGH selection during the stabilization period.
- Update repository/global guidance and integrated acceptance scenarios so they test default-model use and prohibited stronger-model escalation.
- Update the v0.6.0 hardening design record where needed for semantic consistency.
- Run bounded remote source audit and freeze the corrected semantic candidate.

## Out of scope

- Changing current user Codex runtime configuration from its configured default.
- Selecting a different model/provider.
- Building a model router executable.
- Changing positive Sub Agent parallelism, task/context semantics, handoff, evidence-audit, Domain Navigation or Incident Doctor architecture.
- Installed Plugin/Web/Codex integrated acceptance.
- PR merge or v0.6.0 release.

## Verification

`V2` source-architecture corrective.

Verify:

- no active reusable rule instructs Sub Agents to choose/escalate to HIGH during stabilization;
- delegated work uses environment default model/reasoning semantics;
- `xhigh` reasoning is not represented as a stronger model tier;
- positive safe parallelism remains intact;
- integrated acceptance has a default-model scenario and a no-stronger-model-escalation scenario;
- seven top-level Skills remain unchanged;
- no runtime/model-router/workflow implementation is added.

## Acceptance criteria

- Task 063 HIGH-selection semantics are superseded by explicit `DEFAULT_ONLY` stabilization policy.
- Sub Agent orchestration remains positively usable and parallel where safe.
- Model policy is environment-default based and provider-neutral in reusable source.
- Stronger model selection is marked deferred until explicit future re-authorization.
- Remote source audit passes and a new semantic head is frozen.

## Stop conditions

Stop if the correction would require changing the user's actual runtime configuration, introducing a model-router runtime, or materially redesigning another Skill.
