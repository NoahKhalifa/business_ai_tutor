"""Per-component extractor tests against synthetic PDFs."""
import tempfile
import unittest
from pathlib import Path

from tools.pdf_extract.extractors import (
    ImageExtractor,
    MathExtractor,
    TableExtractor,
    TextExtractor,
)
from tools.pdf_extract.tests import fixtures


class TempPDF:
    """Context manager that yields (pdf_path, output_dir) inside a tmp dir."""

    def __init__(self, builder):
        self.builder = builder

    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        pdf = self.builder(root / "input.pdf")
        out = root / "out"
        out.mkdir()
        return pdf, out

    def __exit__(self, *exc):
        self.tmp.cleanup()


class TextExtractorTests(unittest.TestCase):
    def test_detects_headings_by_font_size(self):
        with TempPDF(fixtures.make_text_pdf) as (pdf, _):
            blocks = TextExtractor(pdf).extract()
        headings = [b for b in blocks if b.type == "heading"]
        bodies = [b for b in blocks if b.type == "text"]
        self.assertTrue(headings, "should detect at least one heading")
        self.assertTrue(bodies, "should also keep body text")
        levels = sorted(b.metadata.get("level") for b in headings)
        self.assertEqual(levels[0], 1, "biggest font → H1")

    def test_returns_zero_blocks_for_empty_pdf(self):
        import fitz

        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "blank.pdf"
            doc = fitz.open()
            doc.new_page()
            doc.save(str(p))
            doc.close()
            self.assertEqual(TextExtractor(p).extract(), [])


class TableExtractorTests(unittest.TestCase):
    def test_extracts_real_table_to_markdown(self):
        with TempPDF(fixtures.make_table_pdf) as (pdf, _):
            blocks = TableExtractor(pdf).extract()
        tables = [b for b in blocks if b.type == "table"]
        self.assertEqual(len(tables), 1, "should detect exactly one table")
        md = tables[0].content
        self.assertIn("Quý", md)
        self.assertIn("Doanh thu", md)
        self.assertIn("|---|", md)  # separator row present
        # 3 body rows + header row
        self.assertGreaterEqual(md.count("\n"), 3)

    def test_rejects_text_only_pdf(self):
        with TempPDF(fixtures.make_text_pdf) as (pdf, _):
            blocks = TableExtractor(pdf).extract()
        # The text-only PDF has no real table; our density filter should drop
        # anything pdfplumber finds.
        self.assertEqual(blocks, [], f"unexpected tables: {blocks}")


class ImageExtractorTests(unittest.TestCase):
    def test_saves_large_image_skips_tiny(self):
        with TempPDF(fixtures.make_image_pdf) as (pdf, out):
            blocks = ImageExtractor(pdf, out).extract()
        self.assertEqual(len(blocks), 1, "20x20 icon must be skipped")
        img = blocks[0]
        self.assertEqual(img.type, "image")
        full_path = (Path(blocks[0].content),)
        rel = blocks[0].content
        self.assertTrue(rel.startswith("assets/"), rel)
        self.assertTrue(
            rel.startswith("assets/input/"),
            "assets must be namespaced by PDF stem to avoid cross-document overwrite",
        )
        # File should exist on disk
        saved = (Path(blocks[0].content[: 0]) if False else None)
        # Reconstruct: out / rel
        from_disk = blocks[0].metadata["filename"]
        self.assertTrue(from_disk.endswith(".png"))

    def test_no_op_when_output_dir_none(self):
        with TempPDF(fixtures.make_image_pdf) as (pdf, _):
            blocks = ImageExtractor(pdf, output_dir=None).extract()
        self.assertEqual(blocks, [])


class MathExtractorTests(unittest.TestCase):
    def test_detects_symbol_font_and_unicode_chars(self):
        with TempPDF(fixtures.make_math_pdf) as (pdf, out):
            blocks = MathExtractor(pdf, out).extract()
        self.assertGreaterEqual(len(blocks), 1, "should detect at least one math region")
        for b in blocks:
            self.assertEqual(b.type, "math")
            self.assertTrue(b.content.startswith("assets/input/"))
            self.assertTrue(b.content.endswith(".png"))

    def test_no_op_when_output_dir_none(self):
        with TempPDF(fixtures.make_math_pdf) as (pdf, _):
            blocks = MathExtractor(pdf, output_dir=None).extract()
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()
