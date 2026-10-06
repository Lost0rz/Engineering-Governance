# Engineering-Governance Repository Rules

## Purpose and boundaries

Engineering-Governance defines a lightweight, Git-native, AI-assisted
engineering governance standard that can be reused across repositories. It
helps people and agents route decisions to the right project authority,
evaluate explicit checks against evidence, and communicate drift and findings.

Global workflow guidance defines reusable ways of working. Project-local
controls define a project's scope, operating rules, and current task. The
governance standard may evaluate whether those controls are clear and current;
it does not replace a project's product, domain, data, or runtime authorities.

## Authority and evidence

- Each canonical fact or decision class has one declared owner. A project may
  have multiple authorities for different classes; consumers, projections,
  and tools must not claim ownership of facts they derive or display.
- Project authority maps and adopted governance profiles are repository-local
  and Git-versioned. Global defaults may be inherited only through explicit,
  reviewable precedence and override rules.
- Preserve the distinction between a governance policy, an evaluation
  decision, a finding, and an optional enforcement action.
- Findings must cite evidence with a source, identity or revision, observation
  time where relevant, and a freshness basis. AI-generated explanation is not
  proof of the claim it describes.
- Mark unsupported, stale, or unavailable evidence as unresolved. Do not
  invent project facts or silently infer canonical data.

## Tasks, review, and repository lifecycle

- `CURRENT_TASK.md` is the single active execution contract. Keep one active
  task and one writer for shared governance documents at a time.
- `CURRENT_STATUS.md` is a concise verified snapshot, not a history log.
  Durable rules belong here only in `AGENTS.md`; decisions belong in versioned
  standards or reference records.
- Independent review follows executor evidence. An executor's completion
  claim does not constitute acceptance. Tasks requiring independent review
  remain in an explicit waiting state until that review is recorded.
- Branches, pull requests, and worktrees have explicit task ownership and
  lifecycle states. Do not silently merge, release, publish, or delete task
  resources. Before handoff, synchronize authorized work and control updates
  to the task branch's remote and verify the remote head.
- Keep changes within the active task. Do not modify pilot repositories during
  a read-only reality check.

## Checks and automation

- A check declares its stable identity, purpose, scope, applicability,
  risk/severity, review mode, required evidence, decision, remediation, owner,
  and freshness inputs.
- Distinguish deterministic machine checks from AI judgment, human review,
  and hybrid review. Do not report a judgment-based review as deterministic.
- A decision or finding may inform an advisory or gate. Enforcement is a
  separate, explicitly authorized action; v0.1 defaults to advisory/gate
  behavior and does not auto-remediate.
- Keep the governance model small and project-local. Bootstrap, Doctor, and
  Audit may later reuse one canonical model, but their implementations are
  outside the current candidate-synthesis task.
- MCP services, background enforcement daemons, continuous compliance
  services, automatic remediation, central governance databases, and large
  plugin frameworks are not part of v0.1 unless a later task explicitly
  changes scope.

## Control authority order

Resolve governance coordination using this order, without allowing a lower
item to rewrite facts owned by a higher or canonical project authority:

1. Canonical project authority for the specific fact or decision class.
2. Accepted project contracts and architecture decisions that define its
   meaning and boundaries.
3. Verified Git and remote-host state for repository, branch, commit, pull
   request, and check-run facts.
4. This repository's `AGENTS.md` for durable local operating rules.
5. `CURRENT_STATUS.md` for the latest verified project snapshot.
6. `CURRENT_TASK.md` for one authorized objective and its work boundary.
7. Findings and evidence produced within that boundary.

Governance defaults and project profiles route evaluation; they do not become
business authorities. If authoritative sources conflict and the conflict
cannot be resolved from evidence, stop and record the blocker.
