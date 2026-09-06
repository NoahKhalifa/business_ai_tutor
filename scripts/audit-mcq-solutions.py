#!/usr/bin/env python3
"""Audit MCQ solution files for project review gates."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED_PATTERNS = [
    "Nhiễu:",
    "không khớp trọng tâm khái niệm",
    "lệch khái niệm",
    "không phải trọng tâm",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def front_matter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) >= 3 else ""


def field_int(fm: str, field: str) -> int | None:
    match = re.search(rf"^{re.escape(field)}:\s*(\d+)\s*$", fm, re.MULTILINE)
    return int(match.group(1)) if match else None


def question_blocks(text: str) -> list[tuple[int, str]]:
    detail_match = re.search(r"^##\s+Lời giải chi tiết\b.*$", text, re.MULTILINE)
    if detail_match:
        text = text[detail_match.end() :]
        next_h2 = re.search(r"^##\s+", text, re.MULTILINE)
        if next_h2:
            text = text[: next_h2.start()]
    matches = list(re.finditer(r"^#{2,3}\s+Câu\s+(\d+)\b.*$", text, re.MULTILINE))
    blocks: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((int(match.group(1)), text[start:end]))
    return blocks


def audit_file(path: Path) -> tuple[bool, list[str]]:
    text = read_text(path)
    fm = front_matter(text)
    total = field_int(fm, "total_questions")
    blocks = question_blocks(text)
    answers = re.findall(r"\*\*Đáp án:\s*[A-D]\*\*", text)
    note_lines = re.findall(r"\*\*(?:Lưu ý|Sai lầm)", text)
    cite_lines = re.findall(r"dòng\s+\d+(?:-\d+)?", text, flags=re.IGNORECASE)
    option_totals = {option: 0 for option in "ABCD"}
    for _, block in blocks:
        for option in "ABCD":
            if re.search(rf"^-\s+\*\*{option}\.", block, re.MULTILINE):
                option_totals[option] += 1
    banned_counts = {pattern: text.count(pattern) for pattern in BANNED_PATTERNS}

    issues: list[str] = []
    expected = total if total is not None else len(blocks)

    if total is None:
        issues.append("missing total_questions in front matter")
    if total is not None and len(blocks) != total:
        issues.append(f"question headings {len(blocks)} != total_questions {total}")
    if len(answers) != expected:
        issues.append(f"answers {len(answers)} != expected {expected}")

    for option, count in option_totals.items():
        if count != expected:
            issues.append(f"question blocks with option {option} analysis {count} != expected {expected}")

    missing_cite = [
        number
        for number, block in blocks
        if not re.search(r"dòng\s+\d+(?:-\d+)?", block, flags=re.IGNORECASE)
    ]
    if missing_cite:
        sample = ", ".join(str(number) for number in missing_cite[:10])
        suffix = "..." if len(missing_cite) > 10 else ""
        issues.append(f"questions missing cite-line: {sample}{suffix}")

    banned_total = sum(banned_counts.values())
    nuisance_count = banned_counts["Nhiễu:"]
    if expected and nuisance_count >= max(1, int(expected * 0.30)):
        issues.append(f"banned boilerplate 'Nhiễu:' appears {nuisance_count} times")

    generic_total = banned_total - nuisance_count
    if generic_total >= 5:
        issues.append(f"generic boilerplate patterns appear {generic_total} times")

    min_notes = int(expected * 0.80) if expected else 0
    if expected and len(note_lines) < min_notes:
        issues.append(f"note/sai-lam lines {len(note_lines)} < required {min_notes}")

    summary = [
        f"{path}:",
        f"  total_questions: {total}",
        f"  question_headings: {len(blocks)}",
        f"  answers: {len(answers)}",
        f"  option_lines: {option_totals}",
        f"  cite_lines: {len(cite_lines)}",
        f"  note_or_sai_lam_lines: {len(note_lines)}",
        f"  banned_patterns: {banned_counts}",
    ]
    if issues:
        summary.append("  verdict: REVISE")
        summary.extend(f"  issue: {issue}" for issue in issues)
    else:
        summary.append("  verdict: PASS")

    return not issues, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="MCQ solution file(s) or directories")
    args = parser.parse_args()

    files: list[Path] = []
    for path in args.paths:
        if path.is_dir():
            files.extend(sorted(path.glob("*_solution.md")))
        else:
            files.append(path)

    ok = True
    for file in files:
        file_ok, lines = audit_file(file)
        ok = ok and file_ok
        print("\n".join(lines))

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
