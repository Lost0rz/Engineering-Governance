# CURRENT TASK — EG-V01 Tooling Design

Task ID: `EG-V01-TOOLING-DESIGN-002`

State: `WAITING_FOR_USER_SPEC_REVIEW`

Mode: `TOOLING_FOUNDATION_DESIGN`

## Objective

Produce a reviewable architecture spec for a minimal reusable Bootstrap / Doctor / Audit tooling layer around accepted `EngineeringGovernanceStandard` `0.1.0`, then stop for user review. This is design work only.

## Authority and baseline

- Repository: `Lost0rz/Engineering-Governance`.
- Live `origin/main` baseline and design-branch base: `ab0457c378563d33c6b67f8f81a83f9d10241008`.
- Canonical checkout: `/Users/ox_miles/Documents/Code/Engineering-Governance` on `codex/eg-v01-tooling-design`.
- The merged `codex/eg-v01-reference-synthesis` and superseded `governance/v0.1` branches were safely removed after the required local-work checks; the latter's historical SHA remains recorded in `CURRENT_STATUS.md`.
- Annotated `v0.1.0` exists locally/remotely and peels to `738627a0caad330d277f60cfdaff5f153593135e`.
- Accepted model: seven lifecycle layers, six cross-cutting axes, typed authority routing, standalone profiles, and separate result/freshness/exception/project-decision semantics.

## Design artifact and result

- Spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.
- Compares Skill-only, Executable-core-first, and Hybrid; recommends Hybrid with explicit trade-offs.
- Defines the shared in-process model, data flow, proposed layout, Bootstrap/Doctor/Audit contracts, read/write boundaries, STOP behavior, provenance, reports/exit semantics, validation strategy, versioning, smallest first slice, deferred scope, open questions, and adversarial self-review.
- Root `README.md` was verified and left unchanged: it describes seven layers, says the tools are planned/not implemented, and remains navigational.
- Draft PR #2 is `OPEN / DRAFT` against `main`: https://github.com/Lost0rz/Engineering-Governance/pull/2. It is not merged.

## Scope and non-goals

This task authorizes the written design and its control-plane handoff only. It does not authorize executable Bootstrap/Doctor/Audit, CLI/source code, dependency manifests, machine-readable schema implementation, MCP, daemon/background service, enforcement, automatic remediation/migration, pilot-repository changes, or an implementation plan. Do not merge the Draft PR.

## Validation

- Static review confirmed the required design sections, no TODO/TBD/FIXME placeholders, clean diff whitespace, and consistency with accepted v0.1 authority/evidence boundaries.
- No tests or runtime implementation were run; neither is part of this design-only task.

## Handoff

- The design branch and control-plane updates are pushed; verify local/remote HEAD equality and a clean worktree at handoff.
- Wait at `WAITING_FOR_USER_SPEC_REVIEW`. If the user requests spec changes, make only the requested design/control updates and resynchronize. Do not proceed to implementation until the spec has been reviewed and a separate implementation task authorizes it.
- Keep Draft PR #2 open and draft; do not merge it in this task.
