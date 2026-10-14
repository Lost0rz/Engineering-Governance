# Capability composition

The seven Skills cooperate without creating competing controllers.

## Ownership

`project-governance` owns entry, task/control authorization, lifecycle/reconciliation, workspace/writer boundaries, verification choice, and closeout. A narrower Skill owns only its bounded capability and returns to its caller.

Task, execution unit, and execution context remain distinct. Handoff, Sub Agent dispatch, machine/session change, or Web/local transfer does not alter project authority by itself.

## Default route

```text
request
-> project-governance
-> solution-design?        material design ambiguity
-> domain-navigation?      unclear semantic/source/test/runtime route
-> execution-orchestrator? useful decomposition/parallelism/delegation/recovery
-> agent-handoff?          responsibility crosses contexts
-> authorized implementation / verification
-> incident-doctor?        blocking evidence gap
-> evidence-audit?         explicit acceptance/readiness boundary
-> live host gates?        when host rules govern the requested boundary
-> project-governance      alignment / lifecycle closeout
```

Question marks are real gates. A keyword is not a trigger, and installed capability is not a reason for ceremony.

## Same task vs distinct purpose

Keep one `TASK_ID` across same-purpose delegation/context changes. Reconcile or use a distinct task when engineering purpose/authorization materially changes, such as separately commissioned design, independent acceptance, or corrective work.

Within one execution task, controller/scout/implementer/verifier Sub Agent units remain execution units rather than new task authorities.

## Cross-repository work

One governing task may coordinate several repositories. Project Governance names the participating repositories, per-repository writer authority, shared contract authority, integration order, and acceptance owner only when material. Source/runtime truth remains with the repository/system that owns it; do not copy all repository controls into a new cross-repo control artifact.

Domain Navigation may trace the upstream/downstream route across those named repositories; Agent Handoff may move responsibility across contexts; neither becomes cross-repo task authority.

## Artifact classes

**Authorities:** applicable controls, accepted product/domain/data/runtime sources, accepted durable design when justified, and Git/host/runtime systems for facts they own.

**Evidence/transport:** handoffs, Sub Agent briefs, ledgers, audit reports, CI/test output, runtime observations, probes, review findings. These cannot silently expand scope or replace authority.

## Parallelism

One task can coordinate many independent execution units. Use safe useful parallelism. Overlapping semantic state keeps one writer; concurrent writers require proven-disjoint semantic write authority/workspaces and defined integration evidence.
