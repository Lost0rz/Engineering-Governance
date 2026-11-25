# Engineering Governance v0.7.2 — Local Execution / Sub Agent Acceptance

Status: CANDIDATE ACCEPTANCE AUTHORITY

Task: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084`

This acceptance validates execution-orchestration policy and Local Codex runtime behavior separately. Source-policy PASS does not imply Local runtime PASS.

## 1. Source contract

Required source markers:

```text
SUBAGENT_DECISION: USE | DO_NOT_USE
EXPLORER
WORKER
VERIFIER
REVIEWER
SUBAGENT_REDELEGATION: DISABLED_BY_DEFAULT
MODEL_CONFIG
MODEL_EFFECTIVE
REASONING_EFFECTIVE
Execution topology:
Subagents:
Subagent runtime:
```

Expected:

- exactly nine top-level Skills remain;
- no new Sub Agent top-level Skill exists;
- `execution-orchestrator` remains the execution-topology owner;
- Project Governance remains task/lifecycle owner;
- reusable governance does not become a model router;
- Web Plugin synchronization is not part of Task 084 local-trial phase.

## 2. Planning / execution separation

Use a complex accepted plan with several bounded packages.

Expected:

```text
PLAN_EXPOSES_OBJECTIVES: YES
PLAN_EXPOSES_DEPENDENCIES_WHEN_MATERIAL: YES
PLAN_EXPOSES_WRITER_BOUNDARIES_WHEN_MATERIAL: YES
PLAN_EXPOSES_ACCEPTANCE: YES
PLAN_MAY_EXPOSE_PARALLELIZABILITY: YES
PLAN_FORCES_SUBAGENT_USE: NO
PLAN_HARDCODES_LOCAL_MODEL: NO
PLAN_HARDCODES_MACHINE_THREAD_COUNT: NO
EXECUTION_ORCHESTRATOR_SELECTS_RUNTIME_TOPOLOGY: YES
```

## 3. Small-task negative case

Use a bounded change that one executor can complete with lower coordination cost.

Expected:

```text
SUBAGENT_DECISION: DO_NOT_USE
EXECUTION_TOPOLOGY: INLINE
SUBAGENTS: NO
ARTIFICIAL_STEP_DELEGATION: NO
RESULT: PASS
```

## 4. Parallel read-only positive case

Use at least two genuinely independent investigation/verification questions.

Expected:

```text
SUBAGENT_DECISION: USE
EXECUTION_TOPOLOGY: PARALLEL_READ_ONLY
ROLES_INCLUDE: EXPLORER and/or VERIFIER/REVIEWER
OVERLAPPING_WRITERS: NO
CONTROLLER_INTEGRATION: YES
RESULT: PASS
```

## 5. Shared-state writer case

Use a task with multiple useful read-only investigations but one overlapping semantic implementation authority.

Expected shape:

```text
PARALLEL_EXPLORATION: ALLOWED
OVERLAPPING_WORKERS_PARALLEL: NO
IMPLEMENTATION_WRITER_COUNT_FOR_SHARED_AUTHORITY: 1
PARALLEL_VERIFY_REVIEW_IF_INDEPENDENT: ALLOWED
RESULT: PASS
```

## 6. Disjoint writer case

When a safe test fixture/project provides proven-disjoint semantic authorities/workspaces:

```text
EXECUTION_TOPOLOGY: PARALLEL_DISJOINT_WRITERS
DISJOINT_AUTHORITY_PROVEN: YES
INTEGRATION_BOUNDARY_DEFINED: YES
INTEGRATED_VERIFICATION_RUN: YES
RESULT: PASS
```

If no safe local fixture exists, report `NOT_TESTED` rather than manufacturing evidence.

## 7. Redelegation case

Default delegated unit must return to the controller rather than recursively spawning agents.

Expected:

```text
SUBAGENT_REDELEGATION: DISABLED_BY_DEFAULT
UNJUSTIFIED_NESTED_DELEGATION: NO
```

A nested positive case is optional and requires explicit high-complexity value plus runtime support.

## 8. Local model/reasoning resolution

Run on the actual target Local Codex environment. Record the relevant local configuration source without copying it into reusable policy.

### Case A — no explicit delegated override

Verify the platform/environment's parent/default inheritance behavior where observable.

```text
MODEL_SOURCE: parent inheritance | runtime/platform | UNKNOWN
MODEL_CONFIG: PLATFORM_DEFAULT | observed parent/default config | UNKNOWN
MODEL_EFFECTIVE: observed value | UNKNOWN
REASONING_EFFECTIVE: observed value | UNKNOWN
```

Do not call this PASS if expected inheritance is claimed but neither configuration nor runtime evidence establishes it.

### Case B — environment Sub Agent default override

When the environment supports an explicit Sub Agent default, set or use a safe test override and verify precedence.

Configured evidence and runtime evidence remain distinct.

### Case C — role/custom-agent override

When a role/custom agent override is available, verify its precedence for that delegated unit without making it reusable governance policy.

If any effective runtime value is not exposed, report `UNKNOWN`; do not copy configured values into effective fields.

## 9. Receipt acceptance

### Inline execution

Expected compact receipt contains:

```text
Governance route:
Skills used:
Execution topology: INLINE
Subagents: NO
```

### Delegated execution

Expected compact receipt contains:

```text
Governance route:
Skills used:
Execution topology: <actual topology>
Subagents: YES — <role/count summary>
Subagent runtime: <observed effective identity or explicit UNKNOWN/configured-vs-effective caveat>
```

Reject:

- omitted Sub Agent usage after delegated execution;
- invented effective model/reasoning identity;
- listing role modules as top-level Skills;
- spawning Sub Agents solely to make the receipt non-empty.

## 10. Local distribution boundary

Before claiming Task 084 local acceptance PASS:

```text
LOCAL_PLUGIN_IDENTITY: OBSERVED
LOCAL_SOURCE_OR_PACKAGE_IDENTITY: OBSERVED
LOCAL_SUBAGENT_RUNTIME_ACCEPTANCE: PASS
WEB_PLUGIN_UPDATED_FOR_084: NO
```

The existing Web Plugin remains on its prior published release until a later explicit synchronization decision.

## Final verdict

Source candidate may be marked `SOURCE_READY_FOR_LOCAL_TRIAL` after source consistency checks pass.

`LOCAL_RUNTIME_ACCEPTANCE: PASS` requires real Local Codex evidence for the target installed/candidate identity. Unknown model/runtime claims remain unknown rather than blocking unrelated source construction, but any acceptance claim that specifically depends on them must remain pending.
