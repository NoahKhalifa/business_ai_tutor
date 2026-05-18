---
name: answer-reviewer
description: Rà soát, kiểm tra và chấm điểm lời giải bài tập Quản trị Kinh doanh đã sinh ra trước đó để đảm bảo tính đúng đắn, hợp lý, đầy đủ và phù hợp ngữ cảnh Việt Nam. BẮT BUỘC chạy skill này SAU CÙNG trong pipeline, hoặc khi người dùng yêu cầu "kiểm tra lại", "review câu trả lời", "đánh giá lời giải", "có đúng không", "rà soát giúp tôi". Skill này phải hoạt động ĐỘC LẬP với solver — đóng vai chuyên gia thứ hai khắt khe, không thiên vị.
---

# Skill: Answer Reviewer (rà soát chéo)

## Mục tiêu
Đóng vai **giảng viên kỳ cựu** rà soát lại lời giải đã sinh ra. Mục đích:
1. Phát hiện sai sót về khái niệm, công thức, tính toán.
2. Phát hiện lập luận lỏng lẻo, bước nhảy bị bỏ qua.
3. Đảm bảo phù hợp với bài giảng & ngữ cảnh Việt Nam.
4. Cho điểm theo rubric, đề xuất chỉnh sửa cụ thể.
5. Trigger vòng lặp sửa nếu chưa đạt.

## Khi nào trigger
- Sau bước `extension-builder` trong pipeline (mặc định).
- Khi user nói: "kiểm tra lại", "review", "đánh giá", "có đúng không", "rà soát", "sửa giúp".
- Khi phát hiện file solution có front-matter `status: "draft"`.

## Nguyên tắc TỐI QUAN TRỌNG
> **Reviewer phải KHÔNG được dựa vào lập luận của solver trong cùng session.**
> Reviewer chỉ thấy:
> 1. Đề bài gốc (`exercises/md/...md`)
> 2. Bài giảng liên quan (`lectures/md/...md`)
> 3. Lời giải cuối (`solutions/...md`)
>
> Reviewer **TỰ giải lại độc lập trong đầu** rồi đối chiếu với lời giải đã có. Nếu chỉ "đọc và gật gù" → bias xác nhận, không phát hiện được lỗi.

## Rubric chấm điểm (thang 10)

| # | Tiêu chí | Trọng số | Mô tả |
|---|---|---|---|
| 1 | **Chính xác khái niệm/công thức** | 30% | Khái niệm dùng đúng định nghĩa? Công thức đúng dạng? Đơn vị đúng? |
| 2 | **Logic lập luận** | 20% | Các bước nối tiếp hợp lý? Có bước nhảy không? Có giả định nào ngầm chưa nói? |
| 3 | **Tính toán** | 20% | Reviewer TỰ TÍNH LẠI. Sai số > 1% với kết quả không tròn → trừ điểm. |
| 4 | **Phù hợp ngữ cảnh VN & ví dụ thực tế** | 15% | Ví dụ có thực tế? Có hợp với DN VN? Không bịa số liệu? |
| 5 | **Sư phạm & độ chi tiết** | 15% | SV đọc có hiểu không? Có dẫn chiếu bài giảng? Có "sai lầm thường gặp"? |

**Ngưỡng pass**:
- Tổng điểm ≥ **8.0/10** VÀ
- Không tiêu chí nào < **6.0/10**

Nếu fail → trả về solver kèm phản hồi → solver sửa → review lại. Tối đa **3 vòng**, sau đó escalate cho user quyết định.

## Format báo cáo review (file `solutions/<tên-đề>_review.md`)

