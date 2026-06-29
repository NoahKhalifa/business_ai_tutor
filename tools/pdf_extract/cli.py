"""CLI: python -m tools.pdf_extract <pdf|folder> [-o OUT] [--components ...] [--force]."""
import argparse
import sys
from pathlib import Path
from typing import List, Optional

from .pipeline import DEFAULT_COMPONENTS, DEFAULT_OCR_LANG, extract_pdf
from .utils.frontmatter import read_existing_hash
from .utils.hash import sha256_file

VALID_COMPONENTS = {"text", "tables", "images", "math", "ocr"}


def _force_utf8_console() -> None:
    """Windows defaults stdout to cp1252 — breaks Vietnamese filenames in logs."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def main(argv: Optional[List[str]] = None) -> int:
    _force_utf8_console()
    parser = argparse.ArgumentParser(
        prog="python -m tools.pdf_extract",
        description=(
            "Extract a PDF (text, tables, images, math) into Markdown + assets/. "
            "Pass a folder to convert every PDF inside recursively."
        ),
    )
    parser.add_argument("input", help="Path to a .pdf file or a folder of PDFs.")
    parser.add_argument(
        "-o", "--output",
        help="Output directory (default: same folder as each PDF).",
    )
    parser.add_argument(
        "--components",
        default=",".join(DEFAULT_COMPONENTS),
        help=(
            "Comma-separated components to run. "
            f"Choices: {', '.join(sorted(VALID_COMPONENTS))}. "
            f"Default: {','.join(DEFAULT_COMPONENTS)}."
        ),
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-convert even if the MD's source_hash matches the PDF.",
    )
    parser.add_argument(
        "--no-confusables", action="store_true",
        help="Skip Vietnamese OCR confusable flagging (vi/vĩ etc.).",
    )
    parser.add_argument(
        "--no-ocr", action="store_true",
        help="Skip OCR of scanned (image-only) pages even if present.",
    )
    parser.add_argument(
        "--ocr-lang", default=DEFAULT_OCR_LANG,
        help=f"Tesseract language(s) for OCR. Default: {DEFAULT_OCR_LANG}.",
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="Suppress per-file progress lines.",
    )

    args = parser.parse_args(argv)

    components = tuple(c.strip() for c in args.components.split(",") if c.strip())
    if args.no_ocr:
        components = tuple(c for c in components if c != "ocr")
    invalid = set(components) - VALID_COMPONENTS
    if invalid:
        parser.error(f"Unknown components: {', '.join(sorted(invalid))}")

    pdfs = _collect_pdfs(Path(args.input))
    if not pdfs:
        print(f"No PDF files found at: {args.input}", file=sys.stderr)
        return 1

    new_count = 0
    cached_count = 0
    error_count = 0
    total = len(pdfs)

    for i, pdf in enumerate(pdfs, start=1):
        out_dir = Path(args.output) if args.output else pdf.parent
        outcome = _process_one(pdf, out_dir, components, args, i, total)
        if outcome == "cached":
            cached_count += 1
        elif outcome == "new":
            new_count += 1
        else:
            error_count += 1

    if not args.quiet:
        print(
            f"\nDone. {new_count} new, {cached_count} cached, {error_count} errors."
        )
    return 0 if error_count == 0 else 2


def _process_one(pdf: Path, out_dir: Path, components, args, i: int, total: int) -> str:
    """Convert one PDF (honouring cache). Returns 'cached' | 'new' | 'error'."""
    md_path = out_dir / (pdf.stem + ".md")
    if md_path.exists() and not args.force:
        if read_existing_hash(md_path) == sha256_file(pdf):
            if not args.quiet:
                print(f"[{i}/{total}] cached: {pdf.name}")
            return "cached"

    if not args.quiet:
        print(f"[{i}/{total}] converting: {pdf.name}")
    try:
        result = extract_pdf(
            pdf,
            output_dir=out_dir,
            components=components,
            flag_vn_confusables=not args.no_confusables,
            ocr_lang=args.ocr_lang,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"  ERROR: {pdf.name}: {exc}", file=sys.stderr)
        return "error"

    if not args.quiet:
        print(
            f"  -> {result.markdown_path.name} "
            f"({result.pages} pages, {len(result.blocks)} blocks, "
            f"{result.confusables_flagged} confusables flagged)"
        )
        _print_ocr_note(result.ocr_info)
    return "new"


def _print_ocr_note(ocr_info: dict) -> None:
    if ocr_info.get("used"):
        pages = ocr_info.get("pages") or []
        print(f"     OCR: {len(pages)} trang scan đã OCR ({ocr_info.get('language')})")
    elif ocr_info.get("needed"):
        scanned = ocr_info.get("scanned_pages") or []
        print(
            f"     ⚠ OCR cần cho {len(scanned)} trang scan nhưng chưa cài Tesseract — "
            f"{ocr_info.get('reason', '')}",
            file=sys.stderr,
        )


def _collect_pdfs(path: Path) -> List[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() == ".pdf" else []
    if path.is_dir():
        return sorted(path.rglob("*.pdf"))
    return []


if __name__ == "__main__":
    sys.exit(main())
