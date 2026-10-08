# CURRENT STATUS — Engineering-Governance

Last verified: 2026-10-08.

## Accepted reusable baseline

- Reusable Skill/content baseline remains `2d3274735449c4164dff5859d7a4dd74ddef8f39`.
- Exactly three reusable Skills remain: `project-governance`, `domain-navigation`, and `incident-doctor`.
- Full repeated Skill/content audit remains accepted with zero blocking/important design findings.
- RemoteOrbit read-only adoption-gap audit is complete; no RemoteOrbit mutation is part of the current task.

## Current packaging objective

The next authorized step is to package the existing three Skills as one local Codex plugin named `engineering-governance`, then install and validate that plugin in a supported local Codex surface.

This is packaging/distribution metadata only. It does not authorize changing any Skill instructions, templates, reference semantics, target-project controls, product code, diagnostics, runtime behavior, MCP servers, hooks, daemons, databases, or enforcement tooling.

The preferred portable package shape is the existing repository root plus a minimal root `plugin.json`; the existing root `skills/` directory remains the Skill payload. A compatibility `.codex-plugin/plugin.json` may be added only if the local host demonstrably requires it after checking current official OpenAI plugin documentation.

## Local executor freshness issue

A local executor reported a clean checkout at `e4e3ed975b46617c29b9bf83346a835bf0be8420`, 67 commits behind its local `origin/main`, and correctly stopped because its local control plane was stale and authorized an unrelated Doctor CLI closeout.

The authoritative remote control plane is newer. Before packaging, the local executor must fetch the verified canonical remote and fast-forward the clean local `main` to the current remote `main`. It must not continue from the stale local task. If the fast-forward is not possible without overwriting unique local work, STOP and report.

## Installation/test boundary

The packaging task may also make user-local Codex configuration changes needed for a personal local plugin test, including the personal marketplace and plugin copy/cache workflow described by current official OpenAI documentation. These user-local changes must remain outside business repositories.

The installation test should use a new Codex chat after installation and perform read-only discovery/routing checks against RemoteOrbit. The test must not mutate RemoteOrbit merely to prove plugin discovery.

## Current task

- Task: `EG-CODEX-PLUGIN-PACKAGING-033`.
- State: `AUTHORIZED_FOR_LOCAL_PACKAGING_AND_INSTALL_TEST`.
- Mode: `CODEX_PLUGIN_PACKAGING`.

## Next milestone

Produce the minimal plugin package, install it through a personal local marketplace, verify all three Skills are discoverable/usable from a fresh Codex session, and return exact repository and local-install evidence for independent review before any broader distribution or reusable Skill change.
