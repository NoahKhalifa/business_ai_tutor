"""Math extractor — heuristic detection of math regions, cropped to PNG.

Heuristic: a span is math if either
  (a) its font name contains one of MATH_FONT_KEYWORDS, or
  (b) its text contains a Unicode math symbol from MATH_CHARS.

Adjacent math spans on the same line are merged into a single region,
then rendered to PNG at MATH_DPI. Each region becomes a Block(type="math").
"""
from typing import List, Tuple

import fitz  # PyMuPDF

from .base import BaseExtractor, Block

MATH_FONT_KEYWORDS = (
    "math",
    "symbol",
    "cmsy",
    "cmmi",
    "cmex",
    "cmr10",
    "stix",
    "mathjax",
    "esint",
    "rsfs",
    "msam",
    "msbm",
)

MATH_CHARS = set(
    "∫∮∑∏√∛∜≤≥≠≈≡∝∞∂∇αβγδεζηθικλμνξοπρστυφχψω"
    "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    "ℝℕℤℚℂℵ"
    "∈∉∋⊂⊆⊃⊇∪∩∅"
    "∀∃∄→←↔⇒⇐⇔⊥∥"
    "±×÷∘⊕⊗⊙"
    "ƒ⌈⌉⌊⌋"
)


class MathExtractor(BaseExtractor):
    PADDING = 4
    MATH_DPI = 200
    SAME_LINE_TOL = 6
    HORIZ_GAP_TOL = 24

    def extract(self) -> List[Block]:
        if self.output_dir is None:
            return []
        assets_dir = self.output_dir / "assets" / self.pdf_path.stem
        assets_dir.mkdir(parents=True, exist_ok=True)

        doc = fitz.open(self.pdf_path)
        out: List[Block] = []
        eq_counter = 0
        try:
            for page_idx, page in enumerate(doc, start=1):
                spans = self._collect_math_spans(page)
                regions = self._merge_spans(spans)
                for region in regions:
                    eq_counter += 1
                    block = self._render_region(
                        page, page_idx, eq_counter, region, assets_dir
                    )
                    if block is not None:
                        out.append(block)
            return out
        finally:
            doc.close()

    def _collect_math_spans(self, page) -> List[Tuple[float, float, float, float]]:
        spans: List[Tuple[float, float, float, float]] = []
        for blk in page.get_text("dict").get("blocks", []):
            if blk.get("type") != 0:
                continue
            for line in blk.get("lines", []):
                for span in line.get("spans", []):
                    if self._is_math(span):
                        spans.append(tuple(span["bbox"]))
        return spans

    @staticmethod
    def _is_math(span) -> bool:
        font = str(span.get("font", "")).lower()
        if any(k in font for k in MATH_FONT_KEYWORDS):
            return True
        text = span.get("text", "") or ""
        return any(ch in MATH_CHARS for ch in text)

    def _merge_spans(self, spans):
        if not spans:
            return []
        spans = sorted(spans, key=lambda b: (round(b[1] / self.SAME_LINE_TOL), b[0]))
        merged = []
        current = list(spans[0])
        for bb in spans[1:]:
            same_line = abs(bb[1] - current[1]) <= self.SAME_LINE_TOL
            close_horiz = bb[0] - current[2] <= self.HORIZ_GAP_TOL
            if same_line and close_horiz:
                current[0] = min(current[0], bb[0])
                current[1] = min(current[1], bb[1])
                current[2] = max(current[2], bb[2])
                current[3] = max(current[3], bb[3])
            else:
                merged.append(tuple(current))
                current = list(bb)
        merged.append(tuple(current))
        return merged

    def _render_region(self, page, page_idx, counter, region, assets_dir):
        clip = fitz.Rect(
            region[0] - self.PADDING,
            region[1] - self.PADDING,
            region[2] + self.PADDING,
            region[3] + self.PADDING,
        )
        scale = self.MATH_DPI / 72.0
        try:
            pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=clip)
        except Exception:
            return None

        try:
            fname = f"page_{page_idx:03d}_eq_{counter:02d}.png"
            fpath = assets_dir / fname
            pix.save(str(fpath))
            rel = fpath.relative_to(self.output_dir).as_posix()
            return Block(
                type="math",
                page=page_idx,
                bbox=region,
                content=rel,
                metadata={"filename": fname},
            )
        finally:
            pix = None
