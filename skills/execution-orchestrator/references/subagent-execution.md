# Sub Agent execution

## Purpose

Sub Agents exist to improve effective execution. They are not a maturity signal, mandatory ceremony, or a substitute for a clear plan.

The controller remains responsible for task authority, topology choice, integration and final verification.

## Value decision

Before spawning any delegated unit, answer:

```text
SUBAGENT_DECISION: USE | DO_NOT_USE
REASON:
```

Use Sub Agents when at least one material benefit exists and integration remains safe:

- independent investigation can run concurrently;
- a bounded unit can be context-isolated without repeated reconstruction;
- independent verification/review can run while preserving one implementation writer;
- proven-disjoint writer packages can safely execute concurrently;
- sequential delegation materially improves context/role focus despite no concurrency.

Do not use Sub Agents merely because:

- the task is described as large;
- multi-agent capability is enabled;
- a plan contains multiple numbered steps;
- a specialist role name sounds useful;
- the controller can already complete the bounded work faster than delegation/integration overhead.

## Roles

### EXPLORER

Read-only. Locate code, authority, symbols, tests, runtime paths, dependencies, prior implementations or failure evidence.

Good parallel candidate when questions are independent.

### WORKER

State-changing. Implement only inside an explicit unit writer boundary inherited from the active task.

Default to one WORKER for overlapping semantic state. Multiple WORKER units require proven-disjoint semantic authority/workspaces and an integration boundary.

### VERIFIER

Read-only. Run or inspect targeted tests, type/lint/build checks, runtime/browser checks, claim verification or acceptance evidence.

If the verifier must change tests/config/instrumentation, that becomes a separately bounded state-changing WORKER unit.

### REVIEWER

Read-only. Review diff, regressions, contracts, integration consistency and acceptance coverage.

`VERIFIER` asks primarily whether the implementation demonstrably works. `REVIEWER` asks whether the implementation is correct, bounded and consistent with the accepted objective.

## Dependency/topology rules

Prefer the smallest useful topology.

### INLINE

Use when one executor is clearly fastest/safest, dependencies are tight, or delegation overhead dominates.

### SEQUENTIAL_DELEGATED

Use when a bounded specialist result materially improves the next unit but units cannot safely proceed concurrently.

### PARALLEL_READ_ONLY

Preferred multi-agent pattern for independent exploration, review or verification.

### PARALLEL_DISJOINT_WRITERS

Use only when each writer has proven-disjoint semantic authority/workspace, interface assumptions are sufficiently stable, and controller integration/verification is defined before execution.

A recommended default for complex shared-state work is:

```text
parallel EXPLORER
→ controller synthesis
→ single WORKER
→ parallel VERIFIER / REVIEWER when useful
→ controller integration
```

## Planning linkage

If an accepted plan already exposes work packages, use them as candidate execution units. Do not assume every work package becomes a Sub Agent.

Useful planning fields are:

```text
WORK_PACKAGE
OBJECTIVE
DEPENDENCIES
WRITER_BOUNDARY
ACCEPTANCE
PARALLELIZABLE_WITH
```

Execution Orchestrator still performs the value gate using current repository/runtime facts.

## Unit contract

Each delegated unit carries only what it needs:

```text
TASK_ID
UNIT_ID
ROLE
OBJECTIVE
DEPENDENCIES
AUTHORITY_REFERENCES
READ_WRITE_BOUNDARY
RELEVANT_PATHS_SYMBOLS_TESTS
FRESH_DELTA
ACCEPTANCE
STOP_CONDITIONS
RETURN_CONTRACT
```

## Model and reasoning

Engineering Governance does not map roles to fixed model names.

The Local execution environment owns the resolution chain for parent inheritance, environment Sub Agent defaults, role/custom-agent overrides and actual runtime values.

Record configuration and runtime separately:

```text
MODEL_SOURCE
MODEL_CONFIG
REASONING_CONFIG
MODEL_EFFECTIVE
REASONING_EFFECTIVE
```

If effective runtime identity cannot be observed, say `UNKNOWN`. Do not promote configured values into observed values.

## Redelegation

Delegated units normally return to the controller.

Nested delegation is disabled by default. Permit it only when a flat topology is materially inefficient, the runtime supports it, the nested objective is bounded, writer authority remains safe and the controller retains an explicit integration path.

## Receipt evidence

When no Sub Agent is used:

```text
Execution topology: INLINE
Subagents: NO
```

When used:

```text
Execution topology: <topology>
Subagents: YES — <role/count summary>
Subagent runtime: <observable effective model/reasoning by role/unit, or UNKNOWN>
```

Configuration-only evidence must be labeled, for example:

```text
Subagent runtime: configured <value>; effective runtime identity UNKNOWN
```

The receipt exists for auditability; it must not encourage unnecessary delegation.
