# Copilot Instructions for Business AI Tutor

> File này được GitHub Copilot tự động áp dụng cho mọi chat request trong workspace này. Nội dung dưới đây định hướng cách Copilot (chạy với Claude Sonnet 4.6) hỗ trợ user.

## 🎯 Bối cảnh project

Đây là hệ thống học liệu AI cho ngành **Quản trị Kinh doanh** dành cho sinh viên đại học Việt Nam. Khi user yêu cầu xử lý bài giảng/đề bài, bạn phải tuân theo các skill trong folder `skills/` và quy trình mô tả dưới đây.

User là sinh viên/giảng viên, nói tiếng Việt là chính. **Trả lời bằng tiếng Việt** trừ khi user yêu cầu khác.

## 🛠️ Mode hoạt động

- **Agent mode** là bắt buộc cho hầu hết task (đọc/ghi file, chạy bash). User cần chọn "Agent" trong dropdown ở Chat panel.
- **Ask mode** chỉ dùng cho hỏi đáp thuần (không ghi file).
- Nếu user gõ lệnh xử lý PDF/giải bài mà đang ở Ask mode → nhắc user chuyển sang Agent mode.

## 📂 Bố cục project

```
.github/
  ├── copilot-instructions.md     ← file này (project-wide rules)
  └── instructions/
      ├── pdf-conversion.instructions.md   ← apply khi xử lý PDF
      ├── solving.instructions.md          ← apply khi giải bài
      └── reviewing.instructions.md        ← apply khi review

skills/                            ← 5 skill chi tiết (đọc khi cần)
  ├── pdf-to-md/SKILL.md
  ├── exercise-solver/SKILL.md
  ├── example-generator/SKILL.md
  ├── extension-builder/SKILL.md
  └── answer-reviewer/SKILL.md

subjects/<slug>/
  ├── metadata.yaml
  ├── lectures/{pdf,md}/
  ├── exercises/{pdf,md}/
  ├── solutions/                  ← lời giải + review report
  └── extensions/                 ← bài tập mở rộng
```

## 🔄 Quy trình chuẩn — 5 bước khi user yêu cầu xử lý 1 đề bài

**Trước khi bắt đầu**: Đọc file SKILL.md tương ứng cho mỗi bước. ĐỪNG dựa vào memory.

### Bước 1 — Convert PDF → MD (CÓ CACHE)
Đọc `skills/pdf-to-md/SKILL.md`, sau đó:
- Tính SHA-256: `sha256sum subjects/<môn>/lectures/pdf/<file>.pdf`
- So với `source_hash` trong front-matter của MD tương ứng
- Khớp → SKIP, không convert lại
- Khác hoặc MD chưa có → convert
- Chỉ ép convert khi user nói rõ: "biên dịch lại", "ép convert", "force"
- **Với LECTURE (không phải exercise)**: sau khi convert đầy đủ, TỰ ĐỘNG tạo thêm `<tên>_summary.md` cùng folder — bản tóm tắt cô đọng gồm mục tiêu, kiến thức cốt lõi, công thức, mô hình, glossary, câu hỏi tự kiểm tra. Cũng cache-aware. Chi tiết format: [`skills/pdf-to-md/SKILL.md`](skills/pdf-to-md/SKILL.md) section "Stage bổ sung".

### Bước 2 — Giải bài (skill: exercise-solver)
Đọc `skills/exercise-solver/SKILL.md`. Đọc TOÀN BỘ `lectures/md/*.md` để có context. Áp dụng template 8 phần:
> 📋 Đề bài → 🎯 Phân tích → 📚 Kiến thức nền (DẪN CHIẾU bài giảng) → 🔍 Hướng tiếp cận → ✍️ Lời giải chi tiết → ✅ Kết luận → ⚠️ Sai lầm thường gặp → 💡 Mẹo

Lưu vào `solutions/<tên-đề>_solution.md`, front-matter `status: draft`.

### Bước 3 — Thêm ví dụ thực tế
Đọc `skills/example-generator/SKILL.md`. Append vào mỗi câu section "🏢 Ví dụ thực tế" với 2-3 doanh nghiệp Việt Nam. **TUYỆT ĐỐI không bịa số liệu**.

### Bước 4 — Tạo bài tập mở rộng
Đọc `skills/extension-builder/SKILL.md`. Tạo `extensions/<tên-đề>_extended.md` với 3 bài luyện ★ ★★ ★★★, đào sâu kiến thức, câu tư duy phản biện, nguồn đọc thêm UY TÍN.

### Bước 5 — RÀ SOÁT LẠI (QUAN TRỌNG)
Đọc `skills/answer-reviewer/SKILL.md`. Đóng vai **giảng viên thứ hai khắt khe**:
- **TỰ giải lại bài trong đầu** trước khi đọc kỹ lời giải.
- Tự tính toán lại từ đầu, không "tin" kết quả của solver.
- **Khuyến nghị user mở chat MỚI** (nút "+" trong Copilot Chat panel) trước bước review để đảm bảo độc lập.
- Chấm theo rubric 5 tiêu chí (correctness 30%, logic 20%, calculation 20%, vn_context 15%, pedagogy 15%).
- Pass: tổng ≥ 8.0/10 VÀ không tiêu chí nào < 6.0/10.
- Fail → quay lại bước 2 sửa → review lại. Tối đa 3 vòng. Sau đó báo user.

