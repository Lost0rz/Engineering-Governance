---
name: incident-doctor
description: >-
  Evidence-gated root-cause diagnosis and minimal discriminating probes when a
  real failure, hang, or unsafe ambiguity blocks safe next action. Do not use
  for ordinary bugs whose stack trace, diff, or test failure already supports a
  direct fix (engineering-workflow).
---

# Incident Doctor

Enter only when a real failure blocks progress **and** existing evidence cannot identify a safe next decision.

## Fast route

| Need | Mode | Next reading |
| --- | --- | --- |
| Assess if evidence already supports a safe fix or blocks on 1 missing fact | `EVIDENCE_GATE` | **NONE (this file)** |
| Design a minimal probe, attributable capture, or systematic isolation | `PROBE_AND_TECHNIQUES` | [probes-and-techniques.md](references/probes-and-techniques.md) |
| Write a durable postmortem / incident record when requested | `INCIDENT_RECORD` | [INCIDENT.md](assets/templates/INCIDENT.md) |

## Inline hard evidence gate

1. **Blocked decision:** name the exact next engineering choice that cannot be made safely.
2. **Evidence check:** separate `USER_REPORTED_SYMPTOM` from `DIRECT_OBSERVATION` (source, logs, revision, runtime). Locate unclear code directly or via `codebase-context`.
3. **Exit or isolate one missing fact:**
   - If evidence already supports a minimum fix or falsifies the concern -> exit immediately to `engineering-workflow` (`NO NEW PROBE`).
   - If insufficient -> declare `MISSING_FACT` + `BLOCKED_DECISION`, then read [probes-and-techniques.md](references/probes-and-techniques.md).

## Boundaries

- Diagnosis never grants write or `G3` permission; pause for user confirmation if the fix exceeds task scope or adds privilege/security/irreversible risk.
- Scale post-fix verification (`V1`–`V3`) to impact and explicitly remove temporary probes.
