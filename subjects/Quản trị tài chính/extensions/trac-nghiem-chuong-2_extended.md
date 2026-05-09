---
parent_solution: "solutions/trac-nghiem-chuong-2_solution.md"
created_at: "2026-05-09T12:00:00Z"
---

# Mở rộng & Luyện tập: Chương 2 — Giá trị thời gian của tiền

## 🎯 Bài tập tham khảo (tự luyện)

### Bài luyện 1 — Cơ bản (★): Giá trị tương lai khoản tiết kiệm

**Đề**: Bạn gửi 200 triệu đồng vào ngân hàng với lãi suất 9%/năm, ghép lãi hàng năm. Hỏi sau 5 năm, bạn nhận được bao nhiêu tiền (cả gốc và lãi)?

**Gợi ý**: Áp dụng công thức $FV = PV \times (1+i)^n$

<details>
<summary>Đáp án rút gọn</summary>

$$FV = 200 \times (1{,}09)^5 = 200 \times 1{,}53862 = 307{,}72 \text{ triệu đồng}$$

Tiền lãi thu được = $307{,}72 - 200 = 107{,}72$ triệu.
</details>

---

### Bài luyện 2 — Trung bình (★★): So sánh lãi đơn và lãi ghép

**Đề**: Bạn có 500 triệu đồng, có 2 lựa chọn đầu tư trong 10 năm:
- **Phương án A**: Trái phiếu trả lãi đơn 10%/năm
- **Phương án B**: Gửi tiết kiệm lãi ghép 9%/năm

Phương án nào mang lại nhiều tiền hơn sau 10 năm? Chênh lệch bao nhiêu?

**Gợi ý**: Tính $FV$ theo lãi đơn: $F = P(1+rn)$ và lãi ghép: $F = P(1+r)^n$

<details>
<summary>Đáp án rút gọn</summary>

- Phương án A (lãi đơn): $F = 500 \times (1 + 0{,}10 \times 10) = 500 \times 2 = 1.000$ triệu
- Phương án B (lãi ghép): $F = 500 \times (1{,}09)^{10} = 500 \times 2{,}36736 = 1.183{,}68$ triệu

Phương án B nhiều hơn $1.183{,}68 - 1.000 = 183{,}68$ triệu, dù lãi suất thấp hơn 1%.

**Bài học**: Lãi ghép luôn thắng lãi đơn khi $n > 1$, nhờ hiệu ứng "lãi mẹ đẻ lãi con".
</details>

---

### Bài luyện 3 — Nâng cao (★★★): Lập kế hoạch trả nợ + dòng tiền hỗn hợp

**Đề**: Công ty ABC vay ngân hàng 2 tỷ đồng, lãi suất 10%/năm, trả đều cuối mỗi năm trong 8 năm. Đồng thời, công ty dự kiến có luồng thu nhập từ dự án mới vào cuối các năm 1-8 lần lượt là: 500, 600, 700, 800, 400, 300, 200, 100 (triệu đồng).

a) Tính số tiền trả nợ đều mỗi năm.
b) Tính giá trị hiện tại của luồng thu nhập dự án (chiết khấu 10%).
c) Luồng thu nhập có đủ để trả nợ hàng năm không?

**Gợi ý**: 
- Phần a: dùng công thức vay trả cố định
- Phần b: PV chuỗi biến đổi cuối kỳ
- Phần c: so sánh dòng tiền ròng từng năm

<details>
<summary>Đáp án rút gọn</summary>

a) $A = \frac{2.000 \times 0{,}10}{1-(1{,}10)^{-8}} = \frac{200}{1-0{,}46651} = \frac{200}{0{,}53349} = 374{,}87$ triệu/năm

b) $PV = \frac{500}{1{,}10} + \frac{600}{1{,}21} + \frac{700}{1{,}331} + \frac{800}{1{,}4641} + \frac{400}{1{,}6105} + \frac{300}{1{,}7716} + \frac{200}{1{,}9487} + \frac{100}{2{,}1436}$

$= 454{,}5 + 495{,}9 + 525{,}9 + 546{,}6 + 248{,}4 + 169{,}3 + 102{,}6 + 46{,}7 = 2.589{,}9$ triệu

c) PV thu nhập (2.589,9 triệu) > PV nợ (2.000 triệu) → Đủ trả. Tuy nhiên cần kiểm tra từng năm: năm 7 và 8 thu nhập thấp (200, 100) < trả nợ (374,87) → dòng tiền âm, cần dự phòng.
</details>

---

## 📖 Đào sâu kiến thức

### Khái niệm liên quan cần biết thêm

- **Lãi suất thực (Real interest rate)**: Lãi suất sau khi trừ lạm phát. Công thức Fisher: $1+r_{nominal} = (1+r_{real})(1+\pi)$. Quan trọng khi đánh giá dự án dài hạn. — Tham chiếu: Brealey, Myers & Allen, Ch. 3.

- **Giá trị hiện tại ròng (NPV)**: Mở rộng của PV chuỗi tiền, có trừ chi phí đầu tư ban đầu: $NPV = \sum \frac{CF_t}{(1+r)^t} - C_0$. Nếu $NPV > 0$ → dự án đáng đầu tư. Sẽ học kỹ ở Chương 5.

- **Lãi suất liên tục (Continuous compounding)**: Khi tần suất ghép lãi $m \to \infty$: $F = P \times e^{rt}$. Dùng nhiều trong định giá quyền chọn (Black-Scholes).

### Mối liên hệ với các chương khác

| Chương | Liên hệ với Chương 2 |
|--------|---------------------|
| Chương 3 (Rủi ro & tỷ suất sinh lời) | Lãi suất chiết khấu phản ánh rủi ro — rủi ro cao → chiết khấu cao → PV thấp |
| Chương 5 (Thẩm định dự án) | NPV, IRR đều dựa trên TVM |
| Chương 6 (Định giá trái phiếu) | Giá trái phiếu = PV coupon + PV mệnh giá |
| Chương 7 (Định giá cổ phiếu) | Mô hình DDM = PV chuỗi cổ tức vĩnh viễn |

---

## 🧠 Câu hỏi tư duy phản biện

1. **Nếu lạm phát tăng mạnh**, giá trị thời gian của tiền sẽ thay đổi như thế nào? Tại sao các ngân hàng trung ương thường tăng lãi suất trong thời kỳ lạm phát cao?

2. **Quy tắc 72 có chính xác ở mọi mức lãi suất không?** Hãy thử so sánh kết quả Quy tắc 72 với công thức chính xác ở mức lãi suất 2%, 10%, và 50%. Rút ra nhận xét.

3. **Trong thực tế, tại sao người ta thường chọn trả góp** dù tổng số tiền danh nghĩa phải trả lớn hơn trả ngay? Phân tích từ góc độ giá trị thời gian của tiền và chi phí cơ hội.

4. **Nếu bạn là CFO của một công ty**, bạn sẽ dùng lãi suất nào làm tỷ lệ chiết khấu khi đánh giá dự án mới? Lãi suất ngân hàng, WACC, hay lãi suất yêu cầu của cổ đông? Vì sao?
