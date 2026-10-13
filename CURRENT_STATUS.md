# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-13.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.3` at source `255bd32b1414a9555a7280d6e7562411ed3c7d96`.

That immutable release remains historical publication evidence; no formal `plugin-v0.5.4` GitHub tag/release is claimed by this status.

## Accepted governance source

PR #18 is merged. Its accepted semantics separate literal Repository HEAD from Delivery / Semantic HEAD for `CURRENT_STATUS.md` / `CURRENT_TASK.md`-only drift and keep repository-host merge gates as separate live literal constraints.

PR #18 squash merge commit:

`999c649e499f69bffe7bf870f38e953a0abd59af`

## Repository distribution state

Portable root `plugin.json` is version `0.5.4`.

- PR #19 integrated the portable manifest version at `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- PR #20 added the repo-backed personal marketplace catalog and is merged at `6185a1be962956422b7e4eeb56727ccb9a9386fa`.
- Canonical marketplace entry: `engineering-governance-personal`.
- Plugin source is Git-backed from `Lost0rz/Engineering-Governance@main`, avoiding per-machine fixed-version local sources for future upgrades.

## ChatGPT Web Plugin state

Owned private ChatGPT Plugin `engineering-governance` is version `0.5.4`.

- Plugin ID: `plugins_6acb0b9e8b748191a9b89fad47d89517`
- Current release ID: `pluginrel_6acda259f9ec8191b09ba5cff8742633`
- Scope: `USER`
- Discoverability: `PRIVATE`
- Exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`.
- Web `project-governance` contains the accepted `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and separate repository-host gate semantics.

## Local Codex installation state

Both canonical local Codex hosts have been independently verified on `engineering-governance-personal / engineering-governance / 0.5.4` with exactly one active Engineering Governance authority per host.

### Mac mini

- Machine class: `MAC_MINI`
- Codex CLI: `0.162.1`
- Active authority count: `1`
- Active authority: `engineering-governance@engineering-governance-personal / 0.5.4`
- Exactly three top-level Skills verified.
- `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and repository-host gate boundary checks: PASS.
- `created-by-me-remote / 0.5.4` may exist as a non-active cache copy; it is not an active authority.

### MacBook Air

- Machine class: `MACBOOK_AIR`
- Codex CLI: `0.160.0`
- Active authority count: `1`
- Active authority: `engineering-governance@engineering-governance-personal / 0.5.4`
- Exactly three top-level Skills verified.
- `CONTROL_ONLY_DRIFT`, Delivery / Semantic HEAD, and repository-host gate boundary checks: PASS.
- `created-by-me-remote / 0.5.4` may exist as a non-active cache copy; it is not an active authority.

Neither local convergence used manual active-cache mutation or business-project repository mutation.

## Active development state

Task `EG-PLUGIN-V0.5.4-DISTRIBUTION-056` is complete.

Accepted distribution state is aligned across:

- repository portable manifest: `0.5.4`;
- ChatGPT Web Plugin: `0.5.4`;
- Mac mini canonical Codex authority: `0.5.4`;
- MacBook Air canonical Codex authority: `0.5.4`.

No fourth Skill or new governance runtime/machinery was introduced.

## Next intended milestone

No further action is required for v0.5.4 distribution. The next meaningful Engineering-Governance task should reconcile from this accepted state in one task transition rather than creating a standalone evidence-only closeout cycle.
