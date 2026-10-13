# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release is now `plugin-v0.5.4`.

- Release title: `Engineering Governance Plugin v0.5.4`
- Frozen publication source: `3e028cdbe21e9637cbf7bf9b00a5664d44c272c0`
- GitHub Actions run: `38346638985` — `success`
- Release asset: `engineering-governance-plugin.zip`
- Asset size: `64200` bytes
- SHA-256: `2a39d1bf705b56b53f2514b5bb8012380606278989afabdc4f3c7424dd0f0367`
- Package file entries: `29`
- Included top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`
- The release ZIP contains only `plugin.json` and `skills/**`; repository controls, docs, marketplace catalogs, and workflows are not packaged.

Historical `plugin-v0.5.3` remains immutable publication evidence and is not moved or replaced.

## Accepted v0.5.4 governance and distribution state

- Accepted governance semantics from PR #18 are merged at `999c649e499f69bffe7bf870f38e953a0abd59af`.
- Portable root `plugin.json` version `0.5.4` was integrated by PR #19 at `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- Repo-backed `engineering-governance-personal` marketplace was integrated by PR #20 at `6185a1be962956422b7e4eeb56727ccb9a9386fa`.
- ChatGPT Web Plugin is `0.5.4` with exactly three top-level Skills.
- Mac mini and MacBook Air are independently verified on one active `engineering-governance@engineering-governance-personal / 0.5.4` authority each.
- The 0.5.4 payload contains `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and the separate repository-host gate boundary.

## Active development state

Task `EG-PLUGIN-V0.5.4-FORMAL-RELEASE-057` is complete.

The formal release operation added the one-shot release workflow and published the already accepted payload; it did not change Plugin semantics, add a fourth Skill, change Web/local authority, or mutate local caches/sources.

## Current v0.5.4 alignment

- Repository portable manifest: `0.5.4`
- Formal GitHub release: `plugin-v0.5.4`
- ChatGPT Web Plugin: `0.5.4`
- Mac mini canonical Codex authority: `0.5.4`
- MacBook Air canonical Codex authority: `0.5.4`

## Next intended milestone

No further v0.5.4 publication or distribution work is required. The next meaningful Engineering-Governance task should start from this accepted baseline.
