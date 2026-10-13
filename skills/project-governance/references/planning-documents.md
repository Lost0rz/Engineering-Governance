# Durable planning documents and task linkage

Use a durable planning document only when the work needs long-lived design context that spans more than one bounded execution task. The default pattern is `documents/**` when the target project has no better accepted planning authority. Reuse an existing architecture/product/design authority when one already owns this role; do not create a duplicate tree merely to satisfy a filename convention.

A planning document is **not** a fourth control file. The three-file control plane remains `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`.

## Ownership model

| Source | Owns | Must not become |
| --- | --- | --- |
| `AGENTS.md` | Durable operating rules and stable project/repository boundaries | Current plan, live progress, task history |
| durable planning document | Long-lived design, rationale, multi-task/large-PR plan, work-package decomposition, durable constraints and acceptance boundary | Live progress tracker, task authorization, CI/PR history |
| `CURRENT_TASK.md` | The one active execution authorization and bounded task contract | Long-term architecture/plan, project history |
| `CURRENT_STATUS.md` | Verified current project snapshot and current planning position | Detailed plan or implementation log |

Keep one owner per fact class. Link between sources rather than copying their full contents.

## When to create or reuse a planning document

A durable planning document is justified when at least one of these materially helps future execution:

- a large PR or program is intentionally delivered across multiple bounded tasks/work packages;
- architecture/contract migration rationale must survive multiple sessions;
- later tasks depend on the same accepted design, sequencing, constraints, or whole-plan acceptance boundary;
- a durable design decision would otherwise be repeatedly reconstructed from historical PRs or chat context.

Do not require a document for every bug, one-off maintenance task, small refactor, or otherwise self-contained unit of work. A standalone task may state `Related document: NONE — standalone task`.

## What a durable plan should contain

Keep the document focused on durable planning semantics:

1. purpose and desired outcome;
2. non-goals;
3. accepted design / authority boundaries;
4. durable constraints and dependencies;
5. useful work packages or phases;
6. whole-plan acceptance boundary;
7. assumptions or decisions whose later change would materially alter future work.

Do not maintain routine execution state such as task completion percentages, current CI results, review state, branch/worktree state, or chronological progress. `CURRENT_STATUS.md`, `CURRENT_TASK.md`, live repository/runtime evidence, or task receipts own those facts according to their class.

## Task planning context

When the active task implements part of a durable plan, `CURRENT_TASK.md` records a bounded planning link:

```text
Related document: documents/<name>.md
Document section / work package: <section/phase>
Document revision basis: <verified revision or observation basis>
Relationship to plan: <what this task implements and what remains outside scope>
```

The revision basis is provenance by default. It is not an implicit literal Repository HEAD or Delivery / Semantic HEAD equality lock. A later unrelated document edit does not invalidate the task.

If the planning document materially changes a task-owned prerequisite, scope, acceptance criterion, stop condition, allowed side effect, dependency, explicit head lock, or authorization boundary, reconcile and re-authorize the task before further affected mutation.

## Status planning context

`CURRENT_STATUS.md` may summarize the active planning location so a fresh session can recover the project quickly:

```text
Planning document: documents/<name>.md | NONE
Current work package / phase: <phase> | standalone
Current task: <task id>
Current state: <verified concise state>
Next intended milestone: <next outcome>
```

Do not copy the detailed plan into status. The planning document owns durable design; status owns where the project is now.

## Planning-document alignment at handoff

For a linked plan, final state-changing handoff checks whether execution changed the durable plan itself.

Update the planning document when, for example:

- implementation disproves a durable design assumption;
- a dependency or work-package boundary materially changes;
- whole-plan design, non-goal, or acceptance boundary changes;
- leaving the document unchanged would mislead later tasks.

Do **not** update it merely because:

- the current task completed as planned;
- CI/audit/review passed;
- a PR merged;
- a work package became complete without changing the design.

Report the result as `DOCUMENT_ALIGNMENT: UPDATED | UNCHANGED | NOT_APPLICABLE` in a final state-changing receipt when the project uses this contract.

## Cross-session recovery

Recover context in this order unless a project-specific durable rule says otherwise:

1. applicable `AGENTS.md`;
2. `CURRENT_STATUS.md`;
3. `CURRENT_TASK.md`;
4. the task's `Related document`, when present;
5. additional domain/navigation/source evidence only as needed for the current decision.

This should establish how the project works, where it is now, what is authorized, and why the larger work exists without reconstructing historical PRs.

## Historical material

Do not bulk-migrate historical planning artifacts merely to conform to this contract. Historical `docs/**`, ADRs, specs, Superpowers artifacts, or other existing records may remain where they are. Use the project's accepted durable planning authority for new work; `documents/**` is a default pattern, not a mandatory literal path.

## Delivery identity

Planning documents are durable project/governance content. They are **not** included in the default `CONTROL_ONLY_DRIFT` exclusion. Only `CURRENT_STATUS.md` and `CURRENT_TASK.md` are excluded by default under the control-identity contract.

A planning-document edit therefore participates in normal Delivery / Semantic identity evaluation and receives the verification appropriate to its task and risk.
