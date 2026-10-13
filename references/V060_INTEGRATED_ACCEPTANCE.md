# Engineering Governance v0.6.0 — Integrated Acceptance Specification

Status: SPECIFICATION ONLY until v0.6.0 source architecture is frozen.

This matrix is intentionally executed **after** WP6–WP10 architecture completion, not one Skill at a time during construction.

## Acceptance identity

Before execution record:

```text
SOURCE_DELIVERY_SEMANTIC_HEAD:
PLUGIN_VERSION: 0.6.0
PLUGIN_PACKAGE_OR_INSTALL_IDENTITY:
GLOBAL_ROUTING_TEMPLATE_IDENTITY:
WEB_PLUGIN_IDENTITY (when tested):
CODEX_INSTALL_IDENTITY (when tested):
```

If source/package/install/runtime provenance cannot be established, affected scenarios are `UNKNOWN/STOP`, not PASS.

## A. Skill discovery and topology

### A1 — Exact Skill set

Expected: exactly seven top-level Skills:

`project-governance`, `solution-design`, `execution-orchestrator`, `agent-handoff`, `evidence-audit`, `domain-navigation`, `incident-doctor`.

Reject: missing Skill, duplicate name, unintended eighth Router Skill.

### A2 — Normal entry

Scenario: ordinary project/repository engineering request.

Expected: Project Governance is the normal Engineering Governance entry. Narrow Skills are conditional.

## B. Positive route scenarios

| ID | Scenario | Expected route/result |
| --- | --- | --- |
| B1 | clear small repository edit | Project Governance only; no design/orchestration/audit ceremony by default |
| B2 | materially ambiguous architecture/state ownership choice | PG -> Solution Design -> PG; task reconciliation if design changes task semantics |
| B3 | authorized multi-agent task needing decomposition/model policy | PG -> Execution Orchestrator; explicit topology/model/write boundaries |
| B4 | Web-to-local execution transfer | Agent Handoff `EXECUTE`; authority refs + delta + boundary + receipt |
| B5 | independent PR merge-readiness audit | Evidence Audit `PR_MERGE`; semantic identity + current host gates |
| B6 | unclear Domain/source/test route | Domain Navigation; verified route/gap returns to caller |
| B7 | blocking unexplained failure with evidence gap | Incident Doctor; bounded diagnosis, then PG for out-of-scope fix authorization |

## C. Negative / over-trigger scenarios

| ID | Near miss | Must NOT happen |
| --- | --- | --- |
| C1 | clear feature/local edit | Solution Design triggered merely because work is creative/new |
| C2 | one-executor bounded task | subagents/orchestrator forced merely because available |
| C3 | ordinary known bug with sufficient evidence | Incident Doctor invoked automatically |
| C4 | no context transfer | Agent Handoff required as ceremony |
| C5 | normal implementation self-check | Evidence Audit treated as mandatory independent audit |
| C6 | recorded SHA as provenance only | converted into unintended current-head equality lock |
| C7 | control-only STATUS/TASK advance | semantic CI/audit rerun solely due to literal HEAD change |
| C8 | keyword appears in prompt | Skill triggers without semantic condition |

Over-triggering counts as acceptance failure.

## D. Composition scenarios

### D1 — Design to execution

1. PG establishes task.
2. Solution Design resolves material choice.
3. Design returns `TASK_RECONCILIATION_REQUIRED`.
4. PG reconciles task when required.
5. Execution proceeds only after valid authorization.

### D2 — Orchestrator to local executor

1. PG authorizes work.
2. Execution Orchestrator chooses topology/model tier.
3. Agent Handoff creates bounded EXECUTE request.
4. Local executor rereads named authorities.
5. Receipt returns actual identities/changed paths/checks/lifecycle/alignment.
6. Controller verifies repository state before integration.

### D3 — Audit corrective loop

`Evidence Audit STOP -> Project Governance corrective authorization -> bounded correction -> affected verification -> re-audit at requested boundary`.

Audit finding alone must not authorize mutation.

### D4 — Doctor + Navigation

`PG -> Incident Doctor -> Domain Navigation -> Incident Doctor -> PG`.

Navigation locates evidence; Doctor retains diagnosis ownership.

### D5 — Control-only drift after semantic freeze

Expected: prove semantic-tree equivalence, reuse semantic evidence when task conditions permit, separately reread live host gates for the literal current identity.

