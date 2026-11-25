# Engineering Governance Plugin Rules

- Enter a matching specialist Skill directly (`design`, `solution-design`, `incident-doctor`, `evidence-audit`, `domain-navigation`, `project-profile`) when the user's goal already fits that domain; use `project-governance` for general engineering tasks, portable CI test routing, and delivery coordination.
- Load only the Skill and reference files needed for the current decision; never load unused Skills as a checklist.
- Host/tool permissions and explicit host orchestration or model-routing rules govern actual writes and subagent execution; project `AGENTS.md` governs project-specific constraints.
