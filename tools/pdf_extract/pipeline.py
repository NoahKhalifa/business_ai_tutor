"""Orchestrate the extractors: run each component, merge blocks, render markdown."""
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from .extractors.base import Block
from .extractors.images import ImageExtractor
from .extractors.math import MathExtractor
from .extractors.ocr import OcrExtractor, OcrUnavailable
from .extractors.tables import TableExtractor
from .extractors.text import TextExtractor
from .utils.confusables import flag_confusables, flag_duplicate_options
from .utils.frontmatter import build_frontmatter

DEFAULT_COMPONENTS: Tuple[str, ...] = ("text", "tables", "images", "math", "ocr")
DEFAULT_OCR_LANG = "vie+eng"


@dataclass
class ExtractResult:
    markdown_path: Path
    markdown: str
    blocks: List[Block]
    pages: int
    confusables_flagged: int
    ocr_info: dict


def extract_pdf(
    pdf_path: Path,
    output_dir: Optional[Path] = None,
    components: Iterable[str] = DEFAULT_COMPONENTS,
    flag_vn_confusables: bool = True,
    write_file: bool = True,
    ocr_lang: str = DEFAULT_OCR_LANG,
) -> ExtractResult:
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir) if output_dir else pdf_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    components = tuple(components)

    blocks: List[Block] = []
    if "text" in components:
        blocks.extend(TextExtractor(pdf_path).extract())
    if "tables" in components:
        blocks.extend(TableExtractor(pdf_path).extract())
    if "images" in components:
        blocks.extend(ImageExtractor(pdf_path, output_dir).extract())
    if "math" in components:
        blocks.extend(MathExtractor(pdf_path, output_dir).extract())

    ocr_info: dict = {"used": False}
    if "ocr" in components:
        ocr = OcrExtractor(pdf_path, output_dir, lang=ocr_lang)
        try:
            blocks.extend(ocr.extract())
        except OcrUnavailable:
            pass  # ocr.ocr_info records that OCR was needed but unavailable
        ocr_info = ocr.ocr_info

    blocks = _drop_overlapping_text(blocks)
    blocks.sort(key=lambda b: (b.page, b.bbox[1], b.bbox[0]))

    md_body = render_markdown(blocks)

    flagged = 0
    if flag_vn_confusables:
        md_body, flagged = flag_confusables(md_body)
        md_body, dup_flagged = flag_duplicate_options(md_body)
        flagged += dup_flagged

    pages = max((b.page for b in blocks), default=0)
    fm = build_frontmatter(
        pdf_path=pdf_path,
        pages=pages,
        confusables_flagged=flagged,
        ocr_info=ocr_info,
    )
    full_md = fm + "\n" + md_body + "\n"

    md_path = output_dir / (pdf_path.stem + ".md")
    if write_file:
        md_path.write_text(full_md, encoding="utf-8")

    return ExtractResult(
        markdown_path=md_path,
        markdown=full_md,
        blocks=blocks,
        pages=pages,
        confusables_flagged=flagged,
        ocr_info=ocr_info,
    )


def render_markdown(blocks: List[Block]) -> str:
    """Render an ordered Block list into a single markdown string.

    Inserts `<!-- page N -->` markers at page transitions so the confusables
    flagger can attribute pages.
    """
    parts: List[str] = []
    current_page = 0
    for blk in blocks:
        if blk.page != current_page:
            parts.append(f"<!-- page {blk.page} -->")
            current_page = blk.page
        parts.append(_render_one(blk))
    return "\n\n".join(p for p in parts if p)


def _render_one(blk: Block) -> str:
    if blk.type == "heading":
        level = max(1, min(6, int(blk.metadata.get("level", 2))))
        return "#" * level + " " + blk.content
    if blk.type == "text":
        return blk.content
    if blk.type == "table":
        return blk.content
    if blk.type == "image":
        return f"![Hình trang {blk.page}]({blk.content})"
    if blk.type == "math":
        return f"![Công thức trang {blk.page}]({blk.content})"
    return ""


def _drop_overlapping_text(blocks: List[Block]) -> List[Block]:
    """Remove text/heading blocks fully contained in a table or math region.

    pdfplumber and PyMuPDF both report the inner cells/spans as text; without
    this filter we'd emit the table contents twice.
    """
    containers = [b for b in blocks if b.type in ("table", "math")]
    if not containers:
        return blocks
    kept: List[Block] = []
    for b in blocks:
        if b.type in ("text", "heading") and any(
            b.page == c.page and _contained(b.bbox, c.bbox) for c in containers
        ):
            continue
        kept.append(b)
    return kept


def _contained(inner, outer, tol: float = 2.0) -> bool:
    return (
        inner[0] >= outer[0] - tol
        and inner[1] >= outer[1] - tol
        and inner[2] <= outer[2] + tol
        and inner[3] <= outer[3] + tol
    )
