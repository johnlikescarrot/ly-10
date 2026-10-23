# -*- coding: utf-8 -*-
"""PHẦN C – Đề luyện tập bám sát ma trận."""

from reportlab.lib.units import cm
from reportlab.lib import colors
from doc_kit import *  # noqa
from reportlab.platypus import Paragraph, Table, TableStyle, Spacer, KeepTogether

SQ = st("SQ", fontSize=9.4, leading=14.4, spaceAfter=0)
STAG = st("STAG", fontSize=7.4, leading=10, textColor=GRAY, alignment=TA_RIGHT)
SOPT = st("SOPT", fontSize=9.2, leading=13.6)


def mcq(d, num, stem, opts, tag):
    head = Table([[Paragraph("<b>Câu %d.</b>&nbsp;&nbsp;%s" % (num, F(stem)), SQ),
                   Paragraph(tag, STAG)]],
                 colWidths=[14.9 * cm, 2.2 * cm])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    rows = [[Paragraph("<b>A.</b> %s" % F(opts[0]), SOPT), Paragraph("<b>B.</b> %s" % F(opts[1]), SOPT)],
            [Paragraph("<b>C.</b> %s" % F(opts[2]), SOPT), Paragraph("<b>D.</b> %s" % F(opts[3]), SOPT)]]
    opt = Table(rows, colWidths=[8.5 * cm, 8.6 * cm])
    opt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                             ("LEFTPADDING", (0, 0), (-1, -1), 16),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                             ("TOPPADDING", (0, 0), (-1, -1), 1),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    d.story += [KeepTogether([head, Spacer(1, 2), opt, Spacer(1, 7)])]


