"""Structure-only traceability regression fixtures. NOT truth/depth tests."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("wkb_evidence_check", SCRIPTS / "check_traceability.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class EvidenceLinkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = (ROOT / "examples/value-over-source.example.md").read_text(encoding="utf-8")

    def test_example_and_cli_have_structural_evidence_pass(self):
        self.assertEqual(checker.check_traceability(self.example),
                         {"evidence_count": 2, "source_count": 1})
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "note.md"
            p.write_text(self.example, encoding="utf-8")
            original = p.read_bytes()
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "check_traceability.py"), str(p)],
                capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("EVIDENCE_STRUCTURE_PASS", result.stdout)
            self.assertNotIn("CONTENT_PASS", result.stdout)
            self.assertEqual(p.read_bytes(), original)

    def test_multiple_real_source_indices(self):
        note = self.example.replace(
            "tags: [",
            '  - "2026-11-16 用户提供的网页提示词原始材料"\ntags: [', 1
        ).replace("[E2] [S1]", "[E2] [S1,S2]", 1)
        self.assertEqual(checker.check_traceability(note)["source_count"], 2)

    def test_missing_out_of_range_or_duplicate_source_marker(self):
        for bad in (
            self.example.replace("[E1] [S1]", "[E1]", 1),
            self.example.replace("[E1] [S1]", "[E1] [S2]", 1),
            self.example.replace("[E1] [S1]", "[E1] [S1,S1]", 1),
        ):
            with self.subTest(bad=bad[:170]), self.assertRaisesRegex(ValueError, "source"):
                checker.check_traceability(bad)

    def test_duplicate_skipped_and_orphan_evidence_identifiers(self):
        for bad in (
            self.example.replace("[E2] [S1]", "[E1] [S1]", 1),
            self.example.replace("[E2] [S1]", "[E3] [S1]", 1),
            self.example.replace(
                "## 核心结论\n", "## 核心结论\n\n参见 [E99]。\n", 1,
            ),
        ):
            with self.subTest(bad=bad[-140:]), self.assertRaisesRegex(ValueError, "Evidence IDs|Orphan"):
                checker.check_traceability(bad)

    def test_unlinked_source_and_unfilled_evidence(self):
        unused = self.example.replace(
            "tags: [", '  - "2026-11-16 unrelated documentation"\ntags: [', 1
        )
        with self.assertRaisesRegex(ValueError, "Unlinked"):
            checker.check_traceability(unused)
        for placeholder in ("待补充", "待核查", "TODO", "placeholder"):
            bad = self.example.replace("2026-11-16 用户提供的设计材料", placeholder, 1)
            with self.subTest(placeholder=placeholder), self.assertRaisesRegex(ValueError, "placeholder"):
                checker.check_traceability(bad)

    def test_missing_claim_or_evidence_grade(self):
        for bad in (
            self.example.replace(
                " — 讨论决策", " — ", 1,
            ),
            self.example.replace(" — 讨论决策", " — 完成", 1),
        ):
            with self.assertRaises(ValueError):
                checker.check_traceability(bad)

    def test_visible_inline_code_example_is_not_an_evidence_reference(self):
        note = self.example.replace(
            "## 原理、取舍与经验\n",
            "## 原理、取舍与经验\n\n编号 `[E99]` 只是语法示例，不是引用。\n\n", 1)
        self.assertEqual(checker.check_traceability(note)["evidence_count"], 2)

    def test_indented_fake_evidence_and_html_comment_are_rejected(self):
        indented = self.example.replace("- [E1] [S1]", "    - [E1] [S1]", 1)
        with self.assertRaises(ValueError):
            checker.check_traceability(indented)
        before, body = self.example.split("\n---\n", 1)
        hidden = before + "\n---\n\n<!--\n" + body + "\n-->\n"
        with self.assertRaises(ValueError):
            checker.check_traceability(hidden)

    def test_source_placeholder_and_extra_heading_fail(self):
        loc = "2026-11-16 LLM Wiki 设计讨论：按内容价值与标准化输出组织，而非按 GitHub、聊天、Agent 来源分类"
        for bad in ("TODO", "TBD", "待补充"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                checker.check_traceability(self.example.replace(loc, bad, 1))
        extra = self.example.replace(
            "## 关联与原始入口\n",
            "## 非规范 H2\n\n这是额外章节。\n\n## 关联与原始入口\n", 1)
        with self.assertRaises(ValueError):
            checker.check_traceability(extra)

    def test_windows_style_newlines_pass(self):
        self.assertEqual(checker.check_traceability(
            self.example.replace("\n", "\r\n"))["evidence_count"], 2)

    def test_literal_todo_filename_in_real_source_locator_is_not_a_placeholder(self):
        note = self.example.replace(
            "2026-11-16 LLM Wiki 设计讨论：按内容价值与标准化输出组织，而非按 GitHub、聊天、Agent 来源分类",
            "https://github.com/org/todo-tools/blob/main/TODO.md",
            1,
        ).replace(
            "[E1] [S1] 2026-11-16 用户提供的设计材料",
            "[E1] [S1] src/TODO.md",
            1,
        )
        self.assertEqual(checker.check_traceability(note)["source_count"], 1)

    def test_filename_todo_and_todo_topic_are_not_missing_placeholders(self):
        note = self.example.replace(
            "[E1] [S1] 2026-11-16 用户提供的设计材料",
            "[E1] [S1] TODO.md", 1).replace(
            "记录按内容价值而非来源平台组织 Skill 的设计选择",
            "记录 TODO 事项与实际工具行为", 1)
        self.assertEqual(checker.check_traceability(note)["evidence_count"], 2)

    def test_quoted_source_e1_does_not_satisfy_required_evidence(self):
        note = self.example.replace("- [E1] [S1]", "> - [E1] [S1]", 1)
        with self.assertRaises(ValueError):
            checker.check_traceability(note)

    def test_blockquote_and_escaped_evidence_examples_are_not_orphans(self):
        for snippet in ("> 原文中使用 [E99] 编号，仅作为引文示例。",
                        r"字面量 \[E99] 只是技术文档示例。"):
            with self.subTest(snippet=snippet):
                note = self.example.replace(
                    "## 原理、取舍与经验\n",
                    "## 原理、取舍与经验\n\n" + snippet + "\n\n", 1)
                self.assertEqual(checker.check_traceability(note)["evidence_count"], 2)

    def test_negated_or_ambiguous_grade_is_rejected(self):
        for bogus in ("未测试已执行，仅为设想", "并非源码已检查",
                      "未验证的推断", "尚未测试已执行"):
            with self.subTest(bogus=bogus):
                note = self.example.replace(
                    " — 讨论决策；不等于已经实际部署验证。",
                    " — " + bogus, 1)
                with self.assertRaisesRegex(ValueError, "grade"):
                    checker.check_traceability(note)

    def test_exact_grade_with_explanation_remains_valid(self):
        self.assertEqual(checker.check_traceability(self.example)["evidence_count"], 2)

    def test_realistic_chinese_full_stop_evidence_grades(self):
        # Prior Crawl4AI report generated evidence lines ending in 。
        # Retain canonical exact grade matching while allowing final punctuation.
        for label in ("源码已检查。", "讨论决策。", "来源声称。",
                      "测试已执行。", "文件声明。", "源码已检查.",
                      "来源声称；仅来自官方文档。"):
            with self.subTest(label=label):
                note = self.example.replace(
                    " — 讨论决策；不等于已经实际部署验证。",
                    " — " + label, 1)
                self.assertEqual(checker.check_traceability(note)["evidence_count"], 2)

    def test_chinese_full_stop_does_not_legalize_misleading_grade(self):
        for invalid in ("未测试已执行。", "并非源码已检查。", "尚未验证的推断。",
                        "源码已检查但未核对。", "来源声称，不等于证实。",
                        "源码已检查。。"):
            with self.subTest(label=invalid):
                note = self.example.replace(
                    " — 讨论决策；不等于已经实际部署验证。",
                    " — " + invalid, 1)
                with self.assertRaisesRegex(ValueError, "grade"):
                    checker.check_traceability(note)

    def test_multiple_realistic_crawl4ai_style_evidence_lists(self):
        # Public, source-free regression of the previously failing output style:
        # 4, 5, 6 entries with a trailing Chinese full stop in every grade.
        base = self.example
        baseline_e1 = "- [E1] [S1] 2026-11-16 用户提供的设计材料 — 记录按内容价值而非来源平台组织 Skill 的设计选择 — 讨论决策；不等于已经实际部署验证。"
        baseline_e2 = "- [E2] [S1] v0.1 设计材料和网页提示词 — 约定 KEEP/HOLD/SKIP 与 Canonical Markdown 结构 — 文件声明；不代表真实测试或 Wiki 摄入通过。"
        assert baseline_e1 in base and baseline_e2 in base
        for count in (4, 5, 6):
            with self.subTest(count=count):
                new_lines = [
                    f"- [E{i}] [S1] crawl4ai/example.py:{i} — 已检查参数与返回路径 — "
                    + ("源码已检查。" if i < count else "来源声称。")
                    for i in range(1, count + 1)
                ]
                note = base.replace(baseline_e1 + "\n" + baseline_e2,
                                    "\n".join(new_lines), 1)
                self.assertEqual(checker.check_traceability(note),
                                 {"evidence_count": count, "source_count": 1})

    def test_code_fenced_fake_sources_do_not_satisfy_required_mappings(self):
        bad = self.example.replace(
            "## 原理、取舍与经验\n",
            "## 原理、取舍与经验\n\n```markdown\n"
            "- [E99] [S99] fake evidence — claim — 代码已检查\n```\n\n", 1)
        self.assertEqual(checker.check_traceability(bad)["evidence_count"], 2)

if __name__ == "__main__":
    unittest.main()
