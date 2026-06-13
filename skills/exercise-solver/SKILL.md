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

### Cấu trúc bắt buộc cho TRẮC NGHIỆM (MCQ) — override template 8 phần

> **Định nghĩa**: **MCQ = Multiple Choice Question = câu hỏi trắc nghiệm có nhiều lựa chọn** (trong project này luôn là 4 phương án A/B/C/D, chọn 1 đáp án đúng). Section này áp dụng cho mọi đề trắc nghiệm trong `subjects/<môn>/exercises/`.
>
> **Tại sao có template riêng**: dùng template 8 phần ở trên cho 30-35 câu MCQ là quá nặng → solver thường sinh boilerplate ("không khớp trọng tâm khái niệm" lặp khắp các câu, "Sai lầm thường gặp" copy-paste). Template MCQ dưới đây bắt buộc per-option analysis + cite-line để tránh tình trạng này.

```markdown
## Câu N: [tóm tắt đề ngắn 1 dòng]

**Đề:** [trích nguyên văn đề + 4 phương án A/B/C/D]

**Đáp án: X**

**Phân tích từng phương án:**
- **A.** [nội dung A] — [Đúng/Sai] vì [LÝ DO CỤ THỂ cho câu này — KHÔNG dùng câu generic chung]. Theo `lectures/md/<file>.md` dòng [X-Y].
- **B.** [nội dung B] — [Đúng/Sai] vì [...]. Theo `lectures/md/<file>.md` dòng [X-Y].
- **C.** [...]
- **D.** [...]

**Trích bài giảng (chứng minh đáp án đúng):**
> [Quote nguyên văn đoạn quan trọng nhất, kèm số dòng]

**Sai lầm thường gặp ở CÂU NÀY:** [Phải phản ánh nội dung cụ thể của câu N — không phải template áp dụng cho mọi câu]

**(Tùy chọn) Mẹo phân biệt:** [Nếu khái niệm dễ nhầm với khái niệm khác trong bài]
```

**Bắt buộc khi giải MCQ:**

1. **Phân tích RIÊNG từng phương án A/B/C/D** — không dùng cùng 1 câu generic ("không khớp trọng tâm khái niệm") cho mọi phương án/mọi câu.
2. **Trích số dòng bài giảng** (`dòng X-Y`) **ít nhất 1 lần/câu**. Mở file MD lecture đếm/tìm dòng chính xác.
3. **"Sai lầm thường gặp" RIÊNG cho câu đó** — phản ánh khái niệm cụ thể của câu N, không phải template.
4. **Cảnh báo OCR confusables**: nếu đề/phương án chứa từ trong danh sách OCR confusables (vi/vĩ, sỉ/sĩ, lý/ly, lỗ/lô, hoàn/hoàng — xem `skills/pdf-to-md/SKILL.md`) HOẶC có flag inline `[VERIFY_OCR: ...]` → **DỪNG**, mở PDF gốc verify. Nếu MD đề khác PDF → sửa MD đề trước, rồi giải lại.

### Adaptive verbosity — viết DÀI cho câu khó, viết NGẮN cho câu định nghĩa thuần

Không phải câu MCQ nào cũng đáng giải dài. Phân loại trước, điều chỉnh độ dài:

**Câu KHÓ / QUAN TRỌNG → giải kỹ + mở rộng (~250-400 từ/câu).** Triệu chứng:
- Case study, scenario, suy luận chiến lược (vd "Một DN công nghệ muốn... cần làm gì?")
- Khái niệm nền tảng cần khắc sâu (TCO, EOQ, VMI, 5 lực Porter, BCG, NPV...)
- Wording dễ nhầm / confusables / nghi vấn đáp án — flag rõ cho reviewer
- Phương án nhiễu phức tạp (≥2 phương án có vẻ đúng, cần phân biệt tinh)
- Câu có nhiều khía cạnh liên quan tới các chương khác → cần liên hệ mở rộng

Với câu khó: giữ đầy đủ template (per-option + trích + sai lầm) + thêm **"💡 Mở rộng / Liên hệ"** (1-2 đoạn nối với khái niệm khác trong môn hoặc thực tiễn DN VN).

**Câu định nghĩa THUẦN / thuộc lòng → ngắn gọn (~80-150 từ/câu).** Triệu chứng:
- "Theo X, ___ được định nghĩa là gì?" / "X là khái niệm liên quan đến hoạt động nào?"
- Đề trích nguyên văn 1 câu từ lecture → match 1:1 với 1 đáp án
- Phương án nhiễu chỉ là tên khái niệm khác cùng chủ đề (3-4 thuật ngữ song song)
- Câu cặp đôi với câu khác (cross-reference) — đã viết kỹ ở câu trước

