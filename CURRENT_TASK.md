# CURRENT TASK — Local Execution / Sub Agent Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084`

Task class: `CAPABILITY_HARDENING`

State: `ACTIVE — MERGED_TO_MAIN_FOR_LOCAL_TRIAL`

## Objective

Harden Local Codex execution so Sub Agents are used only when they materially improve throughput, context isolation, or verification quality.

Sub Agent use is an execution optimization, not a goal. Planning exposes executable structure; `execution-orchestrator` decides at execution time whether delegation is worthwhile in the current environment.

## Required behavior

### Planning / execution boundary

Complex plans may expose bounded work packages with objective, dependencies, writer boundary, acceptance, and parallelizability when materially useful. Planning must not freeze machine-specific parallel capacity, concrete model names, reasoning effort, or a mandatory Sub Agent topology.

### Sub Agent value gate

Before delegation, evaluate whether the work has genuinely independent units, dependency structure permits useful concurrency/context isolation, write boundaries are safe, expected value exceeds coordination cost, and the current Local Codex environment exposes enough capability.

Emit:

```text
SUBAGENT_DECISION: USE | DO_NOT_USE
REASON: <bounded execution rationale>
```

Small, tightly coupled, single-writer work should normally remain `INLINE`.

### Stable execution roles

- `EXPLORER` — read-only code/authority/test/runtime investigation;
- `WORKER` — authorized state-changing implementation inside an explicit writer boundary;
- `VERIFIER` — read-only targeted verification/runtime checks;
- `REVIEWER` — read-only diff/regression/acceptance review.

Default writer rule: one writer per overlapping semantic authority. Parallel writers require proven-disjoint authority/workspaces plus a defined integration boundary. Sub Agent redelegation is disabled by default unless a concrete high-complexity execution need and runtime capability justify it.

### Model / reasoning boundary

Engineering Governance selects role/topology, not a fixed provider/model. The receiving Local Codex environment owns concrete Sub Agent model/reasoning resolution.

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

## Source implementation result

- source hardening complete enough for Local trial;
- Plugin manifest: `0.7.2`;
- semantic candidate HEAD: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- latest pre-merge validation run: `38663053412` — `success`;
- PR `#33 — feat: harden local execution and Sub Agent orchestration` merged to `main`;
- merge commit: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.

## Local runtime acceptance

Source merge does not establish runtime PASS. Refresh/install Local Codex from `main` and test:

- installed plugin identity;
- local Sub Agent configuration/default source;
- `INLINE / Subagents: NO` negative case;
- useful delegated read-only case;
- writer-safety behavior;
- effective model/reasoning evidence where exposed, otherwise explicit `UNKNOWN`;
- final execution/Handoff receipt shape.

## Explicit boundaries

- do not create a new top-level Skill;
- do not make Engineering Governance a model router;
- do not hardcode one Local machine's model/capacity into reusable policy;
- do not force Sub Agent use for ordinary small tasks;
- do not create a formal GitHub v0.7.2 release/tag until separately authorized after runtime acceptance;
- do not update the private Web Plugin in this task phase;
- do not claim Local runtime acceptance until a real local install/readback/test is performed.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ROUTING-HARDENING-083` (`COMPLETE`)
- `START_MAIN_HEAD`: `0a2febb5cc294609d5ebfe54a4e84da1216de2dd`
- `PR`: `#33` (`MERGED`)
- `MERGE_COMMIT`: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`
- `TARGET_VERSION`: `0.7.2`
- `SEMANTIC_CANDIDATE_HEAD`: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`
- `PREMERGE_VALIDATION_RUN`: `38663053412`
- `SOURCE_VALIDATION`: `PASS`
- `FORMAL_RELEASE`: `NOT_AUTHORIZED_THIS_PHASE`
- `WEB_PLUGIN_UPDATE`: `NOT_AUTHORIZED_THIS_PHASE`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`
- `TASK_STATE`: `ACTIVE — MERGED_TO_MAIN_FOR_LOCAL_TRIAL`
