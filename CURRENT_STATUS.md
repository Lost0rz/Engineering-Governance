# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.6.6` pending the active corrective release.

Release provenance:

- PR #26: `MERGED`;
- merge/release source SHA: `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`;
- release workflow: `Release Plugin v0.6.6`;
- workflow run: `38549662373` — `success`;
- tag: `plugin-v0.6.6` -> `7866e13cb6a82d59eb9c27ee4e536062ab357b1b`;
- GitHub Release ID: `412590103`;
- asset: `engineering-governance-plugin.zip`;
- asset SHA-256: `433831130c2f85358ba75c4f07ef5063318a8ef00b255a8fa5966b2e7f16b93b`;
- package version: `0.6.6`;
- top-level Skills: exactly `8`.

## Accepted Web / local distribution baseline

The private personal ChatGPT Web Plugin and MacBook Air Local Codex installation both reached version `0.6.6` before the current corrective:

- Web Plugin: `plugins_6acb0b9e8b748191a9b89fad47d89517`, release `pluginrel_6acf45f2c8208191937f142f6c7198a8`, USER / PRIVATE;
- Local Plugin: `engineering-governance@engineering-governance-personal`, version `0.6.6`, exact eight-Skill identity;
- local source: `https://github.com/Lost0rz/Engineering-Governance.git`, ref `main`.

These distribution/install facts remain valid historical evidence for v0.6.6. Full integrated routing acceptance is no longer claimable for v0.6.6 because a reusable Handoff Card generation defect has now been reproduced on the Web surface.

## Reproduced reusable defect

A real cross-context execution card generated from the installed Web Plugin did not satisfy the shipped Agent Handoff contract even though the schema existed in source.

Observed failure class:

- generic/legacy execution-card shape returned instead of the standardized Handoff Card;
- `MODE: CORRECTIVE` rather than the accepted mode set;
- required Handoff core fields omitted;
- task/plan content re-copied into the card rather than using authority references + fresh delta;
- observed commit identity treated as an execution lock without owning task authority;
- return contract biased toward a predetermined successful final state.

The current source/release validation verifies that Handoff field names exist, but does not enforce a mandatory generation pre-return gate or a negative acceptance case for this failure class.

## Current task

Task: `EG-HANDOFF-CARD-GENERATION-CORRECTIVE-079`

State: `AUTHORIZED_IN_PROGRESS`

Current branch:

`codex/handoff-card-generation-corrective-079`

Objective:

- strengthen Project Governance -> Agent Handoff routing for cross-context Card/instruction generation;
- add mandatory Card/Receipt pre-return compliance;
- add regression/negative acceptance for the reproduced legacy-card failure;
- strengthen release validation;
- publish the next patch Plugin release;
- synchronize the existing private ChatGPT Web Plugin;
- leave Local Codex cache untouched so local updates consume the supported published source.

## Control identity

Current `main` at corrective authorization start:

`0d4a4c784e695fc165d9f7283d71dda903d72024`

The active corrective branch was created from that exact main revision. Task 078 is superseded as the active authorization because it explicitly required a separately authorized source corrective when a reusable defect appeared.
