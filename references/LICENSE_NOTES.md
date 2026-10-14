# License notes

`UPSTREAMS.md` records public work that influenced this repository's design and identifies intentional bundled-source exceptions. This note is a maintenance policy, not an exhaustive legal or provenance determination for every repository line.

Before copying or adapting upstream source code, substantial text, or other protected material into the live repository, inspect the applicable license and source provenance first. Include the attribution, notices, and other obligations required by that license, and do not treat an upstream reference as permission to copy by itself.

When the repository only records a project name, link, and concise description of conceptual influence, keep that attribution in `UPSTREAMS.md` rather than vendoring an upstream implementation as a hidden dependency.

## Current bundled-source exception

Engineering Governance v0.6.8 intentionally bundles Anthropic's `frontend-design` Skill inside `skills/design/references/anthropic/` under Apache License 2.0. Keep the adjacent license and provenance records with that source in every Plugin package that includes it. If the imported source text is modified later, record the modification prominently as required by the license and preserve applicable attribution/license terms.
