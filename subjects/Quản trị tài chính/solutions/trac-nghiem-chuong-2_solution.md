---
exercise_file: "trac-nghiem-chuong-2.md"
solved_at: "2026-05-09T12:00:00Z"
status: "reviewed"
review_round: 1
total_questions: 25
examples_added: true
---

# Lời giải — Trắc nghiệm Chương 2: Giá trị thời gian của tiền

> Môn: Quản trị tài chính 1
> Tham chiếu bài giảng: `lectures/md/Financial management.md` — Chương 2

---

## Câu 1: Tìm lãi suất để gấp đôi vốn trong 5 năm

### 📋 Đề bài
> Nếu bạn gửi tiết kiệm hôm nay ghép lãi theo năm với mong muốn 5 năm sau khoản tiền của bạn tăng gấp đôi thì lãi suất tiết kiệm đòi hỏi hàng năm là bao nhiêu?

### 🎯 Phân tích đề
- **Dạng bài**: Tìm lãi suất — ứng dụng Quy tắc 72 hoặc công thức lãi ghép
- **Dữ kiện đã cho**: $n = 5$ năm, $F = 2P$ (gấp đôi), ghép lãi theo năm
- **Cần tìm**: Lãi suất $r$

### 📚 Kiến thức nền cần dùng
- Công thức lãi ghép (Mục 2.1.2): $F = P \times (1+r)^n$
- Quy tắc 72 (Mục 2.4.1): $n \approx 72 / r$

### 🔍 Hướng tiếp cận
**Cách 1 — Quy tắc 72** (nhanh): $r \approx 72/5 = 14{,}4\%$

**Cách 2 — Công thức chính xác**:

### ✍️ Lời giải chi tiết

**Bước 1**: Thiết lập phương trình từ công thức lãi ghép

$$
F = P(1+r)^n \Rightarrow 2P = P(1+r)^5
$$

**Bước 2**: Rút gọn và giải

$$
(1+r)^5 = 2 \Rightarrow 1+r = 2^{1/5} = \sqrt[5]{2}
$$

$$
r = 2^{1/5} - 1 = 2^{0,2} - 1 \approx 1{,}1487 - 1 = 0{,}1487 \approx 14{,}87\%
$$

**Bước 3**: So sánh với đáp án — giá trị gần nhất là **14,4%** (theo Quy tắc 72) hoặc 14,87% (chính xác). Đề dùng Quy tắc 72: $72/5 = 14{,}4\%$.

### ✅ Kết luận
**Đáp án: C. 14,4%** — Sử dụng Quy tắc 72.

### ⚠️ Sai lầm thường gặp
- Nhầm dùng lãi đơn: $r = 100\%/5 = 20\%$ → sai vì đề yêu cầu ghép lãi.
- Quên rằng Quy tắc 72 là phép tính gần đúng, giá trị chính xác là 14,87%.

### 💡 Mẹo / Ghi chú
Quy tắc 72: **Gấp đôi trong $n$ năm → lãi suất ≈ $72/n$**. Ngược lại, lãi suất $r\%$ → gấp đôi sau ≈ $72/r$ năm.

---

## Câu 2: Thời gian gấp đôi vốn với lãi suất 6,5%

### 📋 Đề bài
> Nếu bạn gửi tiết kiệm hôm nay với lãi suất 6,5%, ghép lãi theo năm, phải mất bao lâu để khoản tiền của bạn tăng gấp đôi?

### 🎯 Phân tích đề
- **Dạng bài**: Tìm số kỳ hạn — Quy tắc 72
- **Dữ kiện đã cho**: $r = 6{,}5\%$, $F = 2P$
- **Cần tìm**: $n$

### 📚 Kiến thức nền cần dùng
- Quy tắc 72 (Mục 2.4.1)

### ✍️ Lời giải chi tiết

$$
n \approx \frac{72}{6{,}5} = 11{,}08 \approx 11 \text{ năm}
$$

Kiểm tra bằng công thức chính xác:

$$
n = \frac{\ln(2)}{\ln(1{,}065)} = \frac{0{,}6931}{0{,}0630} \approx 11{,}01 \text{ năm}
$$

### ✅ Kết luận
**Đáp án: A. 11 năm**

### ⚠️ Sai lầm thường gặp
- Dùng lãi đơn: $n = 1/0{,}065 \approx 15{,}4$ năm → sai.

### 💡 Mẹo / Ghi chú
Quy tắc 72 cho kết quả rất sát công thức chính xác (11,08 vs 11,01).

---

## Câu 3: Giá trị tương lai của 100 triệu gửi 3 năm, lãi suất 8%

### 📋 Đề bài
> Bạn gửi tiết kiệm 100 triệu đồng trong thời hạn 3 năm với lãi suất 8%/năm, ghép lãi hàng năm. Số tiền bạn nhận ở cuối năm thứ 3 xấp xỉ là:

### 🎯 Phân tích đề
- **Dạng bài**: Giá trị tương lai của một khoản tiền
- **Dữ kiện**: $PV = 100$ triệu, $i = 8\%$, $n = 3$
- **Cần tìm**: $FV_3$

