---
name: audio-to-transcript
description: Chuyển file audio (MP3, WAV, M4A) thành transcript Markdown sạch, phục vụ các bước giải bài listening/phát âm. BẮT BUỘC kích hoạt skill này khi người dùng đề cập tới việc xử lý/transcribe file audio, hoặc khi pipeline phát hiện file audio mới trong môn có `media_types: [audio]` trong metadata.yaml. Có cơ chế cache: nếu file transcript tương ứng đã tồn tại và hash gốc khớp thì BỎ QUA trừ khi có cờ --force hoặc người dùng yêu cầu rõ "transcribe lại / force".
---

# Skill: Audio → Transcript converter (có cache)

## Mục tiêu
Chuyển file audio (listening exercises, bài giảng có audio) sang Markdown transcript sạch, giữ nguyên nội dung lời nói, phân biệt speaker, đánh dấu timestamp. Transcript này là input cho exercise-solver khi giải bài listening.

## Khi nào trigger
- User nói: "transcribe audio này", "chuyển MP3 sang text", "nghe audio", "xử lý file nghe".
- Pipeline tự động khi phát hiện file audio mới trong `subjects/*/exercises/audio/` hoặc `lectures/audio/` của môn có `media_types: [audio]` trong `metadata.yaml`.
- User yêu cầu "transcribe lại" → bỏ qua cache.

## Điều kiện tiên quyết
- Môn học PHẢI có `media_types` chứa `"audio"` trong `metadata.yaml`.
- Nếu môn KHÔNG có cờ này → KHÔNG chạy skill, báo user thêm cờ vào metadata.
- Tool transcription: **OpenAI Whisper** (chạy local). Nếu chưa cài → hướng dẫn user:
  ```bash
  pip install openai-whisper
  ```

## Quy tắc cache (QUAN TRỌNG — mirror từ pdf-to-md)

### Bước kiểm tra cache
1. Với mỗi file audio cần xử lý, tính SHA-256:
   ```bash
   sha256sum subjects/<môn>/exercises/audio/<file>.mp3
   ```
2. Tên transcript output = tên audio (bỏ extension) + `_transcript.md` (đặt trong folder `md/` cùng cấp).
   - VD: `exercises/audio/unit-1-listening.mp3` → `exercises/md/unit-1-listening_transcript.md`
3. Nếu transcript đã tồn tại:
   - Đọc front-matter YAML → lấy `source_hash`.
   - So với hash vừa tính.
   - **Khớp** → SKIP, log "cached".
   - **Khác** → transcribe lại, ghi đè.
4. Nếu user nói "force"/"transcribe lại" → luôn transcribe lại.

### Báo lại với user
- Tóm tắt: "X file đã transcribe mới, Y file dùng cache".

## Quy trình thực hiện

### Bước 1: Quét audio
- Liệt kê tất cả file trong `exercises/audio/` và `lectures/audio/`.
- Lọc theo extension: `.mp3`, `.wav`, `.m4a`, `.ogg`, `.flac`.
- Kiểm tra cache từng file.

### Bước 2: Transcribe bằng Whisper
- Đọc `audio_language` từ `metadata.yaml` (mặc định: `en` nếu không có).
- Chạy lệnh:
  ```bash
  whisper "<đường_dẫn_file_audio>" --language <audio_language> --output_format txt --output_dir "<thư_mục_tạm>"
  ```
- Whisper model mặc định: `medium` (cân bằng chất lượng/tốc độ). User có thể override bằng flag `--model large-v3` nếu cần chất lượng cao hơn.
- Đọc output text từ file `.txt` mà Whisper tạo ra.

