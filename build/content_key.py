# -*- coding: utf-8 -*-
"""PHẦN D – Đáp án và lời giải chi tiết."""

from reportlab.lib.units import cm
from doc_kit import *  # noqa
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle


def sol(d, label, ans, text):
    head = Paragraph("<b>%s</b>&nbsp;&nbsp;<font color='#1E8449'><b>%s</b></font>" % (label, ans),
                     st("sH", fontSize=9.1, leading=13, spaceBefore=3, spaceAfter=1))
    body = Paragraph(F(text), st("sB", fontSize=8.9, leading=13, leftIndent=14, spaceAfter=4))
    d.story += [head, body]


def build(d: Doc):
    d.pb()
    d.h1("ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT", kicker="Phần D · Tra cứu sau khi đã làm xong đề")

    # ---------------------------------------------------------- bảng đáp án
    d.h2("D.1 · Đáp án nhanh Phần I")
    letters = ["C", "C", "B", "D", "B", "A", "C", "B", "D", "D", "C", "D", "A", "B", "B", "A", "A", "C"]
    head1 = ["Câu"] + [str(i) for i in range(1, 10)]
    row1 = ["Đáp án"] + letters[:9]
    head2 = ["Câu"] + [str(i) for i in range(10, 19)]
    row2 = ["Đáp án"] + letters[9:]
    t = Table([head1, row1, head2, row2], colWidths=[2.0 * cm] + [1.68 * cm] * 9)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("BACKGROUND", (0, 2), (-1, 2), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("TEXTCOLOR", (0, 2), (-1, 2), colors.white),
        ("BACKGROUND", (0, 1), (-1, 1), GREEN_BG), ("BACKGROUND", (0, 3), (-1, 3), GREEN_BG),
        ("FONTNAME", (0, 0), (-1, -1), "VNSans-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.6),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    d.story += [Spacer(1, 2), t, Spacer(1, 8)]

    d.h2("D.2 · Đáp án Phần II (Đúng – Sai)")
    d.table(
        ["Câu", "a)", "b)", "c)", "d)", "Ghi chú nhanh"],
        [
            ["<b>1</b>", "<b>Đ</b>", "<b>Đ</b>", "<b>S</b>", "<b>S</b>",
             "c) đi ngược chiều dương; d) quãng đường 40 km"],
            ["<b>2</b>", "<b>Đ</b>", "<b>Đ</b>", "<b>S</b>", "<b>S</b>",
             "c) giây cuối đi 2 m; d) xe đã dừng ở giây thứ 5"],
        ],
        widths=[1.8 * cm, 1.4 * cm, 1.4 * cm, 1.4 * cm, 1.4 * cm, 10.0 * cm],
        aligns=["C", "C", "C", "C", "C", "L"], font_size=8.6)

    # ---------------------------------------------------------- lời giải P.I
    d.h2("D.3 · Lời giải chi tiết Phần I")
    d.p("<i>Mỗi câu ghi rõ đáp án, lý do chọn và lý do loại các phương án còn lại khi cần.</i>", "Small")

    SOL = [
        ("Câu 1", "C", "Vật lí nghiên cứu các sự vật, hiện tượng của tự nhiên, các dạng vận động của vật chất và "
                      "năng lượng. Xã hội loài người, phản ứng hoá học, cấu trúc tế bào lần lượt thuộc Sử – Xã hội, "
                      "Hoá học, Sinh học."),
        ("Câu 2", "C", "Không bao giờ nếm hoặc ngửi trực tiếp hoá chất trong phòng thực hành. Ba phương án còn lại "
                      "đều là hành vi an toàn bắt buộc."),
        ("Câu 3", "B", "Tam giác đều – viền đen – nền vàng là biển <b>cảnh báo nguy hiểm</b>. Biển cấm có dạng tròn "
                      "viền đỏ, biển bắt buộc dạng tròn nền xanh, biển chỉ dẫn dạng chữ nhật nền xanh lá."),
        ("Câu 4", "D", "Đo vận tốc phải đo trực tiếp quãng đường và thời gian rồi tính qua công thức v = s/t → đây là "
                      "phép đo gián tiếp. Ba phương án còn lại đọc kết quả ngay trên dụng cụ."),
        ("Câu 5", "B", "Độ dịch chuyển là vectơ nối vị trí đầu với vị trí cuối, đặc trưng cho sự thay đổi vị trí "
                      "(cả độ lớn và hướng). Độ dài quỹ đạo là quãng đường."),
        ("Câu 6", "A", "s = 3 + 4 = 7 km. Hai đoạn vuông góc nên |Δd| = √(3² + 4²) = 5 km."),
        ("Câu 7", "C", "Vật đi 10 m rồi quay lại 10 m → s = 20 m; trở về điểm xuất phát nên Δd = 0."),
        ("Câu 8", "B", "Tốc độ trung bình dùng <b>quãng đường</b>: v = s/Δt. Công thức v = Δd/Δt là vận tốc trung bình."),
        ("Câu 9", "D", "d không đổi theo thời gian → đồ thị là đường thẳng nằm ngang (song song trục thời gian)."),
        ("Câu 10", "D", "v = Δd/Δt = 20/5 = 4 m/s (chính là độ dốc của đồ thị)."),
        ("Câu 11", "C", "Gia tốc đặc trưng cho sự biến thiên nhanh hay chậm của vận tốc; đơn vị m/s²."),
        ("Câu 12", "D", "Chậm dần đều khi a ngược chiều với v (a·v &lt; 0). Lưu ý a không nhất thiết âm – điều đó "
                       "còn phụ thuộc chiều dương."),
        ("Câu 13", "A", "Hệ thức độc lập thời gian: v² − v₀² = 2ad. Các phương án B, C là hai công thức khác (đúng "
                       "nhưng không phải “hệ thức liên hệ ba đại lượng”), D sai dấu."),
        ("Câu 14", "B", "Nhanh dần đều: độ lớn vận tốc tăng đều theo thời gian, v = v₀ + at. Quãng đường tỉ lệ với t² "
                       "chứ không phải t."),
        ("Câu 15", "B", "v = v₀ + at = 0 + 0,5·8 = 4 m/s."),
        ("Câu 16", "A", "Rơi tự do là rơi chỉ dưới tác dụng của trọng lực (bỏ qua lực cản không khí). Không phải "
                       "mọi vật rơi trong không khí đều là rơi tự do."),
        ("Câu 17", "A", "t = √(2h/g) = √(2·80/10) = √16 = 4 s."),
        ("Câu 18", "C", "Khi bỏ qua lực cản không khí, mọi vật rơi với cùng gia tốc g nên chạm đất cùng lúc, "
                       "không phụ thuộc khối lượng."),
    ]
    for label, ans, text in SOL:
        sol(d, label, "→ " + ans, text)

    # ---------------------------------------------------------- lời giải P.II
    d.h2("D.4 · Lời giải chi tiết Phần II")

    d.p("<b>Câu 1.</b> Đọc đồ thị theo từng đoạn:", "BodyTight")
    d.bullets([
        "<b>a) ĐÚNG.</b> 0 → 2 h: d tăng 0 → 20 km → v = 20/2 = 10 km/h.",
        "<b>b) ĐÚNG.</b> 2 → 3 h: d = 20 km không đổi → vật đứng yên.",
        "<b>c) SAI.</b> 3 → 4 h: d giảm 20 km → vật chuyển động <b>ngược</b> chiều dương với tốc độ 20 km/h.",
        "<b>d) SAI.</b> s = 20 (đi) + 20 (về) = <b>40 km</b>. Độ dịch chuyển cả hành trình mới bằng 0.",
    ])

    d.p("<b>Câu 2.</b> Chọn chiều dương là chiều chuyển động, v₀ = 20 m/s; xe dừng ở t = 5 s nên a = (0 − 20)/5 = −4 m/s².",
        "BodyTight")
    d.bullets([
        "<b>a) ĐÚNG.</b> a = −4 m/s² (ngược chiều dương → chuyển động chậm dần).",
        "<b>b) ĐÚNG.</b> d = (v₀ + v)t/2 = (20 + 0)·5/2 = 50 m.",
        "<b>c) SAI.</b> s(5) = 50 m; s(4) = 20·4 − ½·4·16 = 48 m → giây cuối đi 50 − 48 = <b>2 m</b> (không phải 4 m).",
        "<b>d) SAI.</b> Xe dừng hẳn ở giây thứ 5; từ 5 s đến 6 s xe không chuyển động nên quãng đường vẫn là "
        "<b>50 m</b>, không phải 60 m. Đây là bẫy “áp dụng công thức sau khi vật đã dừng”.",
    ])

    # ---------------------------------------------------------- lời giải P.III
    d.h2("D.5 · Lời giải chi tiết Phần III")
    d.p("<b>Câu 1 (2,2 điểm kiến thức – mức Biết).</b>", "BodyTight")
    d.bullets([
        "<b>a)</b> <b>Tốc độ trung bình</b> là đại lượng đặc trưng cho mức độ nhanh, chậm của chuyển động, được "
        "xác định bằng quãng đường đi được chia cho thời gian đi hết quãng đường đó: <b>v = s/Δt</b>. "
        "Đơn vị: m/s (hoặc km/h).",
        "<b>b)</b> <b>Vận tốc trung bình</b> là đại lượng vectơ, được xác định bằng thương số của độ dịch chuyển "
        "và thời gian dịch chuyển: <b>v = Δd/Δt</b> (v là đại lượng vectơ). Đơn vị: m/s. Vận tốc cho biết vật chuyển động nhanh, chậm "
        "và theo hướng nào.",
        "<b>c)</b> Ví dụ: một người đi 3 km về phía đông rồi 4 km về phía bắc trong 2 h. Quãng đường 7 km → tốc độ "
        "trung bình 3,5 km/h; độ dịch chuyển 5 km hướng đông – bắc → độ lớn vận tốc trung bình 2,5 km/h. "
        "Như vậy hai đại lượng khác nhau về bản chất (vô hướng – vectơ) và về giá trị.",
    ])
    d.p("<b>Câu 2 (2,6 – mức Hiểu).</b> Chọn chiều dương hướng xuống, gốc thời gian lúc thả, v₀ = 0; g = 10 m/s².", "BodyTight")
    d.bullets([
        "<b>a)</b> h = ½gt² → t = √(2h/g) = √(2·45/10) = √9 = <b>3 s</b>.",
        "<b>b)</b> v = gt = 10·3 = <b>30 m/s</b> (hoặc v = √(2gh) = √(2·10·45) = 30 m/s).",
        "<b>c)</b> Quãng đường trong 2 s đầu: s₂ = ½·10·2² = 20 m. Quãng đường trong giây thứ 3: "
        "45 − 20 = <b>25 m</b>. (Kiểm tra bằng công thức: Δs = ½g(2n − 1) = 5·5 = 25 m.)",
    ])

    # ---------------------------------------------------------- lời giải P.IV
    d.h2("D.6 · Lời giải chi tiết Phần IV")
    d.p("<b>Câu 1 (2,2 – mức Hiểu).</b> Gọi (1) là ca nô, (2) là nước, (3) là bờ, ta có (dạng vectơ): v₁₃ = v₁₂ + v₂₃.", "BodyTight")
    d.bullets([
        "<b>a)</b> Ca nô bơi vuông góc với dòng chảy nên hai vectơ vuông góc:<br/>"
        "v₁₃ = √(v₁₂² + v₂₃²) = √(8² + 6²) = √100 = <b>10 m/s</b>.",
        "<b>b)</b> Gọi α là góc lệch giữa hướng chuyển động thực (v₁₃) và hướng bơi của ca nô (v₁₂):<br/>"
        "tanα = v₂₃/v₁₂ = 6/8 = 0,75 → α ≈ <b>37°</b> (lệch về phía hạ lưu).<br/>"
        "Như vậy ca nô bị dòng nước đẩy lệch 37° so với hướng mũi ca nô.",
    ])

    d.p("<b>Câu 2 (2,5 – mức Vận dụng).</b> Đổi 72 km/h = 20 m/s. Chọn chiều dương là chiều chuyển động, "
        "a = −5 m/s² (chuyển động chậm dần đều).", "BodyTight")
    d.bullets([
        "<b>a)</b> v = v₀ + at → 0 = 20 − 5t → t = <b>4 s</b>.",
        "<b>b)</b> d = (v₀ + v)t/2 = (20 + 0)·4/2 = <b>40 m</b> "
        "(hoặc d = 20·4 − ½·5·4² = 80 − 40 = 40 m).",
        "<b>c)</b> Quãng đường trong 3 s đầu: s₃ = 20·3 − ½·5·9 = 60 − 22,5 = 37,5 m.<br/>"
        "Quãng đường trong giây thứ 4: 40 − 37,5 = <b>2,5 m</b>.",
    ])

    d.p("<b>Câu 3 (2,5 – mức Vận dụng).</b> Chọn gốc toạ độ tại O, chiều dương là chiều chuyển động, "
        "gốc thời gian lúc khảo sát.", "BodyTight")
    d.bullets([
        "<b>a)</b> Xe A: v₀ = 0, a = 1 m/s² → <b>x(A) = 0,5t²</b> (m).<br/>"
        "Xe B: chuyển động thẳng đều, v = 15 m/s, xuất phát tại x₀ = 200 m → <b>x(B) = 200 + 15t</b> (m).",
        "<b>b)</b> Hai xe gặp nhau khi x(A) = x(B):<br/>"
        "0,5t² = 200 + 15t ⇔ t² − 30t − 400 = 0 ⇔ t = 40 s (nhận) hoặc t = −10 s (loại).<br/>"
        "Vị trí gặp: x = 0,5·40² = <b>800 m</b> (cách O 800 m).",
        "<b>c)</b> Vận tốc xe A: v(A) = at = 1·40 = <b>40 m/s</b>. Xe B chuyển động đều: "
        "<b>v(B) = 15 m/s</b>.",
        "<i>Nhận xét:</i> xe B xuất phát trước một đoạn nhưng xe A tăng tốc nên đuổi kịp; tại thời điểm gặp, "
        "xe A đã chạy nhanh hơn nhiều và sẽ vượt lên trước.",
    ])

    # ---------------------------------------------------------- tự chấm
    d.h2("D.7 · Bảng tự chấm và chẩn đoán")
    d.table(
        ["Phần", "Cách tính điểm", "Điểm tối đa"],
        [
            ["I", "Mỗi câu đúng 0,25 điểm (18 câu)", "4,5"],
            ["II", "Mỗi câu 1,25 điểm; mỗi ý đúng ≈ 0,31 điểm", "2,5"],
            ["III", "Mỗi câu 0,5 điểm", "1,0"],
            ["IV", "Câu 1: 0,5 điểm; câu 2: 0,75 điểm; câu 3: 0,75 điểm", "2,0"],
            ["<b>Tổng</b>", "", "<b>10,0</b>"],
        ],
        widths=[1.9 * cm, 11.0 * cm, 4.2 * cm], aligns=["C", "L", "C"], font_size=8.3)

    d.table(
        ["Điểm", "Mức", "Việc cần làm ngay"],
        [
            ["&lt; 5", "Mất gốc công thức",
             "Học lại Phần A chuyên đề 05, 09, 10; viết 4 công thức CĐTBĐĐ 10 lần; làm lại 18 câu Phần I."],
            ["5 – 6,5", "Có công thức nhưng vụng",
             "Luyện mỗi ngày 3 bài hãm phanh + 2 bài rơi tự do; tập đổi đơn vị km/h → m/s."],
            ["6,5 – 8", "Khá, còn sai bẫy",
             "Đọc kĩ Phần B.4 (14 lỗi); làm lại các câu sai và ghi rõ lý do sai vào sổ tay."],
            ["8 – 9", "Tốt",
             "Luyện đề trọn 50 phút; tối ưu tốc độ Phần I (≤ 20 phút); soát đơn vị."],
            ["9 – 10", "Xuất sắc",
             "Giữ nhịp: mỗi ngày 1 đề; tập các bài vận dụng cao (đổi chiều, hai vật gặp nhau)."],
        ],
        widths=[1.7 * cm, 4.0 * cm, 11.4 * cm], aligns=["C", "L", "L"], font_size=8.2)
