# CURRENT TASK — Design Skill Anthropic Baseline Integration

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-DESIGN-ANTHROPIC-BASELINE-080`

Task class: `CAPABILITY_EXPANSION`

State: `ACTIVE`

## Objective

Add a routed top-level `design` capability to Engineering Governance and bundle Anthropic's `frontend-design` Skill as the first complete design-source module, so UI/frontend design work can be selected through the existing Governance routing layer instead of requiring a separate external Plugin.

## Scope

- add `skills/design/SKILL.md` as the stable routed design capability;
- preserve the current upstream Anthropic `frontend-design` Skill content and Apache-2.0 license inside the Design module with source provenance;
- route bounded UI/UX/frontend visual-design requests from `project-governance` / global routing to `design`;
- keep `solution-design` authority for engineering architecture/state-ownership ambiguity;
- update capability composition, README/maintainer-facing capability inventory, package manifest/version, release validation, and acceptance evidence as required;
- prepare the structure so future Microsoft design-review and UX-audit source modules can be incorporated without changing the external route.

## Non-goals

- do not yet merge Microsoft design-review rules or frontend-design-audit heuristics into active Design behavior;
- do not introduce Figma, browser automation, runtime services, or a separate design Plugin dependency;
- do not replace project-specific design authority, component libraries, tokens, content facts, or product requirements.

## Source baseline

Anthropic upstream source:

- repository: `anthropics/skills`;
- path: `skills/frontend-design`;
- upstream `SKILL.md` blob: `a5333457c414d20d625f307df945842c0952ecc3`;
- upstream `LICENSE.txt` blob: `f433b1a53f5b830a205fd2df78e2b34974656c7b`;
- license: Apache License 2.0.

## Verification / acceptance

At minimum verify:

- exact nine top-level Skill set including `design`;
- `design` is selected for bounded frontend/UI visual design and redesign work;
- ordinary engineering remains routed through `project-governance`;
- material architecture/state-ownership ambiguity remains `solution-design`;
- Anthropic source content and license/provenance are packaged and readable;
- Design module does not claim Microsoft/Audit integration before those modules exist;
- Plugin package remains `plugin.json` + `skills/**` only.

## Stop boundaries

Stop rather than inventing behavior if routing creates competing task authority, Design duplicates Solution Design's architecture ownership, upstream licensing/provenance cannot be preserved, or release/package validation cannot distinguish the new ninth Skill.

Control Alignment:

- `PREDECESSOR_TASK`: `EG-HANDOFF-CARD-GENERATION-CORRECTIVE-079`
- `START_MAIN`: `0c4c404e9b173b3f2e125bfa138bd68e76bf42f2`
- `WORK_BRANCH`: `codex/design-anthropic-baseline`
- `CONTROL_ALIGNMENT`: `ACTIVE`
