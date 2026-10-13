# Durable planning documents, Solution Design, and task linkage

Use a durable planning/design document only when long-lived context materially helps more than one bounded execution decision. Reuse an accepted architecture/product/design authority when one already owns this role; `documents/**` is a default pattern only when the target project has no better authority.

A planning/design document is **not** a fourth control file. The three project controls remain `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`.

## Ownership model

| Source | Owns | Must not become |
| --- | --- | --- |
| `AGENTS.md` | durable operating rules and stable repository/project boundaries | live task/progress history |
| durable planning/design authority | accepted long-lived design, rationale, constraints, work-package structure, whole-plan acceptance boundary | task authorization, live CI/PR/progress log |
| `CURRENT_TASK.md` | one active execution authorization and bounded task contract | long-term architecture/plan |
| `CURRENT_STATUS.md` | concise verified project snapshot/current planning position | detailed plan or implementation diary |
| Solution Design output | bounded design decision/evidence before it is placed in the correct authority | automatic task authorization or second design authority |

Keep one owner per fact/decision class and link instead of copying full contents.

## Solution Design relationship

`solution-design` resolves a material design question. Its result may remain bounded to one task when no durable value would be lost. When future tasks/maintainers depend on the accepted decision, write the long-lived portion into the project's accepted durable planning/design authority.

A Solution Design result must return:

```text
TASK_RECONCILIATION_REQUIRED: YES | NO
REASON: <material task-owned semantic change | none>
DURABLE_DOCUMENT: <path/section | NONE>
```

If `YES`, Project Governance reconciles/re-authorizes `CURRENT_TASK.md` before affected implementation. Writing a design document does not itself authorize execution.

## When durable planning is justified

Use it when at least one materially helps future work:

- a large PR/program is delivered across multiple bounded tasks/work packages;
- architecture/contract migration rationale must survive sessions;
- later tasks depend on shared design/sequencing/constraints/whole-plan acceptance;
- a durable decision would otherwise be reconstructed repeatedly from history/chat.

Do not require it for every bug, maintenance change, small refactor or self-contained task. Such a task may state `Related document: NONE — standalone task`.

## What the durable authority contains

Keep durable semantics only:

1. purpose/desired outcome;
2. non-goals/anti-goals where material;
3. accepted design/authority boundaries;
4. durable constraints/dependencies;
5. useful work packages/phases;
6. whole-plan acceptance boundary;
7. assumptions/decisions whose later change materially alters future work.

Do not store routine task completion percentage, current CI/review state, branch/worktree state, or chronological execution logs here.

## Task linkage

When the active task implements part of a durable design/plan, record:

```text
Related document: documents/<name>.md
Document section / work package: <section/phase>
Document revision basis: <verified revision or observation basis>
Relationship to plan: <what this task implements and what remains outside scope>
```

The revision basis is provenance by default, not an implicit literal Repository HEAD or Delivery / Semantic HEAD equality lock.

If a later plan/design change materially alters task-owned prerequisites, scope, acceptance, STOP conditions, dependencies, allowed side effects, verification or explicit locks, stop affected mutation and reconcile/re-authorize the task.

## Status linkage

`CURRENT_STATUS.md` may summarize only where the project is now:

```text
Planning document: <path | NONE>
Current work package / phase: <phase | standalone>
Current task: <task id>
Current state: <concise verified state>
Next intended milestone: <outcome>
```

Do not copy the detailed plan into status.

## Planning/design alignment at final handoff

For a linked durable authority, final state-changing handoff checks whether execution changed what that source owns.

Update it when implementation disproves a durable assumption, materially changes design/dependency/work-package/whole-plan acceptance, or leaving it unchanged would mislead later work.

Do not update it merely because a task finished as planned, CI/audit passed, a PR merged, or a work package completed without changing durable design semantics.

Report `DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE`.

## Cross-session recovery

Recover context in this order unless project rules say otherwise:

1. applicable `AGENTS.md`;
2. `CURRENT_STATUS.md`;
3. `CURRENT_TASK.md`;
4. the task's bounded related design/plan when present;
5. additional Domain/source/runtime/evidence only as needed.

## Delivery identity

Durable planning/design files are governance/delivery-relevant content. They are not part of the default `CONTROL_ONLY_DRIFT` exclusion. Only `CURRENT_STATUS.md` and `CURRENT_TASK.md` are excluded by default.
