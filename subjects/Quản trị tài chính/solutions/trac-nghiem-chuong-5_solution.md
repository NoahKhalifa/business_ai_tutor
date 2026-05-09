---
exercise_file: "trac-nghiem-chuong-5.md"
solved_at: "2026-05-09T00:00:00Z"
status: "reviewed"
review_round: 1
total_questions: 30
examples_added: true
extensions_file: "extensions/trac-nghiem-chuong-5_extended.md"
---

# Lời giải: Trắc nghiệm Chương 5 — Quản trị Đầu tư dài hạn

> Dẫn chiếu bài giảng: [Financial management.md](../lectures/md/Financial%20management.md) — Chương 5
> Tóm tắt nhanh: [Financial management_summary.md](../lectures/md/Financial%20management_summary.md)

---

## Câu 1: Định nghĩa dự án xung khắc

### 📋 Đề bài
> Những dự án nhằm thực hiện cùng một công việc mà nếu chấp nhận dự án này thì buộc phải loại bỏ các dự án còn lại — A. Không loại trừ / B. Xung khắc / C. Phụ thuộc / D. Độc lập.

### 📚 Kiến thức nền
**Phân loại dự án theo quan hệ** (Mục 5.1 — Chương 5):
- **Độc lập**: thực hiện dự án này không ảnh hưởng dự án khác.
- **Phụ thuộc**: dự án này kéo theo dự án khác.
- **Xung khắc (mutually exclusive)**: chấp nhận 1 → loại 1 hoặc nhiều dự án còn lại (cùng phục vụ 1 mục đích).

### ✅ Kết luận
**Đáp án: B. Các dự án xung khắc**

---

## Câu 2: Đặc trưng đầu tư dài hạn

### 📋 Đề bài
> Việc bỏ vốn mua TSCĐ, chấp nhận rủi ro, theo đuổi mục tiêu sử dụng khai thác có hiệu quả — A. Đầu tư dài hạn / B. Đầu tư ngắn hạn / C. Tài trợ dài hạn / D. Tài trợ ngắn hạn.

### 📚 Kiến thức nền
Đầu tư dài hạn = bỏ vốn để hình thành/mua sắm **TSCĐ** và các tài sản dài hạn khác → kỳ vọng sinh lời nhiều năm, chấp nhận rủi ro vốn dài. "Tài trợ" là quyết định **huy động** vốn, khác với quyết định **đầu tư**.

### ✅ Kết luận
**Đáp án: A. Đầu tư dài hạn**

---

## Câu 3: Phương pháp KHÔNG xét giá trị thời gian của tiền

### 📋 Đề bài
> Phương pháp nào không xem xét yếu tố giá trị thời gian của tiền — A. PBP / B. NPV / C. PI / D. IRR.

### 📚 Kiến thức nền
- **PBP truyền thống**: cộng dồn dòng tiền danh nghĩa, KHÔNG chiết khấu → bỏ qua giá trị thời gian.
- **NPV, PI, IRR**: đều dùng chiết khấu, có tính giá trị thời gian.
> *Lưu ý*: nếu là **Discounted PBP** thì lại có chiết khấu, nhưng PBP "truyền thống" trong sách giáo khoa thì không.

### ✅ Kết luận
**Đáp án: A. Kỳ hoàn vốn (PBP)**

---

## Câu 4: Tiêu chuẩn chấp nhận theo NPV

### 📋 Đề bài
> Theo NPV, tỷ lệ sinh lời đòi hỏi xác định trước, tiêu chuẩn lựa chọn — A. NPV không âm / B. NPV = 0 / C. NPV âm / D. NPV dương.

### 📚 Kiến thức nền
Quy tắc NPV: chấp nhận dự án khi $NPV \geq 0$ (không âm). NPV = 0 nghĩa là dự án vừa đủ bù chi phí vốn (điểm hòa vốn kinh tế) — vẫn chấp nhận được. Đáp án D quá hẹp (loại trường hợp NPV = 0).

### ✅ Kết luận
**Đáp án: A. Giá trị hiện tại thuần (NPV) không âm**

---

## Câu 5: Khi nào NPV giảm

