# Business-first development flow

Use this flow for normal governed product/business engineering. It is a lifecycle, not a requirement to invoke every Skill or create a new task for every phase.

## 1. Recover authority, task purpose, and planning context

Read versioned global `CONTROL_POLICY_V1` and independently verified GitHub enrollment for mode: unadopted FILE_CONTROL reads its historical Task/Status; adopted ISSUE_CONTROL selects either an existing approved GitHub Issue/spec revision **or** a verified current top-level USER-requested G1/G2 bounded task without a first Issue/comment. For Issue-backed work fetch relevant approval/decision receipts; direct-user work verifies host role, repository/action and real write permission instead. Project `AGENTS.md` contains only project-specific rules. Read bounded design and live PR evidence when needed. A stale file, unapproved Issue, incidental comment or READY label cannot expand task authorization.

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

Run the **reuse-first creation gate** in `workspace-lifecycle.md` before allocating another checkout, Git worktree, branch or PR. These are separate decisions: a newly authorized task/branch does not inherently need a new physical worktree, and an agent/command/handoff does not inherit permission to create any of them. Reuse the existing safe authorized task ref/PR for related corrections and control alignment; honor any explicit project fresh-branch/PR rules. Read-only investigation normally uses existing source with no new workspace.

### FILE_CONTROL post-merge status reconciliation without another PR

Under FILE_CONTROL, a GitHub merge may occur **after** the last valid pre-merge `CURRENT_STATUS.md`/`CURRENT_TASK.md` commit. Do not predict the merge in those files and do not automatically create a new PR or physical Worktree just to record `MERGED`. At the final post-merge read-only observation, verify the actual host merge/ref identity, report `POST_MERGE_DRIFT` and `CONTROL_ALIGNMENT: NEEDS_RECONCILIATION` where persisted controls are still pre-merge, and treat the old Task as unable to authorize further product/source writes. The observed host fact is not a new control authority.

At the **next normal, user/project-authorized development task**, read fresh project rules and evidence, reuse an eligible checkout, create the task branch/PR only if required, and commit preceding-task closure + new-task authorization as the **first control-only commit** on that ordinary carrier, before implementing the next product change. A separate closure-only PR is not required unless the host/project explicitly demands one or an independently authorized urgent control correction has no permitted normal carrier. Follow `control-plane.md` for STOP conditions and for the difference between checking, persisting, and opening a PR. Never write directly to protected `main` merely to avoid PR churn.

## 4. Confirm authorization and task boundary

Compare the requested action with the active objective, in/out-of-scope boundary, allowed side effects, verification contract and STOP conditions.

In `ISSUE_CONTROL`, retain the strict/direct or explicitly opted-in delegated approval path by default. A genuinely direct, current **host-authenticated USER instruction** is the **first task authorization** for nonprivileged G1/bounded G2 work: no initial Issue creation, 19-field approval, GitHub comment or per-WP reapproval is required. Before the first write, the hosting runtime verifies that user-role message, the exact requested repository/effects/paths, live writer permission and project constraints. A risk label, model-supplied boolean or GitHub actor name cannot replace this host verification. The portable `INTERACTIVE_SCOPE_ELIGIBILITY_V1` classifier is eligibility-only and cannot satisfy that host check. No runtime proof means keep legacy approval or STOP; do not infer permission from GitHub actor login or editable Issue/chat/AGENTS text. For unattended or cross-session risk-scoped autonomy, require a separately trusted global policy opt-in and independent live-host grant/credential-separation proof; an untrusted local snapshot never changes that gate. Record governance risk G0–G3 separately from verification tier V0–V3 and deviation L0–L3.

Keep the same task when the engineering purpose and authorization are materially unchanged across:

- Web/local/session/machine continuation;
- controller-to-Sub-Agent delegation;
- sequential or parallel work units;
- implementation-local verification supporting the task's own acceptance criteria.

Reconcile or create a distinct task when engineering purpose/authorization materially changes, for example a separately commissioned independent acceptance audit, a distinct corrective objective after findings, or a new design decision that changes scope/interfaces/side effects/writer authority.

