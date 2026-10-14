# Design module map

`design` is the stable routed capability. Internal source modules sit behind that route and become active only after explicit source review and acceptance.

## Active baseline

- Anthropic `frontend-design` — active baseline for subject grounding, visual direction, typography, layout/composition, interface copy, anti-template defaults, plan-before-build review and self-critique.

The Design wrapper is responsible for turning that source guidance into an executable bounded workflow: understand/diagnose → explicit Design deliverable → pre-build self-review → implementation → rendered visual critique/corrective pass when supported. Merely reading the Anthropic source is not sufficient evidence that the module was materially used.

## Planned modules

- Microsoft frontend design review/adaptation — planned, not active. Intended for design-system-aware review, implementation adaptation, and structured review output.
- UX heuristic audit source — planned, not active. Intended for usability/accessibility heuristics, severity, and acceptance-oriented review.

## Composition rule

Do not expose source modules as parallel external Skills. Route callers to `design`; Design selects only modules that are actually present and accepted.

Do not treat planned modules as required companions to Anthropic. A Design task should use the smallest accepted internal module set that fully owns the bounded problem.

Adding a planned module requires source/provenance review, scope reconciliation, conflict analysis against existing Design semantics, and acceptance evidence before its rules become active.
