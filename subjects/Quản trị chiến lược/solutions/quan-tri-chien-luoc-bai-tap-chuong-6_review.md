---
reviewed_file: "quan-tri-chien-luoc-bai-tap-chuong-6_solution.md"
reviewed_at: "2026-05-09T22:45:00+07:00"
review_round: 1
overall_score: 9.2
verdict: "PASS"
criteria:
  correctness: 9.5
  logic: 9.0
  calculation: 9.0
  vn_context: 9.5
  pedagogy: 9.0
---

# Báo cáo Rà soát: Quản trị chiến lược — Trắc nghiệm Chương 6

> **Phương pháp review**: Reviewer tự re-derive từng đáp án từ Mục 6.1–6.6 của lecture summary trước, sau đó đối chiếu với solution. Không có bài nào reviewer phải đảo ngược lựa chọn của solver.

## 📊 Điểm tổng quan

**Tổng: 9.2 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---|---|
| Chính xác khái niệm/công thức | 9.5/10 | 21/21 đáp án khớp với re-derivation độc lập từ lecture |
| Logic lập luận | 9.0/10 | Lập luận chặt, có loại trừ đầy đủ; vài chỗ có thể súc tích hơn |
| Tính toán | 9.0/10 | Bài chỉ trắc nghiệm khái niệm, không có tính toán → N/A pass |
| Phù hợp ngữ cảnh VN | 9.5/10 | 4 ví dụ DN VN (Viettel, FPT, MWG, VinFast) cụ thể, không bịa số liệu |
| Sư phạm & chi tiết | 9.0/10 | Có dẫn chiếu lecture, có bẫy thi, có bảng tổng kết phân biệt giai đoạn |

---

## 🔍 Phát hiện chi tiết theo từng câu

### Tổng quan độ chính xác

| Câu | Đáp án solver | Đáp án reviewer (độc lập) | Khớp? | Mức tin cậy |
|---|:---:|:---:|:---:|---|
| 1 | C | C | ✓ | Cao — McKinsey 7S là kiến thức kinh điển |
| 2 | C | C | ✓ | Cao — định nghĩa văn hóa DN chuẩn |
| 3 | B | B | ✓ | Cao — lecture 6.4 confirm |
| 4 | A | A | ✓ | Trung bình-cao — lecture chỉ nói chung "tiếp cận hiệu quả"; A đúng theo giáo trình QTCL chuẩn |
| 5 | A | A | ✓ | Cao — A rõ ràng là mục tiêu, không phải thách thức |
| 6 | B | B | ✓ | **Trung bình — có khả năng OCR sai ở phương án C, xem chú ý dưới** |
| 7 | A | A | ✓ | Cao — phân biệt hoạch định vs thực thi rõ |
| 8 | B | B | ✓ | Cao — chính sách phải bằng văn bản là nguyên tắc chuẩn |
| 9 | B | B | ✓ | Cao — lecture 6.4 confirm "phức tạp" |
| 10 | D | D | ✓ | Cao |
| 11 | B | B | ✓ | Cao |
| 12 | C | C | ✓ | Cao |
| 13 | D | D | ✓ | Cao — lecture nói rõ "tập trung trách nhiệm" cho cấu trúc chức năng |
| 14 | B | B | ✓ | Cao |
| 15 | D | D | ✓ | Cao |
| 16 | C | C | ✓ | Cao |
| 17 | A | A | ✓ | Cao — đa dự án + đa địa lý → ma trận là lựa chọn chuẩn |
| 18 | C | C | ✓ | Cao |
| 19 | D | D | ✓ | Cao — A "tất cả đúng" sai vì B, C là điều kiện áp dụng, không phải "không hiệu quả" |
| 20 | B | B | ✓ | Trung bình-cao — quan sát chung về DN VN, hợp lý |
| 21 | B | B | ✓ | Cao |

**Tỷ lệ khớp: 21/21 = 100%**.

---

### ⚠️ Vấn đề phát hiện (cần lưu ý)

#### Câu 6 — **[LẬP LUẬN/THIẾU DẪN CHỨNG]** — mức độ: NHẸ

- **Mô tả**: Solver đã chọn đúng đáp án B ("các phương án còn lại đều đúng") và có lưu ý OCR ở phương án C. Tuy nhiên, đáp án phụ thuộc vào việc đọc đúng phương án C trong PDF gốc.
- **Đoạn có vấn đề**: Trong file đề và file solution, phương án C được ghi là "Văn hóa doanh nghiệp **phù hợp** với sự thay đổi do chiến lược mới."
- **Phân tích reviewer**: 
  - Nếu nguyên văn đúng là "phù hợp" → C không phải thách thức (vì đã phù hợp rồi) → đáp án có thể là A hoặc D thay vì B.
  - Nếu OCR sót chữ "không" → "VH KHÔNG phù hợp với thay đổi" mới là thách thức → đáp án B đúng.
  - Solver đã giải thích theo hướng "VH BUỘC PHẢI thích ứng theo CL mới = thách thức quản trị thay đổi" → cách diễn dịch hợp lý nhưng hơi gượng.
