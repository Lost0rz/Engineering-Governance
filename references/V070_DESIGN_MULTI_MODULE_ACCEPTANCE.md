# v0.7.0 Design multi-module closed-loop acceptance

Task: `EG-DESIGN-MULTI-MODULE-CLOSED-LOOP-082`

Purpose: verify that the single routed `design` capability now executes an authority-safe, project-grounded, implementation-producing and independently reviewed internal pipeline instead of relying on one generic design reference or a cross-Skill shotgun workflow.

## A. Stable route and Project context

Scenario: a governed target project already has Project Instructions / an accepted Project Profile plus known product/code/design authorities, and the user asks for a material frontend redesign.

Expected:

- ordinary engineering entry remains `project-governance`;
- bounded UI/UX/frontend visual problem routes once to `design`;
- Design consumes already-available Project Profile/Instructions as compact derived context;
- consuming an existing Profile does not route through `project-profile`;
- Design verifies only materially needed underlying authority;
- Profile does not become product/design/business authority;
- unrelated Skills are not traversed as stages.

Acceptance markers:

`TOP_LEVEL_SKILL_COUNT: 9`

`DESIGN_EXTERNAL_ROUTE_ONLY: YES`

`PROJECT_PROFILE_CONTEXT_INTAKE: YES`

`PROFILE_DERIVED_NOT_AUTHORITY: YES`

`EXISTING_PROFILE_FORCES_PROJECT_PROFILE_SKILL: NO`

`ROUTING_SELECTIVE_NOT_CUMULATIVE: YES`

## B. Ordered internal Design pipeline

For qualifying material design/redesign work, Design owns this order:

`project/profile context intake → actual interface audit → Anthropic reasoning → admin pattern composition when applicable → DESIGN.md visual-system synthesis → implementation/prototype → Microsoft final review → corrective pass/re-review → rendered visual acceptance when supported`

Expected:

- reading modules without producing their required outputs is not sufficient;
- modules are internal to `design`, not new top-level Skills/plugins;
- actual implementation/prototype follows an explicit bounded Design package rather than going directly from discussion to code.

Acceptance markers:

`DESIGN_INTERNAL_ORDER_EXPLICIT: YES`

`INTERNAL_MODULES_ARE_TOP_LEVEL_SKILLS: NO`

`DIRECT_REFERENCE_TO_CODE_WITHOUT_DESIGN_PACKAGE: NO`

`DESIGN_IMPLEMENTATION_OR_PROTOTYPE_STAGE: YES`

## C. Anthropic reasoning layer

Expected:

- bundled Anthropic source remains the upstream design-reasoning layer;
- exact local source body identity from v0.6.9 remains unchanged;
- provenance/license remain packaged;
- Anthropic establishes design intent, hierarchy/composition, visual direction, genericity critique and protected authority before implementation.

Acceptance markers:

`ANTHROPIC_ACTIVE_REASONING_MODULE: YES`

`ANTHROPIC_SOURCE_IDENTITY_PRESERVED: YES`

`ANTHROPIC_ANALYSIS_BEFORE_PATTERN_AND_SPEC: YES`

## D. Conditional admin pattern layer

Scenario 1: existing admin product-authoring/settings/data-management page.

Expected:

- classify admin page/workflow family;
- define shell/navigation, header/CTA, main work surface, supporting context, toolbar/search/filter, table/form/editor/dialog pattern, states and responsive reflow;
- map the pattern into target-project components/tokens;
- avoid generic equal-card stacking and competing primary actions.

Scenario 2: consumer storefront/marketing/landing surface.

Expected:

- admin module reports `NOT_APPLICABLE` unless an actual admin/productivity pattern is present;
- do not add sidebar/table/settings patterns just because the module exists.

Acceptance markers:

`ADMIN_PATTERN_MODULE_ACTIVE: YES`

`ADMIN_PATTERN_CONDITIONAL: YES`

`ADMIN_PATTERN_FOR_ADMIN_SURFACE: APPLIED`

`ADMIN_PATTERN_FOR_STOREFRONT_BY_DEFAULT: NOT_APPLICABLE`

`SHADCN_VISUAL_STYLE_BECOMES_PROJECT_AUTHORITY: NO`

## E. DESIGN.md / visual-system synthesis layer

Expected:

- synthesize target-project guidance from current Design decisions and existing project authority;
- cover applicable visual character, semantic color roles, typography, layout/spacing, surfaces/elevation/borders/radius, component/state treatment, interaction/motion, responsive behavior, accessibility-relevant rules, Do/Don't constraints and implementation mapping;
- use existing project tokens/components before introducing new values/primitives;
- external brand references remain optional inspiration only;
- a task-level spec is the default for bounded page work;
- durable project `DESIGN.md` is created/updated only when project-wide design authority is explicitly in scope.

Acceptance markers:

`DESIGN_SPEC_SYNTHESIS_MODULE_ACTIVE: YES`

`EXISTING_PROJECT_DESIGN_AUTHORITY_WINS: YES`

`EXTERNAL_BRAND_REFERENCE_IS_AUTHORITY: NO`

