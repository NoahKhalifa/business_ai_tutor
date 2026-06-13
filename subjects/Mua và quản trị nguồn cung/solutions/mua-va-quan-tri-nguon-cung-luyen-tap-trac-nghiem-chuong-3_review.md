---
reviewed_file: "mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-3_solution.md"
reviewed_at: "2026-06-13T20:10:00+07:00"
review_round: 3
overall_score: 7.0
verdict: "REVISE_MINOR"
criteria:
  correctness: 8.5
  logic: 6
  calculation: 7
  vn_context: 7
  pedagogy: 4.5
---

# Báo cáo Rà soát: Luyện tập trắc nghiệm Chương 3 (Mua & QTNC)

> Lần review này (round 3, 2026-06-13 20:10) **cập nhật sau khi verify T-20260613-01**. Round 2 trước đó nghi ngờ Q16/Q17/Q21 sai đáp án; sau khi đối chiếu trực tiếp với lecture dòng 2039-2078 (Q16, mô hình mua) và dòng 2378-2389 (Q17, Q21, lợi ích TCO hữu hình vs vô hình), kết luận **CẢ 3 ĐÁP ÁN GIỮ A LÀ ĐÚNG**.

## ✅ Verify T-20260613-01 (2026-06-13): Q16/Q17/Q21 đáp án ĐÚNG

| Câu | Đáp án solver | Verify | Bằng chứng |
|---:|:---:|:---:|---|
| 16 | A | ✅ ĐÚNG | Lecture dòng 2073-2078 liệt kê **3 yếu tố** lựa chọn mô hình mua: (1) mục tiêu kiểm soát số lượng mua-dự trữ → D, (2) lợi thế so sánh và quyền mặc cả → B, (3) năng lực NCC trong quản lý giao hàng và dự trữ → C. A "NCC chịu trách nhiệm duy trì dự trữ" là **đặc trưng riêng của mô hình VMI** (dòng 2039-2044), KHÔNG nằm trong 3 yếu tố lựa chọn. Đề hỏi "KHÔNG bao gồm yếu tố nào" → A đúng. |
| 17 | A | ✅ ĐÚNG | Lecture dòng 2378-2389 liệt kê **lợi ích hữu hình của TCO** (4 mục): so sánh NCC, xác định tiềm năng tối ưu hóa, cải thiện minh bạch, xác định EOQ; **lợi ích vô hình** (3 mục): cải thiện giao tiếp nội bộ, tăng hiệu quả đàm phán, hữu ích cho phát triển SP. A "Cải thiện chiến lược mua" KHÔNG xuất hiện trong cả 2 nhóm → đề hỏi "KHÔNG bao gồm lợi ích nào" → A đúng. |
| 21 | A | ✅ ĐÚNG | Lecture dòng 2387 ghi rõ "Cải thiện giao tiếp nội bộ" thuộc nhóm **vô hình**, không phải hữu hình. Đề hỏi "Trong số những lợi ích **hữu hình** KHÔNG có khía cạnh nào" → A đúng (vì A thuộc vô hình → không có trong nhóm hữu hình). B/C/D đều thuộc hữu hình (dòng 2379-2381). |

> **Nguyên nhân nghi vấn ở round 2**: phần "Lời giải chi tiết" của solver dùng boilerplate "không khớp loại trừ" cho mọi phương án sai, không trích dòng bài giảng → reviewer round 2 không thấy bằng chứng nên nghi sai đáp án. Sau khi verify trực tiếp với lecture, **đáp án solver đúng nhưng lập luận yếu** — vấn đề thực tế là sư phạm + boilerplate, không phải sai đáp án.

## 📊 Điểm tổng quan

**Tổng: 6.1 / 10** — Verdict: **REVISE**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---:|---|
| Chính xác khái niệm/công thức | 6.5 | 8/8 câu mẫu khớp; nhưng Câu 16/17/21 có lỗi logic nghi vấn → trừ nặng. |
| Logic lập luận | 5 | Boilerplate; Câu 21 tự mâu thuẫn (vô hình mà loại trừ khỏi câu hữu hình). |
| Tính toán | 7 | EOQ, chi phí phù hợp đúng nhưng không trích công thức từ bài giảng (dòng 1908–1912). |
| Phù hợp ngữ cảnh VN | 7 | Có ví dụ Hòa Phát, Bách Hóa Xanh nhưng thiếu liên kết sâu với từng câu. |
| Sư phạm & chi tiết | 4.5 | "Sai lầm thường gặp" lặp boilerplate; thiếu bảng so sánh đáp án. |

