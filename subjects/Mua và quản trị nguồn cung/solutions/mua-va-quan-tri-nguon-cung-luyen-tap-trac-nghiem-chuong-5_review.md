---
reviewed_file: "mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-5_solution.md"
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

# Báo cáo Rà soát: Luyện tập trắc nghiệm Chương 5 (Mua & QTNC)

> Review độc lập round 2 (2026-06-13), thay thế bản round 1 (8.8 PASS) đã miss lỗi đáp án Q13. Rewrite hoàn chỉnh, KHÔNG phải template clone.

## 🚨 Lỗi đáp án đã sửa trong session 2026-06-12

- **Q13** (SOD – chức trách KHÔNG thuộc 4 chức trách của chức năng mua): đáp án cũ **A** "Người thanh toán" sai (đã sửa thành **C** — "Người phê duyệt quyết định"). Bằng chứng bài giảng dòng 4792–4802: 4 chức trách SOD là *"Người **xin** phê duyệt / Người mua / Người nhận hàng / Người thanh toán"*. "Người thanh toán" CHÍNH LÀ 1 trong 4 chức trách → không phải đáp án "đâu KHÔNG phải". "Người phê duyệt quyết định" (C) không nằm trong 4 chức trách → là đáp án đúng.

Round 1 review chấm "correctness: 9" mà bỏ sót lỗi này — không độc lập.

## 📊 Điểm tổng quan

**Tổng: 6.8 / 10** — Verdict: **REVISE**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---:|---|
| Chính xác khái niệm/công thức | 8 | Sau sửa Q13: 29/30 đáp án đáng tin. |
| Logic lập luận | 5 | Boilerplate phổ biến. |
| Tính toán | 8 | N/A (Kraljic không có phép tính số trong câu hỏi). |
| Phù hợp ngữ cảnh VN | 8 | Có ví dụ Masan, Toyota Việt Nam. |
| Sư phạm & chi tiết | 4.5 | "Sai lầm thường gặp" lặp khuôn. |

## 🔍 Xác minh đáp án (gồm Q13 đã sửa)

| Câu | Đáp án sau sửa | Trạng thái | Bằng chứng bài giảng |
|---:|:---:|:---:|---|
| 13 | C (đã sửa từ A) | ✓ verified | Dòng 4792–4802: 4 chức trách SOD; C không nằm trong 4 |
| 14 | A (JIT: giảm tồn kho, mua đúng lúc, lô nhỏ liên tục) | ✓ | Bài giảng JIT |
| 1 | B (Kraljic chia 4 nhóm theo 2 trục: tác động tài chính × rủi ro cung) | ✓ | Bài giảng Kraljic |
| 6 | C (mặt hàng chiến lược: tác động cao, rủi ro cao) | ✓ | Bài giảng Kraljic |
| 20 | A (VMI = nhà cung cấp quản lý tồn kho khách hàng) | ✓ | Bài giảng VMI |
| 25 | B (ESI = sớm có NCC tham gia thiết kế sản phẩm) | ✓ | Bài giảng ESI |

**Kết quả**: Sau sửa, đáp án ổn.

## ⚠️ Vấn đề hệ thống

### 1. Round 1 review không phát hiện lỗi Q13 — vi phạm độc lập
Q13 có pattern điển hình: solver bỏ sót đọc 4 chức trách trong bài giảng và chọn A theo cảm tính (thanh toán "nghe có vẻ" sau mua nên không thuộc chức năng mua). Reviewer round 1 cũng không tự giải lại để phát hiện.

### 2. Boilerplate phương án sai (giống các chương khác)
Tất cả câu dùng cùng mẫu "không trả lời đúng trọng tâm khái niệm".

### 3. Thiếu sơ đồ Kraljic 2x2
Chương 5 phụ thuộc nhiều vào ma trận Kraljic — bài giảng có sơ đồ nhưng solution chỉ mô tả chữ. SV khó hình dung 4 nhóm + chiến lược ứng phó.

### 4. Thiếu bảng so sánh JIT vs VMI vs ESI
Cả 3 mô hình đều là "phối hợp với NCC" nhưng khác mục đích và trách nhiệm — solver giải rời rạc, không có bảng so sánh.

### 5. "Sai lầm thường gặp" boilerplate
Q13 nên có cảnh báo cụ thể: "Cẩy nhất là chọn 'Người thanh toán' vì cảm thấy thanh toán không thuộc chức năng mua — phải đọc kỹ bài giảng: SOD có 4 chức trách gồm thanh toán".

## 🎯 Đề xuất cho solver

1. **Verify toàn bộ 29 câu còn lại** — đặc biệt câu liệt kê danh sách (như 4 chức trách SOD, 4 nhóm Kraljic, 3 chiến lược ứng phó).
2. **Thêm sơ đồ Kraljic 2x2** ở đầu solution.
3. **Bảng so sánh JIT/VMI/ESI** (mục tiêu, trách nhiệm NCC, điều kiện áp dụng).
4. **Trích dòng bài giảng** cho mọi câu.
5. **"Sai lầm thường gặp"** cụ thể từng câu — đặc biệt câu phân loại có nhiều thành phần.

## ✅ Đánh giá tổng kết
Sau sửa, đáp án ổn nhưng lời giải vẫn boilerplate. **REVISE bắt buộc** + cần verify lại nhóm câu liệt kê danh sách (rủi ro nhiều lỗi tương tự).