### 📋 Đề bài
> NPV giảm (ceteris paribus) nếu — A. Sinh lời đòi hỏi giảm / B. PBP giảm / C. PI tăng / D. Lãi suất chiết khấu tăng.

### 📚 Kiến thức nền
$$NPV = \sum_{t=1}^{n} \dfrac{CF_t}{(1+r)^t} - ICO$$
Khi $r \uparrow$ → mẫu số $\uparrow$ → PV của các $CF_t$ ↓ → NPV ↓. Đây là quan hệ **nghịch biến** giữa NPV và $r$.

### ✅ Kết luận
**Đáp án: D. Lãi suất chiết khấu tăng**

---

## Câu 6: Khi nào NPV tăng

### 📋 Đề bài
> NPV tăng (ceteris paribus) nếu — A. Sinh lời đòi hỏi tăng / B. r tăng / C. r giảm / D. PI giảm.

### 📚 Kiến thức nền
Cùng logic Câu 5: $r \downarrow$ → PV ↑ → NPV ↑.

### ✅ Kết luận
**Đáp án: C. Lãi suất chiết khấu giảm**

---

## Câu 7: Định nghĩa IRR

### 📋 Đề bài
> Tỷ lệ chiết khấu mà tại đó NPV = 0 — A. Lãi vay / B. IRR / C. WACC / D. PI.

### 📚 Kiến thức nền
**IRR (Internal Rate of Return)**: tỷ lệ chiết khấu nội tại $r^*$ thỏa $\sum CF_t/(1+r^*)^t - ICO = 0$.

### ✅ Kết luận
**Đáp án: B. Tỷ suất hoàn vốn nội bộ (IRR)**

---

## Câu 8: Nhận định bất hợp lý về đầu tư hình thành DN

### 📋 Đề bài
> Đầu tư để hình thành & đưa DN vào hoạt động, nhận định bất hợp lý — A. Buộc phải bao gồm XDCB / B. Có thể không bao gồm XDCB / C. Có thể bao gồm XDCB / D. Có thể bao gồm mua sắm thiết bị.

### 📚 Kiến thức nền
Khi hình thành DN, đầu tư **xây dựng cơ bản** (nhà xưởng, văn phòng, hạ tầng) thường là một cấu phần — nhưng KHÔNG bắt buộc với mọi loại hình DN (ví dụ DN dịch vụ, công nghệ thuần có thể chỉ thuê văn phòng & mua thiết bị, không xây dựng gì). Vì vậy "buộc phải bao gồm XDCB" là **bất hợp lý**.

### ✅ Kết luận
**Đáp án: A. Buộc phải bao gồm đầu tư xây dựng cơ bản**

### ⚠️ Sai lầm thường gặp
Dễ chọn B vì nghĩ "DN nào cũng phải xây cái gì đó". Thực tế, DN dịch vụ/công nghệ thuần có thể đầu tư hoàn toàn vào thiết bị + thuê mặt bằng → KHÔNG có XDCB.

---

## Câu 9: Tiêu chuẩn PI cho dự án xung khắc

### 📋 Đề bài
> Khi dùng PI thẩm định dự án xung khắc — A. PI lớn nhất / B. PI không âm lớn nhất / C. PI > 1 và lớn nhất / D. PI = 1.

### 📚 Kiến thức nền
$$PI = \dfrac{\sum PV(CF_t)}{ICO}$$
Quy tắc 2 bước:
1. **Lọc**: chỉ chấp nhận dự án có $PI > 1$ (PV thu nhập > vốn).
2. **Xếp hạng**: trong các dự án thỏa, chọn cái **PI lớn nhất**.

### ✅ Kết luận
**Đáp án: C. Chọn dự án có PI lớn hơn 1 và lớn nhất**

---

## Câu 10: Định nghĩa NPV

### 📋 Đề bài
> NPV = …… của dự án trừ đi …… của dự án.

### 📚 Kiến thức nền
$NPV = \sum PV(\text{thu nhập}) - \sum PV(\text{chi phí đầu tư})$ — bản chất là **lợi ích ròng** của dự án quy về hiện tại.

### ✅ Kết luận
**Đáp án: D. Giá trị hiện tại các khoản thu nhập; giá trị hiện tại các khoản chi phí**

---

## Câu 11: Tính dòng thu nhập (CF) sau thuế

