---
name: design
description: Use for bounded UI/UX and frontend visual-design work: create or redesign interfaces, establish aesthetic direction, typography/layout/visual hierarchy, or critique visual execution. Do not use it for task authority, engineering architecture/state-ownership ambiguity, or formal independent release/readiness evidence verdicts.
---

# Design

Use this Skill as Engineering Governance's stable routed design capability. It owns bounded product-interface and frontend visual-design reasoning; it does not become a second task authority or replace project-specific product/design facts.

## Current module state

The active baseline is the bundled Anthropic `frontend-design` source module:

- read `references/anthropic/frontend-design.md` in full for design/redesign/visual-critique work;
- preserve project/user instructions over generic source guidance;
- source provenance and modification status are recorded in `references/anthropic/PROVENANCE.md`;
- Apache-2.0 terms are preserved in `references/anthropic/LICENSE.txt`.

The Anthropic module is intentionally bundled as source material inside this Skill rather than installed as a separate Plugin. The external route is `design`, so future source modules can be composed behind the same stable capability boundary.

See `references/module-map.md` for active/planned module responsibilities. Planned modules are not active behavior until their source and acceptance are actually added.

## Routing boundary

Use `design` when the requested outcome is primarily one or more of:

- design a new frontend page, screen, component composition, landing page, storefront surface, or product UI;
- redesign an existing interface because visual hierarchy, typography, layout, density, repetition, composition, responsiveness, or interface copy is weak;
- establish a distinctive visual direction before implementation;
- critique the visual/aesthetic execution of an implemented interface and propose bounded design corrections.

Do **not** route here merely because the word “design” appears in an engineering task.

Keep these authorities separate:

- `project-governance` — task/control authority, lifecycle, writers/workspaces, verification and closeout;
- `solution-design` — material engineering requirements, architecture, state ownership, APIs/data-flow/implementation-boundary choices;
- `design` — bounded UI/UX/frontend visual-design choices;
- `evidence-audit` — formal independent/read-only evidence, acceptance, or readiness verdicts when that outcome is explicitly requested.

When a governed implementation task needs both engineering and frontend design, Project Governance remains the task owner and invokes Design only for the bounded design decision/output before implementation continues.

## Project authority and evidence

Before applying generic design guidance, use the project's real authority when available: product intent, user/audience, approved content, existing design tokens/components, brand rules, accepted screenshots/baselines, accessibility requirements, and implementation constraints. Never invent a Figma/design-system authority that the project does not actually have.

Design output is a proposal or bounded design decision unless the project's own authority says otherwise. It does not silently overwrite requirements, business facts, content authority, or task scope.

## Current limitations

This baseline does **not** yet claim:

- Microsoft design-review / design-system adaptation integration;
- the planned UX heuristic/severity audit module;
- a complete formal design-acceptance gate;
- Figma, browser, screenshot, or prototype tooling availability in every environment.

Use only capabilities that actually exist in the current environment and state unknowns explicitly.
