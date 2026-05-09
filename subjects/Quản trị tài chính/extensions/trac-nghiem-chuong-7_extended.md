---
parent_solution: "solutions/trac-nghiem-chuong-7_solution.md"
created_at: "2026-05-09T19:30:00Z"
---

# Mở rộng & Luyện tập: Trắc nghiệm Chương 7 — Chi phí sử dụng vốn

> Sau khi đã giải 30 câu trong [trac-nghiem-chuong-7.md](../exercises/md/trac-nghiem-chuong-7.md), 3 bài luyện dưới đây giúp bạn áp dụng tổng hợp các công thức (CAPM, DDM, WACC, đòn bẩy) vào tình huống doanh nghiệp Việt Nam thực tế.

---

## 🎯 Bài tập tham khảo (tự luyện)

### Bài luyện 1 — Cơ bản (★)

**Đề**: Công ty FPT đang sử dụng 2 nguồn vốn: vay ngân hàng (lãi suất trước thuế 9%/năm, chiếm 40% tổng vốn) và vốn cổ phần thường (chi phí 16%, chiếm 60%). Thuế suất thuế thu nhập doanh nghiệp là 20%. Tính WACC của FPT.

**Gợi ý**: Áp công thức $WACC = w_d \cdot r_d(1-T) + w_e \cdot r_e$, nhớ nhân (1-T) cho chi phí vay vì đề cho lãi suất "trước thuế".

<details>
<summary>Đáp án rút gọn</summary>

**Bước 1**: $r_d^{at} = 9\% \times (1 - 0{,}20) = 9\% \times 0{,}8 = 7{,}2\%$.

**Bước 2**: 
$$WACC = 0{,}40 \times 7{,}2\% + 0{,}60 \times 16\% = 2{,}88\% + 9{,}60\% = 12{,}48\%$$

**Kết luận**: WACC = **12,48%**. Mức này nằm trong khoảng hợp lý cho doanh nghiệp công nghệ niêm yết tại VN (10-14%). FPT chấp nhận đầu tư các dự án có IRR > 12,48% để tạo giá trị cho cổ đông.
</details>

---

### Bài luyện 2 — Trung bình (★★)

**Đề**: Công ty Vinamilk đang xem xét 2 phương án huy động vốn cho dự án mở rộng nhà máy:

- **Phương án A**: Sử dụng lợi nhuận giữ lại. Cổ tức vừa trả ($D_0$) = 5.000đ/cp, giá thị trường $P_0$ = 80.000đ/cp, tốc độ tăng cổ tức kỳ vọng g = 7%.
- **Phương án B**: Phát hành cổ phiếu thường mới. Chi phí phát hành f = 4% trên giá bán.

Đồng thời, Vinamilk đang nghiên cứu hệ số β của cổ phiếu là 0,75 (cổ phiếu ngành tiêu dùng thường ổn định). Lãi suất TPCP 10Y $r_f$ = 4%, $r_m$ = 11%.

**Yêu cầu**: 
1. Tính chi phí vốn cổ phần của Phương án A theo cả 2 phương pháp DDM và CAPM. So sánh.
2. Tính chi phí vốn cổ phần của Phương án B (DDM có flotation).
3. Phương án nào rẻ hơn? Tại sao Vinamilk thường ưu tiên phương án này?

<details>
<summary>Đáp án rút gọn</summary>

**Phần 1 — Phương án A (lợi nhuận giữ lại):**

*Cách 1 (DDM/Gordon):*
- $D_1 = 5.000 \times 1{,}07 = 5.350$đ.
- $r_e^{DDM} = \dfrac{5.350}{80.000} + 0{,}07 = 0{,}06688 + 0{,}07 = 0{,}13688 \approx \mathbf{13{,}69\%}$

*Cách 2 (CAPM):*
- $r_e^{CAPM} = 4\% + 0{,}75 \times (11\% - 4\%) = 4\% + 5{,}25\% = \mathbf{9{,}25\%}$

*So sánh*: Hai phương pháp cho kết quả **khác nhau** (13,69% vs 9,25%). Khoảng chênh ~4,4% phản ánh:
- DDM phụ thuộc giả định g — nếu g = 7% là quá lạc quan, kết quả sẽ thiên cao.
- CAPM phụ thuộc β — nếu thị trường đang định giá rủi ro thấp, $r_e$ ước lượng có thể thấp.
- Trong thực tế, DN nên dùng **trung bình hoặc khoảng** (~10-14%) để có biên an toàn.

**Phần 2 — Phương án B (phát hành mới):**
- $P_0 \times (1-f) = 80.000 \times 0{,}96 = 76.800$đ.
- $r_e^{new} = \dfrac{5.350}{76.800} + 0{,}07 = 0{,}06966 + 0{,}07 = 0{,}13966 \approx \mathbf{13{,}97\%}$

