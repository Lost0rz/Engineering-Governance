# Business-first development flow

Use this flow for normal governed product/business engineering. It is a lifecycle, not a requirement to invoke every Skill or create a new task for every phase.

## 1. Recover authority, task purpose, and planning context

Read applicable `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and only the bounded related planning/design authority needed for the current decision. `CURRENT_TASK.md` is the single active execution authorization. Reading a source does not imply rewriting it.

When useful, interpret `TASK_CLASS` as the current engineering purpose: DESIGN, EXECUTION, AUDIT, VERIFY, DIAGNOSIS, CORRECTIVE, CLOSEOUT, or project-equivalent. This metadata does not create a second authority.

A written accepted solution/design is planning context for execution. Executors should reference it rather than re-derive the solution from chat history.

## 2. Distinguish task, execution unit, and context

- **Task** — engineering objective/authorization.
- **Execution unit** — bounded work inside the task, possibly delegated to a Sub Agent.
- **Execution context** — Web/local/cloud/subagent/session/machine/reviewer surface.

Changing execution context does not by itself create a new task. Multiple Sub Agent units under one execution objective remain one task.

## 3. Establish the safe baseline

Verify only the repository/ref/revision/runtime/workspace facts needed for safe action. Use `control-identity.md` to classify literal Repository HEAD, Delivery / Semantic HEAD, provenance/transition identities, explicit equality locks and `CONTROL_ONLY_DRIFT`.

For state-changing work identify the selected workspace, working-tree/unique-work state, and any task-relevant predecessor writer with overlapping authority. Preserve unknown local work. A project-looking path, branch name or execution card does not itself prove workspace authority.

## 4. Confirm authorization and task boundary

Compare the requested action with the active objective, in/out-of-scope boundary, allowed side effects, verification contract and STOP conditions.

Keep the same task when the engineering purpose and authorization are materially unchanged across:

- Web/local/session/machine continuation;
- controller-to-Sub-Agent delegation;
- sequential or parallel work units;
- implementation-local verification supporting the task's own acceptance criteria.

Reconcile or create a distinct task when engineering purpose/authorization materially changes, for example a separately commissioned independent acceptance audit, a distinct corrective objective after findings, or a new design decision that changes scope/interfaces/side effects/writer authority.

## 5. Resolve material design ambiguity only when needed

If implementation would require guessing about product intent, architecture, state ownership, contract/schema, responsibility boundaries or durable cross-task decisions, route to `solution-design`.

Clear local work stays in this flow. Do not invoke Solution Design merely because the request is a feature.

After design, return to Project Governance. If the accepted design changes scope, prerequisites, allowed side effects, dependency, acceptance or verification, reconcile/re-authorize `CURRENT_TASK.md` before implementation. If design was a separately authorized purpose, a later execution task may reference that accepted design directly.

## 6. Resolve semantic/source route only when unclear

Use `domain-navigation` when the responsible Domain/capability, accepted semantic authority, source location, symbol, runtime entry, dependency or relevant test cannot be established safely. Reuse accepted project maps/authorities; do not require a literal `DOMAIN_MAP.md`.

Return the verified route or unresolved gap to the calling flow. Navigation does not own diagnosis or authorization.

## 7. Resolve writer/code authority

Before adding/changing a writer, backend, shared behavior, module boundary or materially new responsibility, apply `code-structure.md`. Reuse/extend/replace the canonical authority deliberately rather than creating parallel truth. File size alone is not a responsibility boundary.

If the responsibility boundary becomes unclear, return to Domain Navigation or Solution Design according to whether the uncertainty is location/authority or design choice.

## 8. Use execution topology to improve effective throughput

Use `execution-orchestrator` when the authorized task benefits from decomposition, multiple agents/roles, parallelism, delegated-model policy, recovery state or controlled integration.

Do not treat minimum agent count as the goal. If independent work units can safely run concurrently and concurrency materially improves throughput or context isolation, use available parallel capacity. Parallel readers/researchers/reviewers are often cheap to separate; parallel writers still require proven-disjoint semantic authority/workspaces plus an integration boundary.

During the current v0.6.0 stabilization period, delegated Sub Agents follow `ENVIRONMENT_DEFAULT_ONLY`. Each delegated execution context resolves its own authoritative Sub Agent configuration/runtime default. Do not propagate concrete model/reasoning values from another context or infer an unobservable platform default. Do not switch a delegated unit to a stronger model merely because the work becomes harder; return a capability/environment gap to the controller if the current environment default is insufficient.

One inline executor remains correct when decomposition provides no material benefit or dependencies/shared state make concurrency inefficient or unsafe.

Orchestration never expands `CURRENT_TASK.md`.

## 9. Transfer responsibility through context-neutral Agent Handoff

Whenever responsibility crosses agents, sessions, machines or execution contexts, use `agent-handoff`.

A same-task continuation preserves the same `TASK_ID` and references the same task/design authorities. The request carries authority references + fresh delta + immediate action boundary + return contract. It may record source/target context when useful, but Web/local identity does not define task purpose.

Under environment-owned delegated-model policy, handoff carries the policy only. It does not make the sender's concrete model/reasoning configuration authoritative for the receiver.

Do not paste complete task/status/rules into the card by default. If the receiver can read the authority, point to it. The task's own `Handoff / current stop point` is lifecycle/authorization state, not a transport card.

## 10. Implement and verify proportionally

Implement the smallest authorized outcome. Select the lightest safe `V0`–`V3` verification tier and a cadence appropriate to the construction/corrective/task/integration boundary.

Implementation self-check, tests, lint, type-checks and focused verification remain part of the execution task unless an independent acceptance boundary is separately required.

During a multi-part architecture/framework build, the active task may explicitly defer expensive integrated/runtime acceptance until the architecture is frozen so long as bounded construction sanity checks prevent uncontrolled breakage. This is a cadence decision, not permission to skip final required evidence.

Universal mandatory TDD is not required. Regression-first/TDD is appropriate where behavior risk, regression history, contract changes or task requirements justify it.

## 11. Diagnose only when a blocking evidence gap exists

If a real failure/unexplained unsafe ambiguity blocks progress and current evidence cannot answer the next safe decision, enter `incident-doctor`. If existing evidence already supports the fix, stay in the current authorized delivery flow.

Doctor may use Domain Navigation to locate evidence, then resumes diagnosis. If the supported fix is outside authorization, return to Project Governance before mutation.

## 12. Obtain an independent evidence verdict when needed

Use `evidence-audit` when a distinct implementation/code/PR/CI/release/merge-readiness verdict is required. Bind the audit to the exact target/range/identity and evidence freshness before saying PASS.

Calling Evidence Audit from the implementation context does not by itself establish independence. When formal independent acceptance is part of the engineering boundary, authorize the appropriate AUDIT/VERIFY task purpose and state the independence basis required by risk/user/task.

Audit/reviewer findings do not authorize fixes. Corrective mutation returns to Project Governance/task authorization. Read-only audit may report stale controls but must not change them solely to make the audit clean.

## 13. Merge/release host boundary

At a merge/release decision, keep semantic implementation evidence separate from live repository-host gates. Reuse semantic evidence across proven `CONTROL_ONLY_DRIFT` only when semantic equivalence and task conditions permit it. Re-read current required checks/reviews/conflicts/mergeability/merge queue/current-base/latest-head rules for the literal identity the host governs.

## 14. Reconcile controls and close out

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
