"""Flag Vietnamese OCR confusables per skills/pdf-to-md/SKILL.md §3.1.

Two signals, both inline & idempotent (re-running adds nothing new):

1. **Ambiguous confusable words** — `vi`/`vĩ`, `sản`/`sàn`, `lý`/`ly`, …
   The old version flagged *every* occurrence, which buried the file in noise
   (e.g. "sản xuất", "lý luận" flagged hundreds of times). We now SUPPRESS a flag
   when the word sits in a collocation that disambiguates it (`sản xuất` is never
   `sàn xuất`; `vĩ đại` is never `vi đại`). Genuinely ambiguous cases — the
   documented `vi mô`/`vĩ mô` trap — are left unflagged-safe and still flagged.

2. **Duplicate MCQ options** — if two options (A/B/C/D) inside one `### Câu`
   block have identical text, the OCR almost certainly mangled a tone mark in one
   of them. This is the high-value signal §3.1.5 calls out.
"""
import re
import unicodedata
from typing import Dict, List, Set, Tuple

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

# Words whose RIGHT neighbour (the following word) makes them unambiguous.
# Deliberately omits the genuinely ambiguous pairs (e.g. "vi mô" vs "vĩ mô").
SAFE_RIGHT: Dict[str, Set[str]] = {
    "sản": {"xuất", "phẩm", "lượng", "sinh", "nghiệp", "vật", "khoái"},
    "lý": {"luận", "thuyết", "do", "tưởng", "trí", "lẽ", "tính", "giải", "hóa", "sự", "tài"},
    "ly": {"hôn", "dị", "khai", "tâm", "giác", "gián", "biệt", "kỳ", "ti"},
    "vĩ": {"đại", "tuyến", "độ", "nhân", "cuồng"},
    "vi": {"phạm", "khuẩn", "rút", "diệu", "mạch", "tế", "sinh", "trùng", "ô", "cá", "deo"},
    "chỉ": {"số", "tiêu", "đạo", "dẫn", "huy", "định", "thị", "ra", "là", "có",
            "còn", "một", "được", "cần", "thấy", "riêng", "rõ", "tay", "trỏ", "đường"},
    "chí": {"hướng", "khí", "sĩ", "tuyến", "lý", "công", "mạng", "minh"},
    "hoàn": {"thành", "thiện", "vốn", "toàn", "cảnh", "tất", "trả", "lại", "hảo",
             "chỉnh", "mỹ", "nguyên"},
    "hoàng": {"gia", "hậu", "tử", "đế", "cung", "tộc", "bào", "thành", "hôn", "kim", "đạo"},
    "lỗ": {"hổng", "chân", "tai", "mũi", "thủng", "khoan"},
    "lô": {"đất", "hàng", "cốt", "xiên", "đề", "gic"},
    "nhặt": {"rác", "nhạnh", "được"},
    "nhật": {"ký", "báo", "trình", "thực", "dụng", "bản", "nguyệt"},
    "mã": {"số", "hóa", "lực", "vạch", "lai", "đáo", "não"},
    "mả": {"mẹ", "cha", "tổ"},
    "sỉ": {"vả", "nhục", "mắng"},
    "sĩ": {"diện", "quan", "tử", "phu", "khí", "số", "quân"},
}

# Words whose LEFT neighbour (the preceding word) makes them unambiguous.
SAFE_LEFT: Dict[str, Set[str]] = {
    "sản": {"tư", "vô", "cộng", "gia", "di", "thủy", "nông", "lâm", "ngư",
            "khoáng", "đặc", "bất", "hải", "phá"},
    "lý": {"quản", "hợp", "vật", "đạo", "nguyên", "pháp", "tâm", "địa", "xử",
           "sinh", "chân", "công", "lập", "sinh", "tâm", "thụ"},
    "ly": {"phân", "cách", "tách", "chia", "cự", "mi"},
    "vĩ": {"hùng", "bĩ"},
    "vi": {"hành", "ti", "hàn", "phòng"},
    "chỉ": {"không", "chẳng", "đâu", "ngón", "mục"},
    "chí": {"ý", "đồng", "quyết", "thiện", "tạp", "đề", "hạ", "thượng",
            "báo", "nhật", "địa", "tỉnh", "đắc"},
    "hoàn": {"tuần", "luân", "chu", "bổ", "hồi"},
    "hoàng": {"huy", "phượng", "nhà"},
    "lỗ": {"thua", "chịu", "bị", "thâm"},
    "lô": {"từng", "mỗi", "số"},
    "nhặt": {"lượm", "thu", "gom"},
    "nhật": {"thường", "sinh", "chủ"},
    "mã": {"mật", "ngựa", "xe", "kỵ", "giải", "quân", "phi"},
    "mả": {"mồ", "ngôi", "đẹp"},
    "sỉ": set(),
    "sĩ": {"bác", "chiến", "nghệ", "ca", "tiến", "nho", "hạ", "dũng", "văn",
           "võ", "tu", "thạc", "cử", "đạo", "họa", "nhạc", "thi", "y", "nha",
           "binh", "tướng", "hiệp", "đạo"},
}

_PAGE_MARKER_RE = re.compile(r"<!-- page (\d+) -->")
_EXISTING_FLAG_RE = re.compile(r"\s*\[VERIFY_OCR:[^\]]*\]")
_PREV_WORD_RE = re.compile(r"([A-Za-zÀ-ỹ]+)[\W_]*$")
_NEXT_WORD_RE = re.compile(r"^[\W_]*([A-Za-zÀ-ỹ]+)")

