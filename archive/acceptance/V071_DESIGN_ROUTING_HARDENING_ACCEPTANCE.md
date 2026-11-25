# v0.7.1 Design routing hardening acceptance

Task: `EG-DESIGN-ROUTING-HARDENING-083`

Purpose: verify that the single routed `design` capability remains focused without becoming isolated, uses explicit execution modes, composes with other Engineering Governance capabilities only for concrete unresolved dependencies, and reviews rendered output in the correct order.

## A. Stable external route

Expected:

- ordinary engineering entry remains `project-governance`;
- bounded UI/UX/frontend interaction/visual work routes to `design`;
- Anthropic, shadcn-admin, awesome-design-md and Microsoft remain internal Design modules;
- exactly nine top-level Skills remain;
- no Router Skill or peer-controller mesh is added.

Acceptance markers:

`TOP_LEVEL_SKILL_COUNT: 9`

`DESIGN_EXTERNAL_ROUTE_ONLY: YES`

`DESIGN_INTERNAL_MODULES_ARE_TOP_LEVEL_SKILLS: NO`

## B. Interaction workflow vs business/state workflow

Scenario 1: the unresolved question is field grouping, page composition, CTA hierarchy, editing/review flow or frontend state presentation.

Expected: route to `design`.

Scenario 2: the unresolved question is canonical state transition, state/data ownership, API/data-flow responsibility, persistence semantics or implementation boundary.

Expected: route to `solution-design` when materially ambiguous.

Scenario 3: both material problems exist.

Expected: both may participate, but resolve a blocking business/state prerequisite before continuing the affected Design decision.

Acceptance markers:

`INTERACTION_WORKFLOW_OWNER: DESIGN`

`BUSINESS_STATE_WORKFLOW_OWNER_WHEN_AMBIGUOUS: SOLUTION_DESIGN`

`MIXED_FRONTEND_TASK_CAN_USE_BOTH: YES`

`KEYWORD_DESIGN_ALONE_ROUTES_TO_DESIGN: NO`

## C. Design modes

Design must support four purpose-specific modes:

- `AUDIT_ONLY` — context + actual interface audit + findings; stop;
- `DESIGN_SPEC` — audit + reasoning/pattern/spec + pre-build gate; stop before implementation;
- `DESIGN_IMPLEMENT` — full design-to-implementation/review/visual-acceptance loop;
- `FINAL_REVIEW` — review/correct an existing implementation without automatically reopening upstream design direction.

Acceptance markers:

`DESIGN_MODE_AUDIT_ONLY: YES`

`DESIGN_MODE_DESIGN_SPEC: YES`

`DESIGN_MODE_DESIGN_IMPLEMENT: YES`

`DESIGN_MODE_FINAL_REVIEW: YES`

`AUDIT_ONLY_FORCES_IMPLEMENTATION: NO`

`DESIGN_SPEC_FORCES_IMPLEMENTATION: NO`

`FINAL_REVIEW_FORCES_FULL_UPSTREAM_REDESIGN: NO`

## D. Evidence-triggered cross-Skill composition

Design stays primary owner after entry but may call another Skill when a concrete unresolved dependency materially affects the current Design decision.

Every valid cross-Skill call must identify:

```text
UNRESOLVED_DEPENDENCY
DESIGN_IMPACT / DECISION_IMPACT
CAPABILITY
EXPECTED_RETURN
RESUME_STAGE / RESUME_OWNER_OR_STAGE
```

Expected:

- `domain-navigation` is legitimate when needed backend/product authority, source, symbol, state owner, runtime entry, dependency or test route is genuinely unclear;
- `solution-design` is legitimate when the route is known but material business/state/API/data-flow ownership remains ambiguous;
- `agent-handoff`, `evidence-audit`, `execution-orchestrator`, and `incident-doctor` remain available only on their real trigger;
- consuming an existing Project Profile does not trigger `project-profile`;
- no Skill is invoked for general enrichment, completeness, an unbounded second opinion or merely because it is installed.

Acceptance markers:

`CROSS_SKILL_COMPOSITION_ALLOWED_WHEN_TRIGGERED: YES`

