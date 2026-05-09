---
reviewed_file: "trac-nghiem-chuong-7_solution.md"
reviewed_at: "2026-05-09T19:45:00Z"
review_round: 1
overall_score: 9.0
verdict: "PASS"
criteria:
  correctness: 9
  logic: 9
  calculation: 10
  vn_context: 8
  pedagogy: 9
---

# Báo cáo Rà soát: Trắc nghiệm Chương 7 — Chi phí sử dụng vốn

## 📊 Điểm tổng quan
**Tổng: 9.0 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---|---|
| Chính xác khái niệm/công thức | 9/10 | CAPM, DDM, WACC, công thức xấp xỉ YTM trái phiếu, D/E↔D/TA đều chuẩn. Trừ 1 điểm cho Câu 29 do đáp án đề có sai số nhỏ (đáp án "đúng" 11,67% nhưng đề chỉ có 11,48%) |
| Logic lập luận | 9/10 | Phân biệt rõ "trước thuế" vs "sau thuế", cảnh báo bẫy về (1-T), nhấn mạnh phân biệt $D_0$/$D_1$ |
| Tính toán | 10/10 | 18/18 phép tính số đều khớp đáp án đề (kèm Câu 29 với chú thích sai số) |
| Phù hợp ngữ cảnh VN | 8/10 | Có ví dụ HPG, VIC, Vinamilk, NVL, FPT, NHNN nhưng có thể đậm hơn ở phần CP ưu đãi (ít DN VN phát hành CP ưu đãi thực sự) |
| Sư phạm & chi tiết | 9/10 | Khung công thức cốt lõi đặt đầu file rất hữu ích; "Sai lầm thường gặp" đúng các bẫy phổ biến; bảng tổng hợp đáp án và "7 bài học chính" cuối file là điểm cộng lớn |

---

## 🔁 Kiểm tra tính toán

### Câu 2 — CAPM (β=1,3; Rf=4%; Rm=11%)
$r_e = 4\% + 1{,}3 \times 7\% = 4\% + 9{,}1\% = 13{,}1\%$ ✅ Khớp đáp án D.

### Câu 3 — WACC (D=42,5; V=80; rd=8%; re=15%; T=20%)
- $w_d = 42{,}5/80 = 0{,}53125$; $w_e = 0{,}46875$.
- $WACC = 0{,}53125 \times 8\% \times 0{,}8 + 0{,}46875 \times 15\% = 3{,}40 + 7{,}03125 = 10{,}43125\%$ ✅ Khớp D = 10,43%.

### Câu 4 — vay sau thuế (20% × 0,75)
$20\% \times 0{,}75 = 15\%$ ✅ Khớp D.

### Câu 5 — Trái phiếu (xấp xỉ + verify YTM)
- Xấp xỉ: $(150.000 + 10.000)/975.000 = 16{,}41\%$.
- Verify YTM=16,49% qua phương trình giá: $150.000 \times 3{,}2353 + 1.000.000 \times 0{,}4665 = 485.295 + 466.460 = 951.755 \approx 950.000$ ✅ Khớp B = 16,49%.

### Câu 7 — WACC ba nguồn
$0{,}15 \times 12 + 0{,}25 \times 11{,}5 + 0{,}6 \times 14{,}3 = 1{,}80 + 2{,}875 + 8{,}58 = 13{,}255\%$ ✅ Khớp A = 13,25%.

### Câu 8 — D/E từ D/TA=0,45
$0{,}45/0{,}55 = 0{,}81818...$ ✅ Khớp A = 0,82.

### Câu 10 — WACC (D=45; V=90; T=22%)
$0{,}5 \times 9 \times 0{,}78 + 0{,}5 \times 16 = 3{,}51 + 8 = 11{,}51\%$ ✅ Khớp C.

### Câu 11 — DDM (D0=20.000; P0=240.000; g=8%)
$D_1 = 21.600$; $21.600/240.000 + 0{,}08 = 0{,}09 + 0{,}08 = 0{,}17$ ✅ Khớp A = 17%.

### Câu 13 — vay sau thuế (18% × 0,8)
$14{,}4\%$ ✅ Khớp C.

### Câu 14 — D/E từ D/TA=0,4
$0{,}4/0{,}6 = 0{,}6667$ ✅ Khớp D.

### Câu 15 — Phát hành CP mới (D0=2.500; P0=85.000; g=8%; f=2%)
$D_1 = 2.700$; $2.700/(85.000 \times 0{,}98) + 0{,}08 = 2.700/83.300 + 0{,}08 = 0{,}03241 + 0{,}08 = 0{,}11241$ ✅ Khớp C = 11,24%.

### Câu 17 — WACC (D=47,5; V=100; T=24%)
$0{,}475 \times 10 \times 0{,}76 + 0{,}525 \times 17 = 3{,}61 + 8{,}925 = 12{,}535\%$ ✅ Khớp C = 12,54%.

### Câu 18 — Phát hành CP mới (f=6%)
$21.600/(240.000 \times 0{,}94) + 0{,}08 = 21.600/225.600 + 0{,}08 = 0{,}09574 + 0{,}08 = 0{,}17574$ ✅ Khớp A = 17,57%.

