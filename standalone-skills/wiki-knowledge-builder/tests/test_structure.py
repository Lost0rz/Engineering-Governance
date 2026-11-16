"""Portable independent Skill tests. Run from any copied Skill root (PyYAML test-only)."""
from pathlib import Path
import re
import subprocess
import sys
import unittest
import importlib.util

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


VALIDATOR_PATH = ROOT / "scripts/validate_note.py"
spec = importlib.util.spec_from_file_location("wiki_note_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
frontmatter = validator.frontmatter
validate_note = validator.validate_note


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
        meta = validate_note(raw, template=True)
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

    def test_format_validator_rejects_non_date_and_empty_evidence(self):
        source = (ROOT / "examples/value-over-source.example.md").read_text(encoding="utf-8")
        self.assertTrue(validate_note(source))
        for bad_date in ("NOT_A_REAL_DATE", "2026-02-30", "2026-13-09"):
            bad = source.replace("created: 2026-11-16", "created: " + bad_date, 1)
            with self.subTest(date=bad_date), self.assertRaises(ValueError):
                validate_note(bad)
        no_evidence = source.replace(
            "## 证据与来源\n\n- [E1]",
            "## 证据与来源\n\n内容暂缺\n\n## 占位段落\n\n- [E1]", 1,
        )
        with self.assertRaisesRegex(ValueError, "evidence"):
            validate_note(no_evidence)
        bare_evidence = re.sub(r"(?m)^- \[E[12]\].*$", "- [E1] ", source)
        # An empty evidence section must fail regardless of other headings.
        with self.assertRaisesRegex(ValueError, "evidence"):
            validate_note(bare_evidence)

    def test_manual_validator_is_read_only_and_reports_errors(self):
        from hashlib import sha256
        example = ROOT / "examples/value-over-source.example.md"
        before = sha256(example.read_bytes()).digest()
        result = subprocess.run([sys.executable, str(VALIDATOR_PATH), str(example)],
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("NOTE_FORMAT_PASS", result.stdout)
        self.assertEqual(sha256(example.read_bytes()).digest(), before)

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
