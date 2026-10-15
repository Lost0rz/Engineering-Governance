---
name: design
description: Use for bounded UI/UX and frontend visual-design work: audit interfaces, create or redesign frontend experiences, establish implementation-ready design specifications, compose admin/product UI patterns, implement bounded design changes, or perform final frontend design review. Do not use it for task authority, unresolved engineering architecture/state ownership, or formal independent release/readiness evidence verdicts.
---

# Design

Use this Skill as Engineering Governance's stable routed capability for bounded product-interface and frontend visual-design work. Design owns interaction/workflow presentation, page-pattern composition, visual-system specification, bounded implementation guidance and internal visual review for the interface problem it receives.

The external capability route remains `design`. Anthropic, shadcn-admin, awesome-design-md and Microsoft are **internal Design modules**, not peer top-level Skills.

Design is the primary owner after entry, but it is **not isolated**. When a concrete unresolved dependency crosses another Engineering Governance capability boundary, Design may call that capability, consume the bounded result, and resume from the suspended Design stage.

## Route discriminator

Route to `design` when the unresolved problem is materially about **interaction workflow or frontend presentation**, including:

- how users understand, navigate, edit, review, compare or complete a frontend task;
- information architecture and page composition;
- visual hierarchy, typography, layout, density, spacing, surfaces and responsive behavior;
- action hierarchy, disclosure, form/table/editor composition and frontend state presentation;
- visual differentiation between source/read-only facts, editable content, generated content, status and feedback;
- an implementation-ready frontend design specification;
- visual critique or bounded correction of an implemented interface.

Do **not** route to Design merely because frontend files are touched or the word “design” appears.

Keep this discriminator explicit:

```text
INTERACTION_WORKFLOW
How the user sees, understands, navigates, edits, acts and receives feedback.
Owner: design

BUSINESS_STATE_WORKFLOW
Canonical state transitions, data/state ownership, API/data-flow responsibility,
persistence semantics, implementation boundaries or other engineering ownership.
Owner: solution-design when materially ambiguous
```

A simple understood frontend bug with no material design ambiguity can remain in Project Governance. A mixed task may use Solution Design and Design only when both material problems actually exist; resolve a blocking business/state prerequisite before continuing the affected Design decision.

## Design modes

Select the smallest mode that matches the requested outcome. Do not force every Design request through implementation.

### `AUDIT_ONLY`

Use when the user wants a design/UI/UX inspection, diagnosis or findings without a new design package or implementation.

Flow:

`context intake → actual interface audit → findings / classification → stop`

Do not implement merely to make the audit feel complete. If the audit reveals a separate unresolved dependency, use evidence-triggered composition only when resolving that dependency is required to make the requested audit finding reliable.

### `DESIGN_SPEC`

Use when the user wants the page/flow designed or redesigned but implementation is not yet requested/authorized.

Flow:

`context intake → actual interface audit → Anthropic reasoning → admin pattern when applicable → bounded design-spec synthesis → pre-build gate → stop`

### `DESIGN_IMPLEMENT`

Use when the bounded design/redesign should be carried through implementation or prototype and internal visual acceptance.

Flow when rendered evidence is supported:

`context intake → actual interface audit → Anthropic reasoning → admin pattern when applicable → bounded design-spec synthesis → pre-build gate → implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`

When rendered evidence is unavailable, do not fabricate it; Microsoft review and final acceptance must expose the limitation.

### `FINAL_REVIEW`

Use when a concrete implementation/prototype already exists and the requested outcome is a bounded final Design review/correction, not a new upstream design direction.

Flow:

`context + existing design authority → implementation/render evidence → Microsoft final review → bounded correction if authorized/needed → re-render/re-review → final visual acceptance`

Do not automatically rerun Anthropic/Admin/Awesome merely because those modules exist. Reopen upstream design reasoning only when the review identifies a material design defect that cannot be corrected safely from the existing design authority/specification.

Record the chosen mode as:

```text
DESIGN_MODE: AUDIT_ONLY | DESIGN_SPEC | DESIGN_IMPLEMENT | FINAL_REVIEW
```

## Evidence-triggered capability composition

Design stays inside Design by default. Crossing to another Engineering Governance Skill is allowed when a **specific unresolved dependency** materially affects the current Design decision.

A valid cross-Skill call must define all five fields before the call:

```text
UNRESOLVED_DEPENDENCY:
DESIGN_IMPACT:
CAPABILITY:
EXPECTED_RETURN:
RESUME_STAGE:
```

Rules:

