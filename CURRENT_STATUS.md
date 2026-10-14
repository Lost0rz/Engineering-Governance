# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published baseline

Formal immutable GitHub release remains `plugin-v0.5.5`; previously accepted Web/Mac mini/MacBook Air baseline remains `0.5.5`.

No formal GitHub v0.6.0 release has been created yet.

## v0.6.0 source architecture — FROZEN

Current frozen Architecture Delivery / Semantic HEAD:

`d8bdf9da4094a0550d59afe33e02b179582150b2`

- Task `EG-CAPABILITY-CONTRACT-CORRECTIVE-069` is COMPLETE with V2 remote source-architecture audit PASS (`AUDIT_INDEPENDENCE: SELF_CHECK`).
- Bounded corrective Task `EG-V060-HANDOFF-TEMPLATE-CORRECTIVE-071` is COMPLETE; shipped Handoff request/receipt templates now match the accepted Card/Receipt contract.
- PR #26 remains OPEN / DRAFT / UNMERGED.
- No semantic-head CI/check PASS is claimed unless current host evidence reports it.

## Web Plugin candidate 0.6.0

Task `EG-V060-WEB-CANDIDATE-ACCEPTANCE-070` is `WAITING_FRESH_WEB_SESSION`.

Candidate installation evidence:

- exact candidate source: Semantic HEAD `d8bdf9da4094a0550d59afe33e02b179582150b2`;
- candidate overlay: 33 `plugin.json` / `skills/**` entries;
- Git-blob equivalence: `33/33 PASS`;
- candidate ZIP SHA-256: `18bb5d7e063524f015e77f8f66feb7df1ac761512819728a38c4c4f3c48cce9e`;
- personal Web Plugin identity preserved: `plugins_6acb0b9e8b748191a9b89fad47d89517`;
- Web Plugin current version: `0.6.0`;
- current Plugin release: `pluginrel_6acef4a99cac81919f1be1a44f965235`;
- scope/discoverability remain `USER / PRIVATE`;
- stored Plugin file surface contains all eight expected top-level Skill trees;
- platform-managed `.codex-plugin/plugin.json` is also version `0.6.0` and points to `./skills`.

Current already-open Web conversation still exposes the pre-update three-Skill discovery snapshot. This is classified as `STALE_PRE_UPDATE_SNAPSHOT`, not a v0.6.0 routing failure. Fresh-session Web discovery/routing remains `UNKNOWN` until tested in a new Web conversation/session.

Formal GitHub `plugin-v0.6.0` publication is intentionally deferred until the required installed/integrated acceptance boundary supports publication.

## Accepted architecture

- Exactly eight top-level Skills; global routing is policy, not a ninth Skill.
- `project-profile` is a derived context/index. Repository/project-managed Profile mutation requires compatible task authorization.
- A project keeps one current Profile projection surface, or one primary surface plus a derived mirror.
- Project `AGENTS.md` is normative; Domain/navigation owns detailed routing; durable planning owns long-lived design; STATUS/TASK own current state/authorization.
- Handoff separates `CAPABILITY` from `MODE`; required Card/Receipt core fields are standardized and shipped templates match that contract.
- Artifact lifecycle separates normative/design/current/implementation authority, derived projections and observed evidence; unchanged semantics produce no write/commit.
- Advisory read-only status/evidence inspection can remain in Project Governance; formal acceptance/readiness verdicts use Evidence Audit.
- Project Governance emits one compact human status receipt for governed engineering/status/audit/CI/PR/merge responses without duplicating a full Handoff Receipt.
- Same-purpose continuation preserves the active task and prefers a safe current PR/workspace for in-scope corrections.
- Runtime/model/tool/capacity configuration remains environment-owned; stronger-model escalation remains disabled during stabilization.

## Next milestone

Open a fresh Web conversation/session against the updated Plugin and complete v0.6.0 eight-Skill discovery plus Web routing positive/negative scenarios. If Web passes, continue the remaining Local Codex integrated-acceptance surfaces before formal GitHub release/merge preparation.
