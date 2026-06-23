"""Synthetic PDF generators for tests — use PyMuPDF (already a project dep).

PyMuPDF's built-in "helv" font lacks Vietnamese diacritics — it substitutes "·"
which then trips the math detector. We embed a system TTF (Arial on Windows,
DejaVuSans on Linux) so synthetic PDFs look like real Vietnamese PDFs.
"""
import os
from pathlib import Path

import fitz

_FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
]


def _find_font() -> str:
    for p in _FONT_CANDIDATES:
        if os.path.isfile(p):
            return p
    raise RuntimeError(
        "No suitable TTF font found. Test fixtures need a font that supports "
        "Vietnamese diacritics. Add one to _FONT_CANDIDATES in fixtures.py."
    )


FONT_PATH = _find_font()
FONT_ALIAS = "F0"


def _text(page, point, text, fontsize):
    page.insert_text(
        point, text, fontsize=fontsize, fontname=FONT_ALIAS, fontfile=FONT_PATH,
    )


def make_text_pdf(path: Path) -> Path:
    doc = fitz.open()
    page = doc.new_page()
    _text(page, (72, 72), "Chương 1: Mục tiêu", 24)
    _text(page, (72, 120), "1.1 Khái niệm chính", 16)
    _text(page, (72, 160), "Đây là đoạn văn bản nội dung bình thường của bài giảng.", 10)
    _text(page, (72, 180), "Dòng thứ hai của cùng đoạn văn — cần được giữ liền mạch.", 10)
    doc.save(str(path))
    doc.close()
    return path


def make_table_pdf(path: Path) -> Path:
    doc = fitz.open()
    page = doc.new_page()
    _text(page, (72, 60), "Báo cáo doanh thu", 20)
    cols = [120, 240, 360, 480]
    rows = [110, 140, 170, 200, 230]
    for x in cols:
        page.draw_line((x, rows[0]), (x, rows[-1]))
    for y in rows:
        page.draw_line((cols[0], y), (cols[-1], y))
    _text(page, (cols[0] + 5, rows[0] + 18), "Quý", 10)
    _text(page, (cols[1] + 5, rows[0] + 18), "Doanh thu", 10)
    _text(page, (cols[2] + 5, rows[0] + 18), "Lợi nhuận", 10)
    for i, (q, rev, prof) in enumerate(
        [("Q1", "100", "20"), ("Q2", "150", "30"), ("Q3", "200", "45")]
    ):
        y = rows[i + 1] + 18
        _text(page, (cols[0] + 5, y), q, 10)
        _text(page, (cols[1] + 5, y), rev, 10)
        _text(page, (cols[2] + 5, y), prof, 10)
    doc.save(str(path))
    doc.close()
    return path


def make_image_pdf(path: Path) -> Path:
    doc = fitz.open()
    page = doc.new_page()
    _text(page, (72, 60), "Trang có hình", 18)
    big = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 200, 200), False)
    big.set_rect(big.irect, (50, 100, 200))
    page.insert_image(fitz.Rect(72, 100, 272, 300), pixmap=big)
    big = None
    tiny = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 20, 20), False)
    tiny.set_rect(tiny.irect, (255, 0, 0))
    page.insert_image(fitz.Rect(72, 320, 92, 340), pixmap=tiny)
    tiny = None
    doc.save(str(path))
    doc.close()
    return path


def make_math_pdf(path: Path) -> Path:
    doc = fitz.open()
    page = doc.new_page()
    _text(page, (72, 60), "Công thức hòa vốn", 16)
    _text(page, (72, 100), "BEP = FC ÷ (P − VC)", 12)
    # Symbol font line — counts as math even though chars are ASCII
    page.insert_text((72, 130), "abcdef", fontsize=14, fontname="symb")
    _text(
        page, (72, 170),
        "Đoạn văn này hoàn toàn là chữ thường, không phải công thức.", 11,
    )
    doc.save(str(path))
    doc.close()
    return path


def make_confusable_pdf(path: Path) -> Path:
    doc = fitz.open()
    page = doc.new_page()
    _text(page, (72, 80), "Câu 1: Yếu tố nào KHÔNG thuộc môi trường vi mô?", 12)
    _text(page, (72, 110), "A. Đối thủ cạnh tranh", 11)
    _text(page, (72, 130), "B. Khách hàng", 11)
    _text(page, (72, 150), "C. Tỷ giá hối đoái", 11)
    _text(page, (72, 170), "D. Nhà cung cấp", 11)
    _text(page, (72, 210), "Tâm lý quản trị: bán sỉ và lý thuyết quản lý.", 11)
    doc.save(str(path))
    doc.close()
    return path


def make_combined_pdf(path: Path) -> Path:
    doc = fitz.open()

    p1 = doc.new_page()
    _text(p1, (72, 72), "Bài giảng 1", 24)
    _text(p1, (72, 120), "1.1 Khái niệm", 16)
    _text(p1, (72, 160), "Đoạn nội dung mở đầu chương.", 10)
    cols = [72, 200, 330, 460]
    rows = [220, 250, 280, 310]
    for x in cols:
        p1.draw_line((x, rows[0]), (x, rows[-1]))
    for y in rows:
        p1.draw_line((cols[0], y), (cols[-1], y))
    _text(p1, (cols[0] + 5, rows[0] + 18), "STT", 10)
    _text(p1, (cols[1] + 5, rows[0] + 18), "Tên", 10)
    _text(p1, (cols[2] + 5, rows[0] + 18), "Giá trị", 10)
    for i, (s, n, v) in enumerate([("1", "A", "10"), ("2", "B", "20")]):
        y = rows[i + 1] + 18
        _text(p1, (cols[0] + 5, y), s, 10)
        _text(p1, (cols[1] + 5, y), n, 10)
        _text(p1, (cols[2] + 5, y), v, 10)

    p2 = doc.new_page()
    _text(p2, (72, 72), "1.2 Hình minh họa và công thức", 16)
    img = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 150, 150), False)
    img.set_rect(img.irect, (200, 100, 50))
    p2.insert_image(fitz.Rect(72, 100, 222, 250), pixmap=img)
    img = None
    _text(p2, (72, 300), "NPV = ∑ CF ÷ (1 + r)", 12)

    doc.save(str(path))
    doc.close()
    return path
