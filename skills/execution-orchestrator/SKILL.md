---
name: execution-orchestrator
description: Use when an already-authorized engineering task needs explicit decomposition, multiple execution roles/agents, parallel or sequential scheduling, model-tier selection, resumable multi-step execution, or controlled integration of independent work.
---

# Execution Orchestrator

Use this Skill only after Project Governance has established valid task authority. It controls **how authorized work is executed**, not what work is authorized.

Read [Execution contract](references/execution-contract.md) when orchestration is needed.

## Default posture

The lightest safe executor topology wins.

- One executor is preferred when one context can safely complete the task.
- Parallel readers/scouts/reviewers are preferred over parallel writers.
- Keep one writer for overlapping state/behavior authority.
- Multiple writers are allowed only when their write authorities and workspaces are proven disjoint and an integration check is defined.
- Do not dispatch a subagent merely because the capability exists.
- Do not add per-task review loops when the risk/scope does not justify them.

## Execution flow

1. Read the active task and any accepted design/plan it links.
2. Identify work units that are independently checkable and the dependencies between them.
3. Choose executor topology: inline, sequential delegated, parallel read-only, or proven-disjoint parallel writers.
4. Assign each role only the context it needs. Use `agent-handoff` when responsibility crosses agent/session/machine boundaries.
5. Select model capability proportional to the role. Architecture/high-risk judgment may justify the strongest available model; mechanical bounded work should not silently inherit it.
6. During long/multi-agent execution, use an **ephemeral recovery ledger** only when needed to survive compaction/resume. The ledger records completed units, evidence, rulings, and resume point; it is not task authority and should be removable at closeout.
7. Integrate results under the original writer/task authority and run verification proportional to the changed system.
8. Return execution outcome/evidence to Project Governance for audit, alignment, and lifecycle decisions.

## Hard rules

- **No silent model escalation.** If a requested/allowed tier is unavailable, stay within an explicitly allowed fallback or surface the mismatch; do not silently jump to a materially more expensive/capable tier.
- **No authority by delegation.** A subagent brief cannot expand scope beyond `CURRENT_TASK.md`.
- **No context dumping by default.** Give delegated agents bounded references/briefs rather than full chat history or whole-control copies.
- **No overlapping concurrent writers without proof.** Branch/worktree separation alone does not prove semantic write independence.
- **No blind trust in agent success.** Integrate from returned evidence and actual repository state.

## Output contract

Report the chosen topology, role/write authority, model policy actually used, completed work units, verification/integration evidence, unresolved conflicts/rulings, and resume state if execution remains incomplete.
