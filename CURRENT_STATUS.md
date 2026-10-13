# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.3` at source `255bd32b1414a9555a7280d6e7562411ed3c7d96` until Task 057 completes.

## Accepted v0.5.4 distribution state

- Accepted governance semantics from PR #18 are merged at `999c649e499f69bffe7bf870f38e953a0abd59af`.
- Portable root `plugin.json` version `0.5.4` was integrated by PR #19 at `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- Repo-backed `engineering-governance-personal` marketplace was integrated by PR #20 at `6185a1be962956422b7e4eeb56727ccb9a9386fa`.
- ChatGPT Web Plugin is `0.5.4` with exactly three top-level Skills.
- Mac mini and MacBook Air are independently verified on one active `engineering-governance@engineering-governance-personal / 0.5.4` authority each.
- The 0.5.4 payload contains `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and the separate repository-host gate boundary.

## Active development state

Active authorized task: `EG-PLUGIN-V0.5.4-FORMAL-RELEASE-057`.

Current phase: formal GitHub release publication authorized.

The task may add only the one-shot release workflow needed to verify and publish the already accepted 0.5.4 payload. It does not authorize new Skill semantics, a fourth Skill, Plugin manifest version change, marketplace behavior change, or local cache/source mutation.

## Release target

- Tag: `plugin-v0.5.4`
- Release title: `Engineering Governance Plugin v0.5.4`
- Asset: `engineering-governance-plugin.zip`
- Package contents: `plugin.json` plus `skills/**` files only
- Expected top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`
- Expected package file entries: `29`

## Next intended milestone

Publish `plugin-v0.5.4` through the repository one-shot release workflow, verify the GitHub Actions run, immutable tag identity, release asset size/digest/entry count, and then reconcile Task 057 complete.
