# Engineering Governance

Modular AI engineering **Skills, methods, and proportional verification**—structured as a **3-tier lightweight routing pyramid** packaged as a standard, toggleable plugin. Project-specific source, runtime, and business constraints stay with each project.

## 3-Tier Lightweight Routing (7 Orthogonal Domains)

1. **L0 (Frontmatter trigger):** the host sees only Skill names and descriptions (`Do` + `Do not` boundaries) and enters **one** matching domain directly—no intermediate two-hop router.
2. **L1 (`SKILL.md` Fast Route, <=50 lines):** every `SKILL.md` routes straight to an inline fast path (**0 extra file reads** for routine tasks) or names a deep sub-mode.
3. **L2 (Single deep reference):** read at most one consolidated `references/*.md` file only when the deep sub-mode explicitly calls for it.

| Domain Skill | Primary ownership | Inline fast-path modes | Deep reference modes |
| --- | --- | --- | --- |
| [`engineering-workflow`](skills/engineering-workflow/SKILL.md) | G1/G2 coding, batching, handoffs, workspaces, PR delivery | `DIRECT_BUILD` | `DELEGATE_OR_HANDOFF`, `DELIVERY_OR_WORKSPACE` |
| [`ci-governance`](skills/ci-governance/SKILL.md) | Portable CI routing (`ci-router.py`), catalog hygiene, Actions | `SELECT_AND_RUN`, `VALIDATE_CATALOG` | `ONBOARD_OR_CONFIGURE` |
| [`ui-design`](skills/ui-design/SKILL.md) | UI/UX polish, audits, token flows, visual specs, review | `MICRO_POLISH`, `AUDIT_ONLY`, `FLOW_WITH_TOKENS` | `FULL_DESIGN_SYSTEM`, `FINAL_REVIEW` |
| [`architecture`](skills/architecture/SKILL.md) | SSOT state ownership, API contracts, concurrency, migrations | `BOUNDARY_DECISION` | `CONTRACT_OR_MIGRATION` |
| [`incident-doctor`](skills/incident-doctor/SKILL.md) | Evidence-gated diagnosis and minimal probes for blocking faults | `EVIDENCE_GATE` | `PROBE_AND_TECHNIQUES`, `INCIDENT_RECORD` |
| [`evidence-audit`](skills/evidence-audit/SKILL.md) | Collateral-first code review, `P0`–`P2` severity calibration (`SANDBOXED_APP`/`SERVICE`), PR/CI/release verdicts | `DIFF_OR_PR_AUDIT` | `DEEP_PROVENANCE_OR_CI_AUDIT` |
| [`codebase-context`](skills/codebase-context/SKILL.md) | Source/test route discovery (`LOCATE_ROUTE`), profiles, domain maps | `LOCATE_ROUTE` | `PROJECT_PROFILE`, `DOMAIN_MAP` |

## Risk & Verification Layering

- **Action risk (`G0`–`G3`):** `G0` read-only; `G1` localized recoverable fix; `G2` cross-module/contract edit (verify caller compatibility + `V2` integration); `G3` privilege, secrets, security trust, destructive data, or irreversible prod effects (pause for explicit owner confirmation).
- **Test cadence (`V0`–`V3`):** `ci-router.py` separates `draft` (deferred), `focused` (single lane), `milestone` (`V1`/`V2` fast feedback), `ready` (`V1`–`V3` with `supersedes` deduplication), and `release` (complete catalog).

## Standard Toggleable Plugin Installation

Build a deterministic, symlink-safe runtime archive or standalone directory with `python3 scripts/package-plugin.py` (packages `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `rules/AGENTS.md`, and `skills/**` without repo tests or `archive/**`):

- **Standardized setup & new Agent onboarding:** follow [`references/AGENT_INSTALLATION.md`](references/AGENT_INSTALLATION.md) for host-specific configurations, the 3-mode decision tree for onboarding any new Agent without re-running full benchmarks, project `AGENTS.md` threat-profile initialization, and the 30-second smoke check.
- **Antigravity:** place under `plugins/engineering-governance/` or declare in `plugins.json`; toggle via Settings UI or `agy plugin enable|disable engineering-governance`. Individual skills can also be mounted selectively via `skills.json` (`include_only`).
- **Codex / Claude Code:** install via `.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json`, or `.claude-plugin/plugin.json`.

Source commit, CI state, packaged artifact, and installed runtime remain distinct observable claims.
