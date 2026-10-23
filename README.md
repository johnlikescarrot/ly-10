# Đề cương ôn tập Giữa học kì I – Vật lí 10 (2026 – 2027)

Tài liệu ôn tập biên soạn bám sát **“MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I – MÔN VẬT LÝ LỚP 10, NĂM HỌC 2026 – 2027”**.

## Sản phẩm

| Tệp | Nội dung |
|---|---|
| `De-cuong-on-tap-Giua-HKI-Vat-li-10-2026-2027.pdf` | **Sản phẩm chính** – 40 trang A4, có mục lục nhấp được và 92 bookmark. |
| `build/` | Mã nguồn Python (ReportLab) dựng ra PDF – có thể sửa nội dung và build lại. |
| `MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx` | Văn bản gốc do giáo viên cung cấp. |

## Cấu trúc tài liệu

- **Phần 0 – Phân tích ma trận & đặc tả:** cấu trúc đề, phân bố 31 đơn vị hỏi theo từng bài, yêu cầu cần đạt.
- **Phần A – Lý thuyết 10 chuyên đề:** khái niệm, công thức, ví dụ mẫu có lời giải, bẫy thường gặp, mẹo nhớ (kèm 2 hình vẽ đồ thị d–t và v–t).
- **Phần B – Sổ tay công thức:** 18 công thức kèm đơn vị, bảng đổi đơn vị, sơ đồ chọn công thức, 14 lỗi mất điểm.
- **Phần C – Đề luyện tập số 01:** 18 câu trắc nghiệm + 2 câu đúng/sai × 4 ý + 2 câu tự luận + 3 câu vận dụng, đúng cấu trúc 50 phút; có khung viết bài.
- **Phần D – Đáp án và lời giải chi tiết:** đáp án nhanh, lời giải từng câu, bảng tự chấm và chẩn đoán theo mức điểm.
- **Phần E – Chiến lược & kế hoạch:** dòng thời gian 50 phút, kế hoạch ôn 7 ngày, checklist 12 mục, sổ tay lỗi cá nhân.

## Lưu ý về nguồn tài liệu

Văn bản gốc là **ma trận + đặc tả** (quy định nội dung, mức độ nhận thức và số câu của từng phần), **không kèm danh sách câu hỏi cụ thể**. Vì vậy bộ câu hỏi ở Phần C được biên soạn **bám 1:1 theo đúng ma trận** (đủ số câu, đúng đơn vị kiến thức và mức độ), kèm đáp án và lời giải chi tiết.

## Build lại PDF

```bash
python3 -m venv .venv && .venv/bin/pip install reportlab fonttools
.venv/bin/python build/build_pdf.py out.pdf
```

Yêu cầu: font DejaVu (`/usr/share/fonts/truetype/dejavu`) – hỗ trợ đầy đủ dấu tiếng Việt và ký hiệu vật lí.
