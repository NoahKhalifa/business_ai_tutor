---
exercise_file: "trac-nghiem-chuong-7.md"
solved_at: "2026-05-09T19:00:00Z"
status: "reviewed"
review_round: 1
total_questions: 30
examples_added: true
---

# Lời giải: Trắc nghiệm Chương 7 — Chi phí sử dụng vốn (Cost of Capital)

> Dẫn chiếu bài giảng: [Financial management.md § Chương 7](../lectures/md/Financial%20management.md) — phần Chi phí sử dụng vốn (🤖 do AI bổ sung dựa trên Brealey–Myers, Brigham–Houston, Nguyễn Minh Kiều, vì PDF gốc chỉ trình bày đến Chương 6).
> Tóm tắt nhanh: [Financial management_summary.md § 7](../lectures/md/Financial%20management_summary.md)

---

## 📐 Khung công thức cốt lõi (dùng xuyên suốt 30 câu)

| STT | Công thức | Ý nghĩa |
|---|---|---|
| 1 | $r_d^{at} = r_d \times (1 - T)$ | Chi phí nợ vay sau thuế |
| 2 | $r_p = \dfrac{D_p}{P_p}$ | Chi phí cổ phần ưu đãi (cổ tức cố định / giá thị trường) |
| 3 | $r_e = \dfrac{D_1}{P_0} + g = \dfrac{D_0(1+g)}{P_0} + g$ | Chi phí cổ phần thường — Mô hình Gordon (DDM) |
| 4 | $r_e^{new} = \dfrac{D_0(1+g)}{P_0(1-f)} + g$ | Chi phí phát hành cổ phần thường mới (có chi phí phát hành f) |
| 5 | $r_e = r_f + \beta \cdot (r_m - r_f)$ | Chi phí cổ phần thường — CAPM |
| 6 | $r_b \approx \dfrac{C + (M-P)/n}{(M+P)/2}$ | Chi phí trái phiếu (xấp xỉ YTM) |
| 7 | $WACC = w_d \cdot r_d(1-T) + w_p \cdot r_p + w_e \cdot r_e$ | Chi phí vốn bình quân gia quyền |
| 8 | $\dfrac{D}{E} = \dfrac{D/TA}{1 - D/TA}$ | Quy đổi đòn bẩy (TA = E + D) |

---

## Câu 1: Lãi suất trái phiếu chính phủ trong CAPM

### 📋 Đề bài
> Lãi suất của trái phiếu chính phủ được sử dụng như thành phần nào trong mô hình CAPM?

### 🎯 Phân tích đề
- **Dạng bài**: Khái niệm CAPM.
- **Yêu cầu**: Xác định vai trò của lãi suất trái phiếu chính phủ trong $r_e = r_f + \beta(r_m - r_f)$.

### 📚 Kiến thức nền
Mô hình CAPM xác định tỷ suất sinh lời đòi hỏi của vốn cổ phần:
$$r_e = r_f + \beta(r_m - r_f)$$
- $r_f$: tỷ suất sinh lời phi rủi ro — thường lấy bằng **lãi suất trái phiếu kho bạc / chính phủ** (kỳ hạn 10 năm phổ biến).
- $r_m$: lợi suất kỳ vọng thị trường (đại diện bằng chỉ số chứng khoán).
- $\beta$: hệ số rủi ro hệ thống của cổ phiếu.

### 🔍 Hướng tiếp cận
Trái phiếu chính phủ được coi là gần như không rủi ro vỡ nợ (sovereign default risk thấp) → là proxy chuẩn cho $r_f$.

### ✍️ Lời giải
- A. Thu nhập kỳ vọng thị trường → là $r_m$, không phải.
- B. Giá trị thị trường cổ phiếu → không xuất hiện trong CAPM.
- C. Hệ số Beta → đo rủi ro hệ thống, không liên quan trái phiếu chính phủ.
- D. **Tỷ suất sinh lời phi rủi ro** ($r_f$) → đúng.

### ✅ Kết luận
**Đáp án D — Tỷ suất sinh lời phi rủi ro.** Tại Việt Nam, người ta thường dùng lãi suất trái phiếu Chính phủ kỳ hạn 10 năm (do Kho bạc Nhà nước phát hành) làm $r_f$.

### ⚠️ Sai lầm thường gặp
Nhầm $r_f$ với lãi suất tiền gửi ngân hàng: tiền gửi vẫn có rủi ro tổ chức tín dụng (dù được BHTGVN bảo hiểm tới 125 triệu).

### 💡 Mẹo
Kiểm tra nhanh: nếu một đại lượng "không có rủi ro" → nghĩ ngay tới trái phiếu Chính phủ.

---

## Câu 2: Tính $r_e$ bằng CAPM (β=1,3; Rf=4%; Rm=11%)

### 📋 Đề bài
> Công ty X có β = 1,3. $R_f$ = 4%, $R_m$ = 11%. Chi phí vốn cổ phần thường (CAPM) là?

