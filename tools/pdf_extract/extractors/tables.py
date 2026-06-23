"""Table extractor — uses pdfplumber's heuristic table detection."""
from typing import List

import pdfplumber

from .base import BaseExtractor, Block


class TableExtractor(BaseExtractor):
    """Detect tables and convert each to a Markdown table block.

    The first row is treated as header. Missing cells become empty strings.
    """

    MIN_COLS = 2
    MIN_NON_EMPTY_CELLS = 4
    MIN_DENSITY = 0.4  # fraction of non-empty cells

    def extract(self) -> List[Block]:
        out: List[Block] = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_idx, page in enumerate(pdf.pages, start=1):
                for table in page.find_tables() or []:
                    data = table.extract()
                    if not self._looks_like_real_table(data):
                        continue
                    md = self._rows_to_markdown(data)
                    if not md:
                        continue
                    out.append(
                        Block(
                            type="table",
                            page=page_idx,
                            bbox=tuple(table.bbox),
                            content=md,
                            metadata={"rows": len(data), "cols": len(data[0])},
                        )
                    )
        return out

    @classmethod
    def _looks_like_real_table(cls, data) -> bool:
        if not data or not data[0]:
            return False
        cols = max(len(r) for r in data)
        if cols < cls.MIN_COLS:
            return False
        total = sum(len(r) for r in data)
        non_empty = sum(1 for r in data for c in r if c and str(c).strip())
        if non_empty < cls.MIN_NON_EMPTY_CELLS:
            return False
        return (non_empty / max(total, 1)) >= cls.MIN_DENSITY

    @staticmethod
    def _clean(cell) -> str:
        if cell is None:
            return ""
        return str(cell).replace("\n", " ").replace("|", "\\|").strip()

    @classmethod
    def _rows_to_markdown(cls, rows) -> str:
        header = rows[0]
        width = max(len(r) for r in rows)
        # Normalize widths
        norm = [list(r) + [""] * (width - len(r)) for r in rows]
        header_cells = [cls._clean(c) for c in norm[0]]
        if not any(header_cells):
            # Fall back to generic headers when first row is blank
            header_cells = [f"Col {i + 1}" for i in range(width)]
            body_rows = norm
        else:
            body_rows = norm[1:]

        lines = [
            "| " + " | ".join(header_cells) + " |",
            "|" + "|".join(["---"] * width) + "|",
        ]
        for row in body_rows:
            lines.append("| " + " | ".join(cls._clean(c) for c in row[:width]) + " |")
        return "\n".join(lines)