## 5. Resolve material design ambiguity only when needed

If implementation would require guessing about product intent, architecture, state ownership, contract/schema, responsibility boundaries or durable cross-task decisions, route to `solution-design`.

Clear local work stays in this flow. Do not invoke Solution Design merely because the request is a feature.

After design, return to Project Governance. Material authorization changes require FILE_CONTROL Task reconciliation, Issue-backed revision/reapproval **if an Issue is the selected authority**, or a fresh explicit host-authenticated user decision for the revised bounded G1/G2 direct task; never silently widen a direct request. If design was a separately authorized purpose, a later execution task may reference that accepted design directly.

## 6. Resolve semantic/source route only when unclear

Use `domain-navigation` when the responsible Domain/capability, accepted semantic authority, source location, symbol, runtime entry, dependency or relevant test cannot be established safely. Reuse accepted project maps/authorities; do not require a literal `DOMAIN_MAP.md`.

Return the verified route or unresolved gap to the calling flow. Navigation does not own diagnosis or authorization.

## 7. Resolve writer/code authority

Before adding/changing a writer, backend, shared behavior, module boundary or materially new responsibility, apply `code-structure.md`. Reuse/extend/replace the canonical authority deliberately rather than creating parallel truth. File size alone is not a responsibility boundary.

At an ordinary handoff, pass along relevant Issue discussion, PR/ref evidence and local workspace context when helpful, without demanding a separate Writer-release check. Only when specific overlapping writes or unique work are actually at risk, reconcile the relevant facts before making the conflicting write; preserve existing work. See `workspace-lifecycle.md` for the general lifecycle rules.

If the responsibility boundary becomes unclear, return to Domain Navigation or Solution Design according to whether the uncertainty is location/authority or design choice.

## 8. Use execution topology to improve effective throughput

Use `execution-orchestrator` when the authorized task benefits from decomposition, multiple agents/roles, parallelism, delegated-model policy, recovery state or controlled integration.

Do not treat minimum agent count as the goal. If independent work units can safely run concurrently and concurrency materially improves throughput or context isolation, use available parallel capacity. Parallel readers/researchers/reviewers are often cheap to separate; parallel writers still require proven-disjoint semantic authority/workspaces plus an integration boundary.

Delegated Sub Agents follow `ENVIRONMENT_DEFAULT_ONLY`. Each delegated execution context resolves its own authoritative Sub Agent configuration/runtime default. Do not propagate concrete model/reasoning values from another context or infer an unobservable platform default. Do not switch a delegated unit to a stronger model merely because the work becomes harder; return a capability/environment gap to the controller if the current environment default is insufficient.

One inline executor remains correct when decomposition provides no material benefit or dependencies/shared state make concurrency inefficient or unsafe.

Orchestration never expands the selected FILE_CONTROL Task, ISSUE_CONTROL approved Issue, or verified current-user-direct G1/G2 task scope.

## 9. Transfer responsibility through context-neutral Agent Handoff

Whenever responsibility crosses agents, sessions, machines or execution contexts, use `agent-handoff`.

A same-task continuation preserves the same `TASK_ID` and references the same task/design authorities. The request carries authority references + fresh delta + immediate action boundary + return contract. It may record source/target context when useful, but Web/local identity does not define task purpose.

Under environment-owned delegated-model policy, handoff carries the policy only. It does not make the sender's concrete model/reasoning configuration authoritative for the receiver.

Do not paste complete task/status/rules into the card by default. If the receiver can read the authority, point to it. The task's own `Handoff / current stop point` is lifecycle/authorization state, not a transport card.

## 10. Implement and verify proportionally

Implement the smallest authorized outcome. Select the lightest safe `V0`–`V3` verification tier and a cadence appropriate to the construction/corrective/task/integration boundary.

The verification tier covers evidence, not permission. A G1/G2 task can still require V3 security/concurrency review; neither a V0 check nor a small diff authorizes G3 effects.

Implementation self-check, tests, lint, type-checks and focused verification remain part of the execution task unless an independent acceptance boundary is separately required.

