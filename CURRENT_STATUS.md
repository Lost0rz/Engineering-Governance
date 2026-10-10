# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Clean authoritative source baseline

The repository has exactly one remote development branch: `main`.

The accepted clean source used for Plugin v0.5.0 publication is:

`b288161c5a4b869ac9d95588c1501184229b2444`

At that revision:

- Plugin version is `0.5.0`;
- exactly three top-level Skills exist: `project-governance`, `domain-navigation`, `incident-doctor`;
- Navigation Refresh, lightweight Follow-ups, Project Storage Affinity, and the Engineering-Governance-only execution split are integrated and source-audited;
- open PR count was `0`;
- remote development branch set was exactly `main`;
- historical RemoteOrbit adoption-gap evidence is preserved under archive tag `archive/remoteorbit-adoption-gap-audit-032`.

## Published Plugin v0.5.0

GitHub Release:

`plugin-v0.5.0`

Release verification:

- Release title: `Engineering Governance Plugin v0.5.0`
- exact tag/source SHA: `b288161c5a4b869ac9d95588c1501184229b2444`
- asset: `engineering-governance-plugin.zip`
- asset size: `56882` bytes
- asset SHA-256: `66a1b4b4eaf3b87eaf6e1addfe793cad578ceb4c35de3c0d681d02118f3250e0`
- package file entries: `29`
- asset count: exactly `1`
- draft: `false`
- prerelease: `false`
- publisher: GitHub Actions
- publisher workflow run: `38018881361`
- published asset was downloaded again by the publisher and its SHA-256 matched the locally built artifact
- one-shot publisher branch self-deleted after verification

The tag itself was independently re-read after publication and points exactly to the accepted clean source SHA above.

## Accepted v0.5 capabilities

- affected-only Navigation refresh with current-route no-churn and explicit stale/historical/read-only boundaries;
- lightweight evidence-backed non-blocking `CURRENT_STATUS.md / Follow-ups`, with `CURRENT_TASK.md` remaining the only repair authorization;
- Project Storage Affinity derived from the canonical project location, with explicit project-local override and separate machine/runtime plus ephemeral-scratch classes;
- Engineering-Governance repository-specific Web/remote construction and local installed/runtime validation split.

Exactly three top-level Skills remain. Global Router remains selection-only. No fourth Skill, Findings platform, storage runtime subsystem, daemon, service, database, installer, or automatic remediation was added.

## Closed tasks

- `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049` — `PASS`
- `EG-PLUGIN-V0.5.0-RELEASE-050` — `PASS`

Current release state:

`EG_PLUGIN_V0.5.0_RELEASED_VERIFIED`

## Next milestone

Local reinstall and real runtime/behavior acceptance of the published v0.5.0 package.

Local validation should first prove the active installed/runtime Plugin identity is the published v0.5.0 artifact and that no older competing Engineering-Governance authority remains. Then run the focused Navigation/Follow-up/Storage-Affinity behavior checks. Local AI must return evidence rather than repair reusable source; any reusable defect returns to a fresh Web/remote Engineering-Governance corrective task.
