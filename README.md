# Engineering-Governance Skills

Engineering-Governance is a source repository for reusable AI engineering-governance Skills, templates, routing/adoption contracts, operating rules, and reference material. An AI agent reads the relevant material, inspects a target project, and adapts what is useful to that project's verified facts.

## What this repository is

This repository provides three focused capabilities:

- **Project Governance** — the normal engineering entry, three-file control plane, normal task flow, workspace lifecycle, storage-affinity for durable project-controlled development state, risk-proportional verification, and lightweight non-blocking Follow-ups kept in current status for later task selection.
- **Domain Navigation** — conditional evidence-backed semantic routing from a task to the relevant authorities, code, symbols, tests, dependencies, and runtime evidence, reusing existing project maps when they already own domain meaning and refreshing only a verified affected routing claim when an accepted projection is wrong or stale.
- **Incident Doctor** — a reactive process for real blocking problems when existing evidence is insufficient.

It also provides a **global routing/adoption contract** that can be installed by an authorized AI agent into the user's authoritative global `AGENTS.md`. The managed routing block selects among the three Skills; it is not a fourth Skill and it does not duplicate their procedures.

The Skills are source material. A target project keeps ownership of its product, domain, data, and runtime truth. Templates describe structure and required semantics; they are adapted rather than copied blindly.

## What this repository is not

It is not a business product, governance runtime, installer executable, Bootstrap CLI, background service, central database, MCP server, or automatic enforcement/remediation system. It does not require an executable navigation helper and it does not automatically change a target project or the user's global files.

## AI-adapted use

1. Install/verify the Plugin payload and adopt or verify the managed global routing block when Engineering Governance is being installed for cross-project use. Installation is complete only when all three expected Skills are available **and** the authoritative global guidance has exactly one current managed routing block.
2. For software, repository, or project engineering work, enter through **Project Governance** unless a higher-priority instruction explicitly selects another route. Project Governance scales down for simple low-risk work; this default does not require extra plans, worktrees, broad scans, or broad validation.
3. Use **Domain Navigation** only when the responsible Domain/capability/authority/source/test/runtime route is unclear. If that focused work verifies that an existing accepted navigation projection is wrong, incomplete, or stale, refresh only the affected derived claim; do not churn correct routes or imply whole-map freshness.
4. Use **Incident Doctor** only when a real problem blocks safe progress and existing evidence is insufficient for the next safe decision.
5. Inspect the target repository's own controls, source, semantic authorities, and runtime evidence.
6. Select and adapt only the relevant guidance and templates, keeping unsupported project facts explicit as unknown.
7. During normal state-changing work, a small evidence-backed non-blocking adjacent issue may be kept concisely under `CURRENT_STATUS.md / Follow-ups`; it becomes executable only after explicit `CURRENT_TASK.md` scope authorization.
8. Keep project-controlled durable development assets on the storage authority containing the canonical project root by default, unless the project explicitly assigns a different authority for a specific durable asset. Machine/runtime state and ephemeral OS/tool scratch remain separate classes.
9. Verify the result at a level and cadence proportional to the actual change and closure boundary.

## Global routing adoption

The reusable Project Governance payload contains:

- `references/global-routing.md` — route-selection semantics;
- `references/adoption.md` — idempotent agent-mediated install/upgrade contract;
- `assets/templates/GLOBAL_AGENTS_ROUTING.md` — the exact marker-bounded global routing block.

Adoption verifies the three Skill identities, inspects the existing authoritative global file, inserts or replaces exactly one managed block, preserves unrelated rules, and stops rather than guessing when multiple/conflicting managed regions exist. Project-local `AGENTS.md` files remain repository-specific and do not receive a duplicate global routing block by default.

## Fixed principles

- **Three control files:** `AGENTS.md` holds durable project rules, `CURRENT_STATUS.md` records verified current state (including a small optional set of still-material non-blocking Follow-ups), and `CURRENT_TASK.md` defines the one active authorization. Status never authorizes repair.
- **Control identity:** provenance/transition parents, current control revisions, and explicit locked/execution heads are different semantic classes. Verify the relationship the task actually declares; do not treat every SHA as a current-head equality gate.
- **Domain navigation:** discover accepted business/product/domain/capability maps already present, regardless of filename, and route from the task through those authorities to focused source/symbol/test evidence. Add a separate navigation projection only when it provides durable routing value; it remains derived and does not replace product/domain truth. Correct routes do not churn; verified corrections update only affected routing evidence.
- **Project storage affinity:** resolve the canonical project root before choosing locations for project-controlled durable development state. Those durable assets follow the canonical project's storage authority by default; an explicit project-local asset/path rule overrides that default. Do not turn this into a universal host, volume, user-home, or machine rule.
- **Doctor on demand:** normal product work is the default. Investigate through Doctor only when current evidence cannot answer a blocking question safely; add the minimum useful probe.
- **Proportional verification:** `V0`–`V3` is the risk/scope dimension. Verification cadence is separate: focused construction checks, broader affected regression at corrective/task closure when justified, and exact integration/release evidence at the boundary whose claim it proves. Verification effort follows change risk, not change count.

## Maintainer notes

`docs/superpowers/` holds maintainer-only design and implementation planning history for this repository. It is not part of the reusable Skill material for target projects.