### 🎯 Phân tích đề
- **Dạng bài**: Tính số — áp công thức CAPM.
- **Dữ kiện**: $\beta = 1{,}3$; $r_f = 4\%$; $r_m = 11\%$.
- **Cần tìm**: $r_e$.

### 📚 Kiến thức nền
$$r_e = r_f + \beta \cdot (r_m - r_f)$$

### 🔍 Hướng tiếp cận
Thay số trực tiếp.

### ✍️ Lời giải
**Bước 1**: Tính phần bù rủi ro thị trường (market risk premium):
$$r_m - r_f = 11\% - 4\% = 7\%$$
**Bước 2**: Áp công thức:
$$r_e = 4\% + 1{,}3 \times 7\% = 4\% + 9{,}1\% = 13{,}1\%$$

### ✅ Kết luận
**Đáp án D — 13,1%.** Vì β > 1, cổ phiếu X biến động mạnh hơn thị trường → nhà đầu tư đòi suất lợi tức cao hơn $r_m$.

### 🏢 Ví dụ thực tế
Với HPG (Hòa Phát) — β ~ 1,2-1,3 trên HOSE, $r_f$ ≈ 3-4% (TPCP 10Y 2024-2025), $r_m$ ≈ 11-12% → chi phí vốn cổ phần ≈ 12-14%, tương đồng câu này.

### ⚠️ Sai lầm thường gặp
- Quên trừ $r_f$ trước khi nhân β: tính $r_f + \beta \cdot r_m = 4 + 1{,}3 \times 11 = 18{,}3\%$ → sai.
- Nhầm β với tỷ trọng vốn.

### 💡 Mẹo
β > 1 ⇒ cổ phiếu rủi ro cao hơn thị trường ⇒ $r_e > r_m$. Câu này 13,1% > 11% → hợp lý.

---

## Câu 3: WACC với D/V = 0,53125

### 📋 Đề bài
> D = 42,5 tỷ; V = 80 tỷ; $r_e$ = 15%; $r_d$ trước thuế = 8%; T = 20%. Tính WACC.

### 🎯 Phân tích đề
- **Dạng bài**: WACC hai cấu phần (nợ + cổ phần thường).
- **Cần tìm**: $WACC = w_d \cdot r_d(1-T) + w_e \cdot r_e$.

### 📚 Kiến thức nền
$E = V - D$; $w_d = D/V$; $w_e = E/V$.

### ✍️ Lời giải
**Bước 1**: $E = 80 - 42{,}5 = 37{,}5$ tỷ → $w_d = 42{,}5/80 = 0{,}53125$; $w_e = 37{,}5/80 = 0{,}46875$.
**Bước 2**: Chi phí nợ sau thuế: $r_d(1-T) = 8\% \times 0{,}8 = 6{,}4\%$.
**Bước 3**: 
$$WACC = 0{,}53125 \times 6{,}4\% + 0{,}46875 \times 15\% = 3{,}40\% + 7{,}03125\% = 10{,}43\%$$

### ✅ Kết luận
**Đáp án D — 10,43%.**

### ⚠️ Sai lầm thường gặp
- Quên nhân $(1-T)$ với chi phí nợ → ra 11,03% (sai).
- Dùng E = V mà không trừ D.

### 💡 Mẹo
Khi D/V xấp xỉ 50%, WACC ≈ trung bình cộng có trọng số giữa $r_d(1-T)$ và $r_e$.

---

## Câu 4: Chi phí vay sau thuế (rd=20%, T=25%)

### 📋 Đề bài
> Vay ngân hàng lãi 20%, T = 25%. Chi phí vốn vay sau thuế?

### 🎯 Phân tích đề
- **Dạng bài**: Áp công thức $r_d^{at} = r_d (1-T)$.

### ✍️ Lời giải
$$r_d^{at} = 20\% \times (1 - 0{,}25) = 20\% \times 0{,}75 = 15\%$$

### ✅ Kết luận
**Đáp án D — 15%.** Lãi vay được tính vào chi phí hợp lý → "lá chắn thuế" giúp tiết giảm 5% chi phí thực.

### 🏢 Ví dụ thực tế
Vingroup khi vay 1.000 tỷ với lãi 10%/năm (T=20%) → chi phí thực sau thuế 10% × 0,8 = 8%. Tiền tiết kiệm thuế = 1.000 × 10% × 20% = 20 tỷ/năm.

### ⚠️ Sai lầm thường gặp
- Cộng thuế vào lãi ($20 + 25 = 45\%$) → sai cơ bản.
- Quên rằng "không trả cổ tức" và "giữ lại thu nhập" là thông tin nhiễu (không ảnh hưởng tính chi phí nợ vay).

### 💡 Mẹo
Lưu ý: cổ tức KHÔNG được khấu trừ thuế; chỉ lãi vay mới được.

---

## Câu 5: Chi phí trái phiếu phát hành dưới mệnh giá

