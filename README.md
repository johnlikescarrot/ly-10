# Đề cương ôn tập Giữa học kì I – Vật lí 10 (2026–2027)

Tài liệu ôn thi được biên soạn bám sát tệp **`MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx`**
(ma trận đặc tả đề kiểm tra giữa kì I môn Vật lí lớp 10, 70% trắc nghiệm + 30% tự luận, 50 phút).

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| `De_cuong_on_tap_GK1_Vat_li_10_2026-2027.pdf` | **Đề cương hoàn chỉnh – 35 trang, có bookmark, mục lục ghi số trang** |
| `src/` | Mã nguồn Python (ReportLab) sinh ra PDF |
| `assets/fonts/` | Font Be Vietnam Pro + DejaVu Sans (dự phòng cho ký tự toán: Δ, δ, √, ≤…) |

## Cấu trúc đề cương

- **Bìa + mục lục** – lộ trình 3 vòng ôn tập, kế hoạch 3 ngày.
- **Phần A – Bản đồ đề thi**: cấu trúc 4 phần (18 TN · 2 câu Đúng/Sai · 2 câu trả lời ngắn ·
  3 câu tự luận), phân bổ câu theo 10 đơn vị kiến thức, 9 "khuôn" câu hỏi gần như chắc chắn xuất hiện.
- **Phần B – Lý thuyết trọng tâm 10 bài**: mỗi bài có *theo ma trận* (số câu + mức độ), định nghĩa,
  bảng so sánh, công thức, ví dụ mẫu có lời giải, **mẹo nhớ**, **bẫy thường gặp**, câu tự kiểm tra.
- **Phần C – Bộ công thức & sơ đồ tư duy**: 23 công thức xếp theo đại lượng, 4 dạng bài,
  4 hình mẫu đồ thị `d – t`, sơ đồ tư duy 4 nhánh, bảng "một câu – một bài".
- **Phần D – Đề minh họa chuẩn ma trận**: 25 câu / 31 lệnh hỏi / 10 điểm, lập đúng số câu và đúng
  mức độ theo ma trận (10 Biết + 8 Hiểu ở phần I; 6 Biết + 2 Hiểu ở phần II; 1 Biết + 1 Hiểu ở
  phần III; 1 Hiểu + 2 Vận dụng ở phần IV).
- **Phần E – Đáp án & lời giải chi tiết**: bảng đáp án nhanh, lời giải từng câu, chỉ rõ bẫy của
  phương án nhiễu, thang điểm 0,25 đ cho từng bước tự luận.
- **Phần F – 12 bẫy thường gặp** và **Phần G – Checklist + chiến thuật 50 phút**.

## Ghi chú về nguồn

Tệp `.docx` gốc **chỉ chứa ma trận đặc tả và bản mô tả mức độ nhận thức**, không kèm đề thi và
đáp án. Vì vậy toàn bộ lý thuyết được triển khai phủ kín 10 đơn vị kiến thức của ma trận, còn đề
ở Phần D là **đề minh họa được lập đúng ma trận** (đúng số câu – đúng mức độ – đúng đơn vị kiến
thức) kèm đáp án và lời giải đầy đủ.

## Xuất lại PDF

```bash
pip install reportlab pymupdf
python3 src/build_pdf.py
```
