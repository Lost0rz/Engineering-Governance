# Control Files Noise Reduction Design

Status: user-supplied design baseline, normalized for repository execution

Task: `EG-CONTROL-DELIVERY-IDENTITY-055`

## Goal

Reduce governance noise across all governed projects by separating control-record commits from implementation/delivery identity without weakening the authority of `CURRENT_STATUS.md` or `CURRENT_TASK.md` for the semantics they own.

## Problem

The current Project Governance contracts distinguish several Git identity roles, but the final-head freeze text still describes any post-freeze `status`, `task`, or documentation commit as changing the identity being verified. That is correct for literal repository HEAD, but it is too coarse for implementation freshness: a commit that changes only `CURRENT_STATUS.md` and/or `CURRENT_TASK.md` does not change product/source/runtime/test/workflow/schema/dependency implementation.

The result can be unnecessary HEAD-drift stops, CI/audit restarts, merge-readiness resets, lifecycle closeout loops, and extra control commits whose only purpose is to keep controls synchronized with evidence that already exists elsewhere.

## Identity model

### Repository HEAD

The literal Git commit SHA. Every commit changes Repository HEAD.

### Delivery / Semantic HEAD

The implementation identity after excluding exactly these two repository-control paths:

- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`

For implementation freshness, exact-code-tree verification, CI identity, code-review identity, merge-readiness identity, and accepted implementation-tree equivalence, use Delivery / Semantic HEAD.

### Change classes

`CONTROL_ONLY_CHANGE` means the changed path set is non-empty and contains only `CURRENT_STATUS.md` and/or `CURRENT_TASK.md`.

`CONTROL_ONLY_DRIFT` means two repository revisions differ, but the difference is limited to those two control files and therefore leaves Delivery / Semantic HEAD unchanged.

`DELIVERY_HEAD_CHANGE` means any implementation-relevant path changed. A mixed commit that changes a control file plus any other path is a `DELIVERY_HEAD_CHANGE`.

`SEMANTIC_TREE_EQUIVALENCE = PASS` means the compared repository trees are equal after excluding only the two control paths.

## Control authority is preserved

The exclusion is about delivery identity only. It does not weaken control semantics.

`CURRENT_STATUS.md` remains the current verified project-state snapshot. `CURRENT_TASK.md` remains the single active authorization authority. Agents should normally read both at the beginning of governed work.

If `CURRENT_TASK.md` materially changes objective, scope, allowed mutation, prerequisites, acceptance criteria, stop conditions, or another task-owned decision, the new authorization must be read and obeyed before further mutation. That content change may change what work is allowed or what evidence is sufficient even though the commit itself is not implementation identity.

A stale or conflicting task authorization may still require reconciliation. A SHA mismatch caused only by control-record commits does not by itself constitute implementation drift.

## Recorded SHA semantics

A SHA recorded in `CURRENT_STATUS.md` or `CURRENT_TASK.md` is provenance/audit evidence by default, not an implicit current-HEAD equality lock.

An equality lock exists only when the owning control explicitly declares semantics such as `EXPECTED_HEAD`, `REQUIRED_HEAD`, `MUST_EQUAL`, or `FROZEN_IMPLEMENTATION_HEAD`.

When a lock exists, the control must make clear whether it locks:

- Delivery / Semantic HEAD; or
- literal Repository HEAD.

Default implementation-oriented locks to Delivery / Semantic HEAD unless literal repository equality is explicitly required.

## Exact-head and CI semantics

At PR, merge, and release boundaries, the implementation candidate is frozen by Delivery / Semantic HEAD (or an equivalent semantic-tree identity) unless the task explicitly requires literal repository equality.

CI, review, independent audit, mergeability, and repository-host evidence remain bound to the implementation identity they actually observed. A later control-only Repository HEAD advance does not invalidate that evidence when semantic implementation equivalence is proven and no task requirement invalidates the tested implementation.

Do not create additional control commits solely to write transient evidence states such as `CI PASS`, `audit PASS`, `merge-ready`, `merged`, or `closeout complete`. Prefer live GitHub/CI evidence for those facts.

Fresh CI is required when implementation-relevant content changes or when another existing verification rule independently requires it. Real source/config/test/workflow/schema/migration/dependency/runtime-authority changes remain implementation changes.

## Merge-readiness and lazy control reconciliation

After implementation gates pass, merge the already verified implementation. Do not make a post-audit or post-CI control-only commit a prerequisite for merge.

Post-merge control updates are lazy/batched by default. A merge does not require an immediate `CURRENT_STATUS.md` or `CURRENT_TASK.md` commit merely to memorialize the lifecycle event.

At the next meaningful planning boundary, one control transition may both:

- reconcile the accepted state of the previous task; and
- authorize the next task.

This reduces sequences such as `implementation -> status commit -> CI -> status commit -> audit -> task commit -> merge -> closeout commit -> next task commit` to `authorize -> implement -> verify -> audit -> merge -> next-task reconciliation`.

## Workspace lifecycle

Control-only Repository HEAD advances must not reopen an already verified workspace closeout or create a second cleanup cycle.

If a task workspace is already terminal and physically closed, and the only later main-branch difference is `CURRENT_STATUS.md` / `CURRENT_TASK.md`, keep the lifecycle closed and treat the control-only main advance as non-blocking.

This rule does not weaken unique-work preservation, predecessor-writer rules, or local/remote workspace evidence requirements.

## Exclusion boundary

The default exclusion applies only to:

- `CURRENT_STATUS.md`
- `CURRENT_TASK.md`

It does not automatically apply to:

- `AGENTS.md`
- workflows
- tests
- schemas
- migrations
- dependency manifests
- runtime configuration
- source code
- governance implementation itself

A material `AGENTS.md` change can change project rules and therefore remains implementation/governance-relevant unless another explicit project rule says otherwise.

## Read every time; write only when materially necessary

Governed work should normally read `CURRENT_STATUS.md` and `CURRENT_TASK.md` at task start. Reading does not imply writing.

Update `CURRENT_TASK.md` only when task-owned semantics materially change, including a new authorization, objective/scope change, allowed-mutation change, authority-boundary change, task-invalidating blocker, or change to acceptance/STOP conditions.

Do not update it merely because CI, review, audit, mergeability, merge, or another routine lifecycle observation changed.

Update `CURRENT_STATUS.md` when a verified fact is important enough to affect future project reasoning. Prefer batching status reconciliation with the next meaningful task transition rather than writing every external event immediately.

## Baseline RED audit before source modification

The task-start source at Repository HEAD `1a450aacb301e7c5a25dd88d17749911536d989c` inherits reusable source from `4f3d5308aa742014cfbb8a72adcdb18d5d7c147d` and currently demonstrates the following:

### Scenario A — post-audit status update: RED

Current `verification-tiers.md` says a post-freeze source/status/task/documentation commit changes the identity being verified. Therefore a `CURRENT_STATUS.md`-only commit after CI/audit can force a new exact-head cycle even when implementation is unchanged. Required result: `CONTROL_ONLY_DRIFT`, no CI/audit restart.

### Scenario B — post-merge closeout record: RED / ambiguous

Current workspace rules correctly separate remote merge from local closeout, but they do not explicitly state that a later main advance limited to control records is non-blocking after closeout. Existing baseline/head rules can therefore cause the already-closed workspace to appear stale. Required result: lifecycle remains closed; no second cleanup.

### Scenario C — next task after merged prior task: RED / overly eager reconciliation

Current control-plane language requires material lifecycle events to be reconciled before later state-changing action that relies on the earlier phase. Combined with immediate current-state maintenance, this can drive an intermediate closeout control transition before the next task is authorized. Required result: read controls, verify live evidence, then reconcile prior accepted state and authorize the next task together when safe.

### Scenario D — real source drift: existing guard to preserve

A source/config/test/schema/workflow change after audit remains a real delivery change. Required result: `DELIVERY_HEAD_CHANGE`; exact-head evidence invalidated; fresh verification required.

### Scenario E — material task authorization change: existing guard to preserve

A `CURRENT_TASK.md` content change from backend-only to backend-plus-migration remains authoritative. Required result: agent reads and obeys the new authorization before mutation, while the control commit remains excluded from application-code identity.

## Source changes

Update the existing contracts consistently rather than adding a new Skill or runtime mechanism. Expected files:

- `AGENTS.md` for this repository's own durable dogfooding rule;
- `skills/project-governance/SKILL.md`;
- `skills/project-governance/references/control-identity.md`;
- `skills/project-governance/references/control-plane.md`;
- `skills/project-governance/references/verification-tiers.md`;
- `skills/project-governance/references/workspace-lifecycle.md`;
- `skills/project-governance/references/development-flow.md`;
- `skills/project-governance/assets/templates/AGENTS.md` when needed to prevent projects from recreating literal-HEAD drift rules;
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`;
- `skills/project-governance/assets/templates/CURRENT_TASK.md`.

No daemon, hook, database, lifecycle service, installer, remediation runtime, fourth Skill, or new automatic file-mutating mechanism is introduced.

## Acceptance

The change is accepted only if all of the following hold consistently across the reusable Project Governance source:

1. `CURRENT_STATUS.md` / `CURRENT_TASK.md` remain available and authoritative controls.
2. Their commit SHAs are not implementation identity by default.
3. Control-only commits do not by themselves invalidate CI.
4. Control-only commits do not by themselves invalidate independent audit.
5. Control-only commits do not reopen lifecycle closeout.
6. Control-only commits do not trigger HEAD-drift STOP.
7. Semantic tree equivalence excludes exactly the two control paths.
8. Real implementation-relevant changes still invalidate exact-head evidence when appropriate.
9. Material task-authorization changes remain enforced.
10. `AGENTS.md` and other implementation/governance-relevant paths are not silently excluded.
11. No new governance runtime/infrastructure is introduced merely for this rule.
