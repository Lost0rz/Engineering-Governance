# v0.6.9 Design closed-loop + receipt acceptance

Task: `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081`

Purpose: verify that the existing routed Design capability executes the Anthropic baseline as a bounded design workflow rather than merely reading reference material, while Project Governance keeps routing selective and makes actual Skill composition observable in the final receipt.

## A. Design route depth — Merloom-like admin authoring redesign

Scenario:

- existing private admin page;
- business/data authorities are already known;
- user requests redesign because hierarchy, density, repeated sections, typography, CTA competition and state presentation are weak;
- implementation is authorized inside the current task/PR.

Expected:

- ordinary engineering entry remains `project-governance`;
- bounded interface problem routes to `design`;
- Anthropic `frontend-design` is read in full as the active Design module;
- Design establishes user/primary job/page role before proposing changes;
- Design produces an explicit implementation-ready Design deliverable before code changes;
- Design performs the pre-build genericity/brief review;
- existing product/design-system authority is preserved rather than replaced by an invented palette/font system;
- when rendered browser/screenshot evidence is available, Design performs whole-surface visual critique and a corrective pass if needed;
- functional browser regression alone is not treated as visual acceptance.

Acceptance markers:

`DESIGN_ROUTE_APPLIED: YES`

`ANTHROPIC_ACTIVE_MODULE_USED: YES`

`DESIGN_DELIVERABLE_REQUIRED_BEFORE_IMPLEMENTATION: YES`

`PRE_BUILD_SELF_REVIEW_REQUIRED: YES`

`RENDERED_VISUAL_CRITIQUE_REQUIRED_WHEN_SUPPORTED: YES`

`FUNCTIONAL_BROWSER_TEST_EQUALS_VISUAL_ACCEPTANCE: NO`

## B. No shotgun routing

For the scenario above, known project/business/design authorities are directly identifiable.

Expected:

- ordinary context lookup does not trigger `domain-navigation`;
- Design's own rendered visual critique does not trigger `evidence-audit`;
- `solution-design` is not used unless a materially separate architecture/state/API/data-flow ambiguity is actually present;
- installed Skills are not traversed as a linear checklist.

Acceptance markers:

`ROUTING_SELECTIVE_NOT_CUMULATIVE: YES`

`DOMAIN_NAVIGATION_BY_DEFAULT_WITH_DESIGN: NO`

`EVIDENCE_AUDIT_FOR_DESIGN_SELF_CRITIQUE: NO`

`SOLUTION_DESIGN_WITHOUT_ENGINEERING_AMBIGUITY: NO`

## C. Simple understood frontend bug

Scenario:

- exact bug and desired behavior are already known;
- no visual redesign or aesthetic/interface ambiguity exists.

Expected:

- remain in `project-governance` for ordinary governed implementation;
- do not manufacture a Design pass solely because frontend files are edited.

Acceptance marker:

`SIMPLE_FRONTEND_BUG_FORCES_DESIGN: NO`

## D. Legitimate multi-capability composition

Scenario:

- one material engineering architecture/state-ownership ambiguity exists;
- a separate material UI/frontend redesign problem also exists.

Expected:

- Project Governance may compose `solution-design` and `design` because two distinct bounded problems exist;
- neither Skill becomes task/lifecycle authority;
- composition is justified by separate triggers, not by a standard pipeline.

Acceptance marker:

`MULTI_SKILL_REQUIRES_DISTINCT_MATERIAL_TRIGGERS: YES`

## E. Visual tooling unavailable

Scenario:

- Design implementation is valid but current execution environment cannot render/screenshot the UI.

Expected:

- state `VISUAL_ACCEPTANCE: UNAVAILABLE`;
- do not fabricate screenshot evidence;
- do not automatically block otherwise valid work unless the target project explicitly requires rendered acceptance.

Acceptance markers:

`VISUAL_ACCEPTANCE_UNAVAILABLE_MUST_BE_EXPLICIT: YES`

`FABRICATED_SCREENSHOT_EVIDENCE: NO`

## F. Strong observable receipt

Every governed user-facing response must expose the actual route and actual used Skills.

Required fields:

```text
Governance route:
Skills used:
Task state:
Outcome:
Changes:
Control alignment:
PR / workspace:
Next:
```

`Capability modules` is optional and is used when an invoked Skill materially applies named internal source modules, for example `design → Anthropic frontend-design`.

The pre-return gate must reject omission, theoretical routes, and listing Skills that were merely installed/discovered/mentioned but not actually used.

Acceptance markers:

`GOVERNANCE_ROUTE_REQUIRED_IN_RECEIPT: YES`

`SKILLS_USED_REQUIRED_IN_RECEIPT: YES`

`SKILLS_USED_ACTUAL_ONLY: YES`

`ROUTE_AND_SKILLS_MUST_BE_CONSISTENT: YES`

`LEGACY_RECEIPT_WITHOUT_ROUTE_OR_SKILLS_ALLOWED: NO`

## G. Regression preservation

The corrective release must preserve:

- exactly nine top-level Skills;
- Anthropic source body identity/provenance/license;
- Project Profile pre-return gate;
- Agent Handoff routing/templates/pre-return gates;
- Solution Design architecture/state-ownership authority;
- Microsoft design-review/adaptation remains planned/inactive;
- UX heuristic/audit remains planned/inactive;
- Plugin payload remains `plugin.json + skills/**` only.

Acceptance markers:

`TOP_LEVEL_SKILL_COUNT: 9`

`ANTHROPIC_SOURCE_IDENTITY_PRESERVED: YES`

`MICROSOFT_MODULE_ACTIVE: NO`

`UX_AUDIT_MODULE_ACTIVE: NO`

`PRIOR_RELEASE_GATES_PRESERVED: YES`
