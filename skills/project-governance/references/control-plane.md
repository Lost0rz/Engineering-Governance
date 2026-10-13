# Three-file control plane

The project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` have distinct owners. Keep one authoritative owner for each fact or decision class. A control may link to its source or another control, but must not copy detail in a way that creates a second authority.

| Control | Owns | Update it when | It is not |
| --- | --- | --- | --- |
| `AGENTS.md` | Durable operating rules, stable project/repository boundaries, durable workflow rules, and verified pointers to authoritative sources. | An accepted durable rule, boundary, workflow, or authoritative-source pointer changes. | A current-task log, temporary execution state, or progress history. |
| `CURRENT_STATUS.md` | A concise verified snapshot: accepted baseline and capabilities, active problems/blockers, current development state, next milestone, freshness/verification basis, and—when useful—a small set of still-material non-blocking Follow-ups for future task selection. | Owned current-state facts materially change **and** the change is important enough to affect future project reasoning. Prefer batching routine lifecycle reconciliation with the next meaningful task transition rather than writing every external event immediately. | Chronological history, a backlog database, the active task contract, an authorization override, a delivery-identity authority, or a second copy of detailed business/source authority. |
| `CURRENT_TASK.md` | The single active authorization: objective, affected domains, start baseline, scope, evidence, risk, verification, acceptance, stop conditions, workspace lifecycle when material, and handoff/current stop point. | Before authorized work begins and whenever its objective, scope, authorization, verification contract, workspace lifecycle expectation, handoff state, or task-owned conditions materially change. Routine CI/review/audit/mergeability/lifecycle observations do not require a write unless they change those owned semantics. | Durable rules, business/domain truth, project history, or implementation/delivery identity. |

## Ownership and evidence

- Keep each fact or decision in the source that owns that class. Other controls may reference it and `CURRENT_STATUS.md` may summarize verified current state, but neither becomes a competing authority.
- Tie material claims to their source and revision or observation time, with a freshness basis where relevant. A claim that is stale, unavailable, or not verified stays explicitly `stale`, `unknown`, or `unresolved`; do not infer a replacement value.
- `CURRENT_STATUS.md` and `CURRENT_TASK.md` are control records, not Delivery / Semantic HEAD. A commit limited to those two paths is `CONTROL_ONLY_CHANGE`; a later Repository HEAD differing only in those paths is `CONTROL_ONLY_DRIFT`. Use [Control identity and freshness](control-identity.md) for classification and semantic-tree equivalence. The control content remains authoritative for the semantics it owns even though the commit is excluded from delivery identity.
- When a control names commits, parents, refs, or revisions, classify the semantic role before comparing them. A SHA recorded in status/task is provenance/audit evidence by default, not an implicit current-head equality lock. An explicit lock must identify, when ambiguity is possible, whether it binds Delivery / Semantic HEAD or literal Repository HEAD.
- Keep `CURRENT_STATUS.md` as a current snapshot. Replace stale values when verified; do not append a timeline of past states. A Follow-up belongs there only while it remains a current, evidence-backed, non-blocking issue worth considering in a future task decision. Preserve still-material Follow-ups through unrelated status refreshes; remove them when verified resolved, obsolete, or no longer material.
- A Follow-up in `CURRENT_STATUS.md` is not execution authorization. If selected for repair, put that work explicitly into a new or reconciled `CURRENT_TASK.md` objective/in-scope boundary before mutation. Mere selection does not itself remove the Follow-up from status.
- Keep the active authorization in `CURRENT_TASK.md`. If the objective or scope materially changes, stop the affected work, update the task contract, and obtain re-authorization before continuing. Ordinary evidence discovery inside the accepted objective does not by itself change the task.
- A newly verified status fact does not itself modify task authorization. If that fact changes or invalidates a `CURRENT_TASK.md` prerequisite, acceptance criterion, STOP condition, allowed side effect, explicit head lock, or authorization boundary, stop state-changing work and reconcile and re-authorize `CURRENT_TASK.md` before continuing. If the task-owned conditions are unaffected, the status refresh does not require a task rewrite.
- Update only the control whose owned information changed. Reading the controls at task start does not imply they must be rewritten. A handoff may update task state and the status snapshot when their respective owned facts materially need durable reconciliation; it does not grant the executor independent acceptance authority.
- CI/test results, code review, independent audit, mergeability, required status checks, required reviews, and other repository-host checks are external evidence, not control-owned facts that must always be written back. Do not create control commits solely to memorialize `CI PASS`, `audit PASS`, `merge-ready`, `merged`, or `closeout complete`. Report those from live evidence unless a genuinely durable owned fact needs reconciliation.
- Keep semantic verification evidence separate from repository-host gate state. Semantic evidence may remain valid across proven `CONTROL_ONLY_DRIFT`; host gates such as required checks/reviews, current mergeability/conflicts, merge queue, current-base, or latest-head requirements must be read from the live repository host for the literal identity the host governs.

## Control-only drift and delivery identity

A control-only commit advances literal Repository HEAD. Do not claim otherwise.

When the difference between two compared revisions is limited to `CURRENT_STATUS.md` and/or `CURRENT_TASK.md`:

```text
CHANGE_CLASS: CONTROL_ONLY_DRIFT
DELIVERY_IDENTITY_CHANGED: NO
```

That classification must not by itself trigger `STOP_HEAD_DRIFT`, task restart, new construction branch, fresh semantic CI/test run, fresh independent audit, semantic exact-head invalidation, source re-verification, or workspace-closeout reopen.

It also must not be used to infer that current repository-host merge gates remain satisfied. If the host binds a required check, review, conflict state, mergeability decision, merge-queue condition, current-base condition, or latest-head rule to the later literal identity, re-read and satisfy that live gate.

If a control-file content change materially changes authorization or another task-owned condition, obey that new content before further mutation. This is an authorization effect, not a claim that application/delivery identity changed.

Any mixed control+implementation commit, material `AGENTS.md` durable-rule change, source/config/test/workflow/schema/migration/dependency/runtime-relevant change, or other non-excluded path change is not control-only and must be evaluated as `DELIVERY_HEAD_CHANGE`.

## Task lifecycle integrity

- Reconcile a lifecycle event immediately only when the event changes authorization, prerequisites, acceptance, STOP conditions, allowed side effects, workspace disposition needed for the next action, or another task-owned decision that must be known before further mutation. The event name alone does not make it terminal; use the project/task lifecycle authority to determine its effect.
- A task that has reached its project-defined terminal outcome no longer authorizes work under an earlier phase such as `READY_FOR_MERGE`, `WAITING_FOR_ACCEPTANCE`, or `ACTIVE_IMPLEMENTATION`. Do not continue old-phase mutation merely because the control file has not yet been lazily reconciled; use fresh authoritative lifecycle evidence.
- Post-merge control reconciliation is lazy/batched by default. Do not automatically create a status/task commit merely to record that a merge or closeout occurred. When the next meaningful planning boundary arrives, one control transition may both reconcile the accepted state of Task A and authorize Task B, provided fresh evidence establishes Task A's terminal/accepted state and the new Task B authorization is otherwise valid.
- Therefore a healthy sequence may be `authorize -> implement -> verify -> audit -> merge -> next-task reconciliation`, rather than inserting control-only commits between each external lifecycle event.
- When task branches/worktrees or equivalent workspaces are used, the terminal task event and physical workspace disposition remain separate facts. Apply [Workspace lifecycle and closeout](workspace-lifecycle.md) for safe removal, explicit retention, write-capability boundaries, unique-work preservation, and closeout evidence. A later control-only main advance after verified physical closeout does not reopen that closeout.
- At a final implementation merge gate, control reconciliation must not create an evidence loop. Freeze Delivery / Semantic HEAD (or an explicitly required literal Repository HEAD), establish the required semantic evidence, then read the current repository-host gate state separately. A later control-only Repository HEAD advance is non-invalidating for semantic implementation evidence when semantic-tree equivalence passes and no task-owned condition invalidates that evidence; any host requirement bound to the current literal PR/head/base still must pass before merge.

## Next-task reconciliation pattern

When Task A is already verified merged/terminal but controls still describe its last authorized state and the user selects Task B:

1. read `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
2. verify fresh repository/lifecycle evidence for Task A;
3. confirm no unresolved authorization, unique-work, predecessor-writer, or other safety condition blocks the transition;
4. perform one control transition that records the accepted current state as needed and authorizes Task B.

Do not require an intermediate “close Task A” commit merely to make the control files cosmetically current before the Task B authorization commit.
