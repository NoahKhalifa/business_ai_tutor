"""OCR extractor — render image-only (scanned) pages and OCR them with Tesseract.

The other extractors read the PDF text layer. A scanned PDF has *no* text layer,
so they return nothing. This extractor finds those pages, renders each to a raster
image, and runs Tesseract (via pytesseract) to recover the text.

Dependencies (Tesseract binary + pytesseract + Pillow) are imported lazily so a
plain text PDF never needs them. If a scanned page exists but the dependencies are
missing, `extract()` raises `OcrUnavailable` with an install hint — the pipeline
catches it and records the situation in the front-matter instead of crashing.
"""
from typing import List, Optional

import fitz  # PyMuPDF

from .base import BaseExtractor, Block


class OcrUnavailable(RuntimeError):
    """Raised when a page needs OCR but the OCR toolchain is not installed."""


# A page with fewer than this many extractable characters is treated as a scan.
TEXT_LAYER_MIN_CHARS = 20
# Render DPI for OCR. 300 is the Tesseract sweet spot for body text.
OCR_DPI = 300


class OcrExtractor(BaseExtractor):
    """OCR the scanned (text-layer-less) pages of a PDF.

    Usage:
        ocr = OcrExtractor(pdf, lang="vie+eng")
        blocks = ocr.extract()      # OCRs only scanned pages
        ocr.ocr_info                # dict describing what happened (for front-matter)
    """

    def __init__(self, pdf_path, output_dir=None, lang: str = "vie+eng", dpi: int = OCR_DPI):
        super().__init__(pdf_path, output_dir)
        self.lang = lang
        self.dpi = dpi
        # Populated by extract(): {used, engine, language, pages} or {used: False, ...}.
        self.ocr_info: dict = {"used": False}

    # -- public -----------------------------------------------------------------

    def scanned_page_indices(self) -> List[int]:
        """1-based indices of pages that lack a usable text layer."""
        doc = fitz.open(self.pdf_path)
        try:
            scanned: List[int] = []
            for page_idx, page in enumerate(doc, start=1):
                text = page.get_text("text") or ""
                if len(text.strip()) < TEXT_LAYER_MIN_CHARS:
                    scanned.append(page_idx)
            return scanned
        finally:
            doc.close()

    def extract(self) -> List[Block]:
        scanned = self.scanned_page_indices()
        if not scanned:
            self.ocr_info = {"used": False}
            return []

        try:
            ocr_text = self._load_engine()
        except OcrUnavailable as exc:
            # Record that OCR was needed but couldn't run; let the pipeline decide.
            self.ocr_info = {
                "used": False,
                "needed": True,
                "scanned_pages": scanned,
                "reason": str(exc),
            }
            raise

        doc = fitz.open(self.pdf_path)
        out: List[Block] = []
        ocr_pages: List[int] = []
        try:
            for page_idx in scanned:
                page = doc[page_idx - 1]
                text = ocr_text(page).strip()
                if not text:
                    continue
                out.append(
                    Block(
                        type="text",
                        page=page_idx,
                        bbox=tuple(page.rect),
                        content=text,
                        metadata={"ocr": True},
                    )
                )
                ocr_pages.append(page_idx)
        finally:
            doc.close()

        self.ocr_info = {
            "used": bool(ocr_pages),
            "engine": "tesseract",
            "language": self.lang,
            "pages": ocr_pages,
            "scanned_pages": scanned,
        }
        return out

    # -- internals --------------------------------------------------------------

    def _load_engine(self):
        """Return a callable page -> ocr_text, or raise OcrUnavailable."""
        try:
            import pytesseract
            from PIL import Image
        except ImportError as exc:  # pragma: no cover - env dependent
            raise OcrUnavailable(
                "OCR cần 'pytesseract' và 'Pillow'. Cài: "
                "pip install pytesseract pillow"
            ) from exc

        import io

        # Probe the Tesseract binary early so the failure message is clear.
        try:
            pytesseract.get_tesseract_version()
        except Exception as exc:  # pragma: no cover - env dependent
            raise OcrUnavailable(
                "Không tìm thấy Tesseract binary. Cài Tesseract OCR (kèm gói "
                "ngôn ngữ 'vie') rồi thêm vào PATH, hoặc set "
                "pytesseract.pytesseract.tesseract_cmd. "
                "Windows: winget install UB-Mannheim.TesseractOCR"
            ) from exc

        zoom = self.dpi / 72.0
        matrix = fitz.Matrix(zoom, zoom)

        def ocr_text(page) -> str:
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            try:
                return pytesseract.image_to_string(img, lang=self.lang)
            except pytesseract.TesseractError as exc:
                raise OcrUnavailable(
                    f"Tesseract lỗi (thiếu gói ngôn ngữ '{self.lang}'?): {exc}"
                ) from exc

        return ocr_text


def detect_scanned_pages(pdf_path) -> List[int]:
    """Convenience: 1-based indices of scanned pages without constructing state."""
    return OcrExtractor(pdf_path).scanned_page_indices()
