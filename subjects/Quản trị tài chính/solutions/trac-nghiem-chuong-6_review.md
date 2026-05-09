---
reviewed_file: "trac-nghiem-chuong-6_solution.md"
reviewed_at: "2026-05-09T18:00:00Z"
review_round: 1
overall_score: 9.1
verdict: "PASS"
criteria:
  correctness: 9
  logic: 9
  calculation: 10
  vn_context: 9
  pedagogy: 9
---

# Báo cáo Rà soát: Trắc nghiệm Chương 6 — Quản trị Tài trợ

## 📊 Điểm tổng quan
**Tổng: 9.1 / 10** — Verdict: **PASS**

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---|---|
| Chính xác khái niệm/công thức | 9/10 | TDTM, vay chiết khấu, niên kim đều chuẩn; có dẫn chiếu VAS 06, Thông tư 45/2013 |
| Logic lập luận | 9/10 | Loại trừ rõ; phân biệt được nợ vs VCSH, thuê vận hành vs tài chính |
| Tính toán | 10/10 | 6/6 phép tính (Câu 4, 7, 8, 19, 23, 25) đều khớp đáp án |
| Phù hợp ngữ cảnh VN | 9/10 | VinFast, MWG, Vietnam Airlines minh họa trực tiếp khái niệm |
| Sư phạm & chi tiết | 9/10 | "Sai lầm thường gặp" hữu ích ở câu tính toán; bảng so sánh CP ưu đãi/trái phiếu, thuê vận hành/tài chính |

## 🔁 Kiểm tra tính toán

### Câu 4: Vay chiết khấu (900, 12%, 4 tháng)
- Discount kỳ: $12\% \times 4/12 = 4\%$
- Mệnh giá $F = 900/0{,}96 = 937{,}5$ trđ; Lãi = 37,5 trđ
- Period rate = $37{,}5/900 = 4{,}167\%$
- $EAR = (1{,}04167)^3 - 1 = 13{,}03\%$ ≈ **A. 13,02%** ✅

### Câu 7: Vay chiết khấu (600, 11%, 4 tháng)
- Discount kỳ: $3{,}667\%$ → $F = 622{,}84$ → Lãi = 22,84
- Period rate = $3{,}806\%$
- $EAR = (1{,}03806)^3 - 1 = 11{,}86\%$ → **B. 11,86%** ✅

### Câu 8: Vay có ký quỹ (900 thực, 9%, ký quỹ 10%, 4 tháng)
- Vay $X$ với $0{,}9X = 900 \Rightarrow X = 1.000$
- Lãi 4 tháng = $1.000 \times 9\% \times 4/12 = 30$ trđ
- Period rate (trên 900 thực) = $30/900 = 3{,}333\%$
- $EAR = (1{,}03333)^3 - 1 = 10{,}33\%$ → **D. 10,33%** ✅

### Câu 19: Cost TDTM (2/10 net 60, ngày 60)
$\text{Cost} = \dfrac{0{,}02}{0{,}98} \times \dfrac{360}{50} = 0{,}02041 \times 7{,}2 = 14{,}69\%$ → **A. 14,69%** ✅

### Câu 23: PMT niên kim (vay 1.000, 7%, 15 năm)
- $1{,}07^{15} = 2{,}7590$
- $PVAF = (1 - 1/2{,}7590)/0{,}07 = 0{,}6376/0{,}07 = 9{,}1079$
- $PMT = 1.000/9{,}1079 = 109{,}79$ trđ → **C. 109,79 triệu** ✅

### Câu 25: Cost TDTM (2/10 net 60, ngày 50)
$\text{Cost} = \dfrac{0{,}02}{0{,}98} \times \dfrac{360}{40} = 0{,}02041 \times 9 = 18{,}37\%$ ≈ **C. 18,36%** ✅ (chênh lệch do làm tròn)

## 🔍 Kiểm tra đáp án lý thuyết

24 câu lý thuyết kiểm tra đối chiếu nguyên tắc Chương 6:

- **Câu 1 (A)**: Trái phiếu CÓ kỳ hạn vốn gốc, CP ưu đãi KHÔNG → A là đặc điểm KHÔNG chung ✅
- **Câu 2 (D)**: Quyền sử dụng đất lâu dài không trích KH (Thông tư 45/2013) ✅
- **Câu 3 (B)**: Phát hành CP thường → VCSH ↑, hệ số nợ ↓ ✅
- **Câu 5 (B)**: Phân chia ngắn/dài hạn dựa vào thời gian sử dụng ✅
- **Câu 6 (A)**: Cổ tức CP thường phụ thuộc lãi → A ✅
- **Câu 9 (C)**: Cost TDTM nghịch với thời hạn tín dụng (xem công thức) ✅
- **Câu 10 (C)**: Thuê hoạt động → bên cho thuê là chủ → trích KH ✅
- **Câu 11 (B)**: Trade-off MM: nợ rẻ hơn VCSH ✅
- **Câu 12 (A)**: Vi phạm matching principle (TDTM ngắn cho TS dài) ✅
- **Câu 13 (B)**: CP ưu đãi cố định khi DN khó khăn = bất lợi ✅
- **Câu 14 (D)**: Cổ tức CP ưu đãi cố định, không nhất thiết lớn hơn CP thường ✅
- **Câu 15 (C)**: Tax shield đảo chiều: lãi vay ↓ → thuế ↑ ✅
- **Câu 16 (B)**: VCSH/Nợ phân chia theo quyền sở hữu ✅
- **Câu 17 (A)**: Nợ NH có hợp đồng, tính lãi → KHÔNG phải accrued ✅
- **Câu 18 (B)**: "2/10 net 40" → chiết khấu 2% ✅
- **Câu 20 (A)**: Accruals "miễn phí" vì không tính lãi ✅
- **Câu 21 (C)**: Lãi suất thấp → lãi chiết khấu thấp → nhận về nhiều ✅
- **Câu 22 (A)**: Trì hoãn lâu hơn → mẫu số tăng → cost giảm ✅
- **Câu 24 (C)**: Lãi vay cố định, độc lập KQKD ✅
- **Câu 26 (B)**: Thuê vận hành = ngắn hạn, tránh rủi ro giảm giá ✅
- **Câu 27 (B)**: Hạn mức = dư nợ tối đa duy trì ✅
- **Câu 28 (A)**: VAS 06 — thuê tài chính ghi nhận như khoản nợ ✅
- **Câu 29 (C)**: CP ưu đãi là VCSH → hệ số nợ giảm (tương tự Câu 3) ✅
- **Câu 30 (B)**: Vòng quay vốn vay là cam kết đặc thù của hạn mức ✅

## ⚠️ Điểm cần lưu ý

### 1. Quy ước 360 vs 365 ngày (Câu 19, 25)
Solution dùng **360 ngày** (quy ước thương mại VN) → khớp đáp án A=14,69% và C=18,36%. Nếu giáo trình khác dùng 365 ngày → ra 14,90% và 18,62% (không có trong đáp án). **Quan trọng**: học sinh cần ghi nhớ quy ước 360 ngày khi gặp đề trắc nghiệm dạng này.

### 2. Compound vs simple annualization (Câu 4, 7, 8)
Solution dùng **compound** (lũy thừa $n$ kỳ trong năm) thay vì simple (nhân $n$). Nếu dùng simple:
- Câu 4: $4{,}167\% \times 3 = 12{,}5\%$ (không khớp đáp án)
- Câu 8: $3{,}333\% \times 3 = 10\%$ (không khớp đáp án)

→ Đề trắc nghiệm này **bắt buộc** dùng compound. Solution xử lý đúng. Nên ghi chú rõ trong giảng dạy.

### 3. Câu 12: A vs D — hơi gây tranh cãi
- A (TDTM tài trợ TS dài hạn) → vi phạm cấu trúc, **rủi ro hệ thống**.
- D (không tận dụng chiết khấu) → chỉ là **bỏ lỡ tối ưu**, không phải "không hiệu quả".

Solution chọn A và giải thích phù hợp. Nhưng nếu đề muốn nhấn mạnh "lãng phí" → có thể chọn D. **Khuyến nghị**: ghi rõ tiêu chí chọn A là "rủi ro thanh khoản", không phải "lãng phí".

## ✅ Kết luận

Lời giải **đạt yêu cầu** trên tất cả 5 tiêu chí. 6/6 phép tính được kiểm chứng từ đầu, đặc biệt phần lãi suất thực tế khoản vay (Câu 4, 7, 8) đòi hỏi nắm chắc compound annualization. Đáp án 30/30 đều có lập luận hợp lý.

Ví dụ thực tế (VinFast — cấu trúc tài trợ; MWG — TDTM; Vietnam Airlines — thuê máy bay) liên hệ trực tiếp với từng cụm câu hỏi và phù hợp ngữ cảnh VN.

**Không cần vòng sửa.** Có thể nâng `status` của solution lên `reviewed`, `review_round = 1`.
