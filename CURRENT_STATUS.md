# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release is now `plugin-v0.7.2`.

Publication identity:

- release PR: `#34` — `MERGED`;
- publication source SHA: `229f9edc17a9a9c80dac3ac84f7ed45e097ce098`;
- accepted semantic candidate: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- GitHub Actions run: `38668545801` — `success`;
- tag: `plugin-v0.7.2` -> `229f9edc17a9a9c80dac3ac84f7ed45e097ce098`;
- release ID: `413342779`;
- asset: `engineering-governance-plugin.zip`;
- asset ID: `642334384`;
- asset size: `140844` bytes;
- SHA-256: `eba897ba8a9a9a40127e204cf42f44fa7a282a93692c773d6ebc6a5fda5b876b`;
- package entries: `62`;
- package contains only `plugin.json` and `skills/**`;
- included top-level Skills: exactly `9`.

The release workflow source verification, package build, immutable tag creation and GitHub release creation all passed. The one-shot release workflow was then archived at `fd81a56790b8dbf62c2bb2e64b4c8e9d8f5888f6`.

## v0.7.2 accepted capability state

- Project Governance remains the normal engineering entry;
- Project Profile remains derived compact context, not authority;
- Solution Design owns material engineering architecture/state/API/data-flow ambiguity;
- Design owns bounded UI/UX/frontend interaction and visual design;
- Execution Orchestrator uses an explicit Sub Agent value gate;
- Agent Handoff governs cross-context cards/receipts;
- Evidence Audit owns formal read-only acceptance/readiness verdicts;
- Domain Navigation remains conditional for unclear authority/source/test/runtime routes;
- Incident Doctor remains evidence-gated for blocking unexplained failures;
- routing is selective capability composition, not an all-Skill pipeline.

## Acceptance state

- v0.7.2 source validation: `PASS`;
- Design acceptance: `PASS`;
- Web Plugin 0.7.2 readback: `PASS`;
- Air Local Sub Agent runtime acceptance: `PASS`;
- Air nine-Skill routing acceptance: `PASS_WITH_FOLLOWUPS`;
- no Skill-source corrective remained after integrated routing acceptance.

The only Local follow-up was runtime cache-path observability: the session did not expose which of two same-version cache paths supplied the active Skills. This is non-blocking because both observed distributions identify `0.7.2` and no relevant routing-content divergence was found.

## Distribution model

Source authority:

`Lost0rz/Engineering-Governance`

Intentional distribution projections:

1. persistent Local Git-backed Plugin installation, required because the user switches accounts;
2. account-synced Web/remote Plugin projection.

These projections may coexist. Release/distribution correctness depends on source/version/content equivalence rather than forcing one physical runtime cache path.

## PR / lifecycle state

- stale PR #21: `CLOSED / UNMERGED / SUPERSEDED`;
- release PR #34: `MERGED`;
- open PR count: `0`;
- Task `EG-PLUGIN-V0.7.2-FORMAL-RELEASE-086`: `COMPLETE`;
- release branch `release/plugin-v0.7.2-formal` is merged history only and has no active authority.

## Downstream installation state

- private Web Plugin: `0.7.2`;
- Air Local Plugin/runtime: `0.7.2` accepted;
- Mac mini Local Plugin update to `0.7.2`: not yet observed in this release task and should be verified after the user updates that machine.
