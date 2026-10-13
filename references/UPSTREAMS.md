# Upstream concepts

This repository records public work that informed its design. These references describe conceptual influence; they are not hidden runtime dependencies or automatic authorities for target projects. v0.6.0 adapts concepts rather than copying external process text or code.

## Agent Skills and Anthropic skill patterns

The Agent Skills format and related skill-authoring guidance inform one-`SKILL.md`-per-capability structure, progressive disclosure, and trigger-focused descriptions.

## AGENTS.md open format

The AGENTS.md format informs predictable repository-level guidance kept separate from human-facing README content and live task/status state.

## GitHub Spec Kit — `github/spec-kit`

Spec Kit informs the conditional separation of intent/specification, technical planning, actionable tasks, implementation, and convergence. Engineering Governance adopts the idea that ambiguity/consistency gates should be added when needed, while rejecting a mandatory artifact chain for every small task and preserving `CURRENT_TASK.md` as the single execution authorization.

## Superpowers — `obra/superpowers`

Superpowers informs several v0.6.0 mechanisms: explicit separation of design/planning/execution/review concerns, narrow delegated task briefs, ephemeral execution ledgers for compaction/recovery, independent review, explicit model selection, and parallelism only for independent domains. Engineering Governance explicitly does **not** adopt universal mandatory brainstorming, universal TDD/delete-and-rewrite rules, all-bugs debugging entry, unconditional subagent-per-task dispatch, or silent/high-model inheritance.

## OpenAI Agents SDK — `openai/openai-agents-python`

The Agents SDK informs the distinction between manager/orchestrator patterns and explicit handoff patterns, including the idea that handoff context can be filtered/controlled. Engineering Governance uses this concept to separate `execution-orchestrator` from `agent-handoff`; project authority is still reread from project controls rather than transferred by a peer agent.

## LangGraph supervisor patterns — `langchain-ai/langgraph-supervisor-py` and LangGraph multi-agent guidance

LangGraph supervisor patterns inform centralized coordination and explicit context engineering. Engineering Governance adapts this as one controller/authority for overlapping work, parallel readers by default, and multiple writers only when write scopes/workspaces are proven disjoint.

## OpenHands

OpenHands informs separation between control surfaces, agent execution backends, conversations/workspaces, and context management. Engineering Governance applies this concept to Web/local execution separation and bounded cross-context handoffs without making the UI or handoff card the source of project truth.

## SWE-agent

SWE-agent's Agent-Computer Interface work informs the principle that small purpose-built context/tool surfaces can outperform raw full-file/full-repository dumps. Engineering Governance applies this to narrow handoff/subagent briefs and explicit representation of no-change/no-output results.

## reviewdog

reviewdog informs diff-bounded diagnostics and separation between findings and presentation/reporting surfaces. Evidence Audit distinguishes findings introduced/exposed by the audited change from unrelated repository observations.

## OpenSSF Scorecard

Scorecard informs explicit check criteria, evidence source/freshness, risk meaning, and inconclusive states. Engineering Governance preserves `UNKNOWN`/`UNVERIFIED` rather than converting missing evidence into false PASS/FAIL certainty.

## SLSA provenance and verifier

SLSA informs the distinction between provenance metadata and verification against expected repository/ref/producer/artifact identity. Evidence Audit applies this principle to CI/release/PR evidence identities while preserving separate live repository-host gates.

## GitHub `acquire-codebase-knowledge`

GitHub's `awesome-copilot` codebase-knowledge guidance informs evidence-first repository discovery: inspect intent/source, cite concrete paths for non-trivial claims, and leave unsupported details unknown.

## Aider Repo Map

Aider's Repo Map informs optional dynamic context selection and ranking of useful files/symbols under limited context. In this repository it remains a read-only candidate-selection aid; it does not decide semantic ownership/authority or replace direct source verification.
