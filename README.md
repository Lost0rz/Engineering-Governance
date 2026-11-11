# Engineering Governance

Reusable AI engineering **workflow, methods and proportional verification**, not a mandatory Issue/approval system. Project-specific source, runtime and business constraints remain with their project.

## Working method

Understand → route to the needed specialist → implement → test affected behavior at sensible milestones → deliver observed evidence.

| Skill | Responsibility |
| --- | --- |
| `project-governance` | Default engineering task, safety and delivery |
| `design` | UI/UX and visual design |
| `solution-design` | Architecture, API and state ownership |
| `evidence-audit` | Formal evidence/readiness audit |
| `incident-doctor` | Blocking fault diagnosis |
| `domain-navigation` | Unclear source or test owner |
| `execution-orchestrator` | Useful delegation and parallelism |
| `agent-handoff` | Real cross-context transfer |
| `project-profile` | Derived project context |

Routing details: [global routing](skills/project-governance/references/global-routing.md).

## Task coordination

Work can start from an authenticated current user instruction or use an existing Issue/PR plan. Issues are optional collaboration, not approvals. Anyone with real GitHub write capability and authorized task intent may create/update them; comments and fixed fields are not required.

Write permission comes from the real execution host. G3-like privilege/security/destructive changes require a separate responsible decision. Routine scope-preserving code adjustments do not.

## Testing and installation

[Verification tiers](skills/project-governance/references/verification-tiers.md) select test scope. Draft development does not auto-run broad GitHub CI; targeted checks are available and readiness/integration runs broader affected or full checks when justified. Plugin preview/build is separate.

The current source [policy](skills/project-governance/assets/control-policy.json) is not an execution token. The installed Web/Desktop/local version and actual host permissions must be verified independently.
