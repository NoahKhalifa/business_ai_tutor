---
reviewed_file: "quan-tri-nhan-luc-can-ban-luyen-tap-trac-nghiem-chuong-1_solution.md"
reviewed_at: "2026-07-14T14:45:00+07:00"
review_round: 1
overall_score: 7.6
verdict: "REVISE"
criteria:
  correctness: 9.5
  logic: 4.0
  calculation: 10.0
  vn_context: 8.0
  pedagogy: 5.0
---

# Báo cáo rà soát: Chương 1 - Tổng quan quản trị nhân lực

## Điểm tổng quan

**Tổng: 7.6/10 - Verdict: REVISE**

| Tiêu chí | Điểm | Ghi chú |
|---|---:|---|
| Chính xác khái niệm/công thức | 9.5 | 30/30 đáp án cuối khớp lần tự giải từ đề và lecture. |
| Logic lập luận | 4.0 | 90/120 option bullets (75%) chỉ là câu thay thế đáp án, không giải thích nội dung phương án. |
| Tính toán | 10.0 | Chương này không có phép tính; không phát hiện suy luận định lượng sai. |
| Phù hợp ngữ cảnh Việt Nam | 8.0 | Ví dụ Viettel/FPT hợp chủ đề, định tính và không bịa số liệu. |
| Sư phạm và chi tiết | 5.0 | Có ghi nhớ riêng nhưng không có “sai lầm thường gặp” đúng nghĩa cho từng câu. |

## Phạm vi kiểm tra độc lập

- Đọc đề 30 câu trước solution; tự lập đáp án từ lecture dòng 13-565.
- Kiểm tra riêng 9 câu phủ định: 2, 8, 13, 14, 16, 17, 20, 22, 30.
- Mở và kiểm tra đủ 30 cite-line; các khoảng dòng đều tồn tại và nằm trong Chương 1.

## Đối chiếu 30 đáp án

| Câu | Reviewer | Solution | Kết quả |
|---:|:---:|:---:|---|
| 1 | D | D | Khớp |
| 2 | B | B | Khớp |
| 3 | A | A | Khớp |
| 4 | C | C | Khớp |
| 5 | D | D | Khớp |
| 6 | A | A | Khớp |
| 7 | A | A | Khớp |
| 8 | D | D | Khớp |
| 9 | B | B | Khớp |
| 10 | A | A | Khớp |
| 11 | D | D | Khớp |
| 12 | B | B | Khớp |
| 13 | B | B | Khớp |
| 14 | A | A | Khớp |
| 15 | D | D | Khớp |
| 16 | C | C | Khớp |
| 17 | A | A | Khớp |
| 18 | C | C | Khớp |
| 19 | C | C | Khớp |
| 20 | C | C | Khớp |
| 21 | C | C | Khớp |
| 22 | A | A | Khớp |
| 23 | A | A | Khớp |
| 24 | C | C | Khớp |
| 25 | A | A | Khớp |
| 26 | B | B | Khớp |
| 27 | C | C | Khớp |
| 28 | D | D | Khớp |
| 29 | B | B | Khớp |
| 30 | D | D | Khớp |

## Phát hiện chi tiết

### Câu 15 và 22

**Điểm tốt:** hai câu dễ lẫn Đức trị/Pháp trị đều chọn đúng. Lecture dòng 315-321 đặt tuyển người theo tài và giáo dục ở Đức trị; dòng 361-373 đặt hình danh ở Pháp trị.

**Vấn đề mức vừa:** ba phương án sai chỉ được ghi “Giữ lại/chọn/loại” hoặc “Sai; so với...”. Cách này không nói vì sao A, B, C, D thuộc trường phái nào.

**Đề xuất sửa:** với mỗi lựa chọn, chỉ rõ dấu hiệu khái niệm: Đức trị = đức/nhân/lễ/giáo dục; Pháp trị = pháp/thế/thuật/hình danh/quyền biến.

### Câu 14, 16 và 17 - các câu phủ định về X/Y

Đáp án cuối đúng, nhưng option analysis không giúp sinh viên xử lý từ phủ định. Ví dụ Câu 17 cần nói rõ A trái với lecture dòng 455-461 về năng lực suy nghĩ và sáng tạo; B-D đều là giả định Y nên không phải đáp án.

### Lỗi hệ thống về per-option

Trích mẫu: “**B.** ... - Sai; chọn ...”, “**C.** ... - Sai; đáp án ...”, “**D.** ... - Sai; phải chọn ...”. Mẫu này xuất hiện ở toàn bộ ba phương án sai của cả 30 câu. Detector có báo cụm lặp mạnh; sau kiểm tra thủ công, đây là lỗi boilerplate thật chứ không phải false positive do thuật ngữ chương.

## Yêu cầu sửa

1. Giữ bảng đáp án hiện tại.
2. Viết lại 90 phân tích phương án sai bằng lý do khái niệm riêng, không chỉ nhắc lại phương án đúng.
3. Thêm một lỗi dễ mắc cụ thể cho từng câu, đặc biệt các câu có “không phải/không thuộc”.
4. Giữ cite-line hiện có nhưng thu hẹp khoảng dòng ở các câu chỉ cần một định nghĩa ngắn.

## Kết luận

Đáp án cuối có độ chính xác cao, nhưng tiêu chí logic dưới 6 vì per-option analysis không đạt yêu cầu bắt buộc của bài MCQ. Do đó bài chưa thể PASS.