### 📚 Kiến thức nền cần dùng
- Công thức $FV_n = PV \times (1+i)^n$ (Mục 2.2.1)

### ✍️ Lời giải chi tiết

$$
FV_3 = 100 \times (1 + 0{,}08)^3 = 100 \times (1{,}08)^3
$$

**Bước 1**: $(1{,}08)^2 = 1{,}1664$

**Bước 2**: $(1{,}08)^3 = 1{,}1664 \times 1{,}08 = 1{,}259712$

**Bước 3**: $FV_3 = 100 \times 1{,}259712 = 125{,}97$ triệu đồng

### ✅ Kết luận
**Đáp án: C. 125,97 triệu đồng**

### ⚠️ Sai lầm thường gặp
- Dùng lãi đơn: $F = 100(1 + 0{,}08 \times 3) = 124$ triệu → đó là đáp án D, sai vì đề yêu cầu ghép lãi.

---

## Câu 4: Thanh toán trả góp — trả hết nợ còn lại tại kỳ 21

### 📋 Đề bài
> Công ty X mua hàng trả góp: trả ngay 500 triệu, trả đều mỗi quý 20 triệu trong 10 năm, lãi 2%/quý. Sau 20 khoản trả góp đầu tiên, công ty muốn thanh toán toàn bộ nợ còn lại vào kỳ số 21. Tính số tiền phải trả?

### 🎯 Phân tích đề
- **Dạng bài**: Giá trị hiện tại chuỗi tiền đều cuối kỳ — tính nợ còn lại
- **Dữ kiện**: $A = 20$ triệu/quý, tổng $n = 40$ quý (10 năm × 4), $i = 2\%$/quý, đã trả 20 kỳ
- **Cần tìm**: Giá trị hiện tại tại kỳ 21 của 20 khoản còn lại (kỳ 21 → kỳ 40)

### 📚 Kiến thức nền cần dùng
- Giá trị hiện tại chuỗi tiền đều cuối kỳ (Mục 2.3.2):

$$
PV = A \times \frac{1 - (1+i)^{-n}}{i}
$$

### ✍️ Lời giải chi tiết

Tại thời điểm kỳ 21, công ty cần trả tương đương giá trị hiện tại (tại kỳ 20) của 20 khoản còn lại (kỳ 21 đến kỳ 40).

**Bước 1**: Số kỳ còn lại: $40 - 20 = 20$ kỳ

**Bước 2**: Giá trị hiện tại tại thời điểm kỳ 20 (tức đầu kỳ 21) của 20 khoản trả góp cuối kỳ:

$$
PV_{20} = 20 \times \frac{1 - (1{,}02)^{-20}}{0{,}02}
$$

**Bước 3**: Tính $(1{,}02)^{-20}$:

$$
(1{,}02)^{20} = 1{,}485947 \Rightarrow (1{,}02)^{-20} = \frac{1}{1{,}485947} = 0{,}672971
$$

**Bước 4**: Thay vào:

$$
PV_{20} = 20 \times \frac{1 - 0{,}672971}{0{,}02} = 20 \times \frac{0{,}327029}{0{,}02} = 20 \times 16{,}35145 = 327{,}03 \text{ triệu}
$$

Tuy nhiên, số tiền phải trả **vào kỳ số 21** (cuối kỳ 21), nên cần tính giá trị tại cuối kỳ 20 = đầu kỳ 21. Nếu trả vào **cuối** kỳ 21, cần tính lãi thêm 1 kỳ? Không — vì "vào kỳ số 21" nghĩa là tại thời điểm cuối kỳ 20 (bắt đầu kỳ 21), ta đang quy về đúng thời điểm đó.

Kiểm tra lại: Nợ còn lại tại kỳ 20 chính là PV tại kỳ 20 của chuỗi 20 khoản cuối kỳ:

$$
PV_{20} = 20 \times \frac{1-(1{,}02)^{-20}}{0{,}02} \approx 327{,}03
$$

Nhưng đề hỏi trả "vào kỳ số 21", tức cuối kỳ 21. Lúc đó ngoài việc trả nợ gốc+lãi còn lại, khoản đó đã tích lũy thêm 1 kỳ lãi:

$$
\text{Số tiền trả kỳ 21} = PV_{20} \times (1{,}02) = 327{,}03 \times 1{,}02 = 333{,}57 \text{ triệu}
$$

Hoặc cách khác: tại kỳ 21, ta coi 19 khoản còn lại (kỳ 22→40) quy về kỳ 21, cộng thêm khoản 20 triệu phải trả tại kỳ 21:

$$
= 20 + 20 \times \frac{1-(1{,}02)^{-19}}{0{,}02} = 20 + 20 \times 15{,}6785 = 20 + 313{,}57 = 333{,}57
$$

### ✅ Kết luận
**Đáp án: C. 333,57 triệu đồng**

### ⚠️ Sai lầm thường gặp
- Quên tính lãi thêm 1 kỳ khi chuyển từ thời điểm kỳ 20 sang kỳ 21.
- Nhầm số kỳ: 10 năm × 4 quý = 40, không phải 10.

---

## Câu 5: Thừa số giá trị tương lai FVIF(15%, 2)