**Phần 3 — Kết luận**: 
- Phương án A (DDM) = 13,69% < Phương án B = 13,97%.
- Chênh lệch 0,28% chính là chi phí phát hành đẩy lên.
- Vinamilk ưu tiên **lợi nhuận giữ lại** vì:
  1. Rẻ hơn (không có flotation cost).
  2. Theo Pecking-order theory — không phát tín hiệu "kém" ra thị trường.
  3. Vinamilk có dòng tiền hoạt động mạnh (~10.000-12.000 tỷ/năm), đủ tài trợ CAPEX nội sinh.
</details>

---

### Bài luyện 3 — Nâng cao (★★★)

**Đề**: Công ty Cổ phần Hòa Phát (HPG) có cấu trúc vốn mục tiêu sau (theo giá trị thị trường):

| Nguồn | Tỷ trọng | Chi phí trước thuế |
|---|---|---|
| Vay ngân hàng dài hạn | 25% | 8,5% |
| Trái phiếu DN (kỳ hạn 5 năm) | 15% | M = 100.000đ; coupon 11%; P = 96.000đ |
| Cổ phiếu ưu đãi | 10% | Cổ tức $D_p$ = 1.500đ; giá $P_p$ = 18.000đ |
| Cổ phiếu thường | 50% | β = 1,3; $r_f$ = 4%; $r_m$ = 11,5% |

Thuế suất TNDN T = 20%. Chi phí phát hành cổ phiếu thường mới f = 5% (nếu phải huy động ngoài).

**Yêu cầu**:
1. Tính chi phí từng nguồn vốn (sau thuế nếu cần).
2. Tính WACC khi HPG dùng lợi nhuận giữ lại (không phải phát hành CP mới).
3. Tính WACC trong trường hợp HPG buộc phải phát hành CP mới ($r_e^{new}$ thay cho $r_e$).
4. Nếu lãi suất NHNN tăng 1% (đẩy lãi vay ngân hàng lên 9,5% và buộc trái phiếu mới phát hành ở P = 95.000đ), tính lại WACC ở cả 2 trường hợp. Bình luận tác động.

<details>
<summary>Đáp án rút gọn</summary>

**Phần 1 — Chi phí từng nguồn:**

*(a) Vay ngân hàng:* $r_d^{bank,at} = 8{,}5\% \times 0{,}8 = \mathbf{6{,}80\%}$.

*(b) Trái phiếu (xấp xỉ YTM):*
- $C = 11\% \times 100.000 = 11.000$đ; $(M-P)/n = 4.000/5 = 800$đ.
- $r_b \approx \dfrac{11.000 + 800}{(100.000+96.000)/2} = \dfrac{11.800}{98.000} = 12{,}04\%$ (trước thuế).
- $r_b^{at} = 12{,}04\% \times 0{,}8 = \mathbf{9{,}63\%}$.

*(c) Cổ phiếu ưu đãi:* $r_p = 1.500/18.000 = \mathbf{8{,}33\%}$.

*(d) Cổ phiếu thường (CAPM, dùng cho lợi nhuận giữ lại):* 
$r_e = 4\% + 1{,}3 \times (11{,}5\% - 4\%) = 4\% + 9{,}75\% = \mathbf{13{,}75\%}$.

**Phần 2 — WACC khi dùng lợi nhuận giữ lại:**
$$WACC = 0{,}25 \times 6{,}80\% + 0{,}15 \times 9{,}63\% + 0{,}10 \times 8{,}33\% + 0{,}50 \times 13{,}75\%$$
$$= 1{,}70\% + 1{,}444\% + 0{,}833\% + 6{,}875\% = \mathbf{10{,}85\%}$$

**Phần 3 — WACC khi phát hành CP mới:**
- Cần tính $r_e^{new}$ từ DDM (với β = 1,3 ở đây CAPM không có flotation hiệu chỉnh trực tiếp; thông thường ta áp $r_e^{new} = r_e/(1-f)$ — phương pháp xấp xỉ): 
  $r_e^{new} \approx 13{,}75\% / 0{,}95 \approx 14{,}47\%$.
- $WACC^{new} = 1{,}70\% + 1{,}444\% + 0{,}833\% + 0{,}50 \times 14{,}47\% = 1{,}70\% + 1{,}444\% + 0{,}833\% + 7{,}237\% = \mathbf{11{,}21\%}$.
- Chênh ~0,36% — đó là cost penalty của việc phát hành mới.

**Phần 4 — Tác động khi NHNN tăng lãi 1%:**

*(a) Vay ngân hàng:* $r_d^{at} = 9{,}5\% \times 0{,}8 = 7{,}60\%$ (tăng 0,80%).

