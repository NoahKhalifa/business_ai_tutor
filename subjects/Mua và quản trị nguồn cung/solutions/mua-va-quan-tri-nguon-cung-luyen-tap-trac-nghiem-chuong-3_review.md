---
reviewed_file: "mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-3_solution.md"
reviewed_at: "2026-06-13T10:00:00+07:00"
review_round: 2
overall_score: 6.1
verdict: "REVISE"
criteria:
  correctness: 6.5
  logic: 5
  calculation: 7
  vn_context: 7
  pedagogy: 4.5
---

# Báo cáo Rà soát: Luyện tập trắc nghiệm Chương 3 (Mua & QTNC)

> Lần review này được thực hiện độc lập 2026-06-13 (round 2), thay thế bản review round 1 (8.5 PASS) đã được phát hiện là *clone template*. Reviewer tự giải 8 câu trước khi đọc lời giải.

## 🚨 Lỗi nghi vấn phát hiện trong lần re-review này

**Câu 16, 17, 21 — có khả năng lỗi đáp án hoặc lỗi lập luận:**
- **Câu 16**: Solver chọn A "NCC chịu trách nhiệm duy trì dự trữ". Reviewer phân tích đây CHÍNH LÀ đặc trưng quyết định của mô hình VMI (bài giảng dòng 2039–2044) → có thể đáp án đúng là B hoặc D theo bài giảng dòng 2073–2078.
- **Câu 21**: Solver giải thích C "cải thiện giao tiếp nội bộ" là lợi ích **vô hình** của TCO nhưng vẫn đưa vào danh sách phương án để loại trừ khi đề hỏi lợi ích **hữu hình** — tự mâu thuẫn.
- **Câu 17**: Solver dựa vào suy đoán "hữu hình/vô hình" mà không có dòng bài giảng cụ thể chứng minh.

> ⚠️ **Cần verify tay 3 câu này** trước khi sửa solution. Reviewer chưa khẳng định 100% là sai (chỉ phát hiện logic không khớp). Đã ghi vào TODO mục mới [T-20260613-01].

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
| 16 | **B hoặc D** ⚠ | A | ✗ | Dòng 2073–2078 nói rõ yếu tố lựa chọn mô hình; A là đặc trưng VMI cụ thể |
| 19 | A (chất lượng quá trình) | A | ✓ | Dòng 1667–1669 |
| 20 | D (khắc phục/làm lại) | D | ✓ | Dòng 1718–1719 |
| 26 | B (EOQ cân đối chi phí) | B | ✓ | Dòng 1896–1907 |

**Kết quả đối chiếu: 7/8 khớp, 1/8 nghi vấn lỗi (Câu 16).**

## ⚠️ Vấn đề hệ thống

### 1. Lỗi logic tự mâu thuẫn (Câu 17, 21)
Câu 21 hỏi lợi ích **hữu hình** của TCO, đề liệt kê C "cải thiện giao tiếp nội bộ". Solver giải thích "đây là lợi ích **vô hình**" rồi vẫn xếp C vào nhóm "không khớp yêu cầu loại trừ" — không nhất quán. Nếu vô hình thì C chính là đáp án "hữu hình KHÔNG có", không phải "không khớp loại trừ".

### 2. Thiếu trích dẫn bài giảng cho khái niệm TCO/eProcurement
Solver không tìm và trích các đoạn bài giảng cụ thể về (a) lợi ích hữu hình vs vô hình của TCO, (b) yếu tố lựa chọn giữa các mô hình mua sắm. Reviewer dò bài giảng dòng 1620–2250 cũng không thấy bằng chứng phân biệt rõ.

### 3. Boilerplate cho phương án sai
Giống Ch1: hầu hết phương án sai đều dán mẫu "không khớp yêu cầu loại trừ" — không hữu ích sư phạm.

### 4. Lỗi chính tả (file chưa qua proofread)
Dòng 209, 388, 550 có ký tự lỗi "Gắờ" — gợi ý file solution chưa qua một vòng đọc lại.

### 5. Không có bảng so sánh
30 câu mà không có bảng tóm tắt đáp án đầu file để SV scan nhanh.

## 🎯 Đề xuất cho solver

1. **Verify lại Câu 16, 17, 21**: Mở bài giảng đoạn 2039–2078 đối chiếu kỹ — có thể cần đổi đáp án Câu 16 hoặc viết lại phần lập luận Câu 17, 21.
2. **Trích dòng bài giảng** cho mọi câu liên quan TCO, VMI, EOQ — bài giảng có đủ wording chuẩn.
3. **Sửa lỗi chính tả** "Gắờ" ở dòng 209, 388, 550.
4. **Phân tích A-B-C-D riêng** cho từng câu thay vì boilerplate.
5. **Thêm bảng so sánh 3 mô hình** mua (truyền thống/VMI/JIT) ở đầu solution.

## ✅ Đánh giá tổng kết
Đáp án phần lớn đúng nhưng có 1 nghi vấn lớn (Câu 16) và lỗi logic tự mâu thuẫn (Câu 17, 21). **REVISE bắt buộc** + cần verify đáp án Câu 16 trước khi dùng chính thức.