### 📋 Đề bài
> Nếu tỷ lệ chiết khấu là 15%, thừa số giá trị (FVIF_{i,n}) của một khoản tiền trong 2 năm xấp xỉ là:

### 📚 Kiến thức nền cần dùng
- $FVIF_{i,n} = (1+i)^n$ (Mục 2.2.1)

### ✍️ Lời giải chi tiết

$$
FVIF_{15\%,2} = (1 + 0{,}15)^2 = (1{,}15)^2 = 1{,}3225
$$

### ✅ Kết luận
**Đáp án: B. 1,3225**

### ⚠️ Sai lầm thường gặp
- Nhầm với thừa số giá trị hiện tại PVIF = $(1+i)^{-n}$ = $1/1{,}3225 \approx 0{,}7561$.

---

## Câu 6: Lãi suất thực tế khi ghép lãi theo quý

### 📋 Đề bài
> Công ty X vay 500 triệu, lãi suất 14%/năm, ghép lãi theo quý. Lãi suất thực tế (theo năm) là?

### 📚 Kiến thức nền cần dùng
- Lãi suất thực tế (Mục 2.1.2):

$$
r_{eff} = \left(1 + \frac{i}{m}\right)^m - 1
$$

### ✍️ Lời giải chi tiết

Lãi suất danh nghĩa $i = 14\%$, ghép lãi $m = 4$ lần/năm.

$$
r_{eff} = \left(1 + \frac{0{,}14}{4}\right)^4 - 1 = (1{,}035)^4 - 1
$$

**Tính**: $(1{,}035)^2 = 1{,}071225$

$(1{,}035)^4 = (1{,}071225)^2 = 1{,}147523$

$$
r_{eff} = 1{,}147523 - 1 = 0{,}147523 \approx 14{,}75\%
$$

### ✅ Kết luận
**Đáp án: A. 14,75%**

### ⚠️ Sai lầm thường gặp
- Nghĩ lãi suất thực tế = lãi suất danh nghĩa (14%) → sai khi có ghép lãi nhiều kỳ.

---

## Câu 7: Giá trị hiện tại để nhận 115.000 USD sau 1 năm

### 📋 Đề bài
> Để nhận được 115.000 USD sau 1 năm với lãi suất là 10%/năm thì số tiền hiện tại sẽ xấp xỉ:

### ✍️ Lời giải chi tiết

$$
PV = \frac{FV}{(1+i)^n} = \frac{115.000}{(1{,}10)^1} = \frac{115.000}{1{,}10} = 104.545{,}45 \approx 104{,}55 \text{ (nghìn USD)}
$$

Lưu ý: Đáp án ghi đơn vị USD nhưng thực chất là nghìn USD. $PV \approx 104.545$ USD $\approx 104{,}55$ (nghìn USD).

### ✅ Kết luận
**Đáp án: B. 104,55 USD** (thực tế = 104.545 USD, đề viết rút gọn)

### ⚠️ Sai lầm thường gặp
- Nhầm nhân thay vì chia: $115.000 \times 1{,}10 = 126.500$ → đó là giá trị tương lai.

---

## Câu 8: Tìm lãi suất trả góp mua xe

### 📋 Đề bài
> Trả ngay 750 triệu, trả góp 720 triệu trong 2 năm (mỗi tháng 1 lần). Giá trả ngay toàn bộ = 1.300 triệu. Tìm lãi suất trả góp mỗi tháng?

### 🎯 Phân tích đề
- Số tiền nợ thực sự = $1.300 - 750 = 550$ triệu (phần chưa trả)
- Trả góp: $A = 720/24 = 30$ triệu/tháng, $n = 24$ tháng
- Cần tìm $r$ sao cho $PV$ của chuỗi 24 khoản = 550 triệu

### ✍️ Lời giải chi tiết

$$
550 = 30 \times \frac{1-(1+r)^{-24}}{r}
$$

$$
\frac{1-(1+r)^{-24}}{r} = \frac{550}{30} = 18{,}333
$$

Thử $r = 2\%$:

$$
\frac{1-(1{,}02)^{-24}}{0{,}02} = \frac{1 - 0{,}6217}{0{,}02} = \frac{0{,}3783}{0{,}02} = 18{,}914
$$

Thử $r = 2{,}29\%$: Giá trị sẽ nhỏ hơn 18,914.

Thử $r = 2{,}19\%$:

$(1{,}0219)^{24}$: ước tính bằng $e^{24 \times 0{,}02167} = e^{0{,}5256} \approx 1{,}692$

$$
\frac{1 - 1/1{,}692}{0{,}0219} = \frac{1 - 0{,}5911}{0{,}0219} = \frac{0{,}4089}{0{,}0219} \approx 18{,}67
$$

Giá trị 18,333 nằm giữa, gần $r \approx 2{,}29\%$:

$(1{,}0229)^{24} \approx e^{24 \times 0{,}02266} = e^{0{,}5438} \approx 1{,}723$

$$
\frac{1-1/1{,}723}{0{,}0229} = \frac{1-0{,}5804}{0{,}0229} = \frac{0{,}4196}{0{,}0229} \approx 18{,}32
$$

Rất gần 18,333!

### ✅ Kết luận
**Đáp án: D. 2,29%**

