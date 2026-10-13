# Design contract

## 1. When design is justified

Enter Solution Design when one or more are material to correctness:

- product/behavior intent is ambiguous;
- state ownership, writer authority, contract/schema or module responsibility must change;
- credible approaches have different lifecycle/cost/risk implications;
- work spans bounded tasks and needs durable decisions;
- a technical choice cannot safely be inferred from accepted repository convention;
- bounded research/spike evidence is required before choosing.

Do not enter for a clear local edit, known bug with sufficient evidence, routine config/dependency change, or merely because something is a feature.

## 2. Decision classes

Keep these distinct:

- **VERIFIED FACT / CONSTRAINT** — supported by accepted source/evidence;
- **USER / PROJECT DECISION** — explicitly chosen or already authoritative;
- **AGENT ASSUMPTION** — provisional and named as such;
- **AGENT IMPLEMENTATION CALL** — agent-selected detail inside accepted authority;
- **UNRESOLVED DECISION** — blocks or conditions implementation.

Never present an agent-selected default as a user-approved requirement.

## 3. Useful design record

Record only decisions future execution cannot safely reconstruct:

- intent/why;
- verified constraints;
- goals/non-goals/anti-goals where material;
- selected option + credible rejected alternatives/rationale;
- ownership/interfaces/data-flow implications;
- compatibility/migration requirements;
- verification implications;
- decision class for assumptions/defaults.

Avoid line-by-line implementation narration.

## 4. Spike rule

Use a spike only when its possible outcomes can change the design decision. Keep it bounded/disposable and label it as evidence, not production implementation. Retaining spike code becomes normal authorized implementation and must meet project quality/verification rules.

## 5. Durable planning convergence

A self-contained design decision needed only for one bounded task may remain in the task/handoff context if no durable value is lost.

When multiple tasks, future maintainers or whole-plan acceptance depend on the decision, record the accepted result in the project's existing durable architecture/product/design authority. If none exists and durable planning is justified, Project Governance's `documents/**` pattern may be used.

The durable design/planning authority owns long-lived rationale/constraints/work-package structure. It does **not** authorize execution or own live progress.

## 6. Task reconciliation gate

Before implementation, compare accepted design against `CURRENT_TASK.md`.

Return:

```text
TASK_RECONCILIATION_REQUIRED: YES | NO
REASON: <scope/prerequisite/side-effect/dependency/verification/acceptance/stop-condition change | none>
DURABLE_DOCUMENT: <path/section | NONE>
```

If `YES`, return to Project Governance and reconcile/re-authorize before affected mutation.

## 7. Convergence check

Before leaving design, verify that the selected option:

- satisfies the original objective rather than optimizing an adjacent problem;
- preserves or deliberately changes one canonical authority per fact/behavior class;
- respects explicit non-goals/anti-goals;
- does not create an unapproved new writer/control authority;
- has a clear verification implication;
- leaves unresolved decisions explicit.

A technically elegant solution that changes the requested outcome has not converged.
