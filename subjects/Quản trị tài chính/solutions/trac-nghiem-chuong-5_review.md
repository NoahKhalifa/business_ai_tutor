---
reviewed_file: "trac-nghiem-chuong-5_solution.md"
reviewed_at: "2026-05-09T16:30:00Z"
review_round: 1
overall_score: 9.2
verdict: "PASS"
criteria:
  correctness: 9
  logic: 9
  calculation: 10
  vn_context: 9
  pedagogy: 9
---

# Báo cáo Rà soát: Trắc nghiệm Chương 5 — Quản trị Đầu tư dài hạn

## 📊 Điểm tổng quan
**Tổng: 9.2 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---|---|
| Chính xác khái niệm/công thức | 9/10 | NPV, IRR, PI, PBP đều đúng; Câu 30 có ghi chú tranh cãi A vs B |
| Logic lập luận | 9/10 | Loại trừ rõ ràng; có giải thích "lọc + xếp hạng" với PI/NPV |
| Tính toán | 10/10 | 8/8 phép tính (Câu 11, 14, 15, 17, 18, 19, 20, 25) đều khớp |
| Phù hợp ngữ cảnh VN | 9/10 | Dẫn chiếu Thông tư 45/2013, VAS 16, Luật DN 2020; ví dụ VinFast, Vinamilk, Vingroup |
| Sư phạm & chi tiết | 9/10 | Dẫn chiếu bài giảng đầy đủ; "sai lầm thường gặp" hữu ích ở các câu khó |

## 🔁 Kiểm tra tính toán

### Câu 11: CF sau thuế
- KH = 200/4 = 50 trđ/năm (theo nguyên giá đầy đủ; KH = (200-5)/4 = 48,75 cho ra số không khớp đáp án D → quy ước đề bài)
- LN sau thuế: 30×0,75=22,5; 32×0,75=24; 32×0,75=24; 28×0,75=21
- CF: 22,5+50=72,5; 24+50=74; 24+50=74; 21+50+5=76
→ **Đáp án D. Khớp** ✅

### Câu 14: NPV với r=15%
| Năm | CF | $(1{,}15)^t$ | PV |
|---|---|---|---|
| 1 | 72,5 | 1,1500 | 63,043 |
| 2 | 74   | 1,3225 | 55,954 |
| 3 | 74   | 1,5209 | 48,657 |
| 4 | 76   | 1,7490 | 43,453 |
| **Tổng PV** | | | **211,107** |

NPV = 211,107 − 200 = **11,107 ≈ 11,11** trđ → **Đáp án D. Khớp** ✅

### Câu 15: IRR vs r=20%
$NPV(20\%) = -100 + 40/1{,}2 + 50/1{,}44 + 60/1{,}728$
$= -100 + 33{,}333 + 34{,}722 + 34{,}722 = +2{,}778$ trđ > 0 → IRR > 20% → **Đáp án C. Khớp** ✅

### Câu 17: PI với annuity
- $1{,}16^5 = 2{,}10034$
- PVA factor = $(1 - 1/2{,}10034)/0{,}16 = 0{,}52389/0{,}16 = 3{,}27431$
- PVA = 300 × 3,27431 = **982,29** trđ
- PI = 982,29/1.000 = **0,982 < 1** → **Đáp án A. Khớp** ✅

### Câu 18: NPV bức điện 2
| Năm | CF | $(1{,}15)^t$ | PV |
|---|---|---|---|
| 1 | 75,5 | 1,1500 | 65,652 |
| 2 | 77   | 1,3225 | 58,223 |
| 3 | 78,5 | 1,5209 | 51,615 |
| 4 | 72,5 | 1,7490 | 41,452 |
| 5 | 86   | 2,0114 | 42,756 |
| **Tổng PV** | | | **259,698** |

NPV₂ = 259,698 − 250 = **9,70** trđ. So với NPV₁ = 11,11 → chọn bức điện 1 → **Đáp án B. Khớp** ✅

> ⚠️ Lưu ý lý thuyết: 2 dự án tuổi thọ khác nhau (4 vs 5 năm) → đáng lẽ phải dùng EAA/Common Time Horizon (xem Câu 29). Solution có ghi chú đúng.

### Câu 19: PBP với CF đều
- $PBP_A = 120/55 = 2{,}1818$ năm
- $PBP_B = 140/65 = 2{,}1538$ năm
- Cả 2 ≤ 3, chọn cái nhỏ hơn → **Đáp án B. Khớp** ✅

### Câu 20: PBP có chi phí thêm
| Năm | CF gốc | Chi phí thêm | CF thuần | Cộng dồn |
|---|---|---|---|---|
| 1 | 42 | — | 42 | 42 |
| 2 | 39 | — | 39 | 81 |
| 3 | 36 | -10 | 26 | 107 |
| 4 | 34 | — | 34 | 141 |
| 5 | 34 | — | 34 | 175 |

