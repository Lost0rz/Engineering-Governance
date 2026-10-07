# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering-governance Skills, templates, operating rules, and reference material. An AI agent reads the relevant material, inspects a target project, and adapts what is useful to that project's verified facts.

## What this repository is

This repository provides three focused capabilities:

- **Project Governance** — the three-file control plane, normal task flow, and risk-proportional verification.
- **Domain Navigation** — evidence-backed semantic routing from a task to the relevant authorities, code, symbols, tests, and runtime evidence, reusing existing project maps when they already own domain meaning.
- **Incident Doctor** — a reactive process for real problems when existing evidence is insufficient.

The Skills are source material. A target project keeps ownership of its product, domain, data, and runtime truth. Templates describe structure and required semantics; they are adapted rather than copied blindly.

## What this repository is not

It is not a business product, governance runtime, package, background service, central database, or automatic enforcement system. It does not require an executable navigation helper or automatically change a target project.

## AI-adapted use

1. Read the Skill whose trigger matches the current need.
2. Inspect the target repository's own controls, source, semantic authorities, and runtime evidence.
3. Select and adapt only the relevant guidance and templates.
4. Keep unsupported project facts explicit as unknown, then verify the result at a level proportional to the change.

## Fixed principles

- **Three control files:** `AGENTS.md` holds durable rules, `CURRENT_STATUS.md` records verified current state, and `CURRENT_TASK.md` defines the one active authorization.
- **Domain navigation:** discover accepted business/product/domain/capability maps already present, regardless of filename, and route from the task through those authorities to focused source/symbol/test evidence. Add a separate navigation projection only when it provides durable routing value; it remains derived and does not replace product/domain truth.
- **Doctor on demand:** normal product work is the default. Investigate a real failure only when current evidence cannot answer the blocked question safely; add the minimum useful probe.
- **Proportional verification:** choose verification depth from the change's risk and scope. Documentation and layout work do not inherit unrelated historical test burdens.

## Maintainer notes

`docs/superpowers/` holds maintainer-only design and implementation planning history for this repository. It is not part of the reusable Skill material for target projects.
