# Engineering Governance v0.5.0 — Navigation Refresh and Lightweight Follow-ups

> Integration note (2026-10-10): this document remains the accepted design authority for the Navigation Refresh + Lightweight Follow-ups capability. Project Storage Affinity is integrated alongside it by `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049` and does not replace the semantics below.

## Intent

v0.5.0 solves only two recurring problems:

1. A task discovers that an accepted navigation projection is inaccurate, incomplete, or stale; after the correct route is verified, the useful projection should become more accurate instead of forcing the same rediscovery later.
2. A task discovers a small evidence-backed problem that should not interrupt the current objective; the project should remember it long enough to consider it during the next-task decision.

The version deliberately does **not** introduce a general Findings platform, external tracker adapter, background process, scheduler, database, new Skill, or new control file.

## Architecture invariants

The Plugin remains exactly three top-level Skills:

1. `project-governance`
2. `domain-navigation`
3. `incident-doctor`

The managed global Router remains selection-only and semantically unchanged.

The project control plane remains exactly:

- `AGENTS.md` — durable project rules and authority pointers;
- `CURRENT_STATUS.md` — concise verified current state, including a small optional Follow-ups section;
- `CURRENT_TASK.md` — the only active execution authorization.

A navigation projection remains derived routing evidence, never semantic/product truth or task authorization.

---

# Part A — Navigation gets more accurate through use

## Goal

When Domain Navigation or normal governed work verifies that an accepted navigation projection is inaccurate, incomplete, stale, or materially changed, update only the affected routing claim after the correct route is established.

The basic loop is:

`use existing route -> verify needed evidence -> route is wrong/incomplete/changed -> establish correct route -> update affected projection claim -> continue`

## Rules

1. Reuse accepted semantic authorities and existing navigation projections before searching broadly.
2. Verify only the route facts needed for the current task.
3. If the existing route is correct, do not rewrite it merely to record another confirmation.
4. If the existing route is proven wrong, incomplete, stale, or changed and the replacement is verified, update only the affected entry/fields.
5. Maintaining the directly affected claim in an **already accepted derived navigation projection** is normal governance-evidence reconciliation during authorized state-changing work; it does not expand product scope and does not require a per-task permission line merely for that bounded map maintenance. Strict read-only mode or an explicit project/task rule forbidding governance/metadata writes still prevents the mutation.
6. If the old route is proven unsafe but the replacement is still unresolved, keep that uncertainty explicit; do not invent a replacement.
7. Never mark an entire map fresh because one route was checked.
8. Never scan or rebuild the whole repository map merely because one route changed.
9. Do not create a new repository-wide map by default. v0.5 primarily improves an accepted projection that already exists or is already justified by the current task.
10. During strict read-only work, report the verified navigation correction as a candidate but do not mutate the projection.

## Ownership

- `skills/domain-navigation/references/mapping-workflow.md` owns focused route discovery and the verified routing result.
- `skills/domain-navigation/references/refresh-policy.md` owns when and how an affected navigation claim is refreshed.
- Project Governance owns the surrounding task flow and may apply the affected-only refresh contract after normal state-changing work changes a known route without needing Domain Navigation to rediscover an already-clear route.

No `learning-loop.md` is introduced.

---

# Part B — Small adjacent problems become lightweight Follow-ups

## What belongs in Follow-ups

A Follow-up is a problem discovered during current work that is:

- supported by concrete evidence;
- outside the current task's objective or not worth interrupting it for;
- non-blocking for the current task;
- material enough that a future task decision should consider it.

Examples include a stale documentation pointer, a small inconsistency, a bounded cleanup that matters, or a related defect that is understood but not part of the current objective.

Do not record:

- unsupported suspicions;
- generic refactoring wishes;
- naming/style preferences with no material consequence;
- low-value observations;
- a problem that actually blocks safe continuation of the current task.

A current-task blocker stays in the normal Project Governance/current-control flow; it is not a Follow-up.

## Where Follow-ups live

Use a small optional `## Follow-ups` section in `CURRENT_STATUS.md`.

Each retained item needs only enough information to support a future decision:

- area or Domain;
- concise problem;
- why it may matter;
- evidence/revision basis.

A short stable label may be used when useful for reference, but no global ID system is required.

`CURRENT_STATUS.md` remains a current snapshot, not a history log or backlog database. Keep only Follow-ups that still materially deserve future consideration. An unrelated status refresh must preserve a still-material Follow-up; do not drop it merely because another status fact changed.

## Discovery during normal work

During normal state-changing governed work:

