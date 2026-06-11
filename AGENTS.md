# AGENTS.md — Hướng dẫn canonical cho mọi coding agent

> **Single source of truth** cho mọi AI agent làm việc trong repo này: Codex, Claude Code, Cursor, Aider, GitHub Copilot. `README.md` thiên về user, `.github/copilot-instructions.md` chỉ chứa khác biệt riêng cho Copilot — cả hai đều trỏ về file này cho phần "agent rules" chung.

Project này là **Business AI Tutor**: hệ thống học liệu AI hỗ trợ sinh viên ngành Quản trị Kinh doanh. Khi làm việc trong repo này, agent phải ưu tiên tiếng Việt, bám sát bài giảng trong `subjects/<môn>/lectures/md/`, và ghi output Markdown đúng cấu trúc của project.

---

## ⚡ TL;DR — Đọc trong 60 giây

0. **Đọc [`TODO.md`](TODO.md) đầu tiên**: file này liệt kê việc dang dở từ session trước (lỗi đáp án cần sửa, lời giải cần viết lại, review cần làm lại…). Trước khi bắt đầu task mới, kiểm tra xem có mục `pending` nào liên quan đến môn/chương user đang nhắc tới không — nếu có, ưu tiên xử lý hoặc ít nhất warn user.
1. **Trước khi bắt tay**: tra bảng [Routing theo yêu cầu](#routing-theo-yêu-cầu) → đọc skill tương ứng trong `skills/<tên>/SKILL.md`. Đừng đoán workflow.
2. **Pipeline mặc định khi user nói "Giải đề X"**: audio→transcript *(nếu môn có audio)* → pdf→md → solver → example → extension → reviewer. Chi tiết: [Pipeline mặc định](#pipeline-mặc-định-khi-user-nói-giải-đề-x).
3. **Cache-first**: nếu PDF/audio đã có MD/transcript và `source_hash` khớp thì SKIP, trừ khi user yêu cầu force.
4. **Tiếng Việt** là ngôn ngữ chính. Công thức toán dùng LaTeX (`$...$` / `$$...$$`).
5. **Front-matter YAML bắt buộc** ở đầu mọi MD sinh ra (format trong skill tương ứng).
6. **Không bịa** số liệu doanh nghiệp Việt Nam (doanh thu, lợi nhuận cụ thể). Chỉ dùng thông tin công khai.
7. **Reviewer độc lập**: tự giải lại trong đầu trước khi đọc lời giải có sẵn. Pass khi tổng ≥ 8.0/10 VÀ không tiêu chí nào < 6.0/10.
8. **Kiểm tra trạng thái nhanh**: chạy `pwsh scripts/check-project.ps1` để biết môn nào đang thiếu gì. Đọc `subjects/<môn>/STATUS.md` (auto-gen) cho snapshot từng môn.
9. **Không tự ý** commit/push, đổi tên folder/file đã có, hoặc revert thay đổi nằm ngoài phạm vi task.

Đọc đến đây, agent đã đủ context để xử lý 80% yêu cầu thông thường. Các phần dưới là chi tiết khi cần.

## Nguyên tắc cốt lõi

1. **Đọc skill đúng task trước khi làm**. Không tự đoán workflow nếu đã có skill tương ứng trong `skills/`.
2. **Cache-first**. Nếu PDF/audio đã có MD/transcript tương ứng và hash khớp thì bỏ qua convert/transcribe, trừ khi user yêu cầu force/convert lại/transcribe lại.
3. **Tiếng Việt là ngôn ngữ chính** cho trao đổi, lời giải, review, extension và ghi chú học tập.
4. **Không bịa số liệu doanh nghiệp Việt Nam**. Nếu cần số liệu mới, phải kiểm chứng nguồn công khai hoặc viết theo hướng định tính.
5. **Front matter YAML bắt buộc** ở đầu mọi file Markdown sinh ra.
6. **Công thức toán dùng LaTeX** trong `$...$` hoặc `$$...$$`, theo `prompts/math-formatting.md`.
7. **Không sửa/xóa thay đổi ngoài phạm vi task**. Repo có thể đang dirty; giữ nguyên thay đổi của user.

## Routing theo yêu cầu

Đọc file này trước khi bắt tay vào task tương ứng:

| User yêu cầu | File cần đọc |
|---|---|
| Convert PDF, đọc PDF, biên dịch slide/de bài | `skills/pdf-to-md/SKILL.md` |
| Transcribe audio, MP3, bài nghe | `skills/audio-to-transcript/SKILL.md` |
| Giải bài tập, hướng dẫn giải, phân tích case | `skills/exercise-solver/SKILL.md` |
| Thêm ví dụ thực tế, doanh nghiệp Việt Nam | `skills/example-generator/SKILL.md` |
| Bài luyện thêm, mở rộng, ôn thi | `skills/extension-builder/SKILL.md` |
| Review, chấm điểm, kiểm tra lời giải | `skills/answer-reviewer/SKILL.md` |
| Công thức toán | `prompts/math-formatting.md` |
| Template lời giải | `prompts/solver_template.md` |
| Checklist review | `prompts/reviewer_checklist.md` |
| Sơ đồ pipeline và cache | `ARCHITECTURE.md` |
| Định vị nhanh project | `INDEX.md` |
| Việc dang dở / handoff giữa các session | `TODO.md` |

## Pipeline mặc định khi user nói "Giải đề X"

Chạy theo thứ tự dưới đây, trừ khi user yêu cầu chỉ làm một phần:

1. **Audio to transcript**: chỉ khi `metadata.yaml` của môn có `media_types: ["audio"]`.
2. **PDF to Markdown**: convert PDF sang `exercises/md/` hoặc `lectures/md/`; tạo summary cho lecture.
3. **Exercise solver**: giải đề, lưu `solutions/<ten-de>_solution.md`.
4. **Example generator**: thêm ví dụ thực tế, ưu tiên doanh nghiệp Việt Nam.
5. **Extension builder**: tạo `extensions/<ten-de>_extended.md`.
6. **Answer reviewer**: review độc lập, lưu `solutions/<ten-de>_review.md`; nếu chưa đạt thì sửa tối đa 3 vòng.

Nếu user chỉ yêu cầu "giải nhanh trắc nghiệm", có thể dùng format bảng đáp án + giải thích ngắn, nhưng vẫn phải bám bài giảng và ghi rõ đây là bản draft nếu chưa review đầy đủ.

## Cấu trúc project

```text
business_ai_tutor/
├── AGENTS.md                          # ← canonical agent rules (file này)
├── README.md                          # ← user-facing setup + chat commands
├── ARCHITECTURE.md                    # ← sơ đồ pipeline + rubric chi tiết
├── INDEX.md                           # ← bản đồ subject + skill
├── .github/
│   └── copilot-instructions.md        # ← chỉ khác biệt riêng cho Copilot
├── prompts/
│   ├── math-formatting.md
│   ├── solver_template.md
│   └── reviewer_checklist.md
├── scripts/
│   └── check-project.ps1              # ← audit project, sinh STATUS.md
├── skills/
│   ├── pdf-to-md/SKILL.md
│   ├── audio-to-transcript/SKILL.md
│   ├── exercise-solver/SKILL.md
│   ├── example-generator/SKILL.md
│   ├── extension-builder/SKILL.md
│   └── answer-reviewer/SKILL.md
└── subjects/<môn>/
    ├── metadata.yaml
    ├── STATUS.md                      # ← auto-gen bởi check-project.ps1, KHÔNG sửa tay
    ├── lectures/{pdf,md}/
    ├── lectures/audio/                # tùy chọn (chỉ môn có media_types: ["audio"])
    ├── exercises/{pdf,md}/
    ├── exercises/audio/               # tùy chọn
    ├── solutions/
    └── extensions/
```

Tên folder môn có thể là tiếng Việt Unicode hoặc tiếng Anh. Không tự đổi tên folder/file đã có nếu user không yêu cầu.

## Naming convention

Quy ước này áp dụng cho **môn mới**. Môn cũ giữ nguyên (đổi tên = phá hash cache + git history + reference trong front-matter).

| Vị trí | Quy ước | Ví dụ |
|---|---|---|
| Folder môn (`subjects/<…>/`) | Tên dễ đọc, có thể tiếng Việt Unicode hoặc tiếng Anh | `Quản trị chiến lược`, `Quản trị marketing` |
| `subject_code` trong `metadata.yaml` | Mã môn của trường (nếu có), uppercase ASCII | `CNXHKH`, `TXBLOG3041` |
| `subject` slug trong front-matter MD | ASCII kebab-case, bỏ dấu | `quan-tri-chien-luoc`, `marketing-management` |
| File output (`_solution.md`, `_review.md`, `_extended.md`) | ASCII kebab-case slug + suffix | `mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-1_solution.md` |
| File MD convert từ PDF | Giữ nguyên tên gốc của PDF, chỉ đổi extension | PDF `Chương 1.pdf` → MD `Chương 1.md` |
| Front-matter `exercise_file` | Tên file MD trong `exercises/md/`, **không phải PDF** | `Chương 1.md`, không phải `Chương 1.pdf` |

Để verify convention tự động: `pwsh scripts/check-project.ps1` sẽ flag các `exercise_file` trỏ vào file không tồn tại.

## Kiểm tra trạng thái project

Khi user hỏi "môn này còn thiếu gì?" hoặc "project đang ở trạng thái nào?", **đừng scan thủ công** — chạy script:

```powershell
pwsh scripts/check-project.ps1                    # audit toàn project, in báo cáo
pwsh scripts/check-project.ps1 -Subject "<tên>"   # audit 1 môn
pwsh scripts/check-project.ps1 -WriteStatus       # đè STATUS.md cho mỗi môn
```

Script kiểm tra: metadata.yaml, folder bắt buộc, PDF chưa có MD, solution chưa review/extension, `exercise_file` trỏ về file không tồn tại. Exit code 1 nếu có issues, 0 nếu sạch.

**Khi đọc `subjects/<môn>/STATUS.md`**: file này auto-gen, có thể stale nếu chưa chạy lại script sau khi thêm file. Khi cần snapshot mới, chạy lại `-WriteStatus`. **KHÔNG sửa STATUS.md bằng tay** — sửa sẽ bị đè ngay lần chạy tiếp theo.

## Quy ước file sinh ra

### Markdown convert từ PDF

Output đặt ở folder `md/` cùng cấp với folder `pdf/`.

```yaml
---
source_pdf: "ten-file-goc.pdf"
source_hash: "sha256:<hash>"
converted_at: "YYYY-MM-DDTHH:MM:SSZ"
subject: "<slug-mon>"
doc_type: "lecture" # hoặc "exercise"
pages: 42
---
```

Với lecture, tạo thêm `<ten>_summary.md` nếu phù hợp.

### Transcript audio

Transcript đặt ở `lectures/md/` hoặc `exercises/md/`, tên `<ten-audio>_transcript.md`.

```yaml
---
source_audio: "unit-1-listening.mp3"
source_hash: "sha256:<hash>"
transcribed_at: "YYYY-MM-DDTHH:MM:SSZ"
subject: "<slug-mon>"
doc_type: "transcript"
language: "en"
duration_seconds: 180
---
```

Transcript phải giữ nguyên ngôn ngữ gốc, không dịch, không tóm tắt. Nếu dài hơn khoảng 2000 token thì tạo thêm `_transcript_summary.md`.

### Solution

Solution đặt ở `subjects/<môn>/solutions/<ten-de>_solution.md`.

```yaml
---
exercise_file: "<ten-de>.md"
solved_at: "YYYY-MM-DDTHH:MM:SSZ"
status: "draft"
review_round: 0
total_questions: 30
---
```

Lời giải chuẩn nên có: đề bài, phân tích đề, kiến thức nền, hướng tiếp cận, lời giải chi tiết, kết luận, sai lầm thường gặp, mẹo/ghi chú. Với trắc nghiệm số lượng lớn, có thể dùng bảng đáp án nhanh kèm giải thích ngắn nếu user ưu tiên tốc độ.

### Review

Review đặt ở `solutions/<ten-de>_review.md`, theo rubric trong `skills/answer-reviewer/SKILL.md`.

Pass khi tổng điểm >= 8.0/10 và không tiêu chí nào dưới 6.0/10.

### Extension

Extension đặt ở `extensions/<ten-de>_extended.md`, gồm 3 bài luyện mức cơ bản/trung bình/nâng cao, đào sâu kiến thức, câu hỏi phản biện và nguồn đọc thêm có thật.

## Cache và kiểm tra hash

Khi xử lý PDF/audio, tính SHA-256 và so với `source_hash` trong front matter của file output.

- Hash khớp: dùng cache, không convert/transcribe lại.
- Hash khác hoặc thiếu output: xử lý lại.
- User nói force/convert lại/transcribe lại: bỏ qua cache.

Trên Windows/PowerShell, có thể dùng:

```powershell
Get-FileHash -Algorithm SHA256 "<path>"
```

Nếu dùng công cụ có sẵn khác như `sha256sum`, vẫn được.

## Quy tắc giải bài

- Luôn đọc `metadata.yaml` của môn để biết subject, media type và bối cảnh.
- Đọc summary bài giảng trước nếu có; chỉ mở full lecture khi cần xác minh chi tiết.
- Nếu không có summary, đọc lecture MD liên quan hoặc toàn bộ lecture MD khi đề cần bối cảnh rộng.
- Với bài tính toán, trình bày số liệu trung gian, đơn vị và làm tròn rõ ràng.
- Với case study định tính, nêu framework, phân tích phương án và khuyến nghị.
- Với bài có audio, đọc transcript; đưa transcript nguyên văn vào lời giải nếu skill yêu cầu.

## Quy tắc ví dụ thực tế

- Ưu tiên doanh nghiệp Việt Nam: Vinamilk, Viettel, FPT, VinFast, Vingroup, Thế Giới Di Động, Masan, Hòa Phát, Techcombank, Vietcombank, Highlands Coffee, Phúc Long, Trung Nguyên, Biti's, Saigon Co.op, GHN, GHTK, Tiki, MoMo.
- Có thể dùng doanh nghiệp Đông Nam Á hoặc quốc tế nổi tiếng khi phù hợp.
- Không ghi doanh thu/lợi nhuận/số liệu cụ thể nếu chưa kiểm chứng.
- Tập trung vào quyết định quản trị, chiến lược, hành vi và bài học.

## Quy tắc review độc lập

Khi user yêu cầu review hoặc pipeline đến bước review:

1. Đọc đề gốc và bài giảng trước.
2. Tự giải/đánh giá độc lập trước khi đọc kỹ solution.
3. Đối chiếu từng câu, tự tính lại mọi phép tính.
4. Chấm theo 5 tiêu chí: chính xác, logic, tính toán, ngữ cảnh Việt Nam, sư phạm.
5. Nếu REVISE, nêu lỗi cụ thể, mức độ, đoạn cần sửa và đề xuất sửa.

Không review theo kiểu "đọc và gật đầu". Mục tiêu là tìm lỗi thật sự.

## Làm việc với Codex

- Dùng `rg`/`rg --files` để tìm file nhanh.
- Dùng `Get-Content -Encoding UTF8` khi đọc file tiếng Việt trên PowerShell.
- Dùng `apply_patch` để tạo/sửa file thủ công.
- Không dùng lệnh phá hủy như `git reset --hard`, `git checkout --`, xóa hàng loạt nếu user không yêu cầu rõ.
- Không commit/push trừ khi user yêu cầu.
- Khi tạo file mới, giữ tên và vị trí theo pattern hiện có của project.
- Nếu phát hiện file đã có thay đổi ngoài phạm vi task, không revert; làm việc quanh thay đổi đó.

## Khi thiếu công cụ

- Nếu PDF không thể đọc bằng text extractor, thử công cụ sẵn có trong môi trường hoặc chuyển từng trang bằng vision nếu khả dụng.
- Nếu cần cài thêm công cụ hoặc tải phụ thuộc qua mạng, xin phép user trước.
- Nếu không thể xử lý tự động, báo rõ file nào bị lỗi, nguyên nhân và đề xuất bước tiếp theo.

## Checklist trước khi kết thúc task

- File output đúng thư mục và đúng tên chưa?
- Front matter có đủ trường bắt buộc chưa?
- Với đề trắc nghiệm, số câu trong lời giải có khớp đề không?
- Với lecture convert, có summary nếu cần không?
- Với review, có điểm/verdict và tiêu chí rõ không?
- `git status --short` có thay đổi nào ngoài phạm vi cần nhắc user không?
- Nếu task vừa làm có việc dang dở để lại (vd sửa được 3/5 đáp án sai, hoặc phát hiện thêm vấn đề chưa fix) → **cập nhật [`TODO.md`](TODO.md)**: thêm mục mới, hoặc đánh dấu mục hiện có là `✅ Đã xong`. KHÔNG để việc dang dở chỉ tồn tại trong chat session.

