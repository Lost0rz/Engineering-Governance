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

## v0.6.0 architecture — ROUTING / ENVIRONMENT HARDENING ACTIVE

Task `EG-CAPABILITY-ROUTING-ENVIRONMENT-HARDENING-066` is active on `codex/capability-model-v0.6.0`.

- Task start literal HEAD: `b6bb90a4abfb1c99ef7fe91bcfa0b3ba0aa18b2a`.
- Prior frozen semantic HEAD: `b7fb0051b8c51b5c846a507fad9037518dcf18db` — superseded once Task 066 produces a new semantic freeze.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance remains `NOT_RUN_BY_DESIGN`.

## Stable invariants

- Exactly seven top-level Skills remain; global routing is policy, not an eighth Skill.
- `CURRENT_TASK.md` remains the single active execution authorization.
- Task purpose, execution unit, and execution context remain distinct.
- Safe useful Sub Agent parallelism remains encouraged.
- Delegated-model stabilization remains `ENVIRONMENT_DEFAULT_ONLY`; concrete runtime values remain owned by the current execution environment.

## Task 066 focus

- environment-neutral routing surfaces;
- concise Skill-owned portable workflows and lighter repository-only root guidance;
- generic environment capability resolution without hardcoded values;
- bounded cross-repository governance/navigation;
- small routing/safety gaps in Evidence Audit, Handoff, Solution Design, Incident Doctor, and control-write acceptance.

No new runtime/model-router/enforcement implementation is authorized.

## Next milestone

Complete Task 066 as one coherent source change, freeze a new semantic head, then run one consolidated installed Plugin/Web/Codex acceptance matrix rather than testing one Skill at a time.
