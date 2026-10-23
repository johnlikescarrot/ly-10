# Đề cương ôn tập giữa kì I — Vật lí 10

## Tài liệu hoàn chỉnh

**[Mở bản PDF: Đề cương ôn tập giữa kì I — Vật lí 10 (2026–2027)](DE_CUONG_ON_TAP_GIUA_KI_I_VAT_LY_10_2026-2027.pdf)**

Tài liệu được biên soạn từ toàn bộ tệp `MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx`. Tệp nguồn là **ma trận–đặc tả**, không chứa đề thi hay đáp án chính thức. Vì vậy, các thẻ Hỏi–Đáp và đề minh họa trong đề cương là nội dung luyện tập được xây dựng mới để phủ đầy đủ phạm vi đặc tả, không phải đề thi chính thức của trường.

Bản PDF gồm 47 trang A4, có mục lục liên kết, bookmark, bốn hình minh họa và các liên kết nguồn đối chiếu. Nội dung chính:

- Đủ 10 bài từ *Làm quen với Vật lí* đến *Sự rơi tự do*.
- 99 thẻ Hỏi–Đáp, ví dụ có lời giải theo bước, 25 bẫy thường gặp và 48 mục checklist.
- Đề minh họa 50 phút bám cấu trúc ma trận: 18 câu nhiều lựa chọn; 2 câu đúng–sai, mỗi câu 4 ý; 2 câu trả lời ngắn; phần tự luận gồm 1 ý Hiểu và 2 ý Vận dụng.
- Đáp án, lời giải chi tiết và gợi ý chấm cho toàn bộ đề minh họa.
- Bảng phân bố theo ma trận, phương pháp ôn tập và danh mục nguồn chuyên môn dùng để đối chiếu.

## Cấu trúc thư mục

- `de-cuong-on-tap-giua-ki-i-vat-ly-10.md`: nguồn nội dung có thể chỉnh sửa.
- `DE_CUONG_ON_TAP_GIUA_KI_I_VAT_LY_10_2026-2027.pdf`: bản PDF hoàn chỉnh.
- `scripts/build_pdf.py`: chương trình dựng PDF bằng ReportLab.
- `scripts/make_figures.py`: chương trình tạo bốn hình minh họa bằng Pillow.
- `assets/`: các hình PNG được nhúng vào tài liệu.

## Tái dựng PDF

Yêu cầu Python 3.10 trở lên và bộ font **DejaVu Sans**. Trên Debian/Ubuntu, font thường đã có sẵn tại `/usr/share/fonts/truetype/dejavu`. Có thể đặt biến môi trường `DEJAVU_FONT_DIR` nếu font nằm ở thư mục khác; thư mục đó cần có `DejaVuSans.ttf`, `DejaVuSans-Bold.ttf`, `DejaVuSansMono.ttf` và `DejaVuSansMono-Bold.ttf`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Chỉ cần chạy lại khi muốn tái tạo các hình minh họa.
python scripts/make_figures.py

# Tạo hoặc cập nhật PDF từ nguồn Markdown.
python scripts/build_pdf.py
```

Lệnh cuối ghi đè bản PDF ở thư mục gốc. Các dòng `<!-- PAGEBREAK -->` trong nguồn Markdown là chỉ thị ngắt trang có chủ đích để giữ bố cục bản in; không xóa chúng khi chỉnh sửa nội dung nếu chưa kiểm tra lại PDF.