Format câu ngắn (compact):
```markdown
### Câu N: [tóm tắt]
**Đáp án: X** — [trích 1 dòng wording lecture quyết định + dòng X-Y]
- **A.** [tên]. ✗ — [1 cụm ngắn vì sao sai + dòng]
- **B.** [tên]. ✗ — [...]
- **C.** [tên]. ✓ — [...]
- **D.** [tên]. ✗ — [...]

**Lưu ý**: [1 dòng — mẹo phân biệt, hoặc "Cặp với Câu M" nếu cross-reference]
```

**Bắt buộc giữ ngay cả ở câu ngắn:**
- Per-option analysis A/B/C/D (không bỏ option nào)
- Cite-line `dòng X-Y` cho ít nhất đáp án đúng
- 1 dòng "Lưu ý" thay cho "Sai lầm thường gặp" đầy đủ

**Bỏ ở câu ngắn:**
- Section "Trích bài giảng" tách riêng (đã inline trong đáp án)
- "Sai lầm thường gặp" đầy đủ → rút thành "Lưu ý" 1 dòng
- "Mẹo phân biệt" → gộp vào "Lưu ý"

**Tỷ lệ tham khảo cho 1 file MCQ 30 câu:** ~30% câu khó (dài), ~70% câu định nghĩa (ngắn). Nếu tất cả đều dài → tốn token vô ích; nếu tất cả đều ngắn → mất giá trị sư phạm ở câu khó.

**Tự kiểm tra trước khi xuất MCQ solution:**
- [ ] Mỗi câu có 4 dòng phân tích A/B/C/D riêng (kể cả ở format ngắn)?
- [ ] Có ít nhất 1 reference `dòng X-Y` mỗi câu?
- [ ] Đọc lướt 5 câu liên tiếp — phần "Sai lầm thường gặp" / "Lưu ý" có giống nhau không? (Nếu giống → viết lại)
- [ ] Có flag `[VERIFY_OCR]` nào trong đề chưa verify không?
- [ ] Tỷ lệ câu dài vs ngắn có hợp lý không (gợi ý: ~30% dài / ~70% ngắn cho file 30 câu)?

## Quy tắc nội dung

### 1. Bám sát bài giảng — nhưng KHÔNG mù quáng

- LUÔN đọc các file `lectures/md/*.md` của môn trước khi giải.
- Khi dùng khái niệm/công thức → dẫn chiếu rõ: "(theo Mục 2.3 — Bài 1)".
- KHÔNG tự bịa lý thuyết ngoài bài giảng nếu môn đã cung cấp.
- **NHƯNG**: lecture là nguồn ưu tiên cho **đáp án thi**, KHÔNG phải nguồn duy nhất cho **kiến thức**. Sinh viên cần học khái niệm đúng, không chỉ học để thi.

### 1b. Critical engagement với lecture (BẮT BUỘC, đặc biệt khi giải MCQ)

Khi đọc lecture, đối chiếu với **kiến thức chuẩn ngành QTKD** (Kotler cho marketing, Porter cho chiến lược, Brealey/Myers cho tài chính, các sách giáo khoa Anh-Mỹ-VN uy tín). Nếu phát hiện 1 trong 3 vấn đề sau, PHẢI flag rõ trong solution:

**(a) Lecture THIẾU ý quan trọng** — khái niệm/khía cạnh cốt lõi không được nhắc đến.
- VD: lecture định nghĩa SWOT chỉ nói 4 ô mà không nói SWOT phải xuất phát từ phân tích nội bộ + ngoại bộ — đây là thiếu.
- Hành động: bổ sung phần thiếu trong "💡 Mở rộng / Bổ sung" và dẫn nguồn chuẩn.

**(b) Lecture GÂY NHẦM LẪN** — wording không rõ, 2 cách hiểu, hoặc khái niệm cùng tên với 2 nghĩa khác nhau trong tài liệu khác.
- VD: lecture dùng "hợp đồng giao sau" mơ hồ giữa "forward contract" (kỳ hạn OTC) và "futures contract" (giao sau tiêu chuẩn hóa trên sàn) — 2 khái niệm khác nhau trong tài chính.
- Hành động: nêu cả 2 cách hiểu trong "💡 Mở rộng", note đáp án theo lecture nhưng cảnh báo SV về sự khác biệt.

