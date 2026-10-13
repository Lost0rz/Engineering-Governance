# Skill Engineering quality contract

This repository-maintainer contract governs how Engineering Governance Skills are added or changed. It is not a top-level Skill and must not appear as an eighth route.

## Distinct capability test

A top-level Skill is justified only when it has all of:

1. a repeatable engineering capability;
2. a distinct trigger that materially changes what the agent should do;
3. one primary ownership boundary not already owned by another Skill;
4. a clear output/return contract;
5. negative trigger guidance that prevents routine overuse.

A topic, checklist or reference section alone does not justify a Skill.

## Description contract

Frontmatter `description` should primarily answer **when to use this Skill**. Do not put the full workflow in the description; detailed procedure belongs in the body/references so the agent cannot shortcut the Skill from metadata alone.

## Progressive disclosure

Keep frequently loaded `SKILL.md` files focused on trigger, authority boundary, core workflow and supporting references. Put detailed matrices, templates, examples and edge cases under `references/` or `assets/`.

## Composition contract

A Skill may call another Skill only for a bounded dependency. It must preserve task/control authority and return to its caller after the narrower capability finishes. Do not create recursive peer meshes or multiple implicit controllers.

## Route-quality scenarios

Every materially changed routing/trigger contract should define both:

- positive scenarios where the Skill must apply;
- negative/near-miss scenarios where it must **not** apply.

Over-triggering is a defect. A Skill should not run merely because it is installed or because a keyword appears.

## Authority discipline

No Skill may create a hidden replacement for `AGENTS.md`, `CURRENT_STATUS.md`, `CURRENT_TASK.md`, accepted durable planning authority, product/domain truth or repository/runtime evidence sources.

Transport/evidence artifacts such as handoff cards, ledgers, audit reports or reviewer packages remain non-authoritative unless the target project's accepted authority explicitly promotes a durable record.

## Verification of Skill changes

During construction, use bounded static checks for names/frontmatter/references and obvious contradictions. For a multi-Skill architecture change, prefer freezing the complete architecture before expensive integrated installed-runtime acceptance when the active task explicitly defines that cadence. Final acceptance must exercise composition and negative/over-trigger scenarios, not only whether each Skill file can be loaded in isolation.
