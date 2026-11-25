# Engineering Governance

Modular AI engineering **Skills, methods, and proportional verification**—packaged as a standard, toggleable plugin rather than a mandatory approval chain. Project-specific source, runtime, and business constraints stay with each project.

## Direct-entry Skill routing

Start from the requested outcome and enter the matching specialist Skill directly when the domain is clear; use `project-governance` for general engineering tasks, portable CI routing, and delivery coordination. Do not load unused Skills as a checklist.

| Capability bundle / focus | Skill | Primary use |
| --- | --- | --- |
| **Core engineering & CI** | `project-governance` | General implementation, proportional verification, PR delivery, portable CI routing (`ci-router.py`) |
| **Specialist methods** | `design` | UI/UX, `MICRO_POLISH` tweaks, interface audits, specs, implementation, visual review |
| | `solution-design` | Ambiguous architecture, API contracts, data flow, and state ownership |
| | `incident-doctor` | Evidence-gated diagnosis and minimal probes for blocking failures |
| | `evidence-audit` | Formal read-only code, PR, CI, or release readiness verdicts |
| **Context & orchestration** | `domain-navigation` | Unclear source, symbol, dependency, runtime entry, or test owner |
| | `project-profile` | Create, shrink, rebuild, or audit a compact derived project index |
| | `execution-orchestrator` | Intra-session plan-to-execute handoffs, batching, and Sub Agent decomposition |
| | `agent-handoff` | Structured cross-context transfer when an Issue/PR link is insufficient |

Routing details: [global routing](skills/project-governance/references/global-routing.md).

## Task coordination and permissions

Work can start from an authenticated current user instruction or an optional Issue/PR plan. Issues, PR descriptions, and handoff cards provide **context**, not write credentials; the real execution host authenticates user intent and enforces tool/GitHub permissions.

- **G0–G2**: read-only inspection, localized fixes, and bounded multi-module changes proceed directly inside the task scope.
- **G3**: materially new privileges, credentials, security boundaries, destructive data changes, or irreversible production effects require an explicit owner decision.

## Verification and portable CI routing

[Verification tiers](skills/project-governance/references/verification-tiers.md) scale test depth (`V0`–`V3`) with impact. Draft iterations avoid heavy CI; targeted checks run during implementation, and broader checks run at integration or release boundaries.

Cross-repository CI uses the [shared router](skills/project-governance/references/ci-routing.md): `skills/project-governance/scripts/ci-router.py` paired with a reviewed `.github/ci-capabilities.json` and thin caller workflow per consumer repository. This repository itself uses `.github/ci-capabilities.json` and `.github/workflows/governance-contract-checks.yml` via `ci-router.py`.

## Standard plugin installation and toggling

Build a clean runtime plugin directory or Web preview archive with `python3 scripts/package-plugin.py` (packages `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `rules/AGENTS.md`, and `skills/**` without repository tests or historical `archive/**`).

- **Antigravity**: install or symlink into a standard `plugins/engineering-governance/` customization root (or declare in `plugins.json`); toggle anytime via the Settings UI or `agy plugin enable|disable engineering-governance`. You can also consume individual specialist folders under `skills/` à la carte via `skills.json` (`include_only`).
- **Codex / Claude Code**: install via `.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json`, or `.claude-plugin/plugin.json` and enable/disable through the host plugin controls.

See [adoption](skills/project-governance/references/adoption.md). Source commit, CI status, packaged artifact, and installed host behavior remain separate observable claims.