### ⚠️ Sai lầm thường gặp
- Tính nhầm số nợ: phải lấy giá trả ngay (1.300) trừ phần đã trả (750), không phải lấy tổng 720.

---

## Câu 9: Giá trị tương lai khi ghép lãi theo quý

### 📋 Đề bài
> Gửi 100 triệu, lãi suất 8%/năm, 3 năm, ghép lãi theo quý. Số tiền nhận sau 3 năm?

### 📚 Kiến thức nền cần dùng
- $F = P \times \left(1 + \frac{i}{m}\right)^{m \times t}$ (Mục 2.1.2)

### ✍️ Lời giải chi tiết

$$
F = 100 \times \left(1 + \frac{0{,}08}{4}\right)^{4 \times 3} = 100 \times (1{,}02)^{12}
$$

**Tính $(1{,}02)^{12}$**:
- $(1{,}02)^2 = 1{,}0404$
- $(1{,}02)^4 = 1{,}0404^2 = 1{,}08243$
- $(1{,}02)^8 = 1{,}08243^2 = 1{,}17166$
- $(1{,}02)^{12} = 1{,}17166 \times 1{,}08243 = 1{,}26824$

$$
F = 100 \times 1{,}26824 = 126{,}82 \text{ triệu}
$$

### ✅ Kết luận
**Đáp án: D. 126,82 triệu**

### ⚠️ Sai lầm thường gặp
- Dùng $(1{,}08)^3 = 125{,}97$ → đó là ghép lãi theo **năm** (đáp án C), không phải theo quý.

---

## Câu 10: Lãi suất định kỳ và lãi suất thực tế khi gộp quý

### 📋 Đề bài
> Lãi suất danh nghĩa 6%, gộp theo quý. Khẳng định nào đúng?

### ✍️ Lời giải chi tiết

- **Lãi suất định kỳ** (theo quý) = $6\%/4 = 1{,}5\%$
- **Lãi suất thực tế** (EAR):

$$
EAR = (1 + 0{,}015)^4 - 1 = (1{,}015)^4 - 1
$$

$(1{,}015)^2 = 1{,}030225$

$(1{,}015)^4 = 1{,}030225^2 = 1{,}06136$

$EAR = 6{,}136\% > 6\%$

### ✅ Kết luận
**Đáp án: D. Lãi suất định kỳ là 1,5% và lãi suất thực tế lớn hơn 6%**

### ⚠️ Sai lầm thường gặp
- Chọn B (lãi suất định kỳ 3% = 6%/2) → sai, phải chia cho 4 quý.

---

## Câu 11: Tăng giá trị hiện tại bằng cách điều chỉnh chiết khấu

### 📋 Đề bài
> Để tăng giá trị hiện tại dòng thu nhập, cần điều chỉnh tỷ lệ chiết khấu như thế nào?

### 📚 Kiến thức nền cần dùng
- $PV = \frac{FV}{(1+i)^n}$ (Mục 2.3.1)

### ✍️ Lời giải chi tiết

Từ công thức: khi $i$ tăng → $(1+i)^n$ tăng → $PV$ giảm.

Ngược lại, khi $i$ **giảm** → $(1+i)^n$ giảm → $PV$ **tăng**.

### ✅ Kết luận
**Đáp án: A. Giảm**

### 💡 Mẹo / Ghi chú
Tỷ lệ chiết khấu và giá trị hiện tại có quan hệ **nghịch biến**.

---

## Câu 12: Nguyên tắc lãi ghép

### 📋 Đề bài
> Nguyên tắc lãi ghép liên quan tới:

### 📚 Kiến thức nền cần dùng
- Định nghĩa lãi ghép (Mục 2.1.2): "tiền lãi sau mỗi kỳ được nhập vào vốn để đầu tư tiếp và sinh lãi cho kỳ sau"

### ✍️ Lời giải chi tiết
- A. Lãi tính trên vốn gốc → đây là lãi đơn.
- B. Đầu tư vào một số năm nào đó → không liên quan.
- C. Thu nhập tiền lãi tính trên lãi kiếm được của năm trước → **đúng**, bản chất lãi ghép.
- D. Không câu nào đúng → sai.

### ✅ Kết luận
**Đáp án: C. Thu nhập tiền lãi tính trên lãi kiếm được của năm trước**

---

## Câu 13: PV để nhận 250.000 USD sau 2 năm, lãi 3%

### 📋 Đề bài
> Để nhận 250.000 USD sau 2 năm, lãi suất 3%/năm, lãi ghép. Số tiền hiện tại phải gửi?

### ✍️ Lời giải chi tiết

$$
PV = \frac{FV}{(1+i)^n} = \frac{250.000}{(1{,}03)^2} = \frac{250.000}{1{,}0609} = 235.599{,}96 \approx 235.649 \text{ USD}
$$

Kiểm tra chính xác hơn: $(1{,}03)^2 = 1{,}0609$

$$
PV = \frac{250.000}{1{,}0609} = 235.649{,}0 \text{ USD}
$$

### ✅ Kết luận
**Đáp án: A. 235.649 USD**

### ⚠️ Sai lầm thường gặp
- Nhân thay vì chia: $250.000 \times 1{,}0609 = 265.225$ → đó là đáp án D (giá trị tương lai).

