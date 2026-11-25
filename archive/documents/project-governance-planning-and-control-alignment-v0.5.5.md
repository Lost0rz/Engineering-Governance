# Project Governance Planning Documents and Control Alignment v0.5.5

Date: 2026-10-13

Status: accepted design for Task `EG-PLANNING-DOCUMENT-CONTROL-ALIGNMENT-058`

## Purpose

Define a lightweight, cross-session and cross-machine governance model that keeps long-lived planning, current execution authorization, and current project state distinct while ensuring `CURRENT_STATUS.md` and `CURRENT_TASK.md` cannot silently remain stale after governed state-changing work finishes.

This design extends the v0.5.4 control-vs-delivery identity model. It does not restore mandatory control-file writes after every external event. Instead, it makes end-of-execution control alignment mandatory while keeping writes conditional on owned facts actually changing.

## Core model

The project uses four semantic roles while retaining the existing three-file control plane:

| Role | Default location | Owns | Does not own |
| --- | --- | --- | --- |
| Durable operating rules | `AGENTS.md` | Stable project/repository workflow rules and boundaries | Current plan, current task progress, execution history |
| Durable planning/design | `documents/**` when such a document is justified | Long-lived design, large-PR or multi-task plan, rationale, work-package decomposition, durable constraints and acceptance boundary | Current execution authorization, live progress, CI history |
| Active execution authorization | `CURRENT_TASK.md` | The one active task, its exact scope, verification contract, stop conditions, handoff, and optional link to planning context | Long-term plan, project history, live project snapshot |
| Current verified state | `CURRENT_STATUS.md` | Where the project is now: accepted baseline/capabilities, active blockers, active development state, current planning context, and next milestone | Detailed implementation plan, chronological log, task authorization |

`documents/**` is not a fourth control file and does not replace the three-file control plane. It is durable planning authority used only when long-lived planning adds value.

## When a planning document is justified

Use a durable planning document for work that is meaningfully larger than one execution task, for example:

- a large PR or program that is intentionally delivered in several bounded tasks or work packages;
- architecture or contract migration whose rationale and constraints must survive multiple sessions;
- a multi-stage redesign where later tasks need the same accepted background and sequencing;
- a durable design decision that should remain understandable after the active task closes.

Do not require a document for every bug, small refactor, one-off maintenance operation, or otherwise self-contained task. A standalone task may declare `Related document: NONE — standalone task`.

## Planning document contract

A durable planning document should answer only the durable questions needed by later tasks:

1. why the work exists;
2. desired outcome and non-goals;
3. accepted design and authority boundaries;
4. durable constraints and dependencies;
5. work packages / phases when decomposition is useful;
6. whole-plan acceptance boundary;
7. important decisions or assumptions whose future change would alter the plan.

A planning document must not become a live progress tracker. Do not maintain per-task completion percentages, current CI state, current mergeability, current branch state, or routine execution history in the document. Those facts belong to live evidence, `CURRENT_STATUS.md`, or `CURRENT_TASK.md` according to ownership.

## Task-to-document linkage

When an active task implements part of a durable planning document, `CURRENT_TASK.md` records a bounded planning-context link:

```text
Related document: documents/<name>.md
Document section / work package: <bounded section or phase>
Document revision basis: <verified commit/revision or observation basis>
Relationship to plan: <what this task implements and what remains outside scope>
```

The document revision basis is provenance by default, not a Repository HEAD or Delivery / Semantic HEAD equality lock. Later unrelated document edits do not invalidate the task. Reconcile or re-authorize the task only when a document change materially changes task-owned scope, prerequisite, acceptance, stop condition, allowed side effect, dependency, or another task-owned condition.

When no durable document is justified, the task explicitly states that it is standalone rather than inventing a planning artifact.

## Status planning context

`CURRENT_STATUS.md` may summarize the currently relevant planning location so a new session can recover project position without reconstructing old PR history:

