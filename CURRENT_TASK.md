# CURRENT TASK — v0.6.0 Integrated Acceptance

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-V060-INTEGRATED-ACCEPTANCE-067`

Task class: `AUDIT`

State: `ACTIVE`

## Objective

Run one consolidated installed/runtime acceptance against frozen semantic head `f3d47b00cac41ebd19408cef18563c91be67ae53`, covering Web and supported Local Codex environments without modifying reusable source during acceptance.

## Gate 0 — candidate identity / environment readiness

Before behavior scenarios, each tested environment must prove it is actually running the v0.6.0 candidate or a package/install proven from the frozen semantic identity.

- Web: current observed Engineering Governance install exposes only the legacy three Skills (`project-governance`, `domain-navigation`, `incident-doctor`), so the v0.6.0 seven-Skill candidate is **NOT YET PRESENT** in this Web runtime.
- Mac mini Codex: fresh v0.6.0 candidate install/runtime identity not yet observed in Task 067.
- MacBook Air Codex: fresh v0.6.0 candidate install/runtime identity not yet observed in Task 067.

An environment that is not on the candidate is `NOT_READY`, not a v0.6.0 routing PASS/FAIL.

## Acceptance authority

- Source semantic head: `f3d47b00cac41ebd19408cef18563c91be67ae53`.
- Specification: `references/V060_INTEGRATED_ACCEPTANCE.md`.
- Published/accepted baseline remains `0.5.5` until v0.6.0 acceptance and later release work complete.
- No installed cache/source patching is authorized. Reusable defects return to a remote corrective task.

## Current stop point

Complete candidate packaging/install identity for each intended acceptance environment, then run the consolidated matrix. Do not interpret the current Web 0.5.5 behavior as evidence about v0.6.0.
