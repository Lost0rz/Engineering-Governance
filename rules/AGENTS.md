# Engineering Governance Plugin Rules

- **3-Tier Lightweight Routing:** match the user's request directly to **one** domain Skill from frontmatter (`engineering-workflow`, `ci-governance`, `ui-design`, `architecture`, `incident-doctor`, `evidence-audit`, `codebase-context`); follow that Skill's inline `## Fast route` table and load a `references/` file **only** when the selected sub-mode explicitly requires it.
- Never load all Skills or unrelated reference files as a startup checklist.
- Host/tool permissions and explicit host orchestration or model-routing rules govern actual writes and subagent execution; project `AGENTS.md` governs project-specific constraints.
