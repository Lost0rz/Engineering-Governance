# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.x release has been created yet.

## v0.6.x source architecture / current semantic candidate

The eight-Skill architecture remains accepted. Current corrected Delivery / Semantic candidate:

`ca64841b141888675c2670eeaf4c6cbccb8a5395`

Completed bounded correctives:

- `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` — shipped Handoff templates aligned with Card/Receipt contract.
- `EG-V060-PROFILE-COMPACTNESS-CORRECTIVE-072` — Project Profile contract/template/acceptance hardened against generic-workflow duplication and handbook-sized output.

Task 072 focused source audit: PASS.

After the Web Plugin refresh automatically advanced the installed candidate to `0.6.1`, repository `plugin.json` was aligned from `0.6.0` to `0.6.1`. This version-alignment commit changes package identity only; no Skill behavior changed after the Task 072 semantic corrective.

PR #26 remains OPEN / DRAFT / UNMERGED. Host facts are reread at their own boundary; CI/check PASS is not claimed without current evidence.

## Web Plugin candidate acceptance

Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is `WAITING_FRESH_WEB_SESSION`.

Current candidate installation evidence:

- personal Plugin identity preserved: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web Plugin current version: `0.6.1`;
- current Web release: `pluginrel_6acf006fb68c81918d269b6ee46719e6`;
- scope/discoverability remain `USER / PRIVATE`;
- root `plugin.json` and platform-managed `.codex-plugin/plugin.json` both report `0.6.1`;
- the refresh overlaid only the manifest plus the three corrected `project-profile` shipped files;
- installed `project-profile` Skill, template and contract contain the compression gate, anti-content/dedup rules, template-first output discipline, and explicit Profile surface/role rule.

Evidence already established in a previous fresh Web conversation:

- exact eight top-level Skill discovery: PASS;
- ordinary status/progress inspection -> `project-governance`: PASS;
- advisory inspection does not over-route to formal Audit/Navigation/Doctor: PASS;
- Project Profile request -> Project Profile capability: PASS for routing/authority/freshness boundary;
- first generated Profile excluded live PR/HEAD/CI/current-task state but duplicated reusable governance procedure: FAIL, corrected by Task 072 source.

The previous fresh conversation may still hold the pre-refresh 0.6.0 Skill snapshot. The corrected Profile regression must therefore be rerun in a new fresh Web conversation/session against candidate `0.6.1`.

## Project Profile corrected contract

- Profile is a compact `DERIVED_PROJECT_CONTEXT` landing index, not a second governance manual.
- Stable project-specific context, priorities/anti-goals, environment roles and authority pointers remain in Profile.
- Current state/task/host evidence stays in STATUS/TASK/live evidence.
- Project-specific normative MUST/MUST-NOT remains in AGENTS/accepted normative authority.
- Detailed Domain/design content stays in its owning authority.
- Reusable routing tables, Handoff schemas, verification tiers/procedure, Incident Doctor procedure, artifact/workspace/control mechanics are removed or reduced to the shortest useful pointer/invariant.
- Generated output starts from the shipped template, declares known Profile surface/role, and does not add top-level procedure sections merely because a reusable Skill exists.

## Next milestone

Open a new fresh Web conversation against Plugin `0.6.1` and rerun the same Engineering-Governance Project Profile generation case. If compactness/dedup regression passes, continue the remaining Web routing scenarios; then continue Local Codex integrated acceptance. Formal GitHub release/merge remains deferred.
