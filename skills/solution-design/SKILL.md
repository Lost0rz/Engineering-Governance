---
name: solution-design
description: Use when authorized engineering work has materially ambiguous requirements, cross-boundary architecture/state ownership choices, competing solution options, or durable design decisions that must be resolved before implementation.
---

# Solution Design

Use this Skill only when implementation would otherwise require material guessing about what should be built or where responsibility should live. Clear bounded changes stay in Project Governance.

Solution Design does not authorize implementation. FILE_CONTROL Task or ISSUE_CONTROL selected approved spec / independently host-verified active grant remains the relevant authority; target-project product/domain truth stays with the owning project.

Read [Design contract](references/design-contract.md).

## Detailed Issue design responsibility

For complex legacy ISSUE_CONTROL specs, ground necessary WPs in verified code targets, dependencies, risks and tests before declaring readiness. For a future **independently host-verified G1/G2 compact scope**, resolve implementation choices within the selected task/grant envelope without forcing a WP list or new user approval. An L2 uncertainty triggers bounded design resolution, not automatically a spec revision: return to Project Governance for reassessment **only when** task scope, effects, security or permission authority materially changes. Do not fabricate missing API contracts or treat a design conclusion as a new grant.

Record governance risk G0–G3 as an authority/effects boundary and V0–V3 separately as the evidence needed to verify the design. A local snapshot, actor login, or proposed workflow is not host-proof for activating risk-scoped autonomy; unresolved host trust stays fail closed and returns to Project Governance.

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
