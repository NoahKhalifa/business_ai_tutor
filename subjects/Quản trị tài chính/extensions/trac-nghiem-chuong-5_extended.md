---
parent_solution: "solutions/trac-nghiem-chuong-5_solution.md"
created_at: "2026-05-09T00:00:00Z"
---

# Mở rộng & Luyện tập: Trắc nghiệm Chương 5 — Quản trị Đầu tư dài hạn

## 🎯 Bài tập tham khảo (tự luyện)

### Bài luyện 1 — Cơ bản (★)

**Đề**: Một dự án có vốn đầu tư ban đầu 500 triệu đồng, tạo dòng tiền thuần đều 150 triệu đồng/năm trong 5 năm. Chi phí sử dụng vốn là 12%/năm. Tính NPV và quyết định có nên thực hiện dự án không?

**Gợi ý**: Dùng công thức niên kim $PVA = A \times \dfrac{1-(1+r)^{-n}}{r}$ rồi trừ vốn đầu tư.

<details>
<summary>Đáp án rút gọn</summary>

$PVA = 150 \times \dfrac{1 - 1{,}12^{-5}}{0{,}12} = 150 \times 3{,}6048 = 540{,}72$ trđ

$NPV = 540{,}72 - 500 = +40{,}72$ trđ > 0 → **nên thực hiện** dự án.

(IRR ≈ 15,24% > 12% → cùng kết luận.)
</details>

---

### Bài luyện 2 — Trung bình (★★)

**Đề**: Công ty cân nhắc 2 dự án **xung khắc** sau (cùng tuổi thọ 5 năm, r = 10%/năm):
- **Dự án A**: vốn 100 trđ, CF đều 30 trđ/năm
- **Dự án B**: vốn 250 trđ, CF đều 70 trđ/năm

1. Tính NPV và PI của mỗi dự án.
2. Hai phương pháp NPV và PI cho kết quả xếp hạng giống hay khác nhau? Giải thích.
3. Chọn dự án nào? Phân tích trong 2 tình huống: (a) công ty không bị giới hạn vốn; (b) công ty chỉ có ngân sách tối đa 100 trđ.

**Gợi ý**: $PVIFA(10\%, 5) = 3{,}7908$; $PI = \sum PV(CF) / ICO$.

<details>
<summary>Đáp án rút gọn</summary>

| Dự án | Vốn | $\sum PV(CF)$ | NPV | PI |
|---|---|---|---|---|
| A | 100 | $30 \times 3{,}7908 = 113{,}72$ | **+13,72** | **1,137** |
| B | 250 | $70 \times 3{,}7908 = 265{,}36$ | **+15,36** | **1,061** |

**Mâu thuẫn xếp hạng**:
- Theo NPV: B > A (B có giá trị tăng thêm tuyệt đối lớn hơn 1,64 trđ).
- Theo PI: A > B (A sinh lời 13,7% trên mỗi đồng vốn, B chỉ 6,1%).

**Quyết định**:
- (a) Không giới hạn vốn → chọn **B** (NPV cao nhất, mục tiêu tối đa hóa giá trị tuyệt đối).
- (b) Ngân sách 100 trđ → chỉ làm được **A** (B yêu cầu 250 trđ vượt ngân sách); A vẫn cho NPV dương 13,72 trđ — chấp nhận được.

**Bài học**: Khi nguồn vốn dồi dào, NPV là tiêu chí ưu tiên. Khi vốn hạn chế (capital rationing), PI hữu ích để xếp hạng dự án theo "hiệu suất sinh lời/đồng vốn".
</details>

---

### Bài luyện 3 — Nâng cao (★★★)

**Đề**: Một công ty xây dựng VN (giả định "An Phát Constructions") có ngân sách đầu tư cho năm 2027 là **600 triệu đồng**. Phòng đầu tư đề xuất 4 dự án **độc lập**:

| Dự án | Mô tả | Vốn (trđ) | NPV (trđ) |
|---|---|---|---|
| A | Mua máy ép cọc mới | 200 | 80 |
| B | Mở chi nhánh tại Đà Nẵng | 300 | 100 |
| C | Đầu tư phần mềm BIM cho thiết kế | 250 | 90 |
| D | Cải tạo kho vật tư | 150 | 50 |

