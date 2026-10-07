# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose is fixed: a reusable AI engineering-governance **Skill source repository**, not a governance runtime/product and not an installer.
- The stable historical tag `v0.1.0` must remain anchored to commit `738627a0caad330d277f60cfdaff5f153593135e`.
- Root `AGENTS.md` remains the durable repository rule set; no durable-rule change is required for this implementation authorization.

## Accepted redesign and plan

- Accepted design: `docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`.
- Accepted Phase A plan: `docs/superpowers/plans/2026-10-07-skill-repository-skeleton-reset-implementation-plan.md`.
- Plan creation commit: `82099ad7033d9bdc0aec6b7d880f157008157392`.
- Plan-review control baseline: `4c91d767a98d34dc851c12532faf4fdf5551a373`.

The v1 repository remains organized around exactly three reusable Skills:

1. `project-governance` — three-file control-plane standards, normal delivery flow, and proportional verification.
2. `domain-navigation` — semantic Domain Map, evidence-first repository understanding, code navigation, and optional read-only Repo Map assistance.
3. `incident-doctor` — evidence sufficiency, minimum probes, fresh-incident analysis, hypothesis/falsification, and probe lifecycle.

## Active milestone — Phase A skeleton reset implementation

- Active task: `EG-SKILLS-RESTRUCTURE-IMPL-009`.
- State: `AUTHORIZED_FOR_LOCAL_EXECUTION`.
- Authorized branch: `codex/skill-repository-skeleton-reset`.
- Scope: Phase A only — retire the obsolete live runtime/research structure, establish the full three-Skill repository skeleton, create concise reference/template contracts, and perform `V0` verification.
- The implementation must execute the accepted plan task-by-task and must not deepen Phase B-E Skill content.
- No merge is authorized. Local execution must stop after pushing a clean matched task branch in `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Current live-tree condition

At authorization time, `main` still contains the retired Python governance runtime, its tests, legacy governance/reality-check/reference-audit trees, and obsolete Doctor/Bootstrap planning artifacts. Their removal is authorized only on the Phase A task branch according to the exact retirement manifest and STOP conditions in the accepted plan.

Git history and `v0.1.0` are the historical archive; no live `archive/` copy is required.

## Verification policy for this slice

`V0` only:

- exact target tree and exactly three top-level Skills;
- valid/distinct `SKILL.md` frontmatter;
- all referenced template/reference paths exist;
- retired runtime/research trees are absent;
- no executable product/runtime surface is introduced;
- upstream/license notes are present;
- `v0.1.0^{}` still resolves to `738627a0caad330d277f60cfdaff5f153593135e`;
- task worktree is clean and local/remote task heads match at handoff.

## Next milestone

Independent Web audit of the remote Phase A task branch. Only after that audit passes may Web authorize merge or a corrective. Phase B (`project-governance` enrichment) is not authorized by this task.
