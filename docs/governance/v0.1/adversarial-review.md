# Adversarial Review — Governance Model v0.1 Candidate

**Review type:** executor-performed adversarial self-review against the
required challenge list; not independent Web audit and not candidate
acceptance.
**Reviewed revision:** task branch content after Gates 2–5, before final
handoff controls/commit.
**Result:** no unresolved BLOCKER or MAJOR found. Three MINOR clarifications
were made in the candidate; two implementation-stage questions remain open.

## Challenge log

| Challenge | Severity | Adversarial question and result |
|---|---|---|
| Over-design | MINOR, addressed | Seven layers plus six axes could become a mandatory bureaucracy. They are now expressly navigation/review dimensions, not a document-per-layer or check-per-cell requirement; the small-project minimum avoids full architecture artifacts. |
| Authority duplication | MAJOR, addressed | Could profile, finding, or Workspace duplicate canonical facts? The contract now limits maps/findings to source references and dated observations; consumer projections remain derived. InvestDesk reality check confirms the map indexes existing authorities rather than copying them. |
| Precedence | MAJOR, addressed | Could a project override silently contradict an accepted contract or canonical source? Core invariants are non-overridable; one optional parent prevents diamond inheritance; source conflict yields `UNVERIFIED` and blocks consequential decisions. |
| Waiver expiry/revocation | MAJOR, addressed | Could an exception become permanent or conceal a false fact? It has grantor, reason, bounded scope, evidence, expiry, review, history and revocation; expiry triggers review/stale state, never auto-pass or repair. |
| Evidence duplication | MINOR, addressed | Could evidence become a second data store or expose sensitive input? Candidate uses source pointers/digests, limits copies, records redaction and reproduction limits, and prohibits embedding sensitive payload in summaries. |
| AI judgment | MAJOR, addressed | Could AI output become authority or independent audit? It is advisory, must cite input and uncertainty, cannot accept, and cannot review its own prior output as independent evidence. Record evaluator identity/model/version where applicable. |
| Freshness scope | MINOR, remaining | Six drift classes may over-invalidate or miss semantic dependencies. Invalidation is dependency-scoped; check owners define signals/rechecks; unbounded impact becomes stale/unverified. The actual dependency graph is deferred until an evaluator is authorized. |
| Layer/axis stability | MINOR, remaining | Boundaries may overlap (especially evidence vs freshness and domain vs architecture). Layers are distinct decisions/evidence exits; axes are nonexclusive. Revisit counts only during independent audit or implementation evidence, not by adding more categories now. |
| Small-project fit | MAJOR, addressed | Would a small repository need seven documents, a parent, and all checks? No. Its minimum is pinned version, repository/revision, relevant authorities, selected checks, and evidence pointers; unselected is not pass. |
| InvestDesk fit | MAJOR, addressed | Would the model create parallel Decision/Transaction/Position authority or leak into the active MVP-D task? No. Reality check classifies the relation as currently missing and delegates its business semantics to InvestDesk's active task. No InvestDesk files were changed. |
| Future Bootstrap/Doctor/Audit reuse | MINOR, addressed | Is this covert authorization to build tools? No. It defines only stable contracts for future consumers. Every executable, integration, write permission, gate, or remediation requires a later explicit task and review. |
| Duplicate state ownership | MAJOR, addressed | Would `Finding.status` duplicate `CURRENT_TASK` or an issue tracker? Finding state describes the finding only; remediation tasks and project state remain owned by the project's declared task/issue system. A finding links to that owner rather than replacing its workflow. |

## Clarifications made after challenge

1. AI evidence must identify the model/evaluator version when applicable,
   cite supplied inputs, describe uncertainty, and never make final acceptance.
2. `ACCEPTED_RISK` is a project-owned decision linked to a named decision
   record; it does not itself extend an exception or modify the source fact.
3. Finding workflow is descriptive. Where an existing task/issue system owns
   remediation, Governance stores its URI/ID and does not become a second
   task tracker.

## Remaining MINOR questions

- At what point, after an implementation exists, is drift invalidation too
  broad or too narrow for semantic dependencies?
- Should the first accepted release retain all seven layers/six axes, or
  collapse any after observing more than one real project profile?

Both questions are suitable for independent Web audit or a future
implementation-backed revision. Neither blocks a documentary candidate
handoff. No independent review has occurred; state remains
`WAITING_FOR_INDEPENDENT_WEB_AUDIT`.
