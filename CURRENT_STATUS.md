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

## v0.6.0 stabilized architecture — FROZEN FOR CONSOLIDATED ACCEPTANCE

Task `EG-CAPABILITY-MODEL-POLICY-STABILIZATION-064` completed the user-directed delegated-model stabilization on branch `codex/capability-model-v0.6.0`.

- New Architecture Delivery / Semantic HEAD: `31d9d94f1f59a3d5b49fb7c614f37ec752cff479`.
- Prior Task 063 semantic candidate `5ad4f4a4465714f571bce4b9d095d741cd361c03` is historical/superseded for final v0.6.0 acceptance because model-policy source semantics changed.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- PR host mergeability observed during Task 064 audit: `mergeable=true`.
- Commit/check statuses on the new semantic head: none reported; **CI PASS is not claimed**.
- Installed Plugin/Web/Codex integrated acceptance: `NOT_RUN_BY_DESIGN`.

## Active delegated-model policy

Current v0.6.0 stabilization policy:

```text
SUBAGENT_MODEL_POLICY: DEFAULT_ONLY
SUBAGENT_MODEL: environment configured default
SUBAGENT_REASONING: environment configured default
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

- Sub Agents remain a positive throughput/context-isolation capability and safe useful parallelism is encouraged.
- Delegated Sub Agents use the execution environment's configured default Sub Agent model and default reasoning setting.
- Current user Codex convention is a default such as `gpt-6-luna` with `xhigh` reasoning effort; reusable source treats this as environment configuration rather than universal provider/model truth.
- Model identity and reasoning effort are distinct; `xhigh` reasoning is not a HIGH-model selection.
- No automatic or intentional stronger-model escalation is allowed during stabilization.
- `LOW / STANDARD / HIGH` remain inactive future capability vocabulary only; they do not currently route delegated Sub Agents.
- Re-enabling stronger-model/tier routing requires a later explicit user/project policy change.

## Seven-Skill model preserved

Exactly seven top-level Skills remain:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

## Task 064 remote source audit

`V2 remote source-architecture corrective audit: PASS` for semantic head `31d9d94f1f59a3d5b49fb7c614f37ec752cff479`.

Verified:

- Task 064 changed governance/Skill/design/acceptance Markdown/control sources only; no release workflow, runtime, daemon, database, or model-router implementation was added;
- exactly seven top-level Skill directories remain;
- Plugin metadata remains `0.6.0`;
- Execution Orchestrator and Project Governance now use `DEFAULT_ONLY` delegated-model semantics;
- active reusable rules no longer instruct delegated Sub Agents to select or escalate to a stronger model during stabilization;
- `xhigh` reasoning is explicitly separated from model identity/tier;
- safe positive Sub Agent parallelism remains intact;
- global routing is delegated-model-policy neutral and does not embed provider/model names;
- Skill Engineering treats safe parallelism under-use as a possible defect while recognizing stronger-model non-use as intentional stabilization policy;
- parent capability-model and hardening design authorities are aligned with Task 064;
- integrated acceptance now tests default-model continuity, reasoning/model separation, no stronger-model inheritance/escalation, positive safe parallelism, same-task cross-context continuation, and independent audit semantics;
- PR #26 remains Draft and mergeable;
- no commit/check status exists on the semantic head, so CI PASS is not claimed.

## Remaining dependency

Run one consolidated installed Plugin/Web/Codex acceptance pass against semantic head `31d9d94f1f59a3d5b49fb7c614f37ec752cff479` or a proven control-only descendant using `references/V060_INTEGRATED_ACCEPTANCE.md`.

Do not split acceptance into one Skill at a time. Do not patch reusable source inside installed Plugin caches; reusable-source defects return to the remote source flow.

## Task 064 control alignment

- Related document: `documents/engineering-governance-capability-hardening-v0.6.0.md`.
- Parent document: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Document alignment: `UPDATED` — both durable design authorities now reflect `DEFAULT_ONLY` stabilization.
- `CURRENT_STATUS.md`: `UPDATED`.
- `CURRENT_TASK.md`: `UPDATED`.
- Control alignment: `PASS`.