### 📋 Đề bài
> Máy 200 trđ, n = 4 năm, thanh lý 5 trđ, EBT = 30/32/32/28 trđ, t = 25%, KH đường thẳng, thanh lý không bị đánh thuế. Tính CF qua 4 năm.

### 📚 Kiến thức nền
$$CF_t = EBT_t \cdot (1-t) + \text{Khấu hao}_t \quad (\text{năm cuối} + \text{Giá trị thanh lý sau thuế})$$
- $\text{KH/năm} = \dfrac{200}{4} = 50$ trđ (theo nguyên giá; quy ước trong giáo trình QTTC này).
- LN sau thuế: $30 \cdot 0.75 = 22{,}5$; $32 \cdot 0.75 = 24$; $32 \cdot 0.75 = 24$; $28 \cdot 0.75 = 21$.

### ✍️ Lời giải
| Năm | EBT | LN sau thuế | + KH | + Thanh lý | **CF** |
|---|---|---|---|---|---|
| 1 | 30 | 22,5 | 50 | — | **72,5** |
| 2 | 32 | 24   | 50 | — | **74** |
| 3 | 32 | 24   | 50 | — | **74** |
| 4 | 28 | 21   | 50 | 5 | **76** |

### ✅ Kết luận
**Đáp án: D. 72,5; 74; 74; 76 triệu đồng**

### ⚠️ Sai lầm thường gặp
- Nhầm "thu nhập trước thuế = 30" thành "doanh thu" → cộng nhầm KH 2 lần.
- Quên cộng giá trị thanh lý vào CF năm cuối → ra đáp án C (71 thay vì 76).
- Trừ KH = (200-5)/4 = 48,75 (sai cho bài này; giáo trình dùng KH theo nguyên giá đầy đủ).

---

## Câu 12: Phương pháp NPV — đặc điểm

### 📋 Đề bài
> Phương pháp có giá trị thời gian, đo giá trị tăng thêm tuyệt đối, không phản ánh sinh lời/đồng vốn — A. PBP / B. NPV / C. IRR / D. PI.

### 📚 Kiến thức nền
**NPV** đo **mức tăng thêm giá trị tuyệt đối** (đơn vị tiền), không phải tỷ lệ → không cho biết sinh lời/đồng vốn (cái đó là PI hoặc IRR).

### ✅ Kết luận
**Đáp án: B. Phương pháp giá trị hiện tại thuần (NPV)**

---

## Câu 13: NPV cho 3 dự án xung khắc

### 📋 Đề bài
> 3 dự án xung khắc, dùng NPV — chọn dự án — A. NPV>0 nhỏ nhất / B. NPV lớn nhất / C. NPV không âm / D. NPV ≥ 0 lớn nhất.

### 📚 Kiến thức nền
Quy tắc NPV cho dự án xung khắc:
1. **Lọc**: NPV ≥ 0.
2. **Xếp hạng**: chọn cái **NPV lớn nhất** trong nhóm thỏa.
- B sai nhẹ: nếu cả 3 đều có NPV âm thì "NPV lớn nhất" vẫn là số âm → không chấp nhận. Phải có thêm điều kiện ≥ 0.

### ✅ Kết luận
**Đáp án: D. Có NPV không âm (≥0) lớn nhất**

---

## Câu 14: Tính NPV cụ thể

### 📋 Đề bài
> Cùng dự án Câu 11 (CF sau thuế = 22,5/24/24/21 + KH 50, năm 4 thanh lý 5), r = 15%. Tính NPV.

### 📚 Kiến thức nền
$$NPV = -ICO + \sum_{t=1}^{n} \dfrac{CF_t}{(1+r)^t}$$
Sử dụng CF từ Câu 11: 72,5; 74; 74; 76.

### ✍️ Lời giải
$$NPV = -200 + \dfrac{72{,}5}{1{,}15} + \dfrac{74}{1{,}15^2} + \dfrac{74}{1{,}15^3} + \dfrac{76}{1{,}15^4}$$

| Năm | CF | $(1{,}15)^t$ | PV |
|---|---|---|---|
| 1 | 72,5 | 1,1500 | 63,04 |
| 2 | 74   | 1,3225 | 55,95 |
| 3 | 74   | 1,5209 | 48,66 |
| 4 | 76   | 1,7490 | 43,45 |
| **Tổng PV** |  |  | **211,11** |

