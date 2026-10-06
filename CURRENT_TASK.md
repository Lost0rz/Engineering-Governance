# CURRENT TASK — EG-V01 Reference Synthesis

Task ID: `EG-V01-REFERENCE-SYNTHESIS-001`

State: `ACTIVE`

Mode: `GOVERNANCE_MODEL_CANDIDATE`

## Objective

Audit the named upstream references, synthesize an evidence-backed Governance
Model v0.1 candidate, test its explanatory fit against InvestDesk without
changing that repository, perform an adversarial review, and synchronize the
result for independent Web audit.

## Allowed scope

- Create and maintain this repository's `AGENTS.md`, `CURRENT_STATUS.md`, and
  `CURRENT_TASK.md` control plane.
- Add reference audit records under `docs/reference-audit/` for Backstage,
  OpenSSF Allstar, OpenSSF Scorecard, OpenTelemetry Specification, OPA +
  Conftest, arc42, MADR, and DDD Crew Context Mapping + Context Mapper.
- Record upstream source URLs plus verified versions, revisions, or access
  dates; answer the shared 14-question audit for each reference and classify
  important mechanisms as ADOPT, ADAPT, DEFER, or REJECT.
- Add synthesis and Governance Model v0.1 candidate documents under
  `docs/`, including authority, lifecycle, cross-cutting axes, checks,
  evidence, findings, exceptions, freshness, versioning, and
  decision/enforcement contracts.
- Read InvestDesk controls and relevant code/contracts as a read-only reality
  check. Record only verified observations in this repository.
- Perform and record an adversarial review of the candidate.
- Commit and push authorized Engineering-Governance work; create a Draft PR
  when suitable; stop at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.

## Explicit non-goals

- Do not modify InvestDesk files, controls, branches, pull requests, or
  worktrees after the authorized fast-forward synchronization.
- Do not implement Bootstrap, Doctor, executable Audit skill, CLI, MCP,
  background daemon, continuous compliance service, automatic enforcement,
  or automatic remediation.
- Do not merge the task PR, publish a release, or change protected `main`
  after creating the candidate task branch.
- Do not sync unrelated repositories or perform unrelated cleanup/refactoring.

## Required gates

1. **Reference audit:** verify all eight named reference groups using primary
   upstream sources; stop if a necessary reference cannot be verified.
2. **Synthesis:** separate ADOPTED, ADAPTED, DEFERRED, REJECTED, and OPEN
   QUESTIONS; retain only contracts supported by the audit.
3. **Candidate:** specify `GovernanceStandard`, `ProjectProfile`, authority
   map, lifecycle layers, cross-cutting axes, check registry, evidence,
   findings, exceptions/waivers, freshness/drift, versioning, and the
   decision/enforcement boundary. The candidate may change the proposed
   seven-layer/six-axis counts with explicit rationale.
4. **Reality check:** evaluate Business/Product intent, domain boundaries,
   architecture, implementation/integration, verification/release,
   runtime/operability, incident/feedback, authority map, task lifecycle,
   PR/worktree lifecycle, evidence, exceptions, and freshness against the
   current InvestDesk authorities. Classify each as SUPPORTED,
   PARTIALLY_SUPPORTED, MISSING, or OVERMODELED.
5. **Adversarial review:** address over-design, authority duplication,
   precedence, waiver expiry/revocation, evidence duplication, AI judgment,
   freshness scope, layer/axis stability, small-project fit, InvestDesk fit,
   future Bootstrap/Doctor/Audit reuse, and duplicate state ownership. Fix
   BLOCKER or MAJOR findings before handoff; record MINOR findings.
6. **Handoff:** update controls with verified final state; commit and push the
   task branch, verify remote HEAD and clean worktree, and create a Draft PR
   if suitable. End at `WAITING_FOR_INDEPENDENT_WEB_AUDIT`; do not merge.

## Stop conditions

- Stop if a required upstream source cannot be verified, source authority is
  ambiguous, a repository baseline drifts unexpectedly, or InvestDesk cannot
  be inspected read-only at its verified canonical revision.
- Stop if a BLOCKER or MAJOR adversarial finding remains unresolved.
- Stop if task work cannot be synchronized to the authoritative remote; report
  `REMOTE_SYNC_PENDING` with local head, expected remote branch, blocker, and
  what is needed.
- Do not mark candidate acceptance. Independent Web audit owns that decision.
