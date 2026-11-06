# EG-095 — Web-to-GitHub delegated Issue approval (source acceptance)

Scope: Issue #44, stacked Draft on PR #43 (which depends on PR #41). This is a focused source contract, not live Web/Local installed proof or a human intent signature.

| Case | Trigger | Required behavior |
| --- | --- | --- |
| A01 | No accepted AGENTS delegation opt-in | Strict `SPEC_APPROVAL_V1` only; delegated record alone => `NO_MATCHING_TRUSTED_APPROVAL` |
| A02 | Accepted AGENTS contains exactly one `ISSUE_DELEGATED_APPROVAL: ENABLED` | CLI `--allow-delegated --agents-file <accepted AGENTS>` permits the distinct delegated format |
| A03 | Duplicate, missing, disabled, Markdown-fenced, indented, quoted or HTML-comment-only AGENTS declaration | STOP: `DELEGATION_NOT_OPTED_IN`; nonoperative examples never enable proxy approval |
| A04 | Web user explicitly approves exact current repo/Issue/spec digest | AI may post `SPEC_DELEGATED_APPROVAL_V1` via authenticated Issue write surface; record actual comment ID and actor |
| A05 | Chat lacks current-spec human decision, user says generic continue, or agent decides alone | Do not post approval or emit executable handoff |
| A06 | Valid matching delegated record and opted-in receiver | `STRUCTURE_AND_DELEGATED_APPROVAL_PASS`, `DELEGATED_ACCOUNT_ATTESTED`, actual comment ID; receiver still checks code/writer/STOP |
| A07 | Normal direct approval (including when delegation is enabled) | Original `STRUCTURE_AND_APPROVAL_PASS` preserved; direct record takes precedence |
| A08 | Untrusted GitHub actor, malformed/surplus/missing attestations | STOP, no delegated authorization |
| A09 | Changed Issue content/spec revision, reused revision with conflicting hashes | STOP, reapprove updated spec before mutation |
| A10 | Trusted revocation or closed Issue | STOP |
| A11 | Progress/audit/receipt-only comment | May post if separately authorized; cannot widen approved task or force new digest |
| A12 | L2 RESUME_UNCHANGED | Only explicit operator decision, scoped digest and actor plus lower-assurance marker in opted-in mode |
| A13 | L2 RESUME_REVISED | New revision/digest and fresh direct/delegated approval; no comment-only scope expansion |
| A14 | Human UI acceptance, PR merge, release, secrets/destructive steps | Never inferred from delegated source approval; independently owned gates |
| A15 | GitHub Issue writer not exposed to Web connector | Don't invent write success; use available authorized Issue writer or return PENDING/STOP |
| A16 | Existing project not migrated or project policy stricter | No automatic change to its AGENTS, approval mode, Task/Status, runtime or CI |
| A17 | App/GitHub posts on user account | GitHub actor/id verifiable; **user's Web-chat intent is not independently provable** through this record |

## Source check
- Existing direct-approval test cases remain intact.
- Preserve 11 original delegated approval cases and add 7 fenced/indented/blockquote/HTML-comment opt-in guard regressions; 34 focused Python tests total.
- Run `python3 -m unittest discover -s skills/project-governance/scripts -p 'test_*.py' -v` on the exact candidate source before merge; no all-project CI or mandatory full-suite reruns.
- Cross-reference `issue-control.md`, `issue-execution-contract.md`, `project-governance/SKILL.md`, `agent-handoff/references/handoff-contract.md` and `agent-handoff/SKILL.md`.
- Source diff and remote branch identity are not Web Plugin publish, Local Codex install, GitHub required checks, human product acceptance, merge or release evidence.

## Security / operator decision
Delegation is an explicitly **lower-assurance convenience mode** chosen by target-project policy. If independently verifiable human approval is required, leave it disabled and keep direct GitHub approval. The Web agent cannot make GitHub identity cryptographically prove user chat intent.
