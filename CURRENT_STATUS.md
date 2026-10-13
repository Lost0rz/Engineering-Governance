# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.5`.

- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- ChatGPT Web Plugin accepted baseline: `0.5.5`.
- Mac mini Codex accepted Plugin baseline: `0.5.5`.
- MacBook Air Codex accepted Plugin baseline: `0.5.5`.

No v0.6.0 release or installed Plugin/Web/Codex integrated acceptance has been performed yet.

## v0.6.0 architecture — FROZEN FOR INTEGRATED ACCEPTANCE

Task `EG-CAPABILITY-ARCHITECTURE-COMPLETION-062` completed the full reusable-source architecture on branch `codex/capability-model-v0.6.0`.

- Frozen Architecture Delivery / Semantic HEAD: `26fdc590b4c4ef1e25781f7065626fc87fc349cf`.
- PR: `#26` — OPEN / DRAFT / UNMERGED.
- PR host mergeability observed at architecture-freeze audit: `mergeable=true`.
- Commit/check statuses on the frozen architecture head: none reported; **CI PASS is not claimed**.
- Installed Plugin/Web/Codex acceptance: `NOT_RUN_BY_DESIGN` — deferred until after complete architecture freeze.

## Frozen capability model

Exactly seven top-level Skills:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Accepted architecture semantics

- Project Governance owns normal entry, task/control authority, workspace/writer lifecycle, verification selection, specialist composition, final alignment and closeout.
- Solution Design is conditional for material design/ownership ambiguity, distinguishes verified facts/user decisions/assumptions/agent calls, converges into durable planning when justified, and returns `TASK_RECONCILIATION_REQUIRED` before implementation.
- Execution Orchestrator supports `INLINE`, sequential delegation, parallel read-only and proven-disjoint writer topologies. Capability tiers are `LOW / STANDARD / HIGH`; delegated roles do not silently inherit or escalate to unjustified higher tiers.
- Agent Handoff supports `EXECUTE / AUDIT / DIAGNOSE / REVIEW / VERIFY`; a handoff is `authority references + fresh delta + action boundary + return contract`, not a second task authority.
- Evidence Audit supports `CODE_DIFF / PR_MERGE / CI / RELEASE_PROVENANCE / POST_CHANGE`, binds findings to concrete evidence identity, treats required unknowns as STOP, and separates semantic evidence from live host gates.
- Domain Navigation remains conditional bounded semantic/source/test/runtime route discovery.
- Incident Doctor retains the strict gate: real failure/unsafe ambiguity + blocked progress + insufficient evidence.
- Handoff requests/receipts, execution ledgers, audit reports, reviewer findings, CI/test output and probe observations are evidence/transport artifacts, not project controls by default.
- Skill Engineering maintainer rules require distinct triggers, negative/near-miss scenarios, progressive disclosure and explicit return contracts; they do not create an eighth Skill.

## Integrated acceptance specification

`references/V060_INTEGRATED_ACCEPTANCE.md` is the accepted consolidated acceptance specification.

It covers:

- exact Skill discovery/topology;
- positive routing and negative/over-trigger cases;
- cross-Skill composition;
- Web/local handoff anti-duplication/conflict/receipt behavior;
- model-tier fallback and no-silent-escalation behavior;
- single-writer/disjoint-writer rules;
- evidence-audit identity/CI/PR/release/post-change profiles;
- control/planning authority boundaries;
- Plugin/global-routing/Web/Codex integrated environment acceptance.

The specification is defined but not executed under Task 062.

## Remote source-architecture audit

`V2 remote source-architecture audit: PASS` for the frozen architecture.

Verified:

- exact seven-Skill top-level directory set and no Router Skill;
- Plugin metadata version `0.6.0`;
- global routing/adoption/template semantics match the seven-Skill model and keep specialist capabilities conditional;
- Project Governance internal lifecycle composes the new Skills rather than retaining the old three-Skill flow;
- planning/control/verification contracts are integrated with Solution Design, Agent Handoff and Evidence Audit;
- model tiers, fallback limits, writer/parallel gates and recovery semantics are explicit;
- handoff five-mode contracts and compact receipts are explicit;
- Evidence Audit five profiles and identity rules are explicit;
- Incident Doctor evidence gate remains intact;
- no duplicate task/status/control authority was introduced;
- no universal mandatory TDD/debugging/subagent/worktree ceremony was introduced;
- PR diff at the frozen head contains governance/Skill Markdown/JSON only; no release workflow, daemon, model-router executable or enforcement runtime was added;
- historical v0.5.5 release workflow remains outside the changed-path set.

## Active problems and blockers

No blocking remote source-architecture defect is known from Task 062.

Remaining acceptance dependency: run one consolidated installed Plugin/Web/Codex acceptance pass against frozen semantic head `26fdc590b4c4ef1e25781f7065626fc87fc349cf`. PR #26 remains Draft until that acceptance succeeds and any reusable-source defects are corrected remotely.

## Next intended milestone

Authorize one integrated v0.6.0 acceptance task using `references/V060_INTEGRATED_ACCEPTANCE.md` against the frozen architecture. Do not split acceptance into one Skill at a time.

## Task 062 control alignment

- Related document: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Document alignment: `UNCHANGED` — the durable design matches the completed architecture and does not need a progress-only write at final alignment.
- `CURRENT_STATUS.md`: `UPDATED` — architecture freeze, audit result and remaining acceptance dependency are current.
- `CURRENT_TASK.md`: `UPDATED` — Task 062 is terminal as the architecture-completion task.
- Control alignment: `PASS`.
