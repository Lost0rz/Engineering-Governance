# Three-file control plane

The project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` have distinct owners. Keep one authoritative owner for each fact or decision class. A control may link to its source or another control, but must not copy detail in a way that creates a second authority.

| Control | Owns | Update it when | It is not |
| --- | --- | --- | --- |
| `AGENTS.md` | Durable operating rules, stable project/repository boundaries, durable workflow rules, and verified pointers to authoritative sources. | An accepted durable rule, boundary, workflow, or authoritative-source pointer changes. | A current-task log, temporary execution state, or progress history. |
| `CURRENT_STATUS.md` | A concise verified snapshot: accepted baseline and capabilities, active problems/blockers, current development state, next milestone, freshness/verification basis, and—when useful—a small set of still-material non-blocking Follow-ups for future task selection. | Owned current-state facts materially change. Reconcile those changed facts at governed task closeout rather than intentionally leaving the snapshot stale for a later task. | Chronological history, a backlog database, the active task contract, an authorization override, a delivery-identity authority, or a second copy of detailed business/source authority. |
| `CURRENT_TASK.md` | The single active authorization: objective, affected domains, start baseline, scope, evidence, risk, verification, acceptance, stop conditions, workspace lifecycle when material, and handoff/current stop point. | Before authorized work begins and whenever its objective, scope, authorization, verification contract, workspace lifecycle expectation, actual execution/handoff/blocked/terminal state, or task-owned conditions materially change. Reconcile the actual stop point at governed task closeout. | Durable rules, business/domain truth, project history, or implementation/delivery identity. |

## Ownership and evidence

- Keep each fact or decision in the source that owns that class. Other controls may reference it and `CURRENT_STATUS.md` may summarize verified current state, but neither becomes a competing authority.
- Tie material claims to their source and revision or observation time, with a freshness basis where relevant. A claim that is stale, unavailable, or not verified stays explicitly `stale`, `unknown`, or `unresolved`; do not infer a replacement value.
- `CURRENT_STATUS.md` and `CURRENT_TASK.md` are control records, not Delivery / Semantic HEAD. A commit limited to those two paths is `CONTROL_ONLY_CHANGE`; a later Repository HEAD differing only in those paths is `CONTROL_ONLY_DRIFT`. Use [Control identity and freshness](control-identity.md) for classification and semantic-tree equivalence. The control content remains authoritative for the semantics it owns even though the commit is excluded from delivery identity.
- When a control names commits, parents, refs, or revisions, classify the semantic role before comparing them. A SHA recorded in status/task is provenance/audit evidence by default, not an implicit current-head equality lock. An explicit lock must identify, when ambiguity is possible, whether it binds Delivery / Semantic HEAD or literal Repository HEAD.
- Keep `CURRENT_STATUS.md` as a current snapshot. Replace stale values when verified; do not append a timeline of past states. A Follow-up belongs there only while it remains a current, evidence-backed, non-blocking issue worth considering in a future task decision. Preserve still-material Follow-ups through unrelated status refreshes; remove them when verified resolved, obsolete, or no longer material.
- A Follow-up in `CURRENT_STATUS.md` is not execution authorization. If selected for repair, put that work explicitly into a new or reconciled `CURRENT_TASK.md` objective/in-scope boundary before mutation. Mere selection does not itself remove the Follow-up from status.
- Keep the active authorization and actual current stop point in `CURRENT_TASK.md`. If the objective or scope materially changes, stop the affected work, update the task contract, and obtain re-authorization before continuing. Ordinary evidence discovery inside the accepted objective does not by itself change the task.
- A newly verified status fact does not itself modify task authorization. If that fact changes or invalidates a `CURRENT_TASK.md` prerequisite, acceptance criterion, STOP condition, allowed side effect, explicit head lock, or authorization boundary, stop state-changing work and reconcile and re-authorize `CURRENT_TASK.md` before continuing. If the task-owned conditions are unaffected, the status refresh does not require an authorization rewrite; closeout may still need to update the task's actual handoff/blocked/terminal state.
- Update only the control whose owned information changed. Reading the controls at task start does not imply they must be rewritten. The mandatory closeout rule is a reconciliation check, not a requirement to manufacture no-op edits.
- CI/test results, code review, independent audit, mergeability, required status checks, required reviews, and other repository-host checks are external evidence, not chronological control history. Do not create a control commit solely to memorialize `CI PASS`, `audit PASS`, `merge-ready`, `merged`, or `closeout complete`. When that evidence changes a control-owned current-state fact—such as the accepted capability state, active blocker, task handoff, workspace disposition, terminal state, or next milestone—write the resulting current state, not the event log.
- Keep semantic verification evidence separate from repository-host gate state. Semantic evidence may remain valid across proven `CONTROL_ONLY_DRIFT`; host gates such as required checks/reviews, current mergeability/conflicts, merge queue, current-base, or latest-head requirements must be read from the live repository host for the literal identity the host governs.

## Mandatory task closeout reconciliation

Every governed task/session that reaches a handoff or completion boundary must perform a control-reconciliation check before reporting itself fully closed.

For normal state-changing work:

1. re-read the task-relevant repository, branch/ref, Delivery / Semantic HEAD when relevant, working-tree/workspace state, live lifecycle/host evidence needed for the claim, and the current controls;
2. determine whether `CURRENT_STATUS.md` owns any materially changed current-state fact;
3. determine whether `CURRENT_TASK.md` owns any materially changed task state, handoff/current stop point, authorization condition, workspace disposition, blocker, or terminal outcome;
4. reconcile every changed owned fact before the final closeout receipt;
5. verify that the resulting controls describe the actual current state and do not preserve an obsolete earlier execution phase merely because the implementation already finished.

A state-changing execution that materially advances a task normally changes at least its current stop/handoff state. If it does, `CURRENT_TASK.md` must be reconciled. If the accepted project/delivery snapshot, blocker set, capability state, active development state, or next milestone also changed, reconcile `CURRENT_STATUS.md` as well.

Strict read-only work remains read-only. It must still perform the reconciliation check. If current evidence proves a control materially stale but mutation is prohibited, report the needed reconciliation explicitly as blocked/read-only; do not silently present stale controls as current and do not claim full control closeout.

A concise final governed receipt should expose the result, for example:

```text
CONTROL_RECONCILIATION: PASS | NOT_REQUIRED | BLOCKED_READ_ONLY
CURRENT_STATUS: UPDATED | NOT_REQUIRED | BLOCKED
CURRENT_TASK: UPDATED | NOT_REQUIRED | BLOCKED
```

A project may add `SKILLS_USED`, merge state, final heads, changed paths, or other receipt fields, but those do not replace the reconciliation result.

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

- Reconcile a lifecycle event immediately when it changes authorization, prerequisites, acceptance, STOP conditions, allowed side effects, workspace disposition needed for the next action, or another task-owned decision that must be known before further mutation.
- Independently of that immediate-safety rule, reconcile materially changed control-owned state at the next governed handoff/closeout boundary. Do not intentionally defer a known stale current task/status snapshot to a later unrelated planning task merely to avoid a control-only commit.
- A task that has reached its project-defined terminal outcome no longer authorizes work under an earlier phase such as `READY_FOR_MERGE`, `WAITING_FOR_ACCEPTANCE`, or `ACTIVE_IMPLEMENTATION`. Reconcile the terminal/current stop point before claiming full task closeout when writes are authorized.
- A merge or other named event is not terminal by name alone; use the project/task lifecycle authority to determine the actual state. Once the state is verified, write its control-owned consequence at closeout instead of copying the raw event history.
- When task branches/worktrees or equivalent workspaces are used, the terminal task event and physical workspace disposition remain separate facts. Apply [Workspace lifecycle and closeout](workspace-lifecycle.md) for safe removal, explicit retention, write-capability boundaries, unique-work preservation, and closeout evidence. A later control-only main advance after verified physical closeout does not reopen that closeout.
- At a final implementation merge gate, control reconciliation must not create an evidence loop. Freeze Delivery / Semantic HEAD (or an explicitly required literal Repository HEAD), establish the required semantic evidence, then read the current repository-host gate state separately. A later control-only Repository HEAD advance is non-invalidating for semantic implementation evidence when semantic-tree equivalence passes and no task-owned condition invalidates that evidence; any host requirement bound to the current literal PR/head/base still must pass before merge.
- If repository-host policy requires fresh host checks on a later control-only literal head, satisfy that host rule without reclassifying the control-only commit as an implementation change.

A healthy state-changing sequence is therefore:

```text
authorize
-> implement
-> verify
-> audit / host gate as required
-> merge / handoff / terminal decision as applicable
-> reconcile changed CURRENT_STATUS / CURRENT_TASK facts
-> final closeout receipt
```

The reconciliation step may occur on the task branch before handoff, on the accepted integration branch after a terminal merge, or at another project-authorized closeout point. The requirement is semantic: do not knowingly leave materially stale writable controls after claiming the task is fully closed.

## Recovery pattern for pre-existing stale controls

If Task A is already verified terminal but controls still describe an obsolete earlier state because an older workflow deferred reconciliation:

1. read `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
2. verify fresh repository/lifecycle evidence for Task A;
3. confirm no unresolved authorization, unique-work, predecessor-writer, or other safety condition blocks reconciliation;
4. reconcile Task A's accepted current state before relying on those controls for Task B;
5. Task B may be authorized in the same control transition when that combined transition is clear and safe.

Do not require two cosmetic control commits when one reconciliation can both close the stale prior state and authorize the next task. This recovery optimization does not make intentional post-task staleness the normal workflow.
