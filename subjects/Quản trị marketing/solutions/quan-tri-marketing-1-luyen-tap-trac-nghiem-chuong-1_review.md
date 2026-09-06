---
reviewed_file: "quan-tri-marketing-1-luyen-tap-trac-nghiem-chuong-1_solution.md"
reviewed_at: "2026-08-01T00:30:00Z"
review_round: 5
overall_score: 8.1
verdict: "PASS"
criteria:
  correctness: 8
  logic: 8
  calculation: 10
  vn_context: 8
  pedagogy: 8
---

# Báo cáo Rà soát: Quản trị marketing 1 - Chương 1

## 📊 Điểm tổng quan

**Tổng: 8.1 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---:|---|
| Chính xác khái niệm/công thức | 8 | Đã phục hồi Q3, Q4, Q11 từ PDF extract; chưa phát hiện lỗi đáp án mới trong audit này. |
| Logic lập luận | 8 | Đủ A/B/C/D, không còn `Nhiễu:`, mỗi câu có lý do loại trừ và cite-line. |
| Tính toán | 10 | Không có bài tính. |
| Phù hợp ngữ cảnh VN | 8 | Có ví dụ Vinamilk, Shopee Việt Nam, Highlands Coffee; không dùng số liệu chưa kiểm chứng. |
| Sư phạm & chi tiết | 8 | Đã bổ sung `Lưu ý` riêng cho 35/35 câu, đạt hard gate MCQ compact. |

## 🧪 Audit MCQ hard gate

Kết quả `python3 scripts/audit-mcq-solutions.py`:

- `questions`: 35/35
- `answers`: 35/35
- `option_lines`: A=35, B=35, C=35, D=35
- `cite_lines`: 107
- `note_or_sai_lam_lines`: 35
- `banned_patterns`: `Nhiễu:` = 0
- **Verdict hard gate:** PASS

## 🔍 Phát hiện chi tiết

- **Q3:** PDF gốc là câu về phương pháp nghiên cứu; đáp án **D - Hiệu quả tối ưu** không thuộc nhóm phương pháp như tiếp cận hệ thống/logic/lịch sử, thực tiễn và định lượng.
- **Q4:** PDF gốc là câu về bộ ba giá trị QSP; đáp án **B - Chất lượng, dịch vụ, giá cả**.
- **Q11:** Đã phục hồi câu về cơ sở phân đoạn thị trường người tiêu dùng; đáp án **B** khớp bài giảng dòng 49-56.
- Một số câu về phạm vi/nhiệm vụ học phần (Q20, Q31, Q35) vẫn nên được giảng viên xác nhận nếu ngân hàng Onschool có đáp án nội bộ khác, vì bài giảng trình bày phần này khá rộng.

## 🎯 Ghi chú còn lại

Bản này đã qua hard gate MCQ compact sau khi rewrite: không còn `Nhiễu:`, đủ `Lưu ý` từng câu và vẫn giữ đáp án/cite-line. Phần cần theo dõi còn lại là kiểm tra chuyên môn sâu từng phương án nếu ngân hàng Onschool có đáp án nội bộ khác.

