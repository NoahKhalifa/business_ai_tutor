---
name: exercise-solver
description: Giải chi tiết bài tập, câu hỏi ôn tập chuyên ngành Quản trị Kinh doanh (chiến lược, marketing, tài chính, nhân lực, vận hành, kế toán quản trị). BẮT BUỘC dùng skill này bất cứ khi nào người dùng đưa câu hỏi/đề bài/bài tập kinh doanh và muốn lời giải chi tiết, có dẫn dắt từng bước, có dẫn chiếu lý thuyết. Không chỉ trả lời đáp án mà phải có giải thích sư phạm để sinh viên học được.
---

# Skill: Exercise Solver (giải bài chi tiết)

## Mục tiêu
Sinh lời giải chuẩn sư phạm: không phải chỉ ra đáp án, mà DẪN DẮT sinh viên hiểu cách suy luận, dẫn chiếu lý thuyết từ bài giảng, và trình bày như giảng viên đang giải mẫu trên lớp.

## Khi nào trigger
- User đưa file MD đề bài và yêu cầu giải.
- Pipeline tự động sau bước `pdf-to-md` cho file trong `exercises/md/`.
- User nói: "giải bài này", "hướng dẫn giải", "phân tích case study".

## Nguyên tắc viết lời giải

### Cấu trúc bắt buộc cho MỖI câu hỏi

```markdown
## Câu N: [tóm tắt đề trong 1 dòng]

### 📋 Đề bài
> [Trích nguyên văn đề]

### 🎯 Phân tích đề
- **Dạng bài**: [VD: phân tích SWOT, tính NPV, hoạch định nhân sự...]
- **Yêu cầu chính**: [Tách thành các yêu cầu nhỏ nếu đề có nhiều ý]
- **Dữ kiện đã cho**: [liệt kê]
- **Cần tìm**: [liệt kê]

### 📚 Kiến thức nền cần dùng
- [Khái niệm 1] — tham chiếu mục X.Y trong bài giảng `[bai-N.md]`
- [Công thức/mô hình 2]
  $$ \text{công thức nếu có} $$

### 🔍 Hướng tiếp cận
[Giải thích vì sao chọn cách giải này, có cách nào khác không]

### ✍️ Lời giải chi tiết

**Bước 1**: [...]
- Tại sao làm bước này: [...]
- Tính toán/lập luận: [...]

**Bước 2**: [...]

...

### ✅ Kết luận
[Đáp án cuối + ý nghĩa thực tiễn cho doanh nghiệp]

### ⚠️ Sai lầm thường gặp
- [Lỗi 1 SV hay mắc + cách tránh]
- [Lỗi 2]

### 💡 Mẹo / Ghi chú
[Nếu có]
```

## Quy tắc nội dung

### 1. Bám sát bài giảng
- LUÔN đọc các file `lectures/md/*.md` của môn trước khi giải.
- Khi dùng khái niệm/công thức → dẫn chiếu rõ: "(theo Mục 2.3 — Bài 1)".
- Không tự bịa lý thuyết ngoài bài giảng nếu môn đã cung cấp.

### 2. Chuyên ngành Quản trị Kinh doanh
Các dạng bài thường gặp & cách xử lý:

| Dạng bài | Cách giải |
|---|---|
| Phân tích SWOT | Vẽ ma trận 4 ô, mỗi ô ≥ 3 điểm, kèm lập luận từ case |
| 5 áp lực Porter | Phân tích từng áp lực, đánh giá mức độ (cao/trung/thấp) + lý do |
| BCG matrix | Tính thị phần tương đối + tốc độ tăng trưởng → định vị → khuyến nghị |
| NPV / IRR | Liệt kê dòng tiền theo năm → công thức → tính → so sánh ngưỡng |
| Điểm hòa vốn | Công thức $BEP = FC/(P-VC)$ → áp số → diễn giải |
| Marketing 4P/7P | Phân tích từng P, gắn với khách hàng mục tiêu |
| Phân tích báo cáo tài chính | Tính tỷ số → so sánh ngành → diễn giải |
| Hoạch định nhân sự | Dự báo cầu — cung — chênh lệch — kế hoạch |
| Quản trị tồn kho (EOQ) | $EOQ=\sqrt{2DS/H}$ → giải thích các biến |
| Case study định tính | Identify problem → frameworks → alternatives → recommendation |

