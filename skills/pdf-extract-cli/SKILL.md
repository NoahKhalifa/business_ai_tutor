---
name: pdf-extract-cli
description: Invoke local Python CLI `tools/pdf_extract` để convert PDF → Markdown + assets/<pdf-stem>/ (images, math crops) mà KHÔNG tốn token LLM. ƯU TIÊN dùng skill này trước khi tự đọc PDF bằng vision/text tool — chỉ fallback đọc tay khi CLI fail, PDF scan (không text layer), hoặc cần phân tích sâu nội dung (giải bài, review). Skill là wrapper của tool — cache SHA-256, modular component (text/tables/images/math), VN OCR confusable flagging tự động.
---

# Skill: PDF extract CLI (token-saving)

## TL;DR cho AI agent
Convert PDF → MD bằng local Python tool thay vì tự đọc → tiết kiệm 90%+ token mỗi PDF.

```powershell
python -m tools.pdf_extract "<đường-dẫn-pdf>" -o "<thư-mục-output>"
```

Tool ở [`tools/pdf_extract/`](../../tools/pdf_extract/). Xem [tool README](../../tools/pdf_extract/README.md) cho chi tiết.

## Khi nào BẮT BUỘC dùng skill này

- User yêu cầu "convert PDF", "đọc PDF", "biên dịch PDF", "extract PDF".
- Pipeline tự động phát hiện PDF mới trong `subjects/*/lectures/pdf/` hoặc `exercises/pdf/` chưa có MD tương ứng.
- Bất kỳ task nào cần text content của 1 PDF mà CHƯA có file `.md` cùng tên với hash khớp.

## Khi nào KHÔNG dùng skill này (fallback Claude đọc trực tiếp)

| Tình huống | Lý do | Fallback |
|---|---|---|
| PDF scan (không có text layer) | CLI extract sẽ rỗng | Claude đọc bằng vision |
| PDF khóa password | PyMuPDF fail | Hỏi user mật khẩu |
| CLI báo lỗi sau 2 lần thử | Có thể format lạ | Claude đọc trực tiếp + log issue |
| User cần phân tích/giải/tóm tắt nội dung (không phải chỉ convert) | Skill này CHỈ convert | Chain: skill convert trước → skill solver/summarizer sau |

## Cách invoke

### Convert 1 file
```powershell
python -m tools.pdf_extract "subjects/<môn>/lectures/pdf/<file>.pdf" -o "subjects/<môn>/lectures/md/"
```

### Convert cả thư mục (đệ quy, có cache)
```powershell
python -m tools.pdf_extract "subjects/<môn>/lectures/pdf/" -o "subjects/<môn>/lectures/md/"
```

### Force re-convert (bỏ qua cache)
```powershell
python -m tools.pdf_extract "<pdf>" -o "<out>" --force
```

### Chỉ extract 1-2 component
```powershell
# Chỉ text (bỏ qua tables/images/math)
python -m tools.pdf_extract "<pdf>" -o "<out>" --components text

# Text + tables
python -m tools.pdf_extract "<pdf>" -o "<out>" --components text,tables
```

### Tắt confusables flagging (nếu nội dung không phải MCQ tiếng Việt)
```powershell
python -m tools.pdf_extract "<pdf>" -o "<out>" --no-confusables
```

## Cache & front-matter

Tool ghi file MD với YAML front-matter tương thích với skill [`pdf-to-md`](../pdf-to-md/SKILL.md):

```yaml
---
source_pdf: "..."
source_hash: "sha256:..."
converted_at: "..."
subject: "..."
doc_type: "lecture" | "exercise"
pages: N
confusables_flagged: N
---
```

- Khi MD đã tồn tại + `source_hash` khớp PDF → **SKIP**, log "cached".
- Khi hash khác hoặc MD chưa có → re-convert.
- User nói "force / convert lại" → thêm `--force`.

## Setup (chỉ 1 lần / máy)

```powershell
# 1. Cài Python ≥3.10 từ https://www.python.org/downloads/windows/ (TICK Add to PATH)
# 2. Cài deps
pip install -r tools/pdf_extract/requirements.txt
```

Verify:
```powershell
python -m tools.pdf_extract --help
```

## Setup status check

Trước khi invoke, agent NÊN check môi trường:
```powershell
python --version    # phải in ra Python 3.10+
python -c "import fitz, pdfplumber"   # không lỗi import
```

Nếu fail → báo user "Tool chưa setup. Chạy `pip install -r tools/pdf_extract/requirements.txt`" → KHÔNG tự auto-install.

## Test suite

Tool có test suite ở [`tools/pdf_extract/tests/`](../../tools/pdf_extract/tests/):
```powershell
python -m unittest discover -s tools/pdf_extract/tests
```
26 tests cover: text/table/image/math extractors + confusables + cache + CLI flags.

Nếu tự edit code của tool → BẮT BUỘC chạy test trước khi commit.

## Workflow tích hợp với các skill khác

```
PDF → [pdf-extract-cli] → MD (có front-matter) → [exercise-solver | answer-reviewer | ...]
```

Skill này KHÔNG:
- Tóm tắt nội dung (đó là việc của summary stage trong `pdf-to-md`)
- Giải bài (→ `exercise-solver`)
- Review câu trả lời (→ `answer-reviewer`)

Skill này CHỈ convert PDF → MD + extract assets. Nhẹ, nhanh, không tốn token.

## Báo cáo cho user

Sau khi chạy xong, summarize ngắn:
```
✅ Convert hoàn tất:
• X file mới (Y trang tổng), Z file cache hit
• N hình ảnh + M công thức toán đã extract vào assets/
• K confusables flagged (cần solver verify với PDF gốc)
```

Không cần báo từng file trừ khi user hỏi chi tiết.

## Edge cases

- **CLI exit code ≠ 0**: in stderr ra cho user, đề xuất `--force` hoặc fallback Claude đọc.
- **`confusables_flagged > 20` trong 1 file ngắn**: có thể OCR engine kém — báo user kiểm tra PDF gốc.
- **`assets/` rỗng sau khi convert PDF được dự đoán có hình**: ImageExtractor có thể skip (icons < 50px) — chạy lại với `--components images` debug.
- **Tiếng Việt bị mất dấu trong output**: PDF có thể dùng font CID không chuẩn — fallback Claude đọc trực tiếp.
