# Execution contract

## Work-unit sizing

A work unit should have a checkable result and a meaningful review/verification boundary. Do not split setup/config/docs into artificial tasks when they exist only to support one deliverable. Split where one unit could reasonably succeed/fail or be accepted/rejected independently.

When later units depend on earlier outputs, state the interface that crosses the boundary. Exact signatures/contracts matter more than implementation narration.

## Role classes

- **Controller** — owns sequencing/integration decisions; normally no separate write authority beyond the active task.
- **Implementer** — writes within an explicitly bounded authority.
- **Scout / researcher** — read-only discovery/research.
- **Reviewer / auditor** — read-only independent evaluation unless separately authorized for corrective work.
- **Probe / verifier** — bounded observation/test role; writes only when the active task explicitly authorizes diagnostic mutation.

## Parallelism gate

Parallelize only when all are true:

1. work units do not depend on each other's intermediate state;
2. shared mutable resources will not collide;
3. write scopes are read-only or proven disjoint;
4. each result can be integrated/verified independently;
5. concurrency improves wall-clock or context use enough to justify coordination cost.

If any condition is unresolved, execute sequentially or keep parallel agents read-only.

## Model selection

Select by judgment demand, not prestige:

- bounded transcription/mechanical edit: lowest tier that reliably follows the brief;
- multi-file integration/pattern matching: standard tier;
- architecture, subtle concurrency/security, final high-risk audit: strongest justified tier.

State an explicit maximum/fallback when cost or capability bounds matter. Never rely on unspecified inheritance when that could select a materially different model.

## Recovery ledger

Use only for execution long enough that context loss/restart is a realistic risk. Minimum useful fields:

- task/plan identity;
- work unit -> status;
- commits or concrete result identity;
- verification result;
- rulings/deviations;
- next resume point.

The ledger is ephemeral operational state. It does not replace `CURRENT_STATUS.md`, `CURRENT_TASK.md`, a durable plan, or Git history.
