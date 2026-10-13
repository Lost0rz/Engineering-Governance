# CURRENT TASK — Plugin v0.5.3 Release

Task ID: `EG-PLUGIN-V0.5.3-RELEASE-053`

Date: 2026-10-13

Repository: `Lost0rz/Engineering-Governance`

State: `ACTIVE_RELEASE`

## Objective

Publish a new Engineering Governance Plugin release that includes the accepted `EG-FINAL-PR-HEAD-FREEZE-052` corrective, align the GitHub release line and the private ChatGPT Plugin on version `0.5.3`, and leave verified update instructions for local Codex installations.

## Start baseline

- repository: `Lost0rz/Engineering-Governance`
- canonical branch: `main`
- verified start HEAD: `19a90c68d4a602ff38450f34822e3a01d9fedc71`
- published GitHub Plugin release: `plugin-v0.5.0`
- private ChatGPT Plugin observed version: `0.5.2`
- accepted reusable source corrective is already present on `main`

The start HEAD is the verified transition baseline for this release task; it is not a permanent equality lock after authorized release commits.

## In scope

- bump the repository Plugin manifest to `0.5.3`;
- package only the Plugin payload (`plugin.json` plus `skills/**`);
- verify the payload contains exactly the three supported top-level Skills;
- publish GitHub tag/release `plugin-v0.5.3` with the packaged asset;
- update the owned private ChatGPT Plugin to `0.5.3` while preserving its existing audience and identity;
- reconcile repository controls after publication;
- provide verified local Codex upgrade steps for Air and Mac mini.

## Out of scope

- changing the accepted Final PR-head freeze semantics;
- adding a fourth Skill, runtime, daemon, installer, service, database, or automatic remediation;
- directly editing installed Codex caches as a substitute for an upgrade;
- changing target-project governance files merely because the Plugin version changes.

## Known evidence

`main` already contains the freeze rule in:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/references/control-plane.md`

The private ChatGPT Plugin is currently `0.5.2` and contains the same accepted freeze-rule source, while the repository release line remains `0.5.0`. The release version is therefore set to `0.5.3` to converge both channels without version regression.

## Risk and rationale

Release/package identity change with no new behavioral semantics beyond already accepted reusable source. Primary risks are publishing the wrong source identity, packaging extra/missing files, version divergence between channels, or mutating the frozen release identity after verification.

## Verification level, cadence, and rationale

`V1` release/package verification.

Before publication:

- verify manifest version `0.5.3`;
- verify the three expected Skills and freeze-rule source are present;
- verify package scope and entry count;
- bind release evidence to the exact publication commit.

At the final release boundary, freeze the publication commit. Release/tag/check results are external evidence for that immutable identity and must not cause an evidence-only commit loop.

## Acceptance criteria

- repository manifest version is `0.5.3`;
- GitHub tag/release `plugin-v0.5.3` exists and resolves to the exact frozen publication commit;
- release asset is `engineering-governance-plugin.zip` containing only `plugin.json` and `skills/**`;
- exactly three top-level Skills remain: `project-governance`, `domain-navigation`, `incident-doctor`;
- private ChatGPT Plugin reports version `0.5.3` and retains the accepted freeze-rule files;
- no source/control commit is created solely to record transient CI/release evidence for the frozen publication identity;
- repository status is reconciled after publication only for durable release/current-task state.

## Stop conditions

- live `main` differs from the verified task transition in an unauthorized way before release preparation;
- the accepted freeze-rule source is missing or materially different between release source and the private ChatGPT Plugin;
- packaging requires adding an unauthorized runtime or installer mechanism;
- release publication cannot be bound to one exact immutable source commit;
- unknown conflicting Plugin identity or audience would be overwritten.

## Handoff / current stop point

Authorized to prepare and publish `plugin-v0.5.3`, align the private ChatGPT Plugin to `0.5.3`, then return verified Codex upgrade instructions. Local machine installation remains a separate user-executed step unless explicitly handed to a local executor.
