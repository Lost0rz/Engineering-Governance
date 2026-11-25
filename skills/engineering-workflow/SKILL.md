---
name: engineering-workflow
description: >-
  Default workflow for localized (G1) and cross-module (G2) implementation,
  proportional checks, parallel batching, intra-session or cross-context
  handoffs, workspaces, and PR delivery. Do not load first for UI styling
  (ui-design), architecture tradeoffs (architecture), CI setup/selection
  (ci-governance), blocking fault probes (incident-doctor), formal audits
  (evidence-audit), or unfamiliar codebase mapping (codebase-context).
---

# Engineering Workflow

Loop: **understand -> batch/implement -> verify proportionally -> report observed facts**.

## Fast route

| Task need | Mode | Next reading |
| --- | --- | --- |
| Clear G1/G2 code change, bug fix, or delivery summary | `DIRECT_BUILD` | **NONE (this file)** |
| Plan-to-execute handoff, Sub Agents, or Handoff Card | `DELEGATE_OR_HANDOFF` | [execution-and-handoff.md](references/execution-and-handoff.md) |
| Worktrees, optional Issue plans, PR push, plugin install | `DELIVERY_OR_WORKSPACE` | [delivery-and-workspaces.md](references/delivery-and-workspaces.md) |

## Risk-tiered action gates (`G0`–`G3`)

- **G0 (Read-only):** inspect and report without mutating files, branches, or worktrees.
- **G1 (Localized recoverable edit):** implement directly; batch independent reads/edits in parallel and verify with focused `V1` unit/module checks at completion.
- **G2 (Cross-module / shared contract / lockfile / schema edit):** inspect upstream/downstream callers and compatibility before editing, update callers atomically, and run `V2` cross-module integration checks at milestone/closeout (reserve `V3` full/release suites for `ready`/`release`).
- **G3 (Privilege, secrets, security trust, destructive data/schema drop, force-push, prod release, or untrusted CI change):** **pause and obtain explicit user decision** before mutating.

## Rules

- **Host authority:** current user intent and host/tool permissions authorize writes; Issues, PR prose, and handoff cards are context only.
- **Consult only on blockers:** pull a specialist Skill only for an unresolved cross-domain dependency, then resume.
- **Verify proportionally:** batch parallel reads/edits per turn; run affected checks at milestones rather than after every line edit; never invent a `PASS` or hide skipped tests.
