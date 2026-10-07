# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-07

## Repository identity

- Repository: `Lost0rz/Engineering-Governance`; default branch: `main`.
- Repository purpose is fixed: a reusable AI engineering-governance **Skill source repository**, not a governance runtime/product and not an installer.
- Stable tag `v0.1.0^{}` remains `738627a0caad330d277f60cfdaff5f153593135e`.
- Root `AGENTS.md` remains the durable repository rule set.

## Phase A — accepted and merged

Phase A Skill-repository restructuring passed independent Web audit and the control-only re-audit.

- Pre-merge `main`: `954593b82a666bebf677636ce4f3cf08c07ceddd`.
- Accepted Phase A head: `02dd645d06e8fa554e241887c1457f7b15e297b5`.
- `main` was fast-forwarded to that accepted head on 2026-10-07.
- Exactly three top-level Skills are live: `project-governance`, `domain-navigation`, and `incident-doctor`.
- The retired Python runtime/tests and obsolete governance/research live trees are no longer part of the active repository.
- No installer, executable governance runtime, daemon, service, database, enforcement engine, automatic remediation, or Repo Map program is part of Phase A.
- The historical `v0.1.0` tag was not moved.

The merged task branch `codex/skill-repository-skeleton-reset` and its local worktree are lifecycle-closeout artifacts only; they are not an active development authority after the merge.

## Active milestone — Phase B `project-governance` enrichment design

- Active task: `EG-PROJECT-GOVERNANCE-ENRICH-DESIGN-011`.
- State: `WAITING_FOR_USER_DESIGN_REVIEW`.
- Mode: `BOUNDED_DESIGN_REVIEW`.
- Phase B changes only the existing `skills/project-governance/` module after design approval.
- Goal: make the normal-development Skill operational enough for an AI to establish/repair the three-file control plane, keep product/business delivery primary, handle scope changes cleanly, and select verification depth proportionally to risk.
- No local implementation is authorized while the design remains under review.

## Phase B fixed boundaries

- Reuse the existing module structure; do not create a fourth Skill or new runtime/tooling surface.
- Keep `AGENTS.md`, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` responsibilities distinct and project-local.
- Keep Domain/architecture discovery routed to `domain-navigation`.
- Keep real evidence-insufficient failures routed to `incident-doctor`; routine work must not build diagnostics in parallel.
- Keep verification tiered `V0`–`V3`, choosing the lightest level that safely establishes the task.
- Templates must be adapted from verified target-project facts rather than copied as fabricated project truth.

## Verification policy for Phase B

Phase B is documentation/Skill-contract enrichment, so the expected verification level is `V0`: content boundaries, path/link/frontmatter integrity, scope consistency, and proof that unrelated Skills/runtime surfaces did not change.

## Next milestone

User review of the bounded Phase B design. After explicit approval, Web will capture the exact remote `main` baseline, authorize one task branch, and issue the local AI execution card. Independent Web audit remains required before merge.