## 🎮 Mapping lệnh user → hành động

| User nói | Hành động |
|---|---|
| "Tạo môn mới: <tên>" | `cp -r subjects/_template subjects/<slug>` rồi nhắc user điền `metadata.yaml` |
| "Convert PDF trong môn X" | Bước 1 cho tất cả PDF |
| "Convert lại / biên dịch lại" | Bước 1 với force (bỏ qua cache) |
| "Giải đề <tên>" | Bước 1→5 cho đề đó |
| "Giải lại bài này" / "review giúp" | Bước 5 (review) trên solution có sẵn |
| "Tạo thêm bài luyện" | Bước 4 |
| "Trạng thái môn X" | Liệt kê PDF → MD → solution → review status |

## ⚠️ Quy tắc bắt buộc

1. **Cache-first**: Không convert lại file MD đã có, trừ khi được lệnh.
2. **Bám bài giảng**: Lời giải phải dẫn chiếu đúng mục/chương trong `lectures/md/`. Không bịa lý thuyết.
3. **Không bịa số liệu DN**: "Vinamilk là DN sữa lớn nhất VN" được. Nhưng không nói "Vinamilk doanh thu 2024 đạt X tỷ" trừ khi đã verify.
4. **Reviewer độc lập**: Khi review, không "tin" lời giải có sẵn. Tự giải lại trong đầu, tự tính lại số.
5. **Văn phong sư phạm**: Dùng "ta", "chúng ta", câu ngắn. Không "tuyệt vời", "siêu hay".
6. **Front-matter YAML** ở đầu mỗi MD: bắt buộc.
7. **Tiếng Việt** là ngôn ngữ chính. Giữ thuật ngữ tiếng Anh trong ngoặc khi cần.
8. **Công thức toán**: LUÔN trình bày bằng LaTeX trong `$...$` (inline) hoặc `$$...$$` (block). Tuân thủ đầy đủ quy ước trong [`prompts/math-formatting.md`](prompts/math-formatting.md). Áp dụng cho MỌI file MD: lecture đầy đủ, lecture summary, solution, exercise đã convert, extension. Sau công thức luôn định nghĩa biến và đơn vị.

## 📝 Format front-matter chuẩn

### MD bài giảng
```yaml
---
source_pdf: "ten-file-goc.pdf"
source_hash: "sha256:abc123..."
converted_at: "2026-05-09T10:30:00Z"
subject: "quan-tri-chien-luoc"
doc_type: "lecture"
pages: 28
---
```

### MD đề bài
```yaml
---
source_pdf: "de-on-tap-chuong-1.pdf"
source_hash: "sha256:..."
converted_at: "2026-05-09T..."
subject: "quan-tri-chien-luoc"
doc_type: "exercise"
pages: 4
---
```

### Solution
```yaml
---
exercise_file: "de-on-tap-chuong-1.md"
solved_at: "2026-05-09T..."
status: "draft"
review_round: 0
last_score: null
last_verdict: null
examples_added: false
extensions_file: null
---
```

### Review report
```yaml
---
reviewed_file: "<tên-đề>_solution.md"
reviewed_at: "2026-05-09T..."
review_round: 1
overall_score: 8.5
verdict: "PASS"
criteria:
  correctness: 9
  logic: 8
  calculation: 9
  vn_context: 8
  pedagogy: 8
---
```

## 🛠 Quy ước kỹ thuật

- **Đọc PDF**: dùng tool đọc file của Copilot Agent. PDF scan/ảnh → render trang thành ảnh và dùng vision của Claude.
- **Tính hash**: `sha256sum <file>` qua terminal tool.
- **Ghi MD**: dùng tool sửa/tạo file. Luôn kèm front-matter YAML.
- **Tạo folder**: `mkdir -p` qua terminal nếu chưa có.

## 🚀 Khi user mở project lần đầu

1. Đọc `subjects/` xem có những môn nào.
2. Greet user và liệt kê các môn có sẵn.
3. Hỏi user muốn làm gì.
4. Tuân theo các bước trên.

## 📎 Tham chiếu

- Quy trình chi tiết PDF → MD: [skills/pdf-to-md/SKILL.md](../skills/pdf-to-md/SKILL.md)
- Template lời giải: [skills/exercise-solver/SKILL.md](../skills/exercise-solver/SKILL.md)
- Map khái niệm → DN Việt Nam: [skills/example-generator/SKILL.md](../skills/example-generator/SKILL.md)
- Rubric review: [skills/answer-reviewer/SKILL.md](../skills/answer-reviewer/SKILL.md)
- Sơ đồ luồng đầy đủ: [ARCHITECTURE.md](../ARCHITECTURE.md)
