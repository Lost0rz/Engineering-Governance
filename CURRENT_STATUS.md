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

## v0.5.0 behavior acceptance progress

### Case 5 — Project Storage Affinity — PASS on Mac mini

Validated in disposable fixture:

`/Volumes/Jack-Dev/Acceptance/eg-v050-storage-2FjLZd`

Receipt evidence:

- machine: `Mac mini`
- active Plugin: `engineering-governance v0.5.0`
- preflight `pwd`, Git root, and saved fixture path all matched the disposable fixture
- canonical storage authority: `/dev/disk5s1` mounted at `/Volumes/Jack-Dev`
- default retained durable artifact: `/Volumes/Jack-Dev/Acceptance/eg-v050-storage-2FjLZd/acceptance-results/storage-affinity/default-durable-evidence.txt`
- default artifact storage: `/dev/disk5s1` / `/Volumes/Jack-Dev`
- explicit project-local acceptance-export override from `AGENTS.md`: `/Users/ox_miles/Documents/EG-Acceptance-Override/eg-v050-storage-2FjLZd`
- override artifact: `/Users/ox_miles/Documents/EG-Acceptance-Override/eg-v050-storage-2FjLZd/EG-V050-STORAGE-AFFINITY-DISPOSABLE-001-acceptance-export.txt`
- override artifact storage: `/dev/disk3s5` mounted at `/System/Volumes/Data`
- ephemeral scratch: `/private/tmp/eg-v050-storage-affinity-disposable-001-scratch.txt`, created and removed before closure
- machine/runtime state mutated: `NO`
- real business project mutated: `NO`
- Engineering-Governance reusable source/plugin cache hand-edited: `NO`
- no storage manifest, daemon, service, generalized storage subsystem, or host-wide storage rule was introduced
- local fixture result mutation remained uncommitted for inspection

The two earlier MemoX attempts are classified as `NOT_EXECUTED / INVALID_FIXTURE`, not Plugin failures. They correctly stopped before mutating the real MemoX repository.

The disposable Case 5 fixture and explicit override were removed only after PASS had been recorded.

### Case 1 — Navigation affected-only correction — PASS on Mac mini

Validated in disposable fixture:

`/Volumes/Jack-Dev/Acceptance/eg-v050-nav-case1-pg5OKI`

Receipt and independent audit evidence:

- machine: `Mac mini`
- active Plugin: `engineering-governance v0.5.0`
- Skills used: `project-governance`, `domain-navigation`
- accepted stale Orders route: `src/legacy/orders-service.txt`
- verified current Orders route: `src/orders/service.txt`
- `DOMAIN_MAP.md` modified: `YES`
- affected Orders fields changed: `Authority`, `Evidence`, `Freshness`
- unrelated Billing entry changed: `NO`
- actual task mutation: exactly one `case1-task-note` line appended to `src/orders/service.txt`
- whole-map rewrite: `NO`
- generalized mapping subsystem created: `NO`
- pre-cleanup Git status contained only `DOMAIN_MAP.md` and `src/orders/service.txt`
- independent mechanical audit proved Orders entry changed, Billing entry remained unchanged, and the task mutation existed exactly once
- `git diff --check`: `PASS`
- real business project mutated: `NO`
- Engineering-Governance reusable source/plugin cache mutated: `NO`
- disposable fixture removed only after final audit PASS

## Accepted v0.5 capabilities still awaiting behavior acceptance

- current-route Navigation no-churn;
- lightweight evidence-backed non-blocking `CURRENT_STATUS.md / Follow-ups`, with `CURRENT_TASK.md` remaining the only repair authorization;
- strict read-only candidate-only behavior.

Project Storage Affinity and affected-only Navigation correction are now behavior-accepted on the Mac mini.

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

Behavior progress:

- Case 1 Navigation affected-only: `PASS — Mac mini`
- Case 2 Navigation no-churn: `PENDING`
- Case 3 Follow-up lifecycle: `PENDING`
- Case 4 Strict read-only: `PENDING`
- Case 5 Storage Affinity: `PASS — Mac mini`

## Next milestone

Continue focused behavior acceptance on Mac mini with a fresh disposable fixture. Next target: Case 2, correct/current Navigation route produces no churn.

Do not modify Engineering-Governance reusable source during acceptance. Any reusable defect returns to a fresh Web/remote corrective task.