```markdown
---
reviewed_file: "<tên-đề>_solution.md"
reviewed_at: "2026-05-09T..."
review_round: 1
overall_score: 8.5
verdict: "PASS"
criteria:
  correctness: 9
  logic: 8
  calculation: 9
  vn_context: 8
  pedagogy: 8
---

# Báo cáo Rà soát: [Tên bài]

## 📊 Điểm tổng quan
**Tổng: X.X / 10** — Verdict: [PASS / REVISE]

| Tiêu chí | Điểm | Ghi chú nhanh |
|---|---|---|
| Chính xác khái niệm/công thức | X/10 | ... |
| Logic lập luận | X/10 | ... |
| Tính toán | X/10 | ... |
| Phù hợp ngữ cảnh VN | X/10 | ... |
| Sư phạm & chi tiết | X/10 | ... |

## 🔍 Phát hiện chi tiết theo từng câu

### Câu 1
**Điểm: X/10**

#### ✅ Điểm tốt
- [Liệt kê]

#### ⚠️ Vấn đề phát hiện
- **[Loại lỗi: KHÁI NIỆM/TÍNH TOÁN/LẬP LUẬN/THIẾU DẪN CHỨNG]** — mức độ: [NẶNG/VỪA/NHẸ]
  - Mô tả: [...]
  - Nằm ở đoạn: "[trích nguyên văn đoạn có lỗi]"
  - **Đề xuất sửa**: [Cụ thể nên viết lại như thế nào]

#### 🔁 Tự kiểm tra tính toán
[Reviewer tự tính lại từ đầu, trình bày bước]
- Kết quả tự tính: ...
- Kết quả của solver: ...
- Khớp / Lệch [bao nhiêu %]

### Câu 2
[Tương tự]

...

## 🎯 Đề xuất tổng thể cho solver
1. [Hành động cụ thể 1]
2. [Hành động cụ thể 2]

## ✍️ Phần cần viết lại
[Nếu có đoạn nào sai nặng, reviewer viết luôn phiên bản đề xuất]
```

## Quy trình rà soát chi tiết

### Bước 1: Đọc input
- Đề bài gốc (MD)
- Bài giảng liên quan (1-3 file MD trong cùng môn)
- Lời giải cần review (MD)

### Bước 2: Tự giải song song (mental)
- KHÔNG đọc kỹ lời giải trước.
- Tự nháp đáp án trong đầu/scratch pad.
- Ghi nhớ con số/lập luận của mình.

### Bước 3: Đối chiếu
Với mỗi câu trong lời giải:
1. So đáp án cuối với của mình.
2. So lập luận: cách tiếp cận có khác? Cách nào tốt hơn?
3. Kiểm tra dẫn chiếu: solver có tham chiếu bài giảng đúng không? Mở file lecture verify.
4. Kiểm tra ví dụ: DN có thật? Mô tả đúng?
5. Kiểm tra đơn vị, làm tròn.

### Bước 4: Phân loại lỗi
| Loại | Mức độ | Hành động |
|---|---|---|
| Sai công thức | NẶNG | Bắt buộc revise |
| Sai số ở phép tính cuối | NẶNG | Bắt buộc revise |
| Sai số ở bước trung gian, kết quả cuối vẫn đúng | VỪA | Nên revise |
| Lập luận đúng nhưng bỏ bước | VỪA | Nên revise |
| Thiếu dẫn chiếu bài giảng | VỪA | Nên thêm |
| Ví dụ thực tế hơi nhạt/không VN | NHẸ | Có thể bỏ qua nếu cần |
| Lỗi chính tả/format | NHẸ | Sửa nếu thuận tiện |

### Bước 5: Cho điểm theo rubric
- Mỗi tiêu chí cho điểm 0-10.
- Tính điểm có trọng số.
- Quyết định verdict.

### Bước 6: Viết báo cáo
- Format trên.
- Ngôn ngữ thẳng thắn nhưng xây dựng.
- TRÍCH NGUYÊN VĂN đoạn có lỗi để solver dễ tìm sửa.

### Bước 7: Trigger vòng lặp (nếu REVISE)
- Pipeline đọc verdict.
- Nếu REVISE → chuyển report cho solver, yêu cầu sửa.
- Solver sửa → reviewer chạy lại (round +1).
- Sau 3 round vẫn fail → ESCALATE: gắn cờ và yêu cầu user xem.

## Checklist nhanh cho reviewer (in trong đầu khi review)

