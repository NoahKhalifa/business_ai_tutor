# pdf_extract — CLI tách PDF thành Markdown + components

Tool Python local, không cần LLM, không tốn token. Tách PDF học liệu thành các **component độc lập tái sử dụng được**:

| Component | File | Trách nhiệm |
|---|---|---|
| `TextExtractor` | [extractors/text.py](extractors/text.py) | Text + detect heading theo font size (H1/H2/H3) |
| `TableExtractor` | [extractors/tables.py](extractors/tables.py) | Phát hiện bảng → Markdown table |
| `ImageExtractor` | [extractors/images.py](extractors/images.py) | Trích ảnh nhúng → PNG ở `assets/` |
| `MathExtractor` | [extractors/math.py](extractors/math.py) | Detect vùng công thức toán → crop PNG ở `assets/` |
| `OcrExtractor` | [extractors/ocr.py](extractors/ocr.py) | OCR (Tesseract) các trang scan/ảnh không có text layer |
| `pipeline.extract_pdf` | [pipeline.py](pipeline.py) | Orchestrate: gom blocks, dedupe overlap, render MD |

Mỗi extractor trả về `list[Block]` — bạn có thể dùng riêng lẻ trong code khác mà không cần chạy cả pipeline.

## Cài đặt

```powershell
# 1. Cài Python ≥ 3.10 (chưa có): https://www.python.org/downloads/windows/
#    Khi cài, TICK "Add Python to PATH".

# 2. Cài dependencies
pip install -r tools/pdf_extract/requirements.txt
```

Phụ thuộc:
- `pymupdf` — PDF parsing (text, font info, image extraction, render)
- `pdfplumber` — table detection
- `pytesseract` + `pillow` — **chỉ cần cho PDF scan/ảnh**. Text PDF không import tới.

Không có dependency nặng (không ML model).

### Cài Tesseract (cho PDF scan/ảnh)

`pytesseract` chỉ là wrapper — cần **Tesseract binary** + gói ngôn ngữ `vie`:

```powershell
winget install UB-Mannheim.TesseractOCR   # nhớ tick gói "Vietnamese" khi cài
# rồi đảm bảo tesseract.exe nằm trong PATH
```

Nếu Tesseract chưa cài, tool **vẫn chạy bình thường** với PDF text; gặp PDF scan nó
chỉ cảnh báo và ghi `ocr_needed: true` vào front-matter (không crash).

## Dùng CLI

```powershell
# Convert 1 file (MD ghi cạnh PDF, ảnh + math ở ./assets/)
python -m tools.pdf_extract "subjects/Quản trị chiến lược/lectures/pdf/bai-1.pdf"

# Convert cả thư mục (đệ quy)
python -m tools.pdf_extract "subjects/Quản trị chiến lược/lectures/pdf/"

# Output dir riêng
python -m tools.pdf_extract input.pdf -o "subjects/Quản trị chiến lược/lectures/md/"

# Chỉ chạy 1-2 component (vd chỉ text + tables)
python -m tools.pdf_extract input.pdf --components text,tables

# Bỏ qua cache (luôn re-convert)
python -m tools.pdf_extract input.pdf --force

# Tắt cờ confusables tiếng Việt
python -m tools.pdf_extract input.pdf --no-confusables

# PDF scan: OCR tự bật cho trang không có text layer. Đổi ngôn ngữ / tắt OCR:
python -m tools.pdf_extract input.pdf --ocr-lang vie
python -m tools.pdf_extract input.pdf --no-ocr
```

### Cache

CLI tính SHA-256 của PDF, so với `source_hash` trong front-matter của file MD đã có:
- Khớp → SKIP, log "cached"
- Khác hoặc MD chưa có → re-convert

Cờ `--force` bỏ qua cache.

## Dùng như library

```python
from pathlib import Path
from tools.pdf_extract import extract_pdf, TableExtractor, ImageExtractor

# Cả pipeline
result = extract_pdf(
    Path("input.pdf"),
    output_dir=Path("out/"),
    components=("text", "tables", "images", "math"),
)
print(result.markdown_path, result.pages, result.confusables_flagged)

# Chỉ 1 component
tables = TableExtractor(Path("input.pdf")).extract()
for t in tables:
    print(f"Trang {t.page}: {t.metadata['rows']}x{t.metadata['cols']}")
    print(t.content)  # markdown table string

# Custom rendering — bạn tự render từ blocks
images = ImageExtractor(Path("input.pdf"), Path("out/")).extract()
for img in images:
    print(f"Trang {img.page}: {img.content}")  # path tới PNG
```

