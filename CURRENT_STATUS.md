# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-15.

## Published / distributed baseline

Formal GitHub tagged release remains `plugin-v0.7.1` until Task 086 publication completes.

Current source/distribution state:

- root Plugin manifest: `0.7.2`;
- exactly nine top-level Skills;
- PR #33 merged the v0.7.2 source;
- semantic candidate: `23b05c7f8847dd1868f05dd3fe5257aed94f635a`;
- latest source validation run: `38663053412` — `success`;
- private Web Plugin: `0.7.2`, release ID `pluginrel_6ad02855852c8191a7addd05d6026361`;
- Air Local Sub Agent runtime acceptance: `PASS`;
- Air nine-Skill integrated routing acceptance: `PASS_WITH_FOLLOWUPS` with no Skill-source corrective required.

## Active release task

Task `EG-PLUGIN-V0.7.2-FORMAL-RELEASE-086` is:

`ACTIVE — FORMAL_RELEASE`

Objective: publish the already accepted 0.7.2 payload as immutable GitHub tag/release without changing Skill semantics.

## Acceptance evidence

### Local execution / Sub Agent

`LOCAL_RUNTIME_ACCEPTANCE`: `PASS`.

Observed Air fixture for Task 084:

- final fixture HEAD: `0e0b6512af2b67b6cc689ba650597bf308d53b8d`;
- inline negative control: `PASS`;
- parallel read-only `EXPLORER ×2`: `PASS`;
- shared-writer safety with one `WORKER`: `PASS`;
- configured/effective runtime identity remained correctly separated.

### Nine-Skill routing

User-returned Air fixture for Task 085:

- final fixture HEAD: `1e4008896a06566f25720da4e0eb69166c96a0c0`;
- Project Governance default route: `PASS`;
- Solution Design positive/negative: `PASS`;
- Evidence Audit positive/negative: `PASS` / required `UNKNOWN` correctly yields `STOP`;
- Agent Handoff generation: `PASS`;
- Domain Navigation positive/negative: `PASS`;
- Incident Doctor positive/negative: `PASS`;
- Project Profile smoke: `PASS`;
- selective composition: `SELECTIVE_CAPABILITY_ROUTING`;
- unnecessary Skill invocations: none;
- missed required Skill invocations: none;
- route-return failures: none.

`NINE_SKILL_ROUTING_ACCEPTANCE`: `PASS_WITH_FOLLOWUPS`.

Only follow-up: the runtime did not expose which of two same-version local cache paths supplied the active Skills. Both distributions identify `0.7.2`; no relevant routing-content divergence was found. The dual distribution is intentional because the user requires a persistent Local installation independent of account-synced Plugin availability.

## PR / lifecycle state

- PR #33: `MERGED`;
- stale Draft PR #21: `CLOSED / UNMERGED / SUPERSEDED`;
- no further Skill corrective is currently required before formal release.

## Release state

`FORMAL_GITHUB_RELEASE_072`: `IN_PROGRESS`.

Task 086 may add only the bounded one-shot release workflow and publication/control evidence required for formal release. Skill semantics remain frozen at the accepted 0.7.2 source.

## Authority / distribution model

Source authority:

`Lost0rz/Engineering-Governance`

Intentional distribution projections:

1. Local Git-backed Plugin installation — persistent across account switching;
2. account-synced Web/remote Plugin projection.

Runtime cache-path selection is not semantic authority. Release correctness depends on version/content equivalence to repository source, not on forcing a single physical cache path.