### 📋 Đề bài
> Trái phiếu mệnh giá M = 1.000.000đ; coupon 15%; n = 5 năm; giá phát hành P = 950.000đ. Chi phí khoản nợ?

### 🎯 Phân tích đề
- **Dạng bài**: YTM của trái phiếu — dùng công thức xấp xỉ.
- **Cần tìm**: $r_b$.

### 📚 Kiến thức nền
Lãi coupon hàng năm: $C = 15\% \times 1.000.000 = 150.000$đ.
Công thức xấp xỉ:
$$r_b \approx \dfrac{C + (M-P)/n}{(M+P)/2}$$

### ✍️ Lời giải
**Bước 1**: $C = 150.000$; $(M-P)/n = (1.000.000 - 950.000)/5 = 10.000$.
**Bước 2**: Tử số: $150.000 + 10.000 = 160.000$.
**Bước 3**: Mẫu số: $(1.000.000 + 950.000)/2 = 975.000$.
**Bước 4**: $r_b \approx 160.000/975.000 = 0{,}16410 = 16{,}41\%$.

**Bước 5 (kiểm tra YTM chính xác)**: Thử $r = 16{,}49\%$ vào phương trình giá:
$$P = 150.000 \times \dfrac{1-(1+0{,}1649)^{-5}}{0{,}1649} + \dfrac{1.000.000}{(1{,}1649)^5} \approx 485.295 + 466.460 \approx 951.755 \approx 950.000 ✓$$

### ✅ Kết luận
**Đáp án B — 16,49%.** Vì giá phát hành thấp hơn mệnh giá (P < M) nên chi phí thực > coupon = 15%.

### ⚠️ Sai lầm thường gặp
- Lấy thẳng coupon 15% mà không hiệu chỉnh phần chiết khấu (M-P) → đáp án sai.
- Tính $(P-M)/n$ thay vì $(M-P)/n$ → ra số âm.

### 💡 Mẹo
Quy tắc: P < M ⇒ YTM > coupon; P > M ⇒ YTM < coupon. Câu này P = 950k < 1.000k → 16,49% > 15% ✓.

---

## Câu 6: Phương pháp lãi trái phiếu + bù rủi ro

### 📋 Đề bài
> Một mức bù rủi ro tăng thêm được cộng vào lãi suất của trái phiếu để tính:

### 🎯 Phân tích đề
- **Dạng bài**: Khái niệm — phương pháp ước lượng $r_e$ qua công thức $r_e = r_d + \text{risk premium}$.

### 📚 Kiến thức nền
Có 3 cách ước lượng chi phí cổ phần thường:
1. CAPM: $r_e = r_f + \beta(r_m - r_f)$.
2. DDM/Gordon: $r_e = D_1/P_0 + g$.
3. **Bond-yield-plus-risk-premium**: $r_e = r_d + \text{premium}$ (thường 3-5%).

### ✍️ Lời giải
Phương pháp này dùng để ước lượng **chi phí cổ phiếu thường** vì cổ đông gánh rủi ro cao hơn trái chủ → đòi suất lợi tức cao hơn lãi trái phiếu một biên độ rủi ro.

### ✅ Kết luận
**Đáp án A — Chi phí cổ phiếu thường.**

### ⚠️ Sai lầm thường gặp
- Chọn C "cổ phiếu ưu đãi": cổ phiếu ưu đãi tính theo $D_p/P_p$, không dùng cộng bù rủi ro vào lãi trái phiếu.
- Chọn B "vốn lưu động": vốn lưu động không phải nguồn tài trợ riêng có chi phí.

### 💡 Mẹo
Thứ tự rủi ro: Trái phiếu < CP ưu đãi < CP thường. Mỗi nấc thêm một lớp bù rủi ro.

---

## Câu 7: WACC ba nguồn (rd trước thuế, rp, re)

### 📋 Đề bài
> $w_d=15\%$ ($r_d^{bt}=15\%$); $w_p=25\%$ ($r_p=11{,}5\%$); $w_e=60\%$ ($r_e=14{,}3\%$); T=20%.

### ✍️ Lời giải
**Bước 1**: Chi phí nợ sau thuế: $15\% \times 0{,}8 = 12\%$.
**Bước 2**: 
$$WACC = 0{,}15 \times 12\% + 0{,}25 \times 11{,}5\% + 0{,}6 \times 14{,}3\%$$
$$= 1{,}80\% + 2{,}875\% + 8{,}58\% = 13{,}255\% \approx 13{,}25\%$$

### ✅ Kết luận
**Đáp án A — 13,25%.**

### ⚠️ Sai lầm thường gặp
- Quên nhân (1-T) cho chi phí nợ → 13,71% (đáp án nhiễu C — bẫy phổ biến!).
- Áp $(1-T)$ cho cả $r_p$ (cổ phiếu ưu đãi không có lá chắn thuế).

