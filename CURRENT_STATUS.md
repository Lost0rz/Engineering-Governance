# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published baseline

Formal GitHub Plugin release remains `plugin-v0.7.2` until Task 088 publication completes.

Published v0.7.2 identity:

- release PR: `#34` — `MERGED`;
- publication source SHA: `229f9edc17a9a9c80dac3ac84f7ed45e097ce098`;
- GitHub Actions run: `38668545801` — `success`;
- tag: `plugin-v0.7.2` -> `229f9edc17a9a9c80dac3ac84f7ed45e097ce098`;
- release ID: `413342779`;
- asset SHA-256: `eba897ba8a9a9a40127e204cf42f44fa7a282a93692c773d6ebc6a5fda5b876b`;
- included top-level Skills: exactly `9`.

The v0.7.2 release remains immutable historical evidence.

## v0.7.3 source state

Task `EG-REMOTE-DELIVERY-CLOSEOUT-087` source delivery is complete:

- PR `#35 — feat: require verified remote repository delivery at closeout` — `MERGED`;
- validated semantic/source head: `7a5c256b4bdf09768645d252df340870f8d8ef82`;
- `Validate Plugin v0.7.3 Candidate` run `38677775327` — `success`;
- merge commit: `998a8cae62546ed8a2551c1fb54aded037c62985`;
- root `plugin.json`: `0.7.3`;
- exactly nine top-level Skills retained.

The v0.7.3 correction makes local commit creation and remote repository delivery separate evidence claims. When an applicable configured remote exists and the task is not explicitly local-only, full repository delivery requires push of the already-authorized task/project ref plus fresh remote-ref verification. No remote and explicit local-only work are reported distinctly; push failure preserves local work and does not become false remote completion.

## Runtime-acceptance decision

The user explicitly waived an additional disposable Local runtime acceptance round for v0.7.3 and authorized direct formal release and Web Plugin synchronization.

Therefore:

- v0.7.3 source validation: `PASS`;
- v0.7.3 additional Local runtime acceptance: `WAIVED_BY_USER`;
- no runtime PASS claim is inferred from the waiver.

## Active release lifecycle

Task `EG-PLUGIN-V0.7.3-FORMAL-RELEASE-088` is:

`ACTIVE — RELEASE_AUTHORIZED`

Pending lifecycle:

1. formal GitHub `plugin-v0.7.3` tag/release/asset publication;
2. release provenance readback;
3. private Web Plugin in-place synchronization to `0.7.3` and readback;
4. Local Git-backed update by the user on Air/Mac mini;
5. final control reconciliation.

## Distribution model

Source authority:

`Lost0rz/Engineering-Governance`

Intentional distribution projections:

1. persistent Local Git-backed Plugin installation;
2. account-synced Web/remote Plugin projection.

The two projections may coexist. Correctness depends on repository-source/version/content equivalence, not one physical cache path.

## Repository lifecycle

- stale PR #21: `CLOSED / UNMERGED / SUPERSEDED`;
- v0.7.2 release PR #34: `MERGED`;
- v0.7.3 source PR #35: `MERGED`;
- Task 086: `COMPLETE`;
- Task 087: source complete; runtime round waived by user;
- Task 088: `ACTIVE — RELEASE_AUTHORIZED`.

## Downstream installation state

- private Web Plugin: currently `0.7.2`, update pending;
- Air Local accepted baseline: `0.7.2`;
- Mac mini Local installed version: not yet re-verified in this lifecycle;
- Local installations will be updated by the user after formal v0.7.3 publication.