```text
Planning document: documents/<name>.md | NONE
Current work package / phase: <phase> | standalone
Current task: <task id>
Current state: <verified concise state>
Next intended milestone: <next outcome>
```

This summary does not copy the full plan. The planning document remains authority for durable design; status remains authority for the current project snapshot.

## Mandatory Control Alignment Gate

Every governed state-changing execution must run a Control Alignment Gate before its final PASS / COMPLETE / CLOSED / MERGED / RELEASED handoff claim.

The check is mandatory. A control-file write is conditional.

At the gate:

1. obtain fresh evidence for the execution outcome and any material lifecycle state;
2. reread the applicable planning document when the task links one and the outcome could affect a durable plan assumption;
3. reread `CURRENT_STATUS.md` and `CURRENT_TASK.md`;
4. compare current reality with the facts each source owns;
5. update only the sources whose owned facts are now materially inaccurate or incomplete;
6. report every alignment result explicitly in the receipt.

The gate must distinguish:

- `UPDATED` — owned facts changed and the source was reconciled;
- `UNCHANGED` — the source was checked and remains accurate;
- `NOT_APPLICABLE` — no planning document applies;
- `STALE / NEEDS_RECONCILIATION` — read-only or otherwise non-authorized work found a mismatch it may not repair.

Absence of a reported result is not equivalent to `UNCHANGED`.

## What may remain lazy or batched

Routine external evidence does not require immediate control-file writes merely because it exists:

- CI/test completion;
- independent audit completion;
- review approval;
- current mergeability changing;
- individual workflow-run identifiers;
- other repository-host observations that do not change control-owned semantics.

These may be read live and reported without control churn.

However, lazy/batched evidence recording must not be used to leave control-owned project state stale past the final governed handoff boundary. If execution changes task lifecycle/handoff, accepted project baseline/capability, an active blocker, current work package, or next intended milestone, the owning control must be reconciled before final state-changing handoff.

This preserves the healthy v0.5.4 rule that control-only writes do not change Delivery / Semantic HEAD while preventing cross-session or cross-machine readers from inheriting obsolete task/status semantics.

## Planning-document alignment

At closeout, a linked planning document is checked only for durable-plan drift, not task progress.

Examples that require document reconciliation:

- implementation proves a durable architectural assumption false;
- a required dependency or work-package boundary materially changes;
- the accepted whole-plan design or non-goal changes;
- later work packages would be misplanned if the document stayed unchanged.

Examples that do not require document reconciliation:

- the current task completed as planned;
- CI passed;
- a PR merged;
- a work package became complete when the design itself did not change.

If a durable plan change also changes active task authorization, reconcile/re-authorize `CURRENT_TASK.md` before further affected mutation.

## Read-only behavior

Strict read-only work still runs an alignment assessment when relevant but may not mutate controls or planning documents merely to make them current.

A read-only result reports, for example:

```text
CONTROL_ALIGNMENT: NEEDS_RECONCILIATION
CURRENT_STATUS_ALIGNMENT: STALE
CURRENT_TASK_ALIGNMENT: MATCH
DOCUMENT_ALIGNMENT: UNCHANGED
CONTROL_MUTATION: NOT_AUTHORIZED_READ_ONLY
```

The next authorized state-changing transition must reconcile any stale control semantics before relying on them for mutation.

## Mandatory receipt fields

A governed state-changing execution that claims a final successful handoff must report the semantic equivalents of:

```text
RELATED_DOCUMENT: <path | NONE>
DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE
CURRENT_STATUS_RECONCILIATION: UPDATED | UNCHANGED
CURRENT_TASK_RECONCILIATION: UPDATED | UNCHANGED
CONTROL_ALIGNMENT: PASS
```

Include a short reason when an `UPDATED` or potentially surprising `UNCHANGED` result benefits the next reader.

A final successful handoff must not omit control alignment entirely. Project-specific receipts may add fields but should not require irrelevant workspace fields in projects that do not use task workspaces.