### Bước 3: Format thành Markdown transcript
1. Giữ NGUYÊN NỘI DUNG lời nói — KHÔNG tóm tắt, KHÔNG chỉnh sửa ngữ pháp.
2. Phân biệt speaker nếu có thể nhận diện (Speaker 1, Speaker 2, hoặc tên nếu được giới thiệu trong audio).
3. Thêm timestamp mỗi ~30 giây hoặc khi đổi speaker.
4. Sửa lỗi nhận dạng rõ ràng (VD: "I want to buy a car" bị nhận thành "I want to buy a card" khi context rõ ràng).
5. Giữ nguyên ngôn ngữ gốc (KHÔNG dịch).

### Bước 4: Ghi file transcript

#### Front-matter bắt buộc
```yaml
---
source_audio: "unit-1-listening.mp3"
source_hash: "sha256:abc123..."
transcribed_at: "2026-05-10T14:00:00Z"
subject: "tieng-anh"
doc_type: "transcript"
language: "en"
duration_seconds: 180
---
```

#### Nội dung transcript
```markdown
# Transcript: [Tên file / Tiêu đề bài]

🎧 **Audio**: [tên-file.mp3] | ⏱️ [M:SS]

---

## Full Text

**[00:00] Speaker 1**: Good morning, can I help you?

**[00:03] Speaker 2**: Yes, I'd like to open a bank account, please.

**[00:07] Speaker 1**: Certainly. Do you have any identification with you?

...
```

### Bước 5: Tạo transcript summary (có điều kiện)

> **CHỈ tạo `_transcript_summary.md` khi transcript > 2000 token (~5 phút audio).**
> Transcript ngắn (1-3 phút) → solver đọc trực tiếp full transcript, không cần summary.

Nếu cần tạo summary:
- File: `<tên>_transcript_summary.md` cùng folder `md/`
- Nội dung (~300-500 token):
  ```markdown
  ---
  source_transcript: "unit-5-lecture_transcript.md"
  doc_type: "transcript_summary"
  ---

  # Summary: [Tên file]

  ## Thông tin chung
  - **Thời lượng**: M:SS
  - **Số speaker**: N
  - **Ngôn ngữ**: English
  - **Chủ đề chính**: [1-2 câu]

  ## Nội dung chính
  - [Ý chính 1]
  - [Ý chính 2]
  - [Ý chính 3]

  ## Từ vựng / thuật ngữ quan trọng
  - [term 1] — [nghĩa ngắn]
  - [term 2] — [nghĩa ngắn]

  ## Ghi chú cho solver
  - [Điểm cần lưu ý khi giải bài dựa trên audio này]
  ```

### Bước 6: Ghi file
- Tạo folder `md/` nếu chưa có.
- Ghi transcript (+ summary nếu có) với front-matter đầy đủ.

## Quy tắc bất biến
1. **KHÔNG tóm tắt, KHÔNG sửa nội dung audio gốc** — transcript phải nguyên văn.
2. **KHÔNG dịch** — giữ nguyên ngôn ngữ gốc của audio.
3. **Cache-first** — đã có transcript + hash khớp → SKIP.
4. **Metadata gate** — chỉ chạy cho môn có `media_types: [audio]`.

## Khi nào dùng skill khác
- Sau khi transcribe xong → CHUYỂN sang skill `pdf-to-md` cho các file PDF cùng môn (nếu có).
- Transcript là input cho `exercise-solver` ở bước tiếp theo.

## Edge cases
- **Audio chất lượng kém** → ghi chú trong transcript: `[không rõ / inaudible]` tại vị trí không nghe rõ.
- **Audio có nhạc nền / tiếng ồn** → Whisper vẫn xử lý được, nhưng ghi chú `[music]` hoặc `[background noise]` nếu cần.
- **Audio nhiều ngôn ngữ** (code-switching) → dùng `--language` cho ngôn ngữ chính, Whisper sẽ tự nhận diện phần còn lại.
- **File audio rất dài (>30 phút)** → chia transcript thành sections theo chủ đề, mỗi section có timestamp range.
- **Whisper chưa cài** → báo user cài Whisper, KHÔNG dùng tool thay thế mà không hỏi user.
