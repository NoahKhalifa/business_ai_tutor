---
name: extension-builder
description: Tạo bài tập tham khảo, bài tập mở rộng độ khó tăng dần, và phần "đào sâu kiến thức" cho mỗi bài học/lời giải Quản trị Kinh doanh. BẮT BUỘC dùng skill này sau khi đã có lời giải + ví dụ thực tế, hoặc khi người dùng yêu cầu "bài tập tương tự", "mở rộng", "luyện thêm", "đào sâu".
---

# Skill: Extension Builder (mở rộng & luyện tập)

## Mục tiêu
Sau khi đã giải bài và có ví dụ, sinh viên cần:
1. **Bài tập tương tự** để tự luyện (3 bài, độ khó tăng dần).
2. **Phần đào sâu kiến thức** — mở rộng khái niệm, dẫn nguồn đọc thêm.
3. **Câu hỏi tư duy phản biện** để chuẩn bị cho thi vấn đáp/tình huống.

## Khi nào trigger
- Sau bước `example-generator`.
- User nói: "cho bài tập tương tự", "luyện thêm", "đọc gì thêm", "mở rộng kiến thức".

## Cấu trúc output (file `extensions/<tên-đề>_extended.md`)

```markdown
---
parent_solution: "solutions/<tên-đề>_solution.md"
created_at: "2026-05-09T..."
---

# Mở rộng & Luyện tập: [Tên bài]

## 🎯 Bài tập tham khảo (tự luyện)

### Bài luyện 1 — Cơ bản (★)
**Đề**: [Đề bài]
**Gợi ý**: [Gợi ý ngắn, không cho đáp án thẳng]
<details>
<summary>Đáp án rút gọn</summary>
[Đáp án + 2-3 dòng giải thích]
</details>

### Bài luyện 2 — Trung bình (★★)
[Tương tự, phức tạp hơn]

### Bài luyện 3 — Nâng cao (★★★)
[Có thể là case study tổng hợp, đòi nhiều khái niệm]

---

## 📖 Đào sâu kiến thức

### Khái niệm liên quan cần biết thêm
- **[Khái niệm 1]**: [Giải thích ngắn 3-4 câu] — Tham chiếu: [tên sách/tác giả/chương]
- **[Khái niệm 2]**: ...

### Mô hình/Lý thuyết nâng cao
[Trình bày 1 mô hình nâng cao liên quan, vd: từ Porter's 5 Forces → Porter's Diamond, hay Blue Ocean Strategy]

### Tranh luận học thuật
[Có quan điểm trái chiều nào không? VD: Porter vs. Mintzberg về định nghĩa chiến lược]

---

## 🤔 Câu hỏi tư duy phản biện

1. [Câu hỏi mở, không có đáp án "đúng" duy nhất]
2. [Câu hỏi liên hệ thực tiễn VN]
3. [Câu hỏi so sánh/đối chiếu khái niệm]

---

## 📚 Đọc thêm
- Sách: [Tên sách - Tác giả - Chương cụ thể nếu có]
- Bài báo học thuật: [Tên - Tác giả - Tạp chí (chỉ ghi nếu chắc chắn có thật)]
- Case Harvard Business Review (nếu có liên quan)
- Blog/Podcast/YouTube channel chuyên ngành VN: [The Forbes Vietnam, Brands Vietnam, Vietcetera Business...]

---

## 🔗 Liên kết với các bài khác trong môn
- Bài này là nền tảng cho: [Bài N, Bài M]
- Bài này cần dùng kiến thức từ: [Bài X, Bài Y]
```

## Nguyên tắc thiết kế bài tập tương tự

### Bài 1 (Cơ bản — ★)
- Cùng dạng, đổi số liệu nhẹ.
- Mục đích: kiểm tra SV nhớ công thức/quy trình.

### Bài 2 (Trung bình — ★★)
- Cùng dạng nhưng:
  - Thêm 1 ràng buộc mới (vd: tính NPV với rủi ro).
  - Hoặc đổi ngữ cảnh (từ ngành công nghiệp → dịch vụ).
- Mục đích: kiểm tra SV hiểu bản chất, không chỉ máy móc.

### Bài 3 (Nâng cao — ★★★)
- Tích hợp ≥ 2 khái niệm.
- Có thể là case mini với dữ liệu thật của một DN VN.
- Có thể yêu cầu SV phản biện một quyết định.
- Mục đích: chuẩn bị cho thi cuối kỳ/vấn đáp.

## Nguyên tắc cho phần "Đào sâu"

### Khi mở rộng khái niệm:
- Luôn nối với bài đang học, không bay quá xa.
- VD: bài về SWOT → mở rộng tới TOWS matrix (sử dụng SWOT để hành động).
- VD: bài về 4P → mở rộng tới 7P (dịch vụ) hoặc 4C (góc nhìn khách hàng).

### Khi giới thiệu nguồn đọc:
- CHỈ ghi sách/bài thực sự tồn tại và uy tín.
- An toàn: Strategic Management (Hill & Jones), Quản trị marketing (Kotler), Principles of Corporate Finance (Brealey & Myers), Operations Management (Heizer & Render), Human Resource Management (Dessler).
- Sách Việt Nam: NXB Trẻ, NXB Lao động, NXB Đại học Kinh tế Quốc dân.
- KHÔNG bịa tên sách hoặc DOI.

### Khi đặt câu hỏi tư duy:
- Tránh câu yes/no.
- Khuyến khích "phân tích", "so sánh", "đề xuất", "phản biện".

## Quy trình thực hiện
1. Đọc file solution + examples đã có.
2. Xác định khái niệm cốt lõi của bài.
3. Sinh 3 bài luyện theo đúng thang khó.
4. Sinh phần đào sâu (3-4 mục).
5. Sinh 3-5 câu tư duy phản biện.
6. Liệt kê 3-5 nguồn đọc thêm UY TÍN.
7. Liên kết với các bài khác (đọc metadata.yaml của môn).
8. Lưu file vào `extensions/`.
9. Cập nhật front-matter file solution: `extensions_file: ".../extensions/...md"`.

## Edge cases
- **Bài quá đặc thù** (vd: luật doanh nghiệp VN cụ thể) → bài luyện và đào sâu cũng nên về luật, không cố mở rộng sang nước khác.
- **Bài tích hợp nhiều môn** → ghi chú rõ "phần này liên quan môn X, Y, Z".
- **Bài trong môn cơ bản** → giữ phần nâng cao "vừa phải", không hù dọa SV năm 1.
