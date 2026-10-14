# Routing adoption and upgrade

Adoption makes the seven Skills discoverable through the routing surfaces supported by the current execution environment. It does not require an installer daemon, hook, MCP service, background process, or automatic file mutation.

## Completion contract

Adoption is complete when:

1. the intended Plugin payload/version is available and all seven Skills resolve; and
2. at least one supported authoritative routing surface can select them correctly.

If the environment has an authoritative global guidance file, manage exactly one current Engineering Governance routing block using the shipped markers/template. If the environment does not expose such a file, do **not** invent one; rely on its supported Skill metadata/platform/explicit-selection routing surfaces and verify behavior there.

## Global-guidance environments

Use the exact markers in `assets/templates/GLOBAL_AGENTS_ROUTING.md`:

```text
<!-- BEGIN ENGINEERING-GOVERNANCE ROUTING -->
<!-- END ENGINEERING-GOVERNANCE ROUTING -->
```

Manage only that region and preserve unrelated guidance. Multiple/conflicting marker regions require reconciliation rather than guessing.

## Upgrade verification

Verify only the surfaces relevant to the environment being upgraded:

- intended Plugin identity/version;
- exact seven-Skill availability;
- Project Governance as normal engineering entry;
- narrow Skills remain conditional;
- routing is based on semantic outcome/condition rather than keywords;
- no routing surface duplicates Skill procedure or project facts;
- environments with managed global guidance have exactly one current routing block;
- environments without it remain functional through their actual supported routing surface.

Global routing adoption and target-project governance are separate operations.