### 💡 Mẹo
Chỉ chi phí nợ vay/trái phiếu mới được nhân (1-T). Cổ phiếu ưu đãi và cổ phần thường thì KHÔNG.

---

## Câu 8: Chuyển D/TA → D/E (= 0,45)

### 📋 Đề bài
> D/TA = 0,45. Tính D/E.

### 📚 Kiến thức nền
$TA = D + E \Rightarrow E = TA - D \Rightarrow E/TA = 1 - D/TA$.
$$\dfrac{D}{E} = \dfrac{D/TA}{E/TA} = \dfrac{D/TA}{1 - D/TA}$$

### ✍️ Lời giải
$$\dfrac{D}{E} = \dfrac{0{,}45}{1 - 0{,}45} = \dfrac{0{,}45}{0{,}55} = 0{,}8182 \approx 0{,}82$$

### ✅ Kết luận
**Đáp án A — 0,82.**

### ⚠️ Sai lầm thường gặp
Chia ngược: $0{,}55/0{,}45 = 1{,}22$ → sai.

### 💡 Mẹo
D/TA < 0,5 ⇒ D < E ⇒ D/E < 1. Câu này 0,82 < 1 ✓.

---

## Câu 9: Chính sách tác động đến WACC

### 📋 Đề bài
> WACC bị tác động bởi: (1) cấu trúc vốn, (2) cổ tức, (3) đầu tư.

### 🎯 Phân tích
- **Cấu trúc vốn** (1): thay đổi $w_d, w_e$ → đổi WACC trực tiếp ✓.
- **Chính sách cổ tức** (2): ảnh hưởng tỷ lệ lợi nhuận giữ lại vs phát hành CP mới → đổi $r_e$ ✓.
- **Chính sách đầu tư** (3): rủi ro dự án thay đổi β → đổi $r_e$ và toàn bộ WACC ✓.

### ✅ Kết luận
**Đáp án D — Tác động đến cả 3 chính sách.**

### 🏢 Ví dụ thực tế
Vinamilk duy trì cấu trúc vốn ít nợ (D/E ~ 0,1-0,2) và chính sách cổ tức cao (~50% LNST) → giữ WACC ở mức 9-10%, thấp so với ngành (FMCG VN trung bình 11-12%).

### ⚠️ Sai lầm thường gặp
Quên rằng chính sách cổ tức tác động qua kênh "lợi nhuận giữ lại vs phát hành CP mới" — phát hành CP mới có chi phí cao hơn lợi nhuận giữ lại do flotation cost.

---

## Câu 10: WACC với D/V = 0,5

### 📋 Đề bài
> D = 45 tỷ; V = 90 tỷ; $r_e$=16%; $r_d^{bt}$=9%; T=22%.

### ✍️ Lời giải
**Bước 1**: $w_d = 45/90 = 0{,}5$; $w_e = 0{,}5$.
**Bước 2**: $r_d^{at} = 9\% \times (1-0{,}22) = 9\% \times 0{,}78 = 7{,}02\%$.
**Bước 3**: 
$$WACC = 0{,}5 \times 7{,}02\% + 0{,}5 \times 16\% = 3{,}51\% + 8\% = 11{,}51\%$$

### ✅ Kết luận
**Đáp án C — 11,51%.**

### ⚠️ Sai lầm thường gặp
T = 22% (không phải 20% phổ biến) — phải đọc kỹ đề.

---

## Câu 11: Chi phí cổ phần thường (DDM)

### 📋 Đề bài
> $D_0$ = 20.000đ; $P_0$ = 240.000đ; g = 8%. Tính $r_e$.

### 📚 Kiến thức nền
Mô hình Gordon (cổ tức tăng trưởng đều):
$$r_e = \dfrac{D_1}{P_0} + g = \dfrac{D_0(1+g)}{P_0} + g$$

### ✍️ Lời giải
**Bước 1**: $D_1 = 20.000 \times (1+0{,}08) = 21.600$đ.
**Bước 2**: 
$$r_e = \dfrac{21.600}{240.000} + 0{,}08 = 0{,}09 + 0{,}08 = 0{,}17 = 17\%$$

### ✅ Kết luận
**Đáp án A — 17%.**

### ⚠️ Sai lầm thường gặp
- Quên nhân $D_0$ với $(1+g)$ để ra $D_1$ → tính $20.000/240.000 + 8\% = 8{,}33\% + 8\% = 16{,}33\%$ → sai.
- Lẫn $D_0$ và $D_1$: $D_0$ là cổ tức "vừa trả"; $D_1$ là cổ tức "kỳ tới" (kỳ vọng).

### 💡 Mẹo
"Cổ tức trả lần mới nhất" = $D_0$ → phải nhân (1+g). "Cổ tức kỳ tới" = $D_1$ → dùng thẳng.

---

## Câu 12: Yếu tố CAPM (chọn cái KHÔNG cần)

### 📋 Đề bài
> CAPM cần biết các yếu tố ngoại trừ:

