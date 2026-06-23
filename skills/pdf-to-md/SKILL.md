---
name: pdf-to-md
description: Biên dịch tài liệu PDF (bài giảng, đề bài, câu hỏi ôn tập chuyên ngành Quản trị Kinh doanh) sang định dạng Markdown sạch, giữ cấu trúc heading, bảng, công thức. BẮT BUỘC kích hoạt skill này khi người dùng đề cập tới việc xử lý/đọc/chuyển đổi/biên dịch file PDF, hoặc khi pipeline học liệu cần MD từ PDF. Có cơ chế cache: nếu file MD tương ứng đã tồn tại và hash gốc khớp thì BỎ QUA biên dịch trừ khi có cờ --force hoặc người dùng yêu cầu rõ "biên dịch lại / ép convert / force / convert lại từ đầu".
---

# Skill: PDF → Markdown converter (có cache)

> ⚡ **ƯU TIÊN dùng local Python CLI trước** — xem [`skills/pdf-extract-cli/SKILL.md`](../pdf-extract-cli/SKILL.md). Tool ở `tools/pdf_extract/` extract text/tables/images/math hoàn toàn local, không tốn token LLM. Skill này (`pdf-to-md`) chỉ dùng làm **fallback** khi:
> - CLI tool báo lỗi sau 2 lần thử
> - PDF là scan (không có text layer) — tool extract sẽ rỗng
> - Cần phân tích sâu nội dung trong quá trình convert (vd hiệu chỉnh OCR phức tạp)
> - Cần tạo summary cho lecture (stage cuối skill này, sau khi đã có MD đầy đủ)

## Mục tiêu
Chuyển PDF học liệu (bài giảng, slide, đề kiểm tra, câu hỏi ôn tập) sang Markdown sạch, dễ đọc cho cả người và LLM ở các bước sau (solver, reviewer).

## Khi nào trigger
- User nói: "chuyển PDF này sang MD", "đọc tài liệu pdf", "biên dịch slide", "convert đề thi", "extract bài giảng".
- Pipeline tự động khi phát hiện PDF mới trong `subjects/*/lectures/pdf/` hoặc `exercises/pdf/` chưa có MD tương ứng.
- User yêu cầu "biên dịch lại" → bỏ qua cache.

## Quy tắc cache (QUAN TRỌNG)

### Bước kiểm tra cache
1. Với mỗi PDF cần xử lý, dùng tool có sẵn để tính SHA-256:
   ```bash
   sha256sum subjects/<môn>/lectures/pdf/<file>.pdf
   ```
2. Tên MD output = tên PDF + `.md` (đặt trong folder `md/` cùng cấp với folder `pdf/`).
3. Nếu MD đã tồn tại:
   - Đọc front-matter YAML đầu file MD để lấy `source_hash`.
   - So với hash vừa tính.
   - **Khớp** → SKIP, log "cached".
   - **Khác** → biên dịch lại, ghi đè.
4. Nếu user nói "force"/"convert lại"/"biên dịch lại từ đầu" → luôn biên dịch lại.

### Báo lại với user
- Sau khi xử lý xong, báo tóm tắt: "X file đã convert mới, Y file dùng cache".
- Không cần báo từng file một nếu nhiều — chỉ cần tổng kết.

## Format MD output (BẮT BUỘC)
Mỗi file MD phải bắt đầu bằng front-matter:

```yaml
---
source_pdf: "ten-file-goc.pdf"
source_hash: "sha256:abc123..."
converted_at: "2026-05-09T10:30:00Z"
subject: "quan-tri-chien-luoc"
doc_type: "lecture"   # hoặc "exercise"
pages: 42
---
```

Sau front-matter là nội dung MD theo nguyên tắc:
- `# H1` cho tên chương/bài giảng.
- `## H2` cho mục lớn, `### H3` cho mục con.
- Giữ nguyên **bảng** dưới dạng Markdown table.
- Giữ nguyên **công thức** trong `$...$` hoặc `$$...$$`.
- Giữ chú thích ảnh dưới dạng `> Ảnh: mô tả`.
- Đánh số câu hỏi rõ ràng nếu là đề: `### Câu 1`, `### Câu 2`...

## Quy trình thực hiện

### Bước 0: Thử CLI tool trước (token-saving)

```powershell
python -m tools.pdf_extract "<đường-dẫn-pdf>" -o "<thư-mục-md>"
```

