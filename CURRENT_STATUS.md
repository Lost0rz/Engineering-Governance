# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.5`.

- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- ChatGPT Web Plugin: `0.5.5`.
- Mac mini Codex accepted Plugin baseline: `0.5.5`.
- MacBook Air Codex accepted Plugin baseline: `0.5.5`.

No v0.6.0 release or installed-Plugin acceptance has been performed.

## v0.6.0 architecture — ACTIVE COMPLETION

Task `EG-CAPABILITY-ARCHITECTURE-COMPLETION-062` is active on branch `codex/capability-model-v0.6.0` and PR #26 remains OPEN / DRAFT / UNMERGED.

Task 061 established the initial seven-Skill source skeleton and basic routing. The current task completes the internal architecture before any installed Plugin/runtime acceptance.

Exactly seven top-level Skills remain the target model:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Architecture gap found after Task 061

The outer routing/source skeleton is present, but some reusable internal Project Governance references still reflect the former three-Skill lifecycle. In particular, the normal development flow does not yet explicitly compose Solution Design, Execution Orchestrator, Agent Handoff, and Evidence Audit through the task lifecycle.

Task 062 therefore owns cross-Skill integration rather than local acceptance.

## Accepted sequencing decision

The current v0.6.0 sequence is:

`complete full architecture -> freeze source architecture -> integrated remote audit -> consolidated installed Plugin/Web/Codex acceptance -> merge/release preparation`

Do not create separate acceptance milestones for each new Skill while architecture remains in motion. Bounded static consistency checks during construction are allowed; installed Plugin/runtime acceptance is deferred until architecture freeze.

## Current architecture work packages

- WP6 — end-to-end capability composition and Project Governance lifecycle integration.
- WP7 — execution/orchestration and handoff operational contracts.
- WP8 — evidence-audit, design convergence, and artifact-authority integration.
- WP9 — Skill Engineering quality/routing discipline without a new top-level Skill.
- WP10 — one integrated acceptance matrix for the frozen architecture; define now, execute later.

## Active problems and blockers

No blocking source defect is currently known. The known gap is architectural completeness, not Plugin runtime failure.

PR #26 must remain Draft until Task 062 finishes and the later consolidated acceptance task verifies the frozen architecture.

## Next intended milestone

Finish WP6–WP10, perform one final remote source-architecture audit, freeze the resulting Delivery / Semantic HEAD, then hand off a single consolidated v0.6.0 acceptance task.
