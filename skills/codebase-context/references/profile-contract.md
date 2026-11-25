# Project Profile — compact derived context

`PROJECT_PROFILE_CLASS: DERIVED_PROJECT_CONTEXT`

A Profile is a compact **navigation aid**, never task authority, workflow controller, or substitute for canonical source/`AGENTS.md`. Consuming an existing Profile does not invoke `codebase-context`; writing or modifying a repo-managed Profile requires active host/task write authorization.

## 1. Grounding & durability gates

- **Grounding:** trace every project-specific fact to current verified repository sources, accepted architecture docs, runtime evidence, or explicit current-task user direction. Memory, prior chats, and old Profiles are discovery leads only; drop unverified claims rather than promoting them.
- **Durability:** retain only stable facts expected to outlast the current task/PR/milestone (purpose, core domains, version-scoped architecture, stable platform roles, authority pointers). Exclude current sprint/wave/MVP priorities, temporary ports/machines/branches/worktrees, and live CI/incident status.

## 2. Classification & compression

Before emitting a Profile, route non-Profile content back to its real owner:

- Current task/PR/CI state -> Task/Issue/PR/CI;
- Project-specific MUST/MUST-NOT execution rules -> project `AGENTS.md`;
- Detailed code/symbol/test maps -> canonical Domain authority or `DOMAIN_MAP.md`;
- Reusable workflow/verification/CI mechanics -> installed Engineering Governance plugin.

**Authority-map structural rule:** when a detailed Domain/navigation authority exists, keep `Authority map` **pointer-only**—never copy `X owns / Y owns` catalogs or code inventories into the Profile. Keep `Environment` strictly to stable runtime/platform roles and pointers (no source paths, symbols, or local ports).

## 3. Surface role & compliance gate

Preserve fixed metadata fields `Profile surface` and `Primary/mirror role` (`PRIMARY | MIRROR | single surface | UNKNOWN`). Never invent a `PRIMARY` or multiple surfaces without authority.

Before returning a created/updated/audited Profile, verify and fix any defect in the same pass:

- Every claim is grounded, durable, and deduplicated against `AGENTS.md` and Domain authorities;
- `Authority map` is pointer-only when a Domain authority exists;
- `Environment` contains no source paths, symbols, or behavioral rules;
- `Engineering Governance` section stays compact using [PROJECT_PROFILE.md](../assets/templates/PROJECT_PROFILE.md).
