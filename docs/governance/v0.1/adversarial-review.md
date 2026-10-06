# Adversarial Review — Governance Model v0.1 Candidate

**Review type:** executor-performed adversarial self-review plus corrective
reassessment after independent Web audit; not independent re-review and not
candidate acceptance.
**Initial reviewed revision:** task branch content after Gates 2–5, before
the first handoff.
**Corrective base:** `4631a7c7535f18d1739c467a977b9bd94b62c811`, containing the
independent Web audit findings.

## Challenge log

| Challenge | Severity | Adversarial question and result |
|---|---|---|
| Over-design | MINOR, addressed | Seven layers plus six axes could become a mandatory bureaucracy. They are now expressly navigation/review dimensions, not a document-per-layer or check-per-cell requirement; the small-project minimum avoids full architecture artifacts. |
| Authority duplication | MAJOR, addressed | Could profile, finding, or Workspace duplicate canonical facts? The contract now limits maps/findings to source references and dated observations; consumer projections remain derived. InvestDesk reality check confirms the map indexes existing authorities rather than copying them. |
| Precedence | MAJOR, addressed in corrective | Could a project override silently contradict an accepted contract or canonical source? Authority is routed by claim/action class; profile invariants are non-overridable; same-class conflict yields `UNVERIFIED` and blocks consequential decisions. v0.1 has no parent-profile inheritance. |
| Waiver expiry/revocation | MAJOR, addressed in corrective | Could an exception become permanent or conceal a false fact? It has grantor, reason, bounded scope, evidence, expiry, review, history and revocation. Expiry changes exception state only; it does not rewrite a historical result or by itself stale evidence. |
| Evidence duplication | MINOR, addressed | Could evidence become a second data store or expose sensitive input? Candidate uses source pointers/digests, limits copies, records redaction and reproduction limits, and prohibits embedding sensitive payload in summaries. |
| AI judgment | MAJOR/MINOR, addressed in corrective | Could AI output become authority or independent audit? It is derived/advisory, cites underlying evidence, cannot independently satisfy factual PASS/FAIL evidence unless the check targets the AI artifact itself, and cannot review its own prior output as independent evidence. |
| Freshness scope | MINOR, remaining | Six drift classes may over-invalidate or miss semantic dependencies. Invalidation is dependency-scoped; check owners define signals/rechecks; unbounded impact makes the freshness assessment `STALE` or `UNKNOWN`, preserving the historical result. The actual dependency graph is deferred until an evaluator is authorized. |
| Layer/axis stability | MINOR, remaining | Boundaries may overlap (especially evidence vs freshness and domain vs architecture). Layers are distinct decisions/evidence exits; axes are nonexclusive. Revisit counts only during independent audit or implementation evidence, not by adding more categories now. |
| Small-project fit | MAJOR, addressed | Would a small repository need seven documents, profile inheritance, and all checks? No. Its minimum is pinned version, repository/revision, relevant authorities, selected checks, and evidence pointers; unselected is not pass. |
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

## Corrective response to independent Web audit

| Audit finding | Resolution in this corrective |
|---|---|
| MAJOR 1 — historical evaluation result, evidence freshness, and exception/project disposition were conflated. | **RESOLVED:** result is `PASS | FAIL | UNVERIFIED | NOT_APPLICABLE`; a separate time-scoped freshness assessment is `CURRENT | STALE | UNKNOWN`; exception state and project decision are independent. Expiry/revocation never rewrites an old result. |
| MAJOR 2 — authority classes appeared in one total precedence order. | **RESOLVED:** `authority-model.md` and root `AGENTS.md` route claims by type. Precedence applies only within the same claim/action class, with explicit limits between semantics, Git/GitHub, snapshot, task scope, runtime/data, and derived evidence. |
| MINOR — AI-derived analysis could be read as sufficient factual evidence. | **RESOLVED:** AI analysis must cite underlying sources and cannot independently support a factual PASS/FAIL unless the check explicitly evaluates the AI artifact itself. |
| MINOR — parent-profile inheritance lacked repeated project evidence. | **RESOLVED:** removed from the v0.1 ProjectProfile and marked DEFERRED. One pilot and an explicit standalone profile do not demonstrate a repeated need. |

No layer/axis redesign was made. The current audit set provides one pilot, so
profile inheritance is not retained based solely on an upstream precedent.

## Remaining MINOR questions

- At what point, after an implementation exists, is drift invalidation too
  broad or too narrow for semantic dependencies?
- Should the first accepted release retain all seven layers/six axes, or
  collapse any after observing more than one real project profile?

Both questions are suitable for independent Web re-review or a future
implementation-backed revision. They do not block this corrective handoff.
This executor reassessment is not the independent re-review; after push, the
task returns to `WAITING_FOR_INDEPENDENT_WEB_AUDIT`.
