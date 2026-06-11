# Business AI Tutor

Hệ thống học liệu AI hỗ trợ học chuyên ngành **Quản trị Kinh doanh**: tự động đọc PDF bài giảng và câu hỏi ôn tập, biên dịch sang Markdown, giải bài tập chi tiết kèm ví dụ thực tế, bài tập mở rộng, và có cơ chế tự rà soát câu trả lời.

> **Cách dùng**: Project hoạt động qua **VS Code + GitHub Copilot Chat (Agent mode)** với model **Claude Sonnet 4.6**. Không cần code Python, không cần API key trực tiếp (Copilot đã tích hợp).

> 👋 **Bạn là AI agent (Codex, Claude Code, Cursor, Aider, Copilot)?** → đọc [`AGENTS.md`](AGENTS.md). Đó là single source of truth cho mọi quy tắc, pipeline, naming convention, skill routing. README này dành cho người dùng.

---

## 🚀 Setup nhanh

### Yêu cầu
- ✅ VS Code version mới (≥1.95)
- ✅ GitHub Copilot subscription (Pro/Business/Enterprise) — bắt buộc để dùng Claude
- ✅ GitHub Copilot Chat extension (đã cài sẵn nếu có Copilot)
- ✅ Git LFS (cho file PDF nặng)

### Bước 1: Bật Agent mode + chọn Claude Sonnet 4.6
1. Mở Copilot Chat panel (`Ctrl+Alt+I` hoặc `Cmd+Alt+I` trên Mac)
2. Trong dropdown ở góc panel, chọn **Agent** (không phải Ask)
3. Trong model picker (góc phải dưới), chọn **Claude Sonnet 4.6**

