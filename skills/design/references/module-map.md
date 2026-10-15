# Design internal module map

`design` is the single externally routed Engineering Governance Skill for bounded UI/UX/frontend visual-design work. The sources below are internal modules/references behind that stable capability boundary; they are not peer top-level Skills and do not create independent project authority.

## Design modes

Design does not force every request through one full pipeline.

- `AUDIT_ONLY` — context + actual interface audit + findings; stop before design/implementation unless separately requested.
- `DESIGN_SPEC` — audit + reasoning/pattern/specification + pre-build gate; stop before implementation.
- `DESIGN_IMPLEMENT` — full design-to-implementation/review/visual-acceptance loop.
- `FINAL_REVIEW` — review/correct an existing implementation without reopening upstream design direction unless a material defect requires it.

The active mode determines which modules/stages are actually needed.

## Active modules

### 1. Anthropic `frontend-design` — design reasoning

Source: `references/anthropic/frontend-design.md`

Responsibilities:

- subject/product grounding before aesthetic choices;
- deliberate visual direction, typography, composition and hierarchy;
- anti-template / anti-generic-AI guidance;
- plan-before-build reasoning and self-critique.

Use for material `DESIGN_SPEC` / `DESIGN_IMPLEMENT` work unless an accepted bounded design direction already exists and the task explicitly starts later in the pipeline.

### 2. shadcn-admin-informed patterns — conditional admin composition

Source: `references/shadcn-admin/admin-patterns.md`

Responsibilities:

- classify admin/back-office/productivity page families;
- choose shell, header/CTA, toolbar/search/filter, table/form/settings/editor/dialog and state composition;
- reduce mechanical vertical card stacking and clarify interaction workflows;
- define responsive reflow and mapping to existing project components.

This layer is conditional. It owns frontend interaction/page composition, not backend business/state semantics.

### 3. awesome-design-md-informed synthesis — bounded visual-system specification

Source: `references/awesome-design-md/design-spec-synthesis.md`

Responsibilities:

- convert design intent + page composition into a concrete implementation-ready visual system;
- specify visual character, semantic color roles, typography, spacing/layout, surfaces, components/states, responsive behavior, Do/Don't rules and implementation guidance;
- optionally support a durable project `DESIGN.md` only when project-wide design-system authority is explicitly in scope.

External brand design documents are inspiration/reference only. Existing target-project brand/design-system authority wins.

### 4. Microsoft `frontend-design-review`-informed review — final Design audit

Source: `references/microsoft/final-review.md`

Responsibilities:

- review a concrete prototype/implementation after the design direction/specification exists;
- consume rendered evidence before the review when the environment supports it;
- evaluate frictionless insight-to-action, quality craft, trustworthy building, design-system compliance, accessibility and responsive quality;
- classify findings as Blocking / Major / Minor;
- require correction, re-render and re-review for open Blocking/Major findings when rendering is supported.

Only the review function is adapted here. Microsoft's creative-frontend mode is intentionally not used as a competing upstream design-direction stage because Anthropic owns that responsibility in this capability.

## Ordered composition

For `DESIGN_IMPLEMENT` when rendered evidence is supported:

`project/profile context intake → actual interface audit → Anthropic reasoning → admin patterns when applicable → visual-system/design-spec synthesis → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`

For other modes, stop at the mode's declared boundary instead of forcing the remaining stages.

## Evidence-triggered cross-Skill composition

Design remains primary owner after entry, but it is not isolated. A separate Engineering Governance Skill may be called when a concrete unresolved dependency materially affects the current Design decision.

Before such a call, identify:

```text
UNRESOLVED_DEPENDENCY:
DESIGN_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_STAGE:
```

Typical legitimate calls:

- `domain-navigation` — relevant authority/source/symbol/state-owner/runtime/test route is genuinely unclear;
- `solution-design` — the route is known but material business/state/API/data-flow ownership remains unresolved;
- `agent-handoff` — a bounded transfer crosses execution contexts;
- `evidence-audit` — a separate formal readiness/acceptance verdict is explicitly required;
- `execution-orchestrator` — decomposition/delegation materially improves execution;
- `incident-doctor` — a blocking evidence gap prevents a safe next action.

Do not call another Skill for general enrichment, completeness, a second opinion with no unresolved dependency, or merely because it is installed.

After the bounded result returns, resume at `RESUME_STAGE`. Do not restart the whole Design pipeline solely because another capability was consulted.

## Design vs Solution Design

```text
Interaction workflow
How users see, understand, navigate, edit, act and receive feedback.
Owner: design

Business/state workflow
Canonical state transitions, state/data ownership, API/data-flow responsibility,
persistence semantics and implementation boundaries.
Owner: solution-design when materially ambiguous
```

Both may participate only when both material problems actually exist.

## Authority rules

- Project Profile / Project Instructions are compact derived context and pointers, not canonical authority.
- Target-project product, business, content, data/state, design-system and brand authorities win over every generic module here.
- No module may invent Figma, Storybook, tokens, runtime/render evidence, backend intent or permissions that do not exist.
- A reference pattern never becomes authority merely because it is bundled in the Plugin.

## Deferred capability

A separate general-purpose UX heuristic research module remains optional/deferred. Do not add it merely to increase module count; first evaluate the quality of the active closed loop on real project work.
