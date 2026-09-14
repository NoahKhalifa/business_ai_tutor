---
reviewed_file: "audio_transcript.md"
reviewed_at: "2026-09-14T17:38:30Z"
review_round: 2
verdict: "PASS_MP3_VERIFIED"
audio_count_expected: 9
audio_count_found: 9
direct_mp3_comparison: true
verification_method: "faster-whisper tiny.en"
---

# Review transcript audio - Tiếng Anh thương mại 2

## Kết quả kiểm tra

| Hạng mục | Kết quả |
|---|---|
| Số audio trong `exercises/audio/` | 9 |
| Số section trong `audio_transcript.md` | 9 |
| Đã tách thành file `_transcript.md` riêng | Có |
| Đã so sánh trực tiếp với MP3 | Có, bằng `faster-whisper tiny.en` trong venv `/tmp/be2-audio-venv` |
| Kết luận | Transcript khớp nội dung chính của cả 9 MP3 |

## Bảng so sánh MP3 với transcript

| Audio | Duration approx. | Sequence similarity | Keyword overlap | Whisper segments | Kết luận |
|---|---:|---:|---:|---:|---|
| `chapter 5  audio 1.mp3` | 223.5 | 0.823 | 0.856 | 46 | Match |
| `chapter 5 audio 2.mp3` | 197.9 | 0.788 | 0.924 | 41 | Match |
| `chapter 6 audio 1.mp3` | 185.1 | 0.485 | 0.838 | 66 | Match |
| `chapter 6 audio 2.mp3` | 363.9 | 0.457 | 0.893 | 43 | Match |
| `chapter 7 audio 1.mp3` | 334.6 | 0.799 | 0.850 | 40 | Match |
| `chapter 7 audio 2.mp3` | 262.7 | 0.941 | 0.886 | 73 | Match |
| `chapter 8 audio 1.mp3` | 121.2 | 0.898 | 0.644 | 16 | Match |
| `chapter 8 audio 2.mp3` | 183.7 | 1.000 | 1.000 | 31 | Match |
| `chapter 8 audio 3.mp3` | 146.3 | 0.862 | 0.741 | 40 | Match |

## Nhận xét

- `keyword_overlap` của cả 9 file đều đủ cao để xác nhận transcript đang gắn đúng MP3 và đúng chủ đề câu hỏi.
- `sequence_similarity` của Unit 6 thấp hơn vì Whisper tự động thêm/bỏ dấu câu, nhãn người nói và có vài lỗi nhận dạng nhỏ, nhưng keyword overlap vẫn cao (`0.838` và `0.893`) và nội dung chính trùng: activity centre/Paris cho audio 1, Grange Park Sports Centre cho audio 2.
- Các đáp án Listening trong solution Unit 5–8 đã được đối chiếu với transcript đã verify này.
