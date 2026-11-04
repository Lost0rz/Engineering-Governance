---
name: solution-design
description: Use when authorized engineering work has materially ambiguous requirements, cross-boundary architecture/state ownership choices, competing solution options, or durable design decisions that must be resolved before implementation.
---

# Solution Design

Use this Skill only when implementation would otherwise require material guessing about what should be built or where responsibility should live. Clear bounded changes stay in Project Governance.

Solution Design does not authorize implementation. the FILE_CONTROL Task or ISSUE_CONTROL approved Issue/spec revision remains the selected active authorization and project semantic authorities remain product/domain truth.

Read [Design contract](references/design-contract.md).

## Detailed Issue design responsibility

For ISSUE_CONTROL, resolve architecture, state ownership and required API/data decisions before proposing READY_TO_EXECUTE. Translate accepted decisions into grounded Work Packages with verified code targets, ordered steps, dependencies, error cases, tests and STOP conditions; unknown source locations remain UNKNOWN rather than fabricated. A local L2 pause returns unresolved decisions here, then to Project Governance for revised approval, not to the local small model for architectural guessing.

## Core workflow

1. State the unresolved design question and why it matters to the authorized objective.
2. Separate verified constraints, user/project decisions, agent assumptions and choices still open.
3. Capture goals/non-goals/anti-goals only when they materially constrain the design.
4. Reuse existing architecture/product/domain authority and working patterns before inventing a new owner.
5. Compare the smallest credible option set; avoid option theatre.
6. Use bounded research/spikes only when the result can change the decision.
7. Run convergence against the original objective and authority boundaries.
8. Store long-lived cross-task decisions in the accepted durable planning authority when justified; otherwise keep a self-contained result bounded to the task.
9. Return `TASK_RECONCILIATION_REQUIRED: YES | NO` to Project Governance before implementation.

## Output contract

Return design question/objective, constraints/assumptions, selected option/rationale, user/project vs agent-made decisions, ownership/interface/data implications, research/spike evidence, durable document result, task reconciliation requirement and unresolved blockers.
