# Systematic diagnosis techniques

These techniques may be used **after** Incident Doctor's evidence gate is satisfied. They do not broaden the Doctor trigger to every ordinary bug.

## Recent-change comparison

Inspect task-relevant recent changes, configuration/environment differences, and the exact failure boundary before proposing a repair. Keep comparison bounded to evidence that can plausibly affect the blocked decision.

## Working-vs-broken comparison

Find the nearest verified working example/path and compare it with the failing path. List differences before deciding which difference is causal; do not assume a small difference is irrelevant without evidence.

## Backward data-flow tracing

When a bad value/state appears deep in a flow, trace who produced it and what fed that producer until the earliest evidence-supported fault boundary is found. Prefer repairing the causal boundary over patching a downstream symptom.

## Single-hypothesis minimum test

State one falsifiable hypothesis and the observation that would support/refute it. Change/measure one material variable at a time where practical. A failed hypothesis should produce a new hypothesis from new evidence, not a stack of speculative fixes.

## Condition-based waiting

For timing/concurrency behavior, prefer observing the actual condition/event/state transition over arbitrary sleeps/timeouts when the environment provides such an observable. Keep any probe temporary unless a later authorized task promotes it to durable product observability.
