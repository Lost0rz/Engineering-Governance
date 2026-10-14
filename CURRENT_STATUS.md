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

## v0.6.0 architecture — ENVIRONMENT MODEL AUTHORITY CORRECTIVE ACTIVE

Task `EG-CAPABILITY-ENVIRONMENT-MODEL-AUTHORITY-065` is active on branch `codex/capability-model-v0.6.0`.

- Prior Task 064 semantic candidate: `31d9d94f1f59a3d5b49fb7c614f37ec752cff479`.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance remains `NOT_RUN_BY_DESIGN`.

The Task 064 freeze is reopened only to remove environment-specific model/reasoning examples from reusable source and make the current execution environment the sole delegated-model configuration authority.

## User-decided environment model policy

- Sub Agents remain a positive throughput/context-isolation capability; safe useful parallelism remains encouraged.
- Reusable governance must never hardcode or recommend one concrete Sub Agent model or reasoning setting as a cross-environment default.
- Each execution context resolves delegated model behavior from **its own authoritative Sub Agent configuration/runtime default**.
- Local Codex uses its own local configuration when that configuration is authoritative and observable.
- Web/cloud/other contexts use their own environment/platform default; they must not inherit a Local model name or reasoning setting from repository source, handoff, memory, or another machine.
- If an environment does not expose the concrete default model/reasoning identity, do not infer it. Record `PLATFORM_DEFAULT` / `UNKNOWN` as appropriate and do not override it.
- Handoff may transfer the policy (`ENVIRONMENT_DEFAULT_ONLY`) but must not propagate concrete model/reasoning values across execution contexts.
- Stronger-model override/escalation remains disabled until a later explicit policy change.

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

## Active corrective scope

Task 065 updates only model-configuration authority semantics:

- Execution Orchestrator Skill/contract;
- root/reusable guidance that still names concrete model/reasoning examples;
- handoff boundary for cross-context model propagation;
- integrated acceptance scenarios;
- durable v0.6.0 design records and PR metadata for consistency.

Task purpose/context, positive parallelism, audit, Domain Navigation, Incident Doctor and seven-Skill topology remain otherwise unchanged.

## Next milestone

Complete Task 065 source correction, run a bounded remote source audit, freeze a new v0.6.0 semantic candidate, then proceed to one consolidated integrated acceptance pass.