### 🎯 Phân tích
CAPM: $r_e = r_f + \beta(r_m - r_f)$ → cần $r_f$, $\beta$, $r_m$.

### ✍️ Lời giải
- A. **Thu nhập trong năm tiếp theo của công ty** → KHÔNG cần (đây là dòng tiền dự án, dùng cho NPV/Gordon, không phải CAPM).
- B. $r_m$ → cần.
- C. β → cần.
- D. $r_f$ → cần.

### ✅ Kết luận
**Đáp án A — Thu nhập trong năm tiếp theo của công ty.**

### ⚠️ Sai lầm thường gặp
Đề có chữ "ngoại trừ" — đọc lướt sẽ chọn yếu tố cần dùng. Phải gạch dưới chữ "ngoại trừ".

### 💡 Mẹo
Câu hỏi "ngoại trừ" thường là bẫy đảo chiều. Khoanh tròn từ "ngoại trừ" trước khi đọc đáp án.

---

## Câu 13: Chi phí vay sau thuế (18%, T=20%)

### ✍️ Lời giải
$$r_d^{at} = 18\% \times (1 - 0{,}2) = 18\% \times 0{,}8 = 14{,}4\%$$

### ✅ Kết luận
**Đáp án C — 14,40%.**

### ⚠️ Sai lầm thường gặp
Đáp án D = 15,30% là bẫy nếu nhân 18% × (1-0,15) (lẫn thuế suất).

---

## Câu 14: D/TA = 0,4 → D/E

### ✍️ Lời giải
$$\dfrac{D}{E} = \dfrac{0{,}4}{1 - 0{,}4} = \dfrac{0{,}4}{0{,}6} = 0{,}6667$$

### ✅ Kết luận
**Đáp án D — 0,667.**

### 💡 Mẹo
Quy tắc nhanh: $D/TA = a$ ⇒ $D/E = a/(1-a)$. Ví dụ a=1/3 ⇒ D/E=1/2; a=1/2 ⇒ D/E=1.

---

## Câu 15: Chi phí cổ phần thường mới (có flotation 2%)

### 📋 Đề bài
> $P_0$=85.000; $D_0$=2.500; g=8%; f=2%; T=20%.

### 📚 Kiến thức nền
$$r_e^{new} = \dfrac{D_1}{P_0(1-f)} + g$$
Lưu ý: thuế T không tham gia vào công thức chi phí cổ phần thường (cổ tức không được khấu trừ thuế) — T = 20% chỉ là thông tin nhiễu.

### ✍️ Lời giải
**Bước 1**: $D_1 = 2.500 \times 1{,}08 = 2.700$đ.
**Bước 2**: Giá ròng nhận được: $85.000 \times (1-0{,}02) = 85.000 \times 0{,}98 = 83.300$đ.
**Bước 3**: 
$$r_e^{new} = \dfrac{2.700}{83.300} + 0{,}08 = 0{,}03241 + 0{,}08 = 0{,}11241 = 11{,}24\%$$

### ✅ Kết luận
**Đáp án C — 11,24%.**

### ⚠️ Sai lầm thường gặp
- Áp (1-T) vào $r_e$ — sai vì cổ tức không được khấu trừ thuế.
- Quên (1-f) ở mẫu — ra 11,18% gần nhưng không đúng.

---

## Câu 16: Khi $P_p$ tăng → $r_p$?

### 📚 Kiến thức nền
$r_p = D_p / P_p$ ⇒ $r_p$ tỷ lệ nghịch với $P_p$.

### ✅ Kết luận
**Đáp án A — Giảm xuống.**

### 🏢 Ví dụ thực tế
Cổ phiếu ưu đãi VIC-P (giả định) có $D_p$ = 1.000đ/năm. Nếu $P_p$ = 10.000 → $r_p$ = 10%. Khi $P_p$ tăng lên 12.500 → $r_p$ giảm còn 8%. Doanh nghiệp huy động vốn rẻ hơn khi giá cổ phiếu ưu đãi tăng.

### 💡 Mẹo
Giá tăng = nhà đầu tư chấp nhận lợi tức thấp hơn = chi phí vốn của DN giảm.

---

## Câu 17: WACC (D/V=0,475; T=24%)

### ✍️ Lời giải
**Bước 1**: $w_d = 47{,}5/100 = 0{,}475$; $w_e = 52{,}5/100 = 0{,}525$.
**Bước 2**: $r_d^{at} = 10\% \times (1-0{,}24) = 7{,}6\%$.
**Bước 3**: 
$$WACC = 0{,}475 \times 7{,}6\% + 0{,}525 \times 17\% = 3{,}61\% + 8{,}925\% = 12{,}535\% \approx 12{,}54\%$$

### ✅ Kết luận
**Đáp án C — 12,54%.**

---

## Câu 18: Chi phí phát hành CP thường mới (f=6%)

### 📋 Đề bài
> $D_0$=20.000; $P_0$=240.000; g=8%; f=6%.

