"""One-off maintenance: clean already-converted (vision-OCR'd) exercise MD files.

Re-flags confusables with the new suppression logic, drops empty-page markers,
recovers the marked answer key, and corrects the OCR provenance in front-matter.

Usage:
    python tools/pdf_extract/scripts/clean_existing_md.py <file_or_dir> [--dry-run]

Loads the util modules by file path so it runs even when heavy deps
(pdfplumber/pytesseract) are not installed.
"""
import argparse
import importlib.util
import re
import sys
from pathlib import Path

_UTILS = Path(__file__).resolve().parents[1] / "utils"


def _load(mod_name: str):
    spec = importlib.util.spec_from_file_location(mod_name, _UTILS / f"{mod_name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


confusables = _load("confusables")
answers = _load("answers")

_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def split_frontmatter(text: str):
    m = _FM_RE.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def fix_frontmatter(fm: str, confusable_count: int, answer_marks: int) -> str:
    lines = fm.splitlines()
    out = []
    seen = set()
    for line in lines:
        key = line.split(":", 1)[0].strip()
        if key == "ocr_engine":
            # These files were read by Claude vision, not Tesseract — tell the truth.
            out.append('ocr_engine: "claude-vision"')
        elif key == "confusables_flagged":
            out.append(f"confusables_flagged: {confusable_count}")
        elif key == "answers_recovered":
            continue  # drop any earlier (misleading) field
        else:
            out.append(line)
        seen.add(key)
    if "confusables_flagged" not in seen:
        out.append(f"confusables_flagged: {confusable_count}")
    out.append(f"answer_marks_flagged: {answer_marks}")
    return "\n".join(out)


def clean_text(text: str):
    fm, body = split_frontmatter(text)
    body = answers.remove_empty_pages(body)
    body = confusables.strip_existing_flags(body)
    body, n_marks = answers.flag_answer_marks(body)
    body, n_conf = confusables.flag_confusables(body)
    body, n_dup = confusables.flag_duplicate_options(body)
    total_flags = n_conf + n_dup
    if fm is not None:
        fm = fix_frontmatter(fm, total_flags, n_marks)
        text_out = f"---\n{fm}\n---\n{body}"
    else:
        text_out = body
    return text_out, n_marks, total_flags


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    root = Path(args.path)
    files = sorted(root.rglob("*.md")) if root.is_dir() else [root]
    for f in files:
        text = f.read_text(encoding="utf-8")
        out, n_marks, n_flags = clean_text(text)
        print(f"=== {f.name} ===")
        print(f"  answer-mark lines flagged: {n_marks}  | confusable/dup flags: {n_flags}")
        if not args.dry_run:
            f.write_text(out, encoding="utf-8")
            print("  WROTE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