- **Đề xuất sửa**: Thêm 1 câu cảnh báo rõ hơn ở phần giải Câu 6: *"Nếu khi đối chiếu với form gốc thấy phương án C có chữ 'KHÔNG phù hợp' thì đáp án B chắc chắn đúng. Nếu đúng nguyên văn là 'phù hợp', SV nên xem xét lại — có khả năng đáp án thực là một phương án khác hoặc đề có lỗi in ấn."*
- **Hành động**: Không bắt buộc sửa solution; có thể giữ nguyên + thêm 1 dòng cảnh báo. Đây là edge case của OCR, không phải lỗi sư phạm của solver.

#### Câu 16 — **[CÔNG THỨC/THUẬT NGỮ]** — mức độ: NHẸ

- **Mô tả**: Solver giải thích "Tính tổng thể" = "mục tiêu các bộ phận phải kết nối thành tổng thể, không xung đột nhau".
- **Phân tích**: Trong nguyên tắc SMART chuẩn, không có yếu tố "tổng thể" trực tiếp. Yếu tố tương đương trong giáo trình là **"tính nhất quán logic với mục tiêu dài hạn"** (lecture 6.2). Solver đã suy diễn đúng tinh thần nhưng chưa nối thẳng vào thuật ngữ chuẩn của bài giảng.
- **Đề xuất sửa**: Thêm 1 câu: *"Trong bài giảng, yêu cầu này được diễn đạt là 'nhất quán logic với mục tiêu dài hạn' — tức từng mục tiêu của từng bộ phận phải tổng hợp thành định hướng dài hạn của DN."*
- **Hành động**: Tùy chọn; không ảnh hưởng đáp án.

#### Câu 4 — **[DẪN CHIẾU YẾU]** — mức độ: NHẸ

- **Mô tả**: Lecture summary chỉ ghi chung "Bộ phận/SBU: Tiếp cận hiệu quả, thích ứng nhanh", không có ưu điểm cụ thể của cấu trúc theo địa lý.
- **Phân tích**: Đáp án A "giảm chi phí vận tải" là kiến thức từ giáo trình QTCL chuẩn (Hill & Jones, Pearce & Robinson) — đúng nhưng KHÔNG có trong lecture summary của môn này.
- **Đề xuất sửa**: Solver có thể chú thích: *"Lecture không liệt kê chi tiết — kiến thức bổ sung từ giáo trình QTCL: cấu trúc địa lý ưu tiên gần TT/NCC địa phương, giảm chi phí vận tải/kho bãi."*
- **Hành động**: Tùy chọn. Solver đã hiểu đúng tinh thần.

---

### ✅ Điểm tốt nổi bật

1. **Bảng đáp án nhanh ở đầu**: format chuẩn theo các bài chương 1–5, dễ scan, có "từ khóa chính" giúp SV ôn tập.
2. **Phân biệt hoạch định vs thực thi rõ ràng (Câu 7, 14)**: đây là điểm dễ nhầm nhất của chương 6, solver đã đưa vào bảng đối chiếu cuối → sư phạm tốt.
3. **Bảng so sánh 3 cấu trúc tổ chức**: tổng kết Câu 9, 13, 19 thành 1 ô — giúp SV nắm "ưu/nhược điểm điển hình của từng cấu trúc".
4. **Mô hình 7S đầy đủ Hard S + Soft S** (Câu 1): bổ sung kiến thức nâng cao mà nhiều SV bỏ qua.
5. **Loại trừ đầy đủ**: hầu hết câu đều có "Loại trừ A/B/C/D vì..." giúp SV không chỉ chọn đáp án đúng mà còn hiểu vì sao 3 phương án còn lại sai.

### ✅ Phần ví dụ thực tế (4 case)

| Case | DN | Khái niệm minh họa | Đánh giá |
|---|---|---|---|
| 1 | Viettel | Văn hóa "Người lính" + đa SBU | ✅ DN có thật, mô tả khớp thực tế công khai |
| 2 | FPT | Mô hình 7S khi tái cấu trúc 2012–2013 | ✅ Sự kiện đã được công bố; phân tích 7S logic |
| 3 | MWG | Phân bổ nguồn lực + dàn trải | ✅ Số liệu cửa hàng khớp với báo chí công khai (~2.140 → ~1.700 BHX) |
| 4 | VinFast | Cấu trúc ma trận trong dự án xe điện toàn cầu | ✅ Sự kiện có thật; phân tích 2 trục hợp lý |

**Lưu ý nhỏ**: Trong Ví dụ 3, con số "2.140 cửa hàng BHX" cần verify lại nếu publish chính thức (báo cáo MWG 2022 ghi peak ~2.140; số đóng cửa "hơn 400" có thể cần kiểm tra lại nguồn). Hiện tại không bịa nghiêm trọng.

### ✅ Phần extensions

