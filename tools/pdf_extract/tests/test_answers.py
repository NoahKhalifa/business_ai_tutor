"""Tests for answer-mark flagging & empty-page removal — pure text, no PDF."""
import unittest

from tools.pdf_extract.utils.answers import flag_answer_marks, remove_empty_pages


class EmptyPageTests(unittest.TestCase):
    def test_drops_marker_and_page_header(self):
        body = "x\n\n<!-- page 14 -->\n\n[OCR_EMPTY_PAGE]"
        self.assertNotIn("OCR_EMPTY_PAGE", remove_empty_pages(body))
        self.assertNotIn("page 14", remove_empty_pages(body))

    def test_keeps_real_content(self):
        body = "<!-- page 1 -->\nNội dung thật"
        self.assertIn("Nội dung thật", remove_empty_pages(body))
        self.assertIn("page 1", remove_empty_pages(body))


class AnswerMarkTests(unittest.TestCase):
    def test_flags_leading_garble(self):
        out, n = flag_answer_marks("© AH. XanhXimông, R. Oen")
        self.assertEqual(n, 1)
        self.assertIn("đáp án được khoanh", out)

    def test_flags_O_circle_combo(self):
        out, n = flag_answer_marks("O ©. chủ nghĩa tư bản")
        self.assertEqual(n, 1)

    def test_strips_trailing_plus_and_flags(self):
        out, n = flag_answer_marks("- **C.** Chống đánh đập, cúp phạt. +")
        self.assertEqual(n, 1)
        self.assertNotIn(" +", out.split("[VERIFY")[0].rstrip()[-2:])
        self.assertIn("đáp án được khoanh", out)

    def test_lone_plus_line_removed(self):
        out, n = flag_answer_marks("a\n+\nb")
        self.assertEqual(out, "a\nb")

    def test_clean_option_untouched(self):
        out, n = flag_answer_marks("- **A.** Một phương án bình thường")
        self.assertEqual(n, 0)
        self.assertEqual(out, "- **A.** Một phương án bình thường")

    def test_continuation_line_not_flagged(self):
        # "O chủ nghĩa..." is a wrapped continuation, not a marked option.
        out, n = flag_answer_marks("O chủ nghĩa tư bản; không phát hiện ra")
        self.assertEqual(n, 0)

    def test_idempotent(self):
        out1, _ = flag_answer_marks("© AH. XanhXimông")
        out2, n2 = flag_answer_marks(out1)
        self.assertEqual(n2, 0)
        self.assertEqual(out1, out2)


if __name__ == "__main__":
    unittest.main()
