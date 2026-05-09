---
description: "Quy tắc khi convert PDF sang Markdown trong subjects/"
applyTo: "subjects/**/{lectures,exercises}/{pdf,md}/**"
---

# PDF Conversion Instructions

Khi đang làm việc với folder `subjects/*/lectures/pdf|md/` hoặc `subjects/*/exercises/pdf|md/`:

## Quy tắc cache (BẮT BUỘC)
1. Luôn tính SHA-256 của PDF trước: `sha256sum <pdf-path>`
2. So với `source_hash` trong front-matter MD đã có
3. Khớp → SKIP, KHÔNG convert lại
4. Khác hoặc MD chưa có → convert
5. Chỉ ép convert khi user nói "force", "biên dịch lại", "convert lại"

## Format MD output
Mỗi MD phải có front-matter:
```yaml
---
source_pdf: "<tên-file>.pdf"
source_hash: "sha256:..."
converted_at: "<ISO-8601 UTC>"
subject: "<slug-môn>"
doc_type: "lecture" | "exercise"
pages: <số>
---
```
## 📌 Bản tóm tắt cho lecture (BẮT BUỘC)

Sau khi convert một file LECTURE PDF → MD đầy đủ, **luôn tạo thêm** một file tóm tắt:

- **Tên**: `<tên>_summary.md` (cùng folder `lectures/md/`)
- **Chỉ áp dụng với lecture**, KHÔNG tạo summary cho exercise
- **Cache-aware**: nếu file summary đã có và `source_hash` khớp → SKIP
- **Force**: khi user nói "tóm tắt lại" / "regenerate summary"

### Nội dung file summary phải có:
1. Mục tiêu bài học (3-5 ý)
2. Kiến thức cốt lõi (5-10 khái niệm quan trọng nhất)
3. Bảng công thức cần thuộc (LaTeX trong `$...$`)
4. Mô hình/khung phân tích chính
5. Mini-glossary thuật ngữ Việt-Anh
6. 3-5 câu hỏi tự kiểm tra

### Front-matter file summary
```yaml
---
source_pdf: "<tên>.pdf"
source_hash: "sha256:..."   # COPY từ file MD đầy đủ
parent_md: "<tên>.md"
summary_of: "lecture"
created_at: "<ISO-8601>"
subject: "<slug-môn>"
---
```

Chi tiết format đầy đủ: xem section "Stage bổ sung: Tạo bản tóm tắt" trong [`skills/pdf-to-md/SKILL.md`](../../skills/pdf-to-md/SKILL.md).

## Tham chiếu chi tiết
Đọc [`skills/pdf-to-md/SKILL.md`](../../skills/pdf-to-md/SKILL.md) để biết:
- Cách xử lý PDF scan (vision)
- Cách chia chunk PDF dài
- Format heading, bảng, công thức
- Edge cases (PDF khóa, watermark, đa ngôn ngữ)
