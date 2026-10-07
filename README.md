# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering-governance Skills, templates, operating rules, and reference material. An AI agent reads the relevant material, inspects a target project, and adapts what is useful to that project's verified facts.

## What this repository is

This repository provides three focused capabilities:

- **Project Governance** — the three-file control plane, normal task flow, and risk-proportional verification.
- **Domain Navigation** — a semantic Domain Map and evidence-backed routes from a task to relevant code and authority.
- **Incident Doctor** — a reactive process for real problems when existing evidence is insufficient.

The Skills are source material. A target project keeps ownership of its product, domain, data, and runtime truth. Templates describe structure and required semantics; they are adapted rather than copied blindly.

## What this repository is not

It is not a business product, governance runtime, package, background service, central database, or automatic enforcement system. It does not require an executable navigation helper or automatically change a target project.

## AI-adapted use

1. Read the Skill whose trigger matches the current need.
2. Inspect the target repository's own controls, source, and runtime evidence.
3. Select and adapt only the relevant guidance and templates.
4. Keep unsupported project facts explicit as unknown, then verify the result at a level proportional to the change.

## Fixed principles

- **Three control files:** `AGENTS.md` holds durable rules, `CURRENT_STATUS.md` records verified current state, and `CURRENT_TASK.md` defines the one active authorization.
- **Domain navigation:** use a stable semantic Domain Map to identify ownership, authority, entry points, dependencies, tests, and evidence before broad source reading.
- **Doctor on demand:** normal product work is the default. Investigate a real failure only when current evidence cannot answer the blocked question safely; add the minimum useful probe.
- **Proportional verification:** choose verification depth from the change's risk and scope. Documentation and layout work do not inherit unrelated historical test burdens.

## Maintainer notes

`docs/superpowers/` holds maintainer-only design and implementation planning history for this repository. It is not part of the reusable Skill material for target projects.
