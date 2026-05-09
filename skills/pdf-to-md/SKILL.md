---
name: pdf-to-md
description: Biên dịch tài liệu PDF (bài giảng, đề bài, câu hỏi ôn tập chuyên ngành Quản trị Kinh doanh) sang định dạng Markdown sạch, giữ cấu trúc heading, bảng, công thức. BẮT BUỘC kích hoạt skill này khi người dùng đề cập tới việc xử lý/đọc/chuyển đổi/biên dịch file PDF, hoặc khi pipeline học liệu cần MD từ PDF. Có cơ chế cache: nếu file MD tương ứng đã tồn tại và hash gốc khớp thì BỎ QUA biên dịch trừ khi có cờ --force hoặc người dùng yêu cầu rõ "biên dịch lại / ép convert / force / convert lại từ đầu".
---

# Skill: PDF → Markdown converter (có cache)

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

### Bước 4: Ghi file
- Tạo folder `md/` nếu chưa có.
- Ghi file `<tên>.md` với front-matter đầy đủ.
- Doc type: nếu trong path có `lectures/` → `"lecture"`, có `exercises/` → `"exercise"`.

### Bước 5: Verify
- File MD không rỗng (> 200 ký tự với mỗi 5 trang PDF).
- Nếu là đề bài: số `### Câu` ≥ số câu mong đợi.
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

## Báo cáo cho user
```
✅ Convert hoàn tất môn: <slug>
   • Lectures: 5 file (3 mới, 2 cache hit)
   • Exercises: 2 file (1 mới, 1 cache hit)
```
