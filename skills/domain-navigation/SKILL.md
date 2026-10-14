---
name: domain-navigation
description: Use conditionally when semantic routing is missing or stale, or an affected Domain/capability, ownership, authority, code location, symbol, runtime entry, dependency, or relevant test is unclear. Usually invoked from governed work to establish a focused evidence-backed route; do not authorize tasks, diagnose incidents, or modify product code.
---

# Domain Navigation

Use only when the route from the current task/explicit target to the relevant semantic authority/source/test/runtime evidence is unclear or stale. Return the verified route or unresolved gap to the caller, normally Project Governance; when called by Incident Doctor, return to Doctor.

## Boundary

- Reuse accepted business/product/domain/capability authorities; do not duplicate their semantic truth.
- A separate Domain/navigation map is optional and derived, not task or product authority.
- Search/index/Repo Map results are leads; focused source/runtime evidence verifies the route.
- Do not authorize tasks, decide product intent, diagnose incidents, or mutate product code.

## Core route

1. establish the current-task authority or explicit bounded/historical target;
2. identify affected Domain/capability;
3. find accepted semantic authority/navigation projection;
4. identify the smallest candidate source/symbol/test/runtime set;
5. escalate search method only when the current method cannot answer the decision;
6. verify the route with focused evidence;
7. return confirmed route + unresolved gaps and stop when sufficient.

If an accepted derived navigation projection is verified stale and mutation is authorized, refresh only the affected claim; strict read-only work reports the correction candidate.

## Supporting contracts

Read only what the routing decision needs:

- `references/domain-model.md` — semantic ownership model;
- `references/mapping-workflow.md` — current-task/historical authority gate, focused search escalation and cross-repo route;
- `references/evidence-rules.md` — evidence/freshness rules;
- `references/refresh-policy.md` — incremental derived-map refresh;
- `references/repo-map.md` — optional Repo Map boundary;
- `assets/templates/DOMAIN_MAP.md` / `DOMAIN.md` — optional projection templates;
- `scripts/README.md` — optional script boundary.
