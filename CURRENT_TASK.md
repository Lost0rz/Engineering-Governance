# CURRENT TASK — Engineering Governance Plugin v0.5.4 Distribution

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-PLUGIN-V0.5.4-DISTRIBUTION-056`

State: `AUTHORIZED`

Mode: governed plugin distribution

## Objective

Distribute the accepted control-vs-delivery identity semantics merged by PR #18 to ChatGPT Web and prepare the canonical local Codex upgrade path as plugin version `0.5.4`.

## Baseline

- Current accepted repository main before this control transition: `999c649e499f69bffe7bf870f38e953a0abd59af`.
- PR #18 is merged.
- Accepted source semantics include the Delivery / Semantic HEAD model and the separate live repository-host gate boundary.
- Current published/Web Plugin version before this task: `0.5.3`.

## In scope

- Reconcile the portable `plugin.json` version from `0.5.3` to `0.5.4` without changing plugin name or three-Skill architecture.
- Publish/update the owned private ChatGPT Web Plugin `engineering-governance` to `0.5.4`, preserving plugin identity, scope, discoverability, and unchanged non-project-governance files.
- Include the accepted current `skills/project-governance/**` source in the Web Plugin update.
- Preserve `domain-navigation` and `incident-doctor` unchanged.
- Provide a local Codex upgrade command sequence using the existing canonical marketplace authority `engineering-governance-personal`, with no manual active-cache edits.

## Out of scope

- New governance semantics beyond the already merged PR #18.
- Adding a fourth Skill, daemon, hook, service, database, installer, or remediation runtime.
- Changing plugin audience/scope/discoverability/name.
- Manually editing installed Codex cache directories.

## Verification

- Repository manifest version is exactly `0.5.4` after integration.
- Web Plugin metadata reports version `0.5.4` with the same plugin ID, USER scope, and PRIVATE discoverability.
- Web Plugin contains exactly the existing three top-level Skills.
- Web `project-governance` source contains the accepted semantic-evidence vs repository-host-gate distinction.
- Local instructions use marketplace/plugin-manager mechanisms rather than direct cache mutation.

## Stop conditions

- Repository source differs materially from accepted PR #18 semantics before version integration.
- Web Plugin identity/scope/audience would change.
- Updating locally would require manual edits to the active cache.

## Handoff

After the Web Plugin update and verification, return the exact local Codex upgrade/verification commands for both Mac mini and MacBook Air using `$HOME`-relative paths and the existing `engineering-governance-personal` authority.
