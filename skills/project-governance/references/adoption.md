# Global routing adoption and upgrade

Engineering Governance adoption is performed by an authorized AI agent. This contract does **not** define or require an installer executable, Bootstrap CLI, daemon, hook, MCP service, background process, or automatic file-mutating runtime.

The adoption target is the user's declared global agent-guidance file. For Codex-style setups this is commonly the global `AGENTS.md` under the user's agent configuration directory; if the environment declares a different authoritative global file, use that authority instead of guessing a path.

## Installation completion contract

Treat Engineering Governance installation/adoption as a two-part result:

1. the Plugin payload is installed/available and all three expected Skills resolve: `project-governance`, `domain-navigation`, and `incident-doctor`;
2. the authoritative global guidance contains exactly one verified current Engineering Governance managed routing block.

Do not report installation as complete when only the Skill payload exists but the global route has not been adopted. Likewise, a routing block that points to unavailable Skills is not a complete installation. If the environment cannot establish one of the two parts, report the partial state and the missing requirement rather than silently treating it as success.

For an upgrade, verify the new Skill payload first, then update the managed routing block if its current template differs. This ordering avoids installing a route that points to capability definitions that are not yet available.

## Managed block identity

The reusable block is bounded by the exact markers shipped in [GLOBAL_AGENTS_ROUTING.md](../assets/templates/GLOBAL_AGENTS_ROUTING.md):

```text
<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
```

Treat the complete marker-bounded region as one managed unit. Do not manage or rewrite unrelated text outside that region.

## Adoption state machine

Before writing, inspect the existing global file and classify the managed-block state:

1. **No managed block** — insert exactly one current block at an appropriate durable routing/instructions location. Preserve unrelated rules.
2. **Exactly one current block** — make no semantic change. Do not append a duplicate.
3. **Exactly one older/compatible block** — replace that marker-bounded block in place with the current template. Preserve unrelated rules and its surrounding document structure.
4. **Multiple managed blocks or conflicting partial markers** — stop and reconcile. Do not guess which copy is authoritative and do not append another block.
5. **No authoritative global guidance file established** — do not invent project-local substitution. Report the missing adoption authority and establish it through the environment's normal configuration path before installing the block.

## Idempotency contract

Applying the same Plugin routing template repeatedly to a valid target must converge on exactly one current managed block and leave unrelated global rules semantically unchanged. An adoption operation is not complete merely because the three Skills are installed; the global route is adopted only when the authoritative global guidance contains one verified current block.

## Upgrade contract

When the Plugin routing template changes:

- verify the upgraded Plugin payload and all three Skill identities first;
- compare the installed managed region with the current template;
- replace only that region when an upgrade is required;
- never copy full Skill procedures into the global file as part of an upgrade;
- do not rewrite project-specific `AGENTS.md` files merely because the global routing version changed;
- if local customizations were inserted inside the managed region, treat that as a conflict requiring reconciliation rather than silently discarding them.

## Verification

After adoption or upgrade, verify at minimum:

- the installed Plugin identity/version intended by the adoption is established and all three expected Skills are available;
- exactly one BEGIN marker and one END marker exist in the authoritative global file;
- BEGIN precedes END and they bound exactly one managed region;
- the block names the three expected Skills: `project-governance`, `domain-navigation`, `incident-doctor`;
- Project Governance is the normal engineering entry;
- Domain Navigation is conditional rather than unconditional repository scanning;
- Incident Doctor remains evidence-gated and reactive;
- unrelated global rules remain present and materially unchanged;
- no full Skill workflow has been duplicated into the global file.

## Target-project adoption

Global routing and project governance are separate operations. A target project may need its own project-specific governance controls, but the global routing block is not copied into every repository by default. Project-local adoption follows Project Governance after inspecting that repository's real state and authorities.
