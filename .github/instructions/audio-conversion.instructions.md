---
description: "Khi user xử lý file trong subjects/*/lectures/audio/ hoặc exercises/audio/"
applyTo: "subjects/**/{lectures,exercises}/audio/**"
---

# Pointer: Audio Conversion Context

Khi user thao tác trong folder audio và yêu cầu transcribe/chuyển đổi:
- **Đọc trước**: [`skills/audio-to-transcript/SKILL.md`](../../skills/audio-to-transcript/SKILL.md)
- **Cache rule**: SHA-256 của audio phải khớp `source_hash` trong front-matter transcript MD → skip nếu khớp
- **Metadata gate**: Chỉ chạy khi `metadata.yaml` của môn có `media_types` chứa `"audio"`
- **Transcript summary**: Chỉ tạo `_transcript_summary.md` khi transcript > 2000 token (~5 phút)
- **Nguyên tắc**: KHÔNG tóm tắt, KHÔNG dịch, KHÔNG sửa nội dung audio gốc
