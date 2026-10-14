# Project Profile contract

## Role

`PROJECT_PROFILE_CLASS: DERIVED_PROJECT_CONTEXT`

The Profile is a concise context/index compiled from verified project authorities. It helps Web/local/agent context recovery but has no independent power to authorize work or override truth.

A healthy Profile is a **landing index**, not a summarized copy of the governance system, Domain map, or Profile-maintenance rules behind it.

## Current projection surface

A project should have **one current Profile projection surface**. It may be a repository file such as `PROJECT_PROFILE.md`, ChatGPT Project Instructions, or another accepted project context surface.

If the target surface is known, state:

```text
Profile surface: <repository file | project instructions | other accepted surface>
Primary/mirror role: <PRIMARY | MIRROR | single surface | UNKNOWN>
```

Role claims are evidence-bound:

- `MIRROR` requires a verified/explicitly identified primary Profile surface. Name or point to that primary when useful.
- `PRIMARY` requires project/user authority explicitly designating this surface as primary/canonical among multiple Profile surfaces.
- `single surface` is used when this is the only established current Profile surface and no competing surface is verified.
- `UNKNOWN` is preferred to guessing when the relationship cannot be established from current authority/user intent.

Do not infer `MIRROR` merely because the target is ChatGPT Project Instructions, and do not infer `PRIMARY` merely because a repository file could exist.

If two surfaces are operationally required, declare one `PRIMARY_PROFILE_SURFACE` and treat the other as a derived mirror. Do not maintain two independently edited current Profiles. A stale mirror never overrides the primary projection or underlying authorities.

Do not create a new manifest merely to name the surface. Record the pointer in an existing project authority/context surface when that is useful and supported by the project.

## Mutation authority

Profile generation, comparison, or draft output can be read-only. Creating/updating a repository/project-managed Profile is state-changing and requires compatible active task authorization through Project Governance. Profile staleness by itself does not grant write authority.

## Recommended contents

Keep only stable context that materially reduces orientation cost:

- purpose and core business/product loop;
- a few stable concepts needed to understand the project;
- authority map/pointers;
- durable planning/navigation pointers;
- stable project environment roles;
- project-specific priorities, anti-goals, or risk cues;
- a short Engineering Governance hook.

Project-specific stable facts may summarize a concept, but reusable procedure and detailed normative rules should be linked rather than re-explained.

## Anti-content / deduplication

Do **not** turn the Profile into a second `AGENTS.md`, routing manual, handoff protocol, verification guide, incident runbook, control-plane specification, Domain Map, or Profile-maintenance guide.

Normally remove or replace with a short pointer:

- complete Skill routing tables or per-Skill trigger prose;
- Handoff Card/Receipt schemas and mode procedures;
- V0-V3 definitions, verification cadence, or testing procedure;
- Incident Doctor evidence/probe workflow;
- artifact-lifecycle class tables/mechanics;
- continuation, branch/worktree/PR lifecycle procedure;
- detailed Control Alignment / semantic-head / `CONTROL_ONLY_DRIFT` procedure;
- detailed Domain lists and Domain-to-source/symbol/test/runtime maps when an established Domain/navigation authority exists;
- ordered startup/read/check/navigation sequences already owned by Project Governance or project rules;
- instructions explaining what future agents should or should not put in this Profile, when to update it, or how to classify Profile content;
- copied project-specific MUST/MUST-NOT execution-rule lists already owned by `AGENTS.md`/accepted normative authority;
- current progress, current Task contract, PR/CI/release/host state;
- runtime-local model/tool/capacity values.

A short stable invariant is allowed when it materially helps orientation. Example: `Detailed Domain ownership and source/test routes live in docs/architecture/DOMAIN_MAP.md.` Do not reproduce the underlying map/procedure.

### Established Domain authority rule

If an established Domain/navigation authority already maps ownership/source/test/runtime routes:

1. point to that authority;
2. retain at most the few broad Domain distinctions required to understand the product;
3. do not create a separate `Domain Model`, ownership table, symbol list, or reduced copy of that map unless the user explicitly requests a Domain summary rather than a Project Profile.

A Profile that reproduces most Domain names or canonical source owners from an existing Domain Map fails deduplication even if those facts are correct.

### Normative-rule boundary

`Priorities / constraints` may keep concise project-specific priorities, anti-goals and risk cues. It should not restate a detailed set of operational MUST/MUST-NOT rules from `AGENTS.md`.

When a rule is needed only to govern execution, point to normative authority. Keep the Profile statement only when the underlying idea is a stable project identity/risk cue that materially helps orientation.

## Template-first compression

Use the shipped Profile template as the default shape. Prefer its existing top-level sections:

- Purpose
- Stable concepts
- Authority map
- Planning & navigation
- Environment
- Priorities / constraints
- Engineering Governance

Add another top-level section only when a stable **project-specific** context class cannot fit cleanly into these sections. Do not add a section merely because a reusable Skill, Domain Map, or Profile contract has its own concept/procedure.

In particular, generated Profiles normally do **not** add sections named or serving as:

- `Domain Model` when an established Domain Map already exists;
- `Project Profile Rule` / `Profile Maintenance` / `How to use this Profile`;
- `Workflow` / `Startup` / numbered read-order instructions.

Before returning a Profile, apply this compression check:

```text
For each paragraph/bullet:
1. Is this stable project-specific context or an authority pointer?
   YES -> candidate to keep.
2. Is it current status/task/host evidence?
   YES -> remove; point to STATUS/TASK/live evidence if needed.
3. Is it a project-specific normative execution rule?
   YES -> move/point to AGENTS or accepted normative authority; keep only a compact risk cue if it is part of stable project identity.
4. Is it reusable Engineering Governance or Profile-maintenance procedure?
   YES -> remove and replace with the shortest useful pointer/invariant.
5. Is it detailed Domain/design content already owned elsewhere?
   YES -> point to the owning authority; do not rebuild a summary map by default.
6. Does a PRIMARY/MIRROR role claim have evidence?
   NO -> use `single surface` when only one current surface is established, otherwise `UNKNOWN`.
```

A Profile should be substantially smaller than the combined authorities it indexes. Concision is semantic deduplication, not omission of project-specific facts.

## Freshness

Refresh when a profile-owned summary or pointer materially changes: project purpose, stable concepts, authority locations, durable planning/navigation entry points, stable environment roles, or durable priorities/anti-goals.

Routine schema fields, task completion, PR/CI changes, or implementation details do not trigger Profile writes unless they change one of those summaries.

When stale:

```text
AUTHORITY_WINS: YES
PROFILE_STATE: STALE
```

Read-only work reports staleness without mutation. Profile staleness alone does not invalidate a correct underlying authority.

## Context recovery

When a current Profile surface exists and is cheap/available, it may be used first as a landing index. The Profile itself should point to authorities, not reproduce the step-by-step startup procedure owned by Project Governance/project rules.

Before state-changing or authority-sensitive decisions, read the actual normative/current authorities required by Project Governance; do not treat the Profile summary as their substitute.
