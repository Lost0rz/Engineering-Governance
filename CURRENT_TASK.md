# CURRENT TASK — Planning Documents and Control Alignment

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058`

State: `WAITING_FOR_INDEPENDENT_AUDIT`

Mode: governed Project Governance contract update

## Objective

Add the durable planning-document layer and a mandatory end-of-execution Control Alignment Gate so long-lived design, current task authorization, and current project status remain distinct while cross-session/cross-machine handoffs do not inherit silently stale `CURRENT_STATUS.md` / `CURRENT_TASK.md` semantics.

## Planning context

- Related document: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- Document section / work package: `Implementation scope for Task 058`
- Document revision basis: branch commit `290c112710aa3a078b60ef4d43e59c9d2de0086b`
- Relationship to plan: Task 058 implements the reusable Project Governance source/template contract only. Plugin version bump, Web/local distribution, and formal `plugin-v0.5.5` release remain outside this task.

## Start baseline

- Literal repository baseline: `main` at `72042f4157389520c7acd754cab5272a3cfdab85`.
- Accepted formal release baseline: `plugin-v0.5.4` published from frozen source `3e028cdbe21e9637cbf7bf9b00a5664d44c272c0`.
- Accepted v0.5.4 semantics remain authoritative: `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD separation, and separate live repository-host gates.
- Task branch: `codex/planning-doc-control-alignment-v055`.

## In scope

- Define durable planning-document ownership and its relation to `AGENTS.md`, `CURRENT_TASK.md`, and `CURRENT_STATUS.md`.
- Add optional Task-to-document planning context without requiring a planning document for standalone work.
- Add a mandatory Control Alignment Gate for governed state-changing handoff/closeout.
- Keep control writes conditional: update only when owned semantics changed; otherwise report `UNCHANGED`.
- Require final receipts to report document/status/task alignment results.
- Define strict read-only stale-control reporting without unauthorized mutation.
- Update the Project Governance Skill, supporting references, root durable rule, and reusable templates needed to encode the design.
- Verify acceptance scenarios A–G from the planning document at V0 documentation/governance level.

## Out of scope

- Plugin manifest/version bump to `0.5.5`.
- ChatGPT Web Plugin update.
- Mac mini or MacBook Air Plugin update.
- Formal `plugin-v0.5.5` GitHub release.
- New fourth Skill, daemon, hook, service, database, installer, enforcement runtime, or automatic remediation.
- Bulk migration of historical `docs/superpowers/**` records.
- Forcing `documents/` into target projects that already have a verified durable planning authority elsewhere.

## Source result

- Draft PR: `#22` — `feat: add durable planning and control alignment gate`.
- Final Delivery / Semantic HEAD for source audit: `eed269cab32ecdfb52da87627386bcc77a9e42c6`.
- The branch adds the accepted durable design document and `planning-documents.md` reusable contract.
- Project Governance Skill, control-plane, development-flow, workspace lifecycle receipt, root durable rule, and AGENTS/STATUS/TASK templates are updated.
- `plugin.json` remains version `0.5.4`.
- Exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`.

## Verification level, cadence, and result

`V0 — control/documentation/layout`.

Fresh V0 evidence:

- base `72042f4157389520c7acd754cab5272a3cfdab85` to branch source candidate changes only Task 058-authorized paths;
- no Plugin version/distribution/release path changed;
- top-level Skill count remains exactly `3`;
- `plugin.json` remains `0.5.4`;
- scenario audit A–G from the planning document passes by direct rule inspection:
  - A: terminal/task-state change requires final alignment and owned control reconciliation;
  - B: external evidence alone can remain `UNCHANGED` without evidence-only commits;
  - C: multiple tasks may share one durable plan without using it as a progress tracker;
  - D: durable-plan drift updates the plan and re-authorizes the task when authorization is affected;
  - E: strict read-only stale controls are reported without mutation;
  - F: status/task-only closeout remains `CONTROL_ONLY_DRIFT` and does not restart semantic verification;
  - G: cross-session recovery order is `AGENTS -> STATUS -> TASK -> Related document`.

## Acceptance criteria

Source construction satisfies the Task 058 acceptance criteria. Independent Web audit is still required before merge or any Plugin `0.5.5` distribution task begins.

## Stop conditions

- Do not merge PR #22 before independent audit accepts the source contract.
- Do not bump or publish Plugin `0.5.5` under Task 058.
- Stop if audit finds that planning documents become competing authorization/progress authority, conditional writes became unconditional, planning documents are treated as control-only, or v0.5.4 host/identity semantics were weakened.

## Handoff / current stop point

PR #22 is OPEN / DRAFT / UNMERGED and ready for independent Web audit.

Control Alignment Gate for this source-construction handoff:

- `RELATED_DOCUMENT`: `documents/project-governance-planning-and-control-alignment-v0.5.5.md`
- `DOCUMENT_ALIGNMENT`: `UNCHANGED` — implementation follows the accepted durable design; no durable assumption was invalidated.
- `CURRENT_STATUS_RECONCILIATION`: `UPDATED` — project state advanced from active source construction to independent-audit handoff.
- `CURRENT_TASK_RECONCILIATION`: `UPDATED` — task state advanced to `WAITING_FOR_INDEPENDENT_AUDIT` and records PR #22 / frozen semantic source.
- `CONTROL_ALIGNMENT`: `PASS`
