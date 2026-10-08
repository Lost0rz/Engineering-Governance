---
name: domain-navigation
description: Use for evidence-backed domain and repository navigation when semantic routing is missing or stale, or an affected Domain/capability, ownership, authority, code location, symbol, or test is unclear. Route from the authorized task to focused source evidence; do not authorize tasks, diagnose incidents, or modify product code.
---

# Domain Navigation

Use this Skill when navigation for an affected Domain/capability is missing or stale; when ownership, authority, or code location is unclear; when a task needs to be routed to relevant sources, symbols, or tests; or during repository onboarding bounded by a current task or a specific mapping goal. Before assuming a navigation artifact is missing, discover any accepted business, product, domain, or capability authorities already present in the target repository, regardless of filename, and determine what semantic truth they own. Treat those authorities as sources to reference, not material to duplicate. Any separate `DOMAIN_MAP.md` created or refreshed by this Skill is only an optional derived navigation projection, not product truth, domain authority, or task authorization.

## Read the contracts

- [Domain model](references/domain-model.md)
- [Mapping workflow](references/mapping-workflow.md)
- [Evidence rules](references/evidence-rules.md)
- [Refresh policy](references/refresh-policy.md)
- [Repo Map boundary](references/repo-map.md)
- [DOMAIN_MAP.md template](assets/templates/DOMAIN_MAP.md)
- [DOMAIN.md template](assets/templates/DOMAIN.md)
- [Optional script boundary](scripts/README.md)

## Verify current-task authority before routing

Apply this gate when the requested route is for a current or active task. Before treating a task as current, identify the selected repository/checkout, read its applicable controls, and establish that the task authority is current enough for this routing decision from its declared authority and freshness basis. Use only the narrowest relevant revision, ref, or control-state evidence needed. If the project's controls designate a local task contract as authoritative and nothing material calls its applicability or freshness into question, do not require a repository-wide refresh or fetch of every remote.

A local control file's presence is not, by itself, proof that it remains current. Branch names, staged/unstaged/untracked files, local code shape, historical documents, chat context, and memory cannot identify or authorize the current task. They may reveal a mismatch or freshness concern, but they cannot fill an authority gap.

If the current task/control authority is unavailable, materially stale, contradictory, or materially unresolved for the requested route, return `STOP_CURRENT_TASK_NAVIGATION`, state the authority evidence and unresolved point, and hand the task back to Project Governance reconciliation. Stop before routing that guessed task to source files, symbols, or tests.

## Explicit bounded or historical navigation

When the user explicitly names a bounded target such as a commit, historical branch, file, or symbol and does not ask to treat it as the current task, navigate only that target. Clearly label the result `BOUNDED/HISTORICAL SNAPSHOT NAVIGATION`, identify the target revision or scope, and do not present it as current task authority or authorization. This path remains available when current-task authority is unresolved.

## Route from task to source

Follow the smallest useful route:

`verified CURRENT_TASK -> affected Domain(s) -> existing semantic authorities and/or navigation projection -> candidate authorities / entry points / symbols / tests -> optional targeted search or Repo Map -> focused source reading -> confirmed route + unresolved gaps`

If an existing semantic map already owns product/domain meaning, reference it and keep navigation-specific source/symbol/test routing derived and separate. If no current navigation projection exists, do not create a literal `DOMAIN_MAP.md` merely because the filename is absent; first route from the accepted authorities and focused evidence, then create or refresh a navigation projection only when it adds durable routing value. Keep confirmed routes distinct from unresolved ownership or source gaps. Use an optional Repo Map only to select candidate material; direct source reading remains the verification step.

This Skill does not authorize tasks, decide product/business questions, diagnose incidents, mutate product code, or provide an installer, runtime, or indexing platform.
