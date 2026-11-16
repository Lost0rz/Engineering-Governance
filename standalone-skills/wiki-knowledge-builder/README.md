# Wiki Knowledge Builder — Standalone Skill v0.1

**Purpose:** from user-provided/authorized source material, select reusable knowledge and produce independently reviewable Markdown for subsequent Karpathy LLM Wiki ingestion. Source type affects access and citation, **not** the KEEP/HOLD/SKIP decision.

## Package contents

| Path | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent Skill entry point and bounded workflow |
| [references/decision-evidence.md](references/decision-evidence.md) | Value gating, access and claim verification rules |
| [references/output-contract.md](references/output-contract.md) | Canonical Knowledge Note v0.1 contract |
| [assets/knowledge-note.template.md](assets/knowledge-note.template.md) | Fillable Markdown source-note template |
| [references/acceptance-matrix.md](references/acceptance-matrix.md) | T1–T8 quality and negative-route checks |
| [adapters/chatgpt-web.md](adapters/chatgpt-web.md) | Self-contained prompt for a ChatGPT conversation without native Skill loading |
| [examples/value-over-source.example.md](examples/value-over-source.example.md) | Provisional design-decision note (not a test PASS) |
| [tests/test_structure.py](tests/test_structure.py) | Portable package-only structure/schema tests |
| [tests/requirements.txt](tests/requirements.txt) | Test-only YAML dependency, not an Agent runtime requirement |
| [assets/hold-outline.template.md](assets/hold-outline.template.md) | Non-ingestion HOLD outline |
| [references/source-manifest.md](references/source-manifest.md) | Source ZIP fingerprints and verifiable source provenance |

## Use

For Agent hosts with Skill support, install **this directory alone** in the host's supported standalone Skill location. Follow the host's documented discovery/install process; this repository does not activate Skills automatically. For ChatGPT web without native Skill loading, use the complete text in [adapters/chatgpt-web.md](adapters/chatgpt-web.md) as the project/conversation instruction, then supply the actual source material.

Example request: *“从我提供的资料中挑选值得长期沉淀的内容，先给 KEEP/HOLD/SKIP，输出最多 3 篇可复核的 Wiki 原始 Markdown。不要写入 Wiki。”*

The output is **not installed**, imported into Obsidian, tested with the Wiki parser, or synchronized merely because a note was generated. Put approved notes into an independently managed Knowledge Inbox; the user manually invokes Wiki ingestion. Do not place raw notes straight into plugin-generated `wiki/sources/`.

## Knowledge-to-Skill and HOLD outputs

A reusable method **actually observed succeeding once** can produce a KEEP note with optional `skill_candidate: true`, plus the conditions requiring repeatability testing. No executable Skill is automatically packaged. A HOLD produces a non-ingestion **待验证提纲**, not an empty or fabricated ready-to-import knowledge note.

## Independence boundary

This directory is intentionally **outside** root `skills/` and `references/`. The Governance preview workflow currently packages those two root trees; its `plugin.json` and marketplace manifest remain unchanged. A future change to the packaging workflow must preserve this exclusion. No Governance routing, Issue approval, local permission setting, model provider or release is required to use this Skill.

## Provenance and maturity

Derived from the three user-provided files dated **2026-11-16**: `wiki-knowledge-builder-v0.1-design.md`, `wiki-knowledge-builder-v0.1-chatgpt-prompt.md` and `wiki-knowledge-builder-v0.1-example.md`. The original concept was a ChatGPT prompt MVP, not a field-tested Agent Skill. This is a **packaging implementation**, not proof that T1–T8, host discovery or real LLM Wiki ingestion pass. Keep those acceptance states separate from static package checks.

Run package tests from an arbitrary independently copied Skill directory (the tests have no parent Governance dependency):

```sh
python3 -m pip install -r tests/requirements.txt
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Within the original source repository, additionally run `standalone-skills/tests` for packaging/CI isolation. GitHub Actions runs both Python 3.11 and 3.12. These checks **do not** prove model behavior or LLM Wiki ingestion.
