# Three-file control plane

The project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` have distinct owners. Keep one authoritative owner for each fact or decision class. A control may link to its source or another control, but must not copy detail in a way that creates a second authority.

Durable planning documents are separate planning authorities, not a fourth control file. Use [Durable planning documents and task linkage](planning-documents.md) when long-lived design or a multi-task / large-PR plan is justified.

| Control | Owns | Update it when | It is not |
| --- | --- | --- | --- |
| `AGENTS.md` | Durable operating rules, stable project/repository boundaries, durable workflow rules, and verified pointers to authoritative sources. | An accepted durable rule, boundary, workflow, or authoritative-source pointer changes. | A current-task log, temporary execution state, progress history, or detailed long-term plan. |
| `CURRENT_STATUS.md` | A concise verified snapshot: accepted baseline and capabilities, active problems/blockers, current planning/development state, next milestone, freshness/verification basis, and—when useful—a small set of still-material non-blocking Follow-ups for future task selection. | Owned current-state facts materially change. Routine external evidence alone does not require a write, but final governed handoff must not leave status-owned semantics materially stale. | Chronological history, a backlog database, the active task contract, an authorization override, a delivery-identity authority, detailed planning document, or a second copy of business/source authority. |
| `CURRENT_TASK.md` | The single active authorization: objective, optional planning-context link, affected domains, start baseline, scope, evidence, risk, verification, acceptance, stop conditions, workspace lifecycle when material, and handoff/current stop point. | Before authorized work begins and whenever its objective, scope, authorization, verification contract, workspace lifecycle expectation, handoff state, or task-owned conditions materially change. Final governed handoff must reconcile task-owned lifecycle/handoff semantics when they would otherwise be stale. | Durable rules, long-term plan, business/domain truth, project history, or implementation/delivery identity. |

## Ownership and evidence

- Keep each fact or decision in the source that owns that class. Other controls may reference it and `CURRENT_STATUS.md` may summarize verified current state, but neither becomes a competing authority.
- Tie material claims to their source and revision or observation time, with a freshness basis where relevant. A claim that is stale, unavailable, or not verified stays explicitly `stale`, `unknown`, or `unresolved`; do not infer a replacement value.
- `CURRENT_STATUS.md` and `CURRENT_TASK.md` are control records, not Delivery / Semantic HEAD. A commit limited to those two paths is `CONTROL_ONLY_CHANGE`; a later Repository HEAD differing only in those paths is `CONTROL_ONLY_DRIFT`. Use [Control identity and freshness](control-identity.md) for classification and semantic-tree equivalence. The control content remains authoritative for the semantics it owns even though the commit is excluded from delivery identity.
- The default control-only exclusion does **not** include `AGENTS.md`, planning documents, Skill source, workflows, tests, schemas, runtime config, or other governance/implementation-relevant content.
- When a control or planning link names commits, parents, refs, or revisions, classify the semantic role before comparing them. A SHA recorded in status/task or as a planning-document revision basis is provenance/audit evidence by default, not an implicit current-head equality lock. An explicit lock must identify, when ambiguity is possible, whether it binds Delivery / Semantic HEAD or literal Repository HEAD.
- Keep `CURRENT_STATUS.md` as a current snapshot. Replace stale owned values when verified; do not append a timeline of past states. A Follow-up belongs there only while it remains a current, evidence-backed, non-blocking issue worth considering in a future task decision. Preserve still-material Follow-ups through unrelated status refreshes; remove them when verified resolved, obsolete, or no longer material.
- A Follow-up in `CURRENT_STATUS.md` is not execution authorization. If selected for repair, put that work explicitly into a new or reconciled `CURRENT_TASK.md` objective/in-scope boundary before mutation. Mere selection does not itself remove the Follow-up from status.
- Keep the active authorization in `CURRENT_TASK.md`. If the objective or scope materially changes, stop the affected work, update the task contract, and obtain re-authorization before continuing. Ordinary evidence discovery inside the accepted objective does not by itself change the task.
- A newly verified status or planning fact does not itself modify task authorization. If that fact changes or invalidates a `CURRENT_TASK.md` prerequisite, scope, acceptance criterion, STOP condition, allowed side effect, dependency, explicit head lock, or authorization boundary, stop state-changing work and reconcile and re-authorize `CURRENT_TASK.md` before continuing.
- Update only the source whose owned information changed. Reading controls or a linked planning document does not imply rewriting them.
- CI/test results, code review, independent audit, mergeability, required status checks, required reviews, and other repository-host checks are external evidence, not control-owned facts that must always be written back. Do not create control commits solely to memorialize `CI PASS`, `audit PASS`, `merge-ready`, a run identifier, or another external observation when no owned control semantic changed.
- Keep semantic verification evidence separate from repository-host gate state. Semantic evidence may remain valid across proven `CONTROL_ONLY_DRIFT`; host gates such as required checks/reviews, current mergeability/conflicts, merge queue, current-base, or latest-head requirements must be read from the live repository host for the literal identity the host governs.

## Mandatory Control Alignment Gate

Every governed **state-changing** execution must perform a Control Alignment Gate before claiming a final successful handoff such as `PASS`, `COMPLETE`, `CLOSED`, `MERGED`, `RELEASED`, or a project-equivalent terminal/retained-success state.

The **check is mandatory; writes are conditional**.

At the gate:

1. obtain fresh evidence for the actual execution outcome and any material lifecycle state;
2. reread the active `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
3. when the task links a durable planning document and the outcome could affect durable design assumptions, reread that document as well;
4. compare reality with the semantics each source owns;
5. update only sources whose owned semantics are now materially inaccurate or incomplete;
6. report the alignment result explicitly in the final receipt.

