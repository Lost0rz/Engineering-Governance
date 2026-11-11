# Design specification — selected DESIGN_SPEC / DESIGN_IMPLEMENT

Only load after Design selects a specification/implementation task. Start from the entry Skill's bounded context and interface audit; apply only stages relevant to the actual UI and reuse accepted design direction. This document is not required for AUDIT_ONLY or FINAL_REVIEW.

### 2. Anthropic design analysis

Required for material `DESIGN_SPEC` and `DESIGN_IMPLEMENT` work unless an accepted bounded design direction already exists and the task explicitly starts later in the pipeline.

Read `anthropic/frontend-design.md` in full when materially applicable and produce:

- `Design intent` — user, primary job, tone and intended interaction/visual character;
- `Hierarchy thesis` — what dominates, what recedes, and CTA relationships;
- `Composition thesis` — the page-level spatial idea rather than generic card stacking;
- `Typography / visual emphasis` — using project-approved type/tokens where authoritative;
- `Genericity check` — reject default AI/SaaS decoration that does not serve the brief;
- `Protected authority` — business/data/lifecycle facts Design must not alter.

For established products, translate Anthropic guidance into the existing design system instead of inventing a new palette/font family without authority.

### 3. Admin page-pattern composition when applicable

For admin/back-office/operational/productivity surfaces, read `shadcn-admin/admin-patterns.md` and classify the dominant page/workflow family.

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

For `DESIGN_SPEC` / `DESIGN_IMPLEMENT`, read `awesome-design-md/design-spec-synthesis.md` and translate the established direction/composition into implementation-ready guidance covering applicable:

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


## DESIGN_SPEC completion (only when claimed)

Ensure the task-level design is grounded, implementable, does not change protected state/data authority and has resolved material open design questions before implementation. A standalone specification does not grant implementation authorization. The evidence fields below are optional receipt detail, not a universal visible checklist.

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