1. `UNRESOLVED_DEPENDENCY` must be a concrete question that cannot be answered safely from current reliable context.
2. `DESIGN_IMPACT` states why the missing answer can materially change the Design result.
3. `CAPABILITY` is the smallest Skill that actually owns the missing answer.
4. `EXPECTED_RETURN` is bounded; do not ask the called Skill to redo the whole Design problem.
5. `RESUME_STAGE` names where Design continues after the result returns.

Valid examples:

- `domain-navigation` — the relevant backend/product authority, source, symbol, state owner, runtime entry, dependency or test route is not reliably identifiable;
- `solution-design` — the route is known but material business/state/API/data-flow/implementation ownership remains ambiguous;
- `agent-handoff` — responsibility/evidence must cross agent/session/machine/reviewer/execution context;
- `evidence-audit` — a separate formal independent acceptance/readiness verdict is explicitly required;
- `execution-orchestrator` — decomposition/delegation materially improves execution;
- `incident-doctor` — a blocking failure/evidence gap prevents a safe next Design or implementation decision;
- `project-profile` — only when the requested outcome itself becomes creation/rebuild/shrink/audit of the Profile; consuming an existing Profile is not such a trigger.

Invalid reasons to call another Skill:

- general enrichment;
- completeness or “use every available capability”;
- a second opinion with no material unresolved dependency;
- the page touches multiple business domains but the needed authority/route is already known;
- the other Skill is installed or adjacent to the topic;
- repeating a route or authority that Design already has reliable evidence for.

### Return-to-Design contract

A called capability returns only the bounded result it owns. After the result is sufficient:

```text
CALLED_CAPABILITY_RESULT: <bounded result>
DEPENDENCY_RESOLVED: YES | NO
RETURN_TO_DESIGN: YES
RESUME_STAGE: <previously named stage>
```

Resume from the affected stage. Do not restart Project Governance routing or rerun the entire Design pipeline solely because a bounded capability was consulted.

If the result materially changes task scope/authorization, return to Project Governance for reconciliation before mutation; otherwise continue Design directly.

## Project context and authority intake

Before generic design reasoning, establish the smallest reliable project context needed for the surface.

When an accepted Project Profile, Project Instructions or equivalent compact context is already present, use it directly for:

- product purpose and target audience;
- stable constraints and priorities;
- product/domain boundaries;
- authority pointers;
- design-relevant environment constraints.

Treat that Profile as **derived context and navigation**, never as canonical authority. Reading an existing Profile does not route through `project-profile`. Verify only underlying project authorities materially needed by the bounded Design problem.

Then inspect the strongest actual interface/source/rendered baseline available. Preserve existing:

- product and workflow facts;
- content/business authority;
- design tokens/components/brand rules;
- accessibility requirements;
- canonical state, APIs/schema, persistence and lifecycle semantics;
- implementation stack and accepted interaction conventions.

If one of those owners/routes is genuinely unclear and the answer matters to Design, use the evidence-triggered composition contract rather than guessing or forbidding the lookup.

Never invent a Figma, Storybook, design-system, product authority, backend intent or runtime fact that the target project does not actually have.

## Shared Design stages

The stages below apply according to `DESIGN_MODE`; they are not all mandatory for every mode.

### 1. Audit the actual surface

Establish as applicable:

- primary user/audience;
- primary job;
- page role in the surrounding workflow;
- current implementation/rendered baseline;
- applicable product/design/business constraints.

Audit material dimensions only:

- information and visual hierarchy;
- interaction workflow legibility and action hierarchy;
- grouping, ordering and progressive disclosure;
- page length, density, repetition and unnecessary containers;
- typography and copy hierarchy;
- layout, width, alignment, whitespace and responsive behavior;
- loading, empty, error, disabled, dirty/unsaved, success and permission states;
- accessibility-relevant visual/interaction issues;
- mismatch with existing project design authority.

Classify any issue that is actually a business/state/API/data-ownership ambiguity rather than visually papering over it.

For `AUDIT_ONLY`, this stage may be the terminal stage after findings are returned.

### 2. Anthropic design analysis

Required for material `DESIGN_SPEC` and `DESIGN_IMPLEMENT` work unless an accepted bounded design direction already exists and the task explicitly starts later in the pipeline.

Read `references/anthropic/frontend-design.md` in full when materially applicable and produce:

- `Design intent` — user, primary job, tone and intended interaction/visual character;
- `Hierarchy thesis` — what dominates, what recedes, and CTA relationships;
- `Composition thesis` — the page-level spatial idea rather than generic card stacking;
- `Typography / visual emphasis` — using project-approved type/tokens where authoritative;
- `Genericity check` — reject default AI/SaaS decoration that does not serve the brief;
- `Protected authority` — business/data/lifecycle facts Design must not alter.

