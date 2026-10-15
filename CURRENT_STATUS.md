# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.7.2`.

Publication identity:

- release PR: `#34` — `MERGED`;
- publication source SHA: `229f9edc17a9a9c80dac3ac84f7ed45e097ce098`;
- accepted semantic candidate: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- GitHub Actions run: `38668545801` — `success`;
- tag: `plugin-v0.7.2` -> `229f9edc17a9a9c80dac3ac84f7ed45e097ce098`;
- release ID: `413342779`;
- asset: `engineering-governance-plugin.zip`;
- asset SHA-256: `eba897ba8a9a9a40127e204cf42f44fa7a282a93692c773d6ebc6a5fda5b876b`;
- package entries: `62`;
- included top-level Skills: exactly `9`.

The published v0.7.2 release is immutable historical evidence and is not modified by current work.

## Active development

Task `EG-REMOTE-DELIVERY-CLOSEOUT-087` is `ACTIVE`.

Target source version: `0.7.3` candidate.

Observed gap:

- current governance can distinguish local branch/commit state from remote branch identity;
- however, successful state-changing closeout does not currently require a configured repository remote to contain the final delivered commit;
- a local commit can therefore be returned as apparent completion while remote/Web audit cannot see the produced engineering work.

Required correction:

- local commit creation and remote repository delivery become separate evidence claims;
- when an applicable configured remote exists and work is not explicitly local-only, successful repository delivery requires push of the authorized branch/ref plus remote-ref verification;
- no remote -> `NOT_APPLICABLE_NO_REMOTE`;
- explicit local-only authority -> `NOT_REQUIRED_LOCAL_ONLY`;
- push/network/auth failure -> preserve local work and report remote delivery incomplete rather than full completion;
- never infer that `main` or force-push is authorized.

## Accepted v0.7.2 capability state retained

- Design acceptance: `PASS`;
- Web Plugin 0.7.2 readback: `PASS`;
- Air Local Sub Agent runtime acceptance: `PASS`;
- Air nine-Skill routing acceptance: `PASS_WITH_FOLLOWUPS` with no Skill-source corrective;
- Local Git-backed and account-synced Plugin projections may intentionally coexist when version/content equivalent.

## Repository lifecycle

- stale PR #21: `CLOSED / UNMERGED / SUPERSEDED`;
- release PR #34: `MERGED`;
- open PR count before Task 087 source branch: `0`;
- Task 086: `COMPLETE`;
- Task 087: `ACTIVE`.

## Downstream installation state

- private Web Plugin: `0.7.2`;
- Air Local Plugin/runtime: `0.7.2` accepted;
- Mac mini Local Plugin update to `0.7.2`: not yet observed;
- no v0.7.3 distribution or release is authorized until Task 087 source acceptance is complete.
