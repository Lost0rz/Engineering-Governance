# Execution contract

## Trigger

Use orchestration when execution topology itself needs a decision: decomposition, roles/agents, parallelism, environment-aware delegation, recovery, cancellation/supersession, or controlled integration. Do not invoke it when one executor is clearly sufficient.

## Planning-to-execution boundary

Planning may provide executable structure such as work packages, dependencies, writer boundaries, acceptance and useful parallelizability. Treat that as input, not as a preselected runtime topology.

Do not freeze concrete model names, reasoning effort, machine-specific capacity, thread counts, or mandatory Sub Agent use into durable planning. Resolve those at execution time from the current environment.

## Work units and roles

Delegated units stay inside the active `TASK_ID` unless they discover a materially different purpose/authorization need.

Stable roles:

- `EXPLORER` — read-only investigation;
- `WORKER` — authorized mutation inside an explicit writer boundary;
- `VERIFIER` — read-only targeted verification;
- `REVIEWER` — read-only review/regression/acceptance analysis.

Role names do not grant permission. Write authority remains explicit.

## Sub Agent value gate

Before delegation, decide:

```text
SUBAGENT_DECISION: USE | DO_NOT_USE
REASON: <bounded rationale>
```

Evaluate:

1. **Unit independence** — are there real bounded units rather than artificial sequential fragments?
2. **Dependencies** — can units proceed usefully in parallel or with useful context isolation?
3. **Writer safety** — are read/write boundaries explicit and integrable?
4. **Net value** — is expected throughput/context/verification value greater than coordination cost?
5. **Environment capability** — is the selected topology supported by the current runtime?

If the answer is materially negative, use `INLINE`.

## Topology

Choose from dependency/authority/integration needs:

1. `INLINE`
2. `SEQUENTIAL_DELEGATED`
3. `PARALLEL_READ_ONLY`
4. `PARALLEL_DISJOINT_WRITERS`

Prefer read-only parallelism before multi-writer parallelism. Concurrent writers require proven-disjoint semantic authority/workspaces and a defined integration check.

A common high-value pattern is:

```text
parallel EXPLORER units
→ controller synthesis
→ one WORKER for overlapping semantic state
→ parallel VERIFIER / REVIEWER units when independent
→ controller integration
```

When material, track only:

```text
ACTIVE_UNITS
DEPENDENCY_GRAPH
WRITE_AUTHORITY_PER_UNIT
INTEGRATION_BOUNDARY
```

## Delegated-model policy

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
REUSABLE_GOVERNANCE_MODEL_ROUTING: DISABLED
```

The receiving/current execution environment owns concrete Sub Agent model/reasoning resolution. Governance may observe configuration/runtime evidence but does not choose provider/model names.

Distinguish:

```text
MODEL_SOURCE
MODEL_CONFIG
MODEL_EFFECTIVE
REASONING_EFFECTIVE
```

Configured/default values are not automatically proof of effective runtime identity. If the environment does not expose an effective value, keep it `UNKNOWN`.

## Delegation package

Keep briefs bounded:

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

Do not dump the full task/plan when authority references plus fresh delta are sufficient.

## Redelegation

`SUBAGENT_REDELEGATION: DISABLED_BY_DEFAULT`.

Nested delegation requires all of:

- material complexity that a flat topology cannot handle efficiently;
- explicit bounded nested objective;
- runtime support/capacity;
- preserved writer/authority boundaries;
- controller-visible integration path.

Otherwise delegated units return to the controller rather than spawning more units.

## Retry / cancellation / recovery

Retry only when another attempt has a reasonable chance to add evidence/value. Avoid unbounded replacement loops. Mark stale/unnecessary units `CANCELLED` or `SUPERSEDED` and do not integrate them without fresh validation.

Use an ephemeral recovery ledger only when restart/context-loss is realistic; it never replaces project controls.

## Integration

Controller integration verifies returned identity/paths/scope, rejects unknown/stale results, resolves conflicts centrally, runs affected integrated verification, and returns material design/scope/environment gaps to the owning authority before further mutation.

A unit saying `PASS` does not establish integrated task PASS.
