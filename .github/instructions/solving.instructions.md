---
description: "Quy tắc khi viết lời giải bài tập trong solutions/"
applyTo: "subjects/**/solutions/**"
---

# Solution Writing Instructions

Khi đang làm việc với file trong `subjects/*/solutions/`:

## Template 8 phần BẮT BUỘC cho mỗi câu

```markdown
## Câu N: <tóm tắt 1 dòng>

### 📋 Đề bài
> <trích nguyên văn>

### 🎯 Phân tích đề
- **Dạng bài**: ...
- **Yêu cầu chính**: ...
- **Dữ kiện đã cho**: ...
- **Cần tìm**: ...

### 📚 Kiến thức nền cần dùng
- <Khái niệm> — tham chiếu Mục X.Y trong [bai-N.md](../lectures/md/bai-N.md)
- <Công thức> $$ \text{...} $$

### 🔍 Hướng tiếp cận
<vì sao chọn cách này>

### ✍️ Lời giải chi tiết
**Bước 1**: ...
**Bước 2**: ...

### ✅ Kết luận
<đáp án + ý nghĩa thực tiễn>

### ⚠️ Sai lầm thường gặp
- <Lỗi 1>
- <Lỗi 2>

### 💡 Mẹo / Ghi chú
<nếu có>
```

## Quy tắc tuyệt đối
1. **DẪN CHIẾU bài giảng**: mỗi khái niệm phải link đến mục cụ thể trong `lectures/md/`
2. **Văn phong sư phạm**: dùng "ta", "chúng ta", câu ngắn
3. **Trình bày đủ bước trung gian**: không nhảy logic
4. **Đơn vị tiền tệ**: VND/triệu/tỷ rõ ràng
5. **Không bịa số liệu DN** trong ví dụ thực tế
6. **Tiếng Việt** là chính

## Front-matter
```yaml
---
exercise_file: "<tên-đề>.md"
solved_at: "<ISO-8601>"
status: "draft"   # → "reviewed" sau khi pass
review_round: 0
last_score: null
last_verdict: null
examples_added: false
extensions_file: null
---
```

## Tham chiếu chi tiết
- [`skills/exercise-solver/SKILL.md`](../../../skills/exercise-solver/SKILL.md) — bảng dạng bài QTKD & cách giải
- [`skills/example-generator/SKILL.md`](../../../skills/example-generator/SKILL.md) — map khái niệm → DN VN
- [`prompts/solver_template.md`](../../../prompts/solver_template.md) — template
