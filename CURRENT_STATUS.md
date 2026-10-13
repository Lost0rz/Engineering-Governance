# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-14.

## Published release baseline

Formal GitHub Plugin release remains `plugin-v0.5.5`.

- Frozen publication source / tag target: `8871327915396b8de458f3e5709e3f67e36eff8f`.
- GitHub Actions release run: `38395556087` — `success`.
- ChatGPT Web Plugin: `0.5.5`.
- Mac mini Codex accepted Plugin baseline: `0.5.5`.
- MacBook Air Codex accepted Plugin baseline: `0.5.5`.

No v0.6.0 release or installed-Plugin acceptance has been performed yet.

## v0.6.0 capability-model source — REMOTE SOURCE COMPLETE

Task `EG-CAPABILITY-MODEL-V060-061` completed the remote reusable-source construction and audit on branch `codex/capability-model-v0.6.0`.

- Start Repository HEAD: `3b8d99c3dba13ca01098abade5c6e696454ddd10`.
- Delivery / Semantic HEAD for the completed source framework: `c97d3cef13ac5546bf00d9d1eb4d620c88ffad57`.
- Pull request: `#26` — OPEN / DRAFT / UNMERGED.
- PR host mergeability observed at source-audit time: `mergeable=true`.
- CI/check statuses on source head: none reported; **do not classify this as CI PASS**.

## Accepted v0.6.0 source capability model

Exactly seven top-level Skills are present on the task branch:

1. `project-governance`
2. `solution-design`
3. `execution-orchestrator`
4. `agent-handoff`
5. `evidence-audit`
6. `domain-navigation`
7. `incident-doctor`

Global routing remains policy, not an eighth Skill.

Accepted source semantics:

- Project Governance remains the normal project/repository authority/lifecycle entry.
- Solution Design is conditional for materially ambiguous/cross-boundary design decisions and does not authorize implementation.
- Execution Orchestrator controls already-authorized execution topology, prefers one executor/parallel readers, requires proven-disjoint authority for multiple writers, and forbids silent model escalation.
- Agent Handoff defines `authority references + fresh delta + action boundary + return contract`; handoff requests/receipts do not become task/status authority and should not copy full controls/rules by default.
- Evidence Audit binds findings to explicit target/range/identity, distinguishes `BLOCKING / IMPORTANT / MINOR / UNKNOWN`, and keeps semantic evidence separate from live repository-host gates.
- Domain Navigation ownership remains conditional semantic/source/test routing.
- Incident Doctor keeps its evidence-gap entry gate while adding bounded systematic diagnosis techniques; it is not expanded to every ordinary bug.
- Universal mandatory TDD, unconditional subagent-per-task dispatch, mandatory worktree creation, and automatic high-model escalation are explicitly not part of Engineering Governance.

## External-reference audit

Durable design/research authority: `documents/engineering-governance-capability-model-v0.6.0.md`.

Conceptual references recorded in `references/UPSTREAMS.md` include Superpowers, GitHub Spec Kit, OpenAI Agents SDK, LangGraph supervisor patterns, OpenHands, SWE-agent, reviewdog, OpenSSF Scorecard, and SLSA. No external runtime dependency or copied upstream implementation was introduced.

## Remote verification result

`V2 source/routing audit: PASS` for the remote reusable-source framework.

Verified:

- exact seven-Skill directory set;
- new Skill frontmatter/trigger/authority boundaries;
- managed global routing and adoption contract updated for seven Skills;
- root repository rules and README updated from the former three-Skill model;
- handoff non-authority and anti-duplication contract present;
- execution model/parallelism boundaries and no-silent-escalation rule present;
- evidence identity/host-gate separation present;
- Incident Doctor evidence gate preserved;
- no new runtime/daemon/database/automatic enforcement surface;
- historical `release-plugin-v0.5.5.yml` unchanged.

## Active problems and blockers

No blocking remote source defect is known from Task 061 audit.

Remaining acceptance gap: installed Plugin discovery/routing/runtime behavior for v0.6.0 has not yet been verified on local Codex/Web surfaces. PR #26 should remain Draft until that separate acceptance work is completed or the user explicitly chooses another integration boundary.

## Next intended milestone

Run a separate local Plugin/runtime acceptance task against PR #26 / source semantic head `c97d3cef13ac5546bf00d9d1eb4d620c88ffad57`, verify all seven Skills are discoverable and the new routing/handoff behavior works as intended, then return defects to the remote source flow or proceed to final merge/release preparation.

## Task 061 control alignment

- Related document: `documents/engineering-governance-capability-model-v0.6.0.md`.
- Document alignment: `UNCHANGED` — implementation matches the accepted durable capability design; the design document is not a live progress log.
- `CURRENT_STATUS.md`: `UPDATED` — remote source completion, PR state, audit result, and remaining local-acceptance gap are now current.
- `CURRENT_TASK.md`: `UPDATED` — Task 061 is terminal as a remote reusable-source construction task.
- Control alignment: `PASS`.