$NPV = 211{,}11 - 200 = 11{,}11$ triệu đồng > 0 → **nên thực hiện**.

### ✅ Kết luận
**Đáp án: D. NPV = 11,11 triệu đồng, nên thực hiện dự án**

---

## Câu 15: So sánh IRR với r

### 📋 Đề bài
> Vốn 100 trđ, CF = 40/50/60 (3 năm), r = 20%/năm. Có thực hiện không?

### 📚 Kiến thức nền
Quy tắc IRR: chấp nhận nếu $IRR \geq r$. Cách nhanh: tính NPV ở r = 20%, nếu **NPV > 0 → IRR > 20%** → chấp nhận.

### ✍️ Lời giải
$NPV(20\%) = -100 + \dfrac{40}{1{,}2} + \dfrac{50}{1{,}44} + \dfrac{60}{1{,}728}$
$= -100 + 33{,}33 + 34{,}72 + 34{,}72 = +2{,}78$ trđ > 0
→ $IRR > 20\%$ → chấp nhận dự án.

### ✅ Kết luận
**Đáp án: C. Có thực hiện, vì IRR > tỷ lệ chiết khấu**

---

## Câu 16: Định nghĩa dự án phụ thuộc

### 📋 Đề bài
> Dự án mà việc thực hiện DA này dẫn tới buộc phải thực hiện DA khác — A. Độc lập / B. Phụ thuộc / C. Thay thế / D. Xung khắc.

### 📚 Kiến thức nền
- Phụ thuộc: A → B (làm A buộc phải làm B).
- Xung khắc: A và B không thể cùng tồn tại.

### ✅ Kết luận
**Đáp án: B. Dự án phụ thuộc**

---

## Câu 17: Tính PI

### 📋 Đề bài
> Vốn 1.000 trđ, n = 5 năm, CF đều 300 trđ, r = 16%. Tính PI và quyết định.

### 📚 Kiến thức nền
$PI = \dfrac{\sum PV(CF)}{ICO}$. Với CF đều, dùng công thức niên kim:
$$PVA = A \times \dfrac{1-(1+r)^{-n}}{r}$$

### ✍️ Lời giải
$PVA = 300 \times \dfrac{1 - 1{,}16^{-5}}{0{,}16} = 300 \times 3{,}2743 = 982{,}29$ trđ

$PI = \dfrac{982{,}29}{1000} = 0{,}982 < 1$ → **không nên thực hiện**.

### ✅ Kết luận
**Đáp án: A. Không nên thực hiện dự án vì PI < 1**

### ⚠️ Sai lầm thường gặp
Nhầm PI = NPV/ICO (sai). PI = **PV thu nhập** / ICO, KHÔNG phải NPV/ICO.

---

## Câu 18: So sánh 2 dự án xung khắc bằng NPV

### 📋 Đề bài
> Bức 1: vốn 200, CF = 72,5/74/74/76 (4 năm). Bức 2: vốn 250, CF = 75,5/77/78,5/72,5/86 (5 năm). r = 15%.

### 📚 Kiến thức nền
Tính NPV từng dự án; chọn dự án NPV > 0 và lớn nhất.

### ✍️ Lời giải
- $NPV_1 = 11{,}11$ trđ (đã tính ở Câu 14).
- $NPV_2 = -250 + 65{,}65 + 58{,}22 + 51{,}62 + 41{,}45 + 42{,}76 = +9{,}70$ trđ.

So sánh: $NPV_1 = 11{,}11 > NPV_2 = 9{,}70$ → chọn bức điện 1.

### ✅ Kết luận
**Đáp án: B. Thực hiện mua theo bức điện 1, vì NPV(1) > 0 và NPV(1) > NPV(2)**

### 💡 Mẹo
Khi 2 dự án xung khắc có **tuổi thọ khác nhau**, lý thuyết khuyến cáo dùng EAA (Equivalent Annual Annuity) thay vì NPV trực tiếp. Đề trắc nghiệm ở mức cơ bản → vẫn chọn theo NPV trực tiếp.

---

## Câu 19: PBP cho dự án xung khắc

