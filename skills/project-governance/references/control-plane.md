# Mode-aware control selector

Versioned global `CONTROL_POLICY_V1` with independently verified GitHub enrollment selects exactly one task authority; `AGENTS.md` holds only project-specific facts. FILE_CONTROL retains the legacy contract below; ISSUE_CONTROL selects one approved Issue/spec revision and puts meaningful execution/decision receipts in its comments. In ISSUE_CONTROL, legacy Task/Status files are not active, Issue comments/labels are not independent authorization, and PR/CI/merge evidence remains host owned. See [Issue authority](issue-control.md), [deterministic execution](issue-execution-contract.md), and [migration](issue-control-migration.md). A mandatory Issue-mode alignment check rereads approved revision, relevant receipts and host gates; it never requires a new control-only Git PR. Missing/unverified Issue approval blocks mutation.

---

## FILE_CONTROL-only historical three-file contract

# Three-file control plane and non-control artifacts

The project-local `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` have distinct ownership. Keep one authoritative owner for each fact/decision class.

Durable planning/design authorities may exist separately when justified, but they are not a fourth control file and do not authorize execution.

## Control ownership

| Control | Owns | It is not |
| --- | --- | --- |
| `AGENTS.md` | project-specific architecture, business, runtime and data safety rules; pointers to project authorities | global mode, approver permissions, generic workflow or task progress |
| `CURRENT_STATUS.md` | concise verified current snapshot, active blockers/state, next milestone, small still-material non-blocking Follow-ups when useful | backlog DB, active authorization, delivery identity authority |
| `CURRENT_TASK.md` | single active authorization: objective/scope/baseline/risk/verification/acceptance/STOP/workspace/handoff lifecycle plus optional task-purpose metadata such as `TASK_CLASS` | durable rules, long-term plan, implementation identity |

Update only the source whose owned semantics materially changed.

`TASK_CLASS` does not create another authority. It describes the engineering purpose of the one active task when that distinction helps: DESIGN, EXECUTION, AUDIT, VERIFY, DIAGNOSIS, CORRECTIVE, CLOSEOUT, or project-equivalent.

## Task, execution unit, and execution context

Do not conflate:

- **task** — engineering objective/authorization owned by `CURRENT_TASK.md`;
- **execution unit** — bounded work inside that task, potentially delegated to a Sub Agent;
- **execution context** — Web/local/cloud/session/machine/agent/reviewer surface where work occurs.

Changing execution context does not itself change task authority. Multiple Sub Agent units do not create multiple task authorities. A materially different engineering purpose/authorization requires Project Governance reconciliation or a distinct task.

## Non-control artifact taxonomy

The following are **not** project controls by default:

- Solution Design result before its durable portion is written to an accepted planning/design authority;
- Agent Handoff request/receipt;
- execution/Sub Agent brief;
- execution recovery ledger;
- audit report/reviewer finding;
- CI/test output;
- PR/mergeability/review observation;
- runtime/probe observation.

They may carry evidence, references or a bounded request. They do not independently expand task scope, override `CURRENT_TASK.md`, redefine `CURRENT_STATUS.md`, or become a new rule source.

If a target project deliberately promotes a durable fact from such an artifact, write that fact into the source that owns that semantic class; do not treat the whole artifact as a new authority automatically.

## Evidence and identity

Tie material claims to their source/revision/observation freshness. Unsupported or stale claims remain `UNKNOWN`, `STALE` or `UNRESOLVED`.

`CURRENT_STATUS.md` / `CURRENT_TASK.md` commits are control records, not Delivery / Semantic HEAD by default. A comparison limited to those paths is `CONTROL_ONLY_DRIFT`; use `control-identity.md` for equivalence/freshness classification.

The default control-only exclusion does **not** include `AGENTS.md`, durable planning/design documents, Skill source, workflows, tests, schemas, runtime config or other implementation/governance-relevant files.

