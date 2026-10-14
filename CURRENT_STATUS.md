# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.6.8`.

Release provenance:

- PR #28: `MERGED`;
- merge/release source SHA: `7ac2d6262dd280df2b940fa75e9316db8a3615e7`;
- release workflow: `Release Plugin v0.6.8`;
- workflow run: `38572736330` — `success`;
- tag: `plugin-v0.6.8`;
- GitHub Release ID: `412755933`;
- asset SHA-256: `79f19bfec117d6f6c914f72f1504949f7158bbddf888c223ed41b1bf92ccba39`;
- package scope: `plugin.json` + `skills/**` only;
- top-level Skills: exactly `9`.

The ninth Skill is `design`. Anthropic `frontend-design` is the only active internal design-source module; Microsoft design-review/adaptation and UX heuristic/audit modules remain planned and inactive.

## Verified v0.6.8 runtime observation

A real Merloom Product Detail redesign trial confirmed that local routing can load:

- `project-governance`;
- `design`;
- bundled Anthropic `frontend-design`;
- `domain-navigation`.

The route therefore reaches Design, but the observed output exposed two follow-on gaps:

1. Design can be read without a sufficiently explicit bounded design deliverable/closed-loop process before implementation, allowing the result to collapse into ordinary UI correction.
2. The user-facing engineering receipt can omit the actual `Skills used` even though Project Governance already defines that field, reducing routing observability.

These are capability-contract/acceptance issues, not evidence that Design routing itself failed.

## Current corrective task

Task `EG-DESIGN-ANTHROPIC-CLOSED-LOOP-081` is `ACTIVE` on branch:

`codex/design-anthropic-loop-receipt-enforcement`

Objective:

- make the active Anthropic Design baseline execute a bounded design pass before implementation;
- require rendered visual critique/correction when supported by the environment;
- prevent shotgun routing to unrelated Skills;
- strengthen pre-return enforcement for `Governance route` + actual `Skills used`.

Microsoft and UX-audit integration remain explicitly out of scope for this task.

## Distribution state

Published/Web baseline remains `0.6.8` until Task 081 source changes pass acceptance, merge and formal release.

The user has locally installed `0.6.8` on Air at:

`/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.6.8`

Do not claim the Task 081 corrective behavior is locally or Web-installed before a follow-on release/update is completed and read back.

## Control identity

Task 081 start main:

`e0ddabbf265225b42365234880a8b650efb16632`

Current semantic released Plugin identity remains:

`7ac2d6262dd280df2b940fa75e9316db8a3615e7`
