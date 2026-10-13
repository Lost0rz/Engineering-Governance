# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.5`.

- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- ChatGPT Web Plugin: `0.5.5`.
- Installed/local convergence baseline remains the accepted three-Skill `0.5.5` model until a later release/acceptance task changes distribution state.

## Active development — Capability Model v0.6.0

Task `EG-CAPABILITY-MODEL-V060-061` is active on branch `codex/capability-model-v0.6.0` from start Repository HEAD `3b8d99c3dba13ca01098abade5c6e696454ddd10`.

Objective: expand the reusable source capability model from three to seven top-level Skills while preserving the three-file project control plane and existing evidence-gated governance semantics.

Planned capability model:

- `project-governance`
- `solution-design`
- `execution-orchestrator`
- `agent-handoff`
- `evidence-audit`
- `domain-navigation`
- `incident-doctor`

The active durable design/research authority is `documents/engineering-governance-capability-model-v0.6.0.md`.

## External-reference audit direction

The current design uses external projects only as conceptual references, with no runtime dependency:

- Superpowers for fine-grained process-skill patterns, execution ledgers, explicit model selection, independent review, and failure modes; mandatory universal TDD/debugging/subagent behavior is not adopted.
- GitHub Spec Kit for conditional spec/plan/task/convergence structure and optional ambiguity/consistency quality gates.
- OpenAI Agents SDK and LangGraph supervisor patterns for separating manager/orchestrator behavior from explicit handoff behavior and controlling transferred context.
- OpenHands and SWE-agent for workspace/context isolation and small task-relevant context/tool surfaces.
- reviewdog, OpenSSF Scorecard, and SLSA for diff-bounded findings, evidence normalization, provenance/expected-identity verification, and PASS/FAIL/UNKNOWN-style evidence discipline.

## Accepted governance semantics preserved from v0.5.5

The v0.5.5 governance semantics remain accepted unless Task 061 explicitly supersedes a bounded capability/routing rule:

- durable planning-document linkage without a fourth control file;
- mandatory final Control Alignment Gate with conditional writes;
- `CONTROL_ONLY_DRIFT` and Delivery / Semantic HEAD separation;
- separate live repository-host gates;
- risk-proportional `V0`–`V3` verification;
- evidence-gated Incident Doctor entry;
- Project Governance as the normal project/repository authority/lifecycle entry.

## Distribution state

- Formal GitHub release: `0.5.5` — PASS.
- ChatGPT Web Plugin: `0.5.5` — PASS.
- Mac mini Codex: `0.5.5` — PASS.
- MacBook Air Codex: `0.5.5` — PASS.
- No v0.6.0 release or local Plugin acceptance has been performed yet.

## Active problems and blockers

No source blocker is currently known for Task 061.

The main design risk is ownership overlap: the four new Skills must remain narrow capabilities that return to Project Governance instead of creating competing task/control authorities.

## Next intended milestone

Complete the v0.6.0 source framework, final remote evidence audit, and PR-ready handoff. Local Plugin/runtime acceptance and any release publication are separate later milestones.