A SHA in a control/design link is provenance by default. It is an equality lock only when the task explicitly says which identity must equal it.

External evidence such as CI/test/review/audit/mergeability does not force a control write merely because it changed. Semantic evidence and live repository-host gates remain separate evidence classes.

## Handoff conflict and continuity rule

A handoff transports the current task/authority references + fresh delta across execution contexts. For same-purpose continuation, preserve the same `TASK_ID`.

When freshness matters, sender/receiver may record and compare `AUTHORITY_OBSERVED_BASIS`. A handoff never silently overrides a materially changed current authority. Compatible current authority may continue; incompatible task drift returns to Project Governance. Required authority that is unavailable and cannot be safely represented by a bounded snapshot produces a STOP, not a guess.

## Conditional FILE_CONTROL alignment

This is a FILE_CONTROL task/status reconciliation procedure, **not** a universal gate on every code edit, test, agent handoff or ISSUE_CONTROL task. Trigger it when a material FILE_CONTROL task/authorization/terminal state may have changed, or the owning project requires a final control snapshot. For an unchanged active task and routine same-purpose continuation, reuse valid state without another reconciliation pass. Writes remain conditional.

1. obtain fresh outcome/lifecycle evidence;
2. reread current `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
3. reread a linked durable design/plan when the result could have changed its owned semantics;
4. compare reality with what each source owns;
5. update only sources whose owned semantics are materially stale/incomplete;
6. report the relevant discrepancy or final outcome only when material; avoid a mandatory status-field report for a no-change continuation.

When an actual FILE_CONTROL reconciliation was required, concise evidence may use:

```text
RELATED_DOCUMENT: <path | NONE>
DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE
CURRENT_STATUS_RECONCILIATION: UPDATED | UNCHANGED
CURRENT_TASK_RECONCILIATION: UPDATED | UNCHANGED
CONTROL_ALIGNMENT: PASS
```

Absence is not equivalent to `UNCHANGED`.

### Read-only alignment

Strict read-only work may report:

```text
CONTROL_ALIGNMENT: NEEDS_RECONCILIATION
CURRENT_STATUS_ALIGNMENT: STALE | MATCH | UNKNOWN
CURRENT_TASK_ALIGNMENT: STALE | MATCH | UNKNOWN
DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

It must not mutate controls/design solely to make the audit/review clean.

## Control-only drift

When a compared revision changes only `CURRENT_STATUS.md` and/or `CURRENT_TASK.md`:

```text
CHANGE_CLASS: CONTROL_ONLY_DRIFT
DELIVERY_IDENTITY_CHANGED: NO
```

This does not by itself require task restart, new branch, semantic CI/test rerun, fresh independent audit or workspace-closeout reopen.

It also does not prove current repository-host gates pass. Re-read live checks/reviews/conflicts/mergeability/queue/current-base/latest-head requirements for the literal identity the host governs.

If control content materially changes authorization or another task-owned condition, obey the new semantics before mutation. That is an authorization effect, not evidence that application content changed.

## Post-merge control snapshot drift — defer the write, not the authorization check

A PR merge is an **external repository-host event**. A pre-merge control commit correctly records the then-current `READY_TO_MERGE` or equivalent state; it must not predeclare `MERGED`. When the host subsequently merges, GitHub's verified merge/ref evidence establishes the event even if `CURRENT_STATUS.md` / `CURRENT_TASK.md` still show the pre-merge snapshot. The old file is not current truth about that event and its former task authorization must not be reused for new product/source mutation.

At the bounded control check, distinguish these observational classifications (not a new control file, runtime mechanism, mandatory status schema or automatic write):

