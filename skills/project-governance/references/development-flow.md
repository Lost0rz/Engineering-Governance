# Business-first development flow

Use this flow for normal governed product/business engineering. It is a lifecycle, not a requirement to invoke every Skill.

## 1. Recover authority and task context

Read applicable `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and only the bounded related planning/design authority needed for the current decision. `CURRENT_TASK.md` is the single active execution authorization. Reading a source does not imply rewriting it.

When choosing a next task, consider product priority, blockers, roadmap/milestones, accepted planning context and any small still-material `CURRENT_STATUS.md / Follow-ups`. A Follow-up becomes executable only after explicit task authorization.

## 2. Establish the safe baseline

Verify only the repository/ref/revision/runtime/workspace facts needed for safe action. Use `control-identity.md` to classify literal Repository HEAD, Delivery / Semantic HEAD, provenance/transition identities, explicit equality locks and `CONTROL_ONLY_DRIFT`.

For state-changing work identify the selected workspace, working-tree/unique-work state, and any task-relevant predecessor writer with overlapping authority. Preserve unknown local work. A project-looking path, branch name or execution card does not itself prove workspace authority.

## 3. Confirm authorization

Compare the requested action with the active objective, in/out-of-scope boundary, allowed side effects, verification contract and STOP conditions. Ordinary evidence discovery within the objective does not create a new task. A material change to those task-owned semantics requires Project Governance reconciliation before affected mutation.

## 4. Resolve material design ambiguity only when needed

If implementation would require guessing about product intent, architecture, state ownership, contract/schema, responsibility boundaries or durable cross-task decisions, route to `solution-design`.

Clear local work stays in this flow. Do not invoke Solution Design merely because the request is a feature.

After design, return to Project Governance. If the accepted design changes scope, prerequisites, allowed side effects, dependency, acceptance or verification, reconcile/re-authorize `CURRENT_TASK.md` before implementation.

## 5. Resolve semantic/source route only when unclear

Use `domain-navigation` when the responsible Domain/capability, accepted semantic authority, source location, symbol, runtime entry, dependency or relevant test cannot be established safely. Reuse accepted project maps/authorities; do not require a literal `DOMAIN_MAP.md`.

Return the verified route or unresolved gap to the calling flow. Navigation does not own diagnosis or authorization.

## 6. Resolve writer/code authority

Before adding/changing a writer, backend, shared behavior, module boundary or materially new responsibility, apply `code-structure.md`. Reuse/extend/replace the canonical authority deliberately rather than creating parallel truth. File size alone is not a responsibility boundary.

If the responsibility boundary becomes unclear, return to Domain Navigation or Solution Design according to whether the uncertainty is location/authority or design choice.

## 7. Choose execution topology only when it needs policy

If one executor can safely complete the task, keep one executor.

Use `execution-orchestrator` when the authorized task materially benefits from explicit decomposition, multiple agents/roles, parallelism, model-tier selection, recovery state or controlled integration. Parallel readers are preferred over parallel writers. Multiple writers require proven-disjoint semantic authority and workspaces plus an integration check.

Orchestration never expands `CURRENT_TASK.md`.

## 8. Transfer responsibility through Agent Handoff

Whenever responsibility crosses agents, sessions, machines or execution contexts, use `agent-handoff`.

A request contains authority references + fresh delta + immediate action boundary + return contract. Do not paste complete task/status/rules into the card by default. If the receiver can read the authority, point to it.

The task's own `Handoff / current stop point` is lifecycle/authorization state. It is not the same artifact as a transport handoff request.

## 9. Implement and verify proportionally

Implement the smallest authorized outcome. Select the lightest safe `V0`–`V3` verification tier and a cadence appropriate to the construction/corrective/task/integration boundary.

During a multi-part architecture or framework build, the active task may explicitly defer expensive integrated/runtime acceptance until the architecture is frozen so long as bounded construction sanity checks prevent uncontrolled breakage. This is a cadence decision, not permission to skip final required evidence.

Universal mandatory TDD is not required. Regression-first/TDD is appropriate where behavior risk, regression history, contract changes or task requirements justify it.

## 10. Diagnose only when a blocking evidence gap exists

If a real failure/unexplained unsafe ambiguity blocks progress and current evidence cannot answer the next safe decision, enter `incident-doctor`. If existing evidence already supports the fix, stay in the current authorized delivery flow.

Doctor may use Domain Navigation to locate evidence, then resumes diagnosis. If the supported fix is outside authorization, return to Project Governance before mutation.

## 11. Obtain independent evidence verdict when needed

Use `evidence-audit` when a distinct implementation/code/PR/CI/release/merge-readiness verdict is required. Bind the audit to the exact target/range/identity and evidence freshness before saying PASS.

Audit/reviewer findings do not authorize fixes. Corrective mutation returns to Project Governance/task authorization. Read-only audit may report stale controls but must not change them solely to make the audit clean.

## 12. Merge/release host boundary

At a merge/release decision, keep semantic implementation evidence separate from live repository-host gates. Reuse semantic evidence across proven `CONTROL_ONLY_DRIFT` only when semantic equivalence and task conditions permit it. Re-read current required checks/reviews/conflicts/mergeability/merge queue/current-base/latest-head rules for the literal identity the host governs.

## 13. Reconcile controls and close out

Before a final successful governed state-changing handoff, run the mandatory Control Alignment Gate:

1. obtain fresh outcome/lifecycle evidence;
2. reread current `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
3. reread the linked durable planning/design authority when the outcome could have changed its owned semantics;
4. update only sources whose owned semantics are materially stale;
5. report document/status/task reconciliation and `CONTROL_ALIGNMENT` explicitly.

The check is mandatory; writes are conditional.

If task workspaces exist, separately reconcile physical workspace/branch disposition under `workspace-lifecycle.md`. A merge event does not by itself prove local closeout.

## Cross-skill composition

Use [Capability composition](capability-composition.md) for allowed return paths and artifact/writer boundaries. Do not create a second controller, a fourth control file, or a handoff/ledger/audit artifact that competes with project authority.