## Output format

File MD bắt đầu bằng YAML front-matter tương thích với [`skills/pdf-to-md/SKILL.md`](../../skills/pdf-to-md/SKILL.md):

```yaml
---
source_pdf: "bai-1-tong-quan.pdf"
source_hash: "sha256:abc123..."
converted_at: "2026-06-22T..."
subject: "Quản trị chiến lược"
doc_type: "lecture"
pages: 28
confusables_flagged: 3
---
```

Body có marker `<!-- page N -->` ở chỗ chuyển trang để `confusables` flagger gắn số trang đúng. Ảnh và công thức nhúng dạng `![Hình trang 3](assets/page_003_img_01.png)`.

## Heuristic detection của math

Math regions được detect khi:
1. Font name chứa từ khóa math (`cmsy`, `cmmi`, `stix`, `mathjax`...) **hoặc**
2. Span text chứa ký tự Unicode toán học (∫∑√≤≥α…)

Các span math sát nhau trên cùng dòng được merge thành 1 vùng, crop ở 200 DPI.

Nếu PDF tiếng Việt dùng font math không chuẩn → có thể miss. Mở rộng `MATH_FONT_KEYWORDS` trong [extractors/math.py](extractors/math.py).

## Cấu trúc

```
tools/pdf_extract/
├── __init__.py             # Public API exports
├── __main__.py             # `python -m tools.pdf_extract`
├── cli.py                  # argparse + cache check + loop
├── pipeline.py             # extract_pdf(), render_markdown()
├── extractors/
│   ├── __init__.py
│   ├── base.py             # Block dataclass, BaseExtractor
│   ├── text.py             # TextExtractor
│   ├── images.py           # ImageExtractor
│   ├── tables.py           # TableExtractor
│   ├── math.py             # MathExtractor
│   └── ocr.py              # OcrExtractor (Tesseract cho trang scan)
├── utils/
│   ├── __init__.py
│   ├── hash.py             # sha256_file
│   ├── frontmatter.py      # build_frontmatter / read_existing_hash
│   ├── confusables.py      # flag_confusables (suppress collocation) + flag_duplicate_options
│   └── answers.py          # flag_answer_marks / remove_empty_pages
├── scripts/
│   └── clean_existing_md.py  # dọn lại MD đã convert (re-flag, bỏ empty page, sửa front-matter)
├── requirements.txt
└── README.md
```

## OCR cho PDF scan/ảnh

`OcrExtractor` tự phát hiện trang **không có text layer** (scan/ảnh) và OCR riêng các
trang đó bằng Tesseract (`vie+eng` mặc định), 300 DPI. Trang có text vẫn do
`TextExtractor` xử lý — không OCR thừa, không trùng nội dung.

Front-matter ghi lại trung thực:
- OCR chạy được → `ocr_used: true`, `ocr_engine: "tesseract"`, `ocr_language`, `ocr_pages`.
- Có trang scan nhưng thiếu Tesseract → `ocr_used: false`, `ocr_needed: true`, `ocr_scanned_pages` (pipeline không crash, chỉ cảnh báo).

> ⚠️ Tesseract OCR tiếng Việt còn hay nhầm **dấu thanh** (vi/vĩ, sản/sàn…). Bộ flag
> confusables ([utils/confusables.py](utils/confusables.py)) sẽ đánh dấu các chỗ
> nghi ngờ — nhưng đã lọc bỏ các collocation chắc chắn (sản xuất, lý luận…) để
> không gây nhiễu. Với học liệu tiếng Việt chất lượng cao, Claude vision (fallback
> qua skill `pdf-to-md`) thường đọc chuẩn hơn Tesseract.

## Edge cases

- **PDF scan (ảnh, không có text layer)** → `OcrExtractor` tự OCR (nếu đã cài Tesseract). Thiếu Tesseract thì ghi `ocr_needed: true` để convert lại sau.
- **PDF có watermark/footer lặp** → hiện chưa filter. Có thể thêm bằng regex post-process.
- **PDF bảo vệ password** → PyMuPDF sẽ raise; CLI in lỗi và sang file kế.
- **PDF lớn (>200 trang)** → chạy được nhưng tốn RAM (math crop 200 DPI). Có thể giảm `MATH_DPI` trong `extractors/math.py`.
