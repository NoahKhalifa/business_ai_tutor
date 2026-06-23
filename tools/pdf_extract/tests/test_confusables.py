"""Pure regex/unit tests for the confusable flagger — no PDF needed."""
import unittest

from tools.pdf_extract.utils.confusables import (
    CONFUSABLE_PAIRS,
    flag_confusables,
)


class FlagConfusablesTests(unittest.TestCase):
    def test_flags_basic_pair(self):
        out, count = flag_confusables("môi trường vi mô")
        self.assertEqual(count, 1)
        self.assertIn("[VERIFY_OCR: vi/vĩ", out)

    def test_no_flag_when_word_part_of_larger_token(self):
        out, count = flag_confusables("violin")  # "vi" is substring
        self.assertEqual(count, 0)
        self.assertEqual(out, "violin")

    def test_multiple_words_in_one_string(self):
        text = "bán sỉ và lý thuyết quản lý"
        out, count = flag_confusables(text)
        self.assertEqual(count, 3)  # sỉ, lý, lý
        self.assertIn("[VERIFY_OCR: sỉ/sĩ", out)
        self.assertIn("[VERIFY_OCR: lý/ly", out)

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
        """Every key's partner must itself be a key (symmetric)."""
        for k, v in CONFUSABLE_PAIRS.items():
            self.assertIn(v, CONFUSABLE_PAIRS, f"{v} (partner of {k}) missing as key")

    def test_unicode_boundary_against_diacritic_neighbors(self):
        # "vĩ" must be flagged but "vĩnh" (different word containing vĩ) should not.
        out, count = flag_confusables("kế hoạch vĩ đại và sự vĩnh cửu")
        self.assertEqual(count, 1)
        self.assertIn("vĩ [VERIFY_OCR", out)
        self.assertNotIn("vĩnh [VERIFY_OCR", out)


if __name__ == "__main__":
    unittest.main()
