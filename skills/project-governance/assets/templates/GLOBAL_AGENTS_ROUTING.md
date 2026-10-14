<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
## Engineering Governance Skill routing

For software, repository, or project engineering work, use `project-governance` as the normal Engineering Governance entry unless a higher-priority instruction or explicit bounded Skill selection determines another route. Keep simple work lightweight.

Use `solution-design` only to resolve material intent/architecture/state-ownership ambiguity before implementation.

Use `execution-orchestrator` when authorized work materially benefits from decomposition, multiple roles/agents, parallel/sequential scheduling, environment-aware delegation, recovery, or controlled integration.

Use `agent-handoff` when responsibility crosses agents, sessions, machines, or execution contexts and a bounded request/receipt is needed.

Use `evidence-audit` when the requested outcome is a read-only evidence/acceptance/readiness verdict separate from implementation. Do not trigger it merely because code, PR, CI, or release is mentioned during corrective work.

Use `domain-navigation` when the responsible Domain/capability/authority/source/symbol/runtime/dependency/test route cannot be established safely.

Use `incident-doctor` only when a real failure or unsafe ambiguity blocks safe progress and existing evidence cannot support the next safe decision.

These Skills compose without creating parallel task authority. Follow the selected Skill and the target repository's own controls for procedure and project facts.
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
