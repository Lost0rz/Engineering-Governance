# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-12.

## Published release baseline

Published Plugin release remains `plugin-v0.5.0`.

Accepted release source:

`b288161c5a4b869ac9d95588c1501184229b2444`

Published asset:

- `engineering-governance-plugin.zip`
- size: `56882` bytes
- SHA-256: `66a1b4b4eaf3b87eaf6e1addfe793cad578ceb4c35de3c0d681d02118f3250e0`
- package entries: `29`
- exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

Air and Mac mini installation/runtime identity acceptance for v0.5.0 remain accepted. Global Router remains single and selection-only.

## Reusable source state

`main` now contains the accepted source corrective `EG-FINAL-PR-HEAD-FREEZE-052`.

The corrective adds a durable Project Governance rule for final exact-head merge gates:

- finish intended source/control edits before designating the final PR head;
- freeze that PR head for exact-head CI / review / independent audit;
- treat CI, review, audit, mergeability, and repository-host checks as live external evidence for the frozen identity;
- do not create source/control commits solely to record those external results;
- if evidence requires a real correction, unfreeze and restart exact-head verification on the corrected head;
- when evidence passes, merge the same frozen head;
- post-merge CI is external evidence for the merge identity and must not trigger another evidence-only commit.

Reusable source paths updated:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/references/control-plane.md`

This closes the observed self-triggering failure mode:

`exact-head CI PASS → controls-only evidence commit → new HEAD → another exact-head CI`.

## Release boundary

The corrected reusable source is **ahead of the published Plugin release**.

`plugin-v0.5.0` does not yet claim this source corrective. A future release task must package, publish, and install a new Plugin version before installed-plugin identity can claim the rule as part of the released payload.

Do not hand-edit installed Plugin caches to bypass that release boundary.

## Current repository state

- Open pull requests: **none**.
- Active authorized task: **none**.
- Active blockers for repository source work: **none**.
- Next release milestone: publish/install a new Plugin version containing the final PR-head freeze corrective when explicitly authorized.

## Accepted v0.5.0 behavior summary

The existing v0.5.0 acceptance remains valid for its released payload:

- affected-only Navigation correction: `PASS — Mac mini`
- current-route Navigation no-churn: `PASS — Mac mini`
- lightweight Follow-up retention and later explicit task selection: `PASS — Mac mini`
- strict read-only candidate-only behavior: `PASS — Mac mini`
- Project Storage Affinity: `PASS — Mac mini`

No fourth Skill, Findings platform, storage runtime subsystem, daemon, service, database, installer, or automatic remediation was introduced by the source corrective.
