# Evidence rules

Ground every important navigation claim in concrete evidence. Useful evidence includes repository paths, symbols, manifests, tests, runtime/operational entry points, accepted project documentation, and explicit source references. Record the relevant path and, where material, the revision or observation time that supports the claim.

## Separate observation from interpretation

- **Direct observation:** what a named source actually contains or does at the inspected revision (for example, a manifest names an entry point, a test invokes a symbol, or an accepted document assigns an owner).
- **Interpretation:** the navigation conclusion drawn from those observations (for example, that a symbol appears to implement a capability). Label the reasoning and keep it proportionate to its evidence.

Do not present an interpretation or generated summary as a directly observed fact. A search result is a lead to inspect; a Repo Map ranking is only a candidate-selection aid.

## Preserve evidence limits

- Absence of evidence is not evidence of absence.
- Conflicting evidence remains unresolved until the responsible authority or source resolves it.
- Folder layout alone cannot establish Domain ownership.
- A generated summary or Domain Map is not a product, domain, data, or runtime authority.
- Record the source revision or observation/freshness basis for map claims so a later reader can judge whether re-verification is needed.
- Keep unknown claims `unknown` and stale claims `stale` until verified again. Do not invent a numerical confidence score.
