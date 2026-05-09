# Project Index

> Đọc file này nếu cần định vị nhanh trong project. ~200 token, rẻ hơn nhiều so với scan folder.

## Skills (đọc khi vào task tương ứng)
- `skills/pdf-to-md/SKILL.md` — convert PDF, có cache, tạo summary
- `skills/exercise-solver/SKILL.md` — giải bài 8 phần
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
- `subjects/Quản trị tài chính/` — Financal management (3 tín chỉ, Khoa QTTC)

## Cấu trúc 1 môn
```
subjects/<slug>/
├── metadata.yaml
├── lectures/{pdf,md}/        ← <tên>.md (đầy đủ) + <tên>_summary.md (tóm tắt)
├── exercises/{pdf,md}/
├── solutions/                ← <tên>_solution.md + <tên>_review.md
└── extensions/               ← <tên>_extended.md
```
