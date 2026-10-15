---
name: execution-orchestrator
description: Use when an already-authorized engineering task materially benefits from decomposition, multiple roles/agents, parallel or sequential scheduling, environment-aware delegation, resumable execution, cancellation, or controlled integration.
---

# Execution Orchestrator

Use only after valid task authority exists. This Skill controls **how authorized work executes**, not what is authorized. Delegated units normally remain inside the same `TASK_ID`.

Read `references/execution-contract.md`. When Sub Agent delegation is considered, also read `references/subagent-execution.md`. When execution depends on runtime-specific limits/defaults/tools, read `references/environment-capabilities.md`.

## Default posture

Optimize for effective safe execution, not agent count.

**Sub Agents are an efficiency mechanism, not a completion requirement.** Use them only when decomposition, concurrency, context isolation, specialized read-only work, or independent verification creates material value beyond the coordination/integration cost.

- Keep small, tightly coupled, single-writer work `INLINE`.
- Prefer parallel read-only exploration/review/verification when units are genuinely independent.
- Keep one writer for overlapping semantic authority.
- Use parallel writers only when semantic authority/workspaces are proven disjoint and integration evidence is defined.
- Do not split one sequential thought process into artificial Sub Agent steps.
- Cancel/supersede stale units rather than integrating them blindly.

## Sub Agent value gate

Before spawning delegated units, record the execution decision:

```text
SUBAGENT_DECISION: USE | DO_NOT_USE
REASON: <why delegation improves or does not improve this execution>
```

Use `USE` only when all material conditions are satisfied:

1. useful bounded units exist;
2. dependency structure permits useful delegation/concurrency or context isolation;
3. read/write boundaries are explicit enough to integrate safely;
4. expected execution value exceeds coordination/integration cost;
5. the current environment exposes enough capability for the selected topology.

A large task is not automatically a multi-agent task; a small task is not automatically inline if a bounded independent investigation materially helps.

## Stable execution roles

Use the smallest role set that matches the work:

- `EXPLORER` — read-only code/authority/test/runtime investigation;
- `WORKER` — authorized state-changing implementation inside an explicit writer boundary;
- `VERIFIER` — read-only targeted checks/runtime verification;
- `REVIEWER` — read-only diff/regression/acceptance review.

Role names never grant authority. `WORKER` write scope comes from the active task plus its explicit unit boundary.

Sub Agent redelegation is disabled by default. A delegated unit may not create another delegation layer merely for convenience; nested delegation requires a concrete high-complexity execution need plus observable runtime support and must preserve the same authority/writer rules.

## Core flow

1. Read the active task and the bounded accepted plan/design it references.
2. Recover useful work-package/dependency structure when already available; do not re-plan resolved semantics merely to create agents.
3. Build only useful execution units and identify dependencies/write boundaries.
4. Run the Sub Agent value gate.
5. If delegation is not worthwhile, execute `INLINE`.
6. If delegation is worthwhile, resolve only environment capabilities material to the topology, including observable Sub Agent defaults/overrides, parallel capacity, delegation limits, tools, workspace/runtime constraints.
7. Choose `SEQUENTIAL_DELEGATED`, `PARALLEL_READ_ONLY`, or proven-disjoint `PARALLEL_DISJOINT_WRITERS` as appropriate.
8. Give each unit a bounded role/objective/dependency/read-write boundary/context/acceptance/return contract.
9. Apply `ENVIRONMENT_DEFAULT_ONLY`: the receiving execution environment resolves concrete model/reasoning values; reusable governance does not set provider/model names.
10. Use Agent Handoff when responsibility actually crosses execution contexts; do not propagate sender runtime defaults as receiver defaults.
11. Integrate against actual repository/evidence state, not agent success text.
12. Run proportional integrated verification and return topology/runtime/unit/integration evidence to Project Governance.

## Model/runtime observability

Distinguish configuration from effective runtime identity:

```text
MODEL_SOURCE: <parent inheritance | agents default | role/custom config | runtime/platform | UNKNOWN>
MODEL_CONFIG: <configured value | PLATFORM_DEFAULT | UNKNOWN>
MODEL_EFFECTIVE: <observed runtime value | UNKNOWN>
REASONING_EFFECTIVE: <observed runtime value | UNKNOWN>
```

Never report a configured model/reasoning value as effective runtime evidence unless the current environment actually exposes or otherwise verifies it.

## Hard rules

- No authority by delegation.
- No Sub Agent use solely because capability exists.
- No blind model/tool/runtime inference from another context.
- No stronger-model escalation by reusable governance.
- No overlapping concurrent writers without proof.
- No full-context dumping by default.
- No stale/cancelled result integration without revalidation.
- No recursive Sub Agent trees by default.

## Output contract

Report only material execution evidence:

```text
EXECUTION_TOPOLOGY:
SUBAGENT_DECISION:
SUBAGENT_UNITS: <NO | role/count + bounded unit state>
SUBAGENT_RUNTIME: <observable model/reasoning evidence | UNKNOWN | N/A>
WRITER_BOUNDARIES:
INTEGRATION_VERIFICATION:
UNRESOLVED:
RESUME_POINT:
```

Project Governance converts this into the compact user-facing receipt without inventing unobserved runtime identity.
