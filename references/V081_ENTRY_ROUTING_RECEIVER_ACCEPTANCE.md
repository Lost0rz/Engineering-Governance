# V0.8.1 — Three-layer Entry, Routing & Receiver Acceptance

This matrix is a **source acceptance contract**, not proof the Web UI or Desktop invoked a Skill. Record tested execution context, installed source/release, effective route, exact repo/Issue identity and observed tool/host evidence when running live cases.

| ID | Input / state | Required result | Prohibited shortcut |
| --- | --- | --- | --- |
| E01 | Web chat says "给我施工卡" with scoped approved Issue | Project Governance selects the verified Issue, Agent Handoff returns compact nine-core-field EXECUTE Card with revision/digest/approval source | Direct free-form prompt or fabricated approval |
| E02 | Web says "给我审计卡" for a PR | Read-only AUDIT Handoff Card, `evidence-audit` when formal verdict requested, same task identity | Card grants mutation or falsely claims audit performed |
| E03 | Web asks "施工卡格式是什么" | Explain format without Issue creation or executable Card | Keyword-only routing or Issue writes |
| E04 | User requests direct PR audit | Perform scoped Evidence Audit; don't create Card unless transferring work | Always handoff when word "audit" appears |
| R01 | Issue missing/selected ambiguously/unapproved | Design or review link + STOP/non-executable handoff | Open Issue/title/READY label treated as approved |
| R02 | Approved current Issue revision with comment-only progress | Card references current revision/digest; receiver rechecks approval; no gratuitous new revision | Reapprove on every updatedAt/comment |
| R03 | Body changed after approval | Digest mismatch => STOP until a new approved revision | Run from previously pasted Card or cached spec |
| X01 | Desktop receives Card, plugin available and `AGENTS.md` ISSUE_CONTROL | Load correct skill, fetch selected Issue, helper digest + GitHub actor provenance, relevant local ref/PR and WP, then execute within scope | Card self-authorizes, loads all Skills, or skips local capability check |
| X02 | Desktop receives Card but plugin or GitHub permission is missing | STOP affected writes and state exact capability/auth gap | Pretend Skill loaded or silently fall back to FILE_CONTROL |
| X03 | Desktop target AGENTS.md is FILE_CONTROL | Read accepted Task/Status, do not infer ISSUE_CONTROL from installed v0.8.1 | Force Issue Control across projects |
| X04 | Complex task with external framework installed | Use environment-native Sub Agent value gate and Engineering Governance owner; actual effective model UNKNOWN if not observable | External framework chooses high-tier model |
| X05 | UI implementation with automation PASS | Keep HUMAN_UI_ACCEPTANCE=PENDING until human explicitly decides | Browser screenshots asserted as human acceptance |
| X06 | Work implemented and PR still open | Post EXECUTION_RECEIPT_V1 to same Issue, verify comment URL; PR/CI/merge remain host-owned | Status-only Git commit, self-reported merge or unverified comment |

## Structural checks

- Exactly nine top-level Skills; no new Router Skill, task database, GitHub Action runner, or daemon.
- Source manifests agree on `name` and `version` (0.8.1); discovery includes construction/audit/local Codex intents.
- Both entry surfaces preserve `project-governance → agent-handoff` for transfers and direct `evidence-audit` for explicit formal audit; false-positive negatives remain.
- Cross-context Card keeps nine required core fields, ISSUE_CONTROL EXECUTE includes real Issue/revision/digest/approval provenance, while full 19-field spec remains in Issue only.
- Local receiver verifies actual plugin, mode authority and GitHub approval before writes and preserves L0–L3/STOP/receipt semantics; no repeated nine-Skill startup loop.
- Source validation may be PASS independently of Web fresh-session auto-trigger and Desktop runtime; those live gates stay UNKNOWN until observed.
