# Project Index

> Đọc file này nếu cần định vị nhanh trong project. ~200 token, rẻ hơn nhiều so với scan folder.

## Skills (đọc khi vào task tương ứng)
- `skills/pdf-to-md/SKILL.md` — convert PDF, có cache, tạo summary
- `skills/audio-to-transcript/SKILL.md` — transcribe MP3 → transcript MD, có cache (chỉ môn có audio)
- `skills/exercise-solver/SKILL.md` — giải bài 8 phần (+🎧 nếu có audio)
- `skills/example-generator/SKILL.md` — ví dụ DN Việt Nam
- `skills/extension-builder/SKILL.md` — bài luyện ★ ★★ ★★★
- `skills/answer-reviewer/SKILL.md` — rubric chấm 5 tiêu chí

## Templates & guides
- `prompts/math-formatting.md` — quy ước công thức LaTeX
- `prompts/solver_template.md` — khung lời giải 8 phần
- `prompts/reviewer_checklist.md` — checklist khi review

## Docs
- `README.md` — hướng dẫn cho user
- `ARCHITECTURE.md` — sơ đồ luồng + rubric chi tiết

## Subjects hiện có
- `subjects/Khởi nghiệp/` — Start up (3 tín chỉ, Khoa Khởi sự kinh doanh)
- `subjects/Quản trị chiến lược/` — Quản trị Chiến lược (3 tín chỉ, Khoa QTKD)
- `subjects/Quản trị tài chính/` — Financial management (3 tín chỉ, Khoa QTTC)
- `subjects/Tiếng Anh/` — Tiếng Anh (có audio listening, `media_types: ["audio"]`)

## Cấu trúc 1 môn
```
subjects/<slug>/
├── metadata.yaml
├── lectures/{pdf,md}/        ← <tên>.md (đầy đủ) + <tên>_summary.md (tóm tắt)
├── lectures/audio/          ← (tùy chọn) MP3 bài giảng — chỉ khi metadata có media_types: [audio]
├── exercises/{pdf,md}/
├── exercises/audio/         ← (tùy chọn) MP3 đề listening
├── solutions/                ← <tên>_solution.md + <tên>_review.md
└── extensions/               ← <tên>_extended.md
```
