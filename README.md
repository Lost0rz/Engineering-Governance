# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering Skills, routing contracts, templates, and reference material. Project facts stay with the project; reusable workflow stays here.

## Capability model

The current source defines nine top-level Skills:

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
- active task control — selected by each repository's accepted authority, with execution specifics owned by `project-governance` rather than restated here;
- implementation authority — canonical source/schema/config/workflow/persisted contract/state owner for the implementation class;
- observed evidence — CI/test results, PR/host state, runtime/review/audit/probe observations.

A Profile or Domain Map is a derived projection. If it conflicts with its authority, the authority wins and the projection is stale.

## Governance workflow owner

The reusable engineering workflow is owned by the installed Engineering Governance Skills. `project-governance` is the normal entry; capability selection is maintained in [`global-routing.md`](skills/project-governance/references/global-routing.md), while authorization and approval modes are maintained in [`issue-control.md`](skills/project-governance/references/issue-control.md). This README describes repository capabilities but does not define a separate execution or authorization contract.

## Environment policy

Concrete Sub Agent model/reasoning, parallel capacity, delegation limits, tools, and runtime/workspace constraints are resolved from the current execution environment only when decision-relevant. Reusable policy does not copy one environment's values into another.

## Verification

Proportional verification and evidence reuse belong to [`verification-tiers.md`](skills/project-governance/references/verification-tiers.md). Authorization risk and deviation contracts belong to [`issue-execution-contract.md`](skills/project-governance/references/issue-execution-contract.md). Current CI/host and installed-runtime evidence remain separate from this documentation.

## Maintainer references

- `references/SKILL_ENGINEERING.md` — Skill design quality.
- `skills/project-governance/references/global-routing.md` — capability selection.
- `skills/project-governance/references/artifact-lifecycle.md` — artifact ownership/refresh lifecycle.
- `skills/design/references/module-map.md` — Design source-module status and composition boundary.
- `skills/agent-handoff/references/handoff-contract.md` — card/receipt contract.


### Issue Control tooling

The canonical Issue-spec verifier is [`issue-spec-check.py`](skills/project-governance/scripts/issue-spec-check.py). Its supported commands, opt-in boundaries, and receiver preflight are defined by the owning [`issue-control.md`](skills/project-governance/references/issue-control.md), not by this README. The separately opted-in, independently host-verified G1/G2 route uses the 8-field `AUTONOMY_SCOPE_V1` as policy-only input. It remains inactive until trusted host evidence is established; do not infer execution permission from schema or local snapshots.
