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
| `freshness_inputs` | Dependencies whose change can stale a result. |

Check definitions and evaluations are separate records. Updating a check
does not rewrite historical results.

## Review modes

- `MACHINE`: deterministic comparison of identified inputs; result still
  depends on completeness and authority of those inputs.
- `AI_JUDGMENT`: AI summarizes or reasons over supplied evidence; it is
  advisory, cites inputs, states uncertainty, and cannot accept a result.
- `HUMAN`: named reviewer applies domain, product, or risk judgment.
- `HYBRID`: machine/AI evidence plus explicit human decision; record each
  contributor and who owns the final judgment.

AI MUST NOT invent missing source facts, silently normalize canonical data,
or treat its own prior answer as independent review.

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

Evaluation outcomes are `PASS`, `FAIL`, `UNVERIFIED`, `NOT_APPLICABLE`, and
`STALE`. A finding is created for an actionable `FAIL`; unknown or stale
results may require a separate evidence task but must not masquerade as pass.

Finding fields:

- `finding_id`, `check_id` and `check_version`;
- target, standard/profile versions, and exact repository/runtime revision;
- observed result and expected condition;
- severity/risk and impact rationale;
- evidence references, evaluator/reviewer mode, identity, and timestamp;
- remediation recommendation and accountable owner;
- status (`OPEN`, `ACKNOWLEDGED`, `MITIGATED`, `ACCEPTED_RISK`,
  `RESOLVED`, `REOPENED`);
- linked exception, decision, and follow-up task when applicable;
- freshness state and invalidation reason.

Finding status describes only the finding. `ACCEPTED_RISK` requires a link to
an authorized project decision and does not grant or renew an exception.
Where a project task/issue system owns remediation workflow, the finding links
to that task and mirrors only the minimum status needed for review; it MUST
NOT become a competing task tracker or project-status authority.

## Evaluation → finding → decision → enforcement

1. An evaluator applies a versioned check to identified inputs and emits an
   evaluation.
2. A failing evaluation may create/update a finding with evidence links.
3. An authorized human/project gate owner decides priority, accepted risk,
   required correction, or whether a project transition is blocked.
4. An enforcement adapter, if separately authorized in a future task, may
   consume that decision. It does not run as a hidden side effect of
   evaluation.

v0.1 ends at the advisory finding and explicit project-owned decision. No
automatic write, branch protection change, repair, or deployment action is
part of this contract.