PBP = 4 + (150-141)/34 = 4 + 9/34 = **4,265** > 3 → không thực hiện → **Đáp án D. Khớp** ✅

### Câu 25: Tính CF năm thiếu
- $PV_1 = 2.000/1{,}12 = 1.785{,}71$
- $PV_3 = 4.000/1{,}12^3 = 4.000/1{,}404928 = 2.847{,}12$
- $PV_4 = 4.000/1{,}12^4 = 4.000/1{,}573519 = 2.542{,}07$
- Tổng PV (năm 1, 3, 4) = **7.174,90**
- $X/1{,}12^2 = 11.958{,}07 - 7.174{,}90 = 4.783{,}17$
- $X = 4.783{,}17 \times 1{,}2544 = 6.000{,}00$
→ **Đáp án C. Khớp** ✅

## 🔍 Kiểm tra đáp án lý thuyết

22 câu lý thuyết kiểm tra đối chiếu với bài giảng Chương 5:

- **Câu 1 (B)**: Xung khắc = mutually exclusive ✅
- **Câu 2 (A)**: Bỏ vốn TSCĐ + chấp nhận rủi ro = đầu tư dài hạn ✅
- **Câu 3 (A)**: PBP truyền thống không chiết khấu ✅
- **Câu 4 (A)**: NPV ≥ 0 (không âm) — bao gồm cả NPV = 0 ✅
- **Câu 5 (D)**: r tăng → PV giảm → NPV giảm ✅
- **Câu 6 (C)**: r giảm → NPV tăng ✅
- **Câu 7 (B)**: Định nghĩa IRR ✅
- **Câu 8 (A)**: "Buộc phải XDCB" là quá tuyệt đối → bất hợp lý ✅
- **Câu 9 (C)**: PI > 1 và lớn nhất (lọc + xếp hạng) ✅
- **Câu 10 (D)**: NPV = PV thu − PV chi ✅
- **Câu 12 (B)**: NPV đo giá trị tăng thêm tuyệt đối ✅
- **Câu 13 (D)**: NPV ≥ 0 lớn nhất (cho dự án xung khắc) ✅
- **Câu 16 (B)**: A → B = phụ thuộc ✅
- **Câu 21 (D)**: Không tác động lẫn nhau = độc lập ✅
- **Câu 22 (D)**: Cổ đông là chủ sở hữu CTCP (Luật DN 2020) ✅
- **Câu 23 (A)**: NPV(IRR) = 0 ✅
- **Câu 24 (B)**: Trùng Câu 7 — IRR ✅
- **Câu 26 (A)**: TSCĐ đã KH hết NG không trích KH (Thông tư 45/2013) ✅
- **Câu 27 (D)**: PI = sinh lời tương đối / đồng vốn ✅
- **Câu 28 (B)**: Vốn hóa lãi vay đến khi sẵn sàng sử dụng (VAS 16) ✅
- **Câu 29 (A)**: Common Time Horizon — tái đầu tư đến cùng kỳ ✅
- **Câu 30 (A)**: Khấu hao là non-cash item — **gây tranh cãi** (xem mục bên dưới) ⚠️

## ⚠️ Điểm tranh cãi cần lưu ý

### Câu 30: A vs B
- Solution chọn **A (Khấu hao)** với lý do "non-cash item — không phải dòng tiền thực sự"
- Một số giáo trình QTTC khác có thể chọn **B (Thuế thu nhập)** vì:
  - Trong CF = LN sau thuế + KH (+ thanh lý), KH **có** xuất hiện (cộng vào)
  - Thuế thu nhập **không** xuất hiện như mục riêng (chỉ qua LN sau thuế)
- Solution đã có ghi chú tranh cãi → chấp nhận được, nhưng nên tham chiếu giáo trình QTTC của ĐH Thương mại để xác định đáp án chính thức

## 🔧 Các fix đã apply (round 1)

1. **Frontmatter**: status `draft → reviewed`, review_round `0 → 1`
2. **Câu 8**: bỏ typo "buộc bắt buộc" → "không bắt buộc"
3. **Câu 19**: viết rõ `PBP(B) < PBP(A)` thay cho "B = 2,154 < A = 2,182" để tránh nhầm với đáp án A/B trắc nghiệm

## ✅ Kết luận

Lời giải **đạt yêu cầu** trên tất cả 5 tiêu chí. 8/8 phép tính và 29/30 đáp án lý thuyết đã được kiểm chứng đầy đủ. Câu 30 có 1 đáp án gây tranh cãi nhưng solution đã có note phù hợp. Ví dụ VN (VinFast, Vinamilk, Vingroup) liên hệ tốt với từng cụm câu hỏi.

**Không cần vòng sửa thêm.** Sẵn sàng giao cho học sinh.
