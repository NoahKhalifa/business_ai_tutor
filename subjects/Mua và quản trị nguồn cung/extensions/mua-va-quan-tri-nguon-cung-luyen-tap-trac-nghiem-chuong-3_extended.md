---
parent_solution: "solutions/mua-va-quan-tri-nguon-cung-luyen-tap-trac-nghiem-chuong-3_solution.md"
created_at: "2026-06-11T22:20:00+07:00"
---

# Mở rộng & Luyện tập: Chương 3 - Chất lượng, số lượng, tồn kho và chi phí mua

## 🎯 Bài tập tham khảo (tự luyện)

### Bài luyện 1 — Cơ bản (★)
**Đề**: Nêu bốn quyết định cơ bản trong mua vật tư và giải thích ngắn ý nghĩa từng quyết định.

**Gợi ý**: Nghĩ theo chất lượng, số lượng, thời gian và chi phí.

<details>
<summary>Đáp án rút gọn</summary>
Doanh nghiệp cần mua đúng chất lượng, đủ số lượng, đúng thời điểm và với chi phí hợp lý. Bốn quyết định này giúp sản xuất không gián đoạn nhưng không làm tồn kho hoặc chi phí vượt mức.
</details>

### Bài luyện 2 — Trung bình (★★)
**Đề**: Một công ty đặt hàng 12 lần/năm, mỗi lần 1.000 đơn vị. Nếu chi phí đặt hàng cao và chi phí lưu kho thấp, công ty nên cân nhắc thay đổi gì?

**Gợi ý**: Liên hệ logic EOQ, không cần tính số cụ thể.

<details>
<summary>Đáp án rút gọn</summary>
Khi chi phí đặt hàng cao và lưu kho thấp, doanh nghiệp có xu hướng tăng lượng đặt mỗi lần để giảm số lần đặt hàng, miễn là không gây lỗi thời, thiếu không gian hoặc rủi ro chất lượng.
</details>

### Bài luyện 3 — Nâng cao (★★★)
**Đề**: Phân tích rủi ro khi áp dụng VMI cho một chuỗi bán lẻ Việt Nam. Đề xuất điều kiện triển khai để tránh thiếu hàng và ứ đọng hàng.

**Gợi ý**: Xem xét chia sẻ dữ liệu, năng lực nhà cung cấp, mức tồn kho mục tiêu và trách nhiệm khi sai lệch dự báo.

<details>
<summary>Đáp án rút gọn</summary>
VMI giúp giảm tải đặt hàng và cải thiện bổ sung tồn kho, nhưng rủi ro nằm ở dữ liệu bán hàng sai, nhà cung cấp thiếu năng lực hoặc mục tiêu tồn kho không rõ. Cần SLA, dữ liệu thời gian thực, ngưỡng min-max và cơ chế xử lý hàng chậm luân chuyển.
</details>

---

## 📖 Đào sâu kiến thức

- **EOQ**: Mô hình cân bằng chi phí đặt hàng và chi phí lưu kho, hữu ích nhất khi nhu cầu tương đối ổn định.
- **Dự trữ an toàn**: Cần khi nhu cầu hoặc thời gian giao hàng biến động, nhưng mức dự trữ cao làm tăng vốn bị giam.
- **ESI**: Nhà cung cấp tham gia sớm giúp cải thiện thiết kế, vật liệu và khả năng sản xuất.

## 🤔 Câu hỏi tư duy phản biện

1. Mua đúng lúc có luôn tốt hơn giữ tồn kho an toàn không?
2. Khi nào nhà cung cấp nên được quyền quản lý tồn kho của người mua?
3. Nếu chỉ tối ưu chi phí mua, doanh nghiệp có thể đánh đổi chất lượng ra sao?

## 📚 Đọc thêm

- Sách: *Operations Management* - Heizer, Render & Munson.
- Sách: *Inventory Management and Production Planning and Scheduling* - Silver, Pyke & Peterson.
- Sách: *Supply Chain Management* - Chopra & Meindl.

## 🔗 Liên kết với các bài khác trong môn

- Liên hệ Chương 4 về quan hệ nhà cung cấp.
- Là nền cho Chương 5 về JIT, VMI và chiến lược nguồn cung.
