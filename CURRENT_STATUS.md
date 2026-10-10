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
- installed payload matches the 29-file Release payload: `YES`
- enabled Engineering-Governance registrations: `1`
- competing older active authority: `NO`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`

### Mac mini — PASS

- active version: `0.5.0`
- active cache: `/Users/ox_miles/.codex/plugins/cache/engineering-governance-personal/engineering-governance/0.5.0`
- durable local marketplace source: `/Users/ox_miles/.codex/plugin-sources/engineering-governance/0.5.0`
- installed payload matches the 29-file Release payload: `YES`
- enabled Engineering-Governance registrations: `1`
- competing older active authority: `NO`
- Global Router: `CURRENT / SINGLE / SELECTION_ONLY`
- legacy `/Users/ox_miles/.codex/plugins/engineering-governance` v0.4.0 directory remains unregistered and non-authoritative

## v0.5.0 behavior acceptance — COMPLETE

Task: `EG-PLUGIN-V0.5.0-BEHAVIOR-ACCEPTANCE-051`.

Final state: `V0.5_BEHAVIOR_ACCEPTED`.

Mode used: `DISPOSABLE_PROJECT / EVIDENCE_ONLY / NO_REUSABLE_SOURCE_REPAIR`.

### Case 1 — Navigation affected-only — PASS on Mac mini

- stale accepted Orders route `src/legacy/orders-service.txt` was corrected to verified current route `src/orders/service.txt`;
- only the affected Orders navigation fields changed;
- Billing remained unchanged;
- no whole-map rewrite or generalized mapping subsystem was introduced;
- independent mechanical audit and `git diff --check` passed;
- disposable fixture was removed after acceptance.

### Case 2 — Navigation current-route no-churn — PASS on Mac mini

- accepted Orders route was already current and reused;
- `DOMAIN_MAP.md` remained byte-for-byte unchanged by SHA-256;
- Billing remained unchanged;
- only the authorized Orders task mutation occurred;
- no repository-wide mapping scan, regeneration, or unnecessary navigation churn occurred;
- disposable fixture was removed after acceptance.

### Case 3 — Follow-up lifecycle — PASS on Mac mini

- a real, evidence-backed, non-blocking adjacent Orders documentation discrepancy was retained in `CURRENT_STATUS.md / Follow-ups` without expanding or interrupting the active task;
- the adjacent documentation was not repaired under the old task;
- no blocker, Finding ID, backlog subsystem, issue tracker, or new control file was created;
- on later task selection, the retained Follow-up was considered and selected;
- explicit `CURRENT_TASK.md` authorization was created before any repair;
- mere selection did not delete or resolve the Follow-up;
- independent mechanical audits for both retention and later selection passed.

### Case 4 — Strict read-only candidate-only — PASS on Mac mini

Disposable fixture: `/Volumes/Jack-Dev/Acceptance/eg-v050-readonly-case4-H0TSyJ`.

Verified behavior:

- task mode was `STRICT_READ_ONLY`;
- stale navigation claim `src/legacy/orders-service.txt` produced only a correction candidate to `src/orders/service.txt`;
- adjacent endpoint discrepancy (`docs/orders-operations.md` `/orders/v0` versus authoritative Orders implementation `/orders/v1`) produced only a Follow-up candidate;
- `DOMAIN_MAP.md` was not modified;
- `CURRENT_STATUS.md` was not modified;
- `CURRENT_TASK.md` was not modified;
- source/product/docs were not modified;
- no Findings/backlog subsystem was created;
- `git status --short` remained empty;
- before/after SHA-256 for all tracked fixture files matched exactly;
- final mechanical audit reported `ALL_TRACKED_HASHES_UNCHANGED=PASS`, `GIT_WORKTREE_UNCHANGED=PASS`, and `CASE4_FINAL_AUDIT=PASS`.

### Case 5 — Project Storage Affinity — PASS on Mac mini

- canonical project storage authority was established before durable placement decisions;
- default durable project-controlled evidence followed canonical storage;
- explicit project-local override correctly overrode the default;
- ephemeral scratch used system temp and was removed;
- machine/runtime state remained machine-local;
- no universal host/path rule, storage manifest, daemon, service, or generalized storage subsystem was introduced;
- earlier MemoX attempts remain classified as `NOT_EXECUTED / INVALID_FIXTURE`, not Plugin failures;
- disposable fixture and override were removed after acceptance.

## Accepted behavior summary

- affected-only Navigation correction: `PASS — Mac mini`
- current-route Navigation no-churn: `PASS — Mac mini`
- lightweight Follow-up retention and later explicit task selection: `PASS — Mac mini`
- strict read-only candidate-only behavior: `PASS — Mac mini`
- Project Storage Affinity: `PASS — Mac mini`

No behavior case revealed a reusable Plugin source/contract defect. No real business project was mutated during acceptance. Engineering-Governance reusable source and installed Plugin cache were not repaired by hand.

## Closed tasks

- `EG-V0.5-STORAGE-INTEGRATION-CLEAN-BASELINE-049` — `PASS`
- `EG-PLUGIN-V0.5.0-RELEASE-050` — `PASS`
- v0.5.0 Air installation/runtime identity acceptance — `PASS`
- v0.5.0 Mac mini installation/runtime identity acceptance — `PASS`
- `EG-PLUGIN-V0.5.0-BEHAVIOR-ACCEPTANCE-051` — `PASS / V0.5_BEHAVIOR_ACCEPTED`

## Next milestone

v0.5.0 release, installation, and focused behavior acceptance are complete.

Normal business-project adoption/usage may proceed under each target project's own accepted development workflow. The Engineering-Governance Web-construction/local-validation split remains repository-specific and must not be generalized to other projects.