### 📋 Đề bài
> A: vốn 120, CF 55/năm; B: vốn 140, CF 65/năm; n = 4 năm; chỉ chọn dự án có PBP ≤ 3 năm. Chọn 1 trong 2.

### 📚 Kiến thức nền
$PBP = \dfrac{ICO}{CF_{annual}}$ (CF đều).

### ✍️ Lời giải
- $PBP_A = 120/55 = 2{,}182$ năm
- $PBP_B = 140/65 = 2{,}154$ năm

Cả hai đều thỏa ≤ 3, nhưng đề yêu cầu **chọn 1 trong 2** → chọn dự án có PBP nhỏ hơn: $PBP(B) = 2{,}154 < PBP(A) = 2{,}182$ → chọn **dự án B**. Ngoài ra dự án B cũng có CF/năm cao hơn (65 > 55).

### ✅ Kết luận
**Đáp án: B. Chọn dự án B**

---

## Câu 20: PBP có chi phí thêm

### 📋 Đề bài
> Vốn 150, CF = 42/39/36/34/34 (5 năm), năm 3 chi phí thêm 10 (đầu tư bổ sung). PBP ≤ 3?

### 📚 Kiến thức nền
Khi có chi phí đầu tư thêm trong kỳ → coi là dòng tiền âm bổ sung; cộng dồn dòng tiền **thuần** để tìm thời điểm bù được vốn 150.

### ✍️ Lời giải
| Năm | CF gốc | Chi phí thêm | CF thuần | Cộng dồn |
|---|---|---|---|---|
| 1 | 42 | — | 42 | 42 |
| 2 | 39 | — | 39 | 81 |
| 3 | 36 | -10 | 26 | 107 |
| 4 | 34 | — | 34 | 141 |
| 5 | 34 | — | 34 | 175 |

Cuối năm 4 mới có 141 trđ < 150 → cần thêm 9 trđ từ năm 5.
$PBP = 4 + \dfrac{9}{34} \approx 4{,}26$ năm > 3 → **KHÔNG thỏa điều kiện**.

### ✅ Kết luận
**Đáp án: D. Không thực hiện dự án**

### ⚠️ Sai lầm thường gặp
Bỏ qua chi phí thêm 10 trđ năm 3 → tính PBP ≈ 3,97 (vẫn > 3). Cách tính nào cũng dẫn tới PBP > 3 → loại A, B, C (đều cho con số < 3).

---

## Câu 21: Định nghĩa dự án độc lập

### 📋 Đề bài
> Dự án mà thực hiện DA này không ảnh hưởng & không bị tác động bởi DA khác — A. Phụ thuộc / B. Xung khắc / C. Mâu thuẫn / D. Độc lập.

### ✅ Kết luận
**Đáp án: D. Các dự án độc lập**

---

## Câu 22: Sở hữu công ty cổ phần

### 📋 Đề bài
> Công ty cổ phần được sở hữu bởi — A. HĐQT / B. Nhà quản lý / C. HĐ thành viên / D. Cổ đông.

### 📚 Kiến thức nền
Theo Luật Doanh nghiệp 2020 (VN), **cổ đông** là người sở hữu vốn cổ phần → là chủ sở hữu công ty cổ phần. HĐQT là cơ quan **đại diện** quản lý, do cổ đông bầu ra.

### ✅ Kết luận
**Đáp án: D. Các cổ đông**

---

## Câu 23: NPV tại IRR

### 📋 Đề bài
> IRR là mức lãi suất tại đó NPV nhận giá trị — A. 0 / B. âm / C. ≥ 0 / D. > 0.

### ✅ Kết luận
**Đáp án: A. 0** (định nghĩa IRR)

---

## Câu 24: Trùng Câu 7 — IRR

### 📋 Đề bài
> Tỷ lệ chiết khấu mà tại đó NPV = 0 — A. PI / B. IRR / C. Lãi vay / D. WACC.

### ✅ Kết luận
**Đáp án: B. Tỷ suất hoàn vốn nội bộ (IRR)**

---

## Câu 25: Tính CF năm thiếu

### 📋 Đề bài
> CF năm 1 = 2.000 USD, năm 2 = ?, năm 3 = năm 4 = 4.000 USD. Vốn 11.958,07 USD, r = 12%. Tìm CF năm 2 (giả định NPV = 0).

