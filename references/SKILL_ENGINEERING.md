# Skill Engineering quality contract

This repository-maintainer contract governs how Engineering Governance Skills are added or changed. It is not a top-level Skill and must not appear as a ninth route.

## Distinct capability test

A top-level Skill is justified only when it has all of:

1. a repeatable engineering capability;
2. a distinct semantic trigger that materially changes what the agent should do;
3. one primary ownership boundary not already owned by another Skill;
4. a clear output/return contract;
5. negative/near-miss guidance preventing routine overuse;
6. positive guidance strong enough to avoid material under-use.

A topic, checklist, template or reference section alone does not justify a Skill.

`project-profile` qualifies because its requested output is a compact derived context/index produced by classification across project authorities; it neither owns normal engineering execution nor duplicates Domain Navigation.

## Description / progressive disclosure

Frontmatter primarily answers **when to use this Skill**. Keep `SKILL.md` focused on trigger, authority boundary, core workflow and supporting references. Put detailed matrices/templates/examples under `references/` or `assets/`.

## Composition

A Skill may call another only for a bounded dependency. Preserve project task/control authority and return to the caller. Do not create recursive peer meshes or multiple implicit controllers.

Task purpose and execution context remain separate. Runtime configuration remains environment-owned unless accepted project authority explicitly makes it portable.

## Route-quality scenarios

Every materially changed trigger/routing contract defines positive scenarios and negative/near-miss scenarios. Over-triggering is a defect. Materially suppressing safe useful capability can also be a defect.

Project Profile must not trigger merely because a project exists; normal development still enters Project Governance. Domain Navigation must not be replaced by a summary Profile.

## Authority discipline

No Skill may create a hidden replacement for project `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, accepted product/domain/data/runtime truth or durable planning authority.

Derived Profile/Domain projections and transport/evidence artifacts remain non-authoritative. Environment-specific runtime observations remain evidence about that environment, not reusable Plugin defaults.

## Verification of Skill changes

During construction use bounded static checks for names/frontmatter/references/contradictions. For multi-Skill architecture work, freeze the full source architecture before expensive installed/runtime acceptance when the task defines that cadence.

Final acceptance exercises positive/negative routing, cross-Skill composition, authority preservation, task-vs-context separation, environment configuration isolation, and any new artifact/transport lifecycle semantics. Do not prove only that each Skill file loads independently.
