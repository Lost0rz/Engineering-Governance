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

## v0.6.0 architecture — MODEL POLICY STABILIZATION ACTIVE

Task `EG-CAPABILITY-MODEL-POLICY-STABILIZATION-064` is active on branch `codex/capability-model-v0.6.0`.

- Prior hardened semantic candidate: `5ad4f4a4465714f571bce4b9d095d741cd361c03`.
- Task 063 closeout head: `f5c998ab72b6a27577a66cc87beb7a4be6570f37`.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- Installed v0.6.0 integrated acceptance remains `NOT_RUN_BY_DESIGN`.

The Task 063 architecture freeze is reopened only for a narrow user-directed model-policy correction before consolidated acceptance.

## User-decided model stabilization policy

- Sub Agents remain a positive parallel execution capability; safe useful parallelism is still encouraged.
- During the current stabilization period, delegated Sub Agents use the execution environment's configured **default Sub Agent model and default reasoning setting**.
- The user's current Codex convention is the configured default `gpt-6-luna` Sub Agent model with `xhigh` reasoning effort; reusable governance should reference the environment default rather than hardcode that provider/model as universal truth.
- `xhigh` reasoning effort is not the same concept as a higher model tier.
- Orchestrator must not select or escalate delegated Sub Agents to a stronger model than the configured default during this stabilization policy.
- `LOW / STANDARD / HIGH` may remain documented as future capability abstractions, but they are not active delegated-model routing choices for this v0.6.0 stabilization period.
- Stronger-model routing may be re-enabled only by a later explicit user/project policy change.

## Seven-Skill model unchanged

Exactly seven top-level Skills remain:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Active work

Task 064 updates only the model-policy semantics needed to make Sub Agent behavior stable and predictable:

- Execution Orchestrator Skill/contract;
- repository/global operating guidance where it currently describes intentional HIGH selection;
- integrated acceptance scenarios;
- existing v0.6.0 hardening design/records where needed for consistency.

Task purpose/context, handoff, audit, Domain Navigation, Incident Doctor and positive parallelism semantics are otherwise preserved.

## Next milestone

Complete Task 064 source correction, run a bounded remote source audit, freeze a new v0.6.0 semantic candidate, then proceed to one consolidated integrated acceptance pass.