*(b) Trái phiếu:* coupon giữ 11% nhưng giá P = 95.000:
- $r_b \approx (11.000 + 1.000)/97.500 = 12{,}31\%$ → $r_b^{at} = 9{,}85\%$ (tăng 0,22%).

*(c) Cổ phiếu ưu đãi:* không đổi nếu giá $P_p$ không đổi (giả định tĩnh) = 8,33%.

*(d) Cổ phần thường (CAPM):* không đổi nếu $r_f$ vẫn 4% (giả định Rf không đổi đột biến). Nhưng thực tế $r_f$ thường tăng theo lãi suất chính sách → giả sử $r_f$ lên 5%, $r_e = 5\% + 1{,}3 \times (11{,}5\% - 5\%) = 5\% + 8{,}45\% = 13{,}45\%$ (giảm nhẹ do MRP thu hẹp).

**WACC mới (giả định Rf tăng 1% lên 5%):**
$$WACC' = 0{,}25 \times 7{,}60\% + 0{,}15 \times 9{,}85\% + 0{,}10 \times 8{,}33\% + 0{,}50 \times 13{,}45\%$$
$$= 1{,}90\% + 1{,}478\% + 0{,}833\% + 6{,}725\% = \mathbf{10{,}94\%}$$

**Bình luận**:
- WACC tăng từ 10,85% → 10,94% (chỉ +0,09%) — tác động khá nhẹ.
- Lý do: $r_e$ giảm nhẹ (do MRP thu hẹp khi $r_f$ tăng) đã bù trừ phần lớn việc chi phí nợ tăng.
- Nếu HPG có tỷ trọng nợ cao hơn (vd 60%), tác động sẽ lớn hơn nhiều — đây là minh họa cho việc **DN có cấu trúc vốn nghiêng về cổ phần ít chịu sốc lãi suất hơn**.
</details>

---

## 🤔 Câu hỏi tư duy phản biện

1. **Tại sao chi phí vốn cổ phần thường (re) thường lớn hơn chi phí nợ vay sau thuế (rd·(1-T))?** Có trường hợp nào ngược lại không? (Gợi ý: cấu trúc rủi ro — cổ đông là claimant cuối cùng; lá chắn thuế giảm chi phí nợ thực tế.)

2. **WACC tăng có phải lúc nào cũng xấu không?** Trong trường hợp nào DN nên CHẤP NHẬN WACC cao hơn? (Gợi ý: dự án rủi ro cao nhưng IRR rất cao; thay đổi chiến lược; tăng đòn bẩy quá ngưỡng tối ưu.)

3. **Mô hình CAPM giả định β ổn định, nhưng thực tế β biến động theo thời gian**. Khi định giá dự án dài hạn 10-15 năm, ta nên dùng β quá khứ (rolling 5 năm) hay β kỳ vọng tương lai? (Gợi ý: cả hai có hạn chế; thường dùng β trung bình ngành đã unlevered–relevered theo cấu trúc vốn dự án.)

4. **Lá chắn thuế (tax shield) làm chi phí nợ rẻ hơn cổ phần — vậy tại sao DN không vay 100%?** (Gợi ý: chi phí khốn cùng tài chính — financial distress costs; rủi ro phá sản; agency costs; trade-off theory.)

5. **Trong môi trường lãi suất 0% (ZIRP) như Nhật Bản 2000-2022, WACC của các DN Nhật khác Việt Nam thế nào? Tác động đến quyết định đầu tư M&A xuyên biên giới?** (Gợi ý: chênh lệch WACC tạo ra arbitrage chi phí vốn — DN Nhật mua DN Việt giúp giảm WACC tổng; ví dụ: Sumitomo, Mitsubishi mua cổ phần các ngân hàng VN.)

---

## 📚 Nguồn đọc thêm

1. **Brealey, Myers, Allen** — *Principles of Corporate Finance*, Chương 9 ("The Cost of Capital") — khung WACC + CAPM chuẩn quốc tế.
2. **Brigham & Houston** — *Fundamentals of Financial Management*, Chương 10 ("The Cost of Capital") — bài tập đa dạng có lời giải.
3. **Damodaran Online** ([http://pages.stern.nyu.edu/~adamodar/](http://pages.stern.nyu.edu/~adamodar/)) — dữ liệu β ngành, MRP các thị trường (gồm Việt Nam) cập nhật hàng năm.
4. **PGS. TS. Nguyễn Minh Kiều** — *Tài chính Doanh nghiệp Căn bản*, NXB Thống kê — Chương về cấu trúc vốn và WACC theo ngữ cảnh Việt Nam.
5. **Báo cáo Phân tích doanh nghiệp** của các CTCK lớn (SSI, VND, HSC) — phần "Định giá DCF" thường công khai cách tính WACC từng DN, là tài liệu thực hành tốt.
