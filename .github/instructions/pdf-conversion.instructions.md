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

## Tham chiếu chi tiết
Đọc [`skills/pdf-to-md/SKILL.md`](../../skills/pdf-to-md/SKILL.md) để biết:
- Cách xử lý PDF scan (vision)
- Cách chia chunk PDF dài
- Format heading, bảng, công thức
- Edge cases (PDF khóa, watermark, đa ngôn ngữ)
