"""Flag OCR'd answer-marks in an *answered* MCQ scan — WITHOUT guessing the letter.

Answered quizzes have the chosen option circled/ticked. OCR mangles that mark into
garbage at the start of an option line (`© AH.`, `O ©.`, `@ 8.`, `fe) A.`) or a
trailing `+`. It is tempting to recover the answer key from these, but the leading
glyph is unreliable — it is just as often plain OCR noise on a normal option as a
real selection mark (verified: cross-checking against the option text produces
historically wrong answers). So we DO NOT assert a letter.

What we do safely:
  * drop `[OCR_EMPTY_PAGE]` markers,
  * strip a stray trailing `+`,
  * flag any line that looks like it carried a selection mark, so the solver
    (which has the PDF) verifies it rather than trusting the OCR.
"""
import re
from typing import List, Tuple

_PAGE_RE = re.compile(r"^<!--\s*page\s*\d+\s*-->\s*$")
_EMPTY_PAGE_RE = re.compile(r"^\s*\[OCR_EMPTY_PAGE\]\s*$")
_CLEAN_OPT_RE = re.compile(r"^[-*]\s*\*\*([A-D])\.?\*\*\s*(.*)$")

# Leading OCR garbage that stands in for a circle/tick on the chosen option.
_MARK_LEAD_RE = re.compile(r"^\s*(?:[©®@Œœ•◦°º¬]+|O\s+[©Œ]|[©Œ]|fe\)|\([A-Za-z]?\))")
_TRAILING_PLUS_RE = re.compile(r"\s+\+\s*$")
_LONE_PLUS_RE = re.compile(r"^\s*\+\s*$")
_MARK_FLAG = "[VERIFY_OCR: dòng có thể là đáp án được khoanh — OCR hỏng, đối chiếu PDF]"


def remove_empty_pages(body: str) -> str:
    """Drop `[OCR_EMPTY_PAGE]` and the page marker immediately above it."""
    out: List[str] = []
    for line in body.splitlines():
        if _EMPTY_PAGE_RE.match(line):
            if out and _PAGE_RE.match(out[-1]):
                out.pop()
            continue
        out.append(line)
    return "\n".join(out)


def flag_answer_marks(body: str) -> Tuple[str, int]:
    """Strip stray trailing `+`, drop lone-`+` lines, flag mark-looking lines.

    Idempotent: a line already carrying the mark flag is left untouched.
    """
    lines = body.splitlines()
    out: List[str] = []
    count = 0
    for line in lines:
        if _LONE_PLUS_RE.match(line):
            continue  # a tick with no attached text — pure noise
        if _MARK_FLAG in line:
            out.append(line)
            continue
        stripped = line.rstrip()
        had_plus = bool(_TRAILING_PLUS_RE.search(stripped))
        if had_plus:
            stripped = _TRAILING_PLUS_RE.sub("", stripped)
        is_garbled_mark = bool(_MARK_LEAD_RE.match(stripped)) and not _CLEAN_OPT_RE.match(
            stripped.strip()
        )
        if had_plus or is_garbled_mark:
            out.append(f"{stripped} {_MARK_FLAG}")
            count += 1
        else:
            out.append(line)
    return "\n".join(out), count
