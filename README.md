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
- active task control, selected explicitly by `AGENTS.md`: FILE_CONTROL uses legacy Task/Status files; legacy/default ISSUE_CONTROL uses an approved GitHub Issue/spec revision and meaningful decision/final comments. A separately opted-in, independently host-verified G1/G2 autonomy path is a **candidate** and remains inactive until its trust boundary is proven;
- implementation authority — canonical source/schema/config/workflow/persisted contract/state owner for the implementation class;
- observed evidence — CI/test results, PR/host state, runtime/review/audit/probe observations.

A Profile or Domain Map is a derived projection. If it conflicts with its authority, the authority wins and the projection is stale.

## Normal route

Ordinary software/project work enters `project-governance`. Use narrower capabilities only when their semantic trigger applies. `solution-design` handles engineering architecture/state ownership; `design` handles bounded UI/UX/frontend visual direction and execution. They may compose under one Project Governance task without becoming parallel task authorities.

In legacy/default ISSUE_CONTROL, the selected verified 19-field `EXECUTION_SPEC_V1` and its direct or opted-in delegated exact-revision GitHub approval authorize bounded implementation; meaningful PAUSE/TERMINATE/final Issue receipts are posted while PR/CI remain separate evidence. The proposed G1/G2 risk-scoped path accepts a simpler 8-field `AUTONOMY_SCOPE_V1` policy-only input but still requires independent GitHub host authorization and credential separation before routine Issue comments or exact-digest approval comments can be omitted. The current source deliberately fails closed on that path. An ordinary merge or package release is a separate host-governed action, not automatically G3 by name. See `skills/project-governance/references/issue-control.md`, `issue-execution-contract.md` and `issue-control-migration.md`.

Changing agent/session/machine/context does not create a new task. Same-purpose continuation keeps the task and, when safe, the current PR/workspace. Handoffs transport authority references + fresh delta; they do not restate a second task contract.

## Environment policy

Concrete Sub Agent model/reasoning, parallel capacity, delegation limits, tools, and runtime/workspace constraints are resolved from the current execution environment only when decision-relevant. Reusable policy does not copy one environment's values into another.

## Verification

Authorization risk (`G0`–`G3`), verification evidence (`V0`–`V3`) and execution deviation (`L0`–`L3`) are distinct. Verification follows affected consequence and evidence identity. Semantic evidence and live repository-host gates are separate claims. Missing checks are not PASS. Installed/runtime acceptance is performed only after a frozen source candidate exists.

## Maintainer references

- `references/SKILL_ENGINEERING.md` — Skill design quality.
- `skills/project-governance/references/global-routing.md` — capability selection.
- `skills/project-governance/references/artifact-lifecycle.md` — artifact ownership/refresh lifecycle.
- `skills/design/references/module-map.md` — Design source-module status and composition boundary.
- `skills/agent-handoff/references/handoff-contract.md` — card/receipt contract.


### Issue Control local preflight

For a repository that **explicitly** adopted ISSUE_CONTROL, read the complete fresh Issue using `gh issue view <number> -R owner/repo --json number,body,state,comments > issue.json`. The lightweight bundled validator at `skills/project-governance/scripts/issue-spec-check.py` supports `digest` (structural spec + SHA256), legacy `verify --approvers <trusted-github-logins>` (authenticated matching SPEC_APPROVAL_V1, or explicit delegated mode), and a separate `autonomy-verify` candidate that always returns STOP without trusted host and credential-separation evidence. None of these checks proves source ownership or replaces real local writer safety. Use `python3 -m unittest discover -s skills/project-governance/scripts -p 'test_*.py' -v` for the bounded contract scenarios. Legacy/default Issue execution still requires the matching authorized exact-digest approval; in a future independently accepted active autonomy mode, a host grant may replace only that approval-comment prerequisite for in-envelope G1/G2 work. Evidence remains recoverable from the appropriate Issue/PR/commit/CI/receipt surfaces, not Git status-only commits.
