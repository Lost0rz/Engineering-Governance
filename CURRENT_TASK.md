# CURRENT TASK — Phase E RemoteOrbit Read-Only Skill Validation

Task ID: `EG-REMOTEORBIT-PILOT-READONLY-018`

State: `ACTIVE_READ_ONLY_VALIDATION`

Mode: `BOUNDED_INTEGRATION_VALIDATION`

## Objective

Validate the accepted `project-governance`, `domain-navigation`, and `incident-doctor` Skills against the live RemoteOrbit repository without mutating RemoteOrbit. Determine whether the Skills improve real task routing, evidence discipline, and governance clarity without creating duplicate authority or excessive process.

## Authority and baselines

- Engineering-Governance accepted Phase D merge head: `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Engineering-Governance control baseline entering Phase E design: `ec9f32ca437d324b9fba90086f8814a450343ce4`.
- Target repository: `Lost0rz/RemoteOrbit`.
- Target RemoteOrbit `main` at authorization: `5b9c48ace92818e15850eaa3f21399b1cc2f4031`.
- RemoteOrbit current controls and active incident/recovery task remain authoritative for that repository.

## In scope — read-only validation only

1. Read the three accepted Engineering-Governance Skills and relevant templates/references.
2. Read RemoteOrbit `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, README/setup material, and only task-relevant source/tests/docs needed to validate routing.
3. Evaluate project-governance fit:
   - fact ownership and duplication across the three controls;
   - task authorization clarity;
   - business/product-first flow versus governance overhead;
   - freshness and handoff behavior;
   - any project-specific rules that appropriately remain local rather than moving to the reusable Skill.
4. Evaluate domain-navigation fit:
   - infer the smallest semantic Domain set needed for the current RemoteOrbit task from direct evidence;
   - identify candidate authorities, entry points, important symbols, relevant tests, runtime/diagnostic boundaries, and unresolved gaps;
   - do not perform a whole-repository survey unless the evidence proves it necessary.
5. Evaluate incident-doctor fit against the active incident/recovery context:
   - blocked question;
   - evidence sufficiency;
   - user report versus direct observations versus interpretations;
   - hypotheses and falsification status;
   - fresh incident/runtime identity requirements;
   - root-cause status;
   - minimum safe next decision.
6. Identify concrete friction, ambiguity, redundancy, or missing guidance in the accepted Skills.
7. Recommend the smallest later RemoteOrbit adoption, but do not implement it.

## Hard boundaries

- RemoteOrbit mutation: FORBIDDEN.
- Do not edit RemoteOrbit controls, source, tests, docs, diagnostics, settings, evidence, worktrees, refs, branches, PRs, runtime, app installation, journal, input source, driver, CoreAudio, TCC, LaunchAgents, or hardware state.
- Do not run or authorize RemoteOrbit's journal-recovery procedure from this pilot.
- Do not reinterpret the active RemoteOrbit task or advance its control plane.
- Do not modify the reusable Engineering-Governance Skill contents during validation.
- No new Skill, script, index, database, daemon, Repo Map program, or diagnostic platform.
- Findings are evidence for a later design decision only.

## Validation method

Use direct repository evidence. Important conclusions should cite concrete paths, symbols, tests, or accepted project controls. Keep direct observations distinct from interpretations. Unknown, stale, or unresolved facts remain explicit.

For Domain Navigation, follow:

`RemoteOrbit CURRENT_TASK -> affected semantic Domain(s) -> candidate authority/entry point/symbol/test -> focused source reading -> confirmed route + unresolved gaps`

For Incident Doctor, first ask whether existing evidence is already sufficient for the blocked decision. Do not invent a probe merely to exercise the Skill.

## Acceptance criteria

The validation report must answer:

- Can a fresh AI identify what RemoteOrbit currently authorizes without relying on chat history?
- Can it find the relevant Domain/authority/source/test set for the active task with bounded reading?
- Can it classify the incident evidence without promoting correlation or user report to fact/root cause?
- Does the reusable Skill guidance materially help, duplicate existing RemoteOrbit rules, or create friction?
- Which parts should remain RemoteOrbit-specific?
- What is the minimum later adoption set, if any?
- Is any reusable Skill corrective justified by this real-project evidence, or should the Skills remain unchanged?

## Verification level

`V0 — read-only integration validation`.

Required evidence:

- exact RemoteOrbit remote `main` identity used for the review;
- exact Engineering-Governance accepted Skill revision used for the review;
- cited RemoteOrbit controls and focused source/test evidence;
- no RemoteOrbit mutations;
- no reusable Skill mutations during the review;
- explicit unknowns and limits.

## Current stop point

`ACTIVE_READ_ONLY_VALIDATION`

After the read-only review, return findings and a proposed next step. Do not start RemoteOrbit adoption without a new explicit authorization.