For established products, translate Anthropic guidance into the existing design system instead of inventing a new palette/font family without authority.

### 3. Admin page-pattern composition when applicable

For admin/back-office/operational/productivity surfaces, read `references/shadcn-admin/admin-patterns.md` and classify the dominant page/workflow family.

Define as applicable:

- shell/navigation;
- header/context and primary action;
- main work surface;
- secondary context/rail/panel;
- toolbar/search/filter;
- table/form/editor/settings/dialog composition;
- state placement and feedback;
- responsive reflow;
- project component/token mapping.

This is an interaction/page-composition layer, not authority for backend state semantics. If a proposed UI depends on unknown state ownership or backend intent, resolve that dependency through the composition contract before encoding it into the design.

Record:

`ADMIN_PATTERN_LAYER: APPLIED | NOT_APPLICABLE`

Do not force admin patterns onto marketing, editorial or storefront surfaces.

### 4. Synthesize the bounded design specification

For `DESIGN_SPEC` / `DESIGN_IMPLEMENT`, read `references/awesome-design-md/design-spec-synthesis.md` and translate the established direction/composition into implementation-ready guidance covering applicable:

- visual character and density;
- semantic color roles using existing project tokens when authoritative;
- typography hierarchy;
- spacing/grid/content width/alignment;
- surfaces/elevation/borders/radius;
- component treatments and states;
- interaction/motion;
- responsive behavior;
- accessibility-relevant visual rules;
- explicit Do / Don't constraints;
- implementation mapping to existing project components/tokens.

External brand DESIGN.md examples remain optional conceptual references only. Do not clone another brand, assume asset/font rights, or promote external design references over project authority.

Default to a bounded task-level specification. Create/update durable project `DESIGN.md` only when project-wide design authority is explicitly in scope and accepted by the target project.

### 5. Pre-build design gate

Required before implementation in `DESIGN_IMPLEMENT` and terminal for `DESIGN_SPEC`.

Verify:

- the design is specific to this product/user/job;
- composition and CTA hierarchy are coherent;
- admin patterns are applied only when appropriate;
- specification is concrete enough to guide implementation;
- unnecessary cards/badges/borders/gradients/motion are rejected;
- protected product/business/data/design authority is preserved;
- source facts, generated content, editable content and system status are differentiated where material;
- interaction and relevant state behavior are covered;
- any cross-Skill dependency needed for safe implementation is resolved or explicitly blocks progress.

Record:

`PRE_BUILD_DESIGN_GATE: PASS | BLOCKED`

### 6. Implement or prototype

Applies to `DESIGN_IMPLEMENT`, or to `FINAL_REVIEW` corrective work when mutation is authorized.

Use the smallest implementation boundary appropriate to the task:

- existing real page when safe/authorized;
- isolated/static prototype when composition uncertainty warrants it;
- existing component library/design tokens where available.

Implementation must realize the Design package rather than silently replacing it with easiest-local CSS/JSX choices. Preserve canonical business/state/API semantics unless a separately routed capability has resolved an authorized change.

### 7. Capture rendered evidence when supported

Before Microsoft final review, capture/inspect the strongest rendered evidence the environment actually supports:

- exact implementation/prototype identity;
- representative whole-surface viewport(s);
- material responsive states;
- important loading/empty/error/disabled/dirty/saving/generated/published/read-only states when available/in scope.

Record:

`RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE`

A passing functional browser test is not rendered visual evidence. If rendering is unavailable, state the limit and continue only to the evidence strength allowed by the target project's acceptance contract.

### 8. Microsoft final Design review

After a concrete prototype/implementation exists and rendered evidence has been captured when supported, read `references/microsoft/final-review.md`.

Microsoft is **review-only** here. Do not use its Creative Frontend Design mode as a competing upstream aesthetic direction.

Review:

- user task/action efficiency;
- actual project design-system/brand authority;
- bounded Design package;
- implementation source;
- rendered evidence when supported;
- responsive/accessibility evidence;
- trust/error/AI-generated-content treatment when material.

Classify findings:

- `Blocking` — must fix before Design completion;
- `Major` — fix in the current Design pass;
- `Minor` — non-blocking refinement.

Open Blocking/Major findings require correction. After correction, re-render affected surfaces when rendering is supported and rerun Microsoft review before final acceptance.

Never claim Figma/Storybook/token/render/accessibility evidence that was not available.

