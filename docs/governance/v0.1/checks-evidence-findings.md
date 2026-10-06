# Checks, Evidence, Findings, and Decision Boundary

## Check registry

Each check definition SHOULD carry:

| Field | Meaning |
|---|---|
| `check_id` | Stable, unique identifier. |
| `check_version` | Version of check meaning and expected evidence. |
| `title` / `purpose` | Short name and risk/control question. |
| `scope` | Target fact class, repositories, paths, runtime or decision. |
| `applicability` | Preconditions, exclusions, and `NOT_APPLICABLE` criteria. |
| `risk` / `severity` | Impact rationale and level; do not imply a numeric aggregate. |
| `lifecycle_layers` / `axes` | Relevant layers and cross-cutting review dimensions. |
| `review_mode` | `MACHINE`, `AI_JUDGMENT`, `HUMAN`, or `HYBRID`. |
| `required_evidence` | Inputs, source identities, revisions, and freshness needs. |
| `decision_states` | Allowed outcomes and their meanings. |
| `remediation` | Suggested owner/action or canonical remediation reference. |
| `owner` | Accountable maintainer of the check definition. |
| `freshness_inputs` | Dependencies whose change can stale the result's freshness assessment. |

Check definitions and evaluations are separate records. Updating a check
does not rewrite historical results.

## Review modes

- `MACHINE`: deterministic comparison of identified inputs; result still
  depends on completeness and authority of those inputs.
- `AI_JUDGMENT`: AI summarizes or reasons over supplied evidence; it is
  derived/advisory, cites underlying inputs, states uncertainty, and cannot
  accept a result. It cannot independently satisfy factual PASS/FAIL evidence
  unless the check explicitly evaluates the AI artifact itself.
- `HUMAN`: named reviewer applies domain, product, or risk judgment.
- `HYBRID`: machine evidence and, where useful, AI-derived analysis plus an
  explicit human decision. For factual checks, AI analysis is supplemental
  and the underlying source evidence remains required; record each contributor
  and who owns the final judgment.

AI MUST NOT invent missing source facts, silently normalize canonical data,
or treat its own prior answer as independent review. For factual checks, an
AI-derived summary or judgment is not a substitute for the underlying source
evidence. It may be evidence when the check is explicitly about that AI
artifact's properties (for example, whether it cites required sources); it
still does not prove the facts summarized.

## Evidence record

Evidence kinds may include `REPOSITORY`, `TEST`, `RUNTIME`, `EXTERNAL`,
`HUMAN`, or `AI`. A record includes:

- `evidence_id`, kind, claim supported, and source/authority URI;
- target identity and exact revision/build/runtime/version when available;
- capture time, collector/reviewer, method, and relevant scope;
- for AI-derived evidence: model/provider and model/version identity when
  available, prompt/instruction or evaluation-template revision, cited input
  evidence, uncertainty/limitations, and the human decision owner; do not
  retain sensitive prompt payload when a provenance pointer is sufficient;
- content digest or stable artifact reference where appropriate;
- limitations, redactions, and whether evidence is reproducible;
- dependencies used for freshness calculation.

Evidence is a pointer/observation, not a duplicate canonical fact store. Keep
sensitive payload out of evidence summaries; preserve an authorized source
reference instead.

## Evaluation and finding

An evaluation record has a historical `result` of `PASS`, `FAIL`,
`UNVERIFIED`, or `NOT_APPLICABLE`, plus the exact inputs and evaluation time.
That result is immutable evidence of what the check concluded then.

Freshness is a separate, time-scoped assessment, not an evaluation result. A
freshness assessment identifies the evaluation, assessment time, status
(`CURRENT`, `STALE`, or `UNKNOWN`), and changed/unverifiable dependencies.
Later drift may change the current freshness assessment without rewriting the
historical evaluation. A historical `PASS` paired with `STALE` or `UNKNOWN`
freshness MUST NOT be presented as a current PASS; obtain a new evaluation.

A finding is created for an actionable historical `FAIL`. The finding may
link to current freshness assessments, exception records, and project
decisions, each with its own identity and state. An exception or accepted-risk
decision does not rewrite the evaluation result.

Finding fields:

- `finding_id`, `check_id` and `check_version`;
- target, standard/profile versions, and exact repository/runtime revision;
- observed result and expected condition;
- severity/risk and impact rationale;
- evidence references, evaluator/reviewer mode, identity, and timestamp;
- remediation recommendation and accountable owner;
- finding workflow status (`OPEN`, `ACKNOWLEDGED`, `MITIGATED`, `RESOLVED`,
  `REOPENED`);
- current `project_decision`: `NONE`, `REMEDIATION_REQUIRED`,
  `ACCEPTED_RISK`, or `GATE_HOLD`, with decision owner, time, and linked
  canonical decision record;
- current exception reference and its independent status
  (`NONE`, `ACTIVE`, `EXPIRED`, `REVOKED`);
- freshness assessment reference and invalidation reason;
- linked follow-up task in the project's task/issue authority, when applicable.

Finding workflow status describes only finding progress. `ACCEPTED_RISK` is a
separate project decision and does not grant or renew an exception. Exception
status, project decision, evaluation result, and evidence freshness MUST NOT
be collapsed into one finding status.
Where a project task/issue system owns remediation workflow, the finding links
to that task and mirrors only the minimum status needed for review; it MUST
NOT become a competing task tracker or project-status authority.

## Evaluation → finding → decision → enforcement

1. An evaluator applies a versioned check to identified inputs and emits an
   immutable historical result.
2. A separate freshness assessment reports whether that result's dependencies
   remain current; it does not mutate the result.
3. A failing evaluation may create/update a finding with evidence links.
4. An authorized human/project gate owner records the current project
   disposition. Any exception has its own lifecycle and does not mutate the
   finding's historical evaluation.
5. An enforcement adapter, if separately authorized in a future task, may
   consume an explicit current decision. It does not run as a hidden side
   effect of evaluation.

v0.1 ends at the advisory finding and explicit project-owned decision. No
automatic write, branch protection change, repair, or deployment action is
part of this contract.
