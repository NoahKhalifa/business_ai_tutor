---
reviewed_file: "quan-tri-marketing-1-luyen-tap-trac-nghiem-chuong-5_solution.md"
reviewed_at: "2026-08-01T00:30:00Z"
review_round: 5
overall_score: 8.2
verdict: "PASS"
criteria:
  correctness: 8.5
  logic: 8
  calculation: 10
  vn_context: 8
  pedagogy: 8
---

# Báo cáo Rà soát: Quản trị marketing 1 - Chương 5

## 📊 Điểm tổng quan

**Tổng: 8.2 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---:|---|
| Chính xác khái niệm/công thức | 8.5 | Đã đối chiếu lại PDF extract; Q3, Q4, Q23, Q24 không còn placeholder/OCR cũ. |
| Logic lập luận | 8 | Đủ A/B/C/D, không còn `Nhiễu:`, mỗi câu có lý do loại trừ và cite-line. |
| Tính toán | 10 | Không có bài tính. |
| Phù hợp ngữ cảnh VN | 8 | Có ví dụ DN VN, không dùng số liệu bịa. |
| Sư phạm & chi tiết | 8 | Đã bổ sung `Lưu ý` riêng cho 35/35 câu, đạt hard gate MCQ compact. |

## 🧪 Audit MCQ hard gate

Kết quả `python3 scripts/audit-mcq-solutions.py`:

- `questions`: 35/35
- `answers`: 35/35
- `option_lines`: A=35, B=35, C=35, D=35
- `cite_lines`: 105
- `note_or_sai_lam_lines`: 35
- `banned_patterns`: `Nhiễu:` = 0
- **Verdict hard gate:** PASS

## 🔍 Phát hiện chi tiết

- **Q3:** PDF gốc hiện là câu “Trong giai đoạn phát triển, doanh nghiệp thường...” với đáp án **C**, không phải câu cũ trong solution round 1. Sửa theo PDF extract ngày 2026-06-27.
- **Q4:** Đã phục hồi case “Laptop Pro 15” ở giai đoạn suy thoái; đáp án **D** hợp lý theo nhóm chiến lược thu hoạch/khai thác phần giá trị còn lại.
- **Q6:** Đáp án sửa thành **B - Phát triển chiến lược marketing**, vì wording khớp mục 5.1.5 hơn là quản trị chiến lược marketing.
- **Q15:** Đáp án sửa thành **A** theo đoạn thị trường chia cắt/hợp nhất trong sự tiến hóa thị trường.
- **Q17:** Đáp án sửa thành **B - Marketing chiến lược**, khớp nguyên văn định nghĩa Kotler ở dòng 3045-3048.
- **Q23/Q24:** Đã thay nội dung OCR cũ bằng nội dung PDF extract; đáp án lần lượt **B** và **D**.

## 🎯 Ghi chú còn lại

Bản này đã qua hard gate MCQ compact sau khi rewrite: không còn `Nhiễu:`, đủ `Lưu ý` từng câu và vẫn giữ đáp án/cite-line. Phần cần theo dõi còn lại là kiểm tra chuyên môn sâu từng phương án nếu ngân hàng Onschool có đáp án nội bộ khác.