### 9. Final visual acceptance

This is the terminal internal Design gate for `DESIGN_IMPLEMENT` and `FINAL_REVIEW` when visual acceptance is applicable.

When rendered inspection is supported:

1. inspect the final corrected implementation identity;
2. confirm affected representative viewports/states were re-rendered after material corrections;
3. confirm Microsoft has no open Blocking/Major finding;
4. compare the final surface with the bounded Design package and user task;
5. ensure no new material hierarchy, density, alignment, typography, CTA, state, responsive or accessibility regression is visible.

Record:

`VISUAL_ACCEPTANCE: PASS | UNAVAILABLE | NOT_APPLICABLE`

Do not fabricate PASS when evidence is unavailable. Lack of rendering does not automatically block otherwise valid work unless the target project's acceptance contract requires it.

## Mode-aware completion gates

### `AUDIT_ONLY`

```text
DESIGN_MODE: AUDIT_ONLY
DESIGN_CONTEXT_INTAKE: YES
INTERFACE_AUDIT_COMPLETED: YES
DESIGN_FINDINGS_RETURNED: YES
PROTECTED_AUTHORITY_PRESERVED: YES
CROSS_SKILL_CALLS: NONE | BOUNDED_AND_RESOLVED | BLOCKED
```

### `DESIGN_SPEC`

```text
DESIGN_MODE: DESIGN_SPEC
DESIGN_CONTEXT_INTAKE: YES
PROFILE_DERIVED_NOT_AUTHORITY: YES | NOT_APPLICABLE
INTERFACE_AUDIT_COMPLETED: YES
ANTHROPIC_ANALYSIS_COMPLETED: YES | EXISTING_DIRECTION_REUSED
ADMIN_PATTERN_LAYER: APPLIED | NOT_APPLICABLE
DESIGN_SPEC_SYNTHESIZED: YES
PRE_BUILD_DESIGN_GATE: PASS
PROTECTED_AUTHORITY_PRESERVED: YES
CROSS_SKILL_CALLS: NONE | BOUNDED_AND_RESOLVED
```

### `DESIGN_IMPLEMENT`

```text
DESIGN_MODE: DESIGN_IMPLEMENT
DESIGN_CONTEXT_INTAKE: YES
PROFILE_DERIVED_NOT_AUTHORITY: YES | NOT_APPLICABLE
INTERFACE_AUDIT_COMPLETED: YES
ANTHROPIC_ANALYSIS_COMPLETED: YES | EXISTING_DIRECTION_REUSED
ADMIN_PATTERN_LAYER: APPLIED | NOT_APPLICABLE
DESIGN_SPEC_SYNTHESIZED: YES
PRE_BUILD_DESIGN_GATE: PASS
PROTECTED_AUTHORITY_PRESERVED: YES
CROSS_SKILL_CALLS: NONE | BOUNDED_AND_RESOLVED
RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE | NOT_APPLICABLE
MICROSOFT_FINAL_REVIEW: PASS | LIMITED_BY_EVIDENCE
MICROSOFT_BLOCKING_FINDINGS_OPEN: NO
MICROSOFT_MAJOR_FINDINGS_OPEN: NO
CORRECTIVE_PASS_COMPLETED_IF_NEEDED: YES | NOT_NEEDED | UNAVAILABLE
VISUAL_ACCEPTANCE: PASS | UNAVAILABLE | NOT_APPLICABLE
```

### `FINAL_REVIEW`

```text
DESIGN_MODE: FINAL_REVIEW
DESIGN_CONTEXT_INTAKE: YES
EXISTING_IMPLEMENTATION_REVIEWED: YES
RENDERED_EVIDENCE: AVAILABLE | UNAVAILABLE
MICROSOFT_FINAL_REVIEW: PASS | LIMITED_BY_EVIDENCE
MICROSOFT_BLOCKING_FINDINGS_OPEN: NO
MICROSOFT_MAJOR_FINDINGS_OPEN: NO
CORRECTIVE_PASS_COMPLETED_IF_NEEDED: YES | NOT_NEEDED | UNAVAILABLE
VISUAL_ACCEPTANCE: PASS | UNAVAILABLE | NOT_APPLICABLE
```

## Evidence limitations

Design owns its internal critique, but evidence strength still matters. If source, route, authority, render, viewport, state, design-system or runtime evidence is missing, mark the affected conclusion limited/unknown or invoke the narrowly owning capability when its trigger is met.

A separate formal independent release/readiness verdict remains `evidence-audit` when explicitly requested. Microsoft's internal review does not change that authority boundary.
