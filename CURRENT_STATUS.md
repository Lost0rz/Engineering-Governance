# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.6.7`.

Release provenance:

- PR #27: `MERGED`;
- merge/release source SHA: `53590bcec50c057d6c0fdd25b0e834133a808a93`;
- release workflow run: `38552557416` — `success`;
- tag: `plugin-v0.6.7`;
- package version: `0.6.7`;
- package scope: `plugin.json` + `skills/**` only;
- released top-level Skills: exactly `8`.

The existing private personal Web Plugin is still on the verified `0.6.7` release. Local installed/runtime `0.6.7` acceptance remains observational and must not be inferred from source state.

## Active source work

Task: `EG-DESIGN-ANTHROPIC-BASELINE-080`

State: `ACTIVE`

Branch: `codex/design-anthropic-baseline`

Start main: `0c4c404e9b173b3f2e125bfa138bd68e76bf42f2`

Authorized change:

- expand the source capability model from eight to nine top-level Skills by adding stable routed `design`;
- bundle Anthropic `frontend-design` as the first complete internal Design source module with Apache-2.0 license/provenance preserved;
- route bounded UI/UX/frontend visual-design work through `design` while leaving task/lifecycle authority in `project-governance` and material engineering architecture/state-ownership ambiguity in `solution-design`;
- prepare, but do not yet activate, future Microsoft design-review and UX-audit source modules.

## Distribution boundary

No new Plugin version is published yet for task 080. `0.6.7` remains the only released/verified distribution identity until the design source candidate is accepted, merged, and separately released.

No Local cache/source mutation is authorized as part of source construction.

## Control identity

Published Delivery / Semantic Plugin identity remains:

`53590bcec50c057d6c0fdd25b0e834133a808a93`

Active source construction identity begins from repository main:

`0c4c404e9b173b3f2e125bfa138bd68e76bf42f2`

Control-only commits and source-construction commits must not be represented as a published Plugin release before release evidence exists.
