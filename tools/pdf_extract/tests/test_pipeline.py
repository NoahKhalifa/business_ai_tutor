"""End-to-end pipeline tests: extract_pdf + cache + confusables + selective components."""
import tempfile
import unittest
from pathlib import Path

from tools.pdf_extract.pipeline import extract_pdf
from tools.pdf_extract.utils.frontmatter import read_existing_hash
from tools.pdf_extract.utils.hash import sha256_file
from tools.pdf_extract.tests import fixtures


class PipelineTests(unittest.TestCase):
    def test_combined_pdf_emits_all_block_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_combined_pdf(Path(tmp) / "combined.pdf")
            result = extract_pdf(pdf, output_dir=Path(tmp) / "out")
            types = {b.type for b in result.blocks}
            self.assertIn("heading", types)
            self.assertIn("text", types)
            self.assertIn("table", types)
            self.assertIn("image", types)
            self.assertEqual(result.pages, 2)
            sha = sha256_file(pdf)
            self.assertIn(f"sha256:{sha}", result.markdown)

    def test_selective_components_run_only_requested(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_combined_pdf(Path(tmp) / "combined.pdf")
            result = extract_pdf(
                pdf, output_dir=Path(tmp) / "out",
                components=("text",),  # only text/heading
            )
        types = {b.type for b in result.blocks}
        self.assertTrue(types.issubset({"text", "heading"}), f"got: {types}")

    def test_confusables_flagging_can_be_disabled(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_confusable_pdf(Path(tmp) / "vn.pdf")

            with_flags = extract_pdf(
                pdf, output_dir=Path(tmp) / "with", flag_vn_confusables=True
            )
            without = extract_pdf(
                pdf, output_dir=Path(tmp) / "without", flag_vn_confusables=False
            )

        self.assertGreater(with_flags.confusables_flagged, 0)
        self.assertEqual(without.confusables_flagged, 0)
        self.assertNotIn("[VERIFY_OCR", without.markdown)
        self.assertIn("[VERIFY_OCR", with_flags.markdown)

    def test_frontmatter_hash_round_trips(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_text_pdf(Path(tmp) / "in.pdf")
            out = Path(tmp) / "out"
            result = extract_pdf(pdf, output_dir=out)
            recovered = read_existing_hash(result.markdown_path)
            self.assertEqual(recovered, sha256_file(pdf))


if __name__ == "__main__":
    unittest.main()
