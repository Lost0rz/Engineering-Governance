---
name: design
description: Use for bounded UI/UX and frontend visual-design work: audit, create or redesign interfaces, establish aesthetic direction and design specifications, compose admin/product UI patterns, or perform final frontend design review. Do not use it for task authority, engineering architecture/state-ownership ambiguity, or formal independent release/readiness evidence verdicts.
---

# Design

Use this Skill as Engineering Governance's stable routed design capability. It owns bounded product-interface/frontend visual-design reasoning, page-pattern composition, visual-system specification, implementation guidance and the design-to-visual-review loop for that bounded problem. It does not become a second task authority or replace project-specific product/design facts.

The external capability route remains `design`. Anthropic, shadcn-admin, awesome-design-md and Microsoft are **internal Design modules**, not peer Skills and not reasons to traverse other Engineering Governance domains.

## Active internal module stack

Read `references/module-map.md` for the compact responsibility map. For qualifying design/redesign work, use the active modules in this order:

1. **Project context intake + actual interface audit** — ground Design in the current product, user, workflow, existing implementation and applicable project authority.
2. **Anthropic `frontend-design`** — establish design reasoning, visual direction, hierarchy, typography/composition and anti-template critique. Read `references/anthropic/frontend-design.md` in full when materially applicable.
3. **shadcn-admin-informed admin patterns** — when the surface is admin/back-office/productivity UI, compose an appropriate page/workflow pattern from `references/shadcn-admin/admin-patterns.md`.
4. **awesome-design-md-informed design-spec synthesis** — translate the chosen direction and page composition into an explicit bounded visual system using `references/awesome-design-md/design-spec-synthesis.md`.
5. **Implementation / prototype** — realize the bounded design with the target project's existing stack, components and authorities.
6. **Microsoft-informed final review** — audit the implemented/resulting interface using `references/microsoft/final-review.md`; fix material findings and re-review before Design completion.
7. **Rendered visual acceptance** — inspect the corrected surface when the environment supports it and report limitations when it does not.

These modules provide specialized reasoning and reference patterns. They do not create new project authorities. Existing project product/design-system/brand/content/state authorities always win.

## Routing boundary

Use `design` when the requested outcome is primarily one or more of:

- audit, design or redesign a frontend page, screen, component composition, landing page, storefront surface, admin/back-office surface or product UI;
- resolve visual hierarchy, typography, layout, density, repetition, page composition, responsive behavior or interface-copy presentation;
- establish a distinctive visual direction or implementation-ready design specification;
- structure a complex admin workflow, form, table, settings surface, editor/detail page, toolbar or action hierarchy;
- critique the visual/aesthetic execution of an implemented interface and perform bounded design corrections.

Do **not** route here merely because frontend files are edited or the word “design” appears in an engineering task. A simple understood frontend bug with no material design ambiguity can stay in Project Governance.

Keep these authorities separate:

- `project-governance` — task/control authority, lifecycle, writers/workspaces, verification and closeout;
- `project-profile` — creation/rebuild/audit of compact derived Project Profile context, not a mandatory stage in Design;
- `solution-design` — material engineering requirements, architecture, state ownership, APIs/data-flow/implementation-boundary choices;
- `design` — bounded UI/UX/frontend visual-design choices and their internal design/review loop;
- `evidence-audit` — formal independent/read-only evidence, acceptance or readiness verdicts when explicitly requested.

When a governed implementation task needs frontend design, Project Governance remains task owner and routes the bounded interface problem to Design. Design then stays inside this internal module pipeline unless a materially separate capability trigger appears.

## Anti-shotgun composition rule

Do not invoke other installed Skills merely because the page has many domains, because a module name resembles another Skill, or because Design needs ordinary project context.

In particular:

- do not route to `project-profile` merely to consume an already-available Project Profile or Project Instructions;
- do not route to `domain-navigation` when relevant product/design authority and implementation surface are already identifiable;
- do not route to `solution-design` for ordinary information architecture, page/workflow composition, interaction hierarchy or frontend visual decisions;
- do not route to `evidence-audit` merely for Microsoft's internal final Design review or Design's own rendered critique;
- do not route to `execution-orchestrator` unless decomposition/delegation itself has material value.

Route away only when the other Skill's independent real trigger is satisfied. The goal is design depth, not maximum Skill count.

## Project context and authority intake

Before generic design reasoning, establish the smallest reliable project context needed for the surface.