Nếu thành công và MD output trông hợp lý → STOP. Chuyển sang Bước 5 (Verify) và optionally Bước summary (cho lecture). KHÔNG chạy các bước dưới đây.

Nếu fail (exit code ≠ 0, MD rỗng, hoặc PDF là scan) → tiếp tục các bước 1-4 dưới đây (đọc bằng Claude).

### Bước 1: Inspect PDF
- Dùng tool có sẵn (read PDF, view, hoặc bash với `pdfinfo`) để kiểm tra:
  - Số trang
  - Có phải PDF text hay PDF scan?
- Nếu là PDF scan → cần đọc bằng vision (Claude tự render trang thành ảnh khi cần).

### Bước 2: Đọc nội dung PDF
- Dùng tool đọc PDF của IDE để lấy text/ảnh từng trang.
- Với PDF dài (>30 trang), xử lý theo từng đoạn 10-20 trang để giữ chất lượng.

### Bước 3: Format thành Markdown
1. Giữ nguyên cấu trúc phân cấp tiêu đề.
2. Bảng → Markdown table chuẩn.
3. Công thức → LaTeX trong `$...$` hoặc `$$...$$`.
4. KHÔNG tóm tắt, KHÔNG bỏ nội dung. Chuyển đầy đủ.
5. Sửa lỗi OCR rõ ràng nhưng KHÔNG đổi nội dung gốc.
6. Nếu là đề bài → đánh số "### Câu N" rõ ràng, mỗi câu là 1 block.
7. Loại bỏ header/footer template lặp đi lặp lại.

### Bước 3.1: Cảnh báo OCR confusables tiếng Việt (BẮT BUỘC với PDF tiếng Việt)

OCR engine tiếng Anh — mặc định trên hầu hết PDF VN — thường nhầm dấu thanh tiếng Việt. Các cặp confusable đã ghi nhận lỗi thực tế trong project:

| Cặp confusable | Ví dụ ngữ cảnh | Lỗi đã thấy |
|---|---|---|
| **vi / vĩ** | "môi trường **vi** mô" vs "môi trường **vĩ** mô" | QT Marketing Ch3 Q29, Q20 (đáp án sai vì OCR nhầm) |
| **sỉ / sĩ** | "bán **sỉ**" (wholesale) vs "**sĩ** diện" | |
| **lý / ly** | "**lý** thuyết" vs "**ly** hôn" / "**ly** giác" | |
| **lỗ / lô** | "cổ phiếu **lỗ**" / "**lỗ** hổng" vs "**lô** đất" / "**lô** hàng" | |
| **hoàn / hoàng** | "**hoàn** thành" / "**hoàn** vốn" vs "**hoàng** gia" | |
| **nhặt / nhật** | "**nhặt** rác" vs "**nhật** ký" / "**nhật** trình" | |
| **chỉ / chí** | "**chỉ** số" / "**chỉ** tiêu" vs "**chí** hướng" / "**chí** lý" | |
| **sản / sàn** | "**sản** xuất" / "**sản** phẩm" vs "**sàn** giao dịch" | |
| **mã / mả** | "**mã** số" / "**mã** hóa" vs "**mả** mẹ" | |

**Quy tắc khi convert PDF có khả năng chứa confusable:**

1. Sau khi OCR/extract text, scan kết quả tìm các từ trong danh sách trên.
2. Nếu gặp từ confusable trong **đề bài trắc nghiệm** (đặc biệt câu hỏi và 4 phương án A/B/C/D) → **chèn flag inline ngay sau từ**:
   `[VERIFY_OCR: vi/vĩ — check PDF trang N]`
3. **KHÔNG tự ý sửa** "vi" thành "vĩ" hay ngược lại nếu không chắc — chỉ flag, để skill `exercise-solver` verify với PDF gốc khi giải.
4. Trong front-matter, thêm field `confusables_flagged: <số lượng>` để solver biết bài này cần verify.
5. **Tín hiệu nghi vấn cao**: 2 phương án A/B/C/D trong cùng 1 câu có chữ giống hệt nhau (vd cả A và C đều "vi mô") → gần như chắc chắn OCR nhầm 1 trong 2.

Ví dụ output sau khi flag:
```markdown
### Câu 29
"... yếu tố nào KHÔNG thuộc môi trường vi mô [VERIFY_OCR: vi/vĩ — check PDF trang 15]?"
- **A.** Đối thủ cạnh tranh
- **B.** Khách hàng
- **C.** Tỷ giá hối đoái
- **D.** Nhà cung cấp
```

