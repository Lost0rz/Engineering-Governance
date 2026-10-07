# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose is fixed: a reusable AI engineering-governance **Skill source repository**, not a governance runtime/product and not an installer.
- Stable tag `v0.1.0^{}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Root `AGENTS.md` remains the durable repository rule set.

## Phase A — accepted and merged

Phase A Skill-repository restructuring passed independent Web audit and control re-audit and was fast-forwarded into `main` at accepted head `02dd645d06e8fa554e241887c1457f7b15e297b5`.

The live repository contains exactly three top-level Skills: `project-governance`, `domain-navigation`, and `incident-doctor`. The retired Python runtime/tests and obsolete governance/research live trees are no longer active repository content. No installer, executable governance runtime, daemon, service, database, enforcement engine, automatic remediation, or Repo Map program is part of the accepted Phase A baseline.

## Active milestone — Phase B `project-governance` enrichment implementation

- Active task: `EG-PROJECT-GOVERNANCE-ENRICH-IMPL-012`.
- State: `AUTHORIZED_FOR_LOCAL_EXECUTION`.
- Mode: `BOUNDED_IMPLEMENTATION`.
- Authorized branch: `codex/project-governance-enrichment`.
- User-approved bounded design baseline: `88c070596b52f465194c37903921efef76c63350`.
- Scope is limited to enriching the seven existing files under `skills/project-governance/` plus root control-plane handoff updates.
- Independent Web audit is required before merge.

## Phase B accepted design direction

The existing `project-governance` Skill will be strengthened so a fresh AI can:

- distinguish durable rules, verified current state, and the one active task across `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md`;
- know when each control changes and avoid duplicating fact ownership across controls;
- run normal development as business/product-first work rather than a parallel governance program;
- treat material objective/scope changes as re-authorization while ordinary evidence discovery remains part of the same task;
- route code/authority discovery to `domain-navigation` only when needed;
- route real evidence-insufficient failures to `incident-doctor` only when needed;
- choose `V0`–`V3` proportionally to change radius and risk, without a numeric scoring bureaucracy;
- adapt templates from verified target-project evidence and leave unsupported facts unknown.

## Phase B boundaries

- No fourth Skill or new module.
- No changes to reusable `domain-navigation` or `incident-doctor` content.
- No executable script/runtime/dependency.
- No installer, Bootstrap CLI, daemon, service, database, automatic enforcement/remediation, or MCP requirement.
- No complex risk score and no mandatory full-suite test burden for every task.
- No fictional project facts in reusable templates.
- No real-project adoption example yet; validation remains a later phase.

## Verification policy

Phase B is `V0` documentation/Skill-contract enrichment:

- only the seven planned `project-governance` reusable files plus root handoff controls may change;
- Skill frontmatter and relative links must remain valid;
- templates/references must be internally consistent;
- `domain-navigation` and `incident-doctor` reusable content must remain unchanged;
- no executable source or dependency manifest may be introduced;
- final task branch must be clean and local/remote matched.

## Next milestone

Local execution on the authorized Phase B branch, then independent Web audit of the pushed task branch. No merge is authorized to the local executor.
