# Execution contract

## Trigger

Use orchestration when execution topology itself needs a decision: decomposition, roles/agents, parallelism, environment-aware delegation, recovery, cancellation/supersession, or controlled integration. Do not invoke it when one executor is clearly sufficient.

## Work units and roles

Delegated units stay inside the active `TASK_ID` unless they discover a materially different purpose/authorization need. Roles such as controller, implementer, scout, reviewer, and verifier do not grant permission by name; write authority remains explicit.

## Topology

Choose from dependency/authority/integration needs:

1. `INLINE`
2. `SEQUENTIAL_DELEGATED`
3. `PARALLEL_READ_ONLY`
4. `PARALLEL_DISJOINT_WRITERS`

Use parallel capacity when independence and coordination value justify it. Concurrent writers require proven-disjoint semantic authority/workspaces and a defined integration check.

When material, track only:

```text
ACTIVE_UNITS
DEPENDENCY_GRAPH
WRITE_AUTHORITY_PER_UNIT
INTEGRATION_BOUNDARY
```

Resolve `AVAILABLE_PARALLELISM` and other runtime-specific constraints from `environment-capabilities.md`; do not hardcode them in reusable policy.

## Delegated-model stabilization

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
MODEL_OVERRIDE: NONE
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

The receiving/current execution environment resolves its own authoritative Sub Agent default. Concrete provider/model/reasoning settings are environment facts. If not observable, keep them `PLATFORM_DEFAULT` / `UNKNOWN`. `LOW / STANDARD / HIGH` remain inactive future vocabulary only.

If the current default/capability is unavailable or insufficient, return the capability/environment gap; do not silently substitute a stronger model or another context's configuration.

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

Add environment capability information only when the unit actually needs it. Use Agent Handoff for cross-context transfer.

## Retry / cancellation / recovery

Retry only when another attempt has a reasonable chance to add evidence/value. Avoid unbounded replacement loops. Mark stale/unnecessary units `CANCELLED` or `SUPERSEDED` and do not integrate them without fresh validation.

Use an ephemeral recovery ledger only when restart/context-loss is realistic; it never replaces project controls.

## Integration

Controller integration verifies returned identity/paths/scope, rejects unknown/stale results, resolves conflicts centrally, runs affected verification, and returns material design/scope/environment gaps to the owning authority before further mutation.

A unit saying `PASS` does not establish integrated task PASS.
