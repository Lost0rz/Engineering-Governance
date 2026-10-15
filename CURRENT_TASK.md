# CURRENT TASK — Local Execution / Sub Agent Hardening

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084`

Task class: `CAPABILITY_HARDENING`

State: `ACTIVE — DISTRIBUTED_FOR_RUNTIME_TRIAL`

## Objective

Harden Local Codex execution so Sub Agents are used only when they materially improve throughput, context isolation, or verification quality.

Sub Agent use is an execution optimization, not a goal. Planning exposes executable structure; `execution-orchestrator` decides at execution time whether delegation is worthwhile in the current environment.

## Required behavior

### Planning / execution boundary

Complex plans may expose bounded work packages with objective, dependencies, writer boundary, acceptance, and parallelizability when materially useful. Planning must not freeze machine-specific parallel capacity, concrete model names, reasoning effort, or a mandatory Sub Agent topology.

### Sub Agent value gate

Before delegation, evaluate whether the work has genuinely independent units, dependency structure permits useful concurrency/context isolation, write boundaries are safe, expected value exceeds coordination cost, and the current execution environment exposes enough capability.

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

Engineering Governance selects role/topology, not a fixed provider/model. The receiving execution environment owns concrete Sub Agent model/reasoning resolution.

Internal evidence may use:

```text
MODEL_SOURCE: <parent inheritance | agents default | role/custom config | runtime/platform | UNKNOWN>
MODEL_CONFIG: <configured value | PLATFORM_DEFAULT | UNKNOWN>
REASONING_CONFIG: <configured value | PLATFORM_DEFAULT | UNKNOWN>
MODEL_EFFECTIVE: <observed value | UNKNOWN>
REASONING_EFFECTIVE: <observed value | UNKNOWN>
```

Never report an effective model/reasoning value solely because configuration suggests it.

### Receipt observability

Governed execution and cross-context EXECUTE receipts report:

```text
Execution topology:
Subagents:
Subagent runtime:
```

If no Sub Agent was used, `Subagents: NO` is sufficient. If used, report bounded role/count and observable model/reasoning identity; unknown effective runtime values remain `UNKNOWN`.

## Source / distribution result

- Plugin manifest: `0.7.2`;
- semantic candidate HEAD: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- latest pre-merge validation run: `38663053412` — `success`;
- PR `#33 — feat: harden local execution and Sub Agent orchestration` merged to `main`;
- merge commit: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`;
- Air Local Codex cache readback: `0.7.2` present at `/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.7.2`;
- private Web Plugin updated in place to `0.7.2`;
- Web Plugin ID unchanged: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web release ID: `pluginrel_6ad02855852c8191a7addd05d6026361`;
- Web readback confirmed both manifests plus Execution Orchestrator, Sub Agent execution, Project Governance receipt, and Handoff execution evidence contracts.

`V072_SOURCE_READY_FOR_LOCAL_TRIAL`: `PASS`.
`WEB_PLUGIN_SYNC_072`: `PASS`.

## Runtime acceptance

Distribution/install does not establish runtime PASS. Next verify in a fresh Local Codex session:

- loaded plugin identity;
- local Sub Agent configuration/default source;
- `INLINE / Subagents: NO` negative case;
- useful delegated read-only case;
- writer-safety behavior;
- effective model/reasoning evidence where exposed, otherwise explicit `UNKNOWN`;
- final execution/Handoff receipt shape.

## Explicit boundaries

- do not create a new top-level Skill;
- do not make Engineering Governance a model router;
- do not hardcode one machine's model/capacity into reusable policy;
- do not force Sub Agent use for ordinary small tasks;
- do not claim Local runtime acceptance until a real local session/readback/test is performed;
- formal GitHub tag/release remains a separate lifecycle step.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-DESIGN-ROUTING-HARDENING-083` (`COMPLETE`)
- `PR`: `#33` (`MERGED`)
- `MERGE_COMMIT`: `29f7b7581a904b81f1e6ada8ec4fe0266cd6bfe1`
- `TARGET_VERSION`: `0.7.2`
- `SEMANTIC_CANDIDATE_HEAD`: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`
- `SOURCE_VALIDATION`: `PASS`
- `LOCAL_PLUGIN_CACHE_072`: `OBSERVED`
- `WEB_PLUGIN_UPDATE`: `PASS`
- `WEB_RELEASE_ID`: `pluginrel_6ad02855852c8191a7addd05d6026361`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PENDING`
- `TASK_STATE`: `ACTIVE — DISTRIBUTED_FOR_RUNTIME_TRIAL`
