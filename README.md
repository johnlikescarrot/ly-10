# Đề cương ôn tập Vật lí 10 – Kiểm tra giữa kỳ I (2026–2027)

Tài liệu ôn tập tiếng Việt được biên soạn từ **MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx**
(tài liệu nguồn của nhà trường), kèm **toàn bộ câu hỏi và đáp án** của bài kiểm tra giữa kỳ I
được xây dựng để *hiện thực hoá 100% các ô của ma trận đặc tả*.

## 📄 Sản phẩm chính

**[ĐỀ CƯƠNG ÔN TẬP VẬT LÝ 10 - KIỂM TRA GIỮA KỲ I 2026-2027.pdf](ĐỀ%20CƯƠNG%20ÔN%20TẬP%20VẬT%20LÝ%2010%20-%20KIỂM%20TRA%20GIỮA%20KỲ%20I%202026-2027.pdf)** – 34 trang, A4, có mục lục bấm được
(đánh số trang tự động) và header/footer theo từng phần.

### Cấu trúc tài liệu

| Phần | Nội dung |
|------|----------|
| **Bìa** | Thông tin đề thi, hướng dẫn sử dụng, 10 đơn vị kiến thức, mẹo ôn tập |
| **Mục lục** | Liên kết tới từng phần, có số trang |
| **Phần 0** | Cấu trúc đề thi, **ma trận đặc tả gốc**, đặc tả nội dung – mức độ nhận thức, phân bổ điểm |
| **Phần 1** | **Đề cương ôn tập chi tiết cho 10 đơn vị kiến thức**: kiến thức cần đạt (theo đặc tả) → mục tiêu → nội dung trọng tâm → *ghi nhớ nhanh* → bài tập mẫu có lời giải → *lỗi thường gặp* → câu hỏi tương ứng trong đề |
| **Phần 2** | **Toàn bộ câu hỏi và đáp án**: 18 câu trắc nghiệm (A–D, kèm giải thích) · 2 câu tự luận × 4 ý (lời giải từng ý) · 2 câu Phần III · 3 câu Phần IV · bảng đáp án tổng hợp |
| **Phần 3** | Bảng **đối chiếu ma trận ↔ câu hỏi** – chứng minh mọi ô của ma trận đều được hiện thực hoá |
| **Phụ lục** | Bảng công thức tra nhanh, quy ước kí hiệu, đơn vị đo & quy đổi, checklist tự ôn, lời nhắc cuối bài |

### Đối chiếu với ma trận đặc tả

| Phần | Cấu trúc | Mức độ |
|------|----------|--------|
| I – Trắc nghiệm | 18 câu | 10 “Biết” + 8 “Hiểu” |
| II – Tự luận | 2 câu × 4 ý = 8 ý | 6 ý “Biết” + 2 ý “Hiểu” |
| III | 2 câu | 1 “Biết” + 1 “Hiểu” |
| IV | 3 câu | 1 “Hiểu” + 2 “Vận dụng” |
| **Tổng** | **25 câu / 10 đơn vị kiến thức** | 70% trắc nghiệm + 30% tự luận · 50 phút |

## 🛠 Dựng lại tài liệu

Yêu cầu: Python 3.9+, `reportlab`, `fonttools` (dùng để vá phông), `pymupdf` (kiểm tra/xem trước).

```bash
python -m venv .venv && . .venv/bin/activate
pip install reportlab fonttools pymupdf

python tools/build_de_cuong.py          # sinh lại tệp PDF ở thư mục gốc
python tools/verify.py                  # tự kiểm tra đối chiếu ma trận ↔ câu hỏi
python tools/preview.py <file.pdf> out 1,2,3   # xuất trang ra PNG để duyệt
```

`tools/patch_fonts.py` chỉ cần chạy một lần: nó dịch nét dấu thanh (U+0304) của phông
Be Vietnam Pro để dấu “x̄” nằm đúng trên chữ `x` (ReportLab không áp dụng GPOS
mark-to-base). Script có tệp đánh dấu `.macron_patched` nên chạy lại vẫn an toàn.

## 📁 Cấu trúc thư mục

```
MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx      # tài liệu nguồn (không sửa)
ĐỀ CƯƠNG ÔN TẬP VẬT LÝ 10 - ....pdf       # sản phẩm chính
tools/
  build_de_cuong.py      # bộ dựng PDF (bố cục, bảng, khung, mục lục)
  content_units.py       # nội dung đề cương của 10 đơn vị kiến thức
  content_questions.py   # bộ câu hỏi – đáp án của bài kiểm tra giữa kỳ I
  fonts_lib.py           # đăng ký phông + bộ chuyển đổi markup sang ReportLab
  patch_fonts.py         # vá dấu thanh trên chữ (chạy 1 lần)
  preview.py / verify.py # tiện ích kiểm tra
  fonts/                 # Be Vietnam Pro + DejaVu Sans (ký hiệu toán học)
```

## 🔤 Phông chữ

* **Be Vietnam Pro** — phông chữ chính, hỗ trợ đầy đủ dấu tiếng Việt (SIL Open Font License 1.1).
* **DejaVu Sans** — phông dự phòng cho các ký hiệu toán học mà Be Vietnam Pro chưa có
  (Δ, δ, π, √, →, ⇒, ≤, ≥, ± …).

## 📄 Nguồn

Nội dung kiến thức, cấu trúc đề thi và ma trận đặc tả được trích từ
`MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx`. Bộ câu hỏi – đáp án trong Phần 2 được biên soạn
theo đúng ma trận đó nhằm đủ câu hỏi cho từng ô, kèm lời giải và đối chiếu minh bạch ở Phần 3.
