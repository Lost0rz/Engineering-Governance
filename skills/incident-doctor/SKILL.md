---
name: incident-doctor
description: Investigate a real failure, unexplained behavior, or unsafe ambiguity only when current evidence is insufficient for safe progress. Use to assess evidence sufficiency, add the minimum missing probe, capture a fresh incident, falsify hypotheses, bound the minimum fix, and retire or explicitly promote probes; do not use for routine feature development or speculative observability expansion.
---

# Incident Doctor

Use this Skill only when a real failure, unexplained behavior, or unsafe ambiguity blocks safe progress and existing evidence is insufficient to answer the blocked question.

## Read the contracts

- [Evidence gate](references/evidence-gate.md)
- [Probe design](references/probe-design.md)
- [Fresh incident capture](references/fresh-incident.md)
- [Probe lifecycle](references/probe-lifecycle.md)
- [Incident record template](assets/templates/INCIDENT.md)

First review available task, Domain Map, source, and runtime evidence. If it is sufficient, answer from that evidence and bypass new probe work. Otherwise, identify the precise gap and add only a probe that can help close it. Keep diagnosis separate from routine feature delivery and automatic remediation.