### ✍️ Lời giải
**Bước 1**: $D_1 = 20.000 \times 1{,}08 = 21.600$đ.
**Bước 2**: $P_0 \times (1-f) = 240.000 \times 0{,}94 = 225.600$đ.
**Bước 3**: 
$$r_e^{new} = \dfrac{21.600}{225.600} + 0{,}08 = 0{,}09574 + 0{,}08 = 0{,}17574 \approx 17{,}57\%$$

### ✅ Kết luận
**Đáp án A — 17,57%.**

### 📊 So sánh với câu 11 (cùng dữ liệu, không có flotation)
| Trường hợp | $r_e$ |
|---|---|
| Lợi nhuận giữ lại (câu 11) | 17,00% |
| Phát hành CP mới (câu 18, f=6%) | 17,57% |
**Chênh lệch 0,57%** → đó chính là chi phí phát hành đẩy lên. Càng phát hành mới → càng đắt.

### ⚠️ Sai lầm thường gặp
- Cộng f vào g: $g_{new} = 8\% + 6\% = 14\%$ → sai cách áp f.

### 💡 Mẹo
Lợi nhuận giữ lại luôn rẻ hơn phát hành CP mới — đây là một lý do quan trọng để DN ưu tiên lợi nhuận giữ lại (Pecking-order theory).

---

## Câu 19: Giảm tỷ lệ D/TA

### 🎯 Phân tích
$D/TA$ giảm khi: tử (D) giảm HOẶC mẫu (TA) tăng nhanh hơn D.
- A. Chuyển D ngắn hạn → D dài hạn: tổng D không đổi → D/TA **không đổi**.
- B. **Bán cổ phiếu phổ thông**: tăng E → tăng TA, D không đổi → D/TA **giảm** ✓.
- C. Vay thêm: tăng D và TA cùng lượng, nhưng tỷ lệ D/TA **tăng** vì tỷ trọng nợ trong cấu trúc tăng.
- D. Chuyển D dài hạn → D ngắn hạn: tổng D không đổi → không đổi.

### ✅ Kết luận
**Đáp án B — Bán cổ phiếu phổ thông.**

### 🏢 Ví dụ thực tế
Năm 2022, NVL (Novaland) gặp áp lực D/TA cao (~0,75) → công ty phát hành cổ phiếu phổ thông để pha loãng vốn và giảm tỷ lệ nợ. Hành động chuẩn xác cho tình huống này.

---

## Câu 20: WACC ba nguồn (nợ ngân hàng + CP thường + nợ trái phiếu)

### 📋 Phân tích cẩn trọng
- $r_{d-bank}$ = 16% **trước thuế** → cần nhân (1-T).
- $r_e$ = 15,24%.
- $r_{d-bond}$ = 12,58% **đã sau thuế** → dùng thẳng.

### ✍️ Lời giải
**Bước 1**: $r_{d-bank}^{at} = 16\% \times 0{,}8 = 12{,}8\%$.
**Bước 2**: 
$$WACC = 0{,}25 \times 12{,}8\% + 0{,}45 \times 15{,}24\% + 0{,}3 \times 12{,}58\%$$
$$= 3{,}20\% + 6{,}858\% + 3{,}774\% = 13{,}832\% \approx 13{,}83\%$$

### ✅ Kết luận
**Đáp án C — 13,83%.**

### ⚠️ Sai lầm thường gặp
- **Bẫy lớn**: nhân (1-T) cho cả $r_{d-bond}$ → $0{,}3 \times 12{,}58\% \times 0{,}8 = 3{,}019\%$ → WACC = 13,08% (đáp án nhiễu lân cận).
- Nhân (1-T) cho $r_e$ — sai cơ bản.

### 💡 Mẹo
**Đọc kỹ "trước thuế" / "sau thuế"** trước khi áp công thức. Đây là loại bẫy phổ biến nhất trong câu WACC nhiều nguồn.

---

## Câu 21: Lãi suất thị trường tăng → WACC?

### 🎯 Phân tích
Lãi suất thị trường tăng → chi phí huy động nợ mới ($r_d$) tăng → mỗi đồng vốn vay đều đắt hơn → WACC tăng qua kênh chi phí nợ.

### ✅ Kết luận
**Đáp án C — Tăng chi phí sử dụng nợ vay.**

### 🏢 Ví dụ thực tế
Khi NHNN tăng lãi suất điều hành cuối 2022 từ 4% lên 6% → lãi suất cho vay doanh nghiệp tăng từ ~9% lên ~12%. WACC của các DN bất động sản (NVL, DXG, KDH) đều tăng tương ứng → áp lực tài chính lớn → giá cổ phiếu giảm sâu.

### ⚠️ Sai lầm thường gặp
Chọn D "Giảm chi phí nợ vay" — ngược chiều logic kinh tế.

---

## Câu 22: Định nghĩa "cấu trúc vốn"