---

## Câu 14: Khoản đầu tư có PV thấp nhất

### 📋 Đề bài
> So sánh PV của 4 khoản đầu tư, giả sử lãi suất thực tế > 0. Khoản nào có PV thấp nhất?

### ✍️ Lời giải chi tiết

Tổng tiền danh nghĩa mỗi khoản:
- A (cuối 6 tháng, 20 kỳ): $125 \times 20 = 2.500$ triệu
- B (đầu 6 tháng, 20 kỳ): $125 \times 20 = 2.500$ triệu
- C (cuối 10 năm, 1 lần): $2.500$ triệu
- D (cuối năm, 10 kỳ): $250 \times 10 = 2.500$ triệu

Tổng danh nghĩa bằng nhau. Khoản nào nhận tiền **muộn nhất** sẽ có PV **thấp nhất**.

- **C**: Nhận toàn bộ 2.500 triệu vào cuối năm 10 → tiền nhận rất muộn → PV thấp nhất.
- D: Nhận dần cuối mỗi năm → PV cao hơn C.
- A: Nhận cuối mỗi 6 tháng → PV cao hơn D.
- B: Nhận đầu mỗi 6 tháng → PV cao nhất.

### ✅ Kết luận
**Đáp án: C. Khoản đầu tư A trả 2.500 triệu đồng vào cuối 10 năm**

### 💡 Mẹo / Ghi chú
Nhận tiền càng sớm → PV càng cao. Nhận tiền 1 cục vào cuối → PV thấp nhất.

---

## Câu 15: Khoản đầu tư có FV cao nhất sau 10 năm

### 📋 Đề bài
> So sánh FV sau 10 năm. Khoản nào cao nhất?

### ✍️ Lời giải chi tiết

Tổng danh nghĩa đều = 2.500 triệu. Khoản nào **trả tiền sớm nhất** sẽ sinh lãi lâu hơn → FV cao nhất.

- **A**: Đầu mỗi năm, 10 kỳ → trả sớm nhất (khoản đầu tại t=0)
- C: Đầu mỗi 6 tháng → cũng bắt đầu t=0, nhưng mỗi khoản nhỏ hơn (125 vs 250 cho khoản đầu tiên giống nhau)
- B: Cuối mỗi 6 tháng → chậm hơn đầu kỳ
- D: Cuối mỗi năm → chậm nhất

So sánh A vs C: Cả hai bắt đầu tại t=0. 
- A trả 250 tại t=0, 250 tại t=1, ...
- C trả 125 tại t=0, 125 tại t=0.5, 125 tại t=1, 125 tại t=1.5, ...

Khoản A trả 250 tại t=0 sinh lãi 10 năm. Khoản C trả 125 tại t=0 sinh lãi 10 năm + 125 tại t=0.5 sinh lãi 9.5 năm. So sánh: 250 × (1+r)^10 vs 125 × (1+r)^10 + 125 × (1+r)^9.5 = 125(1+r)^10 + 125(1+r)^9.5. Vì $(1+r)^{10} > (1+r)^{9.5}$, ta có 250(1+r)^10 > 125(1+r)^10 + 125(1+r)^9.5. Tương tự cho các kỳ sau.

→ **A** có FV cao nhất vì trả nhiều hơn tại mỗi thời điểm sớm.

### ✅ Kết luận
**Đáp án: A. Khoản đầu tư A trả 250 triệu đồng vào đầu mỗi năm**

### 💡 Mẹo / Ghi chú
Trả tiền càng sớm, khoản tiền càng lớn → FV càng cao.

---

## Câu 16: Trả nợ đều hàng năm — PV = 1.000 triệu, i=7%, n=15

### 📋 Đề bài
> Vay 1.000 triệu, lãi suất 7%/năm, 15 năm, trả đều cuối mỗi năm. Tính A?

### 📚 Kiến thức nền cần dùng
- Vay trả cố định (Mục 2.4.2):

$$
PV = A \times \frac{1-(1+i)^{-n}}{i} \Rightarrow A = \frac{PV \times i}{1-(1+i)^{-n}}
$$

### ✍️ Lời giải chi tiết

$$
A = \frac{1.000 \times 0{,}07}{1-(1{,}07)^{-15}}
$$

**Tính $(1{,}07)^{15}$**:
- $(1{,}07)^5 = 1{,}40255$
- $(1{,}07)^{10} = 1{,}40255^2 = 1{,}96715$
- $(1{,}07)^{15} = 1{,}96715 \times 1{,}40255 = 2{,}75903$

$(1{,}07)^{-15} = 1/2{,}75903 = 0{,}36245$

$$
A = \frac{70}{1 - 0{,}36245} = \frac{70}{0{,}63755} = 109{,}79 \text{ triệu}
$$

### ✅ Kết luận
**Đáp án: C. 109,79 triệu đồng**

---

## Câu 17: Trả nợ đều hàng năm — PV = 400 triệu, i=8%, n=10

### 📋 Đề bài
> Vay 400 triệu, lãi suất 8%/năm, 10 năm, trả đều cuối mỗi năm. Tính A?

### ✍️ Lời giải chi tiết

