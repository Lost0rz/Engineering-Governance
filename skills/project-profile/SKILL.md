---
name: project-profile
description: Use when creating, rebuilding, shrinking, or auditing a project's compact durable context/profile so an agent can quickly understand what the project is and where authoritative facts live. Do not use for current task/status, detailed Domain-to-code mapping, or generic engineering workflow.
---

# Project Profile

Create or refresh a **derived project context/index**, not a new authority or a second governance manual.

## Boundary

A Project Profile answers: what is this project, what stable concepts/constraints matter, and where should an agent go for authoritative detail?

It must not replace project `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, detailed Domain/navigation authority, durable design/planning authority, reusable Engineering Governance Skill contracts, or implementation/runtime/host truth. If Profile text conflicts with an authority, the authority wins and the Profile is stale.

Generating or auditing Profile content may be read-only/output-only. **Writing or refreshing a repository/project-managed Profile is state-changing and requires compatible Project Governance / `CURRENT_TASK.md` authorization.** This Skill never creates that authorization by itself.

## Grounding gate

Apply source grounding before deciding whether content belongs in the Profile.

A substantive project-specific Profile claim is grounded only when it is traceable to either:

1. a current verified project authority appropriate to that claim; or
2. an explicit user instruction/reaffirmation in the current Profile task that clearly establishes or changes durable project context.

The following may help discover what to verify, but they do **not** independently ground a Profile claim:

- ChatGPT/model Memory;
- prior conversations or conversation summaries;
- previous assistant output;
- previous Project Profile or Project Instructions text;
- old task cards, handoffs, audit replies, PR prose, status summaries, or historical notes.

An existing Profile/Project Instructions surface is `DERIVED_PROJECT_CONTEXT`, not source authority. When rebuilding or auditing it, treat its substantive claims as candidates to revalidate against current authority rather than facts to inherit.

If a candidate is supported only by Memory/history/old derived context and cannot be verified, omit it from the generated Profile or keep the uncertainty outside the Profile. Do not silently promote it into durable project context.

An explicit current-task user decision may establish durable user-authorized context. If it is not yet persisted in repository authority, do not describe it as repository-established fact.

Preserve the owning project's authority semantics. Do not collapse storage, raw evidence, projections, implementation state, runtime evidence, or explicitly canonical fact classes into one universal Authority unless the current project authority actually defines that relationship.

This grounding boundary applies only to Project Profile construction/audit. It does **not** disable Memory or prevent ordinary conversation from using Memory/context normally.

## Durability gate

A grounded claim is **not automatically Profile content**. After grounding, decide whether the claim is durable enough to belong in the compact long-lived Profile.

Keep a claim only when it is expected to remain useful across ordinary task, PR, release, runtime and milestone progression, or when the owning authority explicitly establishes it as durable/version-scoped project architecture or product context.

By default, do **not** promote these grounded-but-current facts into the durable Profile:

- current task, milestone, wave, gate, MVP phase, delivery priority or immediate next step;
- current-stage non-goals, deferred work or temporary sequencing decisions that may change after the active delivery phase;
- temporary development/acceptance machine, port, endpoint, branch, worktree, runner, executable, local path or process arrangement;
- current implementation/acceptance shape such as a temporary viewer, provisional integration surface, current local runtime arrangement, or acceptance-only environment detail;
- current live status of a feature, migration, rollout, incident, release or upstream dependency.

A non-goal described by its owning authority as `current`, `current work`, `MVP`, `phase`, `wave`, `deferred`, `not yet`, or equivalent delivery-stage language is **not** a durable Profile anti-goal unless a separate durable authority establishes the same boundary as lasting product identity.

These belong in current control, live evidence, task/delivery planning or the owning runtime surface even when they are true.

Durable/version-scoped architecture may remain when the authority explicitly makes the scope durable and it materially helps orientation. Examples include an accepted V1 storage choice, a long-term Core language, a stable authority boundary, or a durable platform role. Preserve the scope (`V1`, `long-term`, etc.); do not silently turn a current MVP/wave choice into permanent project identity.

A useful test is:

```text
If the current task/milestone completed tomorrow, would this statement still belong in the Project Profile?
```

If not, point to the current/planning authority instead of copying the claim into the Profile.

## Classification workflow

After grounding and durability eligibility are established, classify each candidate item before writing:

1. current state/task -> STATUS/TASK;
2. current delivery wave/milestone/temporary runtime arrangement -> current planning/runtime authority, not Profile;
3. reusable cross-project workflow/protocol -> Engineering Governance Skill/reference, not Profile;
4. project-specific MUST/MUST-NOT execution rule -> `AGENTS.md` or accepted normative authority;
5. detailed Domain -> authority/source/test/runtime route -> Domain/navigation authority;
6. repository source/module paths, symbols and code-responsibility maps -> implementation/navigation authority, not `Environment`;
7. long-lived design rationale/work packages -> durable planning authority;
8. stable descriptive context, durable project-specific priority/anti-goal/risk cue, stable environment role, version-scoped architecture context, or authority pointer -> Project Profile.

Read only sources needed to establish the profile. Keep unknowns explicit; do not infer business truth, Profile-surface relationships, authority, durability, or stable project constraints from filenames, Memory, or unverified historical context.

## Compression gate

Before returning a Profile, remove content that merely restates reusable governance mechanics or another established project authority. In particular, a Profile normally does **not** reproduce:

- full Skill routing tables or per-Skill trigger explanations;
- Handoff Card/Receipt field schemas;
- verification-tier definitions or testing procedure;
- Incident Doctor workflow/probe procedure;
- artifact-lifecycle taxonomy/mechanics beyond a short project-relevant pointer;
- continuation/workspace/PR lifecycle procedure;
- Control Alignment or `CONTROL_ONLY_DRIFT` mechanics;
- detailed Domain lists, ownership/source/symbol/test maps already owned by an established Domain/navigation authority;
- repository directory/module/source responsibility lists when navigation authority exists;
- ordered startup/read/check workflows already owned by Project Governance or project rules;
- instructions for how to maintain, classify, refresh, ground, or write the Project Profile itself;
- copied project-specific MUST/MUST-NOT rule lists already owned by normative authority;
- unverified facts copied from Memory, prior chat, previous Profile/Project Instructions, or historical derived artifacts;
- verified but non-durable current-stage delivery/runtime/acceptance facts that belong in STATUS/TASK/planning/live evidence.

If such material is useful for orientation, replace it with one short pointer or stable invariant. Preserve only grounded **and durable** project-specific facts that materially help an agent understand this project.

## Authority-map structural rule

When a detailed Domain/navigation authority exists, the Profile's `Authority map` is a **pointer section**, not a summarized ownership model.

Required behavior:

- include the Domain/navigation authority pointer;
- keep other authority entries as concise pointers to their owning surfaces;
- do **not** append Domain-specific ownership prose, `X owns / Y owns` subsections, upstream/downstream/runtime ownership lists, source-class catalogs, route catalogs, or canonical-source inventories under `Authority map`;
- if one broad ownership distinction is essential to understand project identity, express at most one short invariant in `Purpose` or `Stable concepts`, then point to the Domain/navigation authority for detail.

An established Domain/navigation authority means the Profile should become **less** descriptive about ownership, not produce a smaller copy of the map.

## Surface-role evidence

When the target Profile surface is known, state it explicitly. Do **not** invent its relationship to another Profile surface.

Use the shipped fixed field names:

- `Profile surface: ...`
- `Primary/mirror role: ...`

Use role values:

- `MIRROR` only when a specific primary Profile surface is verified or explicitly identified by project/user authority;
- `PRIMARY` only when project/user authority explicitly designates this surface as primary/canonical among multiple Profile surfaces;
- `single surface` when this is the only established current Profile surface and no competing Profile surface is verified;
- `UNKNOWN` when the relationship cannot be established.

Do not replace `Primary/mirror role` with a different free-form metadata field such as `Profile role`.

## Output discipline

Start from `assets/templates/PROJECT_PROFILE.md` and preserve its fixed metadata field names.

- Prefer the template's existing top-level sections; add another section only when stable **project-specific** context cannot fit cleanly into them.
- Prefer concise bullets and authority pointers over explanatory procedure.
- If a detailed Domain/navigation authority exists, `Authority map` remains pointer-only. Do not add Domain ownership subsections or catalogs there. Keep at most one broad ownership invariant elsewhere only when essential to orientation.
- `Planning & navigation` contains durable pointers, not current delivery progress or a numbered engineering startup sequence.
- `Environment` contains stable project platform/environment/data-role context and authority pointers only. Do not list repository directories, module paths, source files, symbols, code owners, temporary machines/ports/endpoints, acceptance-only runtime values, or behavioral fail-closed/fallback/verification/execution rules there.
- Do not add a `Project Profile Rule`, maintenance guide, classification guide, freshness procedure, provenance ledger, durability report, or similar meta-section to the generated Profile.
- `Priorities / constraints` may contain compact grounded durable priorities, anti-goals, and risk cues; current-stage delivery priorities/non-goals and detailed normative execution rules remain in their owning authorities.
- The `Engineering Governance` section uses the shipped compact hook. Do not append per-Skill triggers, Skill catalogs, Handoff/verification/incident/PR/worktree procedure, or routing explanations unless the user explicitly requested routing documentation rather than a Project Profile.
- Keep one current Profile projection surface, or one explicit primary surface plus derived mirror; do not maintain independently edited competing Profiles.
- A Profile should be substantially smaller than the combined authorities it indexes. If it reads like a governance handbook, mini Domain Map, code map, current delivery brief, runtime acceptance note, Profile-maintenance guide, or unverified memory summary, run the gates again.

## Mandatory pre-return compliance gate

**Do not return the generated Profile until this gate passes.** This is a correction gate, not advisory prose.

For the complete draft, verify:

```text
GROUNDED: YES
DURABILITY_QUALIFIED: YES
CORRECTLY_CLASSIFIED: YES
AUTHORITY_MAP_POINTER_ONLY_WHEN_DOMAIN_AUTHORITY_EXISTS: YES
DOMAIN_AND_CODE_MAP_DEDUPED: YES
ENVIRONMENT_ROLE_ONLY: YES
ENGINEERING_GOVERNANCE_HOOK_COMPACT: YES
TEMPLATE_FIELDS_PRESERVED: YES
```

If any item is `NO` or uncertain, revise/remove the offending content in the same generation pass and run the gate again before returning the Profile.

Mandatory rejection checks:

- a stage/current/MVP/phase/wave-only non-goal appears as a permanent constraint without separate durable authority -> REMOVE;
- `Environment` contains repository-relative source/module paths, symbols, code-responsibility lists, or behavioral fail-closed/fallback/verification/execution rules -> REMOVE or reclassify only if the underlying idea is a genuinely durable Profile constraint;
- an established Domain/navigation authority exists but `Authority map` contains Domain-specific ownership prose, `X owns / Y owns` subsections, upstream/downstream/runtime ownership lists, source-class catalogs, route catalogs, or canonical-source inventories -> REMOVE all such detail; keep pointers only;
- more than one broad ownership distinction remains elsewhere despite an established detailed Domain/navigation authority -> COMPRESS to at most one short orientation invariant plus pointer;
- `Engineering Governance` contains per-Skill trigger prose or enumerates conditional Skills beyond the shipped compact hook -> REPLACE with the template hook;
- fixed metadata fields were renamed or omitted -> CORRECT before return.

The user should receive the corrected Profile, not a knowingly non-compliant draft plus an explanation of its defects.

See `references/profile-contract.md` for the full contract.

A current Profile may be used as an optional landing page for context recovery when available and cheap to read. It never removes the need to read authoritative controls/rules required for the actual decision.

Refresh only when a grounded durable profile-owned summary/pointer is materially stale.
