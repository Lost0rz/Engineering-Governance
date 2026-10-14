# CURRENT TASK — Environment Model Authority v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065`

Task class: `CORRECTIVE`

State: `COMPLETE`

Mode: remote reusable-source model-authority correction before consolidated installed Plugin/runtime acceptance

## Objective

Remove concrete Local Sub Agent model/reasoning examples from reusable Engineering Governance source and make each execution environment's own authoritative Sub Agent configuration/runtime default the sole source for delegated model selection during stabilization.

The reusable Plugin must remain safe across Local Codex, ChatGPT Web, cloud agents, other machines, and future execution surfaces without importing model settings from another context.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: bounded correction of Task 064 delegated-model authority semantics; seven-Skill architecture and positive safe Sub Agent parallelism remain unchanged.

## Accepted baseline

- Task start literal branch HEAD: `4500698b81efccac9b358860c0ace90cc39602d3`.
- Prior Task 064 Architecture Delivery / Semantic HEAD: `31d9d94f1f59a3d5b49fb7c614f37ec752cff479`.
- Branch: `codex/capability-model-v0.6.0`.
- PR #26 remained OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance was not run.

## Accepted operating policy

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
SUBAGENT_MODEL_SOURCE: current execution environment authoritative Sub Agent configuration/runtime default
MODEL_OVERRIDE: NONE
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

1. Reusable source does not define a concrete provider/model/reasoning setting as the default for Sub Agents.
2. Each execution environment resolves its own Sub Agent default from its authoritative runtime/configuration surface.
3. Local Codex may read and use its own local Sub Agent configuration locally; this is local runtime truth, not reusable repository truth.
4. Web/cloud contexts use their own platform/runtime defaults and do not inherit Local settings through repository text, handoff, memory, or another machine.
5. If exact model/reasoning identity is not exposed by the environment, it remains `PLATFORM_DEFAULT` / `UNKNOWN`; no inference or override is authorized.
6. Handoff transports task/policy/authority context, not concrete delegated-model values across environments.
7. Stronger-model override/escalation remains disabled during stabilization until a later explicit user/project policy change.

## Completed work

### WP16 — Environment model authority

- Updated `execution-orchestrator` Skill and execution contract to `ENVIRONMENT_DEFAULT_ONLY`.
- Removed concrete Local model/reasoning examples from active reusable guidance and durable v0.6.0 design authorities.
- Added explicit environment-configuration isolation to Agent Handoff Skill/contract.
- Updated root `AGENTS.md` and README to make runtime configuration environment-owned.
- Updated Project Governance development flow and Skill Engineering quality contract to the same policy.
- Updated integrated acceptance to test observable local configuration, opaque managed-platform defaults, cross-context isolation, no guessing, and no stronger-model escalation.
- Preserved positive Sub Agent parallelism and all non-model seven-Skill semantics.

## New architecture freeze

Frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`b7fb0051b8c51b5c846a507fad9037518dcf18db`

Later closeout commits are semantic-tree-equivalent descendants: comparison from `b7fb0051...` to the final Task 065 literal head changes only `CURRENT_STATUS.md` and `CURRENT_TASK.md`. The Task 064 semantic candidate `31d9d94f1f59a3d5b49fb7c614f37ec752cff479` is historical/superseded for final v0.6.0 acceptance.

## Verification result

`V2 remote source-architecture audit: PASS`.

Evidence:

- compare from Task 065 start `4500698b...` to semantic head `b7fb0051...` contains only governance/Skill/design/acceptance Markdown/control files;
- exactly seven top-level Skill directories remain;
- Plugin metadata remains `0.6.0`;
- no runtime/daemon/database/release-workflow/model-router implementation was added;
- active reusable policy is `ENVIRONMENT_DEFAULT_ONLY`;
- concrete model/reasoning configuration belongs only to the execution environment that owns it;
- cross-context handoff does not propagate concrete model/reasoning defaults;
- managed/opaque defaults remain `PLATFORM_DEFAULT` / `UNKNOWN` rather than guessed;
- stronger-model escalation remains disabled;
- safe positive Sub Agent parallelism remains intact;
- PR #26 is OPEN / DRAFT / UNMERGED / `mergeable=true` at audit time;
- semantic head has no reported commit/check statuses; CI PASS is not claimed.

## Acceptance criteria

All Task 065 source-corrective acceptance criteria are satisfied.

Installed Plugin/Web/Codex integrated acceptance remains explicitly outside this task and has not run. The accepted next sequence is one consolidated integrated acceptance task against semantic head `b7fb0051b8c51b5c846a507fad9037518dcf18db` or a proven semantic-tree-equivalent descendant.

## Handoff / terminal state

Task 065 is complete. PR #26 remains Draft.

Next authorized work should be the consolidated v0.6.0 integrated acceptance task using `references/V060_INTEGRATED_ACCEPTANCE.md`. Local and Web acceptance must each resolve their own execution-environment Sub Agent default; do not copy one environment's concrete settings into another. Reusable defects discovered during installed acceptance return to remote source; do not patch reusable source inside installed Plugin caches.

Control Alignment Gate:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-hardening-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UPDATED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
