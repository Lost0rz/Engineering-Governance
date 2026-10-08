# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-08.

## Accepted Plugin v0.1.0 release

- GitHub Release `plugin-v0.1.0` is published from accepted payload HEAD `a29c3ecbc513e4db6fc9663c8b933b39bc088292`.
- Release asset: `engineering-governance-plugin.zip`.
- Release asset SHA-256: `c7de1b03f8471ae8cdf38fa35947167d5a1a3238850fd5b8432cd39fb1af36f0`.
- Plugin package version is still `0.1.0`.

## Accepted DN-001 corrective

- PR #7 merged after independent Web audit.
- Audited corrective head: `a177bcd20d68b4361876e234b008c3d851f1281e`.
- Accepted merge/main HEAD before this control transition: `b139811812f73d32927287a0bfbae2b5c6b93afa`.
- Domain Navigation now gates current-task routing on sufficiently verified task/control authority and preserves explicit bounded/historical snapshot navigation.
- `project-governance` and `incident-doctor` were unchanged by DN-001.

## New reusable governance finding

Two durable cross-project development principles are now accepted for addition to `project-governance`:

1. **Single canonical authority.** For each fact/state/policy/mapping/lifecycle/behavior class, establish one canonical authority/owner. Multiple consumers, adapters, projections, caches, or views may exist, but they must derive from or delegate to the canonical authority rather than maintain competing truth or parallel writers. Temporary migration coexistence must identify the primary authority, synchronization/cutover direction, and retirement boundary.
2. **Domain-coherent code structure and anti-redundancy.** Keep modules/files cohesive around a clear Domain/capability responsibility, avoid accidental duplicate behavior/authority, reuse semantics rather than merely similar syntax, and split when responsibilities or reasons-to-change diverge. File length is a signal, not a hard threshold. Do not perform opportunistic broad refactors outside the authorized task.

## Current task

- Task: `EG-PROJECT-GOVERNANCE-STRUCTURE-AUTHORITY-036`.
- State: `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.
- Mode: `REUSABLE_SKILL_ENHANCEMENT`.
- Scope is limited to `project-governance` reusable guidance plus control handoff.
- Task branch: `codex/project-governance-structure-authority-v1`, based on remote control head `3237d4f24f8f46657ba6e5fc859f10b50b2915a0`.
- The code-structure reference and minimal Skill/development-flow gates passed V0 scope/link/diff checks and all six focused contract scenarios.
- No Plugin version bump, tag, release, or business-repository mutation is authorized under this task.

## Next milestone

Independent Web audit of the pushed task branch. Do not merge, tag, release, or publish a new package under this task.