During a multi-part architecture/framework build, the active task may explicitly defer expensive integrated/runtime acceptance until the architecture is frozen so long as bounded construction sanity checks prevent uncontrolled breakage. This is a cadence decision, not permission to skip final required evidence.

Universal mandatory TDD is not required. Regression-first/TDD is appropriate where behavior risk, regression history, contract changes or task requirements justify it.

## 11. Publish repository-backed work when applicable

For state-changing work that produced or advanced Git commits, apply [Remote repository delivery](remote-delivery.md) before reporting successful repository delivery.

A local commit, clean working tree, or local branch SHA proves only local state.

Classify the delivery boundary:

- applicable configured remote + not explicitly local-only -> push the already-authorized task/project ref and verify the fresh remote ref contains the delivered commit before reporting full repository completion;
- no applicable configured remote -> `REMOTE_DELIVERY: NOT_APPLICABLE_NO_REMOTE`;
- accepted project/task authority explicitly requires local-only work -> `REMOTE_DELIVERY: NOT_REQUIRED_LOCAL_ONLY`;
- applicable remote but push/verification cannot complete -> preserve local work and report `PENDING` or `FAILED`; do not claim remotely available completion.

This rule does not authorize a new remote, force-push, credential bypass, branch substitution, or an implicit push to `main`. If the correct remote/ref is ambiguous, remote delivery remains unresolved.

Remote availability is also not merge/CI/release evidence. Repository-host gates remain separate.

## 12. Diagnose only when a blocking evidence gap exists

If a real failure/unexplained unsafe ambiguity blocks progress and current evidence cannot answer the next safe decision, enter `incident-doctor`. If existing evidence already supports the fix, stay in the current authorized delivery flow.

Doctor may use Domain Navigation to locate evidence, then resumes diagnosis. If the supported fix is outside authorization, return to Project Governance before mutation.

## 13. Obtain an independent evidence verdict when needed

Use `evidence-audit` when a distinct implementation/code/PR/CI/release/merge-readiness verdict is required. Bind the audit to the exact target/range/identity and evidence freshness before saying PASS.

Calling Evidence Audit from the implementation context does not by itself establish independence. When formal independent acceptance is part of the engineering boundary, authorize the appropriate AUDIT/VERIFY task purpose and state the independence basis required by risk/user/task.

Audit/reviewer findings do not authorize fixes. Corrective mutation returns to Project Governance/task authorization. Read-only audit may report stale controls but must not change them solely to make the audit clean.

## 14. Merge/release host boundary

At a merge/release decision, keep semantic implementation evidence separate from live repository-host gates. Reuse semantic evidence across proven `CONTROL_ONLY_DRIFT` only when semantic equivalence and task conditions permit it. Re-read current required checks/reviews/conflicts/mergeability/merge queue/current-base/latest-head rules for the literal identity the host governs.

## 15. Reconcile controls and close out when material

At a **real task/authorization/terminal state transition**, verify the affected authority and outcome; do not impose a universal Control Alignment Gate at each edit, ordinary handoff, same-task continuation or test result.

- **FILE_CONTROL:** when Task/Status semantics may change, compare to current facts and update only stale project-owned control fields under `control-plane.md`.
- **ISSUE_CONTROL legacy:** retain actual selected approval, existing material-decision and required final-receipt rules. Do not read/update legacy Task/Status or manufacture Issue-progress Git commits.
- **Verified active G1/G2 autonomy (future):** recover result from selected task/grant/PR/commit/CI/handoff; ordinary Issue comments are optional. Missing host authorization continues to STOP, not silently fall back to an unapproved path.
- **Merge/release:** check the actual host gate and evidence for that operation. Do not infer final acceptance or local workspace cleanup from remote merge alone.

Preserve unique local work and investigate only actual overlapping writer/cleanup risks. When no owned control meaning changed, no additional control write, checkbox report or status-only commit is required.

## Cross-skill composition

Use [Capability composition](capability-composition.md) for allowed return paths and artifact/writer boundaries. Do not create a second controller, a fourth control file, or a handoff/ledger/audit artifact that competes with project authority.