### Bước 4: Ghi file
- Tạo folder `md/` nếu chưa có.
- Ghi file `<tên>.md` với front-matter đầy đủ.
- Doc type: nếu trong path có `lectures/` → `"lecture"`, có `exercises/` → `"exercise"`.

### Bước 5: Verify
- File MD không rỗng (> 200 ký tự với mỗi 5 trang PDF).
- Nếu là đề bài: số `### Câu` ≥ số câu mong đợi.
- **Scan confusables** (vi/vĩ, sỉ/sĩ, lý/ly, lỗ/lô, hoàn/hoàng, nhặt/nhật, chỉ/chí, sản/sàn, mã/mả): nếu có và chưa có flag `[VERIFY_OCR]` → thêm flag.
- **Kiểm tra trùng phương án** (chỉ áp dụng cho đề **MCQ = Multiple Choice Question = trắc nghiệm 4 lựa chọn**): nếu trong cùng 1 câu MCQ có 2+ phương án A/B/C/D với nội dung giống hệt → flag `[VERIFY_OCR: phương án trùng, có thể nhầm dấu]`.
- Lỗi → thử lại lần 2, sau đó báo user.

## Edge cases
- **PDF khóa mật khẩu** → báo lỗi rõ, dừng. Hỏi user mật khẩu.
- **PDF chỉ có ảnh** → đọc bằng vision, ghi chú trong front-matter `ocr_used: true`.
- **PDF tiếng Anh xen tiếng Việt** → giữ nguyên cả hai, KHÔNG tự dịch.
- **PDF có watermark** → cố gắng filter bằng regex hậu xử lý.
- **PDF quá lớn (>100MB hoặc >300 trang)** → báo user, đề xuất chia nhỏ thủ công.

## Output mẫu

```markdown
---
source_pdf: "bai-1-tong-quan-quan-tri-chien-luoc.pdf"
source_hash: "sha256:7d3f9e2a4b1c8d..."
converted_at: "2026-05-09T10:30:00Z"
subject: "quan-tri-chien-luoc"
doc_type: "lecture"
pages: 28
---

# Bài 1: Tổng quan Quản trị Chiến lược

## 1.1 Khái niệm chiến lược

Chiến lược là tập hợp các quyết định dài hạn...

### 1.1.1 Định nghĩa của Michael Porter
> "Chiến lược là sự lựa chọn các hoạt động khác biệt để mang lại giá trị độc đáo."

## 1.2 Mô hình 5 áp lực cạnh tranh

| Áp lực | Mô tả |
|---|---|
| Đối thủ hiện tại | Cạnh tranh trực tiếp về giá, sản phẩm |
| Đối thủ tiềm ẩn | Rào cản gia nhập ngành |
```
## 📌 Stage bổ sung: Tạo bản tóm tắt cho LECTURE

> Chỉ áp dụng với `doc_type: "lecture"`. Không tạo summary cho exercise.

### Khi nào tạo summary
- **Tự động**: ngay sau khi convert thành công 1 file lecture PDF → MD đầy đủ.
- **Chỉ khi đó là lecture**: file trong `subjects/*/lectures/pdf/`, không áp dụng cho `exercises/`.
- **Cache-aware**: nếu `<tên>_summary.md` đã tồn tại VÀ `source_hash` của nó khớp với hash PDF gốc → SKIP.
- **Force**: user nói "tóm tắt lại" / "regenerate summary" / "force" → tạo lại.

### Quy ước đặt tên & vị trí
Hậu tố `_summary.md` cố định, để Copilot và user dễ phân biệt.

### Format file summary