**Yêu cầu**:
1. Tính PI của từng dự án ($PI = 1 + NPV/Vốn$ vì NPV đã chiết khấu).
2. Nếu KHÔNG bị giới hạn vốn → chọn dự án nào? Tổng NPV bao nhiêu?
3. Với giới hạn vốn 600 trđ → xếp hạng theo PI, chọn tổ hợp dự án tối đa hóa **tổng NPV**. So sánh với cách chọn theo NPV đơn lẻ lớn nhất.
4. Biện luận về **chi phí cơ hội** của ngân sách bị bỏ sót (nếu có).

<details>
<summary>Đáp án rút gọn</summary>

**1. PI của từng dự án**:

| Dự án | Vốn | NPV | **PI** |
|---|---|---|---|
| A | 200 | 80 | **1,40** |
| C | 250 | 90 | **1,36** |
| B | 300 | 100 | **1,33** |
| D | 150 | 50 | **1,33** |

**2. Không giới hạn vốn**: chấp nhận tất cả 4 dự án (PI > 1) → tổng vốn 900 trđ, tổng NPV = **80+100+90+50 = 320 trđ**.

**3. Giới hạn 600 trđ — xét tất cả tổ hợp khả thi**:

| Tổ hợp | Tổng vốn | Tổng NPV |
|---|---|---|
| B+C | 550 | 190 |
| **A+C+D** | **600** | **220** ⭐ |
| A+B | 500 | 180 |
| A+C | 450 | 170 |
| B+D | 450 | 150 |
| C+D | 400 | 140 |
| A+D | 350 | 130 |

→ Tổ hợp tối ưu là **A + C + D** (tổng vốn 600 đúng ngân sách, tổng NPV cao nhất = **220 trđ**).

So sánh: nếu chọn theo "NPV đơn lẻ lớn nhất" sẽ chọn B (NPV=100) → còn dư 300 → chọn thêm A (NPV=80) → tổng NPV chỉ 180 trđ → **kém 40 trđ** so với cách dùng PI.

**4. Chi phí cơ hội**: Tổ hợp A+C+D đã dùng hết 600 → không còn vốn dư → không có cơ hội bị bỏ sót. Nếu vốn dư là 50 trđ thì việc không thực hiện được dự án D (cần 150) là một chi phí cơ hội = NPV bị bỏ qua = 50 trđ. Đây là lý do trong thực tế DN có thể tìm kiếm vốn vay bổ sung khi cận biên NPV/đồng vốn còn cao.

**Bài học**: Khi vốn hạn chế, ranking theo PI giúp chọn được tổ hợp tối ưu — KHÔNG phải lúc nào "dự án có NPV lớn nhất" cũng là lựa chọn tốt nhất khi xét toàn ngân sách.
</details>

---

## 📖 Đào sâu kiến thức

### Khái niệm liên quan

- **Equivalent Annual Annuity (EAA)** — *Niên kim tương đương*: Khi 2 dự án xung khắc có **tuổi thọ khác nhau**, không thể so NPV trực tiếp. EAA quy NPV về một dòng tiền đều/năm: $EAA = NPV / PVIFA(r, n)$. Chọn dự án có EAA lớn hơn.

- **Capital Rationing** — *Giới hạn vốn*: Khi tổng vốn yêu cầu > ngân sách, dùng PI để xếp hạng → chọn tổ hợp tối đa hóa tổng NPV trong giới hạn (như Bài luyện 3).

- **Real Options Analysis** — *Phân tích tùy chọn thực*: Mở rộng NPV truyền thống bằng cách định giá các "tùy chọn" trong dự án (vd: tùy chọn mở rộng, hoãn, từ bỏ). Phù hợp với dự án có nhiều bất định (vd: thăm dò dầu khí, R&D dược phẩm).

- **Sensitivity Analysis & Scenario Analysis** — *Phân tích độ nhạy & kịch bản*: NPV phụ thuộc nhiều biến (giá bán, sản lượng, chi phí, r). Phân tích độ nhạy cho biết NPV thay đổi bao nhiêu khi 1 biến thay đổi 1%; phân tích kịch bản xét NPV trong các kịch bản (lạc quan/cơ sở/bi quan).

