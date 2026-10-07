# Incident Record

Keep this as a concise evidence chain, not a chronological diary. Cite evidence paths, source/runtime identities, revisions, and time windows; do not paste large log bodies. `UNKNOWN` and unresolved findings are valid outcomes. Use `not applicable` for optional sections that truly do not apply rather than adding boilerplate.

## Incident ID

[Stable identifier, if one exists; otherwise `unknown`.]

## Blocked Question

[The specific next decision that cannot be made safely. If no decision is blocked, do not enter this Doctor workflow.]

## Root Cause Status

`UNKNOWN` / `BOUNDED` / `SUPPORTED` — default to `UNKNOWN`.

- `UNKNOWN`: evidence does not establish a causal boundary; this is a valid investigation outcome.
- `BOUNDED`: evidence supports a limited fault/causal boundary, while broader cause remains unresolved.
- `SUPPORTED`: evidence supports the explicitly scoped root-cause claim below. `SUPPORTED` is not `ROOT_CAUSE_PROVEN` and does not prove claims beyond that boundary.

## User-Reported Symptom

`USER_REPORTED_SYMPTOM`: [reported behavior, reporter/source, and report time. This is not by itself a system fact.]

## Verified Runtime / Context Identity

Record applicable identities and mark missing values `unknown`: `REPOSITORY_REVISION`; `BUILD_IDENTITY`; `APP_RUNTIME_IDENTITY`; `PROCESS_ID` / `PROCESS_START`; `CONFIGURATION_IDENTITY`; relevant `SESSION_ID` / `REQUEST_ID` / `DATA_ID`; `OBSERVATION_WINDOW`; timestamps / `CLOCK_BASIS`.

## Existing Evidence

[Evidence reviewed as applicable: `CURRENT_TASK.md`, source, tests, runtime/build/configuration, canonical state, logs, prior captures, accepted semantic-authority sources, and existing navigation evidence. Cite paths/identities, revision or observation time, and freshness. If code/authority location was unclear, Domain Navigation may be cited only as the route used to locate evidence; it does not decide diagnosis.]

## Evidence Sufficiency Decision

`SUFFICIENT` / `INSUFFICIENT`: [decision and why. If sufficient, state the safe next decision supported by this evidence and record `NO NEW PROBE`.]

## Evidence Gap

For `INSUFFICIENT`, provide both fields; do not write only “need more logs”:

```text
MISSING_FACT: <one concrete fact not established by existing evidence>
BLOCKED_DECISION: <the specific decision blocked by that missing fact>
```

For `SUFFICIENT`, use `not applicable — no probe is needed`.

## Hypotheses

For each active hypothesis, keep the following fields together:

```text
HYPOTHESIS: <testable possible explanation>
WOULD_SUPPORT: <discriminating observation>
WOULD_WEAKEN_OR_FALSIFY: <observation that weakens or falsifies it>
OBSERVED_RESULT: <result and evidence reference, or not yet observed>
STATUS: OPEN | WEAKENED | FALSIFIED | SUPPORTED
```

`SUPPORTED` means evidence supports the hypothesis; it does not by itself establish root cause.

## Minimum Probe, if Needed

If evidence is `SUFFICIENT`, record `NO NEW PROBE`. Otherwise record only a decision-linked probe:

```text
MISSING_FACT: <the named evidence gap>
COMPETING_EXPLANATIONS: <current reasonable alternatives>
DISCRIMINATING_OBSERVATION: <what would support or weaken each alternative>
RESULT_TO_DECISION: <next decision for each material result>
```

Explain why existing evidence cannot answer the question. Prefer read-only canonical evidence and the smallest useful capture. Do not change product behavior under the label of diagnosis.

## Fresh Reproduction / Capture

[If a probe was added, identify a fresh reproduction after it became active. Record the smallest sufficient observation window and the applicable runtime/context identities above. Keep incompatible historical captures separate. Otherwise state `not applicable` or cite the existing attributable evidence used.]

## Direct Observations

`DIRECT_OBSERVATION`: [what was observed, from which identified source/runtime, at which revision and time window. Keep separate from user reports and interpretation.]

## Falsification Criteria / Results

`FALSIFICATION_RESULT`: [for each hypothesis, compare the observed result and evidence reference with `WOULD_SUPPORT` and `WOULD_WEAKEN_OR_FALSIFY`; record the resulting `OPEN`, `WEAKENED`, `FALSIFIED`, or `SUPPORTED` status.]

## Interpretations

`INTERPRETATION`: [reasoning from cited observations; label inference and do not state correlation as causation.]

## Findings

`FINDING`: [evidence-supported conclusion and its boundary. A finding is not automatically causal.]

## Root-Cause Claim, if Supported

`ROOT_CAUSE_CLAIM`: [state only when evidence supports this causal boundary; otherwise `none — ROOT_CAUSE_STATUS remains UNKNOWN` or `BOUNDED`.]

## Minimum Fix Boundary

[Smallest behavior change supported by the evidence, or `none / unresolved`. This is an evidence boundary, not task authorization. Correlation alone does not establish a root-cause repair boundary.]

## Authorization / Next Owner

[State whether the active `CURRENT_TASK.md` already authorizes the minimum fix and required side effects. If not, record `RETURN_TO_PROJECT_GOVERNANCE_FOR_REAUTHORIZATION` before any behavior change. Incident Doctor does not grant authorization itself.]

## Regression Verification

[If an authorized behavior fix was made, keep fix-verification evidence separate from diagnostic evidence: record the selected Project Governance `V1`/`V2`/`V3` level and rationale, then targeted regression, affected-Domain checks, and integration/runtime acceptance as required by change risk. Record results and known limits. If no behavior fix was made, state that.]

## Probe Lifecycle Decision

`TEMPORARY` / `DURABLE` / `NO PROBE`: [temporary probes are retired/removed after evidence is captured and verified unless a reason to retain them is recorded. Durable promotion requires repeated evidence of continuing value, an explicit owner and scope, and separate authorization.]

## Unresolved Unknowns

[What remains unknown or conflicting and what evidence/authority could resolve it. It is acceptable to end the investigation with these unresolved.]
