# Design module map

`design` is the stable routed capability. Internal source modules sit behind that route and become active only after explicit source review and acceptance.

## Active baseline

- Anthropic `frontend-design` — active baseline for visual direction, typography, layout/composition, interface copy, anti-template defaults, and the plan/build/self-critique loop.

## Planned modules

- Microsoft frontend design review/adaptation — planned, not active. Intended for design-system-aware review, implementation adaptation, and structured review output.
- UX heuristic audit source — planned, not active. Intended for usability/accessibility heuristics, severity, and acceptance-oriented review.

## Composition rule

Do not expose source modules as parallel external Skills. Route callers to `design`; Design selects only modules that are actually present and accepted.

Adding a planned module requires source/provenance review, scope reconciliation, conflict analysis against existing Design semantics, and acceptance evidence before its rules become active.