### 📚 Kiến thức nền
Từ điều kiện $NPV = 0$:
$$ICO = \sum \dfrac{CF_t}{(1+r)^t} \Rightarrow X = \left[ICO - \sum_{t \neq 2} \dfrac{CF_t}{(1+r)^t}\right] \times (1+r)^2$$

### ✍️ Lời giải
$\dfrac{2000}{1{,}12} + \dfrac{4000}{1{,}12^3} + \dfrac{4000}{1{,}12^4} = 1785{,}71 + 2847{,}12 + 2542{,}07 = 7174{,}90$

$\dfrac{X}{1{,}12^2} = 11958{,}07 - 7174{,}90 = 4783{,}17$

$X = 4783{,}17 \times 1{,}2544 = 6000{,}00$ USD

### ✅ Kết luận
**Đáp án: C. 6.000 USD**

---

## Câu 26: TSCĐ không phải trích khấu hao

### 📋 Đề bài
> DN không phải trích KH với TSCĐ — A. Đã KH hết NG / B. Nhận liên doanh / C. Cho thuê hoạt động / D. Thuê tài chính.

### 📚 Kiến thức nền
Theo Thông tư 45/2013/TT-BTC: TSCĐ đã khấu hao hết nguyên giá nhưng còn được sử dụng → **không tính KH nữa** vì không còn giá trị còn lại để phân bổ.
- B, C, D: vẫn trích KH (B: bên nhận liên doanh trích; C: bên cho thuê trích; D: bên đi thuê tài chính trích vì có quyền sử dụng kinh tế).

### ✅ Kết luận
**Đáp án: A. TSCĐ đang được sử dụng song đã khấu hao hết nguyên giá**

---

## Câu 27: Phương pháp PI — đặc điểm

### 📋 Đề bài
> Phương pháp có giá trị thời gian, xác định mức sinh lời/đồng vốn, sinh lời tương đối, không thể hiện đóng góp tuyệt đối — A. PBP / B. IRR / C. NPV / D. PI.

### 📚 Kiến thức nền
**PI là tỷ số tương đối** (PV thu nhập / ICO) → cho biết "1 đồng vốn sinh ra bao nhiêu đồng PV", nhưng không cho biết quy mô tuyệt đối (200 trđ NPV hay 2 trđ NPV — PI có thể giống nhau).

### ✅ Kết luận
**Đáp án: D. Phương pháp Chỉ số sinh lợi (PI)**

---

## Câu 28: Vốn hóa lãi vay vào nguyên giá TSCĐ

### 📋 Đề bài
> TSCĐ hình thành từ vốn vay, NG bao gồm phần lãi vay tính trong khoảng — A. Từ khi vay đến khi trả hết / B. Từ khi mua TSCĐ đến khi sẵn sàng sử dụng / C. Từ khi mua đến khi trả hết vay / D. Từ khi mua đến khi nhận TSCĐ.

### 📚 Kiến thức nền
Theo VAS 16 (Chuẩn mực kế toán TSCĐ hữu hình) & Thông tư 45/2013: lãi vay được **vốn hóa vào nguyên giá** chỉ trong giai đoạn TSCĐ đang được hình thành/lắp đặt, đến khi **sẵn sàng sử dụng**. Sau thời điểm đó, lãi vay được ghi nhận vào **chi phí tài chính** (kết quả kinh doanh).

### ✅ Kết luận
**Đáp án: B. Từ thời điểm mua TSCĐ đến thời điểm đưa TSCĐ đó vào trạng thái sẵn sàng sử dụng**

---

## Câu 29: 2 dự án xung khắc tuổi thọ khác nhau

### 📋 Đề bài
> Dùng NPV cho 2 dự án xung khắc tuổi thọ khác — Cách giải quyết — A. Tái đầu tư CF của DA ngắn hơn đến hết hạn DA dài hơn / B. NPV>0 chọn DA dài hơn / C. NPV>0 chọn DA ngắn hơn / D. Thực hiện cả hai nếu NPV>0.

