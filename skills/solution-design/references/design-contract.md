# Design contract

## When design is justified

Enter Solution Design when one or more of these are material to correctness:

- the request leaves product/behavior intent ambiguous;
- state ownership, writer authority, contract/schema, or module responsibility must change;
- multiple credible approaches have different lifecycle/cost/risk implications;
- the work spans multiple bounded tasks and needs durable decisions;
- implementation needs a technical choice that cannot safely be inferred from repository convention;
- a spike/research result is required before choosing a design.

Do not enter for a clear local edit, a known bug with sufficient evidence, routine dependency/config changes, or merely because a new feature exists.

## Decision record

A useful design record contains only decisions an implementer cannot safely reconstruct:

- intent and why;
- verified constraints;
- goals, non-goals, anti-goals;
- accepted option and rejected alternatives with short rationale;
- ownership/interfaces/data-flow implications;
- compatibility/migration requirements when material;
- verification implications;
- agent-made defaults clearly labeled as such.

Avoid line-by-line implementation steps here. Those belong to the authorized task/execution flow when needed.

## Spike rule

Use a spike only when its possible outcomes can change the design decision. Keep it bounded, disposable, and separately labeled. If the project decides to retain spike code, that retention becomes normal authorized implementation work and must meet the project's verification/quality rules.

## Convergence check

Before returning to implementation, compare the selected design against the original objective and project authorities. A technically elegant design that changes the requested outcome or creates an unapproved new authority has not converged.
