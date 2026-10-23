# Công cụ dựng đề cương ôn tập (PDF)

Thư mục này chứa mã nguồn dùng để tạo tệp
`DeCuongOnTap-KTGK1-VatLi10-2026-2027.pdf` ở thư mục gốc.

## Cách dựng lại

```bash
./tools/build.sh                     # ghi đè tệp PDF mặc định
./tools/build.sh /tmp/xem-thu.pdf    # ghi ra tệp khác
```

Script sẽ tự tạo virtualenv `.pdfenv/`, cài dependency trong
`requirements.txt` rồi gọi `render.py`.

## Cấu trúc

| Đường dẫn | Vai trò |
| --- | --- |
| `render.py` | Trình dựng PDF (fpdf2) + trình phân tích markup |
| `content/01_tongquan.md` | Phần A – Cấu trúc đề, ma trận đặc tả |
| `content/02_kienthuc.md` | Phần B – Hệ thống kiến thức (10 bài) |
| `content/03_dethi.md` | Phần C – Đề minh hoạ đúng ma trận (25 câu) |
| `content/04_dapan.md` | Phần D – Đáp án & hướng dẫn giải chi tiết |
| `content/05_nganhang.md` | Phần E – Ngân hàng câu hỏi bổ sung |
| `content/06_nhonhanh.md` | Phần F – Trang nhớ nhanh trước giờ thi |
| `../assets/fonts/` | Be Vietnam Pro (có đầy đủ dấu tiếng Việt) |

Về phông chữ: `assets/fonts/*.ttf` được tạo bằng cách gộp các tập con
`latin + latin-ext + vietnamese` của gói npm `@fontsource/be-vietnam-pro`
rồi chuyển từ `.woff2` sang `.ttf` bằng `fontTools`. Phông **Be Vietnam
Pro** được thiết kế riêng cho tiếng Việt nên hiển thị đúng toàn bộ dấu.
Các kí hiệu toán học (Δ, δ, √, ≤, ≥, ±, ≈, →, °, α, β, π …) không có trong
phông này sẽ tự động lấy từ phông dự phòng **DejaVu Sans** nhờ cơ chế
`set_fallback_fonts()` của fpdf2.

## Cú pháp markup

Mỗi dòng là một khối; dòng trống kết thúc đoạn.

| Kí hiệu | Ý nghĩa |
| --- | --- |
| `==Văn bản==` | Tiêu đề phần (tự xuống trang, nền màu) |
| `=Văn bản=` | Tiêu đề mục (H2, có trong mục lục) |
| `-Văn bản` | Tiêu đề bài (H3, có trong mục lục) |
| `--Văn bản` | Tiêu đề nhỏ (H4) |
| (dòng thường) | Đoạn văn (các dòng liên tiếp được nối lại) |
| `* Văn bản` | Gạch đầu dòng |
| `** Văn bản` | Gạch đầu dòng cấp 2 |
| `# Văn bản` | Danh sách tự đánh số |
| `~ Văn bản` | Hộp công thức (căn giữa) |
| `@ Văn bản` | Hộp “Cần nhớ” (xanh dương) |
| `! Văn bản` | Hộp “Mẹo nhớ” (xanh lá) |
| `? Văn bản` | Hộp “Lưu ý” (vàng cam) |
| `Q Văn bản` | Câu hỏi |
| `O Văn bản` | Phương án / ý a) b) c) d) |
| `K Văn bản` | Đáp án (xanh lá) |
| `E Văn bản` | Giải thích (xám) |
| `S Văn bản` | Bước giải |
| `\|a\|b\|c` | Bảng (dòng đầu là tiêu đề cột) |
| `///` | Ngắt trang |
| `;;` | Chú thích, bị bỏ qua |

**Ghi đè nhãn hộp:** bắt đầu hộp bằng `[NHÃN]`, ví dụ
`! [Lỗi thường gặp] Cộng đại số 24 + 6 = 30 km/h. Sai!`

**Định dạng trong dòng:** `**in đậm**`, `__in nghiêng__`.

> ⚠️ **Không dùng kí tự `|` bên trong ô bảng** – nó là kí tự phân tách cột.
> Hãy viết lại (ví dụ `v = | v₁ – v₂ |` thành `v = hiệu hai độ lớn v₁ và v₂`).

## Kiểm tra trước khi dựng

Nội dung được kiểm tra tự động về số cột bảng và dấu câu thừa ở tiêu đề.
Nếu bạn sửa nội dung, hãy chạy lại `./tools/build.sh` và mở tệp PDF để
đối chiếu.
