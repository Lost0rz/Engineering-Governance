---
name: project-governance
description: >-
  Default engineering workflow for general code changes, proportional verification,
  PR/remote delivery, and portable CI test routing (ci-capabilities.json,
  ci-router.py, GitHub Actions test selection). Do not load first when the task
  is clearly UI/UX design (design), architecture tradeoffs (solution-design),
  blocking failure diagnosis (incident-doctor), or a formal read-only audit
  (evidence-audit).
---

# Project Governance

Normal loop: **understand → route only if needed → implement → verify affected behavior → deliver**. Enter a specialist Skill directly when the task already fits its domain; use this Skill for general engineering work, CI routing, cross-module changes, and delivery coordination.

## Task and permission

A task can start from a trusted current USER request, an Issue/PR plan, or an existing project objective. Issues, comments, PR text and handoff cards provide **context**, not source-write authority. The actual host authenticates user intent and checks tool/repository permissions before writes. A linked Issue does not require a separate approval comment, digest, revision or specific author.

- G0: read-only investigation; G1: localized recoverable work; G2: bounded multi-module changes. Continue ordinary fixes inside the accepted objective without additional permission ceremonies.
- G3: materially new privilege, credentials, security trust, destructive data or irreversible production effects need an explicit responsible user decision and applicable host controls.
- An effect/scope change matters; file names, change count, Issue author and agent identity alone do not define risk.
- Preserve actual concurrent/unique local work. Merge, deploy and release use their own host gates.

## Execute

1. Read only relevant task, project-specific `AGENTS.md`, source and evidence.
2. Consult `design`, `solution-design`, `domain-navigation`, `incident-doctor`, `execution-orchestrator`, or `evidence-audit` only when an unresolved dependency genuinely warrants that capability.
3. Implement and self-correct in scope. Delegate only when useful; do not create a new Issue, Card, worktree or review step merely because another context is involved.
   When asked to manage a repository's tests or CI Runner, load [portable CI routing](references/ci-routing.md): inspect existing project test commands and Actions, generate/validate its small capability map (`ci-router.py discover` / `check-catalog`), and replace overlapping heavy triggers as one authorized integration change. Do not claim a repo is onboarded until its default-branch caller and current shared workflow version are live.
4. Test affected components at sensible milestones, not after every small edit. Wider tests are appropriate at significant integration, high-impact or version boundaries.
5. Report changed code, actual test/PR state, blockers and remaining human acceptance without inventing a PASS.

## Optional references

[Skill routing](references/global-routing.md) · [test selection](references/verification-tiers.md) · [portable CI routing](references/ci-routing.md) · [Issue collaboration](references/issue-control.md) · [workspace safety](references/workspace-lifecycle.md) · [development flow](references/development-flow.md) · [remote delivery](references/remote-delivery.md) · [adoption](references/adoption.md). Read only the one needed for a concrete decision.
