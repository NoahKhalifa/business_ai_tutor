"""Flag Vietnamese OCR confusables per skills/pdf-to-md/SKILL.md §3.1.

Adds inline `[VERIFY_OCR: a/b — check PDF trang N]` markers after words that
have a known OCR confusable. We do NOT auto-correct — that's the solver's job.
"""
import re
from typing import Tuple

# Curated from skills/pdf-to-md/SKILL.md
CONFUSABLE_PAIRS = {
    "vi": "vĩ",
    "vĩ": "vi",
    "sỉ": "sĩ",
    "sĩ": "sỉ",
    "lý": "ly",
    "ly": "lý",
    "lỗ": "lô",
    "lô": "lỗ",
    "hoàn": "hoàng",
    "hoàng": "hoàn",
    "nhặt": "nhật",
    "nhật": "nhặt",
    "chỉ": "chí",
    "chí": "chỉ",
    "sản": "sàn",
    "sàn": "sản",
    "mã": "mả",
    "mả": "mã",
}

_PAGE_MARKER_RE = re.compile(r"<!-- page (\d+) -->")
_EXISTING_FLAG_RE = re.compile(r"\[VERIFY_OCR:[^\]]*\]")


def _word_pattern() -> re.Pattern:
    # Vietnamese letters with diacritics — \b is unreliable, so we use lookaround
    # against any letter, digit, or Vietnamese diacritic character.
    keys = sorted(CONFUSABLE_PAIRS.keys(), key=len, reverse=True)
    alternation = "|".join(re.escape(k) for k in keys)
    return re.compile(
        rf"(?<![\wÀ-ỹ])({alternation})(?![\wÀ-ỹ])",
        re.IGNORECASE,
    )


_WORD_RE = _word_pattern()


def flag_confusables(md_text: str) -> Tuple[str, int]:
    """Return (annotated_md, count_of_flags_added).

    Page numbers come from `<!-- page N -->` markers emitted by the pipeline.
    Already-flagged regions (existing `[VERIFY_OCR: ...]` blocks) are skipped
    so re-running the flagger is idempotent.
    """
    page_lookup = _build_page_lookup(md_text)
    flag_spans = [m.span() for m in _EXISTING_FLAG_RE.finditer(md_text)]
    count = 0

    def inside_existing_flag(pos: int) -> bool:
        for start, end in flag_spans:
            if start <= pos < end:
                return True
        return False

    def followed_by_flag(end_pos: int) -> bool:
        for start, _ in flag_spans:
            if start - end_pos in (0, 1):
                return True
        return False

    def repl(match: re.Match) -> str:
        nonlocal count
        word = match.group(0)
        key = word.lower()
        partner = CONFUSABLE_PAIRS.get(key)
        if not partner:
            return word
        if inside_existing_flag(match.start()) or followed_by_flag(match.end()):
            return word
        count += 1
        page = page_lookup(match.start())
        page_suffix = f" trang {page}" if page else ""
        return f"{word} [VERIFY_OCR: {key}/{partner} — check PDF{page_suffix}]"

    return _WORD_RE.sub(repl, md_text), count


def _build_page_lookup(text: str):
    refs = [(m.start(), int(m.group(1))) for m in _PAGE_MARKER_RE.finditer(text)]

    def lookup(offset: int):
        last = None
        for pos, pg in refs:
            if pos > offset:
                break
            last = pg
        return last

    return lookup
