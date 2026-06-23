"""Build / parse YAML frontmatter compatible with skills/pdf-to-md/SKILL.md."""
import datetime
from pathlib import Path
from typing import Optional

from .hash import sha256_file


def _infer_doc_type(pdf_path: Path) -> str:
    parts = {p.lower() for p in pdf_path.parts}
    if "exercises" in parts or "exercise" in parts:
        return "exercise"
    if "lectures" in parts or "lecture" in parts:
        return "lecture"
    return "document"


def _infer_subject(pdf_path: Path) -> Optional[str]:
    parts = pdf_path.parts
    for i, part in enumerate(parts):
        if part.lower() == "subjects" and i + 1 < len(parts):
            return parts[i + 1]
    return None


def build_frontmatter(pdf_path: Path, pages: int, confusables_flagged: int = 0) -> str:
    pdf_path = Path(pdf_path)
    sha = sha256_file(pdf_path)
    iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "---",
        f'source_pdf: "{pdf_path.name}"',
        f'source_hash: "sha256:{sha}"',
        f'converted_at: "{iso}"',
        f'doc_type: "{_infer_doc_type(pdf_path)}"',
        f"pages: {pages}",
    ]
    subject = _infer_subject(pdf_path)
    if subject:
        lines.insert(-1, f'subject: "{subject}"')
    if confusables_flagged:
        lines.append(f"confusables_flagged: {confusables_flagged}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def read_existing_hash(md_path: Path) -> Optional[str]:
    """Return the bare sha256 hex from an existing MD's frontmatter, or None."""
    if not md_path.exists():
        return None
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    for line in text[3:end].splitlines():
        line = line.strip()
        if line.startswith("source_hash:"):
            value = line.split(":", 1)[1].strip().strip('"').strip("'")
            return value[7:] if value.startswith("sha256:") else value
    return None
