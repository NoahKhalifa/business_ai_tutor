# Copilot Instructions — Business AI Tutor

> **Quy tắc chung cho mọi agent (bao gồm Copilot) nằm ở [`../AGENTS.md`](../AGENTS.md) — đó là single source of truth.** File này chỉ chứa những gì **khác biệt riêng cho GitHub Copilot Chat**.

## Bắt buộc đọc trước

1. [`../TODO.md`](../TODO.md) — **việc dang dở từ session trước** (lỗi đáp án cần sửa, lời giải cần viết lại, review cần làm lại…). Trước task mới, kiểm tra có mục `pending` nào liên quan môn/chương user đang nhắc tới — nếu có, ưu tiên xử lý hoặc warn user.
2. [`../AGENTS.md`](../AGENTS.md) — TL;DR 60s, routing skill, pipeline 6 stage, quy tắc bất biến, naming convention, cấu trúc project.
3. Skill tương ứng với task user yêu cầu (bảng routing trong AGENTS.md).

Khi hoàn thành task có việc dang dở để lại → cập nhật [`../TODO.md`](../TODO.md). KHÔNG để việc dang dở chỉ tồn tại trong chat session.

Trả lời và viết MD **bằng tiếng Việt**.

## Yêu cầu mode + model

User phải ở **Agent mode** + model **Claude Sonnet 4.6** thì Copilot mới đọc/ghi file và chạy bash được.

- Nếu phát hiện đang ở **Ask mode** mà user yêu cầu xử lý PDF / giải bài → nhắc user chuyển sang Agent mode trước khi tiếp tục.
- Nếu model không phải Claude Sonnet 4.6 → nhắc user đổi (model picker góc phải dưới Copilot Chat panel).

## Settings VS Code nên bật

| Setting | Giá trị | Lý do |
|---|---|---|
| `github.copilot.chat.codeGeneration.useInstructionFiles` | `true` | Copilot tự đọc file `.github/copilot-instructions.md` này (mặc định ON từ 2025) |
| `chat.tools.autoApprove` | có thể bật cho action an toàn (đọc file, list folder) | Giảm prompt approve liên tục |

Giữ **approve thủ công** cho `write_file` và `run_in_terminal` để tránh sửa file ngoài ý muốn.

## Nhắc khi review

Để bước review được khách quan, **mở chat session mới** (nút `+` trên Copilot Chat panel) trước khi gõ lệnh review. Như vậy Claude không bị bias bởi quá trình giải bài trong session trước. Chi tiết rubric: [`../skills/answer-reviewer/SKILL.md`](../skills/answer-reviewer/SKILL.md).

## Token / context

- Claude Sonnet 4.6 context 200K — đủ cho 1 đề + 3-5 bài giảng.
- Nếu môn có >10 lecture dài → tóm tắt trước (lecture `_summary.md`) thay vì load full.
- Cache-first: PDF/audio đã convert thì SKIP, tránh re-spend token. Chi tiết cache trong [`../ARCHITECTURE.md`](../ARCHITECTURE.md).