### Mô hình nâng cao: NPV theo phương pháp APV

NPV truyền thống dùng WACC làm r. Phương pháp **Adjusted Present Value (APV)** tách bạch:

$$APV = NPV_{\text{dự án không vay}} + PV(\text{tiết kiệm thuế từ lãi vay})$$

Hữu ích khi cấu trúc vốn của dự án khác cấu trúc vốn chung của công ty (vd: dự án M&A có sử dụng đòn bẩy cao).

### Tranh luận học thuật

**NPV vs IRR — phương pháp nào chuẩn vàng?**
- *Quan điểm 1 (Brealey & Myers)*: NPV luôn đúng về lý thuyết; IRR có thể bị lỗi nhiều nghiệm (multiple IRR) khi dòng tiền đổi dấu nhiều lần, hoặc xếp hạng sai khi quy mô dự án khác nhau.
- *Quan điểm 2 (thực hành DN)*: IRR dễ truyền thông cho ban lãnh đạo (con số %, dễ so với lãi suất vay) → vẫn được ưa chuộng. Cách dung hòa: dùng cả hai, NPV làm tiêu chí cuối cùng.

---

## 🤔 Câu hỏi tư duy phản biện

1. **NPV và IRR mâu thuẫn xếp hạng** giữa 2 dự án xung khắc — bạn dùng phương pháp nào để ra quyết định cuối cùng? Giải thích bằng ví dụ.
2. **IRR có thể có nhiều nghiệm** (multiple IRR) khi nào? Trong trường hợp đó, NPV có còn đáng tin không? (Gợi ý: dòng tiền đổi dấu nhiều lần — vd dự án khai thác mỏ phải khôi phục môi trường cuối kỳ.)
3. **PBP (kỳ hoàn vốn) có còn ý nghĩa khi đã có NPV/IRR?** Vì sao nhiều DN VN — đặc biệt SME — vẫn dùng PBP làm tiêu chí chính khi ra quyết định? PBP có vai trò gì mà NPV không thay thế được?
4. **Đầu tư xanh / ESG**: nếu chỉ dùng NPV, các dự án ESG (giảm phát thải, năng lượng tái tạo) thường thua dự án truyền thống. Làm sao lồng ghép giá trị phi tài chính vào quyết định đầu tư dài hạn?
5. Trong bài Câu 18 (so sánh 2 bức điện chào hàng máy xay xát), việc dùng **NPV trực tiếp** có thực sự hợp lý khi 2 máy có tuổi thọ khác nhau (4 vs 5 năm)? Phương pháp nào chuẩn hơn? (Gợi ý: EAA hoặc Common Time Horizon.)

---

## 📚 Đọc thêm

- **Brealey, Myers & Allen** — *Principles of Corporate Finance* — Chương 5-6 (Capital Budgeting, NPV vs IRR, Project Analysis).
- **Ross, Westerfield & Jaffe** — *Corporate Finance* — Chương 6-7 (Investment Decision Rules, Making Capital Investment Decisions).
- **Giáo trình Quản trị Tài chính** — NXB Đại học Kinh tế Quốc dân — Chương 5 (Quyết định đầu tư dài hạn).
- **Damodaran** — *Investment Valuation* (chương về DCF cho định giá dự án và DN — mức nâng cao).
- **Case Harvard Business Review**: "Investment Detective" (NPV/IRR ranking) — case kinh điển dạy MBA.

---

## 🔗 Liên kết với các bài khác trong môn

| Mối liên kết | Chương |
|---|---|
| Chương 5 cần kiến thức từ | **Chương 2** (Giá trị thời gian của tiền — PV, FV, niên kim); **Chương 3** (Phân tích BCTC — ước lượng dòng tiền dự án từ doanh thu/chi phí); **Chương 4** (CCC, vốn lưu động — ước lượng nhu cầu vốn lưu động trong CF dự án) |
| Chương 5 là nền tảng cho | **Chương 6** (Tài trợ — chi phí sử dụng vốn WACC dùng làm r chiết khấu trong NPV); **Chương 7** (Phân phối lợi nhuận / Định giá DN — cùng dùng kỹ thuật DCF) |
