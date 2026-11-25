# Outcome-based Skill routing

Start directly from the requested outcome (Direct-Entry Fast Path). When a request clearly matches a specialist Skill, enter that Skill directly without an intermediate `project-governance` hop; do not load all Skills as a checklist.

| Requested result | Primary Skill | Do not use first when |
| --- | --- | --- |
| Normal code change, CI test routing (`ci-router.py`), PR/delivery | `project-governance` | Task is purely UI design, architecture comparison, blocking diagnosis, or formal audit |
| UI/UX concept, visual polish (`MICRO_POLISH`), spec, or visual review | `design` | Work is backend/API/state ownership or a simple non-visual bug |
| Engineering architecture, API, data flow, or state ownership | `solution-design` | Clear bug fix or obvious canonical owner exists |
| Unknown code owner, source, dependency, or test route | `domain-navigation` | Target files/symbols are already known |
| Evidence-led failure diagnosis when safe next step is blocked | `incident-doctor` | Existing error/test/diff already supports a direct fix |
| Intra-session plan-to-execute handoff, batching, or Sub Agents | `execution-orchestrator` | Work is cohesive single-stream inline work |
| Real cross-context transfer needing structured context | `agent-handoff` | An Issue/PR link + short prompt suffices, or work stays in-session |
| Explicit formal code/PR/CI/release audit or readiness verdict | `evidence-audit` | User only asks for a quick status check or active fix |
| Create, shrink, rebuild, or audit compact derived project context | `project-profile` | Simply reading an existing Profile for orientation |

Use the selected Skill's **own** design, diagnostic, or audit standards without restarting an extra authorization chain. Return to `project-governance` only when cross-domain scope changes or repository CI/PR delivery requires coordination.

For Web/local tasks, a linked Issue/PR and short instruction often replace a separate Card. Host permissions and host orchestration/model rules always govern actual tools, subagents, and writes.
