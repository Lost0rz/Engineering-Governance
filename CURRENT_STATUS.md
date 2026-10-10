# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-10.

## Authoritative release baseline

Published Plugin release: `plugin-v0.5.0`.

Accepted release source:

`b288161c5a4b869ac9d95588c1501184229b2444`

Published asset:

- `engineering-governance-plugin.zip`
- size: `56882` bytes
- SHA-256: `66a1b4b4eaf3b87eaf6e1addfe793cad578ceb4c35de3c0d681d02118f3250e0`
- package entries: `29`
- exactly three top-level Skills: `project-governance`, `domain-navigation`, `incident-doctor`

Global Router remains single and selection-only. No fourth Skill, Findings platform, storage runtime subsystem, daemon, service, database, installer, or automatic remediation exists in the accepted v0.5.0 payload.

## Installation acceptance

### Air — PASS

- active version: `0.5.0`
- active cache: `/Users/jack7788/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- installed payload matches all 29 Release files: `YES`
- enabled Engineering-Governance registrations: `1`
- competing older active authority: `NO`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`

### Mac mini — PASS

- active version: `0.5.0`
- active cache: `/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- durable local marketplace source: `/Users/ox_miles/.codex/plugin-sources/engineering-governance/0.5.0`
- installed payload matches all 29 Release files: `YES`
- enabled Engineering-Governance registrations: `1`
- competing older active authority: `NO`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`
- legacy `/Users/ox_miles/.codex/plugins/engineering-governance` v0.4.0 directory is unregistered and non-authoritative

## v0.5.0 behavior acceptance progress

Active acceptance task: `EG-PLUGIN-V0.5.0-BEHAVIOR-ACCEPTANCE-051`.

Mode: `DISPOSABLE_PROJECT / EVIDENCE_ONLY / NO_REUSABLE_SOURCE_REPAIR`.

### Case 1 — Navigation affected-only — PASS on Mac mini

Disposable fixture: `/Volumes/Jack-Dev/Acceptance/eg-v050-nav-case1-pg5OKI`.

Verified behavior:

- stale accepted Orders route `src/legacy/orders-service.txt` was replaced by current verified route `src/orders/service.txt`;
- only Orders `Authority`, `Evidence`, and `Freshness` changed in `DOMAIN_MAP.md`;
- Billing entry remained unchanged;
- exactly one `case1-task-note` was added to the actual Orders authority;
- no whole-map rewrite or new mapping subsystem occurred;
- independent mechanical audit and `git diff --check` passed;
- disposable fixture was removed only after audit PASS.

### Case 2 — Navigation current-route no-churn — PASS on Mac mini

Disposable fixture: `/Volumes/Jack-Dev/Acceptance/eg-v050-nav-case2-peMVKs`.

Verified behavior:

- accepted Orders route was already current: `src/orders/service.txt`;
- only `project-governance` was needed; Domain Navigation was not unnecessarily expanded;
- `DOMAIN_MAP.md` was not modified;
- pre/post `DOMAIN_MAP.md` SHA-256 matched exactly;
- navigation diff was empty;
- Billing remained unchanged;
- exactly one `case2-task-note` was added to `src/orders/service.txt`;
- no whole-map rewrite, repository-wide mapping scan, or new mapping subsystem occurred;
- independent mechanical audit and `git diff --check` passed;
- disposable fixture was removed only after audit PASS.

### Case 5 — Project Storage Affinity — PASS on Mac mini

Disposable fixture: `/Volumes/Jack-Dev/Acceptance/eg-v050-storage-2FjLZd`.

Verified behavior:

- canonical storage authority: `/dev/disk5s1` mounted at `/Volumes/Jack-Dev`;
- default retained durable artifact remained on `/Volumes/Jack-Dev`;
- explicit project-local acceptance-export override correctly placed retained output on `/System/Volumes/Data`;
- ephemeral scratch was created under `/private/tmp` and removed before closure;
- machine/runtime state was not modified;
- no storage manifest, daemon, service, generalized storage subsystem, or host-wide storage rule was introduced;
- the two earlier MemoX attempts are `NOT_EXECUTED / INVALID_FIXTURE`, not Plugin failures;
- disposable fixture and override were removed only after PASS was recorded.

## Remaining behavior acceptance

- Case 3 Follow-up lifecycle: `PENDING`
- Case 4 Strict read-only candidate-only: `PENDING`

Current accepted behavior:

- affected-only Navigation correction: `PASS — Mac mini`
- current-route Navigation no-churn: `PASS — Mac mini`
- Project Storage Affinity: `PASS — Mac mini`

## Closed tasks

- `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049` — `PASS`
- `EG-PLUGIN-V0.5.0-RELEASE-050` — `PASS`
- v0.5.0 Air installation/runtime identity acceptance — `PASS`
- v0.5.0 Mac mini installation/runtime identity acceptance — `PASS`

## Next milestone

Continue focused behavior acceptance on Mac mini with a fresh disposable fixture.

Next target: Case 3, lightweight evidence-backed non-blocking Follow-up retention and later task selection.

Do not modify Engineering-Governance reusable source during acceptance. Any reusable defect returns to a fresh Web/remote corrective task.
