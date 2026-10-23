# Đề cương ôn tập giữa kì I — Vật lí 10 (2026–2027)

Kho tài liệu ôn thi được biên soạn **bám sát** tệp
`MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx` (ma trận đề + bản đặc tả đề kiểm tra giữa học kì I,
môn Vật lí lớp 10, năm học 2026–2027).

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| [`DE-CUONG-ON-TAP-GK1-VAT-LI-10.pdf`](DE-CUONG-ON-TAP-GK1-VAT-LI-10.pdf) | **Đề cương ôn tập hoàn chỉnh – 32 trang A4**, có mục lục, sơ đồ, hình vẽ, đề mô phỏng và lời giải |

## Cấu trúc đề cương

- **Trang bìa + mục lục chi tiết** – kèm bảng tra nhanh “đề hỏi gì → mở trang nào”.
- **Phần A – Hiểu đề để ôn đúng trọng tâm:** cấu trúc 4 phần của đề (18 câu TN + 2 câu đúng/sai
  8 ý + 2 câu tự luận ngắn + 3 ý tự luận vận dụng), ma trận phân bổ câu theo từng bài, biểu đồ
  độ “nặng” của từng bài, ba tầng kiến thức, phân bổ 50 phút, lộ trình ôn 7 ngày.
- **Phần B – Lý thuyết trọng tâm 10 bài:** mỗi bài gồm kiến thức cốt lõi, bảng so sánh, công thức,
  ví dụ mẫu, mẹo nhớ và bẫy thường gặp; kết thúc bằng sơ đồ tư duy tổng kết Chương II.
- **Phần C – Sổ tay công thức & kỹ năng:** toàn bộ công thức học kì I, bảng đổi đơn vị, quy tắc ghi
  kết quả đo, kỹ năng đọc đồ thị, 7 cặp khái niệm dễ nhầm, 6 dạng bài vận dụng, 12 câu đúng–sai kinh điển.
- **Phần D – Đề thi mô phỏng 50 phút:** biên soạn đúng từng ô của ma trận (18 câu TN, 2 câu × 4 ý,
  2 câu tự luận ngắn, 3 ý vận dụng) kèm **đáp án nhanh, lời giải chi tiết, bảng tự chấm và nhật ký lỗi sai**.
- **Phần E – Tự luyện:** 30 câu trắc nghiệm theo bài + 8 bài tự luận có đáp số.
- **Phần F – Checklist 30 mục**, 10 lỗi mất điểm oan, trang ghi chú.
- **Phụ lục – Trang bỏ túi:** một trang A4 gom toàn bộ công thức để đọc 10 phút trước giờ thi.

## Biên soạn lại PDF

```bash
pip install --break-system-packages reportlab
python3 scripts/build_decuong.py
```

Mã nguồn nằm trong `scripts/`:

```
scripts/
├── build_decuong.py        # dựng tài liệu, bìa, mục lục, header/footer, đánh số trang
└── decuong/
    ├── style.py            # font, màu, style, call-out box, bảng, khối câu hỏi
    ├── figures.py          # hình vector: đồ thị d–t, v–t, sơ đồ tư duy, biểu đồ ma trận
    ├── part_a.py           # Phần A – phân tích ma trận, chiến lược ôn
    ├── part_b1.py          # Phần B – Bài 1 → Bài 5
    ├── part_b2.py          # Phần B – Bài 6 → Bài 10 + sơ đồ tư duy
    ├── part_c.py           # Phần C – sổ tay công thức, kỹ năng
    ├── part_d.py           # Phần D – đề mô phỏng, đáp án, lời giải
    ├── part_e.py           # Phần E – ngân hàng câu hỏi tự luyện
    ├── part_f.py           # Phần F – checklist, lỗi thường gặp
    └── appendix.py         # Phụ lục – trang bỏ túi
```

## Ghi chú

Tệp `.docx` gốc là **ma trận + đặc tả**, không chứa nội dung từng câu hỏi, nên tài liệu này không
thể in lại “đề thật”. Phần D vì thế là **đề mô phỏng dựng đúng theo ma trận**; nếu có đề minh hoạ
hoặc đề chính thức, chỉ cần thay bộ câu hỏi ở Phần D, các phần còn lại giữ nguyên giá trị.