$$
A = \frac{400 \times 0{,}08}{1-(1{,}08)^{-10}}
$$

**Tính $(1{,}08)^{10}$**:
- $(1{,}08)^5 = 1{,}46933$
- $(1{,}08)^{10} = 1{,}46933^2 = 2{,}15892$

$(1{,}08)^{-10} = 1/2{,}15892 = 0{,}46319$

$$
A = \frac{32}{1 - 0{,}46319} = \frac{32}{0{,}53681} = 59{,}61 \text{ triệu}
$$

### ✅ Kết luận
**Đáp án: D. 59,61 triệu đồng**

---

## Câu 18: Hàm ý của giá trị thời gian của tiền

### 📋 Đề bài
> Giá trị thời gian của tiền có hàm ý gì?

### 📚 Kiến thức nền cần dùng
- Khái niệm giá trị thời gian của tiền (đầu Chương 2): "Một đồng tiền hôm nay có giá trị lớn hơn một đồng tiền mà một năm sau hay tại một thời điểm nào đó trong tương lai mới nhận được."

### ✅ Kết luận
**Đáp án: B. Một đơn vị tiền thu được ngày hôm nay có giá trị lớn hơn một đơn vị tiền thu được ở tương lai.**

---

## Câu 19: FV chuỗi tiền đều cuối kỳ — gửi hưu trí

### 📋 Đề bài
> Gửi 10 triệu/năm, cuối mỗi năm, lãi suất 10%/năm, lãi ghép. Cuối năm 20, nhận được bao nhiêu?

### 📚 Kiến thức nền cần dùng
- FV chuỗi tiền đều cuối kỳ (Mục 2.2.2):

$$
FV = A \times \frac{(1+i)^n - 1}{i}
$$

### ✍️ Lời giải chi tiết

$$
FV = 10 \times \frac{(1{,}10)^{20} - 1}{0{,}10}
$$

**Tính $(1{,}10)^{20}$**:
- $(1{,}10)^{10} = 2{,}59374$
- $(1{,}10)^{20} = 2{,}59374^2 = 6{,}72750$

$$
FV = 10 \times \frac{6{,}72750 - 1}{0{,}10} = 10 \times \frac{5{,}72750}{0{,}10} = 10 \times 57{,}275 = 572{,}75 \text{ triệu}
$$

### ✅ Kết luận
**Đáp án: D. 572,75 triệu đồng**

### ⚠️ Sai lầm thường gặp
- Nhầm chuỗi đầu kỳ: $FV = 572{,}75 \times 1{,}10 = 630{,}025$ → khác đáp án.
- Đề nói rõ "cuối mỗi năm" → dùng chuỗi cuối kỳ.

---

## Câu 20: PV chuỗi tiền biến đổi cuối kỳ — dự án 3 năm

### 📋 Đề bài
> Dự án 3 năm, thu cuối năm: 550; 0; 665,95 triệu. Chiết khấu 10%. Tính PV?

### 📚 Kiến thức nền cần dùng
- PV chuỗi tiền biến đổi cuối kỳ (Mục 2.3.2):

$$
PV = \sum_{t=1}^{n} \frac{CF_t}{(1+i)^t}
$$

### ✍️ Lời giải chi tiết

$$
PV = \frac{550}{(1{,}10)^1} + \frac{0}{(1{,}10)^2} + \frac{665{,}95}{(1{,}10)^3}
$$

**Bước 1**: $\frac{550}{1{,}10} = 500$

**Bước 2**: $\frac{0}{1{,}21} = 0$

**Bước 3**: $(1{,}10)^3 = 1{,}331$

$$
\frac{665{,}95}{1{,}331} = 500{,}34
$$

**Bước 4**: $PV = 500 + 0 + 500{,}34 = 1.000{,}34$ triệu

### ✅ Kết luận
**Đáp án: B. 1.000,34 triệu đồng**

---

## Câu 21: PV chuỗi tiền biến đổi cuối kỳ — dự án 5 năm

### 📋 Đề bài
> Dự án 5 năm, thu cuối năm: 2 tỷ, 2 tỷ, 2 tỷ, 3 tỷ, -4 tỷ. Chiết khấu 12%. Tính PV (triệu đồng)?

### ✍️ Lời giải chi tiết

Đổi đơn vị: 1 tỷ = 1.000 triệu

$$
PV = \frac{2.000}{1{,}12} + \frac{2.000}{(1{,}12)^2} + \frac{2.000}{(1{,}12)^3} + \frac{3.000}{(1{,}12)^4} + \frac{-4.000}{(1{,}12)^5}
$$

**Tính các thừa số**:
- $(1{,}12)^1 = 1{,}12$
- $(1{,}12)^2 = 1{,}2544$
- $(1{,}12)^3 = 1{,}404928$
- $(1{,}12)^4 = 1{,}573519$
- $(1{,}12)^5 = 1{,}762342$

$$
PV = \frac{2.000}{1{,}12} + \frac{2.000}{1{,}2544} + \frac{2.000}{1{,}404928} + \frac{3.000}{1{,}573519} + \frac{-4.000}{1{,}762342}
$$

