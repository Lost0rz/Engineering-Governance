---
name: design
description: >-
  Use for bounded UI/UX and frontend visual-design work: MICRO_POLISH component
  tweaks, interface audits (AUDIT_ONLY), page/flow specs (DESIGN_SPEC), full
  UI implementation (DESIGN_IMPLEMENT), or visual review (FINAL_REVIEW). Do not
  use for backend/API state ownership (solution-design), non-visual fixes, or
  formal release readiness verdicts (evidence-audit).
---

# Design

Own bounded UI/UX interaction and visual design. External design frameworks are internal reference material, not peer top-level Skills.

## Mode routing — read only the selected procedure

| Requested outcome | Mode | Next reading |
| --- | --- | --- |
| Localized component/spacing/state polish | `MICRO_POLISH` | This entry is sufficient. Inspect target component + project tokens, implement, verify render/tests, preserve `HUMAN_UI_ACCEPTANCE`. |
| Inspect UI, report issues only | `AUDIT_ONLY` | This entry is sufficient. |
| Design/redesign UI, no implementation | `DESIGN_SPEC` | [Design specification](references/design-specification.md) |
| Design and implement or prototype | `DESIGN_IMPLEMENT` | [Specification](references/design-specification.md); [implementation/review](references/design-review.md) **only when that stage is reached**. |
| Review/correct an existing interface | `FINAL_REVIEW` | [Final review](references/design-review.md); do not repeat upstream spec stages without a material defect. |

Do not read both detailed procedures to classify a request. Reuse established design direction and resume the affected stage instead of restarting the whole pipeline. A non-visual logic fix in a frontend file needs no Design pipeline.

## Interaction vs business-state boundary

```text
INTERACTION_WORKFLOW — how users see, understand, navigate, edit, act, and get feedback -> design
BUSINESS_STATE_WORKFLOW — canonical state transitions, API/data ownership, persistence   -> solution-design when ambiguous
```

## Minimal context and audit

Use the smallest reliable context: current user task, relevant UI/source/render evidence, accepted design-system tokens, and owning product/domain facts. An existing Project Profile is **derived context**, not authority; consuming it does not invoke `project-profile`. Never invent Figma, backend contracts, or runtime evidence.

For `AUDIT_ONLY`, inspect the relevant flow and available surface. Assess material hierarchy, actions, information density, responsiveness, loading/error/read-only states, and accessibility, then return bounded evidence/findings without mutation. Do **not** implement or run the full design/review pipeline merely for audit completeness.

Consult another Skill only for a concrete unresolved dependency (e.g., ambiguous state ownership -> `solution-design`, unknown source route -> `domain-navigation`), consume the bounded answer, and resume Design. Detailed module composition is optional in [module-map.md](references/module-map.md), not a required startup read.

## Safety and human UI acceptance

Automated Playwright/Cypress/E2E tests, AI browser/Computer Use, screenshots, and Microsoft internal review establish **machine evidence only**. When the owning project requires human product-interface acceptance, only an explicit human decision may set `HUMAN_UI_ACCEPTANCE` to `PASS` or `FAIL`; otherwise it remains `PENDING`. `NOT_REQUIRED` is valid only when the owning acceptance contract omits that gate. See [design-review.md](references/design-review.md) for stage-specific review fields.

An internal Design review is not formal independent `evidence-audit`, and Design modes never expand host write permissions.