`BRAND_CLONING_REQUIRED: NO`

`DURABLE_PROJECT_DESIGN_MD_ALWAYS_REQUIRED: NO`

## F. Microsoft final review layer

Expected:

- Microsoft's review function is downstream of concrete prototype/implementation;
- Creative Frontend Design mode is not re-run as a competing aesthetic direction;
- review evaluates user task, real project design-system compliance when evidence exists, Frictionless, Quality Craft, Trustworthy, responsive and accessibility-relevant evidence;
- missing Figma/Storybook/render evidence is marked limited rather than fabricated;
- findings are prioritized Blocking / Major / Minor;
- Blocking or Major findings trigger correction and re-review before Design completion.

Acceptance markers:

`MICROSOFT_FINAL_REVIEW_MODULE_ACTIVE: YES`

`MICROSOFT_CREATIVE_MODE_COMPETES_WITH_ANTHROPIC: NO`

`MICROSOFT_REVIEW_AFTER_IMPLEMENTATION_OR_PROTOTYPE: YES`

`MICROSOFT_SEVERITY_MODEL: BLOCKING_MAJOR_MINOR`

`MICROSOFT_BLOCKING_OR_MAJOR_REQUIRES_CORRECTIVE_REREVIEW: YES`

`MISSING_FIGMA_OR_STORYBOOK_CAN_BE_FABRICATED: NO`

## G. Rendered visual acceptance and evidence limits

When the environment supports rendered-page/browser/screenshot inspection:

- inspect representative whole-surface viewports;
- compare implementation with the bounded Design package and final review;
- functional regression alone is not visual acceptance;
- correct material visual regressions and re-inspect.

When unavailable:

- explicitly report `VISUAL_ACCEPTANCE: UNAVAILABLE`;
- do not fabricate evidence;
- do not automatically block valid work unless target-project acceptance requires rendered evidence.

Acceptance markers:

`RENDERED_VISUAL_CRITIQUE_REQUIRED_WHEN_SUPPORTED: YES`

`FUNCTIONAL_BROWSER_TEST_EQUALS_VISUAL_ACCEPTANCE: NO`

`VISUAL_ACCEPTANCE_UNAVAILABLE_MUST_BE_EXPLICIT: YES`

`FABRICATED_RENDER_EVIDENCE: NO`

## H. Simple bug / separate capability boundaries

Expected:

- a fully understood frontend bug with no material design ambiguity does not force Design;
- engineering architecture/state/API/data-flow ambiguity still belongs to `solution-design`;
- formal independent release/readiness evidence verdict still belongs to `evidence-audit` when explicitly requested;
- Design's Microsoft internal review does not automatically invoke Evidence Audit.

Acceptance markers:

`SIMPLE_FRONTEND_BUG_FORCES_DESIGN: NO`

`SOLUTION_DESIGN_ARCHITECTURE_AUTHORITY_PRESERVED: YES`

`MICROSOFT_INTERNAL_REVIEW_FORCES_EVIDENCE_AUDIT: NO`

`FORMAL_EVIDENCE_AUDIT_AUTHORITY_PRESERVED: YES`

## I. Upstream provenance / packaging

The distributed Plugin includes compact adapted modules and their adjacent provenance/license records:

- Anthropic `frontend-design` — existing Apache-2.0 bundled source;
- `satnaing/shadcn-admin` — MIT-informed compact admin-pattern synthesis;
- `VoltAgent/awesome-design-md` — MIT-informed compact design-spec synthesis;
- Microsoft `frontend-design-review` — MIT-informed compact downstream final review.

Expected:

- entire shadcn-admin / awesome-design-md / microsoft repositories are not vendored;
- Plugin payload remains exactly `plugin.json + skills/**`;
- repository controls/references/workflows remain outside Plugin ZIP;
- local license/provenance files are included with their modules.

Acceptance markers:

`SHADCN_ADMIN_WHOLE_REPO_VENDORED: NO`

`AWESOME_DESIGN_MD_WHOLE_REPO_VENDORED: NO`

`MICROSOFT_SKILLS_WHOLE_REPO_VENDORED: NO`

`ADAPTED_MODULE_LICENSES_AND_PROVENANCE_PACKAGED: YES`

`PLUGIN_PAYLOAD_PLUGIN_JSON_PLUS_SKILLS_ONLY: YES`

## J. Prior governance/receipt regression preservation

The release must preserve:

- exactly nine top-level Skills;
- Project Profile authority/pre-return rules;
- Agent Handoff card/receipt gates;
- Solution Design architecture/state-ownership authority;
- Project Governance selective routing and actual-route/actual-Skills-used receipts;
- Anthropic source identity/provenance/license;
- no automatic all-Skill pipeline.

Acceptance markers:

`PROJECT_PROFILE_PRIOR_GATES_PRESERVED: YES`

`AGENT_HANDOFF_PRIOR_GATES_PRESERVED: YES`

`DESIGN_RECEIPT_ROUTE_AND_SKILLS_OBSERVABLE: YES`

`PRIOR_RELEASE_GATES_PRESERVED: YES`