### 3. Tính toán
- Trình bày SỐ LIỆU TRUNG GIAN, không nhảy bước.
- Đơn vị tiền tệ: dùng VND/triệu/tỷ rõ ràng. Quy đổi nếu đề ra USD.
- Làm tròn đúng quy ước (NPV thường 2 chữ số thập phân, tỷ số tài chính 2-4 chữ số).

### 4. Văn phong
- Ngôi xưng: "ta", "chúng ta" (sư phạm).
- Câu ngắn, mệnh đề rõ.
- Dùng emoji header nhẹ để dễ scan (📋 🎯 📚 🔍 ✍️ ✅ ⚠️ 💡).
- KHÔNG dùng ngôn ngữ marketing kiểu "tuyệt vời", "siêu hay".

## Quy trình thực hiện

1. Đọc toàn bộ MD bài giảng của môn (`subjects/<môn>/lectures/md/*.md`).
2. Đọc MD đề bài.
3. Với mỗi câu trong đề:
   a. Áp dụng template ở trên.
   b. Nếu câu phức tạp → chia thành các câu hỏi con tự đặt rồi giải dần.
4. Ghép tất cả thành 1 file `solutions/<tên-đề>_solution.md` với front-matter:

```yaml
---
exercise_file: "de-on-tap-chuong-1.md"
solved_at: "2026-05-09T11:00:00Z"
status: "draft"
review_round: 0
total_questions: 5
---
```

5. Tự kiểm tra nhanh trước khi xuất:
   - Có dẫn chiếu bài giảng không?
   - Có "Sai lầm thường gặp" không?
   - Có kết luận rõ không?

## Quy tắc tiết kiệm token khi đọc bài giảng

Khi đọc bài giảng để có context giải bài, áp dụng chiến lược 2 tầng:

### Tầng 1: Đọc summary trước (mặc định)
- Đọc TẤT CẢ `subjects/<môn>/lectures/md/*_summary.md`
- Mỗi summary ~500-1,000 token, 5 lecture chỉ tốn ~3,000-5,000 token
- Đủ để biết "khái niệm A nằm ở bài N, công thức B trong bài M"

### Tầng 2: Chỉ mở bản đầy đủ khi cần verify
- Sau khi đọc summary, nếu giải bài cần CHI TIẾT về 1-2 khái niệm cụ thể
- → Mở bản đầy đủ `<tên>.md` chỉ của bài liên quan, KHÔNG đọc tất cả
- Ví dụ: bài tập về NPV → chỉ mở `bai-X-tham-dinh-du-an.md`, không cần đọc bài về SWOT

### Khi nào BẮT BUỘC đọc bản đầy đủ
- Bài tập trích nguyên văn case study từ slide → cần đọc full để verify
- User yêu cầu "dẫn chiếu chính xác mục X.Y" → mở chính xác bài đó
- Lời giải bị reviewer phát hiện sai → đọc lại bài đầy đủ liên quan để sửa

## Khi nào dùng skill khác
- Sau khi giải xong → CHUYỂN sang skill `example-generator` để thêm ví dụ thực tế.
- Sau example-generator → `extension-builder` để thêm bài tập mở rộng.
- Cuối cùng → `answer-reviewer` để rà soát.

## Edge cases
- **Đề mơ hồ** → liệt kê các giả định, giải theo từng giả định.
- **Đề thiếu dữ liệu** → ghi rõ "Thiếu dữ liệu: ...", đề xuất cách giả định hợp lý.
- **Đề có nhiều đáp án đúng** (case study) → trình bày 2-3 phương án, so sánh.
- **Đề tiếng Anh** → giải bằng tiếng Việt, giữ thuật ngữ gốc trong ngoặc: "lợi thế cạnh tranh (competitive advantage)".

## Khi sửa lại theo phản hồi reviewer
Nếu file `<tên-đề>_review.md` đã tồn tại với verdict REVISE:
1. Đọc kỹ phản hồi reviewer (đặc biệt phần "⚠️ Vấn đề phát hiện").
2. Sửa từng lỗi NẶNG trước, rồi VỪA, rồi NHẸ.
3. Giữ những phần reviewer đã ghi "✅ Điểm tốt".
4. Cập nhật `review_round +=1` trong front-matter.
5. Đặt lại `status: draft` để chờ review tiếp.