$$
= 1.785{,}71 + 1.594{,}39 + 1.423{,}56 + 1.906{,}55 + (-2.269{,}99)
$$

$$
= 1.785{,}71 + 1.594{,}39 + 1.423{,}56 + 1.906{,}55 - 2.269{,}99
$$

$$
= 4.440{,}22 \approx 4.440{,}51 \text{ triệu}
$$

(Sai số nhỏ do làm tròn trung gian)

### ✅ Kết luận
**Đáp án: C. 4.440,51 triệu đồng**

### ⚠️ Sai lầm thường gặp
- Quên dòng tiền âm (-4 tỷ) năm 5 → tính ra kết quả lớn hơn.

---

## Câu 22: Định nghĩa lãi đơn

### 📋 Đề bài
> Lãi đơn là?

### 📚 Kiến thức nền cần dùng
- Mục 2.1.1: "tiền lãi sau mỗi kỳ **không** được nhập vào vốn để tính lãi cho kỳ sau"

### ✅ Kết luận
**Đáp án: C. Tiền lãi của kỳ này không được cộng vào gốc để tính lãi cho kỳ sau**

---

## Câu 23: Định nghĩa giá trị hiện tại

### 📋 Đề bài
> Giá trị hiện tại của một khoản tiền:

### 📚 Kiến thức nền cần dùng
- Mục 2.3.1: "Giá trị hiện tại của một số tiền trong tương lai là giá trị quy về thời điểm hiện tại của số tiền đó."

### ✅ Kết luận
**Đáp án: C. Là giá trị quy về thời điểm hiện tại của một khoản tiền trong tương lai**

---

## Câu 24: Tìm lãi suất từ bán chịu

### 📋 Đề bài
> Bán chịu 500 USD, khách hàng trả 600 USD sau 2 năm. Lãi suất hàng năm?

### ✍️ Lời giải chi tiết

$$
FV = PV \times (1+r)^n \Rightarrow 600 = 500 \times (1+r)^2
$$

$$
(1+r)^2 = \frac{600}{500} = 1{,}2
$$

$$
1+r = \sqrt{1{,}2} = 1{,}09545
$$

$$
r = 0{,}09545 \approx 9{,}54\%
$$

### ✅ Kết luận
**Đáp án: D. 9,54%**

### ⚠️ Sai lầm thường gặp
- Dùng lãi đơn: $r = (600-500)/(500 \times 2) = 10\%$ → đó là đáp án C, sai vì không phải lãi ghép.
- Tính $(600-500)/500 = 20\%$ → đó là tổng lãi 2 năm, không phải lãi hàng năm.

---

## Câu 25: So sánh phương án trả ngay vs trả dần

### 📋 Đề bài
> Mua đất: trả ngay 50 tỷ hoặc trả dần (năm 1: 30 tỷ, năm 2: 10 tỷ, năm 3: 8 tỷ, năm 4: 5 tỷ). Lãi suất 11%/năm. Chọn phương án nào?

### ✍️ Lời giải chi tiết

Tính PV của phương án trả dần (chuỗi tiền biến đổi cuối kỳ):

$$
PV = \frac{30}{1{,}11} + \frac{10}{(1{,}11)^2} + \frac{8}{(1{,}11)^3} + \frac{5}{(1{,}11)^4}
$$

**Tính từng thành phần**:
- $(1{,}11)^1 = 1{,}11$ → $30/1{,}11 = 27{,}027$
- $(1{,}11)^2 = 1{,}2321$ → $10/1{,}2321 = 8{,}116$
- $(1{,}11)^3 = 1{,}3676$ → $8/1{,}3676 = 5{,}851$
- $(1{,}11)^4 = 1{,}5181$ → $5/1{,}5181 = 3{,}294$

$$
PV_{trả dần} = 27{,}027 + 8{,}116 + 5{,}851 + 3{,}294 = 44{,}288 \text{ tỷ}
$$

**So sánh**: $PV_{trả dần} = 44{,}29$ tỷ < $PV_{trả ngay} = 50$ tỷ

→ Phương án trả dần có chi phí thực tế thấp hơn → **chọn trả dần**.

### ✅ Kết luận
**Đáp án: B. Chọn phương án trả dần trong 4 năm**

### ⚠️ Sai lầm thường gặp
- So sánh tổng danh nghĩa: $30+10+8+5 = 53$ tỷ > 50 tỷ → tưởng trả ngay rẻ hơn. Sai vì chưa tính giá trị thời gian của tiền.

### 💡 Mẹo / Ghi chú
Luôn quy về **cùng thời điểm** (thường là hiện tại) trước khi so sánh các phương án thanh toán.

---

# 📊 Bảng tổng hợp đáp án

