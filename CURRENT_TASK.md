# CURRENT TASK — Capability Architecture Completion v0.6.0

Date: 2026-10-14

Repository: `Lost0rz/Engineering-Governance`

Task ID: `EG-CAPABILITY-ARCHITECTURE-COMPLETION-062`

State: `ACTIVE`

Mode: remote reusable-source architecture completion before integrated Plugin/runtime acceptance

## Objective

Complete the full seven-Skill Engineering Governance v0.6.0 architecture before running local Plugin/runtime acceptance. Integrate the new Skills into one end-to-end governed engineering lifecycle, complete their composition and artifact-authority contracts, define the final integrated acceptance matrix, then freeze the architecture for one consolidated acceptance pass.

## Planning context

- Related document: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Document section / work packages: `WP6` through `WP10`.
- Relationship to plan: Task 061 established the seven-Skill source skeleton. Task 062 completes cross-Skill architecture and acceptance specification; it does not run installed Plugin/runtime acceptance.

## Accepted baseline

- Latest literal branch HEAD at task start: `b70f2b7cd76c199229989a287c83ea3bea0081e3`.
- Task 061 Delivery / Semantic HEAD: `c97d3cef13ac5546bf00d9d1eb4d620c88ffad57`.
- The `c97d3... -> b70f2...` advance is limited to `CURRENT_STATUS.md` / `CURRENT_TASK.md` and is therefore control-only for delivery identity.
- Branch: `codex/capability-model-v0.6.0`.
- PR: `#26` — OPEN / DRAFT / UNMERGED.
- Published/installed baseline remains Plugin `0.5.5`.

## In scope

1. Add a central capability-composition contract for the seven Skills and their return paths.
2. Integrate Solution Design, Execution Orchestrator, Agent Handoff, and Evidence Audit into Project Governance's normal development lifecycle rather than only its outer routing layer.
3. Classify handoff requests/receipts, execution ledgers, design records, audit reports, and reviewer findings explicitly as non-control artifacts unless a project authority separately owns a durable record.
4. Complete execution model tiers, writer/parallel gates, review gates, context packaging, recovery and integration semantics.
5. Complete mode-specific handoff request/receipt semantics for `EXECUTE`, `AUDIT`, `DIAGNOSE`, `REVIEW`, and `VERIFY`.
6. Complete evidence-audit profiles and evidence-identity rules for code/diff, PR/merge, CI, release/provenance, and post-change verification.
7. Connect Solution Design to durable planning/task reconciliation and implementation convergence.
8. Add a repository-wide Skill Engineering quality contract for trigger design, progressive disclosure, composition boundaries, and over-trigger prevention without creating an eighth Skill.
9. Define one integrated acceptance matrix covering positive routes, negative/over-trigger cases, composition, handoff anti-duplication, model escalation, writer authority, and evidence identity.
10. Keep PR #26 Draft until the architecture is complete and the later integrated acceptance pass succeeds.

## Out of scope

- Running local installed Plugin discovery/routing/runtime acceptance before architecture freeze.
- Testing one new Skill at a time as a separate acceptance milestone.
- Publishing/tagging/releasing v0.6.0.
- Merging PR #26.
- Adding daemons, model-router executables, databases, enforcement runtimes, or a fourth project control file.

## Verification level, cadence, and rationale

`V2` source architecture change.

Construction cadence for this task:

- during architecture construction, use only bounded static sanity checks needed to avoid broken paths/frontmatter/internal contradictions;
- do **not** perform per-Skill installed Plugin/runtime acceptance;
- after WP6–WP10 are complete, perform one integrated remote source-architecture audit on the frozen architecture;
- installed Plugin/Web/Codex routing/runtime acceptance is a later consolidated task against that frozen source identity.

This intentionally follows `architecture complete -> freeze -> integrated acceptance`, not `build one -> test one`.

## Acceptance criteria

- Project Governance internal lifecycle explicitly composes all six narrower Skills where applicable.
- No new artifact competes with `AGENTS.md`, `CURRENT_STATUS.md`, or `CURRENT_TASK.md` authority.
- The new Skills have complete operational contracts, not only trigger skeletons.
- Model/concurrency/writer decisions are bounded and no silent escalation path remains.
- Handoff request/receipt profiles are sufficient for Web/local and controller/worker transfers without duplicating controls.
- Evidence Audit has explicit audit profiles and identity semantics.
- Durable planning and Solution Design converge cleanly into authorized execution.
- Skill Engineering quality rules exist without adding a top-level Skill.
- A single integrated acceptance matrix is defined and no installed Plugin/runtime acceptance has been run prematurely.
- PR #26 remains Draft at Task 062 close.

## Stop conditions

- A proposed architecture change creates a second task/status/control authority.
- A new Skill would overlap an existing owner's core responsibility without a distinct trigger/return contract.
- The branch acquires implementation unrelated to v0.6.0 architecture completion.
- A runtime/installed acceptance result is required to decide architecture but cannot be separated from source design; record it as an explicit later acceptance dependency rather than silently testing one Skill early.

## Handoff / current stop point

Task 062 is authorized for remote source architecture completion. The next successful terminal handoff is **architecture frozen and ready for consolidated integrated acceptance**, not release/merge.
