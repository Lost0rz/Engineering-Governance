# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07 — Phase F completed the second real-project read-only validation. The user approved Phase G as one bounded cross-project corrective covering exactly two evidence-backed clarifications; reusable Skill implementation is now authorized under a separate task.

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose remains a reusable AI engineering-governance Skill source repository, not a governance runtime/product and not an installer.
- Stable historical tag `v0.1.0^{}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Accepted reusable Skill revision validated by Phase E and Phase F remains Phase D merge head `ed9cab436f482648288d8fd50553e629f7a1c5a2` until Phase G is independently audited and accepted.
- Exactly three reusable Skills remain live: `project-governance`, `domain-navigation`, and `incident-doctor`.

## Accepted merged baseline

- Phase A Skill-source restructuring: accepted and merged.
- Phase B `project-governance`: accepted and merged at `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- Phase C `domain-navigation`: accepted and merged at `1d28250717e4e72754655ccc3c69bc3664a70eae`.
- Phase D `incident-doctor`: accepted and merged at `ed9cab436f482648288d8fd50553e629f7a1c5a2`.
- Phase E RemoteOrbit read-only validation: complete / PASS.
- Phase F InvestDesk read-only validation: complete / PASS.

## Cross-project evidence now accepted for corrective work

Two materially different projects support exactly two bounded reusable clarifications:

1. **Task contract versus current status.** `CURRENT_STATUS.md` may summarize verified current facts, but a status change must not silently change a task-owned prerequisite, acceptance criterion, STOP condition, allowed side effect, or authorization boundary. When a newly verified fact changes one of those task-owned conditions, `CURRENT_TASK.md` must be reconciled and re-authorized before state-changing work continues.
2. **Navigation projection versus existing semantic maps.** A target repository may already have authoritative business, product, domain, or capability maps under another name. Domain Navigation must discover and reference those authorities first; it must not assume that a new file literally named `DOMAIN_MAP.md` is required or duplicate accepted semantic truth.

No Phase G corrective is justified for `incident-doctor`; its positive trigger in RemoteOrbit and non-trigger in InvestDesk both behaved as intended.

## Active milestone — Phase G bounded cross-project corrective

- Active task: `EG-CROSS-PROJECT-CORRECTIVE-020`.
- State: `AUTHORIZED_FOR_IMPLEMENTATION`.
- Mode: `BOUNDED_CORRECTIVE_IMPLEMENTATION`.
- Design baseline: `9346997c75d3b5dce8a558203b3adb1a40eb5fc3`.
- Planned implementation branch: `codex/cross-project-corrective` from the Phase G authorization commit.
- Reusable scope is limited to three `project-governance` files and four `domain-navigation` files named in `CURRENT_TASK.md`, plus root control handoff files.
- `incident-doctor`, target projects, executable helpers, dependencies, runtime systems, indexes, databases, daemons, Repo Map programs, and new Skills are out of scope.

## Verification expectation

Phase G is documentation/Skill-contract corrective work and uses `V0` verification: exact changed-path allowlist, frontmatter/link consistency, template/reference consistency, exactly three Skills, sibling Skill unchanged, no executable/dependency additions, stable tag unchanged, clean branch state, and local/remote branch head match where applicable.

## Next milestone

Implement the two approved clarifications on the bounded task branch, stop at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`, and independently audit the exact branch diff before any merge to `main`.