Use the semantic equivalents of:

```text
RELATED_DOCUMENT: <path | NONE>
DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE
CURRENT_STATUS_RECONCILIATION: UPDATED | UNCHANGED
CURRENT_TASK_RECONCILIATION: UPDATED | UNCHANGED
CONTROL_ALIGNMENT: PASS
```

Absence of a field/result is not equivalent to `UNCHANGED`. A successful state-changing handoff may not silently omit the alignment check.

A short reason is useful when a source was updated or when an unchanged result would otherwise be surprising.

### What may remain lazy/batched

Routine **external evidence recording** may remain lazy/batched. For example, an individual CI success, review approval, audit result, mergeability observation, or workflow run does not force a control write when it does not change control-owned semantics.

Lazy/batched external evidence recording must **not** be used to leave control-owned state stale past the final governed handoff boundary. If the execution materially changes task lifecycle/handoff, accepted project baseline/capability, active blocker, current planning/work-package position, current development state, or next milestone, reconcile the owning control before final successful handoff.

This preserves low control-file noise without allowing cross-session/cross-machine readers to inherit an obsolete task/status snapshot.

### Read-only alignment

Strict read-only work may assess alignment but must not mutate controls or planning documents merely to make them current. Report mismatches explicitly, for example:

```text
CONTROL_ALIGNMENT: NEEDS_RECONCILIATION
CURRENT_STATUS_ALIGNMENT: STALE
CURRENT_TASK_ALIGNMENT: MATCH
DOCUMENT_ALIGNMENT: UNCHANGED
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

The next authorized state-changing transition must reconcile a material stale control before relying on the stale semantic for further mutation.

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

Any mixed control+implementation commit, material `AGENTS.md` durable-rule change, planning-document change, source/config/test/workflow/schema/migration/dependency/runtime-relevant change, or other non-excluded path change is not control-only and must be evaluated as `DELIVERY_HEAD_CHANGE`.

## Task lifecycle integrity

- Reconcile a lifecycle event immediately when it changes authorization, prerequisites, acceptance, STOP conditions, allowed side effects, workspace disposition needed for the next action, or another task-owned decision that must be known before further mutation.
- A task that has reached its project-defined terminal outcome no longer authorizes work under an earlier phase such as `READY_FOR_MERGE`, `WAITING_FOR_ACCEPTANCE`, or `ACTIVE_IMPLEMENTATION`.
- Do not write controls after every external lifecycle event merely because the event occurred. Instead, preserve live evidence during execution and apply the mandatory Control Alignment Gate at final state-changing handoff.
- A healthy sequence is therefore `authorize -> implement -> verify -> audit -> merge/accept/release as applicable -> closeout/alignment -> receipt`, without inserting evidence-only control commits between every external event.
- When task branches/worktrees or equivalent workspaces are used, the terminal task event and physical workspace disposition remain separate facts. Apply [Workspace lifecycle and closeout](workspace-lifecycle.md) for safe removal, explicit retention, write-capability boundaries, unique-work preservation, and closeout evidence. A later control-only main advance after verified physical closeout does not reopen that closeout.
- At a final implementation merge gate, control reconciliation must not create an evidence loop. Freeze Delivery / Semantic HEAD (or an explicitly required literal Repository HEAD), establish required semantic evidence, then read current repository-host gate state separately. A later control-only Repository HEAD advance is non-invalidating for semantic implementation evidence when semantic-tree equivalence passes and no task-owned condition invalidates that evidence; any host requirement bound to the current literal PR/head/base still must pass before merge.

## Next-task reconciliation pattern

When Task A is already verified terminal and its final Control Alignment Gate left controls accurate, Task B starts from those controls normally.

If legacy or read-only evidence shows Task A is terminal but controls remain stale, then before Task B performs overlapping state-changing work:

1. read `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
2. verify fresh repository/lifecycle evidence for Task A;
3. confirm no unresolved authorization, unique-work, predecessor-writer, or other safety condition blocks the transition;
4. reconcile the stale owned control semantics and authorize Task B in one transition when safe.

Do not require a cosmetic intermediate closeout commit when one combined transition can safely restore alignment and authorize the next task. This fallback does not weaken the normal requirement that a state-changing executor perform the alignment gate before its own final successful handoff.
