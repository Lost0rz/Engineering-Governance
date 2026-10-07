# Upstream concepts

This repository records public work that informed its design. It borrows concepts, not vendored implementations.

## Agent Skills and Anthropic's skill creator

The [Agent Skills format](https://github.com/anthropics/skills) informs the one-`SKILL.md`-per-capability shape, optional references/assets/scripts, progressive disclosure, and trigger descriptions that help agents choose a Skill deliberately.

## AGENTS.md open format

The [AGENTS.md format](https://agents.md/) informs predictable repository-level guidance kept separate from human-facing project descriptions and current task state.

## GitHub `acquire-codebase-knowledge`

The [GitHub `awesome-copilot` skill](https://github.com/github/awesome-copilot/tree/main/skills/acquire-codebase-knowledge) informs evidence-first repository discovery: inspect intent and source, cite concrete paths for non-trivial claims, and leave unsupported details unknown.

## Aider Repo Map

[Aider's Repo Map](https://aider.chat/docs/repomap.html) informs optional dynamic context selection and ranking of useful files or symbols under limited context. It is a navigation aid, not the semantic authority represented by a project's Domain Map, and it is not a runtime dependency here.
