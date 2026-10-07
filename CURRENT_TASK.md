# CURRENT TASK — Phase F InvestDesk Read-Only Skill Validation

Task ID: `EG-INVESTDESK-PILOT-READONLY-019`

State: `ACTIVE_READ_ONLY_VALIDATION`

Mode: `BOUNDED_INTEGRATION_VALIDATION`

## Objective

Validate the accepted `project-governance`, `domain-navigation`, and `incident-doctor` Skills against InvestDesk's live MVP-D Decision ↔ Transaction Traceability planning gate without mutating InvestDesk. Determine whether the governance and navigation model remains lightweight in normal business/product work and whether Incident Doctor correctly stays dormant when no evidence-deficient failure blocks progress.

## Authority and baselines

- Engineering-Governance accepted reusable Skill revision: `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Engineering-Governance control baseline before Phase F authorization: `e355fccb646e24adca5999b1d7a312f4d8a7b7ab`.
- Target repository: `Lost0rz/InvestDesk`.
- Target InvestDesk `main` at authorization: `e21b5be07c5e0295d21b7aea8d1c40f1101fbebc`.
- Target current task: `MVP-D Decision ↔ Transaction Traceability Planning Gate`.
- InvestDesk's own `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, accepted contracts/ADRs, and verified Git remain authoritative for InvestDesk.

## In scope — read-only validation only

1. Read the three accepted Engineering-Governance Skills and only references/templates needed for this review.
2. Read InvestDesk `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, relevant product/ADR/contract material, and the smallest task-relevant source/test set needed to validate routing.
3. Evaluate Project Governance fit: fact ownership, task authorization, business-first flow, planning-versus-construction boundary, proportional verification, handoff/freshness behavior, and project-local rules that should remain local.
4. Evaluate Domain Navigation fit by routing the current MVP-D task to the minimum semantic Domain set and identifying business authorities, persistence/state owners, source entry points, relevant symbols/tests, and unresolved gaps.
5. Confirm whether Incident Doctor should trigger. If no real evidence-deficient failure blocks the current planning decision, record `DOCTOR_NOT_TRIGGERED` rather than inventing an incident or probe.
6. Compare findings with Phase E RemoteOrbit, especially whether the `CURRENT_STATUS` versus `CURRENT_TASK` ownership lesson repeats outside incident work.
7. Decide whether two-project evidence now justifies any minimal reusable Skill corrective. Recommend only; do not edit the Skill in this task.
8. Recommend the smallest later InvestDesk adoption, but do not implement it.

## Hard boundaries

- InvestDesk mutation: FORBIDDEN.
- No edits to InvestDesk controls, docs, ADRs, contracts, source, tests, schema, migrations, DB, API, frontend, branches, refs, PRs, worktrees, runtime, or acceptance environment.
- Do not implement MVP-D or change its business contract from this pilot.
- Do not authorize local construction, merge, or browser/LAN acceptance.
- Do not modify reusable Engineering-Governance Skill contents during validation.
- No new Skill, executable helper, index, database, daemon, Repo Map program, diagnostic platform, or broad repository survey by default.
- Findings are evidence for a later design decision only.

## Validation method

Use direct repository evidence. Important claims should cite concrete InvestDesk controls, accepted contracts/ADRs, source paths, symbols, tests, or Git facts. Keep direct observations separate from interpretation. Unsupported facts stay `unknown` or `unresolved`.

For Domain Navigation:

`InvestDesk CURRENT_TASK -> affected semantic Domain(s) -> accepted business authority -> candidate persistence/service/read-model/API/UI source -> focused tests -> confirmed route + unresolved gaps`

Do not start with a whole-repository survey. Expand only when the current MVP-D contract question requires it.

For Incident Doctor:

First ask whether a real failure, unexplained behavior, or unsafe ambiguity currently blocks safe progress and whether existing evidence is insufficient. If not, Doctor must remain inactive.

## Acceptance criteria

The validation report must answer:

- whether a fresh AI can identify the current InvestDesk authorization without chat history;
- whether the MVP-D planning task can be routed to the correct business/domain authorities and a bounded source/test set;
- whether business truth, immutable ledger facts, human Decision intent, Position derivation, Workspace/Timeline composition, and relation ownership stay distinct;
- whether the three-file model adds clarity without turning ordinary feature planning into incident-style governance;
- whether Incident Doctor correctly does not trigger;
- whether the Phase E control-plane lesson repeats, does not repeat, or needs narrower wording;
- whether evidence from both RemoteOrbit and InvestDesk now supports a reusable Skill corrective;
- what the minimum later InvestDesk adoption should be, if any.

## Verification level

`V0 — read-only integration validation`.

Required evidence:

- exact InvestDesk remote `main` identity used for the review;
- exact Engineering-Governance accepted Skill revision used;
- cited InvestDesk controls plus focused business/source/test evidence;
- no InvestDesk mutations;
- no reusable Skill mutations;
- explicit unknowns and review limits;
- final freshness check of InvestDesk `main` before handoff.

## Current stop point

`ACTIVE_READ_ONLY_VALIDATION`

After the read-only review, return findings and a proposed next phase. Do not start InvestDesk adoption or reusable Skill corrective work without a new explicit authorization.
