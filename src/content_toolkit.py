# -*- coding: utf-8 -*-
"""Module C – Bộ công thức & sơ đồ tư duy; F – 12 bẫy; G – checklist."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (CondPageBreak, KeepTogether, PageBreak, Paragraph, Spacer, Table,
                                TableStyle)

from style import (AMBER, BODY, GREEN, INK, LINE, LM, MUTED, PAGE_W, PRIMARY,
                   RED, RM, SMALL, TEAL, GraphSketch, H2, H3, P, SectionBanner,
                   box, bullets, formula, numbered, table)

W = PAGE_W - LM - RM
CELL = ParagraphStyle("cell", fontName="BVP", fontSize=8.0, leading=10.8,
                      textColor=INK, alignment=TA_LEFT)
CELLB = ParagraphStyle("cellb", fontName="BVP-SB", fontSize=8.0, leading=10.8,
                       textColor=colors.white, alignment=TA_CENTER)


def banner_c():
    out = [CondPageBreak(12.5 * cm)]
    out.append(SectionBanner("PHẦN C", "Bộ công thức & sơ đồ tư duy",
                             "Một chỗ tra cứu – in riêng trang này dán lên tường",
                             color=colors.HexColor("#5B4B8A"), height=80))
    out.append(Spacer(1, 8))
    out.append(P("Nếu chỉ được mang một tờ giấy vào phòng thi, hãy mang trang này. Toàn bộ công "
                 "thức của chương Động học được xếp theo <b>đại lượng</b> để em tra ngược từ đề bài."))
    out.extend(H2("1. Bảng công thức tổng lực"))
    data = [["ĐẠI LƯỢNG", "CÔNG THỨC", "ĐƠN VỊ", "ĐIỀU KIỆN / GHI NHỚ"],
            ["<b>Tốc độ trung bình</b>", "v<sub>tb</sub> = s/Δt", "m/s", "s là quãng đường"],
            ["<b>Vận tốc trung bình</b>", "v = Δd/Δt", "m/s", "Δd là độ dịch chuyển (vectơ)"],
            ["<b>Gia tốc</b>", "a = (v − v₀)/Δt", "m/s²", "a cùng chiều v → nhanh dần"],
            ["<b>Vận tốc (biến đổi đều)</b>", "v = v₀ + a.t", "m/s", "t tính từ lúc t₀"],
            ["<b>Độ dịch chuyển</b>", "d = v₀t + ½at²", "m", "Không đổi chiều thì d = s"],
            ["<b>Hệ thức độc lập thời gian</b>", "v² − v₀² = 2ad", "–", "Dùng khi đề không cho t"],
            ["<b>Độ dịch chuyển (dạng khác)</b>", "d = (v₀ + v).t/2", "m", "Khi a = const"],
            ["<b>Quãng đường giây thứ n</b>", "Δs = v₀ + a(n − 0,5)", "m", "a không đổi"],
            ["<b>Rơi tự do – vận tốc</b>", "v = g.t", "m/s", "v₀ = 0"],
            ["<b>Rơi tự do – quãng đường</b>", "s = h = ½gt²", "m", "g ≈ 9,8 (hay 10) m/s²"],
            ["<b>Rơi tự do – thời gian</b>", "t = √(2h/g)", "s", "Không phụ thuộc khối lượng"],
            ["<b>Rơi tự do – vận tốc chạm đất</b>", "v = √(2gh)", "m/s", "= vận tốc ném lên đạt h"],
            ["<b>Cộng vận tốc (cùng chiều)</b>", "v₁₃ = v₁₂ + v₂₃", "m/s", "Xuôi dòng, thang cuốn"],
            ["<b>Cộng vận tốc (ngược chiều)</b>", "v₁₃ = |v₁₂ − v₂₃|", "m/s", "Ngược dòng"],
            ["<b>Cộng vận tốc (vuông góc)</b>", "v₁₃ = √(v₁₂² + v₂₃²)", "m/s", "Qua sông, bay ngang"],
            ["<b>Tổng hợp độ dịch chuyển vuông góc</b>", "|Δd| = √(Δx² + Δy²)", "m", "Pythagore"],
            ["<b>Sai số tỉ đối</b>", "δA = (ΔA/Ā).100%", "%", "Càng nhỏ càng chính xác"],
            ["<b>Sai số phép đo trực tiếp</b>", "ΔA = Δ̄A + ΔA<sub>dc</sub>", "cùng đơn vị A",
             "ΔA<sub>dc</sub> ≈ nửa ĐCNN"],
            ["<b>Sai số tổng / hiệu</b>", "ΔA = ΔB + ΔC", "–", "Cộng tuyệt đối"],
            ["<b>Sai số tích / thương</b>", "δA = δB + δC", "–", "Cộng tỉ đối"],
            ["<b>Ghi kết quả đo</b>", "A = Ā ± ΔA", "–", "Ā cùng hàng thập phân với ΔA"],
            ["<b>Vận tốc từ đồ thị d – t</b>", "v = độ dốc = Δd/Δt", "m/s", "Đường càng dốc càng nhanh"],
            ["<b>Phương trình từ đồ thị</b>", "d = d₀ + v.t", "m", "d₀ là tung độ gốc"]]
    out.append(table(data, [5.3 * cm, 4.6 * cm, 1.9 * cm, 4.9 * cm], size=8.0,
                     head_bg=colors.HexColor("#5B4B8A")))
    out.append(Spacer(1, 3))
    out.append(P("Đổi đơn vị: <b>1 m/s = 3,6 km/h</b>; 1 km/h = 1/3,6 m/s; 1 km = 1000 m; "
                 "1 h = 3600 s. Đổi <i>km/h → m/s</i> thì <b>chia 3,6</b>.", SMALL))

    out.extend(H2("2. Bốn dạng bài – quy trình bấm máy"))
    data = [["DẠNG BÀI", "DẤU HIỆU NHẬN DẠNG", "CÔNG THỨC DÙNG", "LƯU Ý"],
            ["<b>Tính tốc độ / vận tốc</b>", "Đề cho quãng đường (độ dịch chuyển) và thời gian",
             "v = s/Δt hoặc Δd/Δt", "Phân biệt s và Δd – quyết định dấu"],
            ["<b>Tính gia tốc</b>", "Đề cho v₀, v, t", "a = (v − v₀)/t", "Chậm dần → a âm"],
            ["<b>Bài toán một giai đoạn</b>", "v₀, a, t → hỏi v, d, s",
             "v = v₀ + at; d = v₀t + ½at²; v² − v₀² = 2ad",
             "Thiếu t thì dùng hệ thức bình phương"],
            ["<b>Bài toán nhiều giai đoạn</b>", "Có chữ “sau đó”, “tiếp theo”, “cuối cùng”",
             "Chia giai đoạn, v cuối đoạn này = v₀ đoạn sau",
             "Vẽ đồ thị v – t để kiểm tra; cộng quãng đường"]]
    out.append(table(data, [3.6 * cm, 4.4 * cm, 5.2 * cm, 3.5 * cm], size=8.1,
                     head_bg=colors.HexColor("#1B7A45")))

    head = [Spacer(1, 7)]
    g1 = GraphSketch([{"pts": [(0, 0), (8, 8)]}], xmax=10, ymax=10, height=104,
                     caption="(1) Thẳng đều: dốc đều – v không đổi",
                     marks=[(8, 8, "v = 8/8 = 1 m/s")])
    g2 = GraphSketch([{"pts": [(0, 3), (8, 3)]}], xmax=10, ymax=10, height=104,
                     caption="(2) Đứng yên: đường ngang – v = 0")
    g3 = GraphSketch([{"pts": [(0, 0), (4, 8), (8, 0)]}], xmax=10, ymax=10, height=104,
                     caption="(3) Đổi chiều: gấp khúc tại t = 4 s")
    g4 = GraphSketch([{"pts": [(0, 0), (1, 0.5), (2, 2), (3, 4.5), (4, 8)]}],
                     xmax=10, ymax=10, height=104,
                     caption="(4) Biến đổi đều: cong parabol – v tăng dần")
    t = Table([[g1, g2], [g3, g4]], colWidths=[W / 2, W / 2])
    t.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    out.extend(H2("3. Đọc đồ thị trong 5 giây – 4 hình mẫu"))
    out.append(KeepTogether([t]))
    out.extend(box("Câu thần chú cho đồ thị d – t",
                   [P("<b>Ngang = đứng yên · Dốc lên = đi tới · Dốc xuống = đi lui · "
                      "Gấp khúc = quay đầu · Cong = tăng/giảm tốc.</b> Độ dốc cho biết vận tốc, "
                      "giao điểm hai đồ thị là lúc hai vật gặp nhau.")], kind="amber"))
    return out


def mindmap():
    o = [PageBreak()]
    o.append(SectionBanner("PHẦN C2", "Sơ đồ tư duy cả chương",
                           "Nhìn một lần – nhớ cả 10 bài",
                           color=colors.HexColor("#0E7C86"), height=80))
    o.append(Spacer(1, 10))
    o.append(P("Sơ đồ dưới đây xếp 10 đơn vị kiến thức thành <b>4 nhánh</b>: phương pháp – mô tả "
               "chuyển động – chuyển động có gia tốc – ứng dụng. Hãy tự vẽ lại trên giấy trắng, "
               "đó là cách nhớ nhanh nhất."))
    o.append(Spacer(1, 6))

    def node(title, lines, bg, fg="#FFFFFF"):
        inner = [Paragraph('<font color="%s"><b>%s</b></font>' % (fg, title),
                           ParagraphStyle("nt", fontName="BVP-B", fontSize=8.6,
                                          leading=11.6, alignment=TA_CENTER))]
        for ln in lines:
            inner.append(Paragraph('<font color="%s" size="7.4">%s</font>' % (fg, ln),
                                   ParagraphStyle("nl", fontName="BVP", fontSize=7.4,
                                                  leading=10, alignment=TA_CENTER)))
        t = Table([[inner]], colWidths=[4.35 * cm])
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                               ("ROUNDEDCORNERS", [5, 5, 5, 5]),
                               ("TOPPADDING", (0, 0), (-1, -1), 6),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                               ("LEFTPADDING", (0, 0), (-1, -1), 6),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
        return t

    blue = colors.HexColor("#16357A")
    light = colors.HexColor("#E9EEFA")
    n1 = node("① NỀN TẢNG &amp; ĐO LƯỜNG",
              ["Bài 1 · Làm quen với Vật lí", "Bài 2 · An toàn phòng thực hành",
               "Bài 3 · Sai số phép đo"], blue)
    n2 = node("② MÔ TẢ CHUYỂN ĐỘNG",
              ["Bài 4 · Độ dịch chuyển &amp; quãng đường", "Bài 5 · Tốc độ &amp; vận tốc",
               "Bài 6 · Thực hành đo tốc độ", "Bài 7 · Đồ thị d – t"],
              colors.HexColor("#0E7C86"))
    n3 = node("③ CHUYỂN ĐỘNG CÓ GIA TỐC",
              ["Bài 8 · Gia tốc", "Bài 9 · Thẳng biến đổi đều",
               "Bài 10 · Rơi tự do"], colors.HexColor("#B3261E"))
    n4 = node("④ KỸ NĂNG LÀM BÀI",
              ["Đọc đồ thị · vẽ đồ thị", "Bài nhiều giai đoạn",
               "Tổng hợp vận tốc", "Ghi kết quả &amp; sai số"], colors.HexColor("#B07A15"))

    hub = Table([[Paragraph('<font color="#FFFFFF"><b>VẬT LÍ 10</b><br/>'
                            '<font size="8">GIỮA HỌC KÌ I</font></font>',
                            ParagraphStyle("hub", fontName="BVP-XB", fontSize=11,
                                           leading=15, alignment=TA_CENTER))]],
                colWidths=[3.4 * cm], rowHeights=[1.6 * cm])
    hub.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#111A33")),
                             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                             ("ROUNDEDCORNERS", [8, 8, 8, 8])]))

    grid = Table([[n1, n2], [n3, n4]], colWidths=[8.35 * cm, 8.35 * cm])
    grid.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"),
                              ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                              ("TOPPADDING", (0, 0), (-1, -1), 5),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    o.append(hub)
    o.append(Spacer(1, 6))
    o.append(grid)

    o.append(CondPageBreak(11.5 * cm))
    o.extend(H2("Bảng “một câu – một bài” để nhớ nhanh"))
    data = [["BÀI", "NHỚ ĐÚNG MỘT CÂU"],
            ["1. Làm quen với Vật lí", "Ba giai đoạn (Tiền – Cổ điển – Hiện đại), bốn cuộc CMCN "
                                       "(Watt – Faraday – bán dẫn – AI)."],
            ["2. An toàn phòng thực hành", "Tam vàng cảnh báo – tròn đỏ cấm – tròn xanh bắt buộc – "
                                           "vuông xanh chỉ dẫn."],
            ["3. Sai số phép đo", "Đo nhiều lần → trung bình → cộng sai số dụng cụ → ghi Ā ± ΔA."],
            ["4. Độ dịch chuyển &amp; quãng đường", "Dịch chuyển nối hai đầu, quãng đường đo cả "
                                                    "đường đi; |Δd| ≤ s."],
            ["5. Tốc độ &amp; vận tốc", "Tốc độ vô hướng (s/Δt); vận tốc vectơ (Δd/Δt); cộng vận "
                                        "tốc theo quy tắc vectơ."],
            ["6. Thực hành đo tốc độ", "Cổng quang điện tự động đo thời gian ngắn: nhanh – chính "
                                       "xác – nhưng đắt và cần điện."],
            ["7. Đồ thị d – t", "Độ dốc của đồ thị chính là vận tốc."],
            ["8. Gia tốc", "a = Δv/Δt (m/s²); cùng chiều thì nhanh dần, ngược chiều thì chậm dần."],
            ["9. Thẳng biến đổi đều", "v = v₀ + at; d = v₀t + ½at²; v² − v₀² = 2ad."],
            ["10. Rơi tự do", "Chỉ trọng lực; v = gt; h = ½gt²; t = √(2h/g)."]]
    o.append(table(data, [5.0 * cm, 11.7 * cm], size=8.3,
                   head_bg=colors.HexColor("#16357A")))
    return o


# =========================================================================== F
def traps():
    o = [CondPageBreak(12.5 * cm)]
    o.append(SectionBanner("PHẦN F", "12 bẫy thường gặp",
                           "Mỗi bẫy dưới đây đã từng làm mất điểm của rất nhiều học sinh",
                           color=colors.HexColor("#B3261E"), height=80))
    o.append(Spacer(1, 8))
    data = [["#", "BẪY", "DẤU HIỆU", "CÁCH TRÁNH"],
            ["1", "Nhầm <b>quãng đường</b> với <b>độ dịch chuyển</b>",
             "Vật đổi chiều hoặc quay về chỗ cũ",
             "Viết rõ “s = …” và “Δd = …”; nhớ |Δd| ≤ s"],
            ["2", "Dùng <b>tốc độ</b> khi đề hỏi <b>vận tốc</b>",
             "Đề có chữ “vận tốc” và vật đổi chiều",
             "Vận tốc luôn gắn với độ dịch chuyển và có dấu"],
            ["3", "Không đổi <b>km/h → m/s</b>",
             "Đề cho km/h nhưng công thức cần m/s",
             "Nhìn đơn vị trước khi thay số: chia 3,6"],
            ["4", "Đặt <b>a dương</b> cho chuyển động chậm dần",
             "Đề có “hãm phanh”, “giảm tốc”, “dừng lại”",
             "Chọn chiều dương = chiều chuyển động → a âm khi chậm dần"],
            ["5", "Nghĩ <b>a âm</b> luôn là chậm dần",
             "Chiều dương chọn ngược chiều chuyển động",
             "So <b>dấu a với dấu v</b>, đừng so với 0"],
            ["6", "Nhầm <b>tốc độ trung bình</b> với <b>trung bình cộng các tốc độ</b>",
             "Đề cho nhiều đoạn với thời gian khác nhau",
             "Luôn dùng tổng quãng đường / tổng thời gian"],
            ["7", "Tính vận tốc từ đồ thị bằng <b>d/t</b>",
             "Đồ thị không đi qua gốc toạ độ",
             "Dùng Δd/Δt (hiệu hai điểm), tức độ dốc"],
            ["8", "Nhầm <b>độ dốc</b> với <b>độ cao</b> của đồ thị",
             "Câu hỏi “vật nào nhanh hơn”",
             "So góc dốc, không so vị trí đường"],
            ["9", "Cho rằng <b>vật nặng rơi nhanh hơn</b> trong chân không",
             "Câu hỏi về ống Newton, lông chim – bi chì",
             "Trong chân không mọi vật rơi cùng gia tốc g"],
            ["10", "Dùng công thức <b>rơi tự do</b> cho vật ném lên",
             "Đề cho v₀ ≠ 0",
             "Dùng hệ công thức biến đổi đều; đỉnh cao khi v = 0"],
            ["11", "Tính “quãng đường trong giây thứ 3” = ½g.3²",
             "Chữ “giây thứ n”",
             "Δs = s(n) − s(n−1), hoặc g(n − 0,5)"],
            ["12", "Quên <b>cộng sai số dụng cụ</b> và ghi quá nhiều chữ số",
             "Bài thực hành tính sai số",
             "ΔA = Δ̄A + ΔA<sub>dc</sub>; Ā làm tròn cùng hàng với ΔA"]]
    o.append(table(data, [0.8 * cm, 5.2 * cm, 4.5 * cm, 6.2 * cm], size=8.1,
                   align=[TA_CENTER, TA_LEFT, TA_LEFT, TA_LEFT],
                   head_bg=colors.HexColor("#B3261E")))
    o.append(Spacer(1, 6))
    o.extend(box("Quy tắc 3 giây trước khi thay số",
                 [P("(1) Đơn vị đã đúng chưa? (2) Chiều dương đã chọn chưa, dấu của a đã đúng "
                    "chưa? (3) Đại lượng đề hỏi là <b>quãng đường</b> hay <b>độ dịch chuyển</b>? "
                    "Ba câu hỏi này chặn được phần lớn lỗi mất điểm.")], kind="amber"))
    return o


# =========================================================================== G
def checklist():
    o = [CondPageBreak(12.5 * cm)]
    o.append(SectionBanner("PHẦN G", "Checklist &amp; chiến thuật phòng thi",
                           "Việc cần làm – thứ tự làm – cách giữ điểm",
                           color=colors.HexColor("#16357A"), height=80))
    o.append(Spacer(1, 8))
    o.extend(H2("1. Checklist “đã thuộc chưa?”"))
    items = [
        "Phát biểu được đối tượng nghiên cứu của Vật lí và kể tên 3 giai đoạn phát triển.",
        "Kể được 4 cuộc cách mạng công nghiệp gắn với thành tựu nào, của ai, năm nào.",
        "Nêu 6 bước của phương pháp thực nghiệm và 3 loại mô hình.",
        "Nhận dạng 5 loại biển báo an toàn chỉ qua hình – màu.",
        "Viết đúng 3 công thức sai số và cách ghi A = Ā ± ΔA.",
        "Phân biệt độ dịch chuyển và quãng đường, nêu hệ thức |Δd| ≤ s.",
        "Phân biệt tốc độ và vận tốc; viết công thức cộng vận tốc cho 3 trường hợp.",
        "Nêu ưu – nhược điểm của đồng hồ hiện số + cổng quang điện và ý nghĩa hai cổng.",
        "Đọc được 5 dạng đồ thị d – t và tính vận tốc từ độ dốc.",
        "Viết công thức gia tốc, nêu quan hệ phương – chiều của a và v.",
        "Viết và áp dụng thành thạo 4 công thức chuyển động thẳng biến đổi đều.",
        "Viết 4 công thức rơi tự do và giải bài rơi – ném thẳng đứng.",
        "Tự làm lại đề mục D trong 50 phút, đạt ≥ 7,5 điểm.",
        "Ghi lại danh sách lỗi sai của mình vào một tờ giấy riêng và đọc lại trước khi thi.",
    ]
    rows = [[P("☐", ParagraphStyle("ck", parent=BODY, fontSize=11)),
             P(t, BODY)] for t in items]
    t = Table(rows, colWidths=[0.8 * cm, W - 0.8 * cm])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 2),
                           ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                           ("LINEBELOW", (0, 0), (-1, -2), 0.3, LINE)]))
    o.append(t)

    o.extend(H2("2. Chiến thuật 50 phút trong phòng thi"))
    data = [["THỜI GIAN", "VIỆC LÀM", "MẸO"],
            ["0 – 3 phút", "Đọc lướt toàn đề, đánh dấu câu dễ / câu khó",
             "Đừng sa vào câu khó đầu tiên"],
            ["3 – 21 phút", "Làm trọn 18 câu trắc nghiệm, câu nào quá 1 phút thì bỏ qua đánh dấu",
             "Câu nào chắc chắn thì chốt luôn, không ngoái lại"],
            ["21 – 29 phút", "Phần II – 8 ý Đúng/Sai; đọc kĩ từng ý độc lập",
             "Mỗi ý chỉ 0,25 đ, đừng để một ý làm rối cả câu"],
            ["29 – 33 phút", "Phần III – 2 câu trả lời ngắn",
             "Kiểm tra lại đơn vị và số chữ số"],
            ["33 – 48 phút", "Phần IV – 3 câu tự luận, mỗi câu ~5 phút",
             "Viết tóm tắt + công thức trước, thay số sau – có điểm trình bày"],
            ["48 – 50 phút", "Rà lại: dấu của a, đơn vị, câu đã đánh dấu",
             "Không đổi đáp án nếu không có căn cứ mới"]]
    o.append(table(data, [2.6 * cm, 8.6 * cm, 5.5 * cm], size=8.3,
                   head_bg=colors.HexColor("#1B7A45")))
    o.append(Spacer(1, 6))
    o.extend(box("Ba nguyên tắc giữ điểm",
                 bullets([
                     "<b>Không bỏ trống</b> câu trắc nghiệm nào – sai không bị trừ điểm.",
                     "<b>Viết công thức trước khi thay số</b> ở tự luận: giám khảo chấm theo bước.",
                     "<b>Kiểm tra bằng đơn vị</b>: nếu kết quả ra m/s² cho câu hỏi quãng đường thì "
                     "chắc chắn sai.",
                 ]), kind="primary"))
    o.extend(H2("3. Bảng tự đánh giá sau khi làm đề"))
    data = [["MỨC ĐIỂM", "Ý NGHĨA", "VIỆC CẦN LÀM TIẾP"],
            ["&lt; 5,0", "Chưa nắm công thức", "Học lại mục C, làm lại các ví dụ mẫu trong mục B"],
            ["5,0 – 6,5", "Biết công thức nhưng vận dụng còn yếu",
             "Luyện dạng bài nhiều giai đoạn và bài đổi chiều ở mục B9"],
            ["6,5 – 8,0", "Khá – chỉ mất điểm ở câu hiểu bản chất",
             "Đọc lại mục F, chú ý tốc độ vs vận tốc và đồ thị"],
            ["8,0 – 9,0", "Tốt", "Luyện tốc độ làm bài, giữ ổn định"],
            ["9,0 – 10", "Rất tốt", "Ôn thêm bài toán nâng cao: ném xiên, hai vật gặp nhau"]]
    o.append(table(data, [2.8 * cm, 5.6 * cm, 8.3 * cm], size=8.4,
                   align=[TA_CENTER, TA_LEFT, TA_LEFT],
                   head_bg=colors.HexColor("#5B4B8A")))
    o.append(Spacer(1, 12))
    o.append(Table([[P("Chúc em bình tĩnh – tự tin – làm bài chắc từng câu. "
                       "Điểm số là kết quả của những lần tự làm lại, không phải của những lần đọc lại.",
                       ParagraphStyle("end", parent=BODY, fontName="BVP-It",
                                      fontSize=10.2, leading=15,
                                      textColor=PRIMARY, alignment=TA_CENTER))]],
                   colWidths=[W],
                   style=TableStyle([("TOPPADDING", (0, 0), (-1, -1), 10),
                                     ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                                     ("BACKGROUND", (0, 0), (-1, -1),
                                      colors.HexColor("#EDF1FB")),
                                     ("BOX", (0, 0), (-1, -1), 0.7,
                                      colors.HexColor("#CBD5EE"))])))
    return o