- **Bài luyện 1**: 6 tình huống case nhỏ, đáp án phủ đủ các loại cấu trúc → tốt cho luyện tập áp dụng.
- **Bài luyện 2**: Tích hợp 7S với chuyển đổi CL chi phí thấp → premium → bài hay, đào sâu được mô hình 7S.
- **Bài luyện 3**: Case study CafeChain rất tốt — tích hợp Chương 5 (đa dạng hóa, phát triển TT, tích hợp dọc) với Chương 6 (cấu trúc, văn hóa, lãnh đạo). Sơ đồ SBU bằng text rõ ràng.
- **Đào sâu**: 4 khái niệm bổ sung (Mintzberg, Kotter, BSC, OKR) đều là kiến thức kinh điển, có nguồn dẫn uy tín.
- **Tranh luận học thuật**: Chandler vs Mintzberg là điểm tranh luận có giá trị, sinh viên có thể dùng cho bài tiểu luận/vấn đáp.

---

## 🎯 Đề xuất tổng thể cho solver

1. **(Tùy chọn)** Bổ sung 1 dòng cảnh báo OCR ở Câu 6 — đề cập khả năng phương án C có thể là "KHÔNG phù hợp" thay vì "phù hợp".
2. **(Tùy chọn)** Ở Câu 16, nối "tính tổng thể" với thuật ngữ chuẩn "nhất quán logic với mục tiêu dài hạn" của lecture.
3. **(Tùy chọn)** Ở Câu 4, ghi chú rằng kiến thức bổ sung từ giáo trình tham khảo, không có trong lecture summary.
4. **Khuyến nghị (không bắt buộc)**: Trong tương lai, các chương sau có thể có 1 đoạn ngắn ở đầu solution mô tả "phương pháp luận giải" — vd: "ưu tiên dẫn chiếu lecture, bổ sung từ giáo trình khi lecture im lặng" — để minh bạch nguồn cho SV.

**Tất cả đề xuất trên đều là NHẸ, không bắt buộc revise.** Verdict cuối: **PASS**, chuyển status `draft → approved`, không cần round 2.

---

## 🔁 Tự kiểm tra độc lập (mẫu — Câu khó nhất)

### Câu 6 — Reviewer tự giải lại

**Đề**: "Trong thực thi chính sách nhân sự, việc định hướng và đào tạo nhân viên thường gặp thách thức nào?"
- A. Nhân viên không thấy sự liên kết giữa CL và công việc hàng ngày.
- B. Các phương án còn lại đều đúng.
- C. Văn hóa DN phù hợp với sự thay đổi do CL mới.
- D. CL công ty thay đổi liên tục hàng tuần khiến chương trình đào tạo lỗi thời.

**Reviewer phân tích**:
- A: rõ ràng là thách thức quản trị thay đổi.
- D: rõ ràng là thách thức triển khai.
- C: ngữ pháp "phù hợp" gợi ý đây KHÔNG phải thách thức (vì đã phù hợp rồi). Nhưng nếu đọc theo cách khác — "VIỆC ĐẢM BẢO VH phù hợp với CL mới" — thì đây là thách thức quản trị.

**Hai khả năng**:
1. OCR sót "không" → C nguyên gốc là "VH KHÔNG phù hợp" → 3 phương án đều đúng → đáp án B.
2. OCR đúng → C ngụ ý "việc đảm bảo VH phù hợp" → đáp án B vẫn đúng (vì 3 ý đều có thể là thách thức theo nghĩa rộng).

**Kết luận**: Đáp án B là an toàn nhất trong cả hai trường hợp. Solver chọn B đúng. Tuy nhiên nên cảnh báo SV về tính mơ hồ của phương án C.

---

### Câu 19 — Reviewer tự giải lại (vì có "bẫy" tất cả đều đúng)

**Đề**: "Loại hình cấu trúc tổ chức theo bộ phận tỏ ra không hiệu quả khi nào?"
- A. Tất cả các ý còn lại đều đúng.
- B. DN hoạt động ở nhiều thị trường.
- C. DN có nhiều SP.
- D. Xảy ra sự cạnh tranh về nguồn lực giữa các bộ phận.

**Reviewer phân tích từ lecture 6.4**:
- Cấu trúc bộ phận **PHÙ HỢP** khi: nhiều SP, nhiều TT, nhiều KH (B và C đúng là điều kiện áp dụng).
- Nhược điểm cấu trúc bộ phận: tăng chi phí quản lý, thiên lệch ngắn hạn, **cạnh tranh nguồn lực giữa các bộ phận**.

→ B và C là PHÙ HỢP, không phải "không hiệu quả" → A "tất cả đúng" tự động sai. Chỉ D là đúng.

**Đáp án reviewer**: D. **Khớp với solver**.

---

## ✍️ Phần cần viết lại

Không có. Solution đạt chất lượng PASS không cần revision.

---

## 📌 Hành động cần làm sau review

1. Cập nhật front-matter file solution: `status: "draft"` → `status: "approved"`, `review_round: 0` → `review_round: 1`, thêm `review_score: 9.2`.
2. (Tùy chọn) Áp 3 cải tiến NHẸ ở phần "Đề xuất tổng thể".
3. Pipeline kết thúc — không cần round review tiếp.
