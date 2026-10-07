# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose is now fixed: a reusable AI engineering-governance **Skill source repository**, not a governance runtime/product and not an installer.
- The stable historical tag `v0.1.0` must remain anchored to commit `738627a0caad330d277f60cfdaff5f153593135e`.
- No open pull requests were present at redesign start.

## Accepted redesign

The user accepted the written redesign specification on 2026-10-07:

`docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`

The v1 repository is organized around exactly three reusable Skills:

1. `project-governance` — three-file control-plane standards, normal delivery flow, and proportional verification.
2. `domain-navigation` — semantic Domain Map, evidence-first repository understanding, code navigation, and optional read-only Repo Map assistance.
3. `incident-doctor` — evidence sufficiency, minimum probes, fresh-incident analysis, hypothesis/falsification, and probe lifecycle.

Four repository-wide principles are fixed:

- standardize `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` roles;
- require a project-level Domain navigation layer;
- keep normal business/product development primary and enter Doctor only after a real evidence gap appears;
- scale verification effort by task risk instead of defaulting every task to the heaviest suite.

## Legacy live tree

The current `main` still contains the previous governance-runtime implementation and research structure, including `src/engineering_governance/`, `tests/`, legacy governance/reference documents, and old Doctor/Bootstrap planning artifacts. They remain present until the separately authorized skeleton-reset implementation task executes.

Git history and the existing stable tag are the archive; the redesign does not require an `archive/` live-tree copy.

## Current milestone — Phase A implementation-plan review

- Active task: `EG-SKILLS-RESTRUCTURE-PLAN-008`.
- State: `WAITING_FOR_USER_PLAN_REVIEW`.
- Implementation plan: `docs/superpowers/plans/2026-10-07-skill-repository-skeleton-reset-implementation-plan.md`.
- Plan commit: `82099ad7033d9bdc0aec6b7d880f157008157392`.
- Phase A only resets the live repository skeleton, retires obsolete live runtime/research files, establishes the three Skill entrypoints plus reference/template contracts, and performs `V0` verification.
- Deep Skill content remains deferred to separate, independently reviewed phases.
- No local restructure implementation branch or worktree is authorized while this task remains in plan review.

## Upstream reference direction

The redesign uses external projects as design evidence, not runtime dependencies:

- Agent Skills / Anthropic skill structure and progressive disclosure;
- AGENTS.md open format;
- GitHub `awesome-copilot` `acquire-codebase-knowledge` for evidence-first repository understanding and explicit unknowns;
- Aider Repo Map for dynamic symbol/dependency relevance under limited context.

Phase A copies no upstream source code or long-form text.

## Next milestone

Review the Phase A implementation plan. If accepted, Web will create a separate implementation task with an exact remote baseline and one authorized task branch, then hand the plan to the local AI executor. The local result must stop at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`; Web will audit the remote branch before any merge.
