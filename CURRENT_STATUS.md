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

- exact tag/source SHA: `b288161c5a4b869ac9d95588c1501184229b2444`
- asset: `engineering-governance-plugin.zip`
- asset size: `56882` bytes
- asset SHA-256: `66a1b4b4eaf3b87eaf6e1addfe793cad578ceb4c35de3c0d681d02118f3250e0`
- package file entries: `29`
- asset count: exactly `1`
- draft: `false`
- prerelease: `false`
- publisher workflow run: `38018881361`
- published asset was downloaded again by the publisher and its SHA-256 matched the locally built artifact
- one-shot publisher branch self-deleted after verification

## Installed v0.5.0 acceptance — Air

Published v0.5.0 installation/runtime identity acceptance is complete on the Air.

Accepted receipt:

- previous active version: `0.3.0`
- installed/active version: `0.5.0`
- active cache path: `/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- installed payload matches all `29` Release files: `YES`
- active Skills: `project-governance`, `domain-navigation`, `incident-doctor`
- enabled Engineering-Governance registration count: `1`
- competing older active authority: `NO`
- older backup files may remain on disk but are not active registrations
- global managed routing block count: `1`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`
- router update required: `NO_WRITE`
- source repository mutation during install: `NO`
- business-project mutation during install: `NO`

Installation method used the supported Codex CLI registration remove/reinstall path for `engineering-governance@engineering-governance-personal`.

The local Plugin list reported the active registration as installed and enabled at `0.5.0`. A remote catalog request warning was observed during listing, but the local registration identity was returned completely and is not currently classified as an installation blocker.

## Installed v0.5.0 acceptance — Mac mini

Published v0.5.0 installation/runtime identity acceptance is also complete on the Mac mini.

Accepted receipt:

- previous active version: `0.4.0`
- installed/active version: `0.5.0`
- active cache path: `/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- durable local marketplace source: `/Users/ox_miles/.codex/plugin-sources/engineering-governance/0.5.0`
- installed payload matches all `29` Release files: `YES`
- active Skills: `project-governance`, `domain-navigation`, `incident-doctor`
- enabled Engineering-Governance registration count: `1`
- competing older active authority: `NO`
- global managed routing block count: `1`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`
- router update required: `NO_WRITE`
- source repository mutation during install: `NO`
- business-project mutation during install: `NO`

A legacy v0.4.0 directory remains at `/Users/ox_miles/.codex/plugins/engineering-governance`, but it is unregistered and is not an active authority. It is therefore not an installation or behavior-acceptance blocker and does not require cleanup as part of this task.

Before behavior acceptance on either machine, use a fresh session/runtime so the newly installed Plugin files are loaded.

## Accepted v0.5 capabilities awaiting behavior acceptance

- affected-only Navigation refresh with current-route no-churn and explicit stale/historical/read-only boundaries;
- lightweight evidence-backed non-blocking `CURRENT_STATUS.md / Follow-ups`, with `CURRENT_TASK.md` remaining the only repair authorization;
- Project Storage Affinity derived from the canonical project location, with explicit project-local override and separate machine/runtime plus ephemeral-scratch classes;
- Engineering-Governance repository-specific Web/remote construction and local installed/runtime validation split.

Exactly three top-level Skills remain. Global Router remains selection-only. No fourth Skill, Findings platform, storage runtime subsystem, daemon, service, database, installer, or automatic remediation was added.

## Closed tasks

- `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049` — `PASS`
- `EG-PLUGIN-V0.5.0-RELEASE-050` — `PASS`
- v0.5.0 Air installation/runtime identity acceptance — `PASS`
- v0.5.0 Mac mini installation/runtime identity acceptance — `PASS`

## Active task

Task: `EG-PLUGIN-V0.5.0-BEHAVIOR-ACCEPTANCE-051`.

State: `AUTHORIZED_LOCAL_BEHAVIOR_ACCEPTANCE`.

Mode: `DISPOSABLE_PROJECT / EVIDENCE_ONLY / NO_REUSABLE_SOURCE_REPAIR`.

## Next milestone

Run five focused behavior cases in a fresh local session against the published installed v0.5.0 Plugin. Either accepted machine may be used; if results are machine-sensitive, record the machine explicitly rather than assuming cross-machine equivalence.

1. stale/wrong Navigation correction is affected-only;
2. correct/current Navigation route produces no churn;
3. lightweight Follow-up is retained without repair authorization and survives next-task selection until resolved/obsolete/no longer material;
4. strict read-only reports candidates without mutating navigation or controls;
5. Project Storage Affinity routes durable project-controlled state from the canonical project storage authority while keeping machine/runtime state and ephemeral scratch separate.

Use a disposable test project or other explicitly safe fixture. Do not modify Engineering-Governance reusable source during acceptance. Any reusable defect returns to a fresh Web/remote corrective task.