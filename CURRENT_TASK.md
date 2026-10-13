# CURRENT TASK — Planning Documents and Control Alignment

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058`

State: `ACTIVE_SOURCE_CONSTRUCTION`

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

## Known evidence

- Current `control-plane.md` explicitly permits post-merge reconciliation to remain lazy/batched until a next-task boundary.
- Current `development-flow.md` does not contain a mandatory final status/task alignment result before successful handoff.
- Current Task and Status templates do not provide a durable planning-document linkage contract.
- Current workspace receipt template does not require `CURRENT_STATUS_RECONCILIATION` / `CURRENT_TASK_RECONCILIATION` fields.
- The accepted design is recorded in the related durable planning document above.

## Risk and rationale

This is a governance-contract/documentation change with cross-project behavioral impact but no runtime code. Primary risk is semantic ambiguity or reintroducing control-file churn. The design explicitly preserves conditional writes and v0.5.4 delivery-identity exclusions while making the alignment check mandatory.

## Verification level, cadence, and rationale

`V0 — control/documentation/layout`.

Required checks:

- changed-path scope matches Task 058;
- cross-reference consistency between Skill, references, templates, and root durable rule;
- acceptance scenarios A–G are representable without contradiction;
- lazy/batched external-evidence language cannot be read as permission to leave control-owned semantics stale past final governed handoff;
- `CURRENT_STATUS.md` / `CURRENT_TASK.md` remain the only default Delivery / Semantic identity exclusions;
- planning-document changes are not accidentally classified as control-only;
- no version/distribution/release mutation in this task.

No runtime/full-suite test is required for a pure V0 governance-source change.

## Acceptance criteria

- Durable planning documents have a clear optional authority role and do not become a fourth control file.
- `CURRENT_TASK.md` template can link to a planning document/work package/revision basis or declare standalone work.
- `CURRENT_STATUS.md` template can summarize current planning context without duplicating the plan.
- Every governed state-changing successful final handoff is required to run and report the Control Alignment Gate.
- The gate requires checking document/status/task alignment but writing only sources whose owned semantics changed.
- Strict read-only work reports stale alignment without mutating controls.
- Existing v0.5.4 control-only drift and repository-host-gate semantics remain intact.
- Scenario audit A–G passes.

## Stop conditions

- Any proposed rule would make planning documents a competing execution authorization or live progress authority.
- Any proposed rule would require writing both status and task after every external event regardless of ownership changes.
- Any proposed rule would classify planning-document changes as `CONTROL_ONLY_DRIFT` by default.
- Any proposed rule weakens repository-host live gates or v0.5.4 delivery-identity semantics.
- Scope expands into Plugin distribution/release or runtime machinery.

## Handoff / current stop point

Construct the Project Governance source contract on the authorized task branch, run V0 consistency/scenario audit, and open a Draft PR for independent Web audit. Do not bump/publish v0.5.5 under Task 058.
