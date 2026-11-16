# Standalone Skills

Skills in this directory are **independent source packages**, hosted in the Engineering-Governance repository for convenience only.

They are not part of the Engineering Governance plugin. In particular, do not move them into the root `skills/` or `references/` trees: the existing Web preview builder collects those trees for the Governance plugin.

- [Wiki Knowledge Builder](wiki-knowledge-builder/README.md): evidence-aware, value-first knowledge-note production for subsequent LLM Wiki ingestion.

Each standalone package owns its instructions, references, examples and acceptance cases. Installing or publishing the Governance plugin does not install or enable these packages. Any standalone installation must be separately selected by the user and supported by the target host.

## Multi-package source testing

The standalone CI runner discovers every package directory under `standalone-skills/` that has a `SKILL.md`; any new package without `tests/test_*.py` cases **fails closed** rather than reporting green. A discovered suite must execute at least one unskipped test; zero discovered or all-skipped cases are explicitly BLOCKED. Per-package optional `tests/requirements.txt` installs test dependencies only during verification, not during Agent installation.

## Source CI routing

`standalone-skills/**` PR changes run the independent `standalone-skills-ci.yml` workflow. The Governance workflow ignores **standalone-only** changes but still runs for mixed changes. Repository-only isolation tests do not travel with independently installed packages. This does not add the new Skill to Governance's Web preview or installed plugin.
