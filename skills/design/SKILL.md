---
name: design
description: Use for bounded UI/UX and frontend visual-design work: audit interfaces, create or redesign frontend experiences, establish implementation-ready design specifications, compose admin/product UI patterns, implement bounded design changes, or perform final frontend design review. Do not use it for task authority, unresolved engineering architecture/state ownership, or formal independent release/readiness evidence verdicts.
---

# Design

Own bounded UI/UX interaction and visual design. Engineering state/API/data authority belongs to `solution-design` when materially ambiguous; Project Governance owns task authorization. External design frameworks are internal reference material, not additional top-level Skills.

## Mode routing — read only the selected procedure

| Requested outcome | Mode | Next reading |
| --- | --- | --- |
| Inspect UI, report issues only | `AUDIT_ONLY` | This entry is sufficient. |
| Design/redesign UI, no implementation | `DESIGN_SPEC` | [Design specification](references/design-specification.md) |
| Design and implement or prototype | `DESIGN_IMPLEMENT` | [Specification](references/design-specification.md); [implementation/review](references/design-review.md) **only when that stage is reached**. |
| Review/correct an existing interface | `FINAL_REVIEW` | [Final review](references/design-review.md); do not repeat upstream spec stages without a material defect. |

Do not read both detailed procedures to classify a request. Reuse established design direction and resume the affected stage instead of restarting the whole pipeline. A simple understood frontend bug without a design ambiguity remains normal Project Governance work.

## Minimal context and audit

Use the smallest reliable context: current user task, relevant UI/source/render evidence, accepted design-system tokens and owning product/domain facts. An existing Project Profile is **derived context**, not authority; consuming it does not invoke Project Profile. Never invent Figma, backend contracts or runtime evidence.

For `AUDIT_ONLY`, inspect the relevant flow and available surface. Assess material hierarchy, actions, information density, responsiveness, loading/error/read-only states and accessibility, then report bounded evidence/findings and STOP. Do **not** implement or run the full design/review pipeline merely for audit completeness.

Consult another Skill only for a concrete unresolved dependency (e.g. state ownership in Solution Design, unknown source route in Domain Navigation). Request a bounded answer and resume Design without rerouting the whole task. Detailed composition is optional in [module-map.md](references/module-map.md), not a required startup read.

## Safety and human UI acceptance

Automated Playwright/Cypress/E2E tests, AI browser/Computer Use, screenshots and Microsoft internal review can establish machine evidence **only**. They do not satisfy `HUMAN_UI_ACCEPTANCE`; when the owning project requires human product-interface acceptance, only an actual human decision can set `PASS` or `FAIL`, otherwise it remains `PENDING`. `NOT_REQUIRED` requires the owning acceptance contract to omit that gate. See [design-review.md](references/design-review.md) for relevant render/review fields.

An internal Design review is not formal independent `evidence-audit`. Never expand authorized writes because of a design decision, mode or handoff. Missing material evidence limits the claim.
