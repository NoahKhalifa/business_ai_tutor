# Quy ước trình bày công thức toán

> File này là chuẩn chung cho **mọi MD** sinh ra trong project: lecture đầy đủ, lecture summary, solution, exercise, extension. Mọi skill phải tham chiếu file này khi gặp công thức.

## 1. Quy tắc chính: dùng LaTeX trong cú pháp dollar

### Inline (trong đoạn văn)
Bao công thức bằng `$...$`:
```markdown
Điểm hòa vốn được tính bằng $BEP = FC / (P - VC)$, trong đó $FC$ là chi phí cố định.
```
Render: Điểm hòa vốn được tính bằng $BEP = FC / (P - VC)$.

### Block (đứng riêng 1 khối)
Bao bằng `$$...$$` trên dòng riêng:
```markdown
Công thức NPV:

$$
NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t} - C_0
$$

Trong đó: $CF_t$ là dòng tiền năm $t$, $r$ là tỷ suất chiết khấu.
```

## 2. Khi nào dùng inline, khi nào dùng block

| Tình huống | Inline `$...$` | Block `$$...$$` |
|---|---|---|
| Công thức ngắn 1 dòng, ít biến | ✅ | ❌ |
| Có phân số phức tạp `\frac{}{}` | ❌ | ✅ |
| Có tổng `\sum`, tích phân `\int`, giới hạn `\lim` | ❌ | ✅ |
| Có ma trận, hệ phương trình | ❌ | ✅ |
| Cần đánh số/tham chiếu | ❌ | ✅ |
| Trong bảng so sánh công thức | ✅ (ngắn nhất có thể) | ❌ |

## 3. Cú pháp LaTeX hay dùng trong Quản trị Kinh doanh

### Phân số
```latex
$\frac{tử}{mẫu}$              → tử/mẫu (compact)
$\dfrac{tử}{mẫu}$             → tử/mẫu (display, to hơn — dùng inline khi muốn rõ)
```

### Tổng & tích
```latex
$\sum_{t=0}^{n} x_t$          → Σ từ t=0 đến n
$\prod_{i=1}^{k} (1+r_i)$     → Π
```

### Lũy thừa & chỉ số dưới
```latex
$(1+r)^t$                     → mũ
$CF_t$, $x_{ij}$              → chỉ số dưới (nhiều ký tự dùng {})
```

### Ký hiệu đặc biệt
```latex
$\Delta$ → Δ          $\sigma$ → σ        $\mu$ → μ
$\alpha$ → α          $\beta$ → β         $\theta$ → θ
$\approx$ → ≈         $\geq$ → ≥          $\leq$ → ≤
$\times$ → ×          $\div$ → ÷          $\pm$ → ±
$\infty$ → ∞          $\Rightarrow$ → ⇒    $\to$ → →
```

### Căn thức
```latex
$\sqrt{x}$            → √x
$\sqrt[n]{x}$         → căn bậc n
```

### Hệ phương trình / ma trận
```latex
$$
\begin{cases}
P_1 + P_2 = 100 \\
2P_1 - P_2 = 50
\end{cases}
$$

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$
```

## 4. Bộ công thức chuẩn cho Quản trị Kinh doanh

Dùng đúng các template này khi gặp các bài toán phổ biến:

### Tài chính
| Khái niệm | Công thức chuẩn |
|---|---|
| Điểm hòa vốn (sản lượng) | $BEP_Q = \dfrac{FC}{P - VC}$ |
| Điểm hòa vốn (doanh thu) | $BEP_R = \dfrac{FC}{1 - \dfrac{VC}{P}}$ |
| NPV | $NPV = \sum_{t=0}^{n} \dfrac{CF_t}{(1+r)^t}$ |
| IRR | $\sum_{t=0}^{n} \dfrac{CF_t}{(1+IRR)^t} = 0$ |
| Thời gian hoàn vốn (PP) | $PP = \dfrac{\text{Vốn đầu tư}}{\text{Dòng tiền hằng năm}}$ |
| ROA | $ROA = \dfrac{\text{Lợi nhuận ròng}}{\text{Tổng tài sản}}$ |
| ROE | $ROE = \dfrac{\text{Lợi nhuận ròng}}{\text{Vốn chủ sở hữu}}$ |
| Đòn bẩy hoạt động (DOL) | $DOL = \dfrac{\Delta EBIT / EBIT}{\Delta Q / Q}$ |
| WACC | $WACC = \dfrac{E}{V} \cdot R_e + \dfrac{D}{V} \cdot R_d \cdot (1-T)$ |

### Vận hành / chuỗi cung ứng
| Khái niệm | Công thức |
|---|---|
| EOQ | $EOQ = \sqrt{\dfrac{2DS}{H}}$ |
| Tồn kho an toàn | $SS = z \cdot \sigma_d \cdot \sqrt{L}$ |
| ROP | $ROP = d \cdot L + SS$ |

### Marketing / khách hàng
| Khái niệm | Công thức |
|---|---|
| CLV (đơn giản) | $CLV = \dfrac{\text{ARPU} \times \text{margin}}{\text{churn rate}}$ |
| Market share | $MS = \dfrac{\text{Doanh thu DN}}{\text{Tổng doanh thu thị trường}}$ |
| Thị phần tương đối | $RMS = \dfrac{\text{Thị phần DN}}{\text{Thị phần đối thủ lớn nhất}}$ |

## 5. Quy tắc bắt buộc khi viết công thức

1. **Luôn định nghĩa biến**: ngay sau công thức, liệt kê các biến và đơn vị.
```markdown
   $$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$
   
   Trong đó:
   - $CF_t$: dòng tiền năm $t$ (đồng)
   - $r$: tỷ suất chiết khấu (%)
   - $n$: số năm dự án
```

2. **Đơn vị rõ ràng**: VND/triệu/tỷ, %, hệ số. Không trộn đơn vị.

3. **Số liệu áp vào công thức**: trước khi tính, viết lại công thức với số:
```markdown
   Áp số liệu đề bài:
   $$NPV = \frac{500}{(1+0.1)^1} + \frac{600}{(1+0.1)^2} - 1000 = -38.84 \text{ triệu VND}$$
```

4. **Tránh chữ Việt trong LaTeX có dấu**: LaTeX render lỗi với "Doanh thu", "Lợi nhuận"... Dùng `\text{}`:
```latex
   $$\text{Lợi nhuận} = \text{Doanh thu} - \text{Chi phí}$$
```

5. **Một công thức = một khối**: không nhồi nhiều công thức vào 1 block, trừ khi đó là hệ phương trình.

## 6. Khi không nên dùng LaTeX

- **Trong filename, heading, alt text của ảnh**: render không ổn định
- **Trong commit message git**: không render
- **Khi công thức quá đơn giản** (vd: "1 + 1 = 2") — viết thẳng nhanh hơn

## 7. Test render

Sau khi viết, mở Markdown Preview trong VS Code (`Ctrl+Shift+V`):
- Nếu thấy `$E = mc^2$` đúng dạng → OK
- Nếu thấy `$E = mc^2$` text thô → cài extension "Markdown+Math" hoặc bật setting `markdown.math.enabled`