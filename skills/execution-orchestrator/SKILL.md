---
name: execution-orchestrator
description: Use when an already-authorized engineering task materially benefits from decomposition, multiple roles/agents, parallel or sequential scheduling, environment-aware delegation, resumable execution, cancellation, or controlled integration.
---

# Execution Orchestrator

Use only after valid task authority exists. This Skill controls **how authorized work executes**, not what is authorized. Delegated units normally remain inside the same `TASK_ID`.

Read `references/execution-contract.md`. When execution depends on runtime-specific limits/defaults/tools, also read `references/environment-capabilities.md`.

## Default posture

Optimize for effective safe execution, not minimum agent count.

- Inline when decomposition adds little value or shared/dependent state dominates.
- Use safe parallel Sub Agent capacity when independent units materially improve throughput/context isolation.
- Parallel readers/researchers/reviewers/verifiers are encouraged when independent.
- Keep one writer for overlapping semantic authority; parallel writers require proven-disjoint authority/workspaces plus integration evidence.
- Cancel/supersede stale units rather than integrating them blindly.

## Core flow

1. Read the active task and accepted design/plan it references.
2. Build only useful work units/dependencies.
3. Resolve only the environment capabilities material to this topology (for example parallel capacity, delegation limits, current Sub Agent default, material tool/workspace/runtime constraints).
4. Choose inline, sequential delegated, parallel read-only, or proven-disjoint parallel writers.
5. Give each unit a bounded role/objective/dependency/write boundary/context/acceptance contract.
6. Apply `ENVIRONMENT_DEFAULT_ONLY` for delegated models: the receiving execution environment resolves its own authoritative default; reusable governance does not set concrete model/reasoning values.
7. Use Agent Handoff across execution contexts; do not propagate sender runtime defaults as receiver defaults.
8. Integrate against actual repository/evidence state, not agent success text.
9. Use an ephemeral recovery ledger only when restart/context-loss risk makes it useful.
10. Return topology, material environment-capability observations, unit/integration state, verification evidence, and unresolved gaps to Project Governance.

## Hard rules

- No authority by delegation.
- No blind model/tool/runtime value inference from another context.
- No stronger-model escalation during current stabilization.
- No overlapping concurrent writers without proof.
- No full-context dumping by default.
- No stale/cancelled result integration without revalidation.

## Output contract

Report only what is material: task/topology, active units/dependencies, writer boundaries, environment capability source/unknowns, model policy, integration/verification evidence, unresolved gaps, and resume point if incomplete.
