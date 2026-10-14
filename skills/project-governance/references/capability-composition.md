# Capability composition

The eight Skills cooperate without competing controllers.

`project-governance` owns task/control authority, lifecycle/reconciliation, writer/workspace boundaries, verification choice and closeout. A narrower Skill owns only its bounded capability.

## Typical composition

```text
request
-> project-governance
-> project-profile?         only when compact project context/index is the requested artifact
-> solution-design?         material design ambiguity
-> domain-navigation?       unclear semantic/source/test/runtime route
-> execution-orchestrator? useful decomposition/delegation/recovery
-> agent-handoff?           responsibility crosses contexts
-> implementation / verification
-> incident-doctor?         blocking evidence gap
-> evidence-audit?          explicit independent/read-only boundary
-> project-governance       alignment / closeout
```

Question marks are real gates. Installed capability is not a reason for ceremony.

## Artifact roles

- **Normative/current/design authorities:** project controls and accepted product/domain/data/design/runtime sources for the classes they own.
- **Derived projections:** Project Profile and Domain/navigation maps; authority wins when they are stale.
- **Evidence/transport:** handoffs, briefs, ledgers, audits, CI/test/runtime/review evidence; these cannot expand scope or replace authority.

Same-purpose work keeps one task across agents/contexts. One objective may span repositories, but each repository keeps its own control/write authority. Parallel writers require proven-disjoint semantic write authority and integration evidence.
