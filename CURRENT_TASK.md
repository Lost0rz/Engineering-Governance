# CURRENT TASK — Local Execution / Sub Agent Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084`

Task class: `CAPABILITY_HARDENING`

State: `ACTIVE — SOURCE_READY_FOR_LOCAL_TRIAL`

## Objective

Harden Local Codex execution so Sub Agents are used only when they materially improve throughput, context isolation, or verification quality.

Sub Agent use is an execution optimization, not a goal. Planning exposes executable structure; `execution-orchestrator` decides at execution time whether delegation is worthwhile in the current environment.

## Required behavior

### Planning / execution boundary

Complex plans may expose bounded work packages with:

- objective;
- dependencies;
- writer boundary;
- acceptance;
- parallelizability when materially useful.

Planning must not freeze machine-specific parallel capacity, concrete model names, reasoning effort, or a mandatory Sub Agent topology.

### Sub Agent value gate

Before delegation, evaluate whether:

1. the work has genuinely independent units rather than artificial step splitting;
2. dependency structure permits useful concurrency or context isolation;
3. write boundaries are safe and explicit;
4. expected value exceeds coordination/integration cost;
5. the current Local Codex environment exposes enough capability for the selected topology.

Emit:

```text
SUBAGENT_DECISION: USE | DO_NOT_USE
REASON: <bounded execution rationale>
```

Small, tightly coupled, single-writer work should normally remain `INLINE`.

### Stable execution roles

Use the smallest useful role set:

- `EXPLORER` — read-only code/authority/test/runtime investigation;
- `WORKER` — authorized state-changing implementation inside an explicit writer boundary;
- `VERIFIER` — read-only targeted verification/runtime checks;
- `REVIEWER` — read-only diff/regression/acceptance review.

Default writer rule: one writer per overlapping semantic authority. Parallel writers require proven-disjoint authority/workspaces plus a defined integration boundary.

Sub Agent redelegation is disabled by default unless a concrete high-complexity execution need and runtime capability justify it.

### Model / reasoning boundary

Engineering Governance selects role/topology, not a fixed provider/model.

The receiving Local Codex environment owns concrete Sub Agent model/reasoning resolution. Runtime acceptance must distinguish configured defaults from observed effective runtime identity.

Internal evidence may use:

```text
MODEL_SOURCE: <parent inheritance | agents default | role/custom config | runtime/platform | UNKNOWN>
MODEL_CONFIG: <configured value | PLATFORM_DEFAULT | UNKNOWN>
MODEL_EFFECTIVE: <observed value | UNKNOWN>
REASONING_EFFECTIVE: <observed value | UNKNOWN>
```

Never report an effective model/reasoning value solely because configuration suggests it.

### Receipt observability

Governed execution and cross-context EXECUTE receipts report Sub Agent usage when execution occurred:

```text
Execution topology:
Subagents:
Subagent runtime:
```

If no Sub Agent was used, `Subagents: NO` is sufficient. If used, report bounded role/count and observable model/reasoning identity; unknown effective runtime values remain `UNKNOWN`.

## Local runtime acceptance

Before any release/Web synchronization claim for this task, test Local Codex runtime behavior on the target local environment, including where observable:

- no explicit Sub Agent override -> parent/default inheritance behavior;
- `[agents]` defaults -> delegated resolution;
- role/custom agent override -> precedence when used;
- useful parallel read-only delegation;
- overlapping writer prevention;
- disjoint writer case when safely testable;
- compact receipt with topology, Sub Agent use, and runtime identity evidence.

Repository policy alone does not establish runtime PASS.

## Source implementation result

Source hardening is complete enough for Local trial:

- `execution-orchestrator` now has an explicit Sub Agent value gate;
- execution roles are `EXPLORER / WORKER / VERIFIER / REVIEWER`;
- planning exposes candidate work-package/dependency/writer structure without selecting runtime topology;
- configured model/reasoning and observed effective runtime identity are separated;
- nested delegation is disabled by default;
- Project Governance compact receipts expose execution topology, Sub Agent use and runtime identity evidence;
- cross-context EXECUTE Handoff Receipts preserve the same execution evidence;
- `references/V072_LOCAL_EXECUTION_SUBAGENT_ACCEPTANCE.md` defines source and Local runtime acceptance;
- Plugin manifest on the candidate branch is `0.7.2`;
- v0.7.1 release workflow is archived and the v0.7.2 candidate workflow performs validation/build only, with no publication step.

Candidate validation:

- Draft PR: `#33 — feat: harden local execution and Sub Agent orchestration`;
- semantic candidate HEAD: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- workflow: `Validate Plugin v0.7.2 Candidate`;
- run: `38662974492`;
- result: `success`.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.

## Explicit boundaries

- do not create a new top-level Skill;
- do not make Engineering Governance a model router;
- do not hardcode one Local machine's model/capacity into reusable policy;
- do not force Sub Agent use for ordinary small tasks;
- do not update the private Web Plugin in this task phase;
- do not merge/release merely from source validation;
- do not claim Local runtime acceptance until a real local test/readback is performed.

## Next acceptance boundary

Run Task 084 against Local Codex using the exact candidate/source identity and capture:

1. installed/candidate identity;
2. local Sub Agent configuration source;
3. an `INLINE / Subagents: NO` negative case;
4. a useful delegated read-only case;
5. writer-safety behavior;
6. effective model/reasoning evidence where exposed, otherwise explicit `UNKNOWN`;
7. final receipt shape.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ROUTING-HARDENING-083` (`COMPLETE`)
- `START_MAIN_HEAD`: `0a2febb5cc294609d5ebfe54a4e84da1216de2dd`
- `TASK_BRANCH`: `codex/local-execution-subagent-hardening-v072`
- `PR`: `#33` (`DRAFT / UNMERGED`)
- `TARGET_VERSION`: `0.7.2-candidate`
- `SEMANTIC_CANDIDATE_HEAD`: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`
- `SOURCE_VALIDATION_RUN`: `38662974492`
- `SOURCE_VALIDATION`: `PASS`
- `WEB_PLUGIN_UPDATE`: `NOT_AUTHORIZED_THIS_PHASE`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`
- `TASK_STATE`: `ACTIVE — SOURCE_READY_FOR_LOCAL_TRIAL`
