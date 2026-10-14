# Upstream concepts and bundled source

This repository records public work that informed its design. Most references below describe conceptual influence rather than runtime dependencies or automatic authorities for target projects. When upstream source is intentionally bundled or adapted into distributed Skill references, that exception is identified explicitly with local provenance/license files.

## Anthropic `frontend-design`

The v0.6.8 `design` capability intentionally bundles Anthropic's `frontend-design` Skill as its active design-reasoning source module. The imported Skill body is preserved under `skills/design/references/anthropic/frontend-design.md`; source identity and modification status are recorded in `skills/design/references/anthropic/PROVENANCE.md`, and Apache License 2.0 terms are bundled alongside it.

This is source material inside the routed `design` capability, not a hidden runtime dependency and not a separately installed Plugin.

## `satnaing/shadcn-admin`

Engineering Governance v0.7.0 uses `satnaing/shadcn-admin` as an upstream reference for admin/back-office page-pattern composition. The local `skills/design/references/shadcn-admin/admin-patterns.md` is a new concise synthesis informed by the upstream project's reusable dashboard/admin structure, responsive/accessibility focus and representative feature families such as dashboard, settings, tasks and users.

The upstream React/TypeScript application is not vendored and its Shadcn visual defaults are not target-project authority. The target project's actual workflow, component library, tokens and brand remain authoritative. MIT provenance/license records are kept adjacent to the local adapted module.

## `VoltAgent/awesome-design-md`

Engineering Governance v0.7.0 uses `VoltAgent/awesome-design-md` as an upstream reference for converting design decisions into plain-text visual-system guidance suitable for coding/design agents. The local `skills/design/references/awesome-design-md/design-spec-synthesis.md` adapts the useful DESIGN.md structure into an authority-safe synthesis workflow covering visual character, semantic color roles, typography, layout/spacing, surfaces, components/states, responsive rules, Do/Don't constraints and implementation guidance.

Upstream brand DESIGN.md files, extracted brand tokens, previews and assets are not vendored. External brands remain optional inspiration; the target project's design authority wins. MIT provenance/license records are kept adjacent to the local adapted module.

## Microsoft `frontend-design-review`

Engineering Governance v0.7.0 adapts the Design Review function of `microsoft/skills` `.github/skills/frontend-design-review/` as the final internal review layer under `design`. The local `skills/design/references/microsoft/final-review.md` uses the upstream review concepts of user-task focus, design-system compliance where evidence exists, Frictionless / Quality Craft / Trustworthy pillars, severity-prioritized findings and corrective re-review.

Microsoft's Creative Frontend Design mode is intentionally not used as a competing downstream aesthetic-direction stage because Anthropic already owns upstream design reasoning in this capability. Figma/Storybook/token assumptions are evidence-conditional and may never be fabricated. MIT provenance/license records are kept adjacent to the local adapted module.

## Agent Skills and Anthropic skill patterns

The Agent Skills format and related skill-authoring guidance inform one-`SKILL.md`-per-capability structure, progressive disclosure, and trigger-focused descriptions.

## AGENTS.md open format

The AGENTS.md format informs predictable repository-level guidance kept separate from human-facing README content and live task/status state.

## GitHub Spec Kit — `github/spec-kit`

Spec Kit informs the conditional separation of intent/specification, technical planning, actionable tasks, implementation, and convergence. Engineering Governance adopts the idea that ambiguity/consistency gates should be added when needed, while rejecting a mandatory artifact chain for every small task and preserving `CURRENT_TASK.md` as the single execution authorization.

## Superpowers — `obra/superpowers`

Superpowers informs several v0.6.0 mechanisms: explicit separation of design/planning/execution/review concerns, narrow delegated task briefs, ephemeral execution ledgers for compaction/recovery, independent review, explicit model selection, and parallelism for genuinely independent work. Engineering Governance explicitly does **not** adopt universal mandatory brainstorming, universal TDD/delete-and-rewrite rules, all-bugs debugging entry, unconditional subagent-per-task dispatch, or silent/high-model inheritance.

## OpenAI Agents SDK — `openai/openai-agents-python`

The Agents SDK informs the distinction between manager/orchestrator patterns and explicit handoff patterns, including the idea that handoff context can be filtered/controlled. Engineering Governance uses this concept to separate `execution-orchestrator` from `agent-handoff`; project authority is still reread from project controls rather than transferred by a peer agent.

## Microsoft Agent Framework

Microsoft Agent Framework informs explicit workflow/orchestration patterns such as sequential, concurrent and handoff-driven multi-agent execution. Engineering Governance adapts the positive idea that safe concurrency is useful execution capacity while keeping project/task authority outside the agent workflow itself.

## LangGraph supervisor patterns — `langchain-ai/langgraph-supervisor-py` and LangGraph multi-agent guidance

LangGraph supervisor patterns inform centralized coordination and explicit context engineering. Engineering Governance adapts this as one controller/authority for overlapping work, active use of independent parallel units when useful, and multiple writers only when write scopes/workspaces are proven disjoint.

## OpenHands

OpenHands informs separation between control surfaces, agent execution backends, conversations/workspaces, and context management. Engineering Governance applies this concept to context-neutral cross-session/machine/agent handoffs without making a UI, local machine, Web surface, or handoff card the source of task truth.

## SWE-agent and mini-SWE-agent

SWE-agent's Agent-Computer Interface work informs the principle that small purpose-built context/tool surfaces can outperform raw full-file/full-repository dumps. mini-SWE-agent reinforces the complementary lesson that orchestration complexity is not itself value: use one executor when sufficient, but add parallel/delegated units deliberately when they provide real throughput/context benefit.

## Kubernetes Enhancement Proposals (KEPs)

Kubernetes KEP practices inform the distinction between durable design decisions, implementation/readiness stages, test/acceptance expectations, compatibility and rollback considerations. Engineering Governance adopts the lifecycle/decision-separation concept without requiring KEP-style ceremony for ordinary work.

## Backstage ownership/catalog patterns

Backstage's ownership/catalog model reinforces the distinction between descriptive metadata and ultimate ownership/authority. Engineering Governance adapts this as one owning task/control authority even when many agents, repositories, or execution contexts participate.

## reviewdog

reviewdog informs diff-bounded diagnostics and separation between findings and presentation/reporting surfaces. Evidence Audit distinguishes findings introduced/exposed by the audited change from unrelated repository observations.

## OpenSSF Scorecard

Scorecard informs explicit check criteria, evidence source/freshness, risk meaning, and inconclusive states. Engineering Governance preserves `UNKNOWN`/`UNVERIFIED` rather than converting missing evidence into false PASS/FAIL certainty, and now also records required-claim coverage for material audits.

## SLSA provenance and verifier

SLSA informs the distinction between provenance metadata and verification against expected repository/ref/producer/artifact identity. Evidence Audit applies this principle to CI/release/PR evidence identities while preserving separate live repository-host gates.

## GitHub `acquire-codebase-knowledge`

GitHub's `awesome-copilot` codebase-knowledge guidance informs evidence-first repository discovery: inspect intent/source, cite concrete paths for non-trivial claims, and leave unsupported details unknown.

## Aider Repo Map

Aider's Repo Map informs optional dynamic context selection and ranking of useful files/symbols under limited context. In this repository it remains a read-only candidate-selection aid; it does not decide semantic ownership/authority or replace direct source verification.