### 📚 Kiến thức nền
Cấu trúc vốn (capital structure) chỉ tổng hợp các nguồn tài trợ **dài hạn**:
- Nợ dài hạn (vay dài hạn, trái phiếu).
- Cổ phiếu ưu đãi.
- Vốn cổ phần thường (gồm cả lợi nhuận giữ lại).

### ✍️ Lời giải
Loại trừ:
- B. Chỉ vốn chủ sở hữu — thiếu nợ dài hạn.
- C. Tổng tài sản — đó là phần "Tài sản", không phải "Nguồn vốn".
- D. Tài sản ngắn hạn và nợ ngắn hạn — đây là vốn lưu động (working capital), không phải cấu trúc vốn.

### ✅ Kết luận
**Đáp án A — Nợ dài hạn, cổ phiếu ưu đãi và vốn chủ sở hữu cổ phiếu phổ thông.**

### ⚠️ Sai lầm thường gặp
Lẫn cấu trúc vốn (capital structure — chỉ dài hạn) với cấu trúc tài chính (financial structure — bao gồm cả ngắn hạn).

---

## Câu 23: Chi phí CP ưu đãi ($D_p$=6,3; $P_p$=70)

### ✍️ Lời giải
$$r_p = \dfrac{D_p}{P_p} = \dfrac{6{,}30}{70} = 0{,}09 = 9{,}0\%$$

### ✅ Kết luận
**Đáp án A — 9,0%.**

### 💡 Mẹo
**Lưu ý**: dùng giá thị trường $P_p$ = 70$, KHÔNG phải mệnh giá 100$. Mệnh giá chỉ dùng để tính cổ tức ($D_p$ thường = % × mệnh giá), không dùng làm mẫu số.

### ⚠️ Sai lầm thường gặp
Dùng mệnh giá 100$: $r_p = 6{,}3/100 = 6{,}3\%$ → chọn nhầm D.

---

## Câu 24: Chi phí CP thường (DDM, $D_0$=8.000; $P_0$=90.000; g=10%)

### ✍️ Lời giải
**Bước 1**: $D_1 = 8.000 \times 1{,}10 = 8.800$đ.
**Bước 2**: 
$$r_e = \dfrac{8.800}{90.000} + 0{,}10 = 0{,}0978 + 0{,}10 = 0{,}1978 = 19{,}78\%$$

### ✅ Kết luận
**Đáp án D — 19,78%.**

### ⚠️ Sai lầm thường gặp
- Áp (1-T) cho $r_e$ — sai.
- Dùng $D_0/P_0$ thay vì $D_1/P_0$ → ra 18,89% (gần đáp án nhiễu B).

---

## Câu 25: WACC (chi phí đã sau thuế cho cả 3 nguồn)

### 📋 Phân tích cẩn trọng
Đề ghi rõ "chi phí **sau thuế** lần lượt là 12%, 14%, 17,5%" → KHÔNG cần nhân (1-T) thêm.

### ✍️ Lời giải
$$WACC = 0{,}25 \times 12\% + 0{,}10 \times 14\% + 0{,}65 \times 17{,}5\%$$
$$= 3{,}00\% + 1{,}40\% + 11{,}375\% = 15{,}775\% \approx 15{,}78\%$$

### ✅ Kết luận
**Đáp án B — 15,78%.**

### ⚠️ Sai lầm thường gặp
**Bẫy chính**: Nhân (1-T) cho 12% (vay ngân hàng) → $0{,}25 \times 12\% \times 0{,}8 = 2{,}4\%$ → WACC ra ~15,18% (sai). Đề đã ghi "sau thuế" → không hiệu chỉnh nữa.

### 💡 Mẹo
Câu này đối lập với câu 7 và 20. Phải đọc kỹ "trước thuế" hay "sau thuế" của TỪNG nguồn vốn.

---

## Câu 26: Chi phí CP ưu đãi ($D_p$=7; $P_p$=75)

### ✍️ Lời giải
$$r_p = \dfrac{7}{75} = 0{,}0933 = 9{,}33\%$$

### ✅ Kết luận
**Đáp án B — 9,33%.**

### ⚠️ Sai lầm thường gặp
Dùng mệnh giá 100$ → $7/100 = 7\%$ (đáp án D=6,3% lại không phải 7%, đáp án A=30% là nhiễu, C=70% là nhiễu).

---

## Câu 27: Chi phí vay sau thuế (rd=20%, T=20%)

### ✍️ Lời giải
$$r_d^{at} = 20\% \times (1-0{,}20) = 20\% \times 0{,}8 = 16\%$$

### ✅ Kết luận
**Đáp án A — 16%.**

### 📊 So sánh với câu 4 (cùng $r_d$ = 20%, T khác)
| T | $r_d^{at}$ |
|---|---|
| 25% (câu 4) | 15% |
| 20% (câu 27) | 16% |
T càng cao → lá chắn thuế càng lớn → chi phí thực sau thuế càng thấp.

---