> ⚠️ Nếu không thấy Claude trong dropdown: kiểm tra Copilot subscription tier, có thể admin tổ chức cần bật. Xem [docs](https://docs.github.com/en/copilot).

### Bước 2: Cài Git LFS
```bash
# Mac
brew install git-lfs
# Ubuntu/Debian
sudo apt install git-lfs
# Windows: tải tại https://git-lfs.com

git lfs install   # 1 lần / máy
```

### Bước 3: Clone project & mở trong VS Code
```bash
git clone <repo-url> business_ai_tutor
cd business_ai_tutor
git lfs pull       # tải PDF qua LFS
code .             # mở VS Code
```

Copilot sẽ tự đọc `.github/copilot-instructions.md` → biết cách hỗ trợ user.

---

## 💬 Sử dụng hằng ngày

### Tạo môn học mới
Trong Copilot Chat (Agent mode), gõ:
```
Tạo môn học mới: marketing-can-ban
```
Copilot sẽ:
- Copy `subjects/_template/` → `subjects/marketing-can-ban/`
- Yêu cầu bạn điền `metadata.yaml`

### Bỏ PDF vào folder
- Bài giảng → `subjects/marketing-can-ban/lectures/pdf/`
- Đề bài, câu hỏi ôn tập → `subjects/marketing-can-ban/exercises/pdf/`

### Yêu cầu Copilot xử lý
```
Giải đề "de-on-tap-chuong-1.pdf" trong môn marketing-can-ban
```

Copilot sẽ tự động chạy đủ 5 bước:
1. **Convert** PDF → MD (kiểm tra cache SHA-256, skip nếu đã có)
2. **Giải bài** chi tiết theo template sư phạm 8 phần
3. **Thêm ví dụ thực tế** từ doanh nghiệp Việt Nam
4. **Tạo bài tập mở rộng** (3 bài luyện ★ ★★ ★★★ + đào sâu)
5. **Rà soát chéo** lời giải, tự động sửa nếu chưa đạt 8.0/10

Sau mỗi tool call (đọc/ghi file, chạy bash), Copilot Agent sẽ hỏi approve. Có thể bật auto-approve cho tốc độ.

---

## 🔄 Workflow với Git

### Lưu kết quả lên git
```bash
git add subjects/marketing-can-ban/
git commit -m "Học xong chương 1 môn marketing"
git push
```

### Cache MD share giữa các máy
Vì MD đã commit cùng PDF, máy khác clone về sẽ:
- Thấy MD đã có → Copilot skip bước convert (tiết kiệm token)
- Chỉ chạy lại nếu PDF thay đổi (hash khác)

### Đổi máy
```bash
git pull
git lfs pull   # tải PDF mới
```

---

## 📂 Cấu trúc folder

```
business_ai_tutor/
├── .github/
│   ├── copilot-instructions.md         ← Copilot tự đọc (project-wide)
│   └── instructions/
│       ├── pdf-conversion.instructions.md   ← apply trong subjects/*/{pdf,md}/
│       ├── solving.instructions.md          ← apply trong subjects/*/solutions/
│       └── reviewing.instructions.md        ← apply cho *_review.md
├── .gitattributes                      ← Git LFS cho PDF
├── .gitignore
├── README.md                           ← File này
├── ARCHITECTURE.md                     ← Sơ đồ luồng + rubric chi tiết
│
├── skills/                             ← 6 skill cốt lõi (Copilot đọc khi cần)
│   ├── pdf-to-md/SKILL.md
│   ├── audio-to-transcript/SKILL.md    ← chỉ dùng cho môn có media_types: ["audio"]
│   ├── exercise-solver/SKILL.md
│   ├── example-generator/SKILL.md
│   ├── extension-builder/SKILL.md
│   └── answer-reviewer/SKILL.md
│
├── subjects/
│   ├── _template/
│   └── Quản trị chiến lược/        ← tên folder = tiếng Việt Unicode
│       ├── metadata.yaml
│       ├── lectures/{pdf,md}/          ← PDF qua LFS, MD bình thường
│       ├── exercises/{pdf,md}/
│       ├── solutions/                  ← Lời giải + báo cáo review
│       └── extensions/                 ← Bài tập mở rộng
│
├── prompts/                            ← Template tham khảo
└── outputs/                            ← (gitignored) tổng hợp tạm
```

---

## 💬 Bộ lệnh chat đầy đủ

### Quản lý môn
```
Tạo môn mới: <slug>
Liệt kê các môn hiện có
Trạng thái môn <slug>
```

### Xử lý PDF
```
Convert toàn bộ PDF trong môn <slug>
Convert lại file <tên>.pdf       ← bỏ qua cache
```

### Giải bài
```
Giải đề <tên-file>.pdf trong môn <slug>
Giải lại đề này (sửa theo phản hồi review)
Chỉ giải, bỏ qua review
```

### Rà soát
```
Review lại file <đường-dẫn-solution>.md
Cho điểm chi tiết bài này
Bài giải này có lỗi gì không?
```

> **Lưu ý cực kỳ quan trọng**: Để bước review được khách quan nhất, hãy **nhấn nút `+` trong Copilot Chat panel để bắt đầu chat MỚI** trước khi gõ lệnh review. Như vậy Claude không bị "ảnh hưởng" bởi quá trình giải bài trong session trước.

### Mở rộng
```
Tạo thêm 3 bài tập tương tự cho đề <tên>
Cho tôi câu hỏi ôn thi vấn đáp về chương này
Đào sâu thêm khái niệm <tên khái niệm>
```

---

## 🛡️ Cơ chế rà soát

Chi tiết trong `skills/answer-reviewer/SKILL.md`. Tóm tắt:

| Tiêu chí | Trọng số | Reviewer làm gì |
|---|---|---|
| Chính xác khái niệm/công thức | 30% | So với bài giảng, kiểm tra định nghĩa |
| Logic lập luận | 20% | Có bước nhảy bị bỏ qua không? |
| Tính toán | 20% | **Tự tính lại từ đầu** rồi so |
| Phù hợp ngữ cảnh VN | 15% | Ví dụ có thực, không bịa số liệu |
| Sư phạm & độ chi tiết | 15% | Sinh viên đọc có hiểu không? |

**Pass**: tổng ≥ 8.0 VÀ không tiêu chí nào < 6.0.
**Fail**: Copilot tự sửa theo phản hồi → review lại. Tối đa 3 vòng.

---

## ⚠️ Một vài điểm cần biết khi dùng Copilot Chat Agent

1. **Phải ở Agent mode** (không phải Ask): Agent mới đọc/ghi file và chạy bash được. Kiểm tra dropdown ở Chat panel.

2. **Approve từng action**: Copilot Agent sẽ hỏi approve mỗi lần ghi file hoặc chạy command. Có thể tinh chỉnh trong Settings:
   - `chat.tools.autoApprove` cho các action an toàn (đọc file, list folder)
   - Giữ approve thủ công cho `write_file` và `run_in_terminal`

3. **Token & rate limit**: 
   - Bài giảng dài + giải bài + review tốn nhiều token.
   - Convert PDF → MD trước (1 lần, cache) → các bước sau dùng MD nhẹ hơn nhiều.
   - Chú ý usage limit hằng tuần của Copilot subscription.

4. **Context window**: Claude Sonnet 4.6 có context 200K tokens. Đủ cho 1 đề + 3-5 bài giảng. Nếu môn có >10 file lecture dài → tóm tắt trước.

5. **Settings cần bật**:
   - `github.copilot.chat.codeGeneration.useInstructionFiles` = `true` (mặc định ON từ 2025)

---

## 📚 Đọc thêm

- [`AGENTS.md`](AGENTS.md) — **Canonical rules cho mọi AI agent** (Codex, Claude Code, Cursor, Copilot…). Single source of truth.
- [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — Chỉ phần khác biệt cho Copilot (Agent mode, settings, model picker). Trỏ về AGENTS.md cho mọi rule chung.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — Sơ đồ luồng & rubric chi tiết
- [`INDEX.md`](INDEX.md) — Bản đồ subject + skill
- [`skills/*/SKILL.md`](skills/) — Logic của từng skill
- [`scripts/check-project.ps1`](scripts/check-project.ps1) — Audit trạng thái project, sinh `STATUS.md` cho mỗi môn
- [VS Code Copilot Customization docs](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Git LFS docs](https://git-lfs.com)

### Kiểm tra trạng thái project

```powershell
pwsh scripts/check-project.ps1                    # toàn project
pwsh scripts/check-project.ps1 -Subject "<tên>"   # 1 môn
pwsh scripts/check-project.ps1 -WriteStatus       # đè STATUS.md cho mỗi môn
```

Script phát hiện: PDF chưa convert, solution chưa review, `exercise_file` trỏ về file không tồn tại, môn thiếu folder/metadata. Exit 1 nếu có issues.