- **`CURRENT`** — control-owned facts and authorization match the freshest relevant evidence.
- **`POST_MERGE_DRIFT`** — a newly verified external merge/terminal event occurred *after* the controls' valid pre-event snapshot; the difference is bounded to that observed event and does not make a previously authorized action silently valid. Report the host identity and mismatch, keep any old authorization inactive, and **do not automatically open a control-only PR**.
- **`RECONCILE_BEFORE_MUTATION`** — the current controls lack valid authorization for the proposed next state-changing action, materially contradict safety/ownership/STOP conditions, or the supposed bounded external event cannot be established. STOP before product/source mutation until the owning controls are safely updated under project rules. Read-only recovery and control-authorizing reconciliation remain distinct from product implementation.

**Normal next-task carrier:** at the next *actually authorized* material development activity, read live host/ref/workspace evidence and project `AGENTS.md`, establish the new task's scope/side effects, and use the already-required normal branch/PR when needed. Its **first substantive change is a control-only commit** reconciling the preceding task's verified terminal outcome and authorizing the next task, *before* any product/source mutation. This does not create a separate `close previous task` PR, automatically create a worktree, or authorize changes directly on protected `main`. The user/project authority needed to bootstrap the next task must already be present; old terminal `CURRENT_TASK.md` is not itself new execution authorization. If no safe, permitted carrier/authorization exists, STOP and ask for that boundary rather than inventing it.

**Exceptional immediate correction:** a standalone control-only PR is justified only if an owning project/host rule explicitly requires it or a specific safety/authorization blocker must be corrected before the next normal development carrier and the user/project separately authorizes that corrective path. Do not silently bypass no-direct-main, reviews, branch protection, independent gates or exact host HEAD requirements to reduce PR count.

**Reporting and outcome:** a mandatory Control Alignment **check** does not itself mandate a control **write**, commit, branch, worktree or PR. When persistence is safely deferred, report `CONTROL_ALIGNMENT: NEEDS_RECONCILIATION`, `CONTROL_OBSERVATION: POST_MERGE_DRIFT`, the verified host evidence and the next permitted carrier/boundary; **do not** report `CONTROL_ALIGNMENT: PASS` or a current `CURRENT_TASK.md` while files are stale. Only already-current files can yield `UNCHANGED` with `PASS`. No full semantic CI/audit rerun is implied by eventual control-only reconciliation, though the literal-host gates apply when the host requires them.

## Task lifecycle integrity

- Reconcile immediately when an event changes engineering purpose, authorization, prerequisites, acceptance, STOP conditions, allowed side effects, writer authority, required workspace disposition or another task-owned fact needed for the next mutation.
- Do **not** create a new task merely because work moves to another agent/session/machine or is decomposed into Sub Agent units.
- When a design phase, execution phase, independent acceptance audit, corrective objective, or final verification is a materially distinct engineering purpose/authority boundary, represent that distinction through Project Governance task authorization rather than hiding it inside a handoff card.
- A task that reached its defined terminal outcome no longer authorizes work under an earlier state.
- Routine external evidence may remain external during execution. A successful **pre-merge** handoff must have valid task authority and accurate pre-event controls; a **post-merge external event** may be reported as bounded `POST_MERGE_DRIFT` under the dedicated rule above, with `NEEDS_RECONCILIATION` and next-product-mutation blocked until alignment. Do not claim a stale control snapshot is current or leave a different material authorization/safety conflict unresolved.
- Task terminal state and physical branch/worktree disposition are separate; use `workspace-lifecycle.md`.
- At final implementation merge gate, freeze the applicable Delivery / Semantic identity, obtain required semantic evidence, then separately read live host gates. Do not create evidence-only control commits as a prerequisite to merge.

## Next-task reconciliation fallback

If legacy/read-only/interrupted work leaves Task A terminal but controls stale, before overlapping state-changing Task B:

1. reread controls and bounded design context;
2. verify Task A's actual lifecycle/repository evidence;
3. confirm no unknown unique work, writer conflict or authorization ambiguity;
4. reconcile stale owned semantics and authorize Task B in one transition when safe.

Do not require a cosmetic intermediate closeout commit when one safe combined transition restores alignment.
