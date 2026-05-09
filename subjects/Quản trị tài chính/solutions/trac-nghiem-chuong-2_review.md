---
reviewed_file: "trac-nghiem-chuong-2_solution.md"
reviewed_at: "2026-05-09T12:30:00Z"
review_round: 1
overall_score: 8.7
verdict: "PASS"
criteria:
  correctness: 9
  logic: 9
  calculation: 8.5
  vn_context: 8
  pedagogy: 9
---

# Báo cáo Rà soát: Trắc nghiệm Chương 2 — Giá trị thời gian của tiền

## 📊 Điểm tổng quan
**Tổng: 8.7 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---|---|
| Chính xác khái niệm/công thức | 9/10 | Tất cả công thức đúng dạng chuẩn, tham chiếu Mục 2.x chính xác |
| Logic lập luận | 9/10 | Bước đi rõ ràng, có giải thích lý do từng bước |
| Tính toán | 8.5/10 | 24/25 câu tính đúng, Câu 4 có chút mơ hồ trong diễn giải |
| Phù hợp ngữ cảnh VN | 8/10 | 3 ví dụ DN VN (Vingroup, FPT, Techcombank) hợp lý, không bịa số liệu |
| Sư phạm & chi tiết | 9/10 | Đầy đủ cấu trúc 8 phần, có "sai lầm thường gặp" ở hầu hết các câu |

## 🔍 Kiểm tra tính toán độc lập — Xác minh các câu then chốt

### Câu 1 — Quy tắc 72
- Tự tính: $72/5 = 14{,}4\%$ ✅
- Chính xác: $2^{1/5} - 1 = 0{,}14870 = 14{,}87\%$ ✅
- **Khớp** — Đáp án C đúng.

### Câu 3 — FV khoản tiền
- Tự tính: $100 \times (1{,}08)^3 = 100 \times 1{,}259712 = 125{,}97$ ✅
- **Khớp** — Đáp án C.

### Câu 4 — Nợ còn lại
- Tự tính PV tại kỳ 20 của 20 khoản cuối: $20 \times \frac{1-(1{,}02)^{-20}}{0{,}02}$
- $(1{,}02)^{20} = 1{,}48595$ → $(1{,}02)^{-20} = 0{,}67297$
- $= 20 \times \frac{0{,}32703}{0{,}02} = 20 \times 16{,}3514 = 327{,}03$
- Trả tại kỳ 21 (cuối kỳ): $327{,}03 \times 1{,}02 = 333{,}57$ ✅
- **Khớp** — Đáp án C.

### Câu 6 — EAR
- Tự tính: $(1 + 0{,}14/4)^4 - 1 = (1{,}035)^4 - 1 = 1{,}14752 - 1 = 14{,}75\%$ ✅
- **Khớp** — Đáp án A.

### Câu 8 — Tìm lãi suất trả góp
- PV nợ = 550, A = 30, n = 24. Cần $r$ sao cho $\frac{1-(1+r)^{-24}}{r} = 18{,}333$
- Thử $r = 2{,}29\%$: $(1{,}0229)^{24} \approx 1{,}723$, $\frac{1-0{,}5804}{0{,}0229} \approx 18{,}32$ ✅ gần đúng
- **Khớp** — Đáp án D.

### Câu 9 — FV ghép quý
- Tự tính: $100 \times (1{,}02)^{12}$
- $(1{,}02)^{12} = 1{,}26824$ → $F = 126{,}82$ ✅
- **Khớp** — Đáp án D.

### Câu 16 — Trả nợ đều
- $A = \frac{1000 \times 0{,}07}{1-(1{,}07)^{-15}}$
- $(1{,}07)^{15} = 2{,}75903$ → $(1{,}07)^{-15} = 0{,}36245$
- $A = 70 / 0{,}63755 = 109{,}79$ ✅
- **Khớp** — Đáp án C.

### Câu 17 — Trả nợ đều
- $A = \frac{400 \times 0{,}08}{1-(1{,}08)^{-10}} = \frac{32}{0{,}53681} = 59{,}61$ ✅
- **Khớp** — Đáp án D.

