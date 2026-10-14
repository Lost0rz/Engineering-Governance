# Global Skill routing

This contract answers one question: **which Engineering Governance Skill should handle the request now?** It selects capability; it does not duplicate Skill procedures or project facts.

## Routing precedence

1. Follow higher-priority system, developer, user, and explicitly selected Skill instructions.
2. Follow the selected repository's applicable `AGENTS.md` and project controls.
3. For software/project/repository engineering work, use `project-governance` as the normal Engineering Governance entry unless a higher-priority instruction already selected a narrower route.
4. Route conditionally only for the bounded capability whose trigger is met, then return to the governing caller.

Project Governance remains lightweight for simple clear work: entering it does not require extra plans, agents, worktrees, audits, or broad validation merely because the Plugin is active.

## Route table

| Situation | Route | Return path |
| --- | --- | --- |
| Establishing/using project authority, starting/reconciling authorized work, verification-tier choice, workspace lifecycle, final alignment/closeout | `project-governance` | Remain here unless a narrower capability is needed. |
| Materially ambiguous requirements, cross-boundary architecture/state ownership, competing options, or durable design decisions must be resolved before implementation | `solution-design` | Return accepted design and reconciliation need to Project Governance. |
| Authorized work needs decomposition, multi-agent/role scheduling, parallelism, delegated-model policy, or resumable execution | `execution-orchestrator` | Return execution evidence/result to Project Governance. |
| Responsibility crosses agents/sessions/machines/contexts and needs a bounded request/receipt | `agent-handoff` | Return to the caller/receiver workflow; handoff never becomes task authority. |
| Independent implementation/code/PR/CI/release/merge-readiness evidence verdict is requested | `evidence-audit` | Return verdict/findings to Project Governance or the requesting read-only caller. |
| Domain/capability/authority/source/symbol/runtime/dependency/test route is unclear | `domain-navigation` | Return verified route/unresolved gap to caller. |
| A real failure/unexplained unsafe ambiguity blocks progress and existing evidence is insufficient for the next safe decision | `incident-doctor` | Return evidence/fix boundary to Project Governance when authorization/change is needed. |
| Bug/failure already has enough evidence for safe action | Stay in authorized Project Governance flow | Do not enter Doctor merely because a defect exists. |
| Non-project/non-engineering request | No Engineering Governance route required | N/A. |

## Composition examples

- `project-governance -> solution-design -> project-governance`
- `project-governance -> execution-orchestrator -> project-governance`
- `execution-orchestrator -> agent-handoff -> delegated role -> agent-handoff receipt -> execution-orchestrator`
- `project-governance -> evidence-audit -> project-governance`
- any caller -> `domain-navigation` -> caller when routing evidence is unclear
- `project-governance -> incident-doctor -> domain-navigation -> incident-doctor -> project-governance` only when the Doctor evidence gate and navigation need both apply

A handoff/delegation never creates a second task authority. Narrow Skills do not override project controls.

## Anti-duplication boundary

The global managed block contains only route-selection semantics. Do not copy into it control-plane procedures, design workflows, orchestration/delegated-model rules, handoff templates, audit procedures, workspace lifecycle, V0–V3 details, Doctor probe methods, or current project facts.

## Ambiguity rule

If multiple capabilities appear relevant, keep Project Governance as authority/lifecycle owner and invoke the narrow capability only for the part it owns. Do not create a Router Skill; this file is the routing policy.
