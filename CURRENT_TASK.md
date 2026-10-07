# CURRENT TASK — EG-V01 Tooling Design Corrective

Task ID: `EG-V01-TOOLING-DESIGN-002`

State: `WAITING_FOR_USER_SPEC_REVIEW`

Mode: `SPEC_CORRECTIVE_ONLY`

## Objective

Resolve only the three MAJOR findings from independent Web review in the written tooling design. Preserve the Hybrid recommendation and accepted v0.1 contract. Stop for spec re-review after synchronization.

## Authority

- Repository: `Lost0rz/Engineering-Governance`.
- Branch: `codex/eg-v01-tooling-design`.
- Corrective start head: `81ce94b0d7ebaac89beb4d6f8be28c9b7e5874a3`.
- PR #2: `OPEN / DRAFT / UNMERGED`; do not merge.
- Spec: `docs/superpowers/specs/2026-10-07-tooling-foundation-design.md`.

## Corrective findings and disposition

1. **Bootstrap preview/apply/idempotence:** the conceptual immutable Preview Plan binds target identity and comparison state, template/profile versions, candidate paths/actions, rendered content digests, and the named authorized human actor. Exact expected existing artifacts are `NO_CHANGE`; changed/different artifacts are `CONFLICT / STOP`, never overwritten. Apply recomputes and validates the exact approved plan; any drift stops and requires a new preview/approval. AI skills cannot approve apply.
2. **Evaluation unresolved vs command STOP:** reportable missing/stale/inaccessible evidence and unresolved same-class authority conflicts yield `UNVERIFIED` where applicable, `STALE`/`UNKNOWN` freshness, limitations, and a truthful report with exit `0`. Fatal/unsafe target, root-input, Bootstrap-write, or internal failures are command-level STOPs with nonzero codes. Evidence incompleteness is not an enforcement gate.
3. **Hybrid AI contribution flow:** the deterministic core emits an immutable identified base report; the AI skill consumes only its identified inputs and returns a linked `AIContribution`; the core validates links and composes an ephemeral view. The contribution cannot modify machine results, source evidence, the base report, or project decisions; there is no persistent AI store or AI self-acceptance path. HUMAN/HYBRID final judgment remains with the named human/project authority.

## Invariants and scope

- Preserve Hybrid recommendation, seven lifecycle layers, six axes, typed authority routing, standalone profiles, and `EngineeringGovernanceStandard 0.1.0`.
- Allowed changes: the design spec, `CURRENT_STATUS.md`, and `CURRENT_TASK.md` only.
- Do not write an implementation plan or implement Bootstrap/Doctor/Audit, CLI, dependencies, machine-readable schema, MCP, daemon, enforcement, auto-remediation/migration, or pilot-repository changes.
- Keep PR #2 Draft and unmerged.

## Validation and handoff

- Self-review the exact corrected text for all three findings, hidden writers, authority duplication, and scope expansion.
- Use static document/diff checks only; no runtime implementation or tests are part of this corrective.
- Commit and push the same task branch, verify local/remote HEAD equality and a clean worktree, and return to `WAITING_FOR_USER_SPEC_REVIEW`.
- Wait for re-review. Do not start implementation until the spec is accepted and a separate task authorizes it.
