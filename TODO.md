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

**Cập nhật lần cuối:** 2026-06-13

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

## 🔥 Ưu tiên CAO — Nghi vấn lỗi đáp án mới phát hiện (từ T-10)

### [T-20260613-01] Mua & QTNC — Ch3 Q16/Q17/Q21 nghi vấn lỗi
- **Trạng thái:** pending — cần verify thủ công
- **File:** `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-3_solution.md`
- **Vấn đề** (do reviewer độc lập phát hiện trong vòng review 2026-06-13):
  - **Q16**: Solver chọn **A** "NCC chịu trách nhiệm duy trì dự trữ". Reviewer cho rằng đây là đặc trưng riêng của mô hình **VMI** (bài giảng dòng 2039–2044), không phải tiêu chí lựa chọn mô hình chung. Đáp án đúng có thể là **B** hoặc **D** theo bài giảng dòng 2073–2078.
  - **Q21**: Solver giải thích C "cải thiện giao tiếp nội bộ" là lợi ích **vô hình** của TCO, nhưng vẫn xếp vào "không khớp loại trừ" khi đề hỏi lợi ích **hữu hình**. Tự mâu thuẫn — nếu vô hình thì C chính là đáp án "hữu hình KHÔNG có".
  - **Q17**: Solver dựa vào suy đoán hữu hình/vô hình không có dòng bài giảng cụ thể chứng minh.
- **Hành động:**
  1. Mở `lectures/md/TXBLOG3041_MVQTNC_Baigiangtext.md` dòng 1620–2250 (TCO, mô hình mua, VMI).
  2. Tìm chính xác phần nào liệt kê (a) lợi ích hữu hình vs vô hình của TCO, (b) tiêu chí lựa chọn giữa các mô hình mua.
  3. Nếu xác định Q16 sai → sửa đáp án + cập nhật `_review.md`. Tương tự Q17, Q21.

### [T-20260613-02] QT Marketing 1 — Ch3 Q20 (OCR sai "vĩ"→"vi") — *đã sửa 2026-06-13*
- Soi MD đề: A và C đều là "vi mô" (OCR sai). Đối chiếu PDF gốc (Trang 11): A thực tế là **"vĩ mô"**, C là **"vi mô"**. Giống pattern lỗi Q29.
- Đã sửa MD đề (Ch3 Q20: A → "vĩ mô"). Đã cập nhật đáp án solver **A → C** (vì sau khi sửa OCR, "vi mô" đúng wording đề chuyển sang option C). Cleanup luôn solution Q20.
- **Còn lại**: cần soi toàn bộ MD đề Ch3 (35 câu) để tìm các câu khác cùng pattern lỗi "vĩ → vi" (gợi ý: tìm các câu có nhắc môi trường vi/vĩ mô).

---

## 💡 Việc khác — Ý tưởng/đề xuất

### [T-20260612-01] Bổ sung check trùng lặp cho `check-project.ps1`
- **Trạng thái:** idea (chưa schedule)
- **Đề xuất:** Thêm cảnh báo khi nhiều file `_review.md` trong cùng môn có body giống nhau (so hash sau khi normalize tên chương). Mục tiêu: bắt sớm pattern "review template copy-paste" như đã thấy ở QT Marketing.

---

## ✅ Đã xong (giữ 30 ngày)

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

### [T-20260611-10] Viết lại 11 file _review.md theo rubric thực sự — *hoàn thành 2026-06-13*
- Đã rewrite hoàn chỉnh 11 file `_review.md` (review_round 2) — không còn là clone template:
  - **Mua & QTNC**: Ch1 (7.0 REVISE), Ch2 (6.8 REVISE), Ch3 (6.1 REVISE), Ch4 (6.5 REVISE), Ch5 (6.8 REVISE), Ch6 (7.0 REVISE).
  - **QT Marketing**: Ch1 (3.3 REVISE), Ch2 (6.4 REVISE), Ch3 (7.5 REVISE), Ch4 (5.3 REVISE), Ch5 (7.2 REVISE).
- Mỗi review độc lập: tự giải 8–11 câu mẫu trước khi đọc solution; đối chiếu với bài giảng (có dòng); chấm rubric 5 tiêu chí.
- Phát hiện thêm 2 nghi vấn mới (tách thành T-20260613-01 và T-20260613-02 ở section trên).
- **Pattern lỗi chung khắp 11 chương**: 100% solution dùng boilerplate "không khớp trọng tâm khái niệm" cho phương án sai, "Sai lầm thường gặp" giống nhau khắp các câu → khẳng định lại nhu cầu của [T-20260611-08] (rewrite lời giải chi tiết).

## ❌ Bỏ qua

_(Trống.)_
