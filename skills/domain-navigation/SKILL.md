---
name: domain-navigation
description: Use for evidence-backed Domain Map and repository navigation when a map is missing or stale, or an affected Domain, ownership, authority, code location, symbol, or test is unclear. Route from the authorized task to focused source evidence; do not authorize tasks, diagnose incidents, or modify product code.
---

# Domain Navigation

Use this Skill when the Domain Map is missing or stale for an affected Domain; when ownership, authority, or code location is unclear; when a task needs to be routed to relevant sources, symbols, or tests; or during repository onboarding bounded by a current task or a specific mapping goal. Treat every map as derived navigation evidence, not product truth, domain authority, or task authorization.

## Read the contracts

- [Domain model](references/domain-model.md)
- [Mapping workflow](references/mapping-workflow.md)
- [Evidence rules](references/evidence-rules.md)
- [Refresh policy](references/refresh-policy.md)
- [Repo Map boundary](references/repo-map.md)
- [DOMAIN_MAP.md template](assets/templates/DOMAIN_MAP.md)
- [DOMAIN.md template](assets/templates/DOMAIN.md)
- [Optional script boundary](scripts/README.md)

## Route from task to source

Follow the smallest useful route:

`CURRENT_TASK -> affected Domain(s) -> DOMAIN_MAP -> candidate authorities / entry points / symbols / tests -> optional targeted search or Repo Map -> focused source reading -> confirmed route + unresolved gaps`

If the map is absent or insufficient, inspect only the evidence needed for the current task and map target. Keep confirmed routes distinct from unresolved ownership or source gaps. Use an optional Repo Map only to select candidate material; direct source reading remains the verification step.

This Skill does not authorize tasks, decide product/business questions, diagnose incidents, mutate product code, or provide an installer, runtime, or indexing platform.