### 📚 Kiến thức nền
**Phương pháp Common Time Horizon (chu kỳ chung)**: kéo dài 2 dự án về cùng thời gian, giả định CF của dự án ngắn hơn được **tái đầu tư** ở mức lợi tức yêu cầu (cost of capital) cho đến khi cùng kết thúc với dự án dài. Sau đó so sánh NPV. (Tương đương phương pháp EAA — Equivalent Annual Annuity).

### ✅ Kết luận
**Đáp án: A. Coi toàn bộ luồng tiền của dự án có tuổi thọ ngắn hơn được tái đầu tư cho tới ngày hết hạn của dự án có tuổi thọ dài hơn với mức lợi tức đòi hỏi của công ty**

---

## Câu 30: Luồng tiền thuần KHÔNG bao gồm

### 📋 Đề bài
> Luồng tiền thuần dự án KHÔNG bao gồm — A. Khấu hao / B. Thuế thu nhập / C. Thu nhập sau thuế / D. Giá trị thanh lý.

### 📚 Kiến thức nền
Luồng tiền thuần (Net Cash Flow):
$$CF_t = (\text{Thu nhập sau thuế})_t + (\text{Khấu hao})_t \;[+ \text{Giá trị thanh lý}_n]$$
- **Thu nhập sau thuế** (C): đã trừ thuế thu nhập → có trong CF.
- **Thuế thu nhập** (B): được trừ ở bước EBT → (1-t) → đã được phản ánh trong CF (gián tiếp).
- **Giá trị thanh lý** (D): cộng vào CF năm cuối.
- **Khấu hao** (A): là chi phí KHÔNG sinh ra tiền (non-cash) → tự thân không phải dòng tiền. Trong công thức CF, khấu hao xuất hiện với vai trò **lá chắn thuế** (tax shield) — bị trừ để tính EBT, rồi cộng lại — chứ KHÔNG phải dòng tiền độc lập.

→ Theo nghĩa "khấu hao tự thân không phải khoản tiền vào/ra của dự án", **A là đáp án**.

### ✅ Kết luận
**Đáp án: A. Khấu hao**

### 💡 Ghi chú
Câu này dễ gây tranh cãi vì khấu hao có "xuất hiện" trong công thức CF (bị trừ rồi cộng lại). Nhưng bản chất là **non-cash item**, không phải dòng tiền thực sự. Đáp án A đúng theo cách hiểu phổ biến trong giáo trình QTTC Việt Nam.

---

## 📊 Bảng tóm tắt đáp án

| Câu | Đáp án | Câu | Đáp án | Câu | Đáp án |
|---|---|---|---|---|---|
| 1 | B | 11 | D | 21 | D |
| 2 | A | 12 | B | 22 | D |
| 3 | A | 13 | D | 23 | A |
| 4 | A | 14 | D | 24 | B |
| 5 | D | 15 | C | 25 | C |
| 6 | C | 16 | B | 26 | A |
| 7 | B | 17 | A | 27 | D |
| 8 | A | 18 | B | 28 | B |
| 9 | C | 19 | B | 29 | A |
| 10 | D | 20 | D | 30 | A |

---

## 🏢 Ví dụ thực tế minh họa kiến thức Chương 5

### Ví dụ 1: VinFast — Quyết định đầu tư nhà máy ô tô điện

**Bối cảnh**: Năm 2017, Vingroup khởi công nhà máy VinFast tại Hải Phòng với cam kết đầu tư rất lớn để tham gia ngành ô tô — một trong những quyết định **đầu tư dài hạn** điển hình của DN VN. Sau đó, VinFast pivot sang xe điện hoàn toàn (2022) và xây nhà máy thứ hai tại Mỹ (Bắc Carolina), tiếp tục là chuỗi quyết định đầu tư mở rộng.

**Áp dụng kiến thức Chương 5**:
- **Đặc trưng đầu tư dài hạn** (liên hệ Câu 2): bỏ vốn lớn mua TSCĐ (dây chuyền, thiết bị), chấp nhận rủi ro thị trường mới, theo đuổi mục tiêu khai thác hiệu quả nhiều năm.
- **Dòng tiền dự án** (liên hệ Câu 11, 14): phải dự báo CF gồm doanh thu xe bán ra, trừ chi phí vận hành & khấu hao thiết bị (đường thẳng theo nguyên giá), cộng giá trị thanh lý nhà máy cuối vòng đời.
- **Xung khắc giữa các phương án** (liên hệ Câu 1, 18): VinFast từng phải chọn giữa xe xăng (mở rộng) vs xe điện (chuyển đổi hoàn toàn) — đây là dự án xung khắc, chấp nhận một thì loại bỏ cái còn lại.

