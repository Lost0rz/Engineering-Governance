---
name: solution-design
description: Use when authorized engineering work has materially ambiguous requirements, cross-boundary architecture/state ownership choices, competing solution options, or durable design decisions that must be resolved before implementation.
---

# Solution Design

Use this Skill conditionally from governed engineering work when implementation would otherwise require material guessing about what should be built or where responsibility should live. Clear, bounded changes stay in Project Governance and do not acquire a design ceremony merely because this Skill exists.

## Authority boundary

`solution-design` does not authorize implementation. `CURRENT_TASK.md` remains the active authorization, project semantic authorities remain the source of product/domain truth, and any durable design document is planning context rather than a fourth control file.

Use [Design contract](references/design-contract.md) for the detailed method.

## Core workflow

1. **Establish the design question.** State the unresolved decision and why it matters to the authorized objective. Do not broaden the task into adjacent redesign.
2. **Separate known facts from choices.** Mark verified constraints, user/project decisions, agent assumptions, and choices still open. Never present an agent-selected default as a user-approved requirement.
3. **Define success and failure boundaries.** Capture goals, non-goals, and anti-goals when they materially constrain the design.
4. **Inspect prior authority and working patterns.** Reuse accepted architecture/product/domain authorities and established repository patterns before inventing a new one. Use Domain Navigation only when the responsible authority/source/test route is unclear.
5. **Compare the smallest useful set of options.** Evaluate tradeoffs against the actual project constraints. Prefer one recommended option plus credible alternatives; do not create option theatre for a decision that is already obvious.
6. **Use bounded research or a throwaway spike only when evidence would change the decision.** A spike is evidence, not production implementation and not authorization to keep expanding it.
7. **Record the accepted design at the right durability.** A small self-contained decision may stay in the active task/chat handoff; cross-task or long-lived design belongs in the project's accepted planning authority.
8. **Return to Project Governance.** If the accepted design changes scope, prerequisites, side effects, verification, or authorization boundaries, reconcile `CURRENT_TASK.md` before implementation.

## Output contract

Return a design result that identifies:

- design question and accepted objective;
- verified constraints and unresolved assumptions;
- goals / non-goals / anti-goals when material;
- options considered and why the selected option wins;
- user/project decisions vs agent implementation calls;
- spike/research evidence if used;
- affected authorities/interfaces/data ownership;
- durable document/section if one was created or updated;
- task reconciliation required: `YES | NO`;
- unresolved decisions that block implementation.

Do not return an implementation transcript, duplicate `CURRENT_TASK.md`, or silently create a second execution plan authority.
