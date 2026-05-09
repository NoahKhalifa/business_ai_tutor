---
parent_solution: "solutions/trac-nghiem-chuong-4_solution.md"
created_at: "2026-05-09T15:15:00Z"
---

# Mở rộng & Luyện tập: Trắc nghiệm Chương 4 — Quản trị Vốn lưu động

## 🎯 Bài tập tham khảo (tự luyện)

### Bài luyện 1 — Cơ bản (★)

**Đề**: DN có tổng nhu cầu chi tiền trong năm là 5 tỷ đồng. Chi phí mỗi lần chuyển CK thành tiền là 500.000 đồng, tỷ suất sinh lợi CK là 10%/năm. Tính lượng tiền dự trữ tối ưu theo Baumol (BAT).

**Gợi ý**: $C^* = \sqrt{2BT/i}$, đổi về cùng đơn vị triệu đồng.

<details>
<summary>Đáp án rút gọn</summary>

$C^* = \sqrt{2 \times 0{,}5 \times 5.000 / 0{,}1} = \sqrt{50.000} \approx 223{,}6$ triệu đồng.
Số lần chuyển hoán: 5.000/223,6 ≈ 22,4 lần/năm.
</details>

### Bài luyện 2 — Trung bình (★★)

**Đề**: Công ty ABC có các thông tin:
- Giá vốn hàng bán: 7.200 triệu/năm
- HTK bình quân: 800 triệu
- Doanh thu bán chịu: 9.000 triệu/năm
- KPThu bình quân: 750 triệu
- KPTrả bình quân: 600 triệu

1. Tính CCC.
2. Nếu công ty giảm được ICP xuống 30 ngày (từ mức hiện tại), CCC mới là bao nhiêu?
3. Đánh giá tác động lên nhu cầu vốn lưu động.

**Gợi ý**: Tính ICP, ACP, PDP từ công thức vòng quay rồi chia 365.

<details>
<summary>Đáp án rút gọn</summary>

1. Vòng quay HTK = 7.200/800 = 9 → ICP = 365/9 ≈ 40,6 ngày
   Vòng quay KPThu = 9.000/750 = 12 → ACP = 365/12 ≈ 30,4 ngày
   Vòng quay KPTrả = 7.200/600 = 12 → PDP = 365/12 ≈ 30,4 ngày
   **CCC = 40,6 + 30,4 - 30,4 = 40,6 ngày**

2. Nếu ICP = 30 ngày → CCC mới = 30 + 30,4 - 30,4 = **30 ngày** (giảm 10,6 ngày)

3. Giảm CCC 10,6 ngày → giảm nhu cầu vốn lưu động khoảng: (9.000/365) × 10,6 ≈ **261 triệu đồng**
</details>

### Bài luyện 3 — Nâng cao (★★★)

**Đề**: Công ty sản xuất X đang cân nhắc giữa 3 chính sách đầu tư TSNH:

| Chính sách | Mức TSNH | Doanh thu | TSCĐ | Nợ NH | Chi phí hoạt động |
|---|---|---|---|---|---|
| Cởi mở | 2.000 tỷ | 5.000 tỷ | 3.000 tỷ | 1.500 tỷ | 4.200 tỷ |
| Trung dung | 1.500 tỷ | 5.000 tỷ | 3.000 tỷ | 1.500 tỷ | 4.100 tỷ |
| Hạn chế | 1.000 tỷ | 4.800 tỷ | 3.000 tỷ | 1.500 tỷ | 4.000 tỷ |

1. Tính ROI (Thu nhập thuần/Tổng TS) cho mỗi chính sách (thuế suất 20%).
2. Tính VLĐ ròng và hệ số thanh toán hiện hành cho mỗi chính sách.
3. Chính sách nào phù hợp với DN muốn ưu tiên an toàn? Chính sách nào cho DN muốn tối đa sinh lời?

<details>
<summary>Đáp án rút gọn</summary>

**Cởi mở**: LNST = (5.000 - 4.200) × 0,8 = 640. ROI = 640/5.000 = **12,8%**. VLĐ ròng = 500, CR = 1,33
**Trung dung**: LNST = (5.000 - 4.100) × 0,8 = 720. ROI = 720/4.500 = **16,0%**. VLĐ ròng = 0, CR = 1,0
**Hạn chế**: LNST = (4.800 - 4.000) × 0,8 = 640. ROI = 640/4.000 = **16,0%**. VLĐ ròng = -500, CR = 0,67

- **An toàn**: Cởi mở (VLĐ ròng dương, CR > 1)
- **Tối đa sinh lời**: Trung dung hoặc Hạn chế (ROI = 16%), nhưng Hạn chế rủi ro rất cao (CR < 1)
</details>

---

## 📖 Đào sâu kiến thức

### Khái niệm liên quan
- **Mô hình Miller-Orr**: Mở rộng Baumol cho dòng tiền biến động ngẫu nhiên. Xác định giới hạn trên H, giới hạn dưới L, và mức tồn quỹ tối ưu Z*
- **Phân loại ABC**: Kỹ thuật Pareto 80/20 — Nhóm A (70-80% giá trị, 10-20% SL), B (15-20%, 30%), C (5%, 50%)
- **Điểm tái đặt hàng (ROP)**: Mức HTK tối thiểu để khởi phát đơn đặt hàng mới = Mức tiêu thụ/ngày × Thời gian mua hàng

### Công thức nâng cao: Miller-Orr

$$Z^* = \sqrt[3]{\frac{3B\sigma^2}{4i}} + L$$

$$H^* = 3Z^* - 2L$$

Trong đó $\sigma^2$ là phương sai dòng tiền thuần hàng ngày, $L$ là giới hạn dưới.

---

## 🤔 Câu hỏi tư duy phản biện

1. **JIT có phù hợp với mọi DN Việt Nam?** Hãy phân tích tại sao nhiều DN vừa và nhỏ VN vẫn chọn dự trữ HTK lớn thay vì áp dụng JIT.
2. **CCC âm có tốt không?** Apple có CCC âm (khoảng -35 ngày). Điều này có nghĩa gì và DN VN nào có thể đạt được?
3. **Mô hình Baumol có ứng dụng thực tế không?** Trong thời đại thanh toán điện tử, DN còn cần dự trữ tiền mặt theo mô hình Baumol không?

---

## 📚 Đọc thêm
- Sách: **Van Horne & Wachowicz** — *Fundamentals of Financial Management* — Chương 8-9
- Sách: **Giáo trình Quản trị Tài chính** — Đại học Thương mại — Chương 4
- Case study: **Toyota Production System** — ví dụ kinh điển về JIT

---

## 🔗 Liên kết với các bài khác

| Mối liên kết | Chương |
|---|---|
| Chương 4 cần kiến thức từ | Chương 3 (Phân tích BCTC — tỷ số hoạt động, thanh khoản) |
| Chương 4 là nền tảng cho | Chương 5 (Đầu tư dài hạn — dòng tiền dự án); Chương 6 (Tài trợ — cấu trúc vốn tối ưu) |