`DOMAIN_NAVIGATION_ALLOWED_FOR_GENUINELY_UNCLEAR_ROUTE: YES`

`SOLUTION_DESIGN_ALLOWED_FOR_MATERIAL_STATE_OWNERSHIP_AMBIGUITY: YES`

`GENERAL_ENRICHMENT_TRIGGERS_SKILL: NO`

`INSTALLED_SKILL_TRIGGERS_SKILL: NO`

`EXISTING_PROFILE_FORCES_PROJECT_PROFILE_SKILL: NO`

## E. Return-to-origin contract

Expected:

- the called capability returns only the bounded result it owns;
- the originating capability resumes at the declared stage;
- a bounded dependency call does not restart the whole routing tree or full Design pipeline;
- Project Governance reconciliation is required only when returned evidence materially changes task scope/authorization.

Acceptance markers:

`BOUNDED_RETURN_REQUIRED: YES`

`RETURN_TO_ORIGINATING_CAPABILITY: YES`

`RESUME_STAGE_REQUIRED: YES`

`BOUNDED_CALL_RESTARTS_FULL_ROUTING_TREE: NO`

## F. Render-before-Microsoft final review

For `DESIGN_IMPLEMENT` or applicable `FINAL_REVIEW` work when rendered evidence is supported:

`implementation/prototype → rendered evidence capture → Microsoft final review → corrective pass → re-render → Microsoft re-review as needed → final visual acceptance`

Expected:

- Microsoft receives rendered evidence before its final review when the environment supports it;
- missing render evidence is declared unavailable/limited rather than fabricated;
- Blocking/Major fixes are re-rendered and re-reviewed when rendering is supported;
- final visual acceptance happens after the last Microsoft review/corrective cycle.

Acceptance markers:

`RENDERED_EVIDENCE_BEFORE_MICROSOFT_WHEN_SUPPORTED: YES`

`MICROSOFT_REVIEW_BEFORE_FINAL_VISUAL_ACCEPTANCE: YES`

`BLOCKING_MAJOR_FIX_REQUIRES_RERENDER_REREVIEW_WHEN_SUPPORTED: YES`

`FABRICATED_RENDER_EVIDENCE: NO`

## G. Prior Design modules and authority boundaries preserved

Expected:

- Anthropic source identity/provenance/license remains unchanged;
- shadcn-admin remains conditional admin/page-pattern guidance, not project authority;
- awesome-design-md remains bounded visual-system/design-spec synthesis, not external brand authority;
- Microsoft remains downstream review-only, not a competing creative-design authority;
- Project Profile remains derived context and underlying project authorities win;
- formal independent release/readiness verdicts remain `evidence-audit`.

Acceptance markers:

`ANTHROPIC_SOURCE_IDENTITY_PRESERVED: YES`

`ADMIN_PATTERN_CONDITIONAL: YES`

`EXTERNAL_BRAND_REFERENCE_IS_AUTHORITY: NO`

`MICROSOFT_CREATIVE_MODE_COMPETES_WITH_ANTHROPIC: NO`

`PROFILE_DERIVED_NOT_AUTHORITY: YES`

`FORMAL_EVIDENCE_AUDIT_AUTHORITY_PRESERVED: YES`

## H. Packaging / governance regression

Expected:

- Plugin payload remains `plugin.json + skills/**` only;
- historical v0.6.8/v0.6.9/v0.7.0 acceptance files remain present;
- Project Profile pre-return gate remains present;
- Agent Handoff card/receipt gates remain present;
- Project Governance route/used-Skill receipt remains mandatory;
- v0.7.1 source verification covers this hardening contract.

Acceptance markers:

`PLUGIN_PAYLOAD_PLUGIN_JSON_PLUS_SKILLS_ONLY: YES`

`PROJECT_PROFILE_PRIOR_GATES_PRESERVED: YES`

`AGENT_HANDOFF_PRIOR_GATES_PRESERVED: YES`

`ROUTE_RECEIPT_PRIOR_GATES_PRESERVED: YES`

`V070_ACCEPTANCE_PRESERVED: YES`