```markdown
---
source_pdf: "bai-1-tong-quan.pdf"
source_hash: "sha256:<hash của PDF gốc, KHÔNG phải hash của file md đầy đủ>"
parent_md: "bai-1-tong-quan.md"
summary_of: "lecture"
created_at: "2026-05-09T..."
subject: "quan-tri-chien-luoc"
---

# Tóm tắt: [Tên bài giảng]

> Bản tóm tắt cô đọng phục vụ ôn thi & tra cứu nhanh. Đọc bản đầy đủ tại [bai-1-tong-quan.md](./bai-1-tong-quan.md).

## 🎯 Mục tiêu bài học
- [3-5 mục tiêu chính, lấy từ phần đầu bài giảng]

## 📚 Kiến thức cốt lõi cần nắm

### 1. [Khái niệm chính 1]
- **Định nghĩa**: [1-2 câu]
- **Bản chất**: [Hiểu sâu thêm 1-2 câu]
- **Vì sao quan trọng**: [1 câu]

### 2. [Khái niệm chính 2]
...

(Chỉ liệt kê 5-10 khái niệm CỐT LÕI nhất, không phải mọi khái niệm trong bài. Dùng tiêu chí: cái này thi sẽ hỏi.)

## 🧮 Công thức cần thuộc

| STT | Công thức | Ý nghĩa | Khi nào dùng |
|---|---|---|---|
| 1 | $BEP = \dfrac{FC}{P - VC}$ | Điểm hòa vốn theo sản lượng | Khi cần biết bán bao nhiêu để hết lỗ |
| 2 | $NPV = \sum_{t=0}^{n} \dfrac{CF_t}{(1+r)^t}$ | Giá trị hiện tại ròng | Đánh giá dự án đầu tư |
| ... | ... | ... | ... |

(Nếu bài giảng KHÔNG có công thức → ghi "Bài này không có công thức tính toán; tập trung vào khái niệm và mô hình định tính." và bỏ bảng này.)

## 🗺️ Mô hình / Khung phân tích chính

(Chỉ liệt kê mô hình QUAN TRỌNG: 5 Forces, SWOT, BCG, 4P, McKinsey 7S, Porter Diamond, v.v.)

### [Tên mô hình 1]
- **Mục đích**: ...
- **Các thành phần**: [bullet ngắn]
- **Cách áp dụng**: [1-2 câu]

## 🔑 Thuật ngữ quan trọng (mini-glossary)

| Thuật ngữ Việt | Tiếng Anh | Định nghĩa ngắn |
|---|---|---|
| Lợi thế cạnh tranh | Competitive advantage | ... |
| Chuỗi giá trị | Value chain | ... |
| ... | ... | ... |

## ⚡ Câu hỏi tự kiểm tra nhanh
1. [Câu hỏi 1 — kiểm tra hiểu khái niệm]
2. [Câu hỏi 2 — kiểm tra áp dụng công thức]
3. [Câu hỏi 3 — kiểm tra phân biệt khái niệm gần nhau]

## 🔗 Liên kết
- **Bài giảng đầy đủ**: [bai-1-tong-quan.md](./bai-1-tong-quan.md)
- **Bài tiếp theo cần học**: [bai-2-...](./bai-2-...md) (nếu có trong `metadata.yaml`)
- **Liên quan tới bài tập**: [đề ôn tập tương ứng] (nếu đã có trong `exercises/md/`)
```

### Quy tắc viết summary

1. **Cô đọng nhưng đủ**: target ~1/4 đến 1/5 độ dài bản đầy đủ. Sinh viên đọc summary trong 10-15 phút phải nắm được khung kiến thức.
2. **Lấy từ bản MD đầy đủ, không từ PDF**: tiết kiệm token và đảm bảo nhất quán.
3. **Bám sát nội dung gốc**: KHÔNG bịa khái niệm/công thức không có trong bài giảng.
4. **Công thức phải đúng định dạng LaTeX** trong `$...$` hoặc `$$...$$`.
5. **Bảng glossary**: chỉ thuật ngữ thực sự xuất hiện trong bài, không tự thêm thuật ngữ ngoài.
6. **Câu hỏi tự kiểm tra**: 3-5 câu, mở (không yes/no), trả lời được sau khi đọc summary.
7. **Nếu bài giảng quá ngắn** (< 5 trang) → vẫn tạo summary nhưng có thể bỏ qua một số mục (vd: không có công thức).

### Quy trình thực hiện
1. Sau khi convert xong <tên>.md (đầy đủ):
2. Kiểm tra file <tên>_summary.md đã tồn tại chưa
→ Nếu có và source_hash khớp → SKIP
3. Đọc <tên>.md (bản đầy đủ)
4. Tạo <tên>_summary.md theo format trên
5. Front-matter: source_hash COPY từ file <tên>.md (cùng PDF gốc)
6. Báo user: "Đã tạo summary cho bai-1-tong-quan"
## Báo cáo cho user
```
✅ Convert hoàn tất môn: <slug>
• Lectures: 5 file (3 mới, 2 cache hit)
- Trong đó 5 file đã có summary (3 mới tạo, 2 cache hit)
• Exercises: 2 file (1 mới, 1 cache hit) — không tạo summary
```
