# CURRENT TASK — Environment Model Authority v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065`

Task class: `CORRECTIVE`

State: `ACTIVE`

Mode: remote reusable-source model-authority correction before consolidated installed Plugin/runtime acceptance

## Objective

Remove concrete Local Sub Agent model/reasoning examples from reusable Engineering Governance source and make each execution environment's own authoritative Sub Agent configuration/runtime default the sole source for delegated model selection during stabilization.

The reusable Plugin must remain safe across Local Codex, ChatGPT Web, cloud agents, other machines, and future execution surfaces without importing model settings from another context.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: narrow correction of Task 064 delegated-model authority semantics; seven-Skill architecture and positive safe Sub Agent parallelism remain unchanged.

## Accepted baseline

- Task start literal branch HEAD: `4500698b81efccac9b358860c0ace90cc39602d3`.
- Prior Task 064 Architecture Delivery / Semantic HEAD: `31d9d94f1f59a3d5b49fb7c614f37ec752cff479`.
- Branch: `codex/capability-model-v0.6.0`.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance has not run.

## User-decided operating policy

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
SUBAGENT_MODEL_SOURCE: current execution environment authoritative Sub Agent configuration/runtime default
MODEL_OVERRIDE: NONE
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

1. Reusable source must not contain a concrete provider/model/reasoning setting as the default for Sub Agents.
2. Each execution environment resolves its own Sub Agent default from its authoritative runtime/configuration surface.
3. Local Codex may read and use its own local Sub Agent configuration; this is local runtime truth, not reusable repository truth.
4. Web/cloud contexts use their own platform/runtime defaults. They must not inherit Local settings through repository text, handoff, memory, or another machine.
5. If exact model/reasoning identity is not exposed by the environment, do not infer it; use `PLATFORM_DEFAULT` / `UNKNOWN` evidence semantics and avoid explicit override.
6. Handoff transports task/policy/authority context, not concrete delegated-model values across environments.
7. Stronger-model override/escalation remains disabled during stabilization until a later explicit user/project policy change.

## In scope

- Update `execution-orchestrator` Skill and execution contract from generic `DEFAULT_ONLY` wording to environment-authoritative `ENVIRONMENT_DEFAULT_ONLY` semantics.
- Remove concrete model/reasoning examples from reusable source and durable active design documents.
- Add explicit cross-context non-propagation of model/reasoning configuration to Agent Handoff where needed.
- Update root guidance and integrated acceptance for Local-vs-Web environment separation and unknown/unobservable defaults.
- Update PR metadata and controls after source audit.

## Out of scope

- Reading or changing the user's actual Local Codex configuration from the remote source task.
- Naming or selecting any concrete provider/model/reasoning value in reusable source.
- Building a model router/runtime.
- Re-enabling stronger-model escalation.
- Changing positive Sub Agent parallelism, task/context semantics, Evidence Audit, Domain Navigation or Incident Doctor architecture.
- Installed Plugin/Web/Codex integrated acceptance.
- PR merge or v0.6.0 release.

## Verification

`V2` source-architecture corrective.

Verify:

- no active reusable source names a concrete default Sub Agent model or reasoning value;
- current delegated policy points to the current execution environment's authoritative configuration/runtime default;
- Web/local/cloud model settings cannot be propagated across contexts by handoff/repository defaults;
- unobservable exact defaults remain `PLATFORM_DEFAULT` / `UNKNOWN` rather than guessed;
- stronger-model escalation remains disabled;
- positive safe parallelism remains intact;
- seven top-level Skills remain unchanged;
- no runtime/model-router/workflow implementation is added.

## Acceptance criteria

- Task 064 concrete-environment examples are removed from active reusable semantics.
- `ENVIRONMENT_DEFAULT_ONLY` is the active delegated-model policy.
- Local and Web are explicitly isolated configuration authorities for their own execution environments.
- Handoff does not carry concrete model/reasoning configuration across environment boundaries.
- Remote source audit passes and a new semantic head is frozen.

## Stop conditions

Stop if satisfying this correction requires changing an actual runtime configuration, adding a model-selection runtime, or materially redesigning another Skill.