## Cross-session recovery order

A new Web session, Codex session, or other governed executor should recover context in this order:

1. applicable `AGENTS.md`;
2. `CURRENT_STATUS.md`;
3. `CURRENT_TASK.md`;
4. the `Related document` named by the active task, when present;
5. additional domain/navigation/source evidence only as needed for the current decision.

This order should answer quickly:

- how the project works;
- where the project is now;
- what work is currently authorized;
- why the larger work exists and how this task fits it.

Live repository/runtime evidence still wins for facts owned by those authorities; the alignment gate exists to keep the control summaries from drifting unnecessarily far behind them.

## Existing historical planning artifacts

Do not bulk-migrate historical `docs/superpowers/**` artifacts merely to conform to this design. They remain recoverable historical maintainer records. New durable project planning should use the target project's accepted durable planning location, with `documents/**` as the default pattern when the project has no better existing planning authority.

If a project already has an accepted durable architecture/product/design authority under another path, reuse it instead of creating a duplicate `documents/` tree. The semantic role matters more than the literal directory name.

## v0.5.4 compatibility

This design preserves all accepted v0.5.4 identity rules:

- `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only movement remains `CONTROL_ONLY_DRIFT`;
- control-only movement advances literal Repository HEAD but not Delivery / Semantic HEAD;
- valid semantic evidence may be reused across proven control-only drift when task conditions permit;
- repository-host gates remain separate live literal constraints;
- `AGENTS.md`, planning documents, Skill source, workflows, tests, schemas, runtime config, and other implementation/governance-relevant paths are not excluded from Delivery / Semantic identity by this design.

A planning-document change is therefore not control-only by default. It is durable project/governance content and must be evaluated according to the task's verification contract.

## Acceptance scenarios

### A — Terminal task state changes

A task moves from active/ready-for-merge to a verified terminal outcome. Final handoff must check controls; `CURRENT_TASK.md` is updated when its lifecycle/handoff semantics would otherwise be stale, and `CURRENT_STATUS.md` is updated when status-owned current project state changed.

### B — External evidence only

CI or audit passes without changing any control-owned semantics. Alignment gate reports `CURRENT_STATUS_RECONCILIATION: UNCHANGED` and `CURRENT_TASK_RECONCILIATION: UNCHANGED`; no evidence-only control commit is required.

### C — Multiple tasks share one plan

Several tasks may reference the same durable document and different work packages. Completing one work package does not require editing the document merely to mark progress.

### D — Implementation invalidates durable plan

The planning document is updated. If that design change alters current task authorization, the task is reconciled/re-authorized before further affected work.

### E — Read-only audit finds stale status

The audit reports the mismatch and does not mutate controls under read-only authority.

### F — Control-only closeout

Required task/status reconciliation may create a control-only Repository HEAD advance. Delivery / Semantic HEAD remains unchanged and semantic CI/audit is not restarted solely because of that control-only movement.

### G — Cross-session recovery

A fresh executor can read `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, and the linked planning document and recover the current position, current authorization, and durable rationale without reconstructing the full historical PR sequence.

## Implementation scope for Task 058

Task 058 should update only the Project Governance contract and templates needed to make this design reusable:

- `AGENTS.md` for this repository's durable planning/control rule;
- `skills/project-governance/SKILL.md`;
- `skills/project-governance/references/control-plane.md`;
- new `skills/project-governance/references/planning-documents.md`;
- `skills/project-governance/references/development-flow.md`;
- `skills/project-governance/references/workspace-lifecycle.md`;
- `skills/project-governance/assets/templates/AGENTS.md`;
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`;
- `skills/project-governance/assets/templates/CURRENT_TASK.md`;
- root controls required for this task's own planning link and state.

Do not bump the Plugin version or publish v0.5.5 in Task 058. Distribution/release occurs only after source audit accepts this contract.
