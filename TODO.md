# TODO — Việc dang dở (handoff cho session sau)

> **Single source of truth cho việc CHƯA HOÀN THÀNH trong project.**
> Mọi AI agent (Claude Code, GitHub Copilot, Codex, Cursor, Aider) đọc file này TRƯỚC khi bắt đầu task mới, để biết có việc dang dở nào cần nối tiếp.
>
> ## Quy ước
> - Mỗi mục có ID `[T-YYYYMMDD-NN]`, **Trạng thái** (`pending` / `in-progress` / `blocked`), **Ưu tiên**, **Mô tả ngắn**, **Hành động cụ thể**, **File liên quan**.
> - Khi hoàn thành: chuyển sang section `## ✅ Đã xong` kèm ngày + commit hash (nếu có). Giữ ở đó 30 ngày rồi xóa.
> - Khi không còn relevant: chuyển sang `## ❌ Bỏ qua` kèm lý do.
> - **KHÔNG xóa mục `pending` mà chưa làm.** Nếu không định làm nữa → mark `❌ Bỏ qua` + lý do.
> - Cập nhật `Cập nhật lần cuối:` ở đầu file mỗi khi thay đổi.

**Cập nhật lần cuối:** 2026-07-04 23:40 (T-20260704-01 update: Unit 1/3/4 listening đã verify với transcript; Unit 2 audio vẫn thiếu — user upload nhầm Unit 3 audio thay vì Unit 2)

---

## 🔊 Ưu tiên CAO — Tiếng Anh Thương Mại 1: Unit 2 audio bị upload nhầm