When an accepted Project Profile, Project Instructions or equivalent compact project context is already present, read it first for:

- product purpose and target audience;
- stable constraints and priorities;
- product/domain boundaries;
- pointers to project-specific authority;
- design-relevant environment constraints.

Treat that Profile as **derived context and navigation**, never as canonical authority. Verify only the underlying project authorities materially needed by the bounded Design problem. Do not duplicate the full Profile into the Design deliverable.

Then inspect the actual interface/source/rendered baseline when available. Preserve existing:

- product and workflow facts;
- content/business authority;
- design tokens/components/brand rules;
- accessibility requirements;
- canonical state, APIs/schema, persistence and lifecycle semantics;
- implementation stack and accepted interaction conventions.

Never invent a Figma, Storybook, design-system or brand authority that the target project does not actually have.

## Mandatory Design closed loop

For a qualifying new design/redesign task, perform the following sequence. Reading references without producing their required outputs is not evidence that the module was used.

### 1. Audit the actual surface

Establish:

- primary user/audience;
- primary job the interface must help complete;
- page role in the surrounding workflow;
- current implementation/rendered baseline and applicable project constraints.

Audit only dimensions that materially apply:

- information and visual hierarchy;
- workflow legibility and action hierarchy;
- grouping, ordering and progressive disclosure;
- page length, density, repetition and unnecessary containers;
- typography and copy hierarchy;
- layout, width, alignment, whitespace and responsive behavior;
- loading, empty, error, disabled, dirty/unsaved, success and permission states;
- accessibility-relevant visual/interaction issues;
- mismatch between rendered UI and existing project design authority.

Separate UI/design problems from engineering authority problems. Do not visually paper over unresolved state/API/data-ownership ambiguity.

### 2. Anthropic design analysis

For material design/redesign work, read `references/anthropic/frontend-design.md` in full and apply it as the design-reasoning layer.

Produce an explicit direction covering:

- `Design intent` — user, primary job, tone and intended interaction/visual character;
- `Hierarchy thesis` — what must dominate, what recedes, and the primary/secondary CTA relationship;
- `Composition thesis` — the strong page-level spatial idea rather than a stack of generic cards;
- `Typography / visual emphasis` — deliberate roles using project-approved typography/tokens where authoritative;
- `Genericity check` — reject generic SaaS/admin decoration that does not serve the product/job;
- `Protected authority` — business/data/lifecycle facts Design must not alter.

For established products, translate Anthropic guidance into the existing design system instead of inventing a new palette/font family without authority.

### 3. Admin page-pattern composition when applicable

If the target is an admin, back-office, operational or productivity surface, read `references/shadcn-admin/admin-patterns.md` and classify the page/workflow family before choosing components.

The output must identify as applicable:

- shell/navigation model;
- page header/context and primary action;
- main work surface;
- secondary context/rail/panel;
- search/filter/toolbar behavior;
- table/form/editor/settings/dialog composition;
- state placement and feedback;
- responsive collapse/reflow;
- mapping to the target project's existing components/tokens.

Use these as composition patterns, not a visual template. Do not copy Shadcn styling by default and do not force this layer onto marketing, editorial or storefront surfaces where admin patterns do not materially apply.

Record `ADMIN_PATTERN_LAYER: APPLIED` or `NOT_APPLICABLE` with a short reason.

### 4. Synthesize the bounded design specification

Read `references/awesome-design-md/design-spec-synthesis.md` and turn the analysis/composition into an implementation-ready visual-system specification.

The specification must be concrete enough to prevent implementation from collapsing back into local CSS improvisation. Include the applicable portions of:

- visual character / atmosphere and density;
- semantic color roles using existing project tokens when authoritative;
- typography roles and hierarchy;
- spacing, grid, content width and alignment;
- surfaces, elevation, borders and radius behavior;
- component treatments and state variants;
- interaction/motion guidance;
- responsive behavior;
- accessibility-relevant visual rules;
- explicit `Do / Don't` constraints;
- implementation guidance mapping the design to the project's component/token system.

External brand DESIGN.md examples are inspiration/reference only. Do not clone another brand, assume its assets/fonts are licensed for use, or promote an external DESIGN.md over the target project's own design authority.

For a small bounded redesign, this can remain a concise task-level Design specification. For a project-wide visual-system task explicitly authorized by the project, it may become or update the project's own durable `DESIGN.md`.

### 5. Pre-build design gate