**(c) Lecture VIẾT SAI hoặc LẠC HẬU** — thông tin sai về khoa học/fact, định nghĩa không chuẩn, dữ liệu lỗi thời, hoặc framework đã được cập nhật/thay thế.
- VD: lecture nói "ECRS phát minh bởi Toyota" nhưng đúng là Frank & Lillian Gilbreth (1900s) trước Toyota; lecture trích Porter "5 Forces" nhưng list sai 1 trong 5 lực.
- Hành động: trong "⚠️ Ghi chú về tài liệu" cuối câu, nêu rõ sự sai sót + dẫn nguồn đúng. **Vẫn giữ đáp án theo lecture** (vì SV thi theo lecture) NHƯNG cảnh báo SV "khi học hoặc đi làm thực tế, cần biết phiên bản đúng là...".

**Nguyên tắc cân bằng:**
- 80%+ câu: lecture đúng và đầy đủ → không cần critical note, viết bình thường.
- ~10-20% câu khó/quan trọng: có thể cần bổ sung kiến thức ngoài lecture (mở rộng từ Kotler/Porter/sách chuẩn).
- ~5% câu: có thể có vấn đề lecture (thiếu/nhầm/sai) → flag theo (a)/(b)/(c).
- KHÔNG flag bừa bãi — chỉ flag khi có bằng chứng rõ ràng từ ≥1 nguồn chuẩn khác. Solver không được tự cho mình quyền "đúng hơn lecture" nếu chỉ là cảm tính.

**Format flag trong solution:**
```markdown
**⚠️ Ghi chú về tài liệu (critical engagement):**
- **Phát hiện**: [thiếu ý / gây nhầm lẫn / viết sai — chọn 1]
- **Chi tiết**: [giải thích cụ thể]
- **Nguồn chuẩn**: [tên sách/tác giả/link]
- **Khuyến nghị cho SV**: [khi đi thi: theo lecture; khi học/đi làm: theo nguồn chuẩn]
```

**Khi nào KHÔNG flag (tránh over-engineering):**
- Khác biệt nhỏ về wording không ảnh hưởng nội dung.
- Lecture đơn giản hóa cho mục đích sư phạm — không phải sai.
- Khái niệm có nhiều biến thể trong ngành — lecture chọn 1 biến thể hợp lý.
- Cảm tính của solver mà không có nguồn đối chiếu cụ thể.

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

## Xử lý bài tập có audio (listening / pronunciation)

> **Section này CHỈ áp dụng khi môn có `media_types: ["audio"]` trong `metadata.yaml`.**
> Các môn KHÔNG có cờ này → bỏ qua toàn bộ section, xử lý như bình thường.

### Khi nào cần đọc transcript
- Đề bài chứa từ khóa: "Listen", "nghe", "audio", "recording", "conversation", "dialogue", "speaker"
- Đề bài tham chiếu file MP3 hoặc audio cụ thể
- Phần hướng dẫn đề yêu cầu nghe trước khi trả lời

### Cách tìm transcript
1. Tên transcript = tên file audio (bỏ extension) + `_transcript.md`, nằm trong `exercises/md/` hoặc `lectures/md/`.
   - VD: đề tham chiếu `unit-1-listening.mp3` → tìm `exercises/md/unit-1-listening_transcript.md`
2. Nếu KHÔNG tìm thấy transcript → báo user chạy skill `audio-to-transcript` trước.

### Strategy đọc transcript (tiết kiệm token)
- **Transcript ngắn** (không có file `_transcript_summary.md`) → đọc trực tiếp full transcript.
- **Transcript dài** (có file `_transcript_summary.md`) → đọc summary trước. Chỉ mở full transcript khi cần verify chi tiết câu nói cụ thể.

### Cách tích hợp transcript vào lời giải
- Coi transcript là **"dữ kiện đã cho"** trong phần `🎯 Phân tích đề`.
- Thêm section `🎧 Nội dung Audio (Transcript)` ngay sau `📋 Đề bài` — in NGUYÊN VĂN full transcript.
- Khi trích dẫn đáp án, ghi rõ: "Theo transcript [HH:MM], Speaker X nói: '...'"
- Front-matter solution thêm 2 field:
  ```yaml
  transcript_file: "<tên>_transcript.md"
  audio_file: "<tên>.mp3"
  ```

### Lưu ý
- KHÔNG dịch transcript sang tiếng Việt trong phần `🎧` — giữ nguyên ngôn ngữ gốc.
- Phần giải thích / lời giải vẫn viết bằng tiếng Việt, giữ thuật ngữ gốc trong ngoặc.
- Nếu đề listening có nhiều phần (Part 1, Part 2...) → giải từng phần, trích đúng đoạn transcript liên quan.

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