- **[T-20260704-01]** — in-progress — **Ưu tiên**: CAO (Unit 2 vẫn thiếu audio đúng)
  - **Tiến độ**:
    - ✅ Unit 1 listening (Q26-Q45): đã VERIFY với `Unit1.mp3` → transcript ở `exercises/md/Unit1_transcript.md`. 12/20 dự đoán ban đầu SAI, đã sửa.
    - ⚠️ Unit 2 listening (Q26-Q39, Q50-Q55): **VẪN CHƯA VERIFY** — user upload `Unit2.mp3` nhưng file này thực chất chứa audio Unit 3 (verified qua nội dung Mr. Hall beard/glasses, Brian's birthday, Tanya sports camp, Jeff karate — khớp Unit 3, không phải Unit 2 questions về girl fell off bike / policy number / knife location).
    - ✅ Unit 3 listening (Q26-Q45): đã VERIFY dùng `Unit2.mp3` (nội dung Unit 3) → transcript ở `exercises/md/Unit3_transcript.md`. 12/20 dự đoán ban đầu SAI.
    - ✅ Unit 4 listening (Q26-Q45): đã VERIFY với `Unit4.mp3` → transcript ở `exercises/md/Unit4_transcript.md`. 12/20 dự đoán ban đầu SAI.
  - **Việc còn lại**:
    1. User upload lại đúng file audio cho Unit 2 (câu về girl on bike, policy number Z..., knife location, weather sunny/cloudy...).
    2. Sau đó chạy `python tools/transcribe_units.py` cho file đó.
    3. Rewrite listening Unit 2 solution với đáp án verified + trích transcript.
  - **File liên quan**:
    - `subjects/Tiếng anh thương mại 1/solutions/tieng-anh-thuong-mai-1-unit-2_solution.md` (listening chưa verify)
    - `subjects/Tiếng anh thương mại 1/exercises/audio/Unit2.mp3` (upload nhầm)
    - `subjects/Tiếng anh thương mại 1/exercises/audio/Unit3.mp3` (duplicate của Unit2.mp3)
  - **Ghi chú**:
    - File Whisper transcribe (base model) tự động thông qua `tools/transcribe_units.py`; deps: `openai-whisper`, `static-ffmpeg` (đã pip install).
    - Q14 Unit 4 có OCR issue (verb "notice" trong ngoặc nhưng options về "buy"); Q25 Unit 2 và Q24 Unit 3 có OCR issue với "A.broke" — đã giải theo nội dung logic.

---

## 📝 Ưu tiên TRUNG BÌNH — Tiếng Anh Thương Mại 1: chưa có lecture MD

- **[T-20260704-02]** — pending — **Ưu tiên**: TRUNG BÌNH
  - **Mô tả**: `subjects/Tiếng anh thương mại 1/lectures/pdf/` và `lectures/md/` đều trống → solution phải dựa trên chuẩn Cambridge Business English chứ không dẫn được `dòng X-Y` bài giảng.
  - **Hành động cụ thể**: Nếu user cung cấp PDF lecture (giáo trình), chạy `pdf-extract-cli` để convert MD, sau đó rewrite solutions với dẫn dòng lecture chuẩn.
  - **File liên quan**: Toàn bộ solution môn Tiếng Anh Thương Mại 1.

---

## 🔥 Ưu tiên CAO — Sửa đáp án trắc nghiệm SAI (đã verify với bài giảng)

> Tất cả 5 mục dưới đây đã hoàn thành ngày 2026-06-12. Xem chi tiết ở section `✅ Đã xong`.

---

## ⚠️ Ưu tiên TRUNG BÌNH — Xác minh PDF gốc trước khi sửa

> Tất cả mục trong section này đã hoàn thành 2026-06-12. Xem chi tiết ở section `✅ Đã xong`.

---

## 📝 Ưu tiên TRUNG BÌNH — Viết lại lời giải QT Marketing (boilerplate)

> [T-20260611-08] đã hoàn thành 2026-06-28. Xem chi tiết ở section `✅ Đã xong`.

## 📋 Ưu tiên THẤP — Làm lại các file _review.md

> [T-20260611-10] đã hoàn thành 2026-06-13. Xem chi tiết ở section `✅ Đã xong`. Phát hiện thêm 2 nghi vấn mới — xem [T-20260613-01] và [T-20260613-02] dưới đây.

---

## 📝 Ưu tiên TRUNG BÌNH — Rewrite MCQ solutions theo skill mới

> [T-20260613-04] đã hoàn thành 2026-06-14. Xem chi tiết ở section `✅ Đã xong`.

---

---

## 📚 Ưu tiên TRUNG BÌNH — Thêm "Đáp án ôn tập chương" cho các môn còn lại

> [T-20260614-01] đã hoàn thành 2026-06-28. Xem chi tiết ở section `✅ Đã xong`.

---

## 💡 Việc khác — Ý tưởng/đề xuất

_(Trống — T-20260612-01 đã hoàn thành 2026-06-13.)_

---

## ✅ Đã xong (giữ 30 ngày)

### [T-20260614-01] Tạo file `_chapter-review.md` trả lời câu hỏi ôn tập chương trong lecture summary — *hoàn thành 2026-06-28*
- Bối cảnh: ngày 2026-06-14 đã có file mẫu QTCL `subjects/Quản trị chiến lược/lectures/md/quan-tri-chien-luoc_chapter-review.md` (42 câu × 7 chương). Ngày 2026-06-28 đã rà các môn còn lại và chỉ tạo file khi có block câu hỏi ôn tập rõ.
- Đã tạo mới:
  - `subjects/Chủ nghĩa xã hội khoa học/lectures/md/chu-nghia-xa-hoi-khoa-hoc_chapter-review.md` — 37 câu × 7 chương, lấy từ `chu-nghia-xa-hoi-khoa-hoc_summary.md`.
  - `subjects/Tâm lý quản trị kinh doanh/lectures/md/tam-ly-quan-tri-kinh-doanh_chapter-review.md` — 19 câu × 6 chương, lấy từ lecture full `Text.md` vì môn này chưa có summary riêng chứa câu hỏi ôn tập.
- Đã rà và không tạo file mới vì không có block "Câu hỏi ôn tập chương" rõ trong nguồn hiện có:
  - Quản trị marketing: không có lecture summary/chapter-review source trong `lectures/md`.
  - Mua và quản trị nguồn cung: lecture full hiện không có block "Câu hỏi ôn tập chương" tương tự.
  - Quản trị tài chính: `Financial management_summary.md` chỉ có mục "Câu hỏi tự kiểm tra nhanh", chưa phải đáp án ôn tập chương.
  - Khởi sự kinh doanh: `khoi-su-kinh-doanh_summary.md` chỉ có cụm "Năm câu hỏi cốt lõi", chưa phải block ôn tập chương.
  - Tiếng Anh: không thấy nguồn lecture summary/chapter-review phù hợp trong `lectures/md`.
- Verify:
  - `rg -n "^### Câu|^## Chương|total_questions"` xác nhận CNXHKH có 37 câu và Tâm lý QTKD có 19 câu.
  - `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-project.ps1 -Subject "Tâm lý quản trị kinh doanh"` báo **Issues: none**.

### [T-20260611-08] Viết lại "Lời giải chi tiết" cho 5 chương QT Marketing — *hoàn thành 2026-06-28*
- Đã rewrite các solution QT Marketing Ch1-Ch5 theo MCQ compact: mỗi câu có đáp án, phân tích A/B/C/D riêng, dẫn dòng bài giảng, lưu ý/sai lầm riêng và ví dụ thực tế phù hợp.
- Tiến độ:
  - Ch5: re-extract PDF gốc, làm sạch đề MD, rewrite solution, cập nhật review round 3.
  - Ch1: re-extract PDF gốc, phục hồi Q3/Q4/Q11, rewrite solution, cập nhật review round 3.
  - Ch2: re-extract PDF gốc, phục hồi Q4/Q11, rewrite solution, cập nhật review round 3.
  - Ch4: re-extract PDF gốc bằng `tools.pdf_extract`, phục hồi Q4/Q11/Q24, làm sạch đề MD, sửa Q3 theo wording PDF, rewrite solution, cập nhật review round 3 PASS.
  - Ch3: rewrite lại ngày 2026-06-28 sau khi phát hiện file solution chỉ còn khung rỗng; cập nhật review round 4 PASS.
- Verify: `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-project.ps1 -Subject "Quản trị marketing"` báo **Issues: none**.

### [T-20260611-09] Bổ sung lời giải cho các câu OCR bị ghép — QT Marketing — *hoàn thành 2026-06-28*
- Đã mở/re-extract PDF gốc các chương QT Marketing bị OCR ghép/cắt và cập nhật đề/solution/review tương ứng.
- Tiến độ:
  - Ch5: phục hồi Q4 và Q24 từ PDF extract; đồng thời phát hiện Q3/Q23 trong MD cũ khác PDF và sửa theo PDF gốc.
  - Ch1: phục hồi Q3, Q4, Q11 từ PDF extract và cập nhật đề/solution/review.
  - Ch2: phục hồi Q4, Q11 từ PDF extract và cập nhật đề/solution/review.
  - Ch3: xử lý OCR confusables ở [T-20260613-02].
  - Ch4: phục hồi Q4, Q11, Q24 từ PDF extract ngày 2026-06-28, làm sạch đề, rewrite solution và cập nhật review round 3 PASS.

### [T-20260613-04] Mua & QTNC — Rewrite 6 file solution Ch1-Ch6 theo template MCQ mới — *hoàn thành 2026-06-14*
- Đã rewrite xong toàn bộ 6 file solution Ch1-Ch6 theo template MCQ mới: phân tích riêng A/B/C/D, có dẫn dòng bài giảng, giảm boilerplate, thêm critical engagement khi lecture thiếu/gây nhầm/sai so với chuẩn ngành.
- Tiến độ:
  - Ch1: 30 câu, boilerplate x78 → x5 (~95% giảm). Q3 flag tranh luận đáp án C/B.
  - Ch2: 30 câu, boilerplate = 0. Q21 flag đề kém.
  - Ch3: 30 câu, boilerplate = 0. Giữ Q16/Q17/Q21 đáp án A theo verify T-20260613-01.
  - Ch4: 30 câu; detector còn flag top phrase x6 do cấu trúc "Ghi chú critical engagement" intentional, không phải boilerplate lập luận.
  - Ch5: rewrite 30 câu ngày 2026-06-14, 68 dẫn dòng, không bị `check-project` flag boilerplate.
  - Ch6: rewrite 30 câu ngày 2026-06-14, 44 dẫn dòng, không bị `check-project` flag boilerplate.
- File Ch5/Ch6 đã sửa:
  - `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-5_solution.md`
  - `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-6_solution.md`
- Verify: `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-project.ps1 -Subject "Mua và quản trị nguồn cung"` hiện chỉ còn 2 flag cũ: Ch1 quote lặp x5 và Ch4 critical engagement x6; Ch5/Ch6 sạch boilerplate.

### [T-20260611-01] Mua & QTNC — Ch2 Q15 — *hoàn thành 2026-06-12*
- Đổi đáp án Q15 từ **A** → **C** ("Xây dựng quan hệ với nhà cung cấp").
- File: `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-2_solution.md`. Đã cập nhật bảng đáp án nhanh, phần giải thích chi tiết (trích bài giảng dòng 1085–1117), `review_round: 1`, và đính chính trong file `_review.md` tương ứng.

### [T-20260611-02] Mua & QTNC — Ch4 Q12 — *hoàn thành 2026-06-12*
- Đổi đáp án Q12 từ **A** → **B** ("Quan hệ đồng bộ – chiến lược").
- File: `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-4_solution.md`. Đã cập nhật bảng đáp án, phần giải thích chi tiết (trích bài giảng dòng 2580–2592), `review_round: 1`, đính chính trong `_review.md` Ch4.

### [T-20260611-03] Mua & QTNC — Ch4 Q22 — *hoàn thành 2026-06-12*
- Đổi đáp án Q22 từ **B** → **A** (Xác định / Đánh giá / Phân tích / Xử lý / Giám sát rủi ro).
- Cùng file solution với T-02; đã trích nguyên văn bài giảng dòng 3470–3472 trong phần giải thích chi tiết. Đính chính trong `_review.md` Ch4.

### [T-20260611-04] Mua & QTNC — Ch5 Q13 — *hoàn thành 2026-06-12*
- Đổi đáp án Q13 từ **A** → **C** ("Người phê duyệt quyết định" – KHÔNG thuộc 4 chức trách SOD).
- File: `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-5_solution.md`. Trích bài giảng dòng 4792–4802. `review_round: 1`. Đính chính trong `_review.md` Ch5.

### [T-20260611-05] QT Marketing 1 — Ch5 Q3 — *hoàn thành 2026-06-12*
- Đổi đáp án Q3 từ **C** → **B** ("Tăng cường quảng cáo duy trì nhận diện thương hiệu" – chiến lược growth stage).
- File: `subjects/Quản trị marketing/solutions/quan-tri-marketing-1-luyen-tap-trac-nghiem-chuong-5_solution.md`. Cleanup luôn phần đề bài bị OCR mangled cho Q3 (thay bằng tiếng Việt sạch theo file `exercises/md/...Chương 5.md`). Trích bài giảng mục 5.4.2 (dòng 3741–3770). `review_round: 1`. Đính chính trong `_review.md` Ch5 QT Marketing.

### [T-20260611-06] QT Marketing 1 — Ch3 Q29 (vi/vĩ mô) — *hoàn thành 2026-06-12*
- Soi PDF gốc (Trang 15) → đề thực sự là "KHÔNG phải yếu tố thuộc môi trường **vĩ mô**" (OCR sai thành "vi mô").
- Đã sửa file `subjects/Quản trị marketing/exercises/md/Quản trị marketing 1_Luyện tập trắc nghiệm Chương 3.md` (Q29) cho khớp PDF.
- Solution Q29 giữ đáp án **B** ("Môi trường cạnh tranh" — thuộc vi mô). Cleanup luôn phần đề OCR mangled trong solution. `review_round: 1`.

### [T-20260611-07] QT Marketing 1 — Ch3 Q33 (vai trò trung tâm mua) — *hoàn thành 2026-06-12*
- Soi PDF gốc (Trang 17) → đề thực sự có cả C "Người quản lý" và D "Người giám sát" — **OCR đúng, đề thiết kế tồi** (2 đáp án "không phải" 7 vai trò).
- Solution Q33 giữ đáp án **D** theo bộ đáp án mẫu, nhưng đã thêm ghi chú ⚠️ rằng cả C và D đều không nằm trong 7 vai trò trung tâm mua (initiator/user/buyer/influencer/decider/gatekeeper/approver). Cleanup phần đề OCR mangled. Khi đi thi: chọn nhiều → cả C+D; chọn 1 → ưu tiên D.

### [T-20260613-01] Mua & QTNC Ch3 Q16/Q17/Q21 verify — *hoàn thành 2026-06-13*
- **Kết quả: KHÔNG có lỗi đáp án.** Cả 3 câu solver đã chọn **A**, sau verify với lecture đều ĐÚNG.
  - **Q16**: Lecture dòng 2073-2078 liệt kê 3 yếu tố lựa chọn mô hình (mục tiêu, lợi thế so sánh, năng lực NCC) → B/C/D. A "NCC chịu trách nhiệm duy trì dự trữ" là đặc trưng VMI (dòng 2039-2044), không nằm trong list → đề "KHÔNG bao gồm" → A đúng.
  - **Q17**: Lecture dòng 2378-2389 list 4 lợi ích hữu hình + 3 vô hình của TCO; "Cải thiện chiến lược mua" KHÔNG có ở cả 2 nhóm → đề "KHÔNG bao gồm" → A đúng.
  - **Q21**: "Cải thiện giao tiếp nội bộ" thuộc vô hình (dòng 2387), không thuộc hữu hình → đề "hữu hình KHÔNG có" → A đúng.
- **Nguyên nhân nghi vấn ở round 2**: phần "Lời giải chi tiết" boilerplate không trích dòng → reviewer không tìm thấy bằng chứng nên nghi sai. Sau verify trực tiếp: vấn đề thực tế là chất lượng lập luận, không phải đáp án.
- Đã update `_review.md` Ch3 Mua & QTNC (round 3, score 7.0 REVISE_MINOR thay vì 6.1 REVISE).

### [T-20260613-02] QT Marketing 1 — Ch3 OCR confusables — *hoàn thành 2026-06-13*
- **Mở rộng từ scope cũ**: không chỉ Q20 mà re-extract toàn bộ 35 câu từ PDF gốc bằng vision (PDF Ch3 text-based, hash khớp). Sửa các đoạn OCR mangled ở Q3, Q14, Q20, Q26, Q33.
- Đã áp dụng skill mới: flag `[VERIFY_OCR: vi/vĩ — PDF gốc trang N]` cho **5 câu** chứa cặp vi/vĩ mô (Q8, Q20, Q24, Q29, Q32). Front-matter ghi `confusables_flagged: 5`.
- File: `subjects/Quản trị marketing/exercises/md/Quản trị marketing 1_Luyện tập trắc nghiệm Chương 3.md`.
- Solver tương lai khi giải Ch3 sẽ thấy các flag này → phải dừng verify với PDF gốc trước khi chọn đáp án. Cycle quá trình lỗi đã đóng.

### [T-20260613-03] Nâng cấp skill MCQ + OCR confusables + dup detection — *hoàn thành 2026-06-13*
- **Mục tiêu**: fix root-cause cho 3 pattern lỗi lặp lại (boilerplate giải MCQ, OCR nhầm dấu tiếng Việt, không có cơ chế tự phát hiện template clone). Không retroactive sửa solution cũ.
- **Skill upgrade**:
  - `skills/exercise-solver/SKILL.md`: thêm "Cấu trúc bắt buộc cho TRẮC NGHIỆM (MCQ)" — override template 8 phần, bắt buộc per-option analysis A/B/C/D + trích `dòng X-Y` mỗi câu + "Sai lầm thường gặp" riêng cho từng câu + check OCR confusables.
  - `skills/answer-reviewer/SKILL.md`: cập nhật rubric tiêu chí 2 (Logic) + thêm "Tiêu chí bổ sung cho bài MCQ" (4 check: per-option, cite-line, sai lầm riêng, OCR verify).
  - `skills/pdf-to-md/SKILL.md`: thêm "Bước 3.1: Cảnh báo OCR confusables tiếng Việt" — danh sách 9 cặp confusable (vi/vĩ, sỉ/sĩ, lý/ly, lỗ/lô, hoàn/hoàng, nhặt/nhật, chỉ/chí, sản/sàn, mã/mả) + rule chèn flag inline `[VERIFY_OCR: ...]` + tín hiệu 2 phương án MCQ trùng chữ → flag.
  - `prompts/solver_template.md` + `prompts/reviewer_checklist.md`: thêm note + section MCQ tương ứng.
- **Script upgrade**: `scripts/check-project.ps1` thêm 2 detector boilerplate:
  - **Cross-file**: Jaccard 5-gram ≥85% giữa các `_review.md` / `_solution.md` cùng môn.
  - **Intra-file**: 10-gram lặp ≥5 lần trong cùng 1 file (pattern phổ biến nhất ở solver MCQ).
  - Verify chạy thực tế: bắt đúng QT Marketing (top phrase x96-105) + Mua & QTNC (x45-78), không false-positive ở các môn template-rich khác (Khởi sự kinh doanh).
- **Cập nhật 2026-06-28**: việc viết lại solution cũ ở [T-20260611-08] và OCR ghép/cắt QT Marketing [T-20260611-09] đều đã hoàn thành.

### [T-20260612-01] Dup detection cho check-project.ps1 — *hoàn thành 2026-06-13 (gộp với T-20260613-03)*
- Đã implement trong `scripts/check-project.ps1` (functions: `Get-NormalizedBody`, `Get-ShingleSet`, `Get-JaccardSimilarity`, `Find-BoilerplateDuplicates`, `Get-IntraFileRepetition`, `Find-IntraFileBoilerplate`).
- Audit toàn project lần đầu sau khi enable: 6 môn x ~5 chương = 11 file MCQ solution bị flag là boilerplate nặng. Khớp pattern đã ghi nhận trong T-20260611-08 và T-20260611-10.

### [T-20260611-10] Viết lại 11 file _review.md theo rubric thực sự — *hoàn thành 2026-06-13*
- Đã rewrite hoàn chỉnh 11 file `_review.md` (review_round 2) — không còn là clone template:
  - **Mua & QTNC**: Ch1 (7.0 REVISE), Ch2 (6.8 REVISE), Ch3 (6.1 REVISE), Ch4 (6.5 REVISE), Ch5 (6.8 REVISE), Ch6 (7.0 REVISE).
  - **QT Marketing**: Ch1 (3.3 REVISE), Ch2 (6.4 REVISE), Ch3 (7.5 REVISE), Ch4 (5.3 REVISE), Ch5 (7.2 REVISE).
- Mỗi review độc lập: tự giải 8–11 câu mẫu trước khi đọc solution; đối chiếu với bài giảng (có dòng); chấm rubric 5 tiêu chí.
- Phát hiện thêm 2 nghi vấn mới (tách thành T-20260613-01 và T-20260613-02 ở section trên).
- **Pattern lỗi chung khắp 11 chương**: 100% solution dùng boilerplate "không khớp trọng tâm khái niệm" cho phương án sai, "Sai lầm thường gặp" giống nhau khắp các câu → khẳng định lại nhu cầu của [T-20260611-08] (rewrite lời giải chi tiết).

## ❌ Bỏ qua

_(Trống.)_
