---
reviewed_file: "mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-2_solution.md"
reviewed_at: "2026-06-13T10:30:00+07:00"
review_round: 2
overall_score: 6.8
verdict: "REVISE"
criteria:
  correctness: 8
  logic: 5
  calculation: 8
  vn_context: 8
  pedagogy: 4.5
---

# Báo cáo Rà soát: Luyện tập trắc nghiệm Chương 2 (Mua & QTNC)

> Review độc lập round 2 (2026-06-13), thay thế bản round 1 (8.6 PASS) đã miss lỗi đáp án Q15. Đây là rewrite hoàn chỉnh theo rubric thực sự, KHÔNG phải template clone.

## 🚨 Lỗi đáp án đã sửa trong session 2026-06-12

- **Q15** (chính sách mua, 5 nội dung): đáp án cũ **A** sai (đã sửa thành **C** — "Xây dựng quan hệ với nhà cung cấp"). Bằng chứng bài giảng dòng 1085–1117 liệt kê 5 nội dung Chính sách mua: (1) Vai trò/vị trí/nhiệm vụ BP mua, (2) Tiêu chuẩn hành vi & đạo đức, (3) Đáp ứng PTBV, (4) **Xây dựng quan hệ với NCC**, (5) Vấn đề tác nghiệp. Đề liệt kê 4/5 nội dung và hỏi nội dung còn lại — đáp án đúng **C**. Solver bỏ sót lỗi này trong round 1 review.

## 📊 Điểm tổng quan

**Tổng: 6.8 / 10** — Verdict: **REVISE**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---:|---|
| Chính xác khái niệm/công thức | 8 | Sau khi sửa Q15: 29/30 đáp án đáng tin. Bỏ sót 1 lỗi đáp án trong round 1 là red flag. |
| Logic lập luận | 5 | Boilerplate "không trả lời đúng trọng tâm khái niệm" lặp khắp 30 câu. |
| Tính toán | 8 | N/A (trắc nghiệm khái niệm). |
| Phù hợp ngữ cảnh VN | 8 | Có ví dụ Saigon Co.op, FPT — không bịa số liệu. |
| Sư phạm & chi tiết | 4.5 | "Sai lầm thường gặp" lặp khuôn 30/30 câu. |

## 🔍 Xác minh đáp án (gồm Q15 đã sửa)

| Câu | Đáp án sau sửa | Trạng thái | Bằng chứng bài giảng |
|---:|:---:|:---:|---|
| 15 | C (đã sửa từ A) | ✓ verified | Dòng 1085–1117: 5 nội dung Chính sách mua, có "Xây dựng QH với NCC" |
| 1 | B (mua tức thì/trước/đầu cơ) | ✓ | 3 kiểu theo thời điểm; "mua dự trữ" không trong 3 kiểu |
| 6 | A (5A: Khởi động, Phân tích, Tham vọng, Thực hiện, Nâng cao) | ✓ | Quy trình 5A bài giảng chương 2 |
| 10 | B (3 phương thức: thương lượng/hòa giải/trọng tài-tòa án) | ✓ | "Hủy hợp đồng" không phải phương thức giải quyết |
| 17 | A (A là hạn chế của hòa giải, không phải điều kiện thành công) | ✓ | Đề có từ "ngoại trừ" |
| 23 | B (yêu cầu bồi thường/sửa chữa khi vi phạm) | ✓ | Bài giảng phần hợp đồng |

**Kết quả**: sau khi sửa Q15, đáp án ổn định. Nhưng việc round 1 review không phát hiện Q15 sai cho thấy quy trình review trước đó **không độc lập**.

## ⚠️ Vấn đề hệ thống

### 1. Round 1 review "bỏ sót" lỗi đáp án Q15
Round 1 chấm 8.6 PASS với criterion "correctness: 9" — tức là review trước **không tự giải lại Q15** mà chỉ "đọc và gật đầu". Đây là vi phạm nguyên tắc reviewer độc lập (skill `answer-reviewer/SKILL.md`).

### 2. Boilerplate "Lời giải chi tiết"
Mọi câu dùng cùng mẫu "[Option] không trả lời đúng trọng tâm khái niệm…" cho 3 phương án sai. Không khác biệt hóa A/B/C/D.

### 3. Thiếu trích bài giảng cụ thể
Q15 sau khi sửa đã có trích dòng 1085–1117 — nhưng 29 câu còn lại vẫn không trích dòng nào cụ thể. Mọi câu có thể trích được tương tự.

### 4. "Sai lầm thường gặp" giống nhau 30/30 câu
Không có bẫy cụ thể của từng câu (vd: Q15 nên ghi "Cẩy nhất là nhầm 'xác lập quy trình mua' với 'nội dung Chính sách mua' — quy trình mua là chủ đề riêng, không thuộc 5 nội dung Chính sách").

## 🎯 Đề xuất cho solver

1. **Verify lại 29 câu còn lại** bằng cách tự giải độc lập + trích dòng bài giảng, không chỉ dựa "trông ổn".
2. **Thay boilerplate** bằng phân tích A-B-C-D riêng từng câu.
3. **Trích dòng bài giảng** cho mọi câu — chuẩn theo Q15 đã làm.
4. **"Sai lầm thường gặp"** riêng cho từng câu, đặc biệt câu liệt kê 5/7 nội dung (dễ nhầm con số).
5. **Chú thích nguồn gốc của round 1 review** vì đã miss lỗi — không nên dùng làm tham chiếu trong tương lai.

## ✅ Đánh giá tổng kết
Sau sửa Q15, đáp án ổn nhưng văn bản giải vẫn boilerplate → SV không học sâu. **REVISE** trước khi dùng làm tài liệu chính thức.