## Câu 28: Thuế là yếu tố nào trong công thức?

### 🎯 Phân tích
- Vốn cổ phần ưu đãi: $r_p = D_p/P_p$ → KHÔNG có T.
- **Nợ**: $r_d^{at} = r_d \times (1-T)$ → có T ✓.
- Vốn cổ phần thường (DDM): $r_e = D_1/P_0 + g$ → KHÔNG có T.
- CAPM: $r_e = r_f + \beta(r_m - r_f)$ → KHÔNG có T.

### ✅ Kết luận
**Đáp án C — Nợ.**

### 💡 Mẹo
Lý do: chỉ chi phí lãi vay được khấu trừ thuế (tax-deductible). Cổ tức (kể cả ưu đãi) không được trừ thuế trước khi tính TNDN.

### ⚠️ Sai lầm thường gặp
Chọn D "vốn cổ phần thường" do quen áp T vào tất cả công thức tài chính.

---

## Câu 29: Chi phí CP thường ($D_0$=3.000; $P_0$=90.000; g=8%; f=2%)

### ✍️ Lời giải
**Bước 1**: $D_1 = 3.000 \times 1{,}08 = 3.240$đ.
**Bước 2**: $P_0 \times (1-f) = 90.000 \times 0{,}98 = 88.200$đ.
**Bước 3**: 
$$r_e^{new} = \dfrac{3.240}{88.200} + 0{,}08 = 0{,}03673 + 0{,}08 = 0{,}11673 \approx 11{,}67\%$$

### ✅ Kết luận
**Đáp án C — 11,48%** (đáp án gần nhất với 11,67% theo phương án có sẵn).

### 📌 Ghi chú
Tính chính xác cho ra **11,67%**, đáp án C (11,48%) là phương án gần nhất trong 4 lựa chọn. Có thể đề bài có sai số làm tròn hoặc giả định khác (ví dụ dùng $D_0/[P_0(1-f)] + g \approx 11{,}40\%$). Trong tài liệu chuẩn (Brealey), kết quả tính ra 11,67% là chính xác.

### ⚠️ Sai lầm thường gặp
Quên (1-f) ở mẫu — ra 11,60%; quên nhân (1+g) cho $D_0$ — ra 11,40%.

---

## Câu 30: CAPM (β=1,35; Rf=5%; Rm=12%)

### ✍️ Lời giải
$$r_e = 5\% + 1{,}35 \times (12\% - 5\%) = 5\% + 1{,}35 \times 7\% = 5\% + 9{,}45\% = 14{,}45\%$$

### ✅ Kết luận
**Đáp án B — 14,45%.**

### 🏢 Ví dụ thực tế
β = 1,35 ứng với cổ phiếu ngành chứng khoán/ngân hàng (SSI, VND, VPB) thường có biến động cao hơn VN-Index. Với $r_f$ = 5% (TPCP 10Y), $r_m$ = 12%, các DN này có chi phí vốn cổ phần ~14-15%.

### ⚠️ Sai lầm thường gặp
Quên trừ Rf trước khi nhân β: $5\% + 1{,}35 \times 12\% = 21{,}2\%$ — sai cấu trúc CAPM.

---

## 📊 Tổng hợp đáp án

| Câu | Đ.A | Câu | Đ.A | Câu | Đ.A |
|---|---|---|---|---|---|
| 1 | D | 11 | A | 21 | C |
| 2 | D | 12 | A | 22 | A |
| 3 | D | 13 | C | 23 | A |
| 4 | D | 14 | D | 24 | D |
| 5 | B | 15 | C | 25 | B |
| 6 | A | 16 | A | 26 | B |
| 7 | A | 17 | C | 27 | A |
| 8 | A | 18 | A | 28 | C |
| 9 | D | 19 | B | 29 | C |
| 10 | C | 20 | C | 30 | B |

## 🔑 Bài học chính rút ra

1. **(1-T) chỉ áp cho chi phí nợ** (vay/trái phiếu). Cổ tức (ưu đãi và thường) KHÔNG được khấu trừ thuế.
2. **Phải đọc kỹ "trước/sau thuế"** ở mỗi nguồn vốn trước khi tính WACC.
3. **DDM cần phân biệt $D_0$ (vừa trả) và $D_1$ (kỳ tới)** — luôn nhân (1+g) khi đề cho $D_0$.
4. **Chi phí phát hành CP mới (flotation cost f)** đẩy chi phí cổ phần lên: $D_1/[P_0(1-f)] + g$.
5. **CAPM ≠ DDM ≠ Bond-yield-plus-premium** — 3 phương pháp ước lượng $r_e$ độc lập, có thể cho kết quả khác nhau.
6. **D/TA ↔ D/E**: $D/E = (D/TA)/(1-D/TA)$.
7. **WACC tăng khi**: lãi suất thị trường tăng, tỷ trọng nợ tăng quá ngưỡng tối ưu, rủi ro dự án tăng (β tăng).
