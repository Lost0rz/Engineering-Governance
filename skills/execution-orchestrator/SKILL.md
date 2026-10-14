---
name: execution-orchestrator
description: Use when an already-authorized engineering task needs explicit decomposition, multiple execution roles/agents, parallel or sequential scheduling, delegated-model policy, resumable multi-step execution, or controlled integration of independent work.
---

# Execution Orchestrator

Use this Skill only after Project Governance has established valid task authority. It controls **how authorized work is executed**, not what work is authorized. Delegated units normally remain inside the same `TASK_ID`.

Read [Execution contract](references/execution-contract.md) when orchestration is needed.

## Default posture

Optimize for effective, safe execution rather than minimum agent count.

- Use one inline executor when decomposition provides no material benefit or dependencies/shared state make delegation inefficient.
- When independent work units can safely run concurrently, use available parallel Sub Agent capacity when it materially improves throughput or context isolation.
- Parallel scouts/researchers/reviewers/verifiers are encouraged when their questions/evidence domains are independent.
- Keep one writer for overlapping state/behavior authority.
- Multiple writers are allowed when semantic write scopes/workspaces are proven disjoint and integration evidence is defined.
- Do not dispatch agents only for ceremony; do not suppress useful agents only for conservatism.
- Review cadence follows risk/independence, not agent count.

## Core flow

1. Read the active task and accepted design/plan it links. Treat written accepted design as execution context; do not re-design unless new evidence creates a material unresolved decision.
2. Build only the work units and dependency edges that materially help execution.
3. Establish available parallel capacity when relevant and choose topology: inline, sequential delegated, parallel read-only, or proven-disjoint parallel writers.
4. Assign each delegated unit an explicit role, objective, dependency/write boundary, context package, and acceptance contract.
5. Apply the active delegated-model policy. During the current v0.6.0 stabilization period this is `ENVIRONMENT_DEFAULT_ONLY`: the current execution environment resolves and applies its own authoritative Sub Agent configuration/runtime default. Do not set a concrete model or reasoning value in reusable governance.
6. Use `agent-handoff` whenever responsibility crosses an agent/session/machine/context boundary, preserving the same task authority for same-purpose continuation. Do not transfer concrete Sub Agent model/reasoning settings across contexts.
7. Cancel or supersede outstanding units whose premise becomes stale or unnecessary; do not integrate stale results blindly.
8. Integrate returned work under the original task/writer authority; an agent success message is not repository/evidence confirmation.
9. Use an ephemeral recovery ledger only when resume/compaction risk makes it useful.
10. Return topology, delegated-model policy, unit state, integration evidence, unresolved conflicts and resume state to Project Governance.

## Delegated-model stabilization policy

Current v0.6.0 policy:

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
SUBAGENT_MODEL_SOURCE: current execution environment authoritative Sub Agent configuration/runtime default
MODEL_OVERRIDE: NONE
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

The current execution environment owns concrete Sub Agent model/reasoning configuration. A local runtime may expose an explicit local configuration; a Web/cloud runtime may manage its default internally. Reusable governance does not copy either environment's concrete values into repository source or another execution context.

If the environment exposes the concrete default, it may be observed for acceptance evidence. If it does not expose the concrete identity, keep it `PLATFORM_DEFAULT` / `UNKNOWN` rather than inferring a value or importing one from another machine/context.

`LOW / STANDARD / HIGH` may remain as future capability vocabulary, but they do **not** drive delegated Sub Agent routing while `ENVIRONMENT_DEFAULT_ONLY` is active. Re-enabling tier-based or stronger-model selection requires a later explicit user/project policy change.

## Hard rules

- **Use only the current environment's authoritative Sub Agent default during stabilization.** Do not override a delegated unit onto another model merely because its role looks easier or harder.
- **No cross-context model propagation.** A Web/local/cloud/other handoff may carry this policy, but must not carry a concrete Sub Agent model or reasoning setting as the receiver's default.
- **No guessing unobservable defaults.** If the current environment does not expose exact model/reasoning identity, leave it `PLATFORM_DEFAULT` / `UNKNOWN` and do not infer from repository text, memory, another machine, or controller settings.
- **No stronger-model escalation during stabilization.** Do not automatically or intentionally move a Sub Agent to a stronger model until a later explicit policy authorizes that behavior.
- **Model identity and reasoning configuration are separate evidence fields.** Neither should be inferred from the other.
- **No authority by delegation.** A Sub Agent brief cannot expand scope beyond `CURRENT_TASK.md`.
- **No context dumping by default.** Send bounded authority references, relevant files/tests and fresh delta rather than full chat/control copies.
- **No overlapping concurrent writers without proof.** Branch/worktree separation alone does not prove semantic independence.
- **No blind trust in returned success.** Integration uses actual repository/evidence state.
- **No stale-unit integration.** Cancelled/superseded results require fresh re-authorization/revalidation before use.

## Output contract

Report when material:

- `TASK_ID` and topology;
- `AVAILABLE_PARALLELISM`, dependency/work-unit boundaries and active/cancelled/superseded units;
- role/write authority per unit;
- `SUBAGENT_MODEL_POLICY` and the current environment's model-source observation (`authoritative config/runtime default | PLATFORM_DEFAULT | UNKNOWN`) when evidence requires it;
- completed/failed/skipped work units;
- integration and verification evidence;
- unresolved conflicts/rulings;
- recovery ledger/resume point when incomplete.
