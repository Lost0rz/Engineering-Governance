---
name: ui-design
description: >-
  Bounded UI/UX and frontend visual-design work: MICRO_POLISH component tweaks,
  interface audits (AUDIT_ONLY), flow composition on existing tokens
  (FLOW_WITH_TOKENS), full visual specs (FULL_DESIGN_SYSTEM), and screenshot
  QA (FINAL_REVIEW). Do not use for backend/API state ownership (architecture),
  non-visual frontend logic bugs (engineering-workflow), or formal release
  readiness verdicts (evidence-audit).
---

# UI Design

Own bounded product-interface workflow, hierarchy, visual craft, and rendered review.

## Fast route

| Requested outcome | Mode | Next reading |
| --- | --- | --- |
| Localized component, spacing, copy, or state polish | `MICRO_POLISH` | **NONE (this file)** — inspect target component + project tokens, implement, verify render/tests |
| Inspect UI and report findings without edits | `AUDIT_ONLY` | **NONE (this file)** — audit hierarchy, actions, density, responsive, empty/error/a11y states, stop |
| New dialog/drawer/form/page flow using **existing** tokens | `FLOW_WITH_TOKENS` | Reuse project tokens/components; read `references/shadcn-admin/admin-patterns.md` only for admin UIs; skip full visual synthesis |
| New aesthetic direction or full visual redesign | `FULL_DESIGN_SYSTEM` | [design-specification.md](references/design-specification.md) |
| Final review/fix from rendered UI or screenshots | `FINAL_REVIEW` | [design-review.md](references/design-review.md) |

## Boundaries

```text
INTERACTION_WORKFLOW — how users see, navigate, edit, act, and receive feedback -> ui-design
BUSINESS_STATE_WORKFLOW — canonical state, API/data ownership, persistence      -> architecture
```

- **Project authority wins:** reuse real project tokens, components, and brand rules; never invent Figma/Storybook/runtime evidence. An existing `PROJECT_PROFILE.md` is read directly without invoking `codebase-context`.
- **Non-visual frontend bugs** (e.g., date parsing, API payload wiring) stay in `engineering-workflow`.
- **Machine vs human UI acceptance:** Playwright/Cypress, Computer Use, screenshots, and Microsoft internal review are **machine evidence only**. When human product-interface acceptance is required, only an explicit human decision sets `HUMAN_UI_ACCEPTANCE` to `PASS` or `FAIL`; otherwise keep it `PENDING`.
