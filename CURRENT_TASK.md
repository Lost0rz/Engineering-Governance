# CURRENT TASK — Engineering Governance Plugin v0.7.2 Formal Release

Date: 2026-10-15

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.7.2-FORMAL-RELEASE-086`

Task class: `RELEASE`

State: `ACTIVE — FORMAL_RELEASE`

## Objective

Publish the already accepted Engineering Governance Plugin `0.7.2` payload as a formal GitHub release with immutable tag `plugin-v0.7.2` and release asset `engineering-governance-plugin.zip`, then reconcile repository controls and release provenance.

This task does not authorize new Skill semantics.

## Accepted release basis

- root `plugin.json`: `0.7.2`;
- exactly nine top-level Skills;
- PR `#33 — feat: harden local execution and Sub Agent orchestration` — merged;
- semantic candidate: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- source validation run `38663053412` — `success`;
- private Web Plugin: `0.7.2`, release ID `pluginrel_6ad02855852c8191a7addd05d6026361`;
- Air Local Sub Agent runtime acceptance: `PASS`;
- Air nine-Skill integrated routing acceptance: `PASS_WITH_FOLLOWUPS`, with no Skill-source corrective required;
- dual local/account-synced Plugin distributions are intentional projections of the same repository source; both observed at `0.7.2` and no routing-content divergence was found;
- stale Draft PR `#21` has been closed unmerged as `SUPERSEDED`.

## Release boundary

Allowed:

- add the one-shot `release-plugin-v0.7.2.yml` publication workflow;
- create/merge the bounded release PR;
- publish immutable tag `plugin-v0.7.2`;
- publish GitHub release `Engineering Governance Plugin v0.7.2`;
- publish `engineering-governance-plugin.zip` containing only `plugin.json` and `skills/**`;
- record package size, entry count, SHA-256, source/publication SHA and release URL;
- reconcile `CURRENT_STATUS.md` / `CURRENT_TASK.md` after publication;
- audit remaining open PR state and close obsolete release workspace/branch state when safe.

Not allowed:

- modify Skill semantics or routing behavior;
- change Web Plugin contents/version;
- mutate Local Codex installations;
- delete either intentional local/account-synced distribution projection;
- move or replace an existing release tag.

## Required release checks

Before publication the workflow must verify:

- manifest name `engineering-governance`;
- manifest version `0.7.2`;
- exactly these nine Skill directories: `project-governance`, `project-profile`, `solution-design`, `design`, `execution-orchestrator`, `agent-handoff`, `evidence-audit`, `domain-navigation`, `incident-doctor`;
- every Skill contains `SKILL.md`;
- v0.7.2 Sub Agent value-gate/runtime-evidence contracts are present;
- Project Governance receipt exposes execution topology/Sub Agent evidence;
- Handoff EXECUTE receipt contract preserves execution topology/Sub Agent runtime evidence;
- package boundary contains only `plugin.json` and `skills/**`.

## Acceptance

Formal release is complete only when fresh GitHub evidence establishes:

- tag `plugin-v0.7.2` exists and is immutable publication identity;
- GitHub release exists and is non-draft/non-prerelease;
- release asset exists;
- package SHA-256, size and entry count are recorded;
- release source/publication SHA is recorded;
- open obsolete PR #21 remains closed/unmerged;
- final controls reflect the release result;
- formal release does not claim different Skill semantics from the already accepted 0.7.2 source/runtime evidence.

## Control Alignment

- `PREDECESSOR_TASK`: `EG-LOCAL-EXECUTION-SUBAGENT-HARDENING-084` (`COMPLETE`)
- `TARGET_VERSION`: `0.7.2`
- `SOURCE_VALIDATION`: `PASS`
- `LOCAL_RUNTIME_ACCEPTANCE`: `PASS`
- `NINE_SKILL_ROUTING_ACCEPTANCE`: `PASS_WITH_FOLLOWUPS`
- `WEB_PLUGIN_UPDATE`: `PASS`
- `STALE_PR_21`: `CLOSED / UNMERGED / SUPERSEDED`
- `FORMAL_GITHUB_RELEASE_072`: `IN_PROGRESS`
- `TASK_STATE`: `ACTIVE — FORMAL_RELEASE`
