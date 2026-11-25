---
name: codebase-context
description: >-
  Locate unclear domain ownership, canonical source, symbol, runtime entry, or
  test route in unfamiliar/multi-repo codebases (LOCATE_ROUTE), or create/audit
  compact derived PROJECT_PROFILE.md and DOMAIN_MAP.md indexes. Do not use when
  target files are already known, merely to read an existing profile, to track
  live task status, or to edit product code.
---

# Codebase Context

Orient quickly without creating shadow authorities or scanning entire repositories blindly.

## Fast route

| Need | Mode | Next reading |
| --- | --- | --- |
| Find unclear source, symbol, owner, runtime entry, or test route | `LOCATE_ROUTE` | **NONE (this file)** |
| Create, shrink, rebuild, or audit `PROJECT_PROFILE.md` | `PROJECT_PROFILE` | [profile-contract.md](references/profile-contract.md) + [PROJECT_PROFILE.md](assets/templates/PROJECT_PROFILE.md) |
| Create or incrementally refresh `DOMAIN_MAP.md` | `DOMAIN_MAP` | [domain-mapping.md](references/domain-mapping.md) |

## Inline progressive search escalation (`LOCATE_ROUTE`)

1. Use the lightest search that answers the question: direct path read -> targeted text/grep -> structural/AST pattern -> symbol/xref lookup -> runtime/config entry inspection.
2. Treat search hits, `PROJECT_PROFILE.md`, and `DOMAIN_MAP.md` as **leads only**; verify directly in canonical source/tests before returning the route.
3. Stop once the decision-relevant route and gaps are established; expand at most one dependency hop when needed.

## Boundaries

- Derived profiles and domain maps never outrank `AGENTS.md`, canonical source/schema, or host runtime truth.
- Consuming an existing `PROJECT_PROFILE.md` during a task does **not** invoke this Skill; writing a repository-managed profile requires active task/host write authorization.
- Never synthesize project facts solely from memory or prior chat summaries without source verification.
