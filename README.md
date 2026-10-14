# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering Skills, routing contracts, templates, and reference material. Project facts stay with the project; reusable workflow stays here.

## Capability model

v0.6.8 has nine top-level Skills:

- **Project Governance** — normal engineering entry; task/control authority, lifecycle, writers/workspaces, verification and closeout.
- **Project Profile** — creates/refreshes a compact derived project-context/index from verified authorities; repository/project-managed mutation still requires compatible task authority.
- **Solution Design** — material engineering requirements/architecture/state-ownership/API/data-flow/implementation-boundary ambiguity.
- **Design** — bounded UI/UX/frontend visual design and redesign. The initial baseline bundles Anthropic `frontend-design` internally so design work routes through Engineering Governance rather than a separate Plugin.
- **Execution Orchestrator** — decomposition, Sub Agents, safe parallelism, environment-aware delegation, recovery/integration.
- **Agent Handoff** — standardized bounded cross-context cards/receipts with separate `CAPABILITY` and `MODE` dimensions.
- **Evidence Audit** — formal read-only evidence/acceptance/readiness verdicts bound to identity and required claims; simple advisory inspection may remain in Project Governance.
- **Domain Navigation** — unclear Domain/authority/source/symbol/test/runtime route.
- **Incident Doctor** — blocking evidence gap requiring minimal diagnosis/probes.

Global routing is policy, not another Skill.

## Design module direction

`design` is the stable external capability boundary. Source-specific design material stays internal to that Skill:

- Anthropic `frontend-design` — active baseline;
- Microsoft design-review/adaptation source — planned, not active;
- UX heuristic/audit source — planned, not active.

This lets the design capability evolve without installing multiple overlapping design Plugins or changing project routing every time a source module is added.

## Project information layers

- project `AGENTS.md` — normative project-specific MUST/MUST-NOT rules and durable boundaries;
- Project Profile — concise descriptive context + pointers to authorities; one current projection surface or explicit primary + mirror;
- Domain/navigation authority — detailed semantic ownership/source/test/runtime route;
- durable planning — long-lived design/rationale/work packages when justified;
- `CURRENT_STATUS.md` — concise current-state snapshot;
- `CURRENT_TASK.md` — single active authorization;
- implementation authority — canonical source/schema/config/workflow/persisted contract/state owner for the implementation class;
- observed evidence — CI/test results, PR/host state, runtime/review/audit/probe observations.

A Profile or Domain Map is a derived projection. If it conflicts with its authority, the authority wins and the projection is stale.

## Normal route

Ordinary software/project work enters `project-governance`. Use narrower capabilities only when their semantic trigger applies. `solution-design` handles engineering architecture/state ownership; `design` handles bounded UI/UX/frontend visual direction and execution. They may compose under one Project Governance task without becoming parallel task authorities.

Changing agent/session/machine/context does not create a new task. Same-purpose continuation keeps the task and, when safe, the current PR/workspace. Handoffs transport authority references + fresh delta; they do not restate a second task contract.

## Environment policy

Concrete Sub Agent model/reasoning, parallel capacity, delegation limits, tools, and runtime/workspace constraints are resolved from the current execution environment only when decision-relevant. Reusable policy does not copy one environment's values into another.

## Verification

Verification follows risk (`V0`–`V3`) and evidence identity. Semantic evidence and live repository-host gates are separate claims. Missing checks are not PASS. Installed/runtime acceptance is performed only after a frozen source candidate exists.

## Maintainer references

- `references/SKILL_ENGINEERING.md` — Skill design quality.
- `skills/project-governance/references/global-routing.md` — capability selection.
- `skills/project-governance/references/artifact-lifecycle.md` — artifact ownership/refresh lifecycle.
- `skills/design/references/module-map.md` — Design source-module status and composition boundary.
- `skills/agent-handoff/references/handoff-contract.md` — card/receipt contract.