**Bài học**: Với dự án quy mô lớn, NPV/IRR mới chỉ là 1 lát cắt; thực tế DN còn cân nhắc tầm nhìn chiến lược dài hạn (chuyển dịch toàn cầu sang xe điện) ngay cả khi NPV ngắn hạn của phương án xe điện thấp hơn xe xăng.

---

### Ví dụ 2: Vinamilk — Đánh giá dự án mở rộng nhà máy sữa

**Bối cảnh**: Vinamilk thường xuyên đầu tư mở rộng năng lực sản xuất (nhà máy sữa Việt Nam tại Bình Dương, "siêu nhà máy" sữa nước, các trang trại bò sữa organic). Mỗi dự án đều phải qua quy trình thẩm định tài chính chặt chẽ trình HĐQT.

**Áp dụng kiến thức Chương 5**:
- **Tính dòng tiền sau thuế** (liên hệ Câu 11): EBT = doanh thu sữa - chi phí nguyên liệu - khấu hao dây chuyền; CF = LN sau thuế + khấu hao + giá trị thanh lý cuối kỳ.
- **NPV với r = WACC** (liên hệ Câu 14): chiết khấu CF dự án theo chi phí vốn bình quân của Vinamilk (thường khoảng 10-12%/năm theo công bố báo cáo thường niên).
- **Chỉ số PI cho ranking** (liên hệ Câu 9, 17): khi có nhiều dự án mở rộng cạnh tranh ngân sách hằng năm, Vinamilk dùng PI để xếp hạng — chọn dự án có PI > 1 và lớn nhất trong giới hạn vốn.

**Bài học**: DN trưởng thành như Vinamilk không chỉ nhìn vào 1 chỉ số, mà kết hợp NPV (giá trị tuyệt đối) + PI (hiệu quả/đồng vốn) + PBP (rủi ro thu hồi). Phương pháp PI đặc biệt hữu ích khi nguồn vốn đầu tư hằng năm bị giới hạn (capital rationing).

---

### Ví dụ 3: Vingroup — Lựa chọn giữa các dự án xung khắc trong tập đoàn

**Bối cảnh**: Vingroup vận hành đa ngành (BĐS Vinhomes, bán lẻ VinMart trước đây, ô tô VinFast, công nghệ VinAI, du lịch Vinpearl...). Khi nguồn vốn hạn chế, ban lãnh đạo phải liên tục lựa chọn rút vốn ngành nào, đầu tư mạnh vào ngành nào — câu chuyện điển hình về **dự án xung khắc**.

**Áp dụng kiến thức Chương 5**:
- **Dự án xung khắc** (liên hệ Câu 1, 13, 21): năm 2019 Vingroup quyết định bán mảng bán lẻ VinMart cho Masan để dồn nguồn lực cho VinFast & công nghệ — bỏ dự án này để chấp nhận dự án kia.
- **NPV không âm và lớn nhất** (liên hệ Câu 13): khi cân nhắc ưu tiên giữa nhiều dự án mở rộng, tiêu chí là chọn dự án có NPV ≥ 0 và lớn nhất, nhưng phải xét cả tuổi thọ dự án.
- **Tuổi thọ khác nhau & tái đầu tư** (liên hệ Câu 29, 18): Vinhomes (BĐS) có chu kỳ dự án 3-5 năm, VinFast (sản xuất xe) có chu kỳ 10+ năm — khi so sánh phải dùng phương pháp Common Time Horizon hoặc EAA, không so NPV trực tiếp.

**Bài học**: Tài chính dự án không chỉ là toán — nó là công cụ giúp ban lãnh đạo ra quyết định **tái phân bổ nguồn lực** giữa các đơn vị kinh doanh. Khi dự án xung khắc, khái niệm "chi phí cơ hội" trở nên hiện hữu: tiền dồn vào VinFast là tiền không thể đổ vào VinMart.
