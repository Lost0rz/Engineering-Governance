# CURRENT TASK — Local Execution / Sub Agent Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084`

Task class: `CAPABILITY_HARDENING`

State: `ACTIVE`

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

Governed execution receipts must report Sub Agent usage when execution occurred:

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

## Scope

Primary source changes:

- `skills/execution-orchestrator/SKILL.md`;
- `skills/execution-orchestrator/references/execution-contract.md`;
- `skills/execution-orchestrator/references/environment-capabilities.md`;
- new bounded Sub Agent execution reference;
- `skills/project-governance/references/planning-documents.md`;
- `skills/project-governance/SKILL.md` receipt contract;
- integrated acceptance reference for the new local execution behavior;
- manifests/version only as needed for a testable v0.7.2 candidate.

## Explicit boundaries

- do not create a new top-level Skill;
- do not make Engineering Governance a model router;
- do not hardcode one Local machine's model/capacity into reusable policy;
- do not force Sub Agent use for ordinary small tasks;
- do not update the private Web Plugin in this task phase;
- do not claim Local runtime acceptance until a real local test/readback is performed.

## Acceptance

Source hardening is ready for local trial when:

- planning and execution responsibilities are separated;
- the Sub Agent value gate is explicit;
- the four execution roles and writer safety are explicit;
- topology choice is efficiency-first rather than agent-count-first;
- configured vs effective model/reasoning evidence is distinguished;
- execution receipts expose topology/Sub Agent/runtime information;
- acceptance scenarios cover positive and negative delegation cases;
- source consistency checks pass;
- Web Plugin remains unchanged.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ROUTING-HARDENING-083` (`COMPLETE`)
- `START_MAIN_HEAD`: `0a2febb5cc294609d5ebfe54a4e84da1216de2dd`
- `TASK_BRANCH`: `codex/local-execution-subagent-hardening-v072`
- `TARGET_VERSION`: `0.7.2-candidate`
- `WEB_PLUGIN_UPDATE`: `NOT_AUTHORIZED_THIS_PHASE`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`
- `TASK_STATE`: `ACTIVE`
