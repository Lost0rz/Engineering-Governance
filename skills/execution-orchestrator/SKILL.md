---
name: execution-orchestrator
description: Use when an already-authorized engineering task needs explicit decomposition, multiple execution roles/agents, parallel or sequential scheduling, model-tier selection, resumable multi-step execution, or controlled integration of independent work.
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
4. Assign each delegated unit an explicit role, objective, dependency/write boundary, context package, and model capability requirement.
5. Select the actual model/reasoning setting deliberately when model choice materially affects cost or correctness. `LOW / STANDARD / HIGH` are portable tiers; environment mapping supplies concrete model + reasoning effort.
6. Use `agent-handoff` whenever responsibility crosses an agent/session/machine/context boundary, preserving the same task authority for same-purpose continuation.
7. Cancel or supersede outstanding units whose premise becomes stale or unnecessary; do not integrate stale results blindly.
8. Integrate returned work under the original task/writer authority; an agent success message is not repository/evidence confirmation.
9. Use an ephemeral recovery ledger only when resume/compaction risk makes it useful.
10. Return topology, actual model policy, unit state, integration evidence, unresolved conflicts and resume state to Project Governance.

## Model principle

**Use the strongest justified model, not automatically the strongest available model.**

HIGH capability is allowed and should be chosen deliberately when architecture, difficult diagnosis, subtle integration/concurrency/security reasoning, or high-consequence review justifies it. What is prohibited is silent/unreasoned inheritance or escalation.

## Hard rules

- **No silent model selection.** When model choice is material, a delegated role must not silently inherit a controller/session model or silently move to a materially different capability tier.
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
- capability tier plus actual model/reasoning mapping and intentional escalation/fallback actually used;
- completed/failed/skipped work units;
- integration and verification evidence;
- unresolved conflicts/rulings;
- recovery ledger/resume point when incomplete.
