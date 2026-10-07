# Minimum decision-linked probe

Design a probe only after the evidence gate names one concrete missing fact and the decision it blocks. Explain why existing evidence cannot establish that fact. A probe should close that gap or distinguish the current plausible explanations, and its possible results must be able to change the next decision. If it cannot change a decision, it usually should not be added.

Record for each probe:

```text
MISSING_FACT: <the one fact to establish>
COMPETING_EXPLANATIONS: <current reasonable explanations relevant to the blocked decision>
DISCRIMINATING_OBSERVATION: <what observation would support or weaken each explanation>
RESULT_TO_DECISION: <the next decision for each material result>
```

Prefer, in order, existing read-only evidence, canonical state, identified runtime evidence, and then narrowly scoped instrumentation only when needed. Keep the probe limited to the smallest observation that distinguishes the alternatives or establishes the missing fact.

Do not collect broad logs “just in case,” change product behavior under the label of diagnosis, add permanent telemetry by default, or observe facts unrelated to the blocked question. If all plausible outcomes lead to the same next decision, do not add the probe.
