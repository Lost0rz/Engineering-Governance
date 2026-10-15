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

Task `EG-REMOTE-DELIVERY-CLOSEOUT-087` is:

`SOURCE_MERGED — RUNTIME_ACCEPTANCE_PENDING`

Target source version: `0.7.3` candidate.

Source result:

- PR `#35 — feat: require verified remote repository delivery at closeout` — `MERGED`;
- validated semantic/source head: `7a5c256b4bdf09768645d252df340870f8d8ef82`;
- `Validate Plugin v0.7.3 Candidate` run `38677775327` — `success`;
- merge commit: `998a8cae62546ed8a2551c1fb54aded037c62985`;
- root `plugin.json` is now `0.7.3` candidate on `main`;
- obsolete v0.7.2 candidate validator was archived after the formal v0.7.2 release.

## v0.7.3 remote-delivery behavior

Project Governance now treats local commit creation and remote repository delivery as separate evidence claims.

For state-changing work that produced or advanced commits:

- applicable configured remote + not explicitly local-only -> push only the already-authorized task/project ref and verify the fresh remote ref before claiming full repository delivery;
- local commit / clean working tree / local branch SHA alone does not establish remote delivery;
- no applicable remote -> `REMOTE_DELIVERY: NOT_APPLICABLE_NO_REMOTE`;
- explicit local-only authority -> `REMOTE_DELIVERY: NOT_REQUIRED_LOCAL_ONLY`;
- applicable remote but push/verification failure -> preserve local work and report `PENDING` / `FAILED`, not remotely delivered completion;
- normal closeout does not authorize remote creation, force-push, credential bypass, branch substitution, or an implicit push to `main`.

Project Governance and EXECUTE Handoff receipts can now expose:

```text
LOCAL_COMMIT
REMOTE_DELIVERY
REMOTE_REF
REMOTE_COMMIT
```

## Acceptance state

Accepted prior baseline retained:

- Design acceptance: `PASS`;
- Web Plugin 0.7.2 readback: `PASS`;
- Air Local Sub Agent runtime acceptance: `PASS`;
- Air nine-Skill routing acceptance: `PASS_WITH_FOLLOWUPS` with no Skill-source corrective.

Task 087:

- v0.7.3 source validation: `PASS`;
- source merge: `PASS`;
- Local runtime acceptance of remote/no-remote/local-only/push-failure cases: `PENDING`;
- Web Plugin 0.7.3 sync: `NOT_PERFORMED`;
- formal GitHub `plugin-v0.7.3` release: `NOT_PERFORMED`.

## Distribution model

Source authority:

`Lost0rz/Engineering-Governance`

Intentional distribution projections:

1. persistent Local Git-backed Plugin installation;
2. account-synced Web/remote Plugin projection.

The currently published/distributed accepted baseline remains 0.7.2 until Task 087 runtime acceptance and a later distribution decision.

## Repository lifecycle

- stale PR #21: `CLOSED / UNMERGED / SUPERSEDED`;
- release PR #34: `MERGED`;
- Task 087 PR #35: `MERGED`;
- Task 086: `COMPLETE`;
- Task 087: `SOURCE_MERGED — RUNTIME_ACCEPTANCE_PENDING`.

## Downstream installation state

- private Web Plugin: `0.7.2`;
- Air Local Plugin/runtime accepted baseline: `0.7.2`;
- Mac mini Local Plugin update to `0.7.2`: not yet observed;
- v0.7.3 runtime/distribution acceptance is pending and must not be conflated with the existing formal 0.7.2 release.