1. finish the current authorized objective rather than opportunistically fixing an adjacent issue;
2. if the adjacent issue qualifies as a Follow-up, add or refresh one concise item in `CURRENT_STATUS.md` as part of normal status reconciliation;
3. do not expand `CURRENT_TASK.md` merely because the Follow-up was discovered;
4. do not fix the Follow-up unless the active task already authorizes that work or the task is explicitly re-scoped.

No separate Finding-write permission, selector contract, lifecycle state machine, external tracker mapping, or duplicate-query framework is introduced.

If an equivalent Follow-up is already present, update the existing item only when the new evidence materially improves or changes it; otherwise do not create duplicate status noise.

## Strict read-only work

A strict read-only task does not modify `CURRENT_STATUS.md`.

If it discovers a useful adjacent issue, report a concise **Follow-up candidate** in the result. A later normal planning/state-changing flow may decide whether it belongs in `CURRENT_STATUS.md`.

No durability guarantee is made for a read-only candidate until it is deliberately carried into project controls.

## Next-task selection

When deciding what to do next, Project Governance considers the small `CURRENT_STATUS.md / Follow-ups` section together with product priorities, current blockers, roadmap/milestones, and other accepted project state.

For each relevant Follow-up, choose only what the current decision needs:

- **merge with the next task** when it is closely related and does not materially distort the next task's objective/risk;
- **leave it in Follow-ups** when it still matters but should remain separate;
- **make it a separate future task** when it deserves dedicated scope;
- **remove it from Follow-ups** when current evidence shows it was resolved, became obsolete, or no longer materially matters.

If a Follow-up is selected for execution, place that work explicitly inside the new `CURRENT_TASK.md` objective/in-scope authorization. Selection alone does not remove the Follow-up from current status; remove it only after current evidence shows it is resolved, obsolete, or no longer material. Presence in `CURRENT_STATUS.md` never authorizes mutation by itself.

No Follow-up history needs to be preserved in the control file; Git history already provides document history.

---

# Relationship to the existing normal flow

The mechanism must remain lightweight:

1. normal project work still enters through Project Governance;
2. Domain Navigation is used only when the route is actually unclear/stale/insufficient;
3. after route verification, an existing useful projection may receive the bounded correction;
4. after normal task work, Project Governance may add/remove/update a concise Follow-up while reconciling current status;
5. next-task selection checks the current Follow-ups section once as part of reading `CURRENT_STATUS.md`—there is no separate registry query.

No project that lacks Follow-ups incurs extra lookup machinery beyond the status read that Project Governance already performs.

---

# Implementation scope

## Domain Navigation

Modify only as needed:

- `skills/domain-navigation/SKILL.md`
- `skills/domain-navigation/references/mapping-workflow.md`
- `skills/domain-navigation/references/refresh-policy.md`
- `skills/domain-navigation/assets/templates/DOMAIN_MAP.md`

Do not add a new navigation subsystem or map updater runtime.

## Project Governance

Modify only as needed:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`

Do not create `FINDINGS.md` or a new project control file. Do not add external tracker integration.

## Repository metadata

- update `README.md` concisely;
- set `plugin.json` to `0.5.0` only when freezing the reusable candidate;
- keep global routing semantics unchanged;
- do not migrate target product projects as part of this implementation.

---

# Acceptance criteria

The implementation is accepted when all are true:

1. A verified correction to an existing navigation projection updates only the affected route/fields.
2. Correct unchanged routes do not churn.
3. Unresolved routes remain explicit rather than guessed.
4. Strict read-only navigation never mutates the projection.
5. A material non-blocking adjacent issue discovered during normal state-changing work can be retained as a concise `CURRENT_STATUS.md / Follow-ups` item without expanding the active task.
6. A current blocker is not parked as a Follow-up.
7. Strict read-only work may report a Follow-up candidate but does not modify status.
8. Next-task selection considers current Follow-ups together with normal business priorities.
9. A Follow-up selected for execution becomes explicit `CURRENT_TASK.md` scope before mutation.
10. Still-material Follow-ups survive unrelated status refreshes and selection alone does not erase them.
11. Resolved/obsolete Follow-ups can be removed rather than accumulating history.
12. No fourth Skill/control file, Findings registry, external tracker adapter, scheduler, daemon, database, automatic repair, or repository-wide mapping requirement is introduced.

---

# Non-goals

v0.5.0 does **not** implement:

- a general Findings lifecycle such as `OPEN/PROMOTED/CLOSED`;
- a `FINDINGS.md` registry;
- GitHub Issues/backlog adapters;
- selector/query abstractions;
- background or scheduled review;
- durable history beyond normal Git history;
- automatic repair of adjacent problems;
- mandatory creation of a Domain map when none exists;
- whole-repository remapping;
- target-project migration.

Those can be reconsidered later only if real usage shows the lightweight model is insufficient.
