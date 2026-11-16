"""Portable independent Skill tests. Run from any copied Skill root (PyYAML test-only)."""
from pathlib import Path
import re
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
NOTE_HEADINGS = (
    "适用问题与复用触发", "核心结论", "原理、取舍与经验", "证据与来源",
    "适用边界与风险", "未验证事项 / 未来验证", "关联与原始入口",
)
NOTE_FIELDS = (
    "title", "created", "knowledge_status", "source_access",
    "source_kind", "reuse_scope", "source_refs", "tags",
)
ALLOWED = {
    "knowledge_status": {"verified", "provisional", "hypothesis", "deprecated"},
    "source_access": {"full", "partial", "unavailable"},
    "source_kind": {"conversation", "repository", "document", "execution", "mixed", "other"},
    "reuse_scope": {"cross-project", "project-specific", "research"},
}


def frontmatter(raw: str) -> dict:
    if not raw.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")
    parts = raw.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("Unterminated YAML frontmatter")
    meta = yaml.safe_load(parts[0][4:])
    if not isinstance(meta, dict):
        raise ValueError("Frontmatter must be a mapping")
    return meta


def validate_note(raw: str) -> dict:
    meta = frontmatter(raw)
    for key in NOTE_FIELDS:
        if key not in meta:
            raise ValueError("Missing required field: " + key)
    for field, allowed in ALLOWED.items():
        if meta[field] not in allowed:
            raise ValueError("Invalid enum: " + field)
    for field in ("title",):
        if not isinstance(meta[field], str) or not meta[field].strip():
            raise ValueError("Invalid title")
    for field in ("source_refs", "tags"):
        if not isinstance(meta[field], list) or not meta[field]:
            raise ValueError(field + " must be a nonempty list")
        if any(not isinstance(v, str) or not v.strip() for v in meta[field]):
            raise ValueError(field + " must contain nonblank strings")
    if "skill_candidate" in meta and not isinstance(meta["skill_candidate"], bool):
        raise ValueError("skill_candidate must be a YAML boolean")
    for heading in NOTE_HEADINGS:
        if f"## {heading}" not in raw:
            raise ValueError("Missing heading " + heading)
    return meta


class PortableSkillTests(unittest.TestCase):
    def test_skill_metadata_and_negative_routing(self):
        raw = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        meta = frontmatter(raw)
        self.assertEqual(set(meta), {"name", "description"})
        self.assertEqual(meta["name"], "wiki-knowledge-builder")
        self.assertIsInstance(meta["description"], str)
        self.assertGreater(len(meta["description"]), 20)
        self.assertLess(len(meta["description"]), 1024)
        for token in ("KEEP", "HOLD", "SKIP", "skill_candidate", "not", "agent"):
            self.assertIn(token.lower(), raw.lower())

    def test_all_relative_references_exist(self):
        required = (
            "references/decision-evidence.md", "references/output-contract.md",
            "references/acceptance-matrix.md", "references/source-manifest.md",
            "assets/knowledge-note.template.md", "assets/hold-outline.template.md",
            "adapters/chatgpt-web.md", "examples/value-over-source.example.md",
        )
        for rel in required:
            self.assertTrue((ROOT / rel).is_file(), rel)
        for doc in ROOT.rglob("*.md"):
            text = doc.read_text(encoding="utf-8")
            for url in re.findall(r"\]\(([^)]+)\)", text):
                if url.startswith(("http:", "https:", "#")):
                    continue
                path = (doc.parent / url.split("#", 1)[0]).resolve()
                self.assertTrue(path.is_file(), f"{doc}: unresolved {url}")

    def test_note_template_yaml_parses_and_has_required_sections(self):
        raw = (ROOT / "assets/knowledge-note.template.md").read_text(encoding="utf-8")
        meta = validate_note(raw)
        self.assertEqual(meta["knowledge_status"], "provisional")
        self.assertNotIn("skill_candidate", meta, "optional field must not be default")
        contract = (ROOT / "references/output-contract.md").read_text(encoding="utf-8")
        for term in NOTE_FIELDS + NOTE_HEADINGS:
            self.assertIn(term, contract)

    def test_existing_knowledge_example_is_valid(self):
        raw = (ROOT / "examples/value-over-source.example.md").read_text(encoding="utf-8")
        meta = validate_note(raw)
        self.assertEqual(meta["source_access"], "partial")
        self.assertEqual(meta["knowledge_status"], "provisional")

    def test_skill_candidate_optional_boolean_and_rejection(self):
        raw = (ROOT / "examples/value-over-source.example.md").read_text(encoding="utf-8")
        self.assertNotIn("skill_candidate", validate_note(raw))
        candidate = raw.replace("tags: [", "skill_candidate: true\ntags: [", 1)
        self.assertIs(validate_note(candidate)["skill_candidate"], True)
        invalid = candidate.replace("skill_candidate: true", 'skill_candidate: "true"', 1)
        with self.assertRaisesRegex(ValueError, "boolean"):
            validate_note(invalid)
        self.assertIn("repeated", (ROOT / "references/output-contract.md").read_text(encoding="utf-8").lower())

    def test_hold_outline_is_not_an_ingestion_note(self):
        raw = (ROOT / "assets/hold-outline.template.md").read_text(encoding="utf-8")
        self.assertIn("不建议摄入 Wiki", raw)
        self.assertIn("下一步核验", raw)
        self.assertFalse(raw.startswith("---\n"))
        with self.assertRaisesRegex(ValueError, "frontmatter"):
            validate_note(raw)

    def test_chatgpt_adapter_contract_and_no_auto_write(self):
        raw = (ROOT / "adapters/chatgpt-web.md").read_text(encoding="utf-8")
        for token in ("KEEP", "HOLD", "SKIP", "skill_candidate",
                      "knowledge_status", "source_access", "source_kind",
                      "reuse_scope", "source_refs", "待验证提纲"):
            self.assertIn(token, raw)
        for heading in NOTE_HEADINGS:
            self.assertIn(heading, raw)
        self.assertIn("不要自动修改", raw)

    def test_manifest_identifies_original_sources_without_claiming_storage(self):
        raw = (ROOT / "references/source-manifest.md").read_text(encoding="utf-8")
        for filename in ("wiki-knowledge-builder-v0.1-design.md",
                         "wiki-knowledge-builder-v0.1-chatgpt-prompt.md",
                         "wiki-knowledge-builder-v0.1-example.md"):
            self.assertIn(filename, raw)
        self.assertIn("SHA256", raw)
        self.assertIn("not copied into this public repository", raw)

if __name__ == "__main__":
    unittest.main()
