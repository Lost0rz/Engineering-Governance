# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Clean authoritative source baseline

The repository has exactly one remote development branch: `main`.

The accepted clean baseline produced by the integration/cleanup task is:

`b288161c5a4b869ac9d95588c1501184229b2444`

At that revision:

- Plugin version is `0.5.0`;
- exactly three top-level Skills exist: `project-governance`, `domain-navigation`, `incident-doctor`;
- integrated Navigation Refresh, lightweight Follow-ups, Project Storage Affinity, and Engineering-Governance-only execution split are accepted;
- open PR count was `0`;
- remote development branch set was exactly `main`;
- historical RemoteOrbit adoption-gap evidence is preserved under archive tag `archive/remoteorbit-adoption-gap-audit-032` rather than a development branch.

## Published Plugin status

Latest published Release is still `plugin-v0.4.0`.

Fresh release preflight for `plugin-v0.5.0`:

- Release exists before publication: `NO`
- tag exists before publication: `NO`

## Active task

Task: `EG-PLUGIN-V0.5.0-RELEASE-050`.

State: `AUTHORIZED_REMOTE_PUBLICATION`.

Mode: `EXACT_CLEAN_BASELINE_RELEASE`.

Exact release source:

`b288161c5a4b869ac9d95588c1501184229b2444`

Publication must package only that revision's `plugin.json + skills/**`, publish tag `plugin-v0.5.0` against that exact source, upload one `engineering-governance-plugin.zip` asset, verify artifact identity/hash, and leave no publisher branch behind.

## Local validation boundary

No local Plugin reinstall/runtime behavior validation begins until this release is published and independently verified. Local validation must use the published v0.5.0 artifact/runtime identity rather than an old A2 or pre-integration candidate.

## Next milestone

Publish and verify Plugin v0.5.0 from the exact clean baseline, then hand the published artifact to local installation/runtime acceptance.
