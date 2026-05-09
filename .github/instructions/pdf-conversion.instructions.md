---
description: "Khi user xử lý file trong subjects/*/lectures/pdf|md/ hoặc exercises/pdf|md/"
applyTo: "subjects/**/{lectures,exercises}/{pdf,md}/**"
---

# Pointer: PDF Conversion Context

Khi user thao tác trong folder này và yêu cầu convert/biên dịch:
- **Đọc trước**: [`skills/pdf-to-md/SKILL.md`](../../skills/pdf-to-md/SKILL.md)
- **Cache rule**: SHA-256 của PDF phải khớp `source_hash` trong front-matter MD → skip nếu khớp
- **Lecture cần thêm summary**: tạo `<tên>_summary.md` cùng folder
- **Công thức trong MD**: tuân thủ [`prompts/math-formatting.md`](../../prompts/math-formatting.md)
