"""Text & heading extractor — uses PyMuPDF span info to detect headings by font size."""
from typing import List

import fitz  # PyMuPDF

from .base import BaseExtractor, Block


class TextExtractor(BaseExtractor):
    """Extract text blocks with heading-level inference.

    Heading detection: body size = median font size across document.
    A block is a heading if its largest span size exceeds body * threshold.
    """

    H1_RATIO = 1.5
    H2_RATIO = 1.25
    H3_RATIO = 1.10
    BOLD_FLAG = 16  # PyMuPDF span flag bit for bold

    def extract(self) -> List[Block]:
        doc = fitz.open(self.pdf_path)
        try:
            body_size = self._estimate_body_size(doc)
            blocks: List[Block] = []
            for page_idx, page in enumerate(doc, start=1):
                blocks.extend(self._extract_page(page, page_idx, body_size))
            return blocks
        finally:
            doc.close()

    def _estimate_body_size(self, doc) -> float:
        sizes: List[float] = []
        for page in doc:
            for blk in page.get_text("dict").get("blocks", []):
                if blk.get("type") != 0:
                    continue
                for line in blk.get("lines", []):
                    for span in line.get("spans", []):
                        sizes.append(float(span.get("size", 0)))
        if not sizes:
            return 10.0
        sizes.sort()
        return sizes[len(sizes) // 2]

    def _extract_page(self, page, page_idx: int, body_size: float) -> List[Block]:
        out: List[Block] = []
        for blk in page.get_text("dict").get("blocks", []):
            if blk.get("type") != 0:
                continue
            text_parts: List[str] = []
            max_size = 0.0
            has_bold = False
            for line in blk.get("lines", []):
                line_parts = []
                for span in line.get("spans", []):
                    line_parts.append(span.get("text", ""))
                    max_size = max(max_size, float(span.get("size", 0)))
                    if int(span.get("flags", 0)) & self.BOLD_FLAG:
                        has_bold = True
                text_parts.append("".join(line_parts))
            text = "\n".join(p.strip() for p in text_parts if p.strip()).strip()
            if not text:
                continue

            level = self._heading_level(max_size, body_size, has_bold)
            if level:
                out.append(
                    Block(
                        type="heading",
                        page=page_idx,
                        bbox=tuple(blk["bbox"]),
                        content=text.replace("\n", " "),
                        metadata={"level": level},
                    )
                )
            else:
                out.append(
                    Block(
                        type="text",
                        page=page_idx,
                        bbox=tuple(blk["bbox"]),
                        content=text,
                    )
                )
        return out

    def _heading_level(self, max_size: float, body_size: float, has_bold: bool) -> int:
        if body_size <= 0:
            return 0
        ratio = max_size / body_size
        if ratio >= self.H1_RATIO:
            return 1
        if ratio >= self.H2_RATIO:
            return 2
        if ratio >= self.H3_RATIO and has_bold:
            return 3
        return 0
