---
name: example-generator
description: Sinh ví dụ thực tế minh họa cho khái niệm/bài tập quản trị kinh doanh, ưu tiên doanh nghiệp Việt Nam và Đông Nam Á để sinh viên dễ liên hệ. BẮT BUỘC dùng skill này sau khi đã có lời giải sơ bộ và cần thêm phần "ví dụ thực tế" để minh họa, hoặc khi người dùng hỏi "ví dụ thực tế là gì", "doanh nghiệp Việt Nam nào áp dụng".
---

# Skill: Example Generator (ví dụ thực tế)

## Mục tiêu
Mỗi lời giải/khái niệm phải có **2–3 ví dụ thực tế** từ doanh nghiệp Việt Nam (ưu tiên), Đông Nam Á, hoặc quốc tế nổi tiếng. Mục đích: sinh viên thấy lý thuyết áp dụng được, không hàn lâm khô cứng.

## Khi nào trigger
- Sau bước `exercise-solver` trong pipeline.
- User hỏi: "ví dụ thực tế?", "doanh nghiệp nào áp dụng?", "case study Việt Nam?".

## Nguyên tắc chọn ví dụ

### Ưu tiên theo thứ tự
1. **Doanh nghiệp Việt Nam có thông tin công khai**: Vinamilk, Viettel, FPT, VinFast, Vingroup, Thế Giới Di Động, Masan, Hòa Phát, Techcombank, Vietcombank, Mobile World, ACB, Sabeco, Highlands Coffee, Phúc Long, The Coffee House, Trung Nguyên, Biti's, Saigon Co.op, GHN, Giao Hàng Tiết Kiệm, Tiki, Shopee VN.
2. **Doanh nghiệp Đông Nam Á**: Grab, Gojek, Lazada, Garena/Sea, Traveloka.
3. **Quốc tế nổi tiếng có liên hệ thị trường VN**: Apple, Samsung, Toyota, Honda, Unilever, Nestlé, Coca-Cola, Starbucks.

### Tránh
- Ví dụ quá cũ (trước 2010) trừ khi đó là case kinh điển (VD: Kodak).
- Doanh nghiệp ít thông tin để xác minh.
- Bịa số liệu cụ thể không kiểm chứng được — dùng "khoảng", "ước tính" hoặc nói rõ là minh họa.

## Format ví dụ (append vào lời giải)

```markdown
### 🏢 Ví dụ thực tế

#### Ví dụ 1: [Tên doanh nghiệp] — [Ngắn gọn vấn đề]
**Bối cảnh**: [2-3 câu mô tả tình huống doanh nghiệp]

**Áp dụng [khái niệm/mô hình vừa học]**:
- [Phân tích điểm 1]
- [Phân tích điểm 2]
- [Phân tích điểm 3]

**Kết quả/Bài học**: [Doanh nghiệp đạt được gì? Bài học cho SV?]

**Liên hệ với bài**: [Khái niệm này thể hiện ở đâu trong case này?]

---

#### Ví dụ 2: [Tên DN khác]
[Cấu trúc tương tự]
```

## Một số gợi ý map khái niệm → doanh nghiệp Việt Nam

| Khái niệm | Doanh nghiệp gợi ý |
|---|---|
| Chiến lược khác biệt hóa | Vinamilk (sữa organic), Highlands Coffee, VinFast |
| Chiến lược chi phí thấp | Bách Hóa Xanh, AirAsia, Mobile World |
| Chiến lược tập trung | Biti's Hunter (giới trẻ), The Coffee House (gen Z) |
| Đa dạng hóa | Vingroup (BĐS → ô tô → giáo dục), FPT (CNTT → giáo dục → bán lẻ) |
| M&A | Masan mua VinCommerce, ThaiBev mua Sabeco |
| 5 lực Porter | Ngành viễn thông VN (Viettel/VNPT/Mobifone) |
| BCG matrix | Danh mục SP của Vinamilk hoặc Masan |
| Định giá thâm nhập | Shopee, Grab khi mới vào VN |
| Định giá hớt váng | iPhone, Samsung Galaxy S series |
| Marketing 4P/7P | Phúc Long, Highlands, Starbucks VN |
| CRM | Thế Giới Di Động, Tiki |
| Quản trị chuỗi cung ứng | Vinamilk, Hòa Phát, Vinfast |
| Lean / Tinh gọn | Toyota VN, Honda VN |
| Quản trị nhân tài | FPT, Viettel, VinGroup |
| KPI/OKR | FPT, Viettel, MoMo |
| Văn hóa doanh nghiệp | Viettel ("Người lính"), FPT ("STCo"), Vingroup |
| Khởi nghiệp/đổi mới | MoMo, VNG, Tiki, Got It |
| Đạo đức kinh doanh / ESG | Vinamilk, TH True Milk |

## Quy trình thực hiện
1. Đọc lời giải hiện có.
2. Xác định 1-2 khái niệm CỐT LÕI mà bài tập đang minh họa.
3. Chọn 2-3 doanh nghiệp phù hợp từ bảng map.
4. Với mỗi DN, viết theo format ở trên (~150-250 từ/ví dụ).
5. Append vào file solution, giữ nguyên phần đã có.
6. Cập nhật front-matter: thêm `examples_added: true`.

## Lưu ý quan trọng về tính chính xác
- KHÔNG đưa số liệu doanh thu/lợi nhuận cụ thể nếu không chắc chắn.
- Có thể nói: "Vinamilk là doanh nghiệp sữa lớn nhất Việt Nam" (đúng, công khai).
- KHÔNG nên: "Vinamilk doanh thu 2024 đạt 60.5 nghìn tỷ" trừ khi đã verify.
- Nếu cần con số → ghi: "(số liệu công bố trong báo cáo thường niên, sinh viên có thể tra cứu để cập nhật)".
- Tốt hơn là tập trung vào **chiến lược, hành vi, quyết định** chứ không phải con số.

## Edge cases
- **Bài tập quá hẹp** (vd: tính EOQ với số liệu cụ thể) → ví dụ thực tế là về cách doanh nghiệp tương tự áp dụng EOQ trong quản lý kho.
- **Bài về luật/quy định** → ví dụ về vụ việc đã được công bố trên báo chính thống.
- **Bài về văn hóa quốc tế** → so sánh DN VN với DN nước ngoài tương đương.
