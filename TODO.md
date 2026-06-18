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

**Cập nhật lần cuối:** 2026-06-14 00:30 (QTCL chapter-review xong; thêm T-20260614-01 cho các môn còn lại)

---

## 🔥 Ưu tiên CAO — Sửa đáp án trắc nghiệm SAI (đã verify với bài giảng)

> Tất cả 5 mục dưới đây đã hoàn thành ngày 2026-06-12. Xem chi tiết ở section `✅ Đã xong`.

---

## ⚠️ Ưu tiên TRUNG BÌNH — Xác minh PDF gốc trước khi sửa

> Tất cả mục trong section này đã hoàn thành 2026-06-12. Xem chi tiết ở section `✅ Đã xong`.

---

## 📝 Ưu tiên TRUNG BÌNH — Viết lại lời giải QT Marketing (boilerplate)

### [T-20260611-08] Viết lại "Lời giải chi tiết" cho 5 chương QT Marketing
- **Trạng thái:** pending
- **Files:**
  - `subjects/Quản trị marketing/solutions/quan-tri-marketing-1-luyen-tap-trac-nghiem-chuong-1_solution.md`
  - `... chuong-2_solution.md`
  - `... chuong-3_solution.md`
  - `... chuong-4_solution.md`
  - `... chuong-5_solution.md`
- **Vấn đề hiện tại:** Phần "Lời giải chi tiết" của 35 câu × 5 chương đều dùng cùng 1 đoạn template copy-paste, không bàn nội dung câu hỏi cụ thể. Mục "Sai lầm thường gặp" cũng giống hệt nhau cho mọi câu. Sinh viên đọc chỉ thấy đáp án, không học được khái niệm.
- **Hành động:** với mỗi câu, viết lại:
  - Phân tích từng phương án A/B/C/D — vì sao đúng/sai.
  - Trích đoạn bài giảng `lectures/md/TXMAGM0411_QTMKT1_Baigiangtext.md` (kèm dòng) khi định nghĩa khái niệm.
  - "Sai lầm thường gặp" riêng cho câu đó.
- **Pipeline:** chạy lại skill `exercise-solver` + `example-generator` + `answer-reviewer` cho từng chương.
- **Thứ tự khuyến nghị:** Ch5 trước (gộp với việc sửa lỗi Q3 ở [T-20260611-05]), rồi Ch1 → Ch4.

### [T-20260611-09] Bổ sung lời giải cho các câu OCR bị ghép — QT Marketing
- **Trạng thái:** pending
- **Vấn đề:** Một số câu (vd Q4, Q11 mỗi chương) đề bị OCR ghép/cắt, không đọc được đầy đủ. Solver vẫn in đáp án mà không cảnh báo "không có đề".
- **Hành động:** mở PDF gốc, OCR lại câu bị lỗi → cập nhật MD đề → giải lại đúng.

---

## 📋 Ưu tiên THẤP — Làm lại các file _review.md

> [T-20260611-10] đã hoàn thành 2026-06-13. Xem chi tiết ở section `✅ Đã xong`. Phát hiện thêm 2 nghi vấn mới — xem [T-20260613-01] và [T-20260613-02] dưới đây.

---

## 📝 Ưu tiên TRUNG BÌNH — Rewrite MCQ solutions theo skill mới

> [T-20260613-04] đã hoàn thành 2026-06-14. Xem chi tiết ở section `✅ Đã xong`.

---

---

## 📚 Ưu tiên TRUNG BÌNH — Thêm "Đáp án ôn tập chương" cho các môn còn lại

### [T-20260614-01] Tạo file `_chapter-review.md` trả lời câu hỏi ôn tập chương trong lecture summary — các môn còn lại
- **Trạng thái:** pending
- **Bối cảnh:** Ngày 2026-06-14 đã tạo file mẫu cho QTCL: `subjects/Quản trị chiến lược/lectures/md/quan-tri-chien-luoc_chapter-review.md` (42 câu × 7 chương). Cần áp dụng pattern tương tự cho 7 môn còn lại — *với điều kiện* lecture summary của môn đó có sẵn các mục "Câu hỏi ôn tập chương".
- **Pattern áp dụng:**
  - Đặt file ở `subjects/<môn>/lectures/md/<slug>_chapter-review.md`
  - Front-matter: `source_lecture`, `created_at`, `subject`, `doc_type: "chapter_review"`, `chapters`, `total_questions`, `language: "vi"`
  - Cấu trúc: 1 section/chương → mỗi câu trả lời gồm định nghĩa + bảng/khung + ví dụ DN VN (không bịa số liệu)
  - Cross-link tới lecture summary đầu file
- **Danh sách môn cần kiểm tra & xử lý:**
  - [ ] Quản trị marketing — kiểm tra summary có Q ôn tập không, nếu có thì làm
  - [ ] Mua và quản trị nguồn cung
  - [ ] Quản trị tài chính
  - [ ] Khởi sự kinh doanh
  - [ ] Tâm lý quản trị kinh doanh
  - [ ] Chủ nghĩa xã hội khoa học
  - [ ] Tiếng Anh (nếu phù hợp — môn ngôn ngữ có thể không có Q ôn tập theo chương)
- **Lưu ý khi triển khai:**
  - Nếu summary không có sẵn "Câu hỏi ôn tập chương" → cần xem lecture gốc hoặc bỏ qua (warn user).
  - Bám sát bài giảng của môn đó, không kéo công thức/khái niệm từ QTCL sang.
  - Ưu tiên DN VN trong ví dụ, không bịa số liệu doanh thu/lợi nhuận cụ thể.

---

## 💡 Việc khác — Ý tưởng/đề xuất

_(Trống — T-20260612-01 đã hoàn thành 2026-06-13.)_

---

## ✅ Đã xong (giữ 30 ngày)

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
- **Còn lại sau update này**: việc viết lại solution cũ (T-20260611-08, T-20260611-09) vẫn pending — skill mới sẽ áp dụng khi rewrite, không tự sửa cũ.

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