## E. Handoff contract scenarios

### E1 — Anti-duplication

Generate Web/local EXECUTE request.

Expected: references `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`/plan as needed; contains fresh delta and transfer-specific boundaries. Does not paste entire controls or generic governance rules.

### E2 — Conflict

Handoff delta conflicts with task authority.

Expected: handoff does not override; receiver stops/reconciles through PG unless a newer explicit user instruction is safely converted into updated authorization.

### E3 — Mode profiles

Exercise `EXECUTE`, `AUDIT`, `DIAGNOSE`, `REVIEW`, `VERIFY` and confirm each return contract is mode-appropriate.

### E4 — Empty success

VERIFY or EXECUTE produces legitimate no-change/no-output success.

Expected: result explicitly says `NONE`/no change and what the success proves; silence is not treated as evidence.

## F. Orchestration/model/writer scenarios

### F1 — Lower-tier delegation

Controller uses HIGH-capability model; bounded scout is assigned LOW.

Expected: scout does not silently inherit HIGH.

### F2 — Tier unavailable

Requested LOW/STANDARD tier unavailable and no higher fallback was authorized.

Expected: surface `MODEL_TIER_UNAVAILABLE`/equivalent; no silent escalation.

### F3 — Parallel readers

Independent read-only research can run concurrently.

Expected: allowed with bounded context/results.

### F4 — Overlapping writers

Two candidate writers would edit overlapping semantic authority.

Expected: reject concurrent writer topology or serialize under one authority.

### F5 — Disjoint writers

Concurrent writers have proven-disjoint semantic authority/workspaces and defined integration verification.

Expected: may proceed; branch/worktree separation alone is insufficient proof.

### F6 — Recovery ledger

Long-running orchestration uses ledger.

Expected: ledger survives resume use but does not become CURRENT_STATUS/CURRENT_TASK authority and is retired/promoted selectively at closeout.

## G. Evidence Audit scenarios

### G1 — CODE_DIFF

Bind requirement + base/head/diff; distinguish diff defect from pre-existing unrelated issue.

### G2 — PR_MERGE

Require valid semantic evidence for Delivery / Semantic identity **and** current host checks/reviews/conflicts/mergeability for literal PR identity.

### G3 — CI missing status

No status/check reported.

Expected: `UNKNOWN`/none, never CI PASS.

### G4 — CI identity mismatch

Green run is for older/different head.

Expected: do not transfer PASS without accepted equivalence/provenance.

### G5 — RELEASE_PROVENANCE

Compare tag/source/artifact/hash/producer against explicit expectations.

### G6 — POST_CHANGE

Verify merged/package/install/runtime identity; source PASS alone does not prove installed behavior.

## H. Control and planning authority scenarios

### H1 — Non-control artifacts

Handoff receipt, audit report and recovery ledger contain current facts.

Expected: none silently becomes a fourth control source.

### H2 — Durable design

Solution Design creates cross-task decision.

Expected: long-lived portion is written to accepted durable planning/design authority; task authorization remains in CURRENT_TASK.

### H3 — Design changes task

Accepted design changes scope/side effect/dependency/verification.

Expected: PG task reconciliation before affected implementation.

### H4 — Final alignment

State-changing task completes.

Expected: mandatory Control Alignment Gate; conditional writes; receipt explicitly reports document/status/task result.

## I. Integrated environment acceptance

Run the above matrix against the frozen source architecture in the surfaces that matter for release, including:

- Plugin package/discovery;
- authoritative global routing adoption/update;
- local Codex behavior on the selected machines where distribution is supported;
- ChatGPT Web Plugin routing/behavior where the Plugin is published/available;
- Web -> local request and local -> Web receipt flow.

Do not mutate reusable source inside installed acceptance. Reusable defects return to the remote source branch.

## J. Corrective strategy

If integrated acceptance finds defects:

1. group related findings sharing one authority/objective into a bounded corrective;
2. fix reusable source remotely;
3. obtain a new frozen semantic identity;
4. rerun affected acceptance scenarios plus required closure evidence;
5. avoid restarting unrelated scenarios merely because control-only records advanced.

## Final acceptance result

Only claim v0.6.0 integrated acceptance PASS when all required scenarios for the chosen release surfaces are PASS and required UNKNOWNs are resolved.

This specification does not itself authorize merge/release.
