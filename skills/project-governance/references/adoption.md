# Global routing adoption and upgrade

Engineering Governance adoption is performed by an authorized AI agent. This contract does **not** define or require an installer executable, daemon, hook, MCP service, background process, or automatic file-mutating runtime.

The adoption target is the user's declared authoritative global agent-guidance file.

## Installation completion contract

Installation/adoption is complete only when:

1. the Plugin payload is installed/available and all seven expected Skills resolve: `project-governance`, `solution-design`, `execution-orchestrator`, `agent-handoff`, `evidence-audit`, `domain-navigation`, `incident-doctor`;
2. the authoritative global guidance contains exactly one verified current Engineering Governance managed routing block.

For upgrades, verify the new Skill payload first, then reconcile the managed routing block. Do not install a route that points to unavailable capabilities.

## Managed block identity

Use the exact markers shipped in [GLOBAL_AGENTS_ROUTING.md](../assets/templates/GLOBAL_AGENTS_ROUTING.md):

```text
<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
```

Manage only that complete region; preserve unrelated global guidance.

## Adoption state machine

1. **No managed block** — insert exactly one current block.
2. **Exactly one current block** — no semantic change.
3. **Exactly one older compatible block** — replace that marker-bounded region in place.
4. **Multiple blocks/conflicting partial markers** — stop and reconcile; do not guess.
5. **No authoritative global guidance established** — report the missing authority rather than inventing a project-local substitute.

## Upgrade/verification contract

After adoption or upgrade verify:

- intended Plugin identity/version is established;
- all seven expected Skills are available;
- exactly one BEGIN and one END marker exist and bound one current region;
- Project Governance is the normal engineering entry;
- the four new capabilities are conditional rather than mandatory ceremony;
- Domain Navigation remains conditional routing evidence;
- Incident Doctor remains reactive/evidence-gated;
- the block does not duplicate Skill procedures or project facts;
- unrelated global rules remain materially unchanged.

Global routing and target-project governance remain separate operations. Do not copy the global block into every repository by default.
