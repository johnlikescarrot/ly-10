# Đề cương ôn tập giữa kì I – Vật lí lớp 10

Đề cương ôn tập toàn diện cho bài kiểm tra giữa kì I môn Vật lí lớp 10 (năm học 2026–2027),
được biên soạn trực tiếp từ tài liệu **“MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx”** trong repo này.

## Sản phẩm chính

📄 **[DE-CUONG-ON-TAP-GIUA-KI-I-VAT-LI-10.pdf](DE-CUONG-ON-TAP-GIUA-KI-I-VAT-LI-10.pdf)** — 29 trang A4, in ra học trực tiếp được.

| Phần | Nội dung |
|---|---|
| Phần 0 | Giải mã ma trận: đề có 18 câu trắc nghiệm + 2 câu Đúng/Sai (8 ý) + 2 câu trả lời ngắn + 3 câu tự luận = 31 mục chấm; bài 2.5 chiếm tỉ trọng cao nhất (9/31) |
| Phần A | Kiến thức cốt lõi A1–A9 theo đúng 9 đơn vị của ma trận (hộp “Nhớ nhanh”, bảng so sánh, mẹo nhớ, bẫy hay gặp, ví dụ mẫu) |
| Phần B | Đề mẫu đúng 100% cấu trúc ma trận (50 phút) + đáp án và lời giải chi tiết từng câu/ý |
| Phần C | Ngân hàng 30 câu luyện thêm theo từng đơn vị, có đáp án và giải thích |
| Phần D + Phụ lục | Phiếu công thức 1 trang, lộ trình ôn tập, bảng đối chiếu phủ 100% yêu cầu của bản đặc tả |

> **Lưu ý trung thực:** tài liệu gốc là *ma trận + bản đặc tả* (bản thiết kế của đề thi),
> không chứa sẵn câu hỏi cụ thể của đề thi thật. Vì vậy đề cương bảo đảm tính đầy đủ bằng cách
> phủ 100% ô ma trận và 100% yêu cầu đặc tả (xem Phụ lục đối chiếu trong PDF), kèm một đề mẫu
> đúng cấu trúc và ngân hàng câu hỏi đổi dạng — mọi câu hỏi thật thuộc phạm vi này đều đã được học và luyện ít nhất một lần.

## Tái dựng PDF từ mã nguồn

Mã nguồn dựng PDF nằm trong thư mục [`de-cuong/`](de-cuong/) (ReportLab + font DejaVu có sẵn trên Debian/Ubuntu):

```bash
python3 -m venv /tmp/venv
/tmp/venv/bin/pip install -r de-cuong/requirements.txt
/tmp/venv/bin/python de-cuong/build_pdf.py
```

Lệnh cuối sẽ ghi lại file `DE-CUONG-ON-TAP-GIUA-KI-I-VAT-LI-10.pdf` ở thư mục gốc của repo.

- `de-cuong/build_pdf.py` — khung tài liệu, trang bìa, Phần 0, mục lục tự động
- `de-cuong/content_theory.py` — Phần A (lí thuyết)
- `de-cuong/content_exam.py` — Phần B (đề mẫu + đáp án)
- `de-cuong/content_practice.py` — Phần C, D và Phụ lục đối chiếu
- `de-cuong/helpers.py` — style, bảng, hộp công thức và hình vẽ (đồ thị d–t, v–t, cộng vectơ)

## Tài liệu gốc

- `MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx` — ma trận phân bổ câu hỏi (Phần I–IV × Biết/Hiểu/Vận dụng)
  và bản đặc tả 10 đơn vị kiến thức của đề kiểm tra giữa kì I, Vật lí 10.
