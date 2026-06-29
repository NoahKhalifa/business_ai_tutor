"""Pure regex/unit tests for the confusable flagger — no PDF needed."""
import unittest

from tools.pdf_extract.utils.confusables import (
    CONFUSABLE_PAIRS,
    flag_confusables,
    flag_duplicate_options,
    strip_existing_flags,
)


class FlagConfusablesTests(unittest.TestCase):
    def test_flags_ambiguous_pair(self):
        # "vi mô"/"vĩ mô" is genuinely ambiguous → must stay flagged.
        out, count = flag_confusables("môi trường vi mô")
        self.assertEqual(count, 1)
        self.assertIn("[VERIFY_OCR: vi/vĩ", out)

    def test_no_flag_when_word_part_of_larger_token(self):
        out, count = flag_confusables("violin")  # "vi" is substring
        self.assertEqual(count, 0)
        self.assertEqual(out, "violin")

    def test_suppresses_unambiguous_collocations(self):
        # "lý thuyết", "quản lý", "sản xuất" are never the confusable partner.
        text = "lý thuyết quản lý về sản xuất"
        out, count = flag_confusables(text)
        self.assertEqual(count, 0, out)
        self.assertNotIn("[VERIFY_OCR", out)

    def test_flags_only_residual_ambiguous_word(self):
        # sỉ (no safe neighbour here) flagged; lý thuyET / quản lý suppressed.
        text = "bán sỉ và lý thuyết quản lý"
        out, count = flag_confusables(text)
        self.assertEqual(count, 1)
        self.assertIn("[VERIFY_OCR: sỉ/sĩ", out)
        self.assertNotIn("lý [VERIFY_OCR", out)

    def test_already_flagged_word_is_skipped(self):
        text = "vi [VERIFY_OCR: vi/vĩ — check PDF trang 1] mô"
        out, count = flag_confusables(text)
        self.assertEqual(count, 0)

    def test_page_lookup_uses_html_marker(self):
        text = "<!-- page 7 -->\nyếu tố vi mô"
        out, count = flag_confusables(text)
        self.assertEqual(count, 1)
        self.assertIn("trang 7", out)

    def test_all_pairs_have_inverse(self):
        for k, v in CONFUSABLE_PAIRS.items():
            self.assertIn(v, CONFUSABLE_PAIRS, f"{v} (partner of {k}) missing as key")

    def test_unicode_boundary_against_diacritic_neighbors(self):
        # "vĩ mô" flagged (ambiguous); "vĩnh" (longer word) must not be touched.
        out, count = flag_confusables("kế hoạch vĩ mô và sự vĩnh cửu")
        self.assertEqual(count, 1)
        self.assertIn("vĩ [VERIFY_OCR", out)
        self.assertNotIn("vĩnh [VERIFY_OCR", out)

    def test_idempotent_rerun_adds_nothing(self):
        out1, _ = flag_confusables("môi trường vi mô")
        out2, count2 = flag_confusables(out1)
        self.assertEqual(count2, 0)
        self.assertEqual(out1, out2)

    def test_strip_existing_flags_round_trip(self):
        flagged, _ = flag_confusables("môi trường vi mô")
        self.assertEqual(strip_existing_flags(flagged), "môi trường vi mô")


class DuplicateOptionTests(unittest.TestCase):
    def _mcq(self, options):
        lines = ["### Câu 1", "Nội dung câu hỏi?"]
        for label, text in options:
            lines.append(f"- **{label}.** {text}")
        return "\n".join(lines) + "\n"

    def test_flags_identical_options(self):
        md = self._mcq([
            ("A", "lực lượng sản xuất"),
            ("B", "quan hệ sản xuất"),
            ("C", "lực lượng sản xuất"),  # dup of A (tone-only OCR slip elsewhere)
            ("D", "tư liệu sản xuất"),
        ])
        out, count = flag_duplicate_options(md)
        self.assertEqual(count, 1)
        self.assertIn("phương án trùng", out)
        self.assertIn("A", out.splitlines()[0])

    def test_no_flag_when_all_distinct(self):
        md = self._mcq([
            ("A", "của cải vật chất"),
            ("B", "lực lượng sản xuất"),
            ("C", "quan hệ sản xuất"),
            ("D", "tư liệu sản xuất"),
        ])
        out, count = flag_duplicate_options(md)
        self.assertEqual(count, 0)

    def test_diacritic_only_difference_counts_as_duplicate(self):
        # OCR dropped the tone: "sản" vs "san" normalise to the same key.
        md = self._mcq([
            ("A", "giai cấp tư sản"),
            ("B", "giai cấp tư san"),
            ("C", "giai cấp công nhân"),
            ("D", "giai cấp nông dân"),
        ])
        out, count = flag_duplicate_options(md)
        self.assertEqual(count, 1)

    def test_idempotent(self):
        md = self._mcq([
            ("A", "lực lượng sản xuất"),
            ("B", "lực lượng sản xuất"),
            ("C", "x khác biệt rõ ràng"),
            ("D", "y khác biệt rõ ràng"),
        ])
        out1, _ = flag_duplicate_options(md)
        out2, count2 = flag_duplicate_options(out1)
        self.assertEqual(count2, 0)
        self.assertEqual(out1, out2)


if __name__ == "__main__":
    unittest.main()
