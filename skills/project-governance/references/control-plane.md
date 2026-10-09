# Three-file control plane

The project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` have distinct owners. Keep one authoritative owner for each fact or decision class. A control may link to its source or another control, but must not copy detail in a way that creates a second authority.

| Control | Owns | Update it when | It is not |
| --- | --- | --- | --- |
| `AGENTS.md` | Durable operating rules, stable project/repository boundaries, durable workflow rules, and verified pointers to authoritative sources. | An accepted durable rule, boundary, workflow, or authoritative-source pointer changes. | A current-task log, temporary execution state, or progress history. |
| `CURRENT_STATUS.md` | A concise verified snapshot: accepted baseline and capabilities, active problems/blockers, current development state, next milestone, and freshness/verification basis. | Owned current-state facts materially change or their verification basis becomes stale. Update the snapshot in place. | Chronological history, the active task contract, an authorization override, or a second copy of detailed business/source authority. |
| `CURRENT_TASK.md` | The single active authorization: objective, affected domains, start baseline, scope, evidence, risk, verification, acceptance, stop conditions, workspace lifecycle when material, and handoff/current stop point. | Before authorized work begins and whenever its objective, scope, authorization, verification contract, workspace lifecycle expectation, handoff state, or task-owned conditions materially change. | Durable rules, business/domain truth, or a project history log. |

## Ownership and evidence

- Keep each fact or decision in the source that owns that class. Other controls may reference it and `CURRENT_STATUS.md` may summarize verified current state, but neither becomes a competing authority.
- Tie material claims to their source and revision or observation time, with a freshness basis where relevant. A claim that is stale, unavailable, or not verified stays explicitly `stale`, `unknown`, or `unresolved`; do not infer a replacement value.
- Keep `CURRENT_STATUS.md` as a current snapshot. Replace stale values when verified; do not append a timeline of past states.
- Keep the active authorization in `CURRENT_TASK.md`. If the objective or scope materially changes, stop the affected work, update the task contract, and obtain re-authorization before continuing. Ordinary evidence discovery inside the accepted objective does not by itself change the task.
- A newly verified status fact does not itself modify task authorization. If that fact changes or invalidates a `CURRENT_TASK.md` prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary, stop state-changing work and reconcile and re-authorize `CURRENT_TASK.md` before continuing. If the task-owned conditions are unaffected, the status refresh does not require a task rewrite.
- Update only the control whose owned information changed. A handoff may update task state and the status snapshot when their respective facts change; it does not grant the executor independent acceptance authority.

## Task lifecycle integrity

- Reconcile a material lifecycle event—such as merge, release, deployment, explicit human acceptance, abandonment, supersession, rollback, or invalidation of a task prerequisite—into the active task controls before any state-changing action that relies on the earlier phase.
- A task that has reached its project-defined terminal outcome no longer authorizes work under an earlier phase such as `READY_FOR_MERGE`, `WAITING_FOR_ACCEPTANCE`, or `ACTIVE_IMPLEMENTATION`. Mark it inactive and retain its historical record according to project controls; authorize a new task when the next objective or scope is new. Keep lifecycle names project-specific rather than imposing a universal status enum.
- When task branches/worktrees or equivalent workspaces are used, the terminal task event and physical workspace disposition are separate facts. Reconcile the task authorization here, and apply [Workspace lifecycle and closeout](workspace-lifecycle.md) for safe removal, explicit retention, unique-work preservation, and closeout evidence. Do not infer local closeout from a remote merge alone.
- Reconcile only when the event changes authorization, prerequisites, acceptance, STOP conditions, allowed side effects, workspace disposition, or the next action. Non-material status changes do not require control churn.
