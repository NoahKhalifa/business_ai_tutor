"""OCR extractor tests — env-independent (no real Tesseract needed; engine mocked)."""
import tempfile
import unittest
from pathlib import Path

from tools.pdf_extract.extractors.ocr import (
    OcrExtractor,
    OcrUnavailable,
    prepare_image_for_ocr,
)
from tools.pdf_extract.pipeline import extract_pdf
from tools.pdf_extract.tests import fixtures


class ScannedDetectionTests(unittest.TestCase):
    def test_detects_image_only_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_scanned_pdf(Path(tmp) / "scan.pdf", pages=2)
            self.assertEqual(OcrExtractor(pdf).scanned_page_indices(), [1, 2])

    def test_text_pdf_has_no_scanned_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_text_pdf(Path(tmp) / "text.pdf")
            self.assertEqual(OcrExtractor(pdf).scanned_page_indices(), [])


class OcrEngineTests(unittest.TestCase):
    def test_preprocess_recovers_light_gray_text(self):
        from PIL import Image

        image = Image.new("L", (2, 1))
        image.putdata([220, 255])
        processed = prepare_image_for_ocr(image)
        self.assertEqual(
            [processed.getpixel((0, 0)), processed.getpixel((1, 0))],
            [0, 255],
        )

    def test_extract_with_fake_engine_sets_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_scanned_pdf(Path(tmp) / "scan.pdf", pages=1)
            ocr = OcrExtractor(pdf, lang="vie+eng")
            ocr._load_engine = lambda: (lambda page: "Câu 1: nội dung OCR.")
            blocks = ocr.extract()
        self.assertEqual(len(blocks), 1)
        self.assertTrue(blocks[0].metadata.get("ocr"))
        self.assertTrue(ocr.ocr_info["used"])
        self.assertEqual(ocr.ocr_info["engine"], "tesseract")
        self.assertEqual(ocr.ocr_info["pages"], [1])

    def test_extract_raises_and_records_when_engine_unavailable(self):
        def boom():
            raise OcrUnavailable("no tesseract")

        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_scanned_pdf(Path(tmp) / "scan.pdf", pages=1)
            ocr = OcrExtractor(pdf)
            ocr._load_engine = boom
            with self.assertRaises(OcrUnavailable):
                ocr.extract()
        self.assertFalse(ocr.ocr_info["used"])
        self.assertTrue(ocr.ocr_info["needed"])
        self.assertEqual(ocr.ocr_info["scanned_pages"], [1])


class PipelineOcrTests(unittest.TestCase):
    def test_pipeline_degrades_gracefully_without_engine(self):
        # No Tesseract in CI → scanned PDF must not crash the pipeline.
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_scanned_pdf(Path(tmp) / "scan.pdf", pages=1)
            result = extract_pdf(pdf, output_dir=Path(tmp) / "out")
        # Either it OCR'd (engine present) or recorded that OCR is needed.
        if not result.ocr_info.get("used"):
            self.assertTrue(result.ocr_info.get("needed"))
            self.assertIn("ocr_needed: true", result.markdown)

    def test_text_pdf_never_needs_ocr(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = fixtures.make_text_pdf(Path(tmp) / "text.pdf")
            result = extract_pdf(pdf, output_dir=Path(tmp) / "out")
        self.assertFalse(result.ocr_info.get("used"))
        self.assertNotIn("ocr_used: true", result.markdown)


if __name__ == "__main__":
    unittest.main()
