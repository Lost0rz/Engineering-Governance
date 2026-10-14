---
name: design
description: Use for bounded UI/UX and frontend visual-design work: create or redesign interfaces, establish aesthetic direction, typography/layout/visual hierarchy, or critique visual execution. Do not use it for task authority, engineering architecture/state-ownership ambiguity, or formal independent release/readiness evidence verdicts.
---

# Design

Use this Skill as Engineering Governance's stable routed design capability. It owns bounded product-interface and frontend visual-design reasoning and the design-to-visual-review loop for that bounded problem. It does not become a second task authority or replace project-specific product/design facts.

## Current module state

The active baseline is the bundled Anthropic `frontend-design` source module:

- read `references/anthropic/frontend-design.md` in full for design/redesign/visual-critique work;
- apply its subject grounding, deliberate visual choices, anti-template guidance, typography/layout thinking, plan-before-build discipline and self-critique;
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
- `design` — bounded UI/UX/frontend visual-design choices and their visual acceptance loop;
- `evidence-audit` — formal independent/read-only evidence, acceptance, or readiness verdicts when that outcome is explicitly requested.

When a governed implementation task needs frontend design, Project Governance remains the task owner, but Design must complete the bounded design pass below before implementation continues. Reading this Skill or the Anthropic reference without performing that pass is not evidence that Design was actually used.

## Anti-shotgun composition rule

Once a bounded interface problem has routed to Design, keep the design work inside Design unless a **materially separate** capability boundary appears.

Do not invoke other installed Skills merely because they exist, because the page has many domains, or because Design needs ordinary project context. In particular:

- do not route to `domain-navigation` when the relevant product/design authority and implementation surface are already identifiable;
- do not route to `solution-design` for ordinary UI structure, information hierarchy, layout, component composition, interaction hierarchy or frontend visual decisions;
- do not route to `evidence-audit` merely to review Design's own implementation; Design owns its bounded visual critique loop;
- do not route to `execution-orchestrator` unless decomposition/delegation itself is materially useful.

Route away only when the separate Skill's real trigger is satisfied, then return to the governed task. The goal is capability depth, not maximum Skill count.

## Project authority and evidence

Before applying generic design guidance, use the project's real authority when available: product intent, user/audience, approved content, existing design tokens/components, brand rules, accepted screenshots/baselines, accessibility requirements, and implementation constraints. Never invent a Figma/design-system authority that the project does not actually have.

Design output is a proposal or bounded design decision unless the project's own authority says otherwise. It does not silently overwrite requirements, business facts, content authority, canonical state, API/schema, persistence ownership, lifecycle semantics, or task scope.

For an established product/admin surface, preserve the existing design system unless the task explicitly authorizes changing it. Translate Anthropic's color/type planning into deliberate use of existing tokens, type roles and component primitives rather than inventing a new palette or font family without authority.

## Mandatory Design pass

For a qualifying new design/redesign task, perform this bounded sequence before implementation.

### 1. Understand

Establish only the design facts needed for the page/surface:

- primary user/audience;
- primary job the interface must help them complete;
- page role in the surrounding workflow;
- applicable content/business/design-system constraints;
- existing rendered implementation or baseline when available.

Do not reopen settled engineering/domain questions just to make the Design pass look comprehensive.

### 2. Diagnose

Inspect the actual interface/implementation and identify the material design problems. Consider only dimensions that apply, including:

- information and visual hierarchy;
- workflow legibility and action hierarchy;
- grouping, ordering and progressive disclosure;
- density, repetition and unnecessary containers;
- typography and copy hierarchy;
- layout, width, alignment, whitespace and responsive behavior;
- state presentation: loading, empty, error, disabled, dirty/unsaved, success;
- accessibility-relevant visual/interaction issues.

Separate genuine design problems from business/engineering authority problems. Do not solve the latter by visually papering over them.

### 3. Produce the bounded Design deliverable

Before code changes, form a concise implementation-ready design decision containing:

- `Design intent` — user, primary job and the intended interaction/visual character;
- `Page composition` — proposed information structure and, when useful, a compact ASCII wireframe or spatial description;
- `Hierarchy` — primary/secondary information and CTA/action hierarchy;
- `Visual system` — relevant typography, spacing, width/alignment, component/token decisions; include palette/type changes only when actually in scope;
- `Interaction/state treatment` — disclosure, editing, feedback and important state behavior;
- `Protected authority` — business/data/lifecycle facts this Design pass must not change.

This deliverable may be concise and need not become a new repository artifact unless project authority requires one. It must nevertheless exist as an explicit design decision before implementation.

### 4. Review against the brief before build

Apply Anthropic's second-pass self-review before implementation:

- Does the proposal reflect this product/user/job rather than a generic admin/SaaS pattern?
- Is it adding cards, badges, labels, borders, gradients, animation or decoration without informational purpose?
- Is the design solving hierarchy/workflow problems rather than merely restyling them?
- Is one strong compositional idea sufficient instead of many competing treatments?
- Does it fit the existing product/design system where that is authoritative?
- Does it preserve the protected business/engineering authorities?

Revise the design decision if this check finds a generic/default treatment.

### 5. Implement the approved bounded design

Implementation should realize the design decision, not silently replace it with the easiest local CSS/JSX edits. Keep changes inside the authorized task and preserve existing canonical ownership/lifecycle unless a separately routed capability has explicitly resolved a material engineering change.

### 6. Visual acceptance and corrective pass

For implemented visual/design work, use the best available rendered evidence.

When the environment supports browser/rendered-page screenshots or equivalent visual inspection:

1. inspect the exact implementation identity at representative viewport(s);
2. review the whole relevant surface, not only individual components;
3. check hierarchy, density, alignment, whitespace, typography, CTA competition, state duplication, responsive behavior and obvious accessibility regressions;
4. compare the rendered result against the bounded Design deliverable and the product brief;
5. correct material visual/design regressions found by that review;
6. re-inspect the corrected implementation before calling the Design pass complete.

A functional browser regression alone is not visual acceptance.

If rendered visual evidence is not available in the current environment, state that limitation explicitly. Do not fabricate screenshot/visual acceptance, and do not block an otherwise valid task solely because the environment lacks such tooling unless the project's acceptance contract requires it.

## Design completion gate

Before returning Design to Project Governance, verify:

```text
DESIGN_BASELINE_READ: YES
DESIGN_INTENT_ESTABLISHED: YES
DESIGN_DELIVERABLE_COMPLETED: YES
PRE_BUILD_SELF_REVIEW_COMPLETED: YES
PROTECTED_AUTHORITY_PRESERVED: YES
SHOTGUN_ROUTING_AVOIDED: YES
VISUAL_ACCEPTANCE: PASS | UNAVAILABLE | NOT_APPLICABLE
CORRECTIVE_PASS_COMPLETED_IF_NEEDED: YES | NOT_NEEDED | UNAVAILABLE
```

Do not claim Design completion if a qualifying redesign skipped the bounded Design deliverable and went directly from reading guidance to implementation.

## Current limitations

This baseline does **not** yet claim:

- Microsoft design-review / design-system adaptation integration;
- the planned UX heuristic/severity audit module;
- Figma, browser, screenshot, or prototype tooling availability in every environment.

Use only capabilities that actually exist in the current environment and state unknowns explicitly.
