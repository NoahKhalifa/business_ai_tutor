# ARCHITECTURE.md — Kiến trúc chi tiết

## 1. Triết lý thiết kế

Project được xây trên 4 nguyên tắc:

1. **Cache-first**: Không bao giờ làm lại việc đã làm (PDF→MD đã có thì skip). Tiết kiệm token, thời gian.
2. **Skill-based**: Mỗi nhiệm vụ là 1 file SKILL.md độc lập trong `skills/`. Claude trong IDE tự đọc skill khi cần.
3. **Reviewer độc lập**: Khi rà soát, Claude phải tự giải lại trong đầu trước khi đọc lời giải có sẵn. Tránh bias xác nhận.
4. **Revision loop**: Nếu review fail → tự sửa theo phản hồi → review lại. Tối đa 3 vòng.

---

## 2. Luồng xử lý 5 bước (do Claude trong IDE thực hiện)

```
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: pdf-to-md   (cache-aware)                          │
│                                                              │
│  Cho mỗi PDF trong lectures/pdf/ và exercises/pdf/:          │
│    1. Tính SHA-256 của PDF                                   │
│    2. Kiểm tra MD tương ứng đã có chưa                       │
│    3. Đọc front-matter MD → so source_hash                   │
│    4. Khớp → SKIP                                            │
│       Khác/không có → convert (đọc PDF qua tool)             │
│    5. Ghi MD với front-matter mới                            │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: exercise-solver                                    │
│                                                              │
│  • Đọc TẤT CẢ lectures/md/*.md để có context lý thuyết        │
│  • Đọc exercises/md/<đề>.md                                  │
│  • Với mỗi câu, viết theo template 8 phần                    │
│  • Lưu solutions/<đề>_solution.md (status: draft)            │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 3: example-generator                                  │
│                                                              │
│  • Append vào mỗi câu section "🏢 Ví dụ thực tế"             │
│  • 2-3 doanh nghiệp Việt Nam                                 │
│  • KHÔNG bịa số liệu                                         │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 4: extension-builder                                  │
│                                                              │
│  Tạo extensions/<đề>_extended.md gồm:                        │
│  • 3 bài luyện ★ ★★ ★★★ (đáp án collapse)                    │
│  • Đào sâu khái niệm + mô hình nâng cao                      │
│  • 3-5 câu tư duy phản biện                                  │
│  • Nguồn đọc thêm UY TÍN                                     │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 5: answer-reviewer  (NGUYÊN TẮC ĐỘC LẬP)              │
│                                                              │
│  1. Mở chat session MỚI (hoặc reset thinking)                │
│  2. Đọc đề bài + bài giảng                                   │
│  3. TỰ GIẢI LẠI trong đầu, ghi nhớ kết quả/lập luận          │
│  4. SAU ĐÓ mới đọc kỹ solution có sẵn → đối chiếu            │
│  5. Chấm theo rubric 5 tiêu chí                              │
│                                                              │
│  if score >= 8.0 AND min_criterion >= 6.0:                   │
│      verdict = PASS  →  status: reviewed                     │
│  else:                                                        │
│      verdict = REVISE  →  quay về STAGE 2 với feedback       │
│      max 3 vòng → ESCALATE: báo user                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Cấu trúc một môn học

> **Quy ước**: tên folder môn dùng tiếng Việt Unicode (VD: `Quản trị chiến lược`). Trường `subject` trong front-matter MD dùng slug ASCII (`quan-tri-chien-luoc`).

```
subjects/Quản trị chiến lược/
├── metadata.yaml
├── lectures/
│   ├── pdf/
│   │   └── bai-1-tong-quan.pdf
│   └── md/
│       └── bai-1-tong-quan.md          ← Đã convert, có cache hash
├── exercises/
│   ├── pdf/
│   │   └── de-on-tap-chuong-1.pdf
│   └── md/
│       └── de-on-tap-chuong-1.md
├── solutions/
│   ├── de-on-tap-chuong-1_solution.md   ← Lời giải + ví dụ
│   └── de-on-tap-chuong-1_review.md     ← Báo cáo review
└── extensions/
    └── de-on-tap-chuong-1_extended.md
```

---

## 4. Status Machine của 1 đề bài

```
                    [empty]
                       │ user bỏ PDF vào exercises/pdf/
                       ▼
                    [pdf_only]
                       │ Stage 1: pdf-to-md
                       ▼
                    [md_ready]
                       │ Stage 2: solver
                       ▼
                  [draft_solution]
                       │ Stage 3: example-generator
                       ▼
              [solution_with_examples]
                       │ Stage 4: extension-builder
                       ▼
              [solution_with_extensions]
                       │ Stage 5: reviewer
                       ▼
                  ┌────┴────┐
                  │         │
              [REVISE]   [PASS]
                  │         │
                  │         ▼
        (back to solver) [reviewed]  ← final
                  │
                  └─ sau 3 vòng vẫn REVISE → [escalated]
```

Trạng thái này được lưu trong front-matter của file solution (`status: draft | reviewed | escalated`).

---

## 5. Cơ chế cache (chi tiết)

Mỗi file MD bài giảng/đề bài có front-matter:

```yaml
---
source_pdf: "ten-file.pdf"
source_hash: "sha256:7d3f9e..."
converted_at: "2026-05-09T10:30:00Z"
---
```

Khi cần xử lý PDF, Claude tính lại hash bằng tool sẵn có:
```bash
sha256sum subjects/<môn>/lectures/pdf/<file>.pdf
```

So với `source_hash` trong MD:
- **Khớp** → skip, dùng MD cũ.
- **Khác hoặc MD không tồn tại** → convert mới.
- **User nói "force"/"convert lại"** → luôn convert.

Tương tự cho solution: nếu `status: reviewed` và đề chưa đổi → có thể skip toàn bộ pipeline cho đề đó.

---

## 6. Rubric Review

> **Single source of truth**: [`skills/answer-reviewer/SKILL.md`](skills/answer-reviewer/SKILL.md)

Tóm tắt: 5 tiêu chí (Chính xác 30%, Logic 20%, Tính toán 20%, Ngữ cảnh VN 15%, Sư phạm 15%).
**Pass**: tổng ≥ 8.0/10 VÀ không tiêu chí nào < 6.0/10. Chi tiết trọng số, cách chấm, phân loại lỗi → xem skill.

---

## 7. Mở rộng tương lai

- **Banking đề thi**: Sau N đề đã giải, sinh đề mới từ ngân hàng kiến thức.
- **Theo dõi tiến độ SV**: Mỗi SV có hồ sơ học tập → AI nhớ điểm yếu để cá nhân hóa.
- **Multi-language**: Hỗ trợ tài liệu tiếng Anh xen tiếng Việt.
- **Tích hợp Anki**: Tự xuất flashcard từ phần "Sai lầm thường gặp" + "Khái niệm cốt lõi".
- **Đa người dùng**: Nhiều SV chia sẻ cùng pool bài giảng nhưng riêng solutions.
