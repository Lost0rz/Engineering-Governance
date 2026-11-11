# Outcome-based Skill routing

Start from the requested outcome. Only invoke a specialist when its method will materially help; do not load all Skills as a checklist.

| Requested result | Skill |
| --- | --- |
| Normal code change, coordination, test/delivery decisions | `project-governance` |
| UI/UX concept, visual implementation, design review | `design` |
| Engineering architecture, API or state ownership | `solution-design` |
| Unknown code owner, source, dependency or test route | `domain-navigation` |
| Evidence-led failure investigation | `incident-doctor` |
| Parallel work, subagents or delegated execution | `execution-orchestrator` |
| A real cross-context transfer needing structured context | `agent-handoff` |
| Explicit formal audit or acceptance/readiness verdict | `evidence-audit` |
| Create/refresh compact derived project context | `project-profile` |

Use the selected Skill's **own** design/audit/diagnostic methods and acceptance standards. Return its result to the current task instead of starting a new authorization chain. A status query is not automatically a formal audit, and a known bug is not automatically an incident.

For a Web/local task, a linked Issue/PR and short current instruction often replace a separate Card. Receiving environments own actual tools, model choices and writer permissions.
