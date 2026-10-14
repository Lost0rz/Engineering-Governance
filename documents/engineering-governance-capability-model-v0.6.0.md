# Engineering Governance Capability Model v0.6.0

Status: ACTIVE DESIGN AUTHORITY; current amendment `EG-CAPABILITY-PROFILE-HANDOFF-LIFECYCLE-068`

Date: 2026-10-14

Related hardening authority: `documents/engineering-governance-capability-hardening-v0.6.0.md`

## 1. Purpose

Engineering Governance v0.6.0 provides eight narrowly triggered reusable capabilities around one lightweight project authority model.

Top-level Skills:

1. `project-governance`
2. `project-profile`
3. `solution-design`
4. `execution-orchestrator`
5. `agent-handoff`
6. `evidence-audit`
7. `domain-navigation`
8. `incident-doctor`

Global routing is policy, not a ninth Skill.

## 2. Project information / authority model

| Layer | Role |
| --- | --- |
| project `AGENTS.md` | normative project-specific rules/boundaries |
| Project Profile | compact derived context/index + authority pointers |
| Domain/navigation authority | detailed semantic ownership/source/test/runtime route |
| durable planning/design | long-lived rationale/design/work packages when justified |
| `CURRENT_STATUS.md` | concise verified current-state snapshot |
| `CURRENT_TASK.md` | single active execution authorization |
| code/schema/CI/host/runtime | implementation/evidence sources for what they own |

Profile, Domain maps, handoff cards, audit reports and CI output do not become competing project controls. Derived projections yield to the authority they summarize.

## 3. Task and execution model

- **Task** — engineering objective/authorization owned by `CURRENT_TASK.md`.
- **Execution unit** — bounded work inside that task, potentially delegated.
- **Execution context** — Web/local/cloud/Sub Agent/reviewer/machine/session.

Context changes and Sub Agent decomposition do not create tasks by themselves. If the active task remains accurate, continuation resumes it directly. A materially different engineering purpose or authorization boundary is reconciled through Project Governance.

## 4. Capability ownership

| Skill | Primary trigger / ownership |
| --- | --- |
| `project-governance` | normal engineering entry; task/control/lifecycle/writers/verification/closeout |
| `project-profile` | compact project context/profile generation, reduction or freshness audit |
| `solution-design` | material intent/architecture/state-ownership ambiguity |
| `execution-orchestrator` | useful decomposition, agents, parallelism, environment-aware delegation, recovery/integration |
| `agent-handoff` | standardized bounded cross-context Card + Receipt transport |
| `evidence-audit` | read-only evidence/readiness verdict bound to identity/claims/independence |
| `domain-navigation` | unclear semantic/authority/source/symbol/test/runtime route |
| `incident-doctor` | blocking failure/unsafe ambiguity with insufficient evidence |

Narrow Skills do not silently retain task authority after their bounded result.

## 5. Environment capability authority

Current delegated-model policy remains:

```text
SUBAGENT_MODEL_POLICY: ENVIRONMENT_DEFAULT_ONLY
MODEL_OVERRIDE: NONE
CROSS_CONTEXT_MODEL_PROPAGATION: DISABLED
STRONGER_MODEL_ESCALATION: DISABLED_UNTIL_EXPLICIT_REAUTHORIZATION
```

Concrete model/reasoning, parallel capacity, delegation limits, tools and workspace/runtime constraints are resolved from the execution environment that owns them. Unexposed values remain platform-managed/`UNKNOWN`; do not infer from another machine, controller, memory, repository text or handoff.

## 6. Orchestration and writer safety

Use one executor when decomposition gives little value; use parallel read-only or proven-disjoint writer units when safe concurrency materially helps. Overlapping semantic state keeps one writer. A same-task correction reuses the current safe PR/workspace by default; new successors require a real boundary, not merely discovery of a defect.

## 7. Handoff / transport

Core rule:

```text
HANDOFF = AUTHORITY REFERENCES + FRESH DELTA + ACTION BOUNDARY + RETURN CONTRACT
```

Cards do not restate a second task contract. EXECUTE permits authorized mutation. AUDIT/REVIEW/VERIFY/DIAGNOSE are read-only; a normal test run is VERIFY, while changing tests/instrumentation is EXECUTE. Receipts report actual identity/outcome/evidence/unknowns and remain transport/evidence.

## 8. Project artifact lifecycle

Classes:

- normative authority;
- durable design authority;
- current controls;
- derived projections;
- evidence.

At state-changing boundaries, identify materially affected semantic owners and reconcile only those owners. `NO_SEMANTIC_CHANGE -> NO_WRITE -> NO_COMMIT`.

## 9. Evidence / audit / navigation / diagnosis

Verification follows risk and evidence identity. Semantic evidence and live host gates are separate claims. Evidence Audit binds verdicts to required claims and independence basis. Domain Navigation uses focused evidence-backed route discovery. Incident Doctor enters only when a real blocker plus evidence gap prevents the next safe decision.

## 10. Skill Engineering constraints

Each top-level Skill requires a distinct semantic trigger, primary ownership boundary, clear output/return contract, near-miss guidance, positive utilization guidance and progressive disclosure. Over-triggering and material under-use are both defects. Reusable source must not create hidden replacements for project controls, domain/data truth, durable planning, or runtime authorities.

## 11. v0.6.0 sequence

Tasks 061–066 established and hardened the original seven-Skill architecture. Task 068 adds Project Profile plus standardized transfer/lifecycle contracts before installed acceptance. Task 067 was superseded before runtime acceptance and produced no v0.6.0 runtime verdict.

The authoritative integrated matrix is `references/V060_INTEGRATED_ACCEPTANCE.md`. Final acceptance must test composition and positive/negative routing on the frozen eight-Skill candidate rather than only proving individual Skill files load.