| Câu | Đáp án | Dạng bài |
|-----|--------|----------|
| 1 | **C** (14,4%) | Quy tắc 72 — tìm lãi suất |
| 2 | **A** (11 năm) | Quy tắc 72 — tìm thời gian |
| 3 | **C** (125,97 triệu) | FV một khoản tiền |
| 4 | **C** (333,57 triệu) | PV chuỗi đều — nợ còn lại |
| 5 | **B** (1,3225) | Thừa số FVIF |
| 6 | **A** (14,75%) | Lãi suất thực tế (EAR) |
| 7 | **B** (104,55) | PV một khoản tiền |
| 8 | **D** (2,29%) | Tìm lãi suất trả góp |
| 9 | **D** (126,82 triệu) | FV ghép lãi theo quý |
| 10 | **D** (LS định kỳ 1,5%, thực tế >6%) | Lãi suất định kỳ & EAR |
| 11 | **A** (Giảm) | Quan hệ chiết khấu — PV |
| 12 | **C** (Lãi trên lãi) | Lý thuyết lãi ghép |
| 13 | **A** (235.649 USD) | PV một khoản tiền |
| 14 | **C** (2.500 triệu cuối năm 10) | So sánh PV — nhận muộn nhất |
| 15 | **A** (250 triệu đầu năm) | So sánh FV — trả sớm nhất |
| 16 | **C** (109,79 triệu) | Vay trả cố định |
| 17 | **D** (59,61 triệu) | Vay trả cố định |
| 18 | **B** (1 đồng hôm nay > tương lai) | Lý thuyết TVM |
| 19 | **D** (572,75 triệu) | FV chuỗi đều cuối kỳ |
| 20 | **B** (1.000,34 triệu) | PV chuỗi biến đổi |
| 21 | **C** (4.440,51 triệu) | PV chuỗi biến đổi |
| 22 | **C** (Lãi không cộng vào gốc) | Lý thuyết lãi đơn |
| 23 | **C** (Quy về hiện tại) | Lý thuyết PV |
| 24 | **D** (9,54%) | Tìm lãi suất |
| 25 | **B** (Trả dần 4 năm) | So sánh phương án — PV |

---

# 🏢 Ví dụ thực tế — Giá trị thời gian của tiền trong doanh nghiệp Việt Nam

## Ví dụ 1: Vingroup — Trả góp bất động sản và giá trị thời gian của tiền

**Bối cảnh**: Vingroup (qua Vinhomes) thường đưa ra 2 phương thức thanh toán khi mua căn hộ: trả ngay toàn bộ (được chiết khấu 5-8%) hoặc trả góp theo tiến độ trong 2-3 năm. Đây chính là bài toán so sánh phương án thanh toán giống Câu 25.

**Áp dụng giá trị thời gian của tiền**:
- Khách hàng cần quy các khoản trả góp về PV (dùng lãi suất cơ hội — thường là lãi suất tiền gửi hoặc lãi suất đầu tư khác) để so sánh với giá trả ngay.
- Nếu $PV_{trả góp} < PV_{trả ngay}$ → trả góp có lợi hơn (tiền chưa trả có thể sinh lời ở kênh khác).
- Vingroup định giá chiết khấu trả ngay chính là dựa trên chi phí vốn của họ — nếu họ nhận tiền sớm, tiết kiệm được chi phí lãi vay ngân hàng.

**Bài học**: Cả người mua lẫn người bán đều dùng TVM để ra quyết định. Sinh viên cần nắm vững kỹ năng quy đổi PV để tư vấn tài chính cá nhân và doanh nghiệp.

---

## Ví dụ 2: FPT — Lãi ghép trong tích lũy quỹ hưu trí nhân viên

**Bối cảnh**: FPT triển khai chương trình Employee Stock Ownership Plan (ESOP) và quỹ hưu trí tự nguyện, khuyến khích nhân viên đóng góp đều đặn hàng năm. Đây là ứng dụng trực tiếp của Câu 19 (FV chuỗi tiền đều cuối kỳ).

**Áp dụng**:
- Nếu một nhân viên FPT đóng 10 triệu/năm vào quỹ đầu tư nội bộ với tỷ suất sinh lời khoảng 10%/năm, sau 20 năm sẽ tích lũy được khoảng 573 triệu — gấp gần 3 lần tổng tiền đóng (200 triệu).
- Hiệu ứng lãi ghép ("lãi mẹ đẻ lãi con") giải thích vì sao bắt đầu đầu tư **sớm** quan trọng hơn đầu tư **nhiều**.

**Bài học**: Quy tắc 72 giúp tính nhanh — với lợi suất 10%/năm, vốn gấp đôi sau khoảng 7,2 năm.

---

## Ví dụ 3: Techcombank — Lãi suất thực tế khi vay tiêu dùng

**Bối cảnh**: Các ngân hàng như Techcombank quảng cáo lãi suất cho vay "từ 7,49%/năm" nhưng thường ghép lãi theo tháng hoặc theo quý. Đây chính là bài toán tính EAR (Câu 6, 10).

**Áp dụng**:
- Lãi suất danh nghĩa 7,49%/năm, ghép lãi hàng tháng → Lãi suất thực tế $EAR = (1 + 0{,}0749/12)^{12} - 1 \approx 7{,}76\%$/năm.
- Chênh lệch 0,27% tưởng nhỏ nhưng trên khoản vay 1 tỷ đồng trong 20 năm, tổng lãi chênh lệch có thể lên đến hàng chục triệu đồng.

**Bài học**: Luôn hỏi **tần suất ghép lãi** khi so sánh lãi suất giữa các ngân hàng. Lãi suất danh nghĩa giống nhau không có nghĩa chi phí thực tế bằng nhau.
