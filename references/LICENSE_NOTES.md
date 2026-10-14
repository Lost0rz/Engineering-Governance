# License notes

`UPSTREAMS.md` records public work that influenced this repository's design and identifies intentional bundled/adapted-source exceptions. This note is a maintenance policy, not an exhaustive legal or provenance determination for every repository line.

Before copying or adapting upstream source code, substantial text, or other protected material into the live repository, inspect the applicable license and source provenance first. Include the attribution, notices, and other obligations required by that license, and do not treat an upstream reference as permission to copy by itself.

When the repository only records a project name, link, and concise description of conceptual influence, keep that attribution in `UPSTREAMS.md` rather than vendoring an upstream implementation as a hidden dependency.

## Bundled/adapted Design sources

### Anthropic `frontend-design`

Engineering Governance v0.6.8 intentionally bundles Anthropic's `frontend-design` Skill inside `skills/design/references/anthropic/` under Apache License 2.0. Keep the adjacent license and provenance records with that source in every Plugin package that includes it. If the imported source text is modified later, record the modification prominently as required by the license and preserve applicable attribution/license terms.

### shadcn-admin-informed pattern module

Engineering Governance v0.7.0 includes a newly written admin-pattern synthesis under `skills/design/references/shadcn-admin/`, informed by `satnaing/shadcn-admin` under the MIT License. It does not vendor the upstream application implementation. Preserve the adjacent MIT license and provenance record while the adapted module is distributed.

### awesome-design-md-informed synthesis module

Engineering Governance v0.7.0 includes a newly written design-spec synthesis module under `skills/design/references/awesome-design-md/`, informed by `VoltAgent/awesome-design-md` under the MIT License. It does not vendor upstream brand DESIGN.md files, extracted brand tokens, previews, assets or identities. Preserve the adjacent MIT license and provenance record while the adapted module is distributed.

### Microsoft frontend-design-review-informed final review

Engineering Governance v0.7.0 includes a newly written final-review module under `skills/design/references/microsoft/`, informed by the Design Review mode of `microsoft/skills` `frontend-design-review` under the MIT License. The adaptation intentionally excludes Microsoft's Creative Frontend Design mode from this downstream stage. Preserve the adjacent MIT license and provenance record while the adapted module is distributed.

## Maintenance rule

Every bundled/adapted Design source directory must keep its local provenance and applicable license adjacent to the module. Release acceptance must verify those files are packaged with `skills/**` and that upstream references never silently become target-project authority.
