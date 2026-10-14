# Minimum decision-linked probe

Add a probe only after the evidence gate names one concrete missing fact and the decision it blocks. Prefer existing read-only/canonical/runtime evidence first.

Record only what matters:

```text
MISSING_FACT
COMPETING_EXPLANATIONS
DISCRIMINATING_OBSERVATION
RESULT_TO_DECISION
```

If the probe can change timing, ordering, resource use, state, privacy exposure, or user-visible behavior, also record:

```text
OBSERVER_EFFECT_RISK
SAFETY_PRIVACY_IMPACT
CLEANUP_PLAN
```

Choose the least intrusive observation whose possible outcomes can change the next decision. If all plausible results lead to the same action, do not add the probe.

Do not collect broad logs "just in case", change product behavior under the label of diagnosis, or add permanent telemetry by default.
