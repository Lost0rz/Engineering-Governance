# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal release remains `plugin-v0.5.5`; accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No v0.6.0 release or installed Plugin/Web/Codex integrated acceptance has run yet.

## v0.6.0 architecture — FROZEN FOR CONSOLIDATED ACCEPTANCE

Task `EG-CAPABILITY-ROUTING-ENVIRONMENT-HARDENING-066` is complete.

- Frozen Architecture Delivery / Semantic HEAD: `f3d47b00cac41ebd19408cef18563c91be67ae53`.
- Prior Task 065 freeze `b7fb0051b8c51b5c846a507fad9037518dcf18db` is superseded for final v0.6.0 acceptance.
- PR #26 remains OPEN / DRAFT / UNMERGED; source audit observed `mergeable=true`, `mergeable_state=clean`.
- Semantic head commit statuses: none reported; **CI PASS is not claimed**.
- Installed integrated acceptance: `NOT_RUN_BY_DESIGN`.

## Accepted architecture

- Exactly seven top-level Skills; no Router Skill.
- Routing surfaces are environment-neutral: explicit selection, Skill metadata/platform discovery, project guidance, and authoritative global guidance where supported.
- Portable workflow lives in Skills/references; root `AGENTS.md` is source-repository maintenance guidance.
- `ENVIRONMENT_DEFAULT_ONLY` remains active for delegated models; stronger-model escalation remains disabled.
- Environment-specific model/reasoning, parallel capacity, delegation limits, material tools, workspace/runtime constraints are resolved from the current environment only when decision-relevant.
- Same-purpose work can cross Web/local/session/machine/Sub Agent contexts without changing task purpose.
- Cross-repository work keeps per-repository control/write authority; a primary task does not automatically authorize another repository.
- Evidence Audit routes on requested verdict/outcome, not CI/PR keywords.
- `DIAGNOSE` handoff is read-only; state-changing diagnostic probes use `EXECUTE` + `PURPOSE: DIAGNOSTIC_PROBE`.
- Solution Design and Incident Doctor retain lightweight reversibility/probe-safety rules only when material.
- No-op control reconciliation means no write/commit.

## Task 066 source audit

`V2 remote source-architecture audit: PASS` for semantic head `f3d47b00cac41ebd19408cef18563c91be67ae53`.

Verified: only governance/Skill/design/acceptance Markdown/control changes; Plugin version remains `0.6.0`; no runtime/daemon/database/workflow/model-router/automatic enforcement was added; exact seven-Skill directory set remains.

## Next milestone

Run one consolidated v0.6.0 installed Plugin/Web/Codex acceptance using `references/V060_INTEGRATED_ACCEPTANCE.md`. Do not split it into one Skill at a time and do not patch reusable source inside installed Plugin caches.
