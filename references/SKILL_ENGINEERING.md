# Skill Engineering quality contract

This repository-maintainer contract governs how Engineering Governance Skills are added or changed. It is not a top-level Skill and must not appear as an additional external route.

## Distinct capability test

A top-level Skill is justified only when it has all of:

1. a repeatable engineering capability;
2. a distinct semantic trigger that materially changes what the agent should do;
3. one primary ownership boundary not already owned by another Skill;
4. a clear output/return contract;
5. negative/near-miss guidance preventing routine overuse;
6. positive guidance strong enough to avoid material under-use.

A topic, checklist, template, or small rule fragment does not justify a separate Skill or a separate micro-reference file. Keep routine sub-modes inline in `SKILL.md` (`<= 50` lines total) and consolidate deep reference contracts into cohesive files (`>= 28` lines) so agents never pay multi-round file-read taxes for tiny rules.

## 3-Tier Lightweight Routing Pyramid

- **L0 (Frontmatter):** `name` and `description` must provide orthogonal positive triggers and explicit `Do not...` exclusions so hosts enter **one** matching domain directly without an intermediate router hop.
- **L1 (`SKILL.md` Fast Route):** begin with a `## Fast route` mode table where common modes require `NONE` extra reference reads.
- **L2 (`references/*.md`):** load at most one consolidated reference for the selected deep sub-mode. Never place nested `SKILL.md` files inside `references/`.

## Composition & authority discipline

- A Skill may consult another only for an unresolved cross-domain dependency, then resume. Do not create recursive peer meshes.
- Runtime orchestration, model selection, and actual write authorization remain host-owned (`AGENTS.md`, host permissions, explicit user delegation rules). Derived profiles (`PROJECT_PROFILE.md`), domain maps (`DOMAIN_MAP.md`), and handoff cards never grant credentials or override canonical source truth.

## Route-quality scenarios & verification

Every materially changed routing contract must remain consistent with [tests/routing_golden_cases.json](../tests/routing_golden_cases.json) and pass [tests/test_workflow_contracts.py](../tests/test_workflow_contracts.py) (frontmatter positive/negative checks, `SKILL.md` line budget, non-fragmented references, link integrity, and upstream license provenance).