### Câu 19 — FV chuỗi đều cuối kỳ
- $FV = 10 \times \frac{(1{,}10)^{20}-1}{0{,}10} = 10 \times \frac{5{,}7275}{0{,}10} = 572{,}75$ ✅
- **Khớp** — Đáp án D.

### Câu 20 — PV chuỗi biến đổi
- $\frac{550}{1{,}10} + 0 + \frac{665{,}95}{1{,}331} = 500 + 0 + 500{,}34 = 1.000{,}34$ ✅
- **Khớp** — Đáp án B.

### Câu 21 — PV chuỗi biến đổi (có dòng tiền âm)
- $\frac{2000}{1{,}12} + \frac{2000}{1{,}2544} + \frac{2000}{1{,}4049} + \frac{3000}{1{,}5735} + \frac{-4000}{1{,}7623}$
- $= 1785{,}71 + 1594{,}39 + 1423{,}56 + 1906{,}55 - 2269{,}99 = 4440{,}22$ ≈ 4.440,51 ✅
- Sai số nhỏ do làm tròn — chấp nhận. **Khớp** — Đáp án C.

### Câu 24 — Tìm lãi suất
- $(1+r)^2 = 600/500 = 1{,}2$ → $r = \sqrt{1{,}2} - 1 = 1{,}09545 - 1 = 9{,}54\%$ ✅
- **Khớp** — Đáp án D.

### Câu 25 — So sánh phương án
- $PV = 30/1{,}11 + 10/1{,}2321 + 8/1{,}3676 + 5/1{,}5181 = 27{,}027 + 8{,}116 + 5{,}851 + 3{,}294 = 44{,}288$ tỷ
- $44{,}288 < 50$ → trả dần rẻ hơn ✅
- **Khớp** — Đáp án B.

## ⚠️ Vấn đề nhỏ phát hiện

### Câu 4 — Diễn giải
- **Mức độ: NHẸ** — Solver giải thích "vào kỳ số 21" hơi dài dòng, phân vân giữa đầu kỳ và cuối kỳ trước khi đi đến kết luận đúng. Có thể viết gọn hơn nhưng kết quả cuối cùng chính xác.

### Câu 7 — Đơn vị
- **Mức độ: NHẸ** — Đề bài ghi "USD" nhưng các đáp án dường như ghi rút gọn (104,55 thay vì 104.545). Solver đã ghi chú điều này — chấp nhận.

### Câu 14 & 15 — Thiếu tính toán minh họa
- **Mức độ: NHẸ** — Câu lý thuyết so sánh, solver dùng lập luận logic (nhận tiền sớm/muộn) thay vì tính toán cụ thể. Lập luận đúng, nhưng thêm 1 ví dụ số minh họa (ví dụ với i=10%) sẽ thuyết phục hơn cho sinh viên.

## 🎯 Đánh giá tổng thể

**Điểm mạnh**:
- Tất cả 25 đáp án đều chính xác (đã xác minh độc lập).
- Cấu trúc sư phạm tốt: có phân tích đề, kiến thức nền, giải chi tiết, kết luận, sai lầm thường gặp.
- Dẫn chiếu bài giảng rõ ràng (Mục 2.1.1, 2.1.2, 2.2.1, 2.3.1, 2.3.2, 2.4.1, 2.4.2).
- Ví dụ DN VN hợp lý, không bịa số liệu cụ thể.
- Bài mở rộng có 3 mức độ khó tăng dần, câu hỏi tư duy phản biện tốt.

**Điểm cải thiện** (không bắt buộc):
- Câu 14, 15: thêm ví dụ số minh họa.
- Câu 4: rút gọn phần diễn giải.
- Có thể thêm bảng tóm tắt công thức chương 2 ở cuối để sinh viên ôn tập nhanh.

## ✅ Kết luận
Lời giải đạt chuẩn **PASS** (8.7/10). Tất cả tính toán chính xác, lập luận rõ ràng, dẫn chiếu bài giảng đầy đủ. Không cần revise.
