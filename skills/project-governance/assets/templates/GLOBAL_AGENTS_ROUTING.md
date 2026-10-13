<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
## Engineering Governance Skill routing

For software, repository, or project engineering work, use `project-governance` as the normal Engineering Governance entry point unless a higher-priority instruction explicitly selects another route. Keep simple low-risk work lightweight.

Use `solution-design` only when materially ambiguous requirements, cross-boundary architecture/state ownership, competing options, or durable design decisions must be resolved before implementation.

Use `execution-orchestrator` only when authorized work needs explicit decomposition, multiple roles/agents, parallel/sequential scheduling, model-tier policy, or resumable multi-step execution.

Use `agent-handoff` whenever responsibility crosses agents, sessions, machines, or execution contexts and a bounded request/receipt is needed. A handoff references project authorities plus fresh delta; it does not replace `CURRENT_TASK.md`, `CURRENT_STATUS.md`, or durable rules.

Use `evidence-audit` for an independent or explicit implementation/code/PR/CI/release/merge-readiness evidence verdict. Read-only audit reports stale controls/findings without mutating them.

Use `domain-navigation` when the responsible Domain/capability, semantic authority, source location, symbol, runtime entry, dependency, or relevant test cannot be established safely. Return the verified route/unresolved gap to the caller.

Use `incident-doctor` only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and current evidence is insufficient for the next safe decision. A defect with sufficient evidence stays in normal governed work.

These Skills compose; they do not create parallel task authority. Follow the selected Skill and the target repository's own `AGENTS.md`/controls for procedure and project facts.
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
