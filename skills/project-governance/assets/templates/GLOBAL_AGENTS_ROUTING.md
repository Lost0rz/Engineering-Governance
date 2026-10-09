<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
## Engineering Governance Skill routing

For software, repository, or project engineering work that acts on or reasons about a project/repository, use `project-governance` as the normal Engineering Governance entry point unless a higher-priority instruction explicitly selects another route. Project Governance should scale its procedure to the task; simple low-risk work does not require extra plans, worktrees, broad scans, or broad validation merely because this route is active.

Use `domain-navigation` when the responsible Domain/capability, semantic authority, source location, symbol, runtime entry, dependency, or relevant test cannot be established safely. Return the verified route or unresolved gap to the calling workflow; do not use Domain Navigation as a substitute for task authorization or diagnosis.

Use `incident-doctor` only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and current evidence is insufficient for the next safe decision. If an incident also needs source/authority location, Incident Doctor may use `domain-navigation` for that bounded purpose and then resume diagnosis. If diagnosis requires a behavior change outside the active authorization, return to `project-governance` before mutation.

Do not force these Skills onto non-project or non-engineering requests. This block selects Skills only; follow the selected Skill and the target repository's own `AGENTS.md`/controls for procedure and project facts.
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