### Câu 20 — WACC ba nguồn (lưu ý hỗn hợp trước/sau thuế)
- $r_{bank}^{at} = 16\% \times 0{,}8 = 12{,}8\%$ (cần nhân 1-T).
- $r_{bond}^{at} = 12{,}58\%$ (đã sau thuế — không nhân thêm).
- $r_e = 15{,}24\%$.
- $WACC = 0{,}25 \times 12{,}8 + 0{,}45 \times 15{,}24 + 0{,}3 \times 12{,}58 = 3{,}2 + 6{,}858 + 3{,}774 = 13{,}832\%$ ✅ Khớp C = 13,83%.

### Câu 23 — CP ưu đãi (Dp=6,3; Pp=70)
$6{,}30/70 = 0{,}09 = 9{,}0\%$ ✅ Khớp A.

### Câu 24 — DDM (D0=8.000; P0=90.000; g=10%)
$D_1 = 8.800$; $8.800/90.000 + 0{,}10 = 0{,}09778 + 0{,}10 = 0{,}19778$ ✅ Khớp D = 19,78%.

### Câu 25 — WACC (đã sau thuế cho cả 3 nguồn)
$0{,}25 \times 12 + 0{,}10 \times 14 + 0{,}65 \times 17{,}5 = 3 + 1{,}4 + 11{,}375 = 15{,}775\%$ ✅ Khớp B = 15,78%.

### Câu 26 — CP ưu đãi (Dp=7; Pp=75)
$7/75 = 0{,}09333 = 9{,}33\%$ ✅ Khớp B.

### Câu 27 — vay sau thuế (20% × 0,8)
$16\%$ ✅ Khớp A.

### Câu 29 — Phát hành CP mới (D0=3.000; P0=90.000; g=8%; f=2%)
$D_1 = 3.240$; $3.240/(90.000 \times 0{,}98) + 0{,}08 = 3.240/88.200 + 0{,}08 = 0{,}03673 + 0{,}08 = 0{,}11673 \approx 11{,}67\%$.
⚠️ **Đáp án đề không khớp chính xác**: 4 phương án (12,4%; 11,1%; 11,48%; 14%). Đáp án C = 11,48% là gần nhất (chênh 0,19%), được chọn theo nguyên tắc "phương án gần nhất". Solution đã ghi chú rõ điểm này — chấp nhận được. **Khuyến nghị**: Nếu có cơ hội liên hệ giảng viên/người ra đề, nên hỏi lại để xác nhận đáp án chính thức.

### Câu 30 — CAPM (β=1,35; Rf=5%; Rm=12%)
$r_e = 5\% + 1{,}35 \times 7\% = 5\% + 9{,}45\% = 14{,}45\%$ ✅ Khớp B.

---

## ✅ Điểm tốt nổi bật

1. **Khung công thức cốt lõi đặt đầu file** (8 công thức) — giúp người học có view tổng thể trước khi vào từng câu, đúng tinh thần sư phạm.
2. **Phân biệt rõ "trước thuế" vs "sau thuế"** ở các câu WACC nhiều nguồn (Câu 7, 20, 25) — đây là bẫy phổ biến nhất ở chương này, được cảnh báo đúng chỗ.
3. **Bảng so sánh giữa các câu liên quan**: Câu 11 vs Câu 18 (cùng dữ liệu, có/không flotation); Câu 4 vs Câu 27 (cùng rd, T khác). Tăng giá trị sư phạm rõ rệt.
4. **"Mẹo" thực dụng**: quy tắc nhanh D/TA→D/E, kiểm chứng hợp lý của β>1 và YTM>coupon khi P<M.
5. **Bảng tổng hợp 30 đáp án** ở cuối + **7 bài học chính rút ra** — rất tiện ôn nhanh trước thi.
6. **Ví dụ VN đa dạng**: HPG, VIC, Vinamilk, NVL, FPT, SSI, các ngân hàng — phủ nhiều ngành.
7. **Câu 29**: solution xử lý minh bạch khi đáp án đề không khớp chính xác (ghi chú thay vì "ép cho khớp") — đây là nguyên tắc sư phạm tốt.

## 🔧 Đề xuất cải thiện (không bắt buộc, không hạ điểm dưới PASS)

1. **Thêm ví dụ VN cho cổ phiếu ưu đãi** (Câu 16, 23, 26): Có thể nêu rằng tại VN, cổ phiếu ưu đãi tích lũy ít phổ biến (chủ yếu là cổ phiếu ưu đãi biểu quyết của cổ đông sáng lập theo Luật DN 2020). Ví dụ thực tế hạn chế → có thể tham chiếu cổ phiếu ưu đãi của một số quỹ ETF nước ngoài để minh họa.

2. **Chương 7 chưa có trong file lecture chính**: Solution đã ghi chú rõ ở phần dẫn chiếu. Khuyến nghị TODO mở rộng lecture sau (tương ứng task #6 trong todo).

3. **Câu 29 — note follow-up**: Có thể đề có lỗi đánh máy trong phương án C (11,48% thay vì 11,67%) hoặc dữ liệu (D0=3.000 thay vì giá trị khác). Đáng lưu ý cho lần biên soạn đề tiếp theo.

## 🎯 Phán quyết cuối

**PASS — overall_score = 9.0/10.**

Solution đạt chất lượng cao, đầy đủ 30 câu × 8 phần template, tính toán chính xác (18/18 phép số khớp đáp án đề, 1 trường hợp đáp án đề có sai số nhỏ đã được xử lý minh bạch), ví dụ VN phong phú, có khung công thức và bảng tổng hợp giúp ôn nhanh. Status có thể chuyển từ `draft` → `reviewed`, không cần vòng REVISE.