# MCQ structure
_QUESTION_RE = re.compile(r"^#{2,4}\s*C[âa?]u\b", re.IGNORECASE)
_OPTION_RE = re.compile(r"^[-*]\s*\*\*([A-D])\.?\*\*\s*(.*)$")


def _word_pattern() -> re.Pattern:
    keys = sorted(CONFUSABLE_PAIRS.keys(), key=len, reverse=True)
    alternation = "|".join(re.escape(k) for k in keys)
    return re.compile(
        rf"(?<![\wÀ-ỹ])({alternation})(?![\wÀ-ỹ])",
        re.IGNORECASE,
    )


_WORD_RE = _word_pattern()


def strip_existing_flags(md_text: str) -> str:
    """Remove all `[VERIFY_OCR: ...]` markers (and the space before them)."""
    return _EXISTING_FLAG_RE.sub("", md_text)


def flag_confusables(md_text: str) -> Tuple[str, int]:
    """Return (annotated_md, count_of_flags_added).

    A confusable word is flagged ONLY when its surrounding collocation does not
    disambiguate it. Page numbers come from `<!-- page N -->` markers. Already
    flagged spans are skipped, so re-running is idempotent.
    """
    page_lookup = _build_page_lookup(md_text)
    flag_spans = [m.span() for m in _EXISTING_FLAG_RE.finditer(md_text)]
    count = 0

    def inside_existing_flag(pos: int) -> bool:
        return any(start <= pos < end for start, end in flag_spans)

    def followed_by_flag(end_pos: int) -> bool:
        return any(start - end_pos in (0, 1) for start, _ in flag_spans)

    def repl(match: re.Match) -> str:
        nonlocal count
        word = match.group(0)
        key = word.lower()
        partner = CONFUSABLE_PAIRS.get(key)
        if not partner:
            return word
        if inside_existing_flag(match.start()) or followed_by_flag(match.end()):
            return word
        if _is_disambiguated(key, md_text, match.start(), match.end()):
            return word
        count += 1
        page = page_lookup(match.start())
        page_suffix = f" trang {page}" if page else ""
        return f"{word} [VERIFY_OCR: {key}/{partner} — check PDF{page_suffix}]"

    return _WORD_RE.sub(repl, md_text), count


def _is_disambiguated(key: str, text: str, start: int, end: int) -> bool:
    """True if the collocation around the word resolves the ambiguity."""
    next_match = _NEXT_WORD_RE.search(text[end:end + 40])
    if next_match and next_match.group(1).lower() in SAFE_RIGHT.get(key, ()):
        return True
    prev_match = _PREV_WORD_RE.search(text[max(0, start - 40):start])
    if prev_match and prev_match.group(1).lower() in SAFE_LEFT.get(key, ()):
        return True
    return False


def flag_duplicate_options(md_text: str) -> Tuple[str, int]:
    """Flag MCQ questions where two options (A-D) have identical text.

    Appends a single `[VERIFY_OCR: phương án trùng ...]` note to the question
    heading. Idempotent: skips questions already carrying that note.
    """
    lines = md_text.splitlines(keepends=True)
    blocks = _split_question_blocks(lines)
    added = 0
    for heading_idx, opt_lines in blocks:
        if "[VERIFY_OCR: phương án trùng" in lines[heading_idx]:
            continue
        norms = [_normalize_option(t) for _, t in opt_lines]
        dup_labels = _duplicate_labels(opt_lines, norms)
        if dup_labels:
            note = (
                f" [VERIFY_OCR: phương án trùng ({'/'.join(dup_labels)}) — "
                "có thể OCR nhầm dấu, check PDF]"
            )
            lines[heading_idx] = lines[heading_idx].rstrip("\n") + note + "\n"
            added += 1
    return "".join(lines), added


def _split_question_blocks(lines: List[str]) -> List[Tuple[int, List[Tuple[str, str]]]]:
    """Yield (heading_line_index, [(label, option_text), ...]) per question."""
    blocks: List[Tuple[int, List[Tuple[str, str]]]] = []
    current_heading = None
    current_opts: List[Tuple[str, str]] = []
    for idx, line in enumerate(lines):
        if _QUESTION_RE.match(line.strip()):
            if current_heading is not None:
                blocks.append((current_heading, current_opts))
            current_heading = idx
            current_opts = []
        elif current_heading is not None:
            m = _OPTION_RE.match(line.strip())
            if m:
                current_opts.append((m.group(1), m.group(2)))
    if current_heading is not None:
        blocks.append((current_heading, current_opts))
    return blocks


def _normalize_option(text: str) -> str:
    """Lowercase, strip flags/diacritics/punctuation for duplicate comparison."""
    text = _EXISTING_FLAG_RE.sub("", text)
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.replace("đ", "d")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def _duplicate_labels(opt_lines, norms) -> List[str]:
    seen: Dict[str, str] = {}
    dups: List[str] = []
    for (label, _), norm in zip(opt_lines, norms):
        if len(norm) < 4:  # ignore near-empty / single-letter OCR garbage
            continue
        if norm in seen:
            for lbl in (seen[norm], label):
                if lbl not in dups:
                    dups.append(lbl)
        else:
            seen[norm] = label
    return dups


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
