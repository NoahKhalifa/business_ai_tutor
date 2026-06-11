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

**Cập nhật lần cuối:** 2026-06-12

---

## 🔥 Ưu tiên CAO — Sửa đáp án trắc nghiệm SAI (đã verify với bài giảng)

> Kết quả re-review độc lập ngày 2026-06-11. Mỗi câu đều có trích bài giảng làm bằng chứng. Khi sửa solution, nhớ cập nhật cả phần giải thích, front-matter `review_round`, và file `_review.md` tương ứng.

### [T-20260611-01] Mua & QTNC — Ch2 Q15
- **Trạng thái:** pending
- **File:** `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-2_solution.md`
- **Hành động:** đổi đáp án Q15 từ **A** → **C** (Xây dựng quan hệ với nhà cung cấp).
- **Verify:** Bài giảng `lectures/md/TXBLOG3041_MVQTNC_Baigiangtext.md` dòng 1085–1117 liệt kê 5 nội dung của chính sách mua: (1) Vai trò/vị trí/nhiệm vụ BP mua; (2) Tiêu chuẩn hành vi & đạo đức; (3) Đáp ứng PTBV; (4) **Xây dựng quan hệ với NCC**; (5) Vấn đề tác nghiệp. "Xác lập quy trình mua" (đáp án solver A) không có trong danh mục.

### [T-20260611-02] Mua & QTNC — Ch4 Q12
- **Trạng thái:** pending
- **File:** `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-4_solution.md`
- **Hành động:** đổi đáp án Q12 từ **A** → **B** (Quan hệ đồng bộ – chiến lược).
- **Verify:** Bài giảng dòng 2589–2592: "Quan hệ đồng bộ: NCC thực hiện dịch vụ chuyên môn cao, liên quan nhiều tới SXKD" — khớp wording đề bài "chuyên môn cao, liên quan nhiều tới quá trình SXKD".

### [T-20260611-03] Mua & QTNC — Ch4 Q22
- **Trạng thái:** pending
- **File:** `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-4_solution.md`
- **Hành động:** đổi đáp án Q22 từ **B** → **A** (Xác định, đánh giá, phân tích, xử lý, giám sát).
- **Verify:** Bài giảng dòng 3470–3472 ghi rõ 5 công đoạn quản trị rủi ro: "Xác định rủi ro / Đánh giá rủi ro / Phân tích rủi ro / Xử lý rủi ro / Giám sát rủi ro". Đáp án B dùng "nhận dạng" và "đo lường" — không khớp wording bài giảng.

### [T-20260611-04] Mua & QTNC — Ch5 Q13
- **Trạng thái:** pending
- **File:** `subjects/Mua và quản trị nguồn cung/solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-5_solution.md`
- **Hành động:** đổi đáp án Q13 từ **A** → **C** (Người phê duyệt quyết định).
- **Verify:** Bài giảng dòng 4793–4797 liệt kê 4 chức trách cần tách (SOD): Người **xin** phê duyệt / Người mua / Người nhận hàng / Người thanh toán. C "Người phê duyệt quyết định" KHÔNG có trong danh sách 4 chức trách → đây mới là đáp án "đâu KHÔNG phải".

### [T-20260611-05] QT Marketing 1 — Ch5 Q3
- **Trạng thái:** pending
- **File:** `subjects/Quản trị marketing/solutions/quan-tri-marketing-1-luyen-tap-trac-nghiem-chuong-5_solution.md`
- **Hành động:** đổi đáp án Q3 từ **C** → **B** (Tăng cường quảng cáo duy trì/mở rộng nhận diện thương hiệu).
- **Verify:** Câu hỏi về **giai đoạn phát triển** (growth stage) của chu kỳ sống sản phẩm. Đáp án C "Giảm giá sâu xả hàng tồn kho" là đặc trưng giai đoạn **suy thoái** (decline). Growth stage = đẩy mạnh truyền thông giữ thị phần khi đối thủ vào → B.

---

## ⚠️ Ưu tiên TRUNG BÌNH — Xác minh PDF gốc trước khi sửa

### [T-20260611-06] QT Marketing 1 — Ch3 Q29 (vi/vĩ mô)
- **Trạng thái:** pending — cần soi PDF gốc.
- **File:** `subjects/Quản trị marketing/exercises/pdf/Quản trị marketing 1_Luyện tập trắc nghiệm Chương 3.pdf` + MD tương ứng.
- **Vấn đề:** OCR ghi đề là "KHÔNG phải vi mô" → solver chọn B "Cạnh tranh" là sai (cạnh tranh THUỘC vi mô). Nếu PDF gốc thực ra là "KHÔNG phải vĩ mô" thì B đúng — chỉ cần sửa MD đề khớp PDF.
- **Hành động:** mở PDF kiểm tra, sửa `exercises/md/.../Chương 3.md` cho khớp.

### [T-20260611-07] QT Marketing 1 — Ch3 Q33 (vai trò trung tâm mua)
- **Trạng thái:** pending — cần soi PDF gốc.
- **Vấn đề:** Bài giảng liệt kê 7 vai trò trung tâm mua. Cả C "Người quản lý" và D "Người giám sát" đều không nằm trong 7 vai trò → đề "đâu KHÔNG phải" hiện có 2 đáp án hợp lệ. Solver chọn D.
- **Hành động:** soi PDF xem đề thực sự có 2 phương án này hay OCR lỗi. Nếu OCR đúng → ghi nhận đề thiết kế tồi, không cần sửa solution; nếu OCR lỗi → sửa MD đề.

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

### [T-20260611-10] Viết lại 11 file _review.md theo rubric thực sự
- **Trạng thái:** pending
- **Phụ thuộc:** **Phải sửa [T-20260611-01] → [T-20260611-05] TRƯỚC**, rồi mới review lại.
- **Vấn đề:**
  - 6 review của Mua & QTNC: cho điểm an toàn 8.5–8.8 cho mọi chương, **bỏ sót 4 lỗi đáp án** xác nhận ở Ch2/4/5. Không trích bài giảng, ghi "không có lỗi nặng" sai sự thật.
  - 5 review của QT Marketing: là **bản clone của nhau** (diff chỉ khác tên chương), cùng điểm 8/8/10/8/8, không thực sự đối chiếu nội dung từng chương.
- **Hành động:** với mỗi chương, mở **chat session mới** + chạy lại skill `skills/answer-reviewer/SKILL.md` đúng quy trình: tự giải lại độc lập trước, đối chiếu từng câu với bài giảng, tự tính lại nếu có số. KHÔNG copy template giữa các chương.

---

## 💡 Việc khác — Ý tưởng/đề xuất

### [T-20260612-01] Bổ sung check trùng lặp cho `check-project.ps1`
- **Trạng thái:** idea (chưa schedule)
- **Đề xuất:** Thêm cảnh báo khi nhiều file `_review.md` trong cùng môn có body giống nhau (so hash sau khi normalize tên chương). Mục tiêu: bắt sớm pattern "review template copy-paste" như đã thấy ở QT Marketing.

---

## ✅ Đã xong (giữ 30 ngày)

_(Trống — chưa có mục nào.)_

## ❌ Bỏ qua

_(Trống.)_
