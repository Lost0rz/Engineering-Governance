# CURRENT TASK — Engineering Governance Plugin v0.5.4 Distribution

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.5.4-DISTRIBUTION-056`

State: `WEB_UPDATED_LOCAL_CODEX_PENDING`

Mode: governed plugin distribution

## Objective

Distribute the accepted control-vs-delivery identity semantics merged by PR #18 to ChatGPT Web and converge the canonical local Codex installations to plugin version `0.5.4`.

## Baseline

- Accepted PR #18 source semantics are merged at `999c649e499f69bffe7bf870f38e953a0abd59af`.
- Repository portable manifest version `0.5.4` is integrated at `9a4025c69fdfc42ba8f35df28f638f89dbe96c51`.
- Formal historical GitHub Plugin release remains `plugin-v0.5.3`; this task does not claim a formal `plugin-v0.5.4` tag/release exists.

## Completed

- Repository manifest bumped to `0.5.4` through PR #19 with no Skill semantic change in that PR.
- Owned private ChatGPT Web Plugin `engineering-governance` updated to `0.5.4`.
- Web Plugin identity preserved: plugin ID `plugins_6acb0b9e8b748191a9b89fad47d89517`, scope `USER`, discoverability `PRIVATE`.
- Web Plugin release ID is `pluginrel_6acda259f9ec8191b09ba5cff8742633`.
- Exactly three top-level Skills remain.
- Web `project-governance` verified to contain the accepted Delivery / Semantic HEAD, `CONTROL_ONLY_DRIFT`, and separate repository-host gate semantics.

## Remaining in scope

- Refresh/update the existing canonical local marketplace authority `engineering-governance-personal` on Mac mini and MacBook Air.
- Verify installed canonical Plugin version `0.5.4` without manual active-cache mutation.
- Verify the three Skills: `project-governance`, `domain-navigation`, `incident-doctor`.
- Confirm no competing active Engineering Governance authority on each host.

## Out of scope

- New governance semantics beyond PR #18.
- Fourth Skill, daemon, hook, service, database, installer, or remediation runtime.
- Changing Web Plugin audience/scope/discoverability/name.
- Manually editing installed Codex cache directories.
- Deleting historical/non-active local copies merely for cosmetic cleanup.

## Verification

For each local host, verify marketplace refresh/update succeeds, canonical installed version is `0.5.4`, the three expected Skills are present, and the new `project-governance` source contains the repository-host gate boundary.

## Stop conditions

- The marketplace does not expose `0.5.4` after refresh.
- The update would require manual edits to active cache/source directories.
- More than one active Engineering Governance authority is discovered.
- The installed payload lacks one of the three expected Skills or does not contain the accepted host-gate semantics.

## Handoff / current stop point

Web distribution is complete. Run the provided local Codex marketplace/update verification sequence independently on Mac mini and MacBook Air. Return the local receipts if either machine does not converge cleanly to `engineering-governance-personal / 0.5.4`.