def tf(d, num, stem, rows, tag):
    head = Table([[Paragraph("<b>Câu %d.</b>&nbsp;&nbsp;%s" % (num, F(stem)), SQ),
                   Paragraph(tag, STAG)]],
                 colWidths=[14.9 * cm, 2.2 * cm])
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (-1, -1), 0),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    data = [[Paragraph("<b>Phát biểu</b>", S["TblHead"]), Paragraph("<b>Đúng</b>", S["TblHead"]),
             Paragraph("<b>Sai</b>", S["TblHead"])]]
    for letter, txt in rows:
        data.append([Paragraph("<b>%s)</b>&nbsp; %s" % (letter, F(txt)), S["TblCell"]),
                     Paragraph("□", S["TblCellC"]), Paragraph("□", S["TblCellC"])])
    t = Table(data, colWidths=[13.3 * cm, 1.9 * cm, 1.9 * cm], repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (2, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    d.story += [KeepTogether([head, t, Spacer(1, 8)])]


def essay(d, num, stem, parts, tag):
    d.story.append(Paragraph("<b>Câu %d.</b>&nbsp;&nbsp;%s&nbsp;&nbsp;<font size='7.4' color='#5F6B7A'>(%s)</font>"
                             % (num, F(stem), tag), SQ))
    for p in parts:
        d.story.append(Paragraph(F(p), st("SP", fontSize=9.3, leading=14, leftIndent=14, spaceAfter=1.5)))
    d.story.append(Spacer(1, 8))


def build(d: Doc):
    d.pb()
    d.h1("ĐỀ LUYỆN TẬP SỐ 01", kicker="Phần C · Bám 1:1 theo ma trận – Thời gian 50 phút")
    d.p("<b>Họ và tên:</b> ……………………………………  <b>Lớp:</b> …………  "
        "<b>Điểm:</b> …………  <b>Nhận xét:</b> ……………………………………", "Small")

    d.table(
        ["Phần", "Nội dung", "Số câu", "Điểm"],
        [
            ["I", "Trắc nghiệm nhiều lựa chọn", "18 câu (câu 1 → 18)", "4,5"],
            ["II", "Trắc nghiệm đúng – sai", "2 câu × 4 ý", "2,5"],
            ["III", "Tự luận ngắn", "2 câu", "1,0"],
            ["IV", "Tự luận vận dụng", "3 câu", "2,0"],
        ],
        widths=[1.6 * cm, 8.6 * cm, 4.6 * cm, 2.3 * cm],
        aligns=["C", "L", "C", "C"], font_size=8.4)
    d.p("<i>Hướng dẫn: không dùng tài liệu. Với Phần I chọn một phương án; với Phần II đánh dấu □ vào cột "
        "Đúng hoặc Sai; với Phần III – IV trình bày lời giải và ghi rõ đơn vị. Nhãn nhỏ bên phải mỗi câu "
        "(ví dụ “2.5 · NB”) cho biết câu đó thuộc đơn vị kiến thức nào và ở mức độ nào – dùng để tra cứu "
        "sau khi làm bài.</i>", "Small")

    # ------------------------------------------------------------ PHẦN I
    d.h2("PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (18 câu)")
    d.p("<i>Thí sinh trả lời từ câu 1 đến câu 18. Mỗi câu chỉ chọn một phương án.</i>", "Small")

    Q = [
        ("Đối tượng nghiên cứu chủ yếu của Vật lí là",
         ["sự hình thành và phát triển của xã hội loài người.",
          "các phản ứng hoá học giữa các chất.",
          "các sự vật, hiện tượng xảy ra trong tự nhiên.",
          "cấu trúc và chức năng của tế bào sống."], "1.1 · NB"),
        ("Hành vi nào sau đây <b>không</b> an toàn khi làm thí nghiệm trong phòng thực hành Vật lí?",
         ["Buộc gọn tóc dài trước khi làm thí nghiệm.",
          "Đeo kính bảo hộ khi sử dụng hoá chất.",
          "Tự ý nếm thử dung dịch để nhận biết.",
          "Đọc kĩ hướng dẫn sử dụng thiết bị trước khi dùng."], "1.2 · NB"),
        ("Biển báo có dạng tam giác đều, viền đen, nền vàng thuộc nhóm biển",
         ["cấm.", "cảnh báo nguy hiểm.", "bắt buộc.", "chỉ dẫn."], "1.2 · TH"),
        ("Phép đo nào sau đây là phép đo <b>gián tiếp</b>?",
         ["Đo chiều dài mặt bàn bằng thước cuộn.",
          "Đo thời gian chạy 100 m bằng đồng hồ bấm giây.",
          "Đo khối lượng một vật bằng cân điện tử.",
          "Đo vận tốc bằng cách đo quãng đường và thời gian rồi tính."], "1.3 · NB"),
        ("Độ dịch chuyển là",
         ["đại lượng vô hướng, luôn có giá trị dương.",
          "đại lượng vectơ, đặc trưng cho sự thay đổi vị trí của vật.",
          "độ dài quỹ đạo mà vật đã đi được.",
          "quãng đường vật đi được trong một giây."], "2.1 · NB"),
        ("Một người đi 3 km về phía đông rồi 4 km về phía bắc. Quãng đường và độ dịch chuyển của người đó là",
         ["7 km và 5 km.", "5 km và 7 km.", "7 km và 7 km.", "1 km và 5 km."], "2.1 · TH"),
        ("Một vật đi từ A đến B (AB = 10 m) rồi quay trở lại A. Quãng đường và độ dịch chuyển của vật là",
         ["10 m và 10 m.", "20 m và 20 m.", "20 m và 0.", "0 và 20 m."], "2.1 · TH"),
        ("Công thức tính <b>tốc độ trung bình</b> của một chuyển động là",
         ["v = Δd/Δt.", "v = s/Δt.", "v = a·t.", "v = v₀ + at."], "2.2 · NB"),
        ("Trên đồ thị độ dịch chuyển – thời gian, vật đứng yên được biểu diễn bằng",
         ["đường thẳng dốc lên.", "đường cong parabol.", "đường thẳng dốc xuống.",
          "đường thẳng nằm ngang."], "2.3 · NB"),
        ("Một vật chuyển động thẳng đều có đồ thị độ dịch chuyển – thời gian là đường thẳng đi qua gốc toạ độ "
         "và điểm (5 s; 20 m). Vận tốc của vật là",
         ["2 m/s.", "5 m/s.", "100 m/s.", "4 m/s."], "2.3 · TH"),
        ("Gia tốc là đại lượng đặc trưng cho",
         ["sự thay đổi vị trí của vật theo thời gian.",
          "mức độ nhanh, chậm của chuyển động.",
          "sự biến thiên nhanh hay chậm của vận tốc.",
          "quãng đường vật đi được trong một đơn vị thời gian."], "2.4 · NB"),
        ("Một vật chuyển động thẳng chậm dần đều. Nhận định nào sau đây <b>đúng</b>?",
         ["Gia tốc cùng chiều với vận tốc.", "Gia tốc bằng 0.",
          "Gia tốc vuông góc với vận tốc.", "Gia tốc ngược chiều với vận tốc."], "2.4 · TH"),
        ("Hệ thức liên hệ giữa vận tốc, gia tốc và độ dịch chuyển của chuyển động thẳng biến đổi đều là",
         ["v² − v₀² = 2ad.", "v = v₀ + at.", "d = v₀t + ½at².", "v² + v₀² = 2ad."], "2.5 · NB"),
        ("Trong chuyển động thẳng nhanh dần đều thì",
         ["vận tốc không đổi theo thời gian.",
          "vận tốc tăng đều theo thời gian.",
          "gia tốc luôn có giá trị âm.",
          "quãng đường tỉ lệ thuận với thời gian."], "2.5 · NB"),
        ("Một xe đạp bắt đầu chuyển động từ trạng thái nghỉ với gia tốc 0,5 m/s². Sau 8 s, vận tốc của xe là",
         ["2 m/s.", "4 m/s.", "8 m/s.", "16 m/s."], "2.5 · TH"),
        ("Sự rơi tự do là sự rơi của một vật",
         ["chỉ dưới tác dụng của trọng lực.",
          "trong không khí, có lực cản rất lớn.",
          "có vận tốc ban đầu bằng không.",
          "từ một độ cao rất lớn so với mặt đất."], "2.6 · NB"),
        ("Một vật rơi tự do từ độ cao 80 m, lấy g = 10 m/s². Thời gian rơi của vật là",
         ["4 s.", "2 s.", "8 s.", "16 s."], "2.6 · TH"),
        ("Hai vật được thả rơi tự do cùng lúc từ cùng một độ cao (bỏ qua lực cản của không khí). Kết luận đúng là",
         ["vật nặng chạm đất trước.", "vật nhẹ chạm đất trước.",
          "hai vật chạm đất cùng lúc.", "không so sánh được vì chưa biết khối lượng."], "2.6 · TH"),
    ]
    for i, (stem, opts, tag) in enumerate(Q, 1):
        mcq(d, i, stem, opts, tag)

    # ------------------------------------------------------------ PHẦN II
    d.condbreak(260)
    d.h2("PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu, mỗi câu 4 ý)")
    d.p("<i>Với mỗi ý a), b), c), d), thí sinh đánh dấu □ vào cột Đúng nếu phát biểu đúng, cột Sai nếu phát biểu sai.</i>", "Small")

    tf(d, 1,
       "Một người đi xe đạp trên một đường thẳng. Đồ thị độ dịch chuyển – thời gian của người này cho thấy: "
       "từ t = 0 đến t = 2 h, độ dịch chuyển tăng từ 0 đến 20 km; từ t = 2 h đến t = 3 h, độ dịch chuyển giữ "
       "nguyên 20 km; từ t = 3 h đến t = 4 h, độ dịch chuyển giảm từ 20 km về 0.",
       [("a", "Trong 2 giờ đầu, người đi với tốc độ 10 km/h."),
        ("b", "Từ giờ thứ 2 đến giờ thứ 3, người đứng yên."),
        ("c", "Từ giờ thứ 3 đến giờ thứ 4, người chuyển động cùng chiều dương."),
        ("d", "Quãng đường người đi được trong cả hành trình là 20 km.")],
       "2.2 + 2.3 · NB")

    tf(d, 2,
       "Một ô tô đang chạy với vận tốc 20 m/s thì người lái hãm phanh, ô tô chuyển động chậm dần đều và dừng "
       "lại sau 5 s.",
       [("a", "Gia tốc của ô tô trong thời gian hãm phanh là −4 m/s²."),
        ("b", "Quãng đường ô tô đi được từ lúc hãm phanh đến khi dừng lại là 50 m."),
        ("c", "Trong giây cuối cùng, ô tô đi được quãng đường 4 m."),
        ("d", "Kể từ lúc hãm phanh, sau 6 s ô tô đi được quãng đường 60 m.")],
       "2.5 · NB + TH")

    # ------------------------------------------------------------ PHẦN III
    d.condbreak(300)
    d.h2("PHẦN III. TỰ LUẬN NGẮN (2 câu)")
    essay(d, 1,
          "Phát biểu định nghĩa tốc độ trung bình và vận tốc trung bình; viết công thức, nêu đơn vị của mỗi đại lượng.",
          ["a) Tốc độ trung bình là gì? Viết công thức và nêu đơn vị.",
           "b) Vận tốc trung bình là gì? Viết công thức và nêu đơn vị.",
           "c) Phân biệt hai đại lượng trên bằng một ví dụ ngắn."],
          "2.2 · Biết")
    essay(d, 2,
          "Một vật được thả rơi tự do từ độ cao 45 m so với mặt đất. Lấy g = 10 m/s², bỏ qua lực cản của không khí.",
          ["a) Tính thời gian vật rơi đến khi chạm đất.",
           "b) Tính vận tốc của vật ngay khi chạm đất.",
           "c) Tính quãng đường vật đi được trong giây cuối cùng."],
          "2.6 · Hiểu")

    d.writebox(7, "PHẦN III – BÀI LÀM CỦA EM")

    # ------------------------------------------------------------ PHẦN IV
    d.condbreak(340)
    d.h2("PHẦN IV. TỰ LUẬN VẬN DỤNG (3 câu)")
    essay(d, 1,
          "Một ca nô chạy với vận tốc 8 m/s so với mặt nước, nước chảy với vận tốc 6 m/s so với bờ. "
          "Ca nô bơi theo hướng vuông góc với dòng chảy.",
          ["a) Tính vận tốc của ca nô so với bờ.",
           "b) Xác định góc lệch giữa hướng chuyển động của ca nô so với bờ và hướng bơi của ca nô."],
          "2.2 · Hiểu")
    essay(d, 2,
          "Một ô tô đang chạy với vận tốc 72 km/h thì hãm phanh, chuyển động chậm dần đều với gia tốc 5 m/s² "
          "cho đến khi dừng hẳn.",
          ["a) Tính thời gian từ lúc hãm phanh đến khi ô tô dừng lại.",
           "b) Tính quãng đường ô tô đi được trong thời gian đó.",
           "c) Tính quãng đường ô tô đi được trong giây cuối cùng trước khi dừng."],
          "2.5 · Vận dụng")
    essay(d, 3,
          "Từ điểm O, xe A khởi hành chuyển động thẳng nhanh dần đều với gia tốc 1 m/s². Cùng lúc đó, xe B đi "
          "qua điểm M cách O 200 m, chuyển động thẳng đều cùng chiều với xe A với vận tốc 15 m/s.",
          ["a) Viết phương trình chuyển động của mỗi xe (chọn O làm gốc toạ độ, chiều dương là chiều chuyển động, "
           "gốc thời gian lúc hai xe bắt đầu khảo sát).",
           "b) Xác định thời điểm và vị trí hai xe gặp nhau.",
           "c) Tính vận tốc của mỗi xe tại thời điểm gặp nhau."],
          "2.5 · Vận dụng")

    d.writebox(8, "PHẦN IV – BÀI LÀM CỦA EM")
    d.condbreak(240)
    d.h2("Phiếu tự đánh giá sau khi làm bài")
    d.table(
        ["Nội dung tự kiểm tra", "Kết quả", "Nội dung tự kiểm tra", "Kết quả"],
        [
            ["Số câu Phần I <b>chắc chắn đúng</b>", "……/18",
             "Số câu Phần I <b>phải đoán / bỏ trống</b>", "……/18"],
            ["Số ý Phần II <b>tự tin</b>", "……/8", "Số ý Phần II <b>chưa chắc</b>", "……/8"],
            ["Câu TL <b>viết được công thức</b> nhưng chưa ra số", "…………",
             "Câu TL <b>bỏ trắng</b>", "…………"],
            ["Lỗi <b>đơn vị</b> em phát hiện", "…………", "Lỗi <b>dấu của a</b> em phát hiện", "…………"],
            ["Lỗi <b>đọc đề</b> (nhầm quãng đường / dịch chuyển)", "…………",
             "Thời gian còn thừa khi hết giờ", "…… phút"],
        ],
        widths=[6.05 * cm, 2.1 * cm, 6.45 * cm, 2.1 * cm],
        aligns=["L", "C", "L", "C"], font_size=8.2, zebra=False)
    d.p("<i>Đối chiếu với bảng chấm ở Phần D.7 để biết mình đang ở mức nào và cần làm gì tiếp theo.</i>", "Small")

    d.box("note",
          "Đáp án và lời giải chi tiết ở Phần D (trang tiếp theo). Hãy bấm giờ đủ 50 phút và làm hết bài trước khi "
          "tra đáp án – đó là cách duy nhất để biết mình thật sự đang ở đâu.",
          title="TRƯỚC KHI XEM ĐÁP ÁN")

    d.h2("Nhật ký làm đề – giữ lại để thấy mình tiến bộ")
    d.table(
        ["Lần", "Ngày làm", "Điểm Phần I", "Điểm Phần II", "Điểm tự luận", "Tổng", "Lỗi chính cần sửa"],
        [["1", "", "……/4,5", "……/2,5", "……/3,0", "……/10", ""],
         ["2", "", "……/4,5", "……/2,5", "……/3,0", "……/10", ""],
         ["3", "", "……/4,5", "……/2,5", "……/3,0", "……/10", ""]],
        widths=[1.1 * cm, 2.2 * cm, 2.2 * cm, 2.2 * cm, 2.3 * cm, 1.9 * cm, 5.1 * cm],
        aligns=["C"] * 6 + ["L"], font_size=8.2, zebra=False)
    d.p("<i>Làm lại đề sau 3 – 5 ngày. Điểm lần sau cao hơn không phải vì đã nhớ đáp án, mà vì đã nhớ cách làm.</i>",
        "Small")
