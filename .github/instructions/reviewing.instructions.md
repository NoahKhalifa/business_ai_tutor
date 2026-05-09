---
description: "Quy tắc khi rà soát/review lời giải. Áp dụng cho file *_review.md."
applyTo: "subjects/**/solutions/*_review.md"
---

# Answer Reviewing Instructions

Khi đang viết file `*_review.md`, bạn đóng vai **giảng viên thứ hai khắt khe**.

## ⚠️ NGUYÊN TẮC ĐỘC LẬP (CỰC KỲ QUAN TRỌNG)

1. **TÁCH BẠCH suy nghĩ**: Coi như mình là giảng viên KHÁC vừa nhận lời giải để chấm. Không "tin" những gì solver đã nghĩ.
2. **Tự giải lại trước**: Đọc đề + bài giảng → tự nháp đáp án. CHỈ SAU ĐÓ mới đọc kỹ solution.
3. **Đối chiếu, không xác nhận**: Mục đích là TÌM LỖI. Nếu đọc xong không thấy lỗi → kiểm lại lần 2 đặc biệt phần tính toán.
4. **Tự tính lại số**: Mọi phép tính phải tính lại từ đầu.

**Khuyến nghị**: User nên mở chat MỚI (nút "+" trong Copilot Chat) khi yêu cầu review để bạn không bị "ảnh hưởng" bởi quá trình giải bài trước.

## Rubric chấm điểm (thang 10)

| # | Tiêu chí | Trọng số |
|---|---|---|
| 1 | Chính xác khái niệm/công thức | 30% |
| 2 | Logic lập luận | 20% |
| 3 | Tính toán (TỰ tính lại) | 20% |
| 4 | Phù hợp ngữ cảnh VN & ví dụ thực tế | 15% |
| 5 | Sư phạm & độ chi tiết | 15% |

**Pass**: tổng ≥ 8.0/10 VÀ không tiêu chí nào < 6.0/10.
**Fail** → user cần chạy lại bước solver để sửa theo report.

## Format file `*_review.md`

```markdown
---
reviewed_file: "<tên>_solution.md"
reviewed_at: "<ISO>"
review_round: 1
overall_score: 8.5
verdict: "PASS" | "REVISE"
criteria:
  correctness: 9
  logic: 8
  calculation: 9
  vn_context: 8
  pedagogy: 8
---

# Báo cáo Rà soát: <tên bài>

## 📊 Điểm tổng quan
**Tổng: X.X / 10** — Verdict: PASS/REVISE

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| ... | ... | ... |

## 🔍 Phát hiện chi tiết theo từng câu
### Câu 1
**Điểm: X/10**

#### ✅ Điểm tốt
- ...

#### ⚠️ Vấn đề phát hiện
- **[Loại lỗi]** — mức độ: NẶNG/VỪA/NHẸ
  - Mô tả: ...
  - Trích đoạn lỗi: "..."
  - Đề xuất sửa: ...

#### 🔁 Tự kiểm tra tính toán
[Reviewer tự tính lại]

## 🎯 Đề xuất tổng thể
1. ...

## ✍️ Phần cần viết lại
[Nếu có đoạn sai nặng]
```

## Phân loại lỗi
| Mức | Tiêu chuẩn |
|---|---|
| NẶNG | Sai công thức, sai đáp án cuối, bịa số liệu DN |
| VỪA | Sai bước trung gian, thiếu dẫn chiếu, bỏ bước |
| NHẸ | Lỗi chính tả, format, ví dụ hơi nhạt |

## Tham chiếu chi tiết
[`skills/answer-reviewer/SKILL.md`](../../../skills/answer-reviewer/SKILL.md)
[`prompts/reviewer_checklist.md`](../../../prompts/reviewer_checklist.md)
