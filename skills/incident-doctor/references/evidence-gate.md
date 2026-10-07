# Evidence gate

# Hard evidence gate

Complete these steps in order before adding any probe or diagnostic instrumentation:

1. **Blocked Question:** State the specific next decision that cannot yet be made safely.
2. **Real Observed Problem:** Describe the real failure, unexplained behavior, or unsafe ambiguity that makes the question relevant. Keep a user report labeled as a report until directly observed.
3. **Existing Evidence Review:** Inspect what applies: `CURRENT_TASK`, source, tests, runtime identity, build identity, configuration, canonical state, logs, prior captures, and Domain Map/authority evidence. Record source identity, revision, and freshness where relevant; do not assume unlike captures belong to one event.
4. **Evidence Sufficiency Decision:** Decide whether the reviewed evidence supports the next safe decision, and state why.
5. **Missing Fact, if any:** If evidence is insufficient, name one concrete `MISSING_FACT` that is not established.
6. **Decision Blocked by that Missing Fact:** State the exact `BLOCKED_DECISION` that cannot be made safely because that fact is missing. “Need more logs” is not a fact or an adequate gap; say what those logs must establish.
7. **Probe allowed only if necessary:** Design a probe only when it can establish that missing fact or distinguish explanations in a way that can change the blocked decision.

## Sufficiency exits

### SUFFICIENT

Choose `SUFFICIENT` when existing evidence supports the relevant safe next decision, including the minimum fix boundary, rejection of a hypothesis, or a no-fix conclusion. Cite the evidence and proceed on that basis.

**NO NEW PROBE.** Do not instrument merely to make diagnostics more complete.

### INSUFFICIENT

Choose `INSUFFICIENT` only with both fields stated:

```text
MISSING_FACT: <one concrete fact not established by existing evidence>
BLOCKED_DECISION: <the specific decision that cannot safely be made without it>
```

Then explain why available evidence cannot establish that fact. Only after this gate may probe design begin.

## Evidence categories

Keep the evidence chain explicit and do not promote a category without supporting evidence:

- `USER_REPORTED_SYMPTOM`: what a user says happened; it is not by itself a verified system fact.
- `DIRECT_OBSERVATION`: an event or state observed in an identified source/runtime and observation window.
- `INTERPRETATION`: a reasoned reading of observations; label it as inference.
- `HYPOTHESIS`: a testable possible explanation with support and falsification criteria.
- `FALSIFICATION_RESULT`: an observed result compared with those criteria.
- `FINDING`: a conclusion supported by cited evidence; it is not automatically causal.
- `ROOT_CAUSE_CLAIM`: a causal conclusion supported by evidence for the stated boundary, not by correlation or plausibility alone.

Do not turn a user report directly into a system fact, correlation into causation, or the most likely hypothesis into a root-cause claim. Default to `ROOT_CAUSE_STATUS: UNKNOWN`. A supported hypothesis is not by itself a proven root cause.
