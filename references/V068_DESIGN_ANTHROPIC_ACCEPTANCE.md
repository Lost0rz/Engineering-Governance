# v0.6.8 Design / Anthropic Baseline Acceptance

Task: `EG-DESIGN-ANTHROPIC-BASELINE-080`

## Capability inventory

- TOP_LEVEL_SKILL_COUNT: `9`
- DESIGN_SKILL_PRESENT: `YES`
- DESIGN_EXTERNAL_ROUTE: `design`
- SEPARATE_ANTHROPIC_PLUGIN_REQUIRED: `NO`

## Source import

- UPSTREAM_REPOSITORY: `anthropics/skills`
- UPSTREAM_PATH: `skills/frontend-design`
- UPSTREAM_SKILL_BLOB: `a5333457c414d20d625f307df945842c0952ecc3`
- UPSTREAM_LICENSE_BLOB: `f433b1a53f5b830a205fd2df78e2b34974656c7b`
- LOCAL_FRONTEND_DESIGN_CONTENT_SHA_MATCH: `YES`
- APACHE_2_LICENSE_INCLUDED: `YES`
- PROVENANCE_INCLUDED: `YES`

## Routing cases

### Case A — frontend visual redesign

Request: redesign a storefront page because typography, visual hierarchy, section repetition, image/text balance, and composition are weak.

Expected route:

- Project Governance remains task/lifecycle owner when implementation is governed;
- bounded visual-design decision routes to `design`;
- Design reads the bundled Anthropic baseline.

Result: `PASS`.

### Case B — architecture ambiguity containing the word design

Request: design the persistence/state ownership and API boundary for a new authoring workflow.

Expected route:

- `solution-design`, not `design`.

Result: `PASS`.

### Case C — ordinary corrective implementation

Request: fix an already-understood frontend bug with no material visual-design ambiguity.

Expected route:

- remain in `project-governance` unless another narrow trigger applies;
- do not add Design ceremony merely because frontend code is involved.

Result: `PASS`.

### Case D — future module claims

Expected:

- Microsoft review/adaptation is marked planned, not active;
- UX heuristic/audit module is marked planned, not active;
- no Figma/browser/runtime dependency is claimed.

Result: `PASS`.

## Composition boundary

- PROJECT_GOVERNANCE_TASK_AUTHORITY_PRESERVED: `YES`
- SOLUTION_DESIGN_ARCHITECTURE_AUTHORITY_PRESERVED: `YES`
- DESIGN_BOUNDED_UI_VISUAL_AUTHORITY: `YES`
- ROUTER_SKILL_CREATED: `NO`
- PARALLEL_TASK_AUTHORITY_CREATED: `NO`

## Regression preservation

The v0.6.8 release verification carries forward the previously accepted Project Profile and Handoff gates from v0.6.7 in addition to the new Design checks.

- PROJECT_PROFILE_PRE_RETURN_GATE_PRESERVED: `YES`
- HANDOFF_PRE_RETURN_GATE_PRESERVED: `YES`
- HANDOFF_REQUEST_RECEIPT_SCHEMA_GATES_PRESERVED: `YES`
- V067_HANDOFF_REGRESSION_MARKERS_PRESERVED: `YES`
- PRIOR_RELEASE_GATES_PRESERVED: `YES`

## Package boundary

The Plugin payload remains limited to `plugin.json` plus `skills/**`. The Anthropic source module, license, provenance, and Design module map therefore travel with the Plugin release without packaging repository control files.

Acceptance state for source contract: `PASS`.

Installed/runtime behavior remains a separate claim until the released Plugin is read back in the target host.
