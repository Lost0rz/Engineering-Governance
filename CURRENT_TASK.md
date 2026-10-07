# CURRENT TASK — Phase B Project Governance Enrichment Design

Task ID: `EG-PROJECT-GOVERNANCE-ENRICH-DESIGN-011`

State: `WAITING_FOR_USER_DESIGN_REVIEW`

Mode: `BOUNDED_DESIGN_REVIEW`

## Objective

Define the bounded Phase B enrichment of the existing `skills/project-governance/` module so it is operationally useful for normal AI-assisted development without turning governance into a parallel product or heavyweight process.

This task is design-only. No local implementation is authorized until the user explicitly approves the bounded design.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Phase A accepted merge head: `02dd645d06e8fa554e241887c1457f7b15e297b5`.
- Phase A result: accepted, merged to `main`, exactly three Skill modules live.
- Stable historical tag: `v0.1.0^{}` = `738627a0caad330d277f60cfdaff5f153593135e`.
- Exact Phase B implementation baseline will be captured only after design approval and before a local execution card is issued.

## Proposed Phase B file scope

Only the existing `project-governance` module:

- `skills/project-governance/SKILL.md`
- `skills/project-governance/references/control-plane.md`
- `skills/project-governance/references/development-flow.md`
- `skills/project-governance/references/verification-tiers.md`
- `skills/project-governance/assets/templates/AGENTS.md`
- `skills/project-governance/assets/templates/CURRENT_STATUS.md`
- `skills/project-governance/assets/templates/CURRENT_TASK.md`

Root controls may be updated only for task authorization/handoff. No other reusable module is part of Phase B.

## Proposed design

### 1. Three-file control plane becomes operational, not merely descriptive

`control-plane.md` will define:

- one owner per fact/decision class;
- what belongs in `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`;
- what explicitly does **not** belong in each file;
- when each file changes;
- how to avoid duplicating the same fact across files;
- how to preserve current verified state without turning status into a history log.

The templates will mirror those boundaries with concise prompts rather than generic boilerplate.

### 2. Normal development flow remains business-first

`development-flow.md` will define the minimum repeatable flow:

1. read applicable repository guidance and the current task;
2. establish/verify the current baseline needed for the work;
3. identify the affected Domain and route to `domain-navigation` only when code/authority location is unclear;
4. implement the smallest authorized product/business outcome;
5. verify at the chosen risk-proportional level;
6. update only controls whose facts materially changed;
7. hand off or close cleanly.

A material objective/scope change requires updating the active task before implementation continues, but ordinary evidence discovery does not create a new task by itself.

Incident Doctor remains reactive: use it only for a real blocked failure/ambiguity when existing evidence is insufficient.

### 3. Verification tiers gain lightweight selection guidance

`verification-tiers.md` will retain `V0`–`V3` and add simple decision guidance based on change radius and risk, not a numeric scoring bureaucracy.

- `V0`: control/docs/layout only.
- `V1`: localized behavior, narrow blast radius.
- `V2`: domain behavior, persistence/state/external integration within one domain, or meaningful integration boundary.
- `V3`: cross-domain, concurrency/security/system-runtime/release-critical or broad user-critical path.

`CURRENT_TASK.md` must state the chosen level and short rationale. The rule remains: choose the lightest level that can safely establish the task; do not default to the full historical suite.

### 4. Templates become adaptation contracts

The three templates will tell an adopting AI to derive project-specific values from repository evidence and leave unsupported items unknown.

They will stay concise and will not include fictional sample project facts, installer instructions, fixed branch names, or mandatory commands that may not apply to the target repository.

### 5. Routing between Skills stays explicit

`project-governance/SKILL.md` will be strengthened as the normal-development entrypoint:

- use for establishing/repairing the control plane and running normal governed delivery;
- route semantic repository understanding to `domain-navigation`;
- route evidence-insufficient real incidents to `incident-doctor`;
- do not make Project Governance itself a codebase mapper, diagnostics platform, installer, or enforcement engine.

## Out of scope

Phase B must not:

- modify `skills/domain-navigation/` or `skills/incident-doctor/` content;
- add new Skill modules;
- add executable scripts/runtime/dependencies;
- add an installer, Bootstrap CLI, daemon, service, database, automatic enforcement/remediation, or MCP requirement;
- create a complex risk score or mandatory full-suite gate for every task;
- create project-specific facts in reusable templates;
- perform real-project adoption/validation yet; that remains a later validation phase.

## Expected verification

`V0` only:

- only the seven planned `project-governance` files plus root control handoff files may change;
- Skill frontmatter remains valid and trigger boundaries stay distinct;
- all relative links resolve;
- templates and references are internally consistent;
- `domain-navigation` and `incident-doctor` reusable contents are unchanged;
- no executable source or dependency manifest is introduced;
- branch is clean and local/remote matched at handoff.

## Success criteria

After Phase B, a fresh AI reading only the target repository plus `project-governance` should be able to answer, without inventing project facts:

- which of the three control files owns a given rule/state/task fact;
- when each control file should be updated;
- how to begin and finish a normal business/product task;
- when a scope change requires task re-authorization;
- when to use Domain Navigation versus Incident Doctor;
- which `V0`–`V3` verification depth is proportionate and why.

The guidance should reduce process ambiguity without making every task heavier.

## Current stop point

`WAITING_FOR_USER_DESIGN_REVIEW`

If the user approves this bounded design, Web will create the implementation authorization from the then-current exact `main` HEAD and issue a local AI execution card. No separate architectural spec or large implementation plan is required for this bounded enrichment.
