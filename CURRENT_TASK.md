# CURRENT TASK — Environment Model Authority v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065`

Task class: `CORRECTIVE`

State: `COMPLETE`

Mode: remote reusable-source model-authority correction before consolidated installed Plugin/runtime acceptance

## Objective

Remove concrete Local Sub Agent model/reasoning examples from reusable Engineering Governance source and make each execution environment's own authoritative Sub Agent configuration/runtime default the sole source for delegated model selection during stabilization.

## Planning context

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture authority: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Relationship to plan: bounded correction of Task 064 model-authority semantics; seven-Skill architecture and positive safe Sub Agent parallelism remain unchanged.

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

- Reusable source does not define a concrete provider/model/reasoning setting as the default for Sub Agents.
- Each execution environment resolves its own Sub Agent default from its authoritative runtime/configuration surface.
- Local configuration remains local runtime truth; Web/cloud/managed defaults remain authority for those environments.
- If exact model/reasoning identity is not exposed, keep it `PLATFORM_DEFAULT` / `UNKNOWN`; no inference or override is authorized.
- Handoff transports policy/task authority, not concrete delegated-model values across environments.
- Stronger-model override/escalation remains disabled until a later explicit user/project policy change.

## Completed work

- Updated `execution-orchestrator` Skill and contract to `ENVIRONMENT_DEFAULT_ONLY`.
- Removed concrete Local model/reasoning examples from active reusable guidance and durable v0.6.0 design authorities.
- Added environment-configuration isolation to Agent Handoff Skill/contract.
- Updated root guidance, Project Governance development flow, Skill Engineering quality contract, and integrated acceptance.
- Preserved positive Sub Agent parallelism and all non-model seven-Skill semantics.

## Architecture freeze

Frozen v0.6.0 Architecture Delivery / Semantic HEAD:

`b7fb0051b8c51b5c846a507fad9037518dcf18db`

Later closeout descendants are semantic-tree-equivalent: the final tree differs from this semantic head only in `CURRENT_STATUS.md` and `CURRENT_TASK.md`.

## Verification result

`V2 remote source-architecture audit: PASS`.

Verified:

- Task 065 source changes are governance/Skill/design/acceptance Markdown/control only;
- exactly seven top-level Skill directories remain;
- Plugin metadata remains `0.6.0`;
- no runtime/daemon/database/release-workflow/model-router implementation was added;
- active policy is `ENVIRONMENT_DEFAULT_ONLY`;
- concrete model/reasoning configuration remains environment-owned and does not propagate across contexts;
- opaque defaults remain `PLATFORM_DEFAULT` / `UNKNOWN` rather than guessed;
- stronger-model escalation remains disabled;
- safe positive Sub Agent parallelism remains intact;
- PR #26 was OPEN / DRAFT / UNMERGED / `mergeable=true` at audit time;
- semantic head has no reported commit/check statuses; CI PASS is not claimed.

## Handoff / terminal state

Task 065 is complete. PR #26 remains Draft.

Next authorized work should be one consolidated v0.6.0 integrated acceptance task using `references/V060_INTEGRATED_ACCEPTANCE.md`. Each tested execution environment resolves its own Sub Agent configuration/runtime default. Reusable defects found during acceptance return to remote source; do not patch reusable source inside installed Plugin caches.

Control Alignment Gate:

- `RELATED_DOCUMENT`: `documents/engineering-governance-capability-hardening-v0.6.0.md`
- `DOCUMENT_ALIGNMENT`: `UPDATED`
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED`
- `CURRENT_TASK_RECONCILIATION`: `UPDATED`
- `CONTROL_ALIGNMENT`: `PASS`