Before implementation/prototyping, verify the combined Design package:

- reflects this product/user/job rather than a generic pattern;
- has one coherent page composition and clear CTA hierarchy;
- uses the admin-pattern layer only where appropriate;
- has enough visual-system detail to guide implementation;
- avoids unnecessary cards, badges, labels, borders, gradients, motion and decorative containers;
- preserves project product/business/data/design authority;
- distinguishes source facts, generated content, editable content and system status where that distinction matters;
- covers important interaction and state behavior.

Revise before build if any of these fail.

### 6. Implement or prototype

Realize the bounded Design package using the target project's authorized implementation surface.

Use the smallest prototype/build boundary appropriate to the task:

- existing real page when the redesign is already authorized and safe to implement;
- isolated/static prototype when the visual composition is materially uncertain and a prototype would reduce rework;
- existing component library/design tokens where available.

Implementation must realize the Design decisions rather than silently replace them with easiest-local CSS/JSX choices. Preserve canonical state/API/business semantics unless a separately routed capability has explicitly changed them.

### 7. Microsoft final Design review

After a concrete prototype or implementation exists, read `references/microsoft/final-review.md` and perform the final internal Design audit.

This stage is deliberately **review-only**. Do not invoke Microsoft's creative-design mode as a second competing upstream aesthetic direction after Anthropic/admin/spec synthesis have established the design.

Review against:

- user task and action efficiency;
- target project's actual design-system/brand authority;
- the bounded Design package created above;
- rendered implementation when available;
- responsive/accessibility behavior supported by evidence;
- trust/error/AI-generated-content treatment when materially applicable.

Classify findings as:

- `Blocking` — must fix before Design completion;
- `Major` — material quality/workflow/design-system issue that should be fixed in the current Design pass;
- `Minor` — refinement that does not block completion.

If Blocking or Major findings exist, perform a bounded corrective pass and re-run the Microsoft review. Design cannot pass merely by listing known material findings.

Never claim Figma/Storybook/token/render evidence that was not actually available.

### 8. Rendered visual acceptance

When the environment supports browser/rendered-page screenshots or equivalent visual inspection:

1. inspect the exact implementation identity at representative viewport(s);
2. review the whole relevant surface rather than isolated components;
3. compare it with the bounded Design package and Microsoft review criteria;
4. correct material hierarchy, density, alignment, typography, CTA, state, responsive or accessibility regressions;
5. re-inspect before completion.

A functional browser regression alone is not visual acceptance.

If rendered visual evidence is unavailable, state `VISUAL_ACCEPTANCE: UNAVAILABLE`; do not fabricate it. Lack of rendering does not automatically block otherwise valid work unless the target project's acceptance contract requires rendered acceptance.

## Design completion gate

Before returning the bounded problem to Project Governance, verify:

```text
DESIGN_CONTEXT_INTAKE: YES
PROFILE_DERIVED_NOT_AUTHORITY: YES | NOT_APPLICABLE
INTERFACE_AUDIT_COMPLETED: YES
ANTHROPIC_ANALYSIS_COMPLETED: YES
ADMIN_PATTERN_LAYER: APPLIED | NOT_APPLICABLE
DESIGN_SPEC_SYNTHESIZED: YES
PRE_BUILD_DESIGN_GATE: PASS
PROTECTED_AUTHORITY_PRESERVED: YES
MICROSOFT_FINAL_REVIEW: PASS | LIMITED_BY_EVIDENCE
MICROSOFT_BLOCKING_FINDINGS_OPEN: NO
MICROSOFT_MAJOR_FINDINGS_OPEN: NO
SHOTGUN_ROUTING_AVOIDED: YES
VISUAL_ACCEPTANCE: PASS | UNAVAILABLE | NOT_APPLICABLE
CORRECTIVE_PASS_COMPLETED_IF_NEEDED: YES | NOT_NEEDED | UNAVAILABLE
```

For a qualifying redesign, do not claim Design completion if it skipped the explicit analysis/specification and went straight from reference reading to implementation.

## Evidence limitations

Design owns its internal critique, but evidence strength still matters. If source, render, viewport, state, design-system or runtime evidence is missing, mark the affected conclusion as limited/unknown rather than manufacturing certainty.

Use only capabilities that actually exist in the current environment. A separate formal independent readiness/release verdict still belongs to `evidence-audit` when explicitly requested; Microsoft's internal final review does not change that authority boundary.
