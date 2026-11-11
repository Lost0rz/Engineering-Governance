# Durable plans and design decisions

A plan is useful when it resolves material architecture, API, state-ownership or multi-session ambiguity. Small, clear changes can proceed directly from the accepted task.

## Ownership

- `solution-design` helps resolve engineering choices; `design` owns actual UI/UX design decisions.
- Durable documents record **why** an accepted direction was chosen, key interfaces, alternatives/tradeoffs and impact. They do not create another authorization mode.
- `project-governance` owns execution task scope; code/schema owns implemented truth. A planning document is neither an Issue approval nor a source-write credential.

## When to record

Write the shortest useful decision note for cross-module interfaces, substantive irreversible design choices or work that another context will need to recover. Include objective, accepted decision, affected owners/interfaces, material risks, verification and remaining open choices. Link instead of copying entire tasks or GitHub comments.

Once a choice is accepted and stays within authority, implementation may proceed without new planning iterations. Reconcile the active task only when objective, side effects, material design ownership or risk envelope changes.

The plan remains reference context; implementation evidence, CI results, release and human UI acceptance are recorded by their actual owners.
