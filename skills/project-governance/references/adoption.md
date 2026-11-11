# Routing adoption and upgrade

Adoption makes the nine Skills discoverable through routing surfaces supported by the current environment. It does not require a daemon, hook, MCP service, background process, or automatic file mutation.

## Completion contract

Adoption is complete when:

1. the intended Plugin payload/version is available and all nine Skills resolve; and
2. at least one supported authoritative routing surface can select them correctly.

If the environment has authoritative global guidance, manage exactly one current Engineering Governance routing block with the shipped markers/template. If not, do not invent one; verify the environment's actual metadata/platform/explicit-selection route.

## Web and Desktop entry acceptance

When installing/updating Governance, check **separate execution surfaces** only when they are actually targeted, using current runtime evidence:

1. **Web entry**: in a fresh project chat, say "给我施工卡" or "给我审计卡" with a known task context and check actual Governance Skill resolution, correct task/Issue selection, right `agent-handoff` Card schema and truthful handling of missing approval. Plugin manifest descriptions/keywords increase discovery relevance but **do not guarantee** an automatic invocation.
2. **Codex Desktop/local receive**: in a fresh local session, check actual installed source/version/Skill availability and the accepted repository's authority, selected task, current PR/workspace and necessary permissions before an allowed write. A terminal-only `gh` check does not establish Desktop tool permissions.
3. **Claude Code/local receive**: inspect the actually installed or symlink-resolved Skill source and the receiving agent's effective permissions; a Codex installation does not prove Claude Code uses the same version.
4. Negative controls: explanation-only prompts must not auto-create Issues, direct read-only audit must not become construction handoff, inaccessible plugin/GitHub must not be described as success, and a changed/unapproved Issue must not authorize writes.

A source/package check does not establish Web auto-selection, Codex Desktop or Claude Code runtime behavior. Record **source SHA, packaged manifest version and payload digest, Web-installed identity, Codex-installed source and Claude-installed source separately**, reusing existing host/install metadata instead of inventing a runtime controller. A plugin ZIP built from a Draft PR is a test artifact, not an accepted release, and a marketplace `main` ref will not install Draft PR changes.

## Verification router adoption

The reusable V0–V3 selection policy is maintained in `verification-tiers.md`. A repository's CI adapter must fetch its own trusted base/head diff and obtain a deterministic verification plan from an **accepted** selector, never from untrusted PR source; the receiving repository remains responsible for executable test commands, dependency maps, its required check names and actual host acceptance. If those capabilities are absent, preserve existing checks or conservatively execute the relevant full suite rather than silently skipping. A successful scope selector with skipped jobs is not a full-test PASS. Install or upgrade of the Skill source alone does not modify another repository's GitHub Actions.

## Upgrade verification

Verify only relevant surfaces:

- intended Plugin identity/version and exact nine-Skill availability;
- Project Governance remains normal engineering entry;
- Project Profile triggers for profile/context-index work, not normal development;
- Design triggers for bounded UI/UX/frontend interaction/visual design while Solution Design remains engineering architecture/state-ownership authority;
- mixed frontend workflow routing distinguishes interaction workflow from business/state workflow;
- selected Skills may make bounded evidence-triggered calls to another capability when a concrete unresolved dependency requires it;
- each such call has a specific dependency, decision impact, bounded expected return and a return/resume owner or stage;
- no Skill is invoked merely for enrichment, completeness, a generic second opinion or because it is installed;
- bounded nested calls return to the originating capability instead of restarting an all-Skill pipeline;
- routing does not duplicate Skill procedure or project facts;
- supported global-guidance environments have one current block; environments without it remain functional.

Global routing adoption and target-project governance/profile generation are separate operations. The historical `references/V081_ENTRY_ROUTING_RECEIVER_ACCEPTANCE.md` documents the v0.8.1 nine-field acceptance baseline and must not be treated as a current requirement for the seven-field compatible Handoff; do not rewrite historical acceptance evidence into a new result. A release candidate still needs a fresh live Web, Codex Desktop and Claude Code smoke check against the same accepted source SHA and package manifest identity.


## ISSUE_CONTROL project adoption

Skill installation does not switch a consuming project. Versioned CONTROL_POLICY_V1 owns the common default Issue Control workflow. Existing repositories must prove their accepted migration by live GitHub merge-commit ancestry (using the global routing locator, not project `AGENTS.md`), after establishing an approved Issue and verified Web connector/local `gh` access. Unverified or unmigrated projects remain FILE_CONTROL and gain no implicit write permission. Verify cutover, authority uniqueness, issue receipt posting and original PR/human acceptance. Do not add a daemon, runtime router, issue watcher or mandatory per-comment CI validator simply to adopt this source contract.
