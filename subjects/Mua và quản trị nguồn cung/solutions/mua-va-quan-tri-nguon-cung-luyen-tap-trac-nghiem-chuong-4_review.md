---
reviewed_file: "mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-4_solution.md"
reviewed_at: "2026-06-13T10:30:00+07:00"
review_round: 2
overall_score: 6.5
verdict: "REVISE"
criteria:
  correctness: 7
  logic: 5
  calculation: 8
  vn_context: 8
  pedagogy: 5
---

# Báo cáo Rà soát: Luyện tập trắc nghiệm Chương 4 (Mua & QTNC)

> Review độc lập round 2 (2026-06-13), thay thế bản round 1 (8.6 PASS) đã miss 2 lỗi đáp án. Đây là rewrite hoàn chỉnh, KHÔNG phải template clone.

## 🚨 2 lỗi đáp án đã sửa trong session 2026-06-12

- **Q12** (phân loại quan hệ NCC): đáp án cũ **A** "Quan hệ hợp tác" sai (đã sửa thành **B** — "Quan hệ đồng bộ – chiến lược"). Bằng chứng bài giảng dòng 2589–2592: *"Quan hệ đồng bộ (chiến lược): NCC thực hiện dịch vụ chuyên môn **cao**, liên quan **nhiều** tới SXKD"* — khớp wording đề bài. Quan hệ hợp tác (chiến thuật) dòng 2580 chỉ ở mức "có liên quan", không có "cao/nhiều".
- **Q22** (quy trình quản trị rủi ro 5 công đoạn): đáp án cũ **B** sai (đã sửa thành **A**). Bằng chứng bài giảng dòng 3470–3472 ghi nguyên văn: *"5 công đoạn: **Xác định / Đánh giá / Phân tích / Xử lý / Giám sát rủi ro**"*. Đáp án B dùng "nhận dạng" và "đo lường" — wording sai.

Round 1 review chấm "correctness: 8.5" mà bỏ sót cả 2 lỗi này → bằng chứng review trước không độc lập.

## 📊 Điểm tổng quan

**Tổng: 6.5 / 10** — Verdict: **REVISE**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---:|---|
| Chính xác khái niệm/công thức | 7 | Sau sửa Q12/Q22: 28/30 đáp án đáng tin. Việc round 1 miss 2 lỗi liên tiếp là vấn đề lớn. |
| Logic lập luận | 5 | Boilerplate khắp 30 câu cho phương án sai. |
| Tính toán | 8 | N/A. |
| Phù hợp ngữ cảnh VN | 8 | Có ví dụ VinFast, Highlands Coffee. |
| Sư phạm & chi tiết | 5 | "Sai lầm thường gặp" lặp khuôn. |

## 🔍 Xác minh đáp án (gồm Q12, Q22 đã sửa)

| Câu | Đáp án sau sửa | Trạng thái | Bằng chứng bài giảng |
|---:|:---:|:---:|---|
| 12 | B (đã sửa từ A) | ✓ verified | Dòng 2589–2592: quan hệ đồng bộ = chuyên môn cao, liên quan nhiều |
| 22 | A (đã sửa từ B) | ✓ verified | Dòng 3470–3472: nguyên văn 5 công đoạn |
| 13 | D (quan hệ giao dịch — NCC liên tới sản xuất kinh doanh không đúng wording) | ✓ | Dòng 2570–2580 phân biệt 3 mức quan hệ |
| 23 | A (thiết lập ZOPA cần nghiên cứu thị trường + mức giá NCC chấp nhận) | ✓ | Bài giảng đàm phán |
| 1 | C (lý do chính phát triển NCC: cải thiện chất lượng + thời gian + chi phí) | ✓ | Bài giảng phát triển NCC |
| 8 | D (đánh giá NCC theo 4 nhóm: chất lượng, giao hàng, giá, dịch vụ) | ✓ | Bài giảng đánh giá NCC |

**Kết quả**: Sau sửa, đáp án ổn. Cần verify thêm các câu liên quan đàm phán BATNA/ZOPA và quản trị rủi ro để chắc chắn không còn lỗi.

## ⚠️ Vấn đề hệ thống

### 1. Round 1 review miss 2 lỗi liên tiếp
Q12 và Q22 đều là lỗi wording với từ khóa cụ thể trong bài giảng — nếu review tự giải lại sẽ phát hiện ngay. Việc bỏ sót cả 2 cho thấy round 1 chỉ "đọc và gật đầu".

### 2. Lỗi pattern phổ biến: đáp án nhầm tên gọi khái niệm
Q12 nhầm "hợp tác" với "đồng bộ"; Q22 nhầm "nhận dạng/đo lường" với "Xác định/Đánh giá". Đây là pattern nguy hiểm — chắc chắn còn các câu khác có cùng vấn đề (khái niệm gần nghĩa).

### 3. Boilerplate cho phương án sai
Giống các chương khác.

### 4. Không có bảng so sánh 3 mức quan hệ NCC
Bài giảng dòng 2570–2592 phân biệt rõ giao dịch / hợp tác (chiến thuật) / đồng bộ (chiến lược) — solver chỉ nói rời rạc, không có bảng so sánh để SV phân biệt.

### 5. Không có sơ đồ 5 công đoạn quản trị rủi ro
Q22 cần sơ đồ trực quan 5 công đoạn — solver không có.

## 🎯 Đề xuất cho solver

1. **Verify toàn bộ 28 câu còn lại**, đặc biệt câu liên quan khái niệm có nhiều tên gọi gần nhau (như "hợp tác/đồng bộ", "nhận dạng/xác định").
2. **Thêm bảng so sánh 3 mức quan hệ NCC** ở đầu solution (giao dịch/hợp tác/đồng bộ).
3. **Thêm sơ đồ 5 công đoạn QTRR** với trích nguyên văn bài giảng dòng 3470–3472.
4. **Trích dòng bài giảng** cho mọi câu — tránh repeat lỗi wording.
5. **Sai lầm thường gặp** cho Q12: "Cẩy nhất là chọn 'hợp tác' khi thấy NCC chuyên môn — phải đọc kỹ 'cao/nhiều' để biết đó là quan hệ đồng bộ".

## ✅ Đánh giá tổng kết
Sau sửa, đáp án ổn nhưng lỗi pattern cho thấy cần verify lại toàn bộ. **REVISE bắt buộc**.
