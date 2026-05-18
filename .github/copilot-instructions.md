# Project: Business AI Tutor

Hệ thống học liệu AI cho sinh viên ngành **Quản trị Kinh doanh** (tiếng Việt). Trả lời và viết MD bằng tiếng Việt.

## 🗺️ Routing — KHI USER YÊU CẦU GÌ → ĐỌC FILE NÀO

Đừng tự đoán cách làm. Đọc skill tương ứng TRƯỚC KHI bắt tay vào việc. KHÔNG đọc trước skill nào nếu user chưa yêu cầu task tương ứng.

| User yêu cầu | Đọc file này trước |
|---|---|
| Convert PDF / biên dịch / extract bài giảng | `skills/pdf-to-md/SKILL.md` |
| Transcribe audio / chuyển MP3 / xử lý file nghe | `skills/audio-to-transcript/SKILL.md` |
| Giải bài tập / hướng dẫn giải / phân tích case | `skills/exercise-solver/SKILL.md` |
| Thêm ví dụ thực tế / DN Việt Nam nào | `skills/example-generator/SKILL.md` |
| Bài luyện thêm / mở rộng / câu hỏi ôn thi | `skills/extension-builder/SKILL.md` |
| Review / chấm điểm / kiểm tra lời giải | `skills/answer-reviewer/SKILL.md` |
| Công thức toán | `prompts/math-formatting.md` |
| Sơ đồ luồng tổng quan | `ARCHITECTURE.md` |
| Bản đồ project nhanh | `INDEX.md` |

## 🔄 Pipeline mặc định khi user nói "Giải đề X"

0. **audio-to-transcript** *(chỉ khi môn có `media_types: ["audio"]` trong metadata.yaml)*: Transcribe MP3 (cache theo SHA-256 — skip nếu đã có)
1. **pdf-to-md**: Convert PDF (cache theo SHA-256 — skip nếu đã có) + tạo `_summary.md` cho lecture
2. **exercise-solver**: Giải đầy đủ, lưu `solutions/<đề>_solution.md` (+ section 🎧 nếu có audio)
3. **example-generator**: Thêm ví dụ DN Việt Nam
4. **extension-builder**: Tạo `extensions/<đề>_extended.md`
5. **answer-reviewer**: Chấm điểm, sửa nếu < 8.0/10. Đọc skill này khi review.

## ⚠️ Quy tắc bất biến (không cần đọc skill cũng phải nhớ)

1. **Cache-first**: PDF → MD đã có thì SKIP convert, trừ khi user nói "force/biên dịch lại".
2. **Không bịa số liệu DN Việt Nam** (doanh thu, lợi nhuận cụ thể) — chỉ thông tin công khai.
3. **Reviewer độc lập**: khi review, tự giải lại trong đầu trước khi đọc lời giải có sẵn.
4. **Tiếng Việt** là ngôn ngữ chính.
5. **Công thức toán**: LaTeX trong `$...$` hoặc `$$...$$` — chi tiết tại `prompts/math-formatting.md`.
6. **Front-matter YAML** ở đầu mọi MD sinh ra (format trong skill tương ứng).
7. **Transcript nguyên văn**: KHÔNG tóm tắt, KHÔNG dịch, KHÔNG sửa nội dung audio gốc khi transcribe.

## 🎯 Mode bắt buộc

User phải ở **Agent mode** + model **Claude Sonnet 4.6** để đọc/ghi file. Nếu phát hiện đang ở Ask mode mà user yêu cầu xử lý PDF/giải bài → nhắc chuyển mode.

## 📂 Cấu trúc nhanh
```
skills/{pdf-to-md, audio-to-transcript, exercise-solver, example-generator, extension-builder, answer-reviewer}/SKILL.md
subjects/<slug>/{lectures, exercises}/{pdf, md, audio}/  +  solutions/  +  extensions/
prompts/{math-formatting, solver_template, reviewer_checklist}.md
```

Chi tiết format folder và quy ước đặt tên: xem [`ARCHITECTURE.md`](../ARCHITECTURE.md).