## 🔍 Tự giải lại 8 câu mẫu (độc lập)

| Câu | Đáp án độc lập | Solver | Khớp | Bằng chứng bài giảng |
|---:|:---:|:---:|:---:|---|
| 1 | D (TCO) | D | ✓ | Dòng 1620+: định nghĩa TCO |
| 2 | C (áp lực tài chính) | C | ✓ | Dòng 1999–2003 |
| 10 | C (TCO) | C | ✓ | Định nghĩa lặp |
| 12 | B (không kiểm định) | B | ✓ | Dòng 1777–1780: liệt kê 3 "không" |
| 16 | A | A | ✓ | Đã verify 2026-06-13: A đúng vì A là đặc trưng VMI, KHÔNG nằm trong 3 yếu tố lựa chọn mô hình (dòng 2073–2078). Đề hỏi "KHÔNG bao gồm" → A. |
| 19 | A (chất lượng quá trình) | A | ✓ | Dòng 1667–1669 |
| 20 | D (khắc phục/làm lại) | D | ✓ | Dòng 1718–1719 |
| 26 | B (EOQ cân đối chi phí) | B | ✓ | Dòng 1896–1907 |

**Kết quả đối chiếu (sau verify 2026-06-13): 8/8 khớp đáp án.** Vấn đề còn lại nằm ở chất lượng lập luận, không phải đáp án.

## ⚠️ Vấn đề hệ thống

### 1. Lập luận Q21 thiếu nhất quán (đáp án A đúng, nhưng diễn giải gây hiểu nhầm)
Solver chọn đúng A "Cải thiện giao tiếp nội bộ" cho Q21. Tuy nhiên phần "Lời giải chi tiết" lại đưa C "Cải thiện tính minh bạch" vào diện "loại trừ" với cùng cụm boilerplate, khiến reviewer round 2 hiểu nhầm rằng solver tự mâu thuẫn về phân loại hữu hình/vô hình. **Cần viết lại Q21**: khẳng định A là **vô hình** (dòng 2387) → đáp án "hữu hình KHÔNG có" = A; B/C/D đều thuộc hữu hình (dòng 2379-2381).

### 2. Thiếu trích dẫn bài giảng cho khái niệm TCO/eProcurement
Solver không tìm và trích các đoạn bài giảng cụ thể về (a) lợi ích hữu hình vs vô hình của TCO, (b) yếu tố lựa chọn giữa các mô hình mua sắm. Reviewer dò bài giảng dòng 1620–2250 cũng không thấy bằng chứng phân biệt rõ.

### 3. Boilerplate cho phương án sai
Giống Ch1: hầu hết phương án sai đều dán mẫu "không khớp yêu cầu loại trừ" — không hữu ích sư phạm.

### 4. Lỗi chính tả (file chưa qua proofread)
Dòng 209, 388, 550 có ký tự lỗi "Gắờ" — gợi ý file solution chưa qua một vòng đọc lại.

### 5. Không có bảng so sánh
30 câu mà không có bảng tóm tắt đáp án đầu file để SV scan nhanh.

## 🎯 Đề xuất cho solver

1. ~~Verify lại Câu 16, 17, 21~~ → **Đã verify 2026-06-13**: cả 3 đáp án giữ A là đúng. KHÔNG đổi đáp án. Chỉ cần viết lại phần lập luận theo skill MCQ mới.
2. **Trích dòng bài giảng** cho mọi câu liên quan TCO (2376-2389), VMI (2039-2044), 3 yếu tố lựa chọn mô hình (2073-2078), EOQ (1896-1907) — bài giảng có đủ wording chuẩn.
3. **Sửa lỗi chính tả** "Gắờ" ở dòng 209, 388, 550 (lỗi OCR còn sót).
4. **Phân tích A-B-C-D riêng** cho từng câu theo template MCQ mới trong `skills/exercise-solver/SKILL.md` — bỏ boilerplate "không khớp yêu cầu loại trừ".
5. **Thêm bảng so sánh 6 mô hình mua** ở đầu solution (mua nhiều/NCC phụ trách 1 phần/phần lớn/ký gửi/VMI/JIT).

## ✅ Đánh giá tổng kết
Đáp án **8/8 câu mẫu đã verify đều đúng**. Vấn đề thực tế là **chất lượng lập luận**: boilerplate khắp các câu, thiếu trích dòng bài giảng, lỗi chính tả OCR còn sót. **REVISE_MINOR** — không đổi đáp án, chỉ rewrite phần lập luận theo skill MCQ mới (cùng nhóm task với T-20260611-08, nay đã mở rộng cho Mua & QTNC).
