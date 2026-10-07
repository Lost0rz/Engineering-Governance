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

## Delivery priority and proportionality

- Governance, diagnostics, and audit mechanisms exist to support reliable
  product/business delivery; expanding those mechanisms is not a default
  milestone by itself.
- Once current controls and evidence are sufficient to execute a bounded task
  safely, prefer the next useful product/tool capability over speculative
  governance hardening.
- Add or deepen a diagnostic/governance mechanism when an actual task exposes
  a concrete evidence gap, repeated failure mode, unsafe ambiguity, or blocker.
  Keep that corrective proportional to the demonstrated need, then return to
  the interrupted delivery path.
- Distinguish required delivery gates from optional hardening. Optional checks,
  probes, or framework expansion must not silently become prerequisites for
  unrelated feature work.
- A follow-on Doctor, Audit, Bootstrap, AI, CLI, or enforcement capability must
  be separately authorized by the active task; completing one does not imply
  permission to expand the others.

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

## Authority routing by claim class

Route each claim or action to its authority class. These classes are not one
global precedence list:

- **Product/domain/architecture semantics:** the project's declared product,
  domain, and accepted architecture contracts define meaning. They do not
  authorize work outside the active task scope.
- **Repository/remote state:** verified Git and GitHub state owns branch,
  commit, pull request, and check-run claims. Those facts do not decide product
  semantics.
- **Shared current-state snapshot:** `CURRENT_STATUS.md` publishes the
  project's concise verified snapshot. It is a coordination view of its
  declared fields, not a replacement for the underlying semantic, Git,
  runtime, or data authority.
- **Execution authorization and scope:** the user's authorization and active
  `CURRENT_TASK.md` define the work allowed now, constrained by durable
  workflow rules in `AGENTS.md`. Task scope cannot rewrite canonical business
  truth, and business truth cannot expand task scope.
- **Runtime/data facts:** use the project-declared runtime or data authority
  for that fact class, verifying its identity, scope, and observation time.
- **Derived outputs:** evaluations, findings, evidence summaries, projections,
  and AI analysis support claims but do not become source authorities. AI
  analysis must cite underlying source evidence and remains advisory.

When sources compete for the same claim or action class, use the owner and
resolution rule declared for that class. If ownership is undeclared or the
conflict cannot be resolved from verified evidence, stop the affected
decision and record the blocker. Split a mixed claim into its distinct classes
instead of letting one class override another.

Governance defaults and project profiles route evaluation; they do not become
business authorities.
