# Design contract

## Trigger

Use Solution Design only when implementation would otherwise require material guessing about intent, architecture, state ownership, contract/schema, responsibility boundary, or durable cross-task decisions.

Do not enter for a clear local edit, known bug with sufficient evidence, routine config/dependency change, or merely because work is a feature.

## Decision classes

Keep distinct:

- `VERIFIED FACT / CONSTRAINT`
- `USER / PROJECT DECISION`
- `AGENT ASSUMPTION`
- `AGENT IMPLEMENTATION CALL`
- `UNRESOLVED DECISION`

Never present an agent-selected default as a user-approved requirement.

## Useful design record

Record only what future execution cannot safely reconstruct:

- intent/why and verified constraints;
- selected option + credible rejected alternatives/rationale;
- ownership/interfaces/data-flow implications;
- compatibility/migration and verification implications;
- **material** quality attributes only when they constrain the decision (for example reliability, performance, security, operability, maintainability, privacy);
- consequences/reversibility when the choice is costly to undo.

When material, add:

```text
CONSEQUENCES
REVERSIBILITY
REVERSAL_TRIGGER
```

Avoid implementation narration and checklist inflation.

## Research / spike

Use a spike only when possible results can change the decision. Keep it bounded/disposable and label it as evidence. Retained spike code becomes normal authorized implementation.

## Durable decision lifecycle

Use durable planning only when multiple tasks/future maintainers/whole-plan acceptance depend on the decision. The durable record owns rationale/constraints, not execution authorization or live progress.

When an accepted durable decision is replaced, mark the old record/section clearly `SUPERSEDED` and point to the new authority. Do not maintain two active versions of the same decision.

## Task reconciliation

Before implementation compare the accepted design with `CURRENT_TASK.md`:

```text
TASK_RECONCILIATION_REQUIRED: YES | NO
REASON: <material authorization change | none>
DURABLE_DOCUMENT: <path/section | NONE>
```

If `YES`, return to Project Governance before affected mutation.

## Convergence

Before leaving design verify that the selected option satisfies the original objective, preserves/deliberately changes canonical authority, respects material non-goals, has clear verification implications, and leaves unresolved decisions explicit.
