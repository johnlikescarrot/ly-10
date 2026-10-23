# Đề cương ôn tập Giữa học kì I — Vật lí 10 (2026–2027)

Đề cương ôn tập được biên soạn **bám sát ma trận đặc tả** của đề kiểm tra giữa học kì I
môn Vật lí 10, năm học 2026–2027.

## 📄 Sản phẩm

| Tệp | Mô tả |
|---|---|
| [`De-cuong-on-tap-Giua-HKI-Vat-li-10-2026-2027.pdf`](De-cuong-on-tap-Giua-HKI-Vat-li-10-2026-2027.pdf) | **Đề cương hoàn chỉnh — 35 trang, khổ A4** |
| [`MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx`](MA%20TRẬN%20ĐẶC%20TẢ%20KTGK%20I%20L10-%202026.docx) | Tài liệu gốc do giáo viên cung cấp |

## 🎯 Nội dung tài liệu

| Phần | Nội dung |
|---|---|
| **Phần 0** | Giải mã ma trận: 4 phần thi, thang điểm 10, trọng số từng bài, chiến lược 50 phút, lộ trình ôn 7 ngày |
| **Phần 1** | Lý thuyết trọng tâm **10 bài** — công thức, bảng so sánh, mẹo nhớ, bẫy thường gặp, tự kiểm tra 60 giây |
| **Phần 2** | Tổng hợp công thức 1 trang · sơ đồ tư duy · **15 bẫy** · bảng đổi đơn vị |
| **Phần 3** | **Đề minh hoạ bám đúng ma trận**: 18 TN + 2 câu Đúng–Sai (8 ý) + 2 trả lời ngắn + 2 tự luận |
| **Phần 4** | **Đáp án và lời giải chi tiết từng câu** |
| **Phụ lục** | Checklist kiến thức · checklist dụng cụ · 10 lời nhắc trước giờ thi |

### Độ phủ ma trận

Toàn bộ **31 lượt hỏi** trong ma trận gốc (10 đơn vị kiến thức × 4 mức độ nhận thức)
đều được ánh xạ tới một câu hỏi cụ thể trong đề minh hoạ — xem bảng kiểm tra độ phủ ở Phần 3.

| Đơn vị kiến thức | Lượt hỏi | Tỉ lệ |
|---|---:|---:|
| 2.5. Chuyển động thẳng biến đổi đều | 9 | 29,0% |
| 2.2. Tốc độ và vận tốc | 5 | 16,1% |
| 2.3. Đồ thị độ dịch chuyển – thời gian | 4 | 12,9% |
| 2.6. Sự rơi tự do | 4 | 12,9% |
| 2.1. Độ dịch chuyển và quãng đường | 3 | 9,7% |
| 1.2. Quy tắc an toàn phòng thực hành | 2 | 6,5% |
| 2.4. Chuyển động biến đổi. Gia tốc | 2 | 6,5% |
| 1.1. Làm quen với Vật lí | 1 | 3,2% |
| 1.3. Sai số trong phép đo | 1 | 3,2% |

## 🛠 Dựng lại PDF

Yêu cầu: Python 3.11+, `fpdf2`, `fonttools`, `pymupdf` (chỉ để kiểm tra).

```bash
python3 -m venv .venv
.venv/bin/pip install fpdf2 fonttools pymupdf

cd build
../.venv/bin/python build.py ../De-cuong-on-tap-Giua-HKI-Vat-li-10-2026-2027.pdf
```

Mã nguồn nằm trong `build/`:

| Tệp | Vai trò |
|---|---|
| `engine.py` | Bộ layout PDF (đo chữ, ngắt dòng, bảng tự co giãn, khối công thức, callout) |
| `content_a.py` | Phần 0 + Bài 1–5 |
| `content_b.py` | Bài 6–10 + Phần 2 |
| `content_c.py` | Phần 3 (đề) + Phần 4 (đáp án) + Phụ lục |
| `dsl.py` | Helper cho block DSL |
| `build.py` | Lắp ráp, mục lục, trang bìa |
| `fonts/` | Be Vietnam Pro (chữ chính) + Roboto Mono (công thức) + DejaVu Sans (dự phòng ký hiệu) |

## 📚 Nguồn tham chiếu

- Ma trận đặc tả đề kiểm tra giữa kì I — Vật lí 10, năm học 2026–2027 (tài liệu gốc).
- Vật lí 10 — Chương trình GDPT 2018, bộ sách *Kết nối tri thức với cuộc sống*
  (Chương I: Bài 1–3; Chương II: Bài 4–10).
- Quyết định 764/QĐ-BGDĐT ngày 08/3/2024 về cấu trúc định dạng đề thi và cách tính điểm
  phần trắc nghiệm Đúng–Sai.

> Đề minh hoạ ở Phần 3 được dựng bám sát ma trận gốc nhằm mục đích ôn tập,
> **không phải đề thi chính thức**.
