# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07 — Phase C was independently audited and fast-forward merged to `main`; the existing Incident Doctor module was then read from the merged baseline for the next bounded design review.

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose remains a reusable AI engineering-governance **Skill source repository**, not a governance runtime/product and not an installer.
- Stable historical tag `v0.1.0^{}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Root `AGENTS.md` remains the durable repository rule set.

## Accepted merged baseline

- Phase A Skill-source restructuring: accepted and merged.
- Phase B `project-governance` enrichment: accepted and merged at `3b10169a475d97ed8b79ab7d5fa30df5fbdd6f04`.
- Phase C `domain-navigation` enrichment: accepted and merged at `1d28250717e4e72754655ccc3c69bc3664a70eae`.
- Exactly three reusable Skills remain live: `project-governance`, `domain-navigation`, and `incident-doctor`.

Accepted navigation behavior now treats Domains as evidence-backed semantic capability/ownership/state/authority boundaries; routes tasks to the smallest useful source-reading set; keeps Domain Map distinct from any optional Repo Map; preserves unknown/stale/conflicting claims; refreshes incrementally; and requires no executable navigation helper.

## Active milestone — Phase D `incident-doctor` bounded design review

- Active task: `EG-INCIDENT-DOCTOR-ENRICH-DESIGN-015`.
- State: `WAITING_FOR_USER_DESIGN_REVIEW`.
- Mode: `BOUNDED_DESIGN_REVIEW`.
- The next candidate change is enrichment of the existing `skills/incident-doctor/` module only.
- No local Phase D implementation is authorized before explicit user approval of the bounded design.

## Phase D fixed boundaries

- Incident Doctor remains reactive, not part of normal feature development.
- Existing evidence must be evaluated before any new probe is added.
- If evidence is already sufficient for the next safe decision, new probe work is bypassed.
- Diagnosis must preserve the distinction between user report, direct observation, interpretation, hypothesis, finding, and root-cause claim.
- Any probe must be the minimum evidence needed for the blocked question and must not silently change product behavior.
- Fresh incident capture must preserve runtime/build/configuration identity and the relevant observation window.
- Temporary probes are retired by default; durable promotion requires separate evidence, ownership, and authorization.
- No automated repair, broad observability platform, background monitor, daemon, database, or permanent diagnostic expansion is implied.

## Next milestone

User review of the bounded Phase D Incident Doctor design in chat. After explicit approval, Web will capture the then-current exact `main` baseline, authorize one implementation branch, and issue the local AI execution card.
