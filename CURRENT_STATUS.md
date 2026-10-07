# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Current remote baseline before this redesign control update: `d13e6895f6d4bddb753cabcc87566613eaa9bbec`.
- Repository purpose has been redefined: this repository will be a reusable AI engineering-governance **Skill source repository**, not a governance runtime/product and not an installer.
- The stable historical tag `v0.1.0` remains part of Git history and is not to be moved.
- No open pull requests were found at the redesign start.

## Accepted v1 direction

The v1 repository is organized around three reusable Skills:

1. `project-governance` — three-file control-plane standards, normal delivery flow, and proportional verification.
2. `domain-navigation` — semantic Domain Map, evidence-first repository understanding, code navigation, and optional read-only Repo Map assistance.
3. `incident-doctor` — evidence sufficiency, minimum probes, fresh-incident analysis, hypothesis/falsification, and probe lifecycle.

Four repository-wide principles are fixed for this redesign:

- standardize `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` roles;
- require a project-level Domain navigation layer;
- keep normal business/product development primary and enter Doctor only after a real evidence gap appears;
- scale verification effort by task risk instead of defaulting every task to the heaviest suite.

## Legacy live tree

The current `main` still contains the previous governance-runtime implementation and research structure, including `src/engineering_governance/`, `tests/`, legacy governance/reference documents, and Doctor/Bootstrap planning artifacts. Those remain present until a separately authorized restructure implementation task removes or replaces them.

Git history and the existing stable tag are sufficient archival mechanisms; the redesign does not require carrying obsolete runtime code into a new `archive/` directory.

## Current milestone — Skill repository redesign specification

- Active task: `EG-SKILLS-RESTRUCTURE-DESIGN-007`.
- State: `WAITING_FOR_USER_SPEC_REVIEW`.
- Design document: `docs/superpowers/specs/2026-10-07-skills-repository-restructure-design.md`.
- No local restructure implementation, deletion of legacy trees, new Skill skeleton, or implementation branch is authorized until the written design is reviewed and accepted.

## Upstream reference direction

The redesign uses external projects as design evidence, not as runtime dependencies:

- Agent Skills / Anthropic skill-creator structure for `SKILL.md`, `references/`, `assets/`, optional `scripts/`, and progressive disclosure.
- `AGENTS.md` open format for predictable agent-facing repository instructions.
- GitHub `awesome-copilot` `acquire-codebase-knowledge` for evidence-first repository understanding and explicit unknowns.
- Aider Repo Map for dynamic symbol/dependency ranking under a context/token budget.

No upstream code is authorized to be copied during the skeleton task.

## Next milestone

User review of the written redesign specification. If accepted, Web will produce a concrete implementation plan whose first local execution slice performs only the repository skeleton reset and legacy-live-tree retirement. After independent review of that slice, the three Skills will be enriched one module at a time rather than in one large implementation.