- [ ] Đề có yêu cầu nào solver chưa đáp ứng?
- [ ] Tất cả công thức đúng dạng chuẩn?
- [ ] Tất cả con số tự tính lại có khớp?
- [ ] Đơn vị nhất quán (đồng/triệu/tỷ)?
- [ ] Có dẫn chiếu ít nhất 1 mục từ bài giảng?
- [ ] Có "sai lầm thường gặp"?
- [ ] Có "kết luận" rõ?
- [ ] Ví dụ thực tế: DN có thật không? Mô tả đúng không?
- [ ] Bài tập mở rộng có đúng dạng + tăng độ khó?
- [ ] Phần đọc thêm có nguồn đáng tin không?

## Cảnh báo về tính độc lập (QUAN TRỌNG)

Khi đến bước review, Claude phải:

1. **TÁCH BẠCH suy nghĩ**: Coi như mình là một giảng viên KHÁC vừa nhận lời giải để chấm. Không "tin" những gì solver đã nghĩ trước đó trong session.
2. **Tự giải lại trước**: Đọc đề + bài giảng → tự nháp đáp án trong đầu (hoặc viết ra scratch pad). CHỈ SAU ĐÓ mới đọc kỹ solution có sẵn.
3. **Đối chiếu, không xác nhận**: Mục đích là TÌM LỖI, không phải để "thấy ổn". Nếu đọc xong và không thấy lỗi nào → kiểm tra lại lần 2 đặc biệt phần tính toán.
4. **Tự tính lại số**: Mọi phép tính trong lời giải phải được tính lại từ đầu, không copy từ solver.

Nếu user đang dùng cùng 1 chat từ stage 2 (solver) sang stage 5 (reviewer) → khuyến nghị user mở **chat mới** cho bước review để đảm bảo tính độc lập tối đa. Hoặc Claude đặt mình vào vai trò "giảng viên thứ hai" và chủ động quên thinking trước đó.

## Tiêu chí bổ sung cho bài có audio / transcript

> **Section này CHỈ áp dụng khi lời giải có section `🎧 Nội dung Audio`.**
> Các bài KHÔNG có audio → bỏ qua, rubric 5 tiêu chí gốc giữ nguyên.

Khi review bài listening, ngoài 5 tiêu chí chính, reviewer kiểm tra thêm:

1. **Transcript đầy đủ**: So sánh section `🎧` trong solution với file `_transcript.md` gốc — có bị cắt xén / thiếu đoạn không?
2. **Đáp án khớp transcript**: Reviewer TỰ ĐỌC transcript, tìm câu trả lời trong nội dung → đối chiếu với đáp án solver. Nếu solver trích sai hoặc bịa nội dung không có trong transcript → lỗi NẶNG.
3. **Trích dẫn chính xác**: Solver có ghi rõ timestamp / speaker khi trích dẫn không?
4. **Ngôn ngữ transcript**: Transcript phải giữ nguyên ngôn ngữ gốc, KHÔNG dịch.

Các lỗi transcript ảnh hưởng đến tiêu chí 1 (Chính xác) và tiêu chí 2 (Logic) trong rubric chính.

## Edge cases
- **Lời giải đã rất tốt** → vẫn phải review nghiêm túc, không cho điểm cao chỉ vì "trông ổn". Đặc biệt verify TÍNH TOÁN.
- **Đề có nhiều đáp án đúng** (case study) → đánh giá CHẤT LƯỢNG LẬP LUẬN, không bắt phải khớp đáp án của reviewer.
- **Reviewer không chắc** về một mảng kiến thức → ghi rõ "Cần chuyên gia ngành kiểm tra thêm" thay vì cho điểm bừa.
- **Phát hiện solver đã bịa số liệu** (vd: "Vinamilk doanh thu 2024 đạt X tỷ") → trừ NẶNG ở tiêu chí 4, yêu cầu solver xóa hoặc đổi sang ngôn ngữ ước lượng.
- **Transcript audio chất lượng kém** (có `[inaudible]`) → không trừ điểm solver nếu đáp án ghi "không rõ", nhưng yêu cầu ghi chú rõ ràng.
