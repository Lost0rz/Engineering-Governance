# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.5`.

- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- ChatGPT Web Plugin accepted baseline: `0.5.5`.
- Mac mini Codex accepted Plugin baseline: `0.5.5`.
- MacBook Air Codex accepted Plugin baseline: `0.5.5`.

No v0.6.0 release or installed Plugin/Web/Codex integrated acceptance has been performed yet.

## v0.6.0 architecture — FROZEN FOR CONSOLIDATED ACCEPTANCE

Task `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065` completed the environment-model-authority corrective on branch `codex/capability-model-v0.6.0`.

- Architecture Delivery / Semantic HEAD: `b7fb0051b8c51b5c846a507fad9037518dcf18db`.
- Prior Task 064 semantic candidate `31d9d94f1f59a3d5b49fb7c614f37ec752cff479` is historical/superseded for final v0.6.0 acceptance because reusable model-authority semantics changed after that freeze.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- PR host mergeability observed during Task 065 source audit: `mergeable=true`.
- Commit/check statuses on the semantic head: none reported; **CI PASS is not claimed**.
- Installed Plugin/Web/Codex integrated acceptance: `NOT_RUN_BY_DESIGN`.

## Seven-Skill model unchanged

Exactly seven top-level Skills remain:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Accepted delegated-model authority semantics

- Sub Agents remain a positive throughput/context-isolation capability; safe useful parallelism remains encouraged.
- Active stabilization policy is `ENVIRONMENT_DEFAULT_ONLY`.
- Reusable Engineering Governance does not define a concrete provider/model/reasoning value for delegated Sub Agents.
- Each execution context resolves its own authoritative Sub Agent configuration/runtime default.
- A local runtime may use/read its own local configuration locally without promoting that configuration into reusable Plugin truth.
- Web/cloud/managed runtimes use their own platform/runtime defaults and do not inherit Local settings through repository source, handoff, memory, or another machine.
- If an environment does not expose exact model/reasoning identity, keep it `PLATFORM_DEFAULT` / `UNKNOWN`; do not guess or override it.
- Agent Handoff may carry the model **policy**, but concrete sender model/reasoning values do not become receiver defaults.
- Stronger-model override/escalation remains disabled until a later explicit user/project policy change.
- `LOW / STANDARD / HIGH` remain inactive future vocabulary only and do not route delegated Sub Agents during stabilization.

## Other hardened v0.6.0 semantics preserved

- Task purpose, Sub Agent execution unit, and execution context remain distinct.
- Same-purpose work may continue across Web/local/cloud/session/machine/Sub Agent contexts under the same `TASK_ID`.
- Safe independent Sub Agent parallelism is positively used when beneficial.
- Parallel writers require proven-disjoint semantic authority/workspaces and integration evidence.
- Agent Handoff remains context-neutral and rereads current authority.
- Evidence Audit distinguishes implementation self-check from independent acceptance and binds verdicts to required claims/evidence/independence basis.
- Domain Navigation and Incident Doctor trigger boundaries remain unchanged.

## Integrated acceptance specification

`references/V060_INTEGRATED_ACCEPTANCE.md` now tests:

- exact seven-Skill discovery and normal Project Governance entry;
- positive and negative routing;
- same-task continuation across contexts;
- positive safe parallel Sub Agent use;
- `ENVIRONMENT_DEFAULT_ONLY` behavior;
- environment-specific configuration authority and Local/Web/cloud isolation;
- observable current-environment configuration without promoting it into reusable source;
- `PLATFORM_DEFAULT` / `UNKNOWN` behavior when managed defaults are opaque;
- no cross-context concrete model/reasoning propagation;
- no stronger-model escalation during stabilization;
- handoff, audit, control, CI/PR/release/post-change, Domain Navigation, and Incident Doctor scenarios.

The consolidated acceptance matrix has **not** been executed under Task 065.

## Task 065 remote source audit

`V2 remote source-architecture audit: PASS` for semantic head `b7fb0051b8c51b5c846a507fad9037518dcf18db`.

Verified:

- exact seven-Skill directory set and no eighth Router Skill;
- Plugin metadata remains `0.6.0`;
- Task 065 changes are governance/Skill/design/acceptance Markdown/control only;
- no runtime, daemon, database, release workflow, model-router, or automatic model-selection implementation was added;
- active reusable model semantics use `ENVIRONMENT_DEFAULT_ONLY` rather than a concrete model/reasoning default;
- concrete sender settings do not propagate across Web/local/cloud handoff boundaries;
- unobservable platform defaults stay `PLATFORM_DEFAULT` / `UNKNOWN` rather than guessed;
- stronger-model escalation remains disabled;
- positive safe parallelism remains intact;
- PR #26 remained Draft and mergeable during the audit;
- no commit/check status exists on the semantic head, so CI PASS is not claimed.

## Active problems and blockers

No blocking remote source defect is known from Task 065 audit.

Remaining acceptance dependency: run one consolidated installed Plugin/Web/Codex acceptance pass against semantic head `b7fb0051b8c51b5c846a507fad9037518dcf18db` or a proven semantic-tree-equivalent descendant. Reusable-source defects discovered there return to the remote source flow.

## Next intended milestone

Authorize the consolidated v0.6.0 integrated acceptance task using `references/V060_INTEGRATED_ACCEPTANCE.md`. Do not split acceptance into one Skill at a time.

## Task 065 control alignment

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent architecture: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Document alignment: `UPDATED` — both active design authorities now express environment-owned delegated-model configuration and cross-context isolation.
- `CURRENT_STATUS.md`: `UPDATED`.
- `CURRENT_TASK.md`: `UPDATED`.
- Control alignment: `PASS`.
