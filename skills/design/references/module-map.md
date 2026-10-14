# Design internal module map

`design` is the single externally routed Engineering Governance Skill for bounded UI/UX/frontend visual-design work. The sources below are internal modules/references behind that stable capability boundary; they are not peer top-level Skills and do not create independent project authority.

## Active modules

### 1. Anthropic `frontend-design` — design reasoning

Source: `references/anthropic/frontend-design.md`

Responsibilities:

- subject/product grounding before aesthetic choices;
- deliberate visual direction, typography, composition and hierarchy;
- anti-template / anti-generic-AI guidance;
- plan-before-build reasoning and pre-build self-critique.

Read the bundled source in full for material design/redesign work. Merely reading the Anthropic source is not sufficient evidence that Design ran; the required analysis/output in `../SKILL.md` must be produced.

### 2. shadcn-admin-informed patterns — conditional admin composition

Source: `references/shadcn-admin/admin-patterns.md`

Responsibilities:

- classify admin/back-office/productivity page families;
- choose shell, header/CTA, toolbar/search/filter, table/form/settings/editor/dialog and state composition;
- reduce mechanical vertical card stacking and clarify operational workflows;
- define responsive reflow and mapping to existing project components.

This layer is conditional. Use it when the surface is materially admin/back-office/productivity UI. Record `ADMIN_PATTERN_LAYER: NOT_APPLICABLE` for storefront, landing, editorial or other surfaces where those patterns would distort the product.

### 3. awesome-design-md-informed synthesis — bounded visual-system specification

Source: `references/awesome-design-md/design-spec-synthesis.md`

Responsibilities:

- convert design intent + page composition into a concrete implementation-ready visual system;
- specify visual character, semantic color roles, typography, spacing/layout, surfaces, components/states, responsive behavior, Do/Don't rules and agent implementation guidance;
- optionally support a durable project `DESIGN.md` only when the project explicitly authorizes project-wide design-system work.

External brand design documents are inspiration/reference only. Existing target-project brand/design-system authority wins.

### 4. Microsoft `frontend-design-review`-informed review — final Design audit

Source: `references/microsoft/final-review.md`

Responsibilities:

- review the concrete prototype/implementation after the design direction/specification exists;
- evaluate frictionless insight-to-action, quality craft, trustworthy building, design-system compliance, accessibility and responsive quality;
- classify findings as Blocking / Major / Minor;
- require correction and re-review for open Blocking/Major findings.

Only the review function is adapted here. Microsoft's creative-frontend mode is intentionally not used as a competing upstream design-direction stage because Anthropic owns that responsibility in this capability.

## Ordered composition

For qualifying design/redesign work:

`project/profile context intake → actual interface audit → Anthropic reasoning → admin patterns when applicable → visual-system/design-spec synthesis → implementation/prototype → Microsoft final review → corrective pass/re-review → rendered visual acceptance when supported`

This is an **internal Design pipeline**, not a global all-Skill pipeline. Project Governance routes the bounded interface problem to `design`; Design does not invoke `project-profile`, `domain-navigation`, `solution-design`, `evidence-audit` or `execution-orchestrator` unless their separate material triggers exist.

## Authority rules

- Project Profile / Project Instructions are compact derived context and pointers, not canonical authority.
- Target-project product, business, content, data/state, design-system and brand authorities win over every generic module here.
- No module may invent Figma, Storybook, tokens, runtime/render evidence or permissions that do not exist.
- A reference pattern never becomes authority merely because it is bundled in the Plugin.

## Deferred capability

A separate general-purpose UX heuristic research module remains optional/deferred. Do not add it merely to increase module count; first evaluate the quality of the active closed loop on real project work.
