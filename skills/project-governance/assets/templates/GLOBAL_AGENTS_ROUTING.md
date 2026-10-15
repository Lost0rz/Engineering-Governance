<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
## Engineering Governance Skill routing

For ordinary software, repository, or project engineering work, use `project-governance` as the normal entry unless a higher-priority instruction or explicit bounded Skill selection determines another route. Keep simple work lightweight.

Use `project-profile` only when creating, rebuilding, shrinking, or auditing the compact derived project context/index. It is not task authority or a Domain Map replacement; repository/project-managed Profile mutation still requires compatible task authorization.

Use `solution-design` for material engineering requirements/architecture/state-ownership/API/data-flow/implementation-boundary ambiguity. Use `design` for bounded UI/UX/frontend interaction and visual design/redesign, including hierarchy, composition, typography, density, interface copy, design specification and visual execution critique. Mentioning the word “design” alone is not enough to select `design`.

For mixed frontend workflow questions, distinguish:
- interaction workflow — how users see, understand, navigate, edit, act and receive feedback -> `design`;
- business/state workflow — canonical state transitions, data/state ownership, API/data-flow responsibility, persistence or implementation boundaries -> `solution-design` when materially ambiguous.

Use `execution-orchestrator` for useful decomposition/delegation/recovery; `agent-handoff` for bounded cross-context transfer; `evidence-audit` for formal read-only evidence/acceptance/readiness verdicts; `domain-navigation` for unclear semantic/source/symbol/test/runtime/dependency routes; and `incident-doctor` only for a blocking evidence gap.

Routing is selective, not cumulative, but selected Skills are not isolated silos. A bounded Skill may call another capability when a concrete unresolved dependency crosses that capability's real boundary and can materially change the current decision. State the unresolved dependency, decision impact, capability, bounded expected return, and where the originating capability will resume. Return to that owner/stage after the bounded result is sufficient.

Do not walk the installed Skills as a checklist or invoke a Skill for general enrichment, completeness, a second opinion without an unresolved dependency, or because it is installed. An already-understood frontend redesign can remain `project-governance → design`; if Design genuinely cannot identify a needed backend authority/source route, it may call `domain-navigation`, receive the verified route, and then resume Design.

When the requested output itself is a construction/execution/audit/review/verify/diagnose Card, instructions, or structured Receipt intended for another agent, session, machine, reviewer, or execution context, use `agent-handoff` for that transfer artifact. Preserve current task authority; generating the Card does not create a new task.

Simple advisory read-only status/evidence inspection may remain in `project-governance`. Keywords alone do not select a Skill. These capabilities compose without creating parallel task authority. Follow the selected Skill and the target repository's own authorities for project facts.

For governed user-facing responses, make routing observable: report the actual `Governance route` and actual `Skills used`; do not list installed/discovered Skills that did not materially govern the work.
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
