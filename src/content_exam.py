# -*- coding: utf-8 -*-
"""Module D – Đề minh họa; Module E – Đáp án và lời giải."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (CondPageBreak, KeepTogether, PageBreak, Spacer, Table,
                                TableStyle)

from style import (AMBER, BODY, GREEN, INK, LINE, LM, MUTED, PAGE_W, PRIMARY,
                   RED, RM, SMALL, TEAL, SectionBanner, H2, H3, P, box, bullets,
                   formula, numbered, table)

W = PAGE_W - LM - RM
OPT = ParagraphStyle("opt", parent=BODY, fontSize=9.6, leading=14.2,
                     alignment=TA_LEFT, spaceAfter=0.5)
QW = ParagraphStyle("qw", parent=BODY, fontSize=9.8, leading=14.6,
                    alignment=TA_LEFT, spaceAfter=2)
TAG = ParagraphStyle("tagtxt", parent=SMALL, fontSize=7.2, leading=9.4)


def qnum(n, text, level=None, unit=None):
    tag = ""
    if level or unit:
        bits = [b for b in [unit, level] if b]
        tag = ' <font size="7" color="#8A93AC">[%s]</font>' % " · ".join(bits)
    return P("<b>Câu %d.</b> " % n + text + tag, QW)


def opts(lines, cols=2):
    """Chia phương án A–D thành 1 hoặc 2 cột."""
    items = [P(x, OPT) for x in lines]
    if cols == 1:
        for it in items:
            yield it
        return
    rows = []
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        if len(pair) == 1:
            pair.append("")
        rows.append(pair)
    t = Table(rows, colWidths=[(W - 6) / 2, (W - 6) / 2])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (0, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5)]))
    yield t


# =========================================================================== A
def part_a():
    o = [PageBreak()]
    o.append(SectionBanner("PHẦN A", "Bản đồ đề thi",
                           "Ma trận rút gọn – biết chỗ nào nên dồn sức",
                           color=colors.HexColor("#16357A"), height=88))
    o.append(Spacer(1, 8))
    o.append(P("Tài liệu gốc là <b>ma trận đặc tả</b> – nó quy định đề sẽ hỏi ở đơn vị kiến thức "
               "nào, với mức độ nhận thức nào, và mỗi phần có bao nhiêu câu. Nắm được bản đồ này "
               "trước khi học giúp em <b>không học lan man</b>."))
    o.extend(H2("1. Cấu trúc đề trong 50 phút"))
    data = [["PHẦN", "DẠNG CÂU", "SỐ CÂU", "SỐ Ý", "ĐIỂM", "MỨC ĐỘ (theo ma trận)"],
            ["I", "Trắc nghiệm nhiều phương án", "18", "18", "4,5",
             "10 câu Biết + 8 câu Hiểu"],
            ["II", "Trắc nghiệm Đúng / Sai", "2", "8", "2,0",
             "6 ý Biết + 2 ý Hiểu"],
            ["III", "Trả lời ngắn (điền số)", "2", "2", "0,5", "1 Biết + 1 Hiểu"],
            ["IV", "Tự luận", "3", "3", "3,0", "1 Hiểu + 2 Vận dụng"],
            ["", "<b>TỔNG</b>", "<b>25</b>", "<b>31</b>", "<b>10,0</b>",
             "<b>Trắc nghiệm 70% – Tự luận 30%</b>"]]
    o.append(table(data, [1.5 * cm, 4.5 * cm, 1.7 * cm, 1.5 * cm, 1.6 * cm, 6.9 * cm],
                   size=8.4, align=[TA_CENTER, TA_LEFT, TA_CENTER, TA_CENTER,
                                    TA_CENTER, TA_LEFT]))
    o.append(Spacer(1, 3))
    o.append(P("<b>Cách tính điểm:</b> Phần I 0,25 điểm/câu; Phần II 0,25 điểm/ý; Phần III 0,25 "
               "điểm/câu; Phần IV 1,0 điểm/câu. Trắc nghiệm = 4,5 + 2,0 + 0,5 = <b>7,0 điểm</b> "
               "(70%); tự luận = <b>3,0 điểm</b> (30%).", SMALL))

    o.extend(H2("2. Phân bổ câu hỏi theo đơn vị kiến thức"))
    data = [["ĐƠN VỊ KIẾN THỨC", "P.I", "P.II", "P.III", "P.IV", "TỔNG ĐIỂM", "ƯU TIÊN"],
            ["1.1 Làm quen với Vật lí", "1", "–", "–", "–", "0,25", "★"],
            ["1.2 Quy tắc an toàn phòng thực hành", "2", "–", "–", "–", "0,50", "★"],
            ["1.3 Sai số trong phép đo", "1", "–", "–", "–", "0,25", "★★"],
            ["2.1 Độ dịch chuyển và quãng đường", "3", "–", "–", "–", "0,75", "★★★"],
            ["2.2 Tốc độ và vận tốc", "1", "2 ý", "1", "1", "1,50", "★★★★"],
            ["2.3 Đồ thị độ dịch chuyển – thời gian", "2", "2 ý", "–", "–", "1,00", "★★★"],
            ["2.4 Chuyển động biến đổi. Gia tốc", "2", "–", "–", "–", "0,50", "★★"],
            ["2.5 Chuyển động thẳng biến đổi đều", "3", "4 ý", "–", "2", "3,00", "★★★★★"],
            ["2.6 Sự rơi tự do", "3", "–", "1", "–", "1,00", "★★★"],
            ["(Thực hành đo tốc độ – có trong bản đặc tả)", "–", "–", "–", "–", "–", "★★"]]
    o.append(table(data, [7.5 * cm, 1.2 * cm, 1.4 * cm, 1.3 * cm, 1.3 * cm, 2.2 * cm, 1.8 * cm],
                   size=8.2, align=[TA_LEFT, TA_CENTER, TA_CENTER, TA_CENTER,
                                    TA_CENTER, TA_CENTER, TA_CENTER]))
    o.append(Spacer(1, 3))
    o.append(P("<b>Đọc bảng này thế nào?</b> Chỉ riêng đơn vị <b>2.5 (chuyển động thẳng biến đổi "
               "đều)</b> đã chiếm <b>3,0/10 điểm</b>; cộng với 2.2, 2.3 và 2.6 thì phần động học "
               "“có công thức” chiếm tới <b>6,5 điểm</b>. Nếu chỉ còn ít thời gian, hãy học chắc "
               "mục B9 (bài 9) trước tiên.", SMALL))
    o.extend(box("Lưu ý quan trọng về tài liệu gốc",
                 [P("Tệp <i>“MA TRẬN ĐẶC TẢ KTGK I L10 – 2026.docx”</i> chỉ chứa <b>ma trận đặc tả "
                    "và bảng mô tả mức độ</b> (9 dòng 1.1 → 2.6 trong ma trận, 10 mục trong bản đặc "
                    "tả vì có thêm mục thực hành “Đo tốc độ của vật chuyển động”). Tệp <b>không "
                    "kèm đề thi và đáp án</b>. Do đó mục D dưới đây là <b>đề minh họa được lập "
                    "đúng theo ma trận</b> (đúng số câu, đúng mức độ, đúng đơn vị kiến thức), kèm "
                    "lời giải đầy đủ ở mục E – để em có thể tự “thi thử” ngay.")], kind="amber"))

    o.extend(H2("3. Mức độ nhận thức – đề hỏi gì ở mỗi mức?"))
    data = [["MỨC ĐỘ", "ĐỘNG TỪ TRONG ĐẶC TẢ", "NGHĨA LÀ", "CÁCH HỌC"],
            ["<b>Biết</b>", "Nêu, phát biểu, kể tên, viết công thức, định nghĩa",
             "Nhớ lại đúng nội dung đã học", "Học thuộc định nghĩa + công thức + đơn vị"],
            ["<b>Hiểu</b>", "Giải thích, phân biệt, so sánh, tính toán đơn giản một bước",
             "Hiểu bản chất, dùng được công thức vào tình huống quen",
             "Làm ví dụ mẫu, tự giải thích bằng lời của mình"],
            ["<b>Vận dụng</b>", "Tính, xác định, giải bài toán",
             "Dùng kiến thức vào bài toán mới, có thể 2 bước",
             "Luyện dạng bài, viết đủ bước – đủ đơn vị"],
            ["<b>Vận dụng cao</b>", "Giải quyết, phân tích bài toán phức hợp",
             "Bài toán nhiều giai đoạn, nhiều đại lượng", "Làm bài tổng hợp, kiểm tra lại kết quả"]]
    o.append(table(data, [2.4 * cm, 5.6 * cm, 4.8 * cm, 3.9 * cm], size=8.2,
                   head_bg=colors.HexColor("#5B4B8A")))

    o.extend(H2("4. Chín “khuôn” câu hỏi gần như chắc chắn xuất hiện"))
    left = bullets([
        "<b>Định nghĩa – khái niệm</b>: “đại lượng nào là vectơ”, “rơi tự do là gì”, "
        "“gia tốc đặc trưng cho…”.",
        "<b>Nhận dạng biển báo</b>: cho hình – màu, hỏi loại biển.",
        "<b>Tính toán một bước</b>: v = s/t; a = Δv/Δt; t = √(2h/g).",
        "<b>Đọc đồ thị d – t</b>: hỏi vận tốc, trạng thái chuyển động.",
        "<b>Đổi đơn vị</b>: km/h → m/s trong bài tốc độ.",
    ])
    right = bullets([
        "<b>Phân biệt cặp khái niệm</b>: tốc độ – vận tốc; quãng đường – độ dịch chuyển; "
        "nhanh dần – chậm dần.",
        "<b>Chọn công thức đúng</b>: v² − v₀² = 2ad, δA = (ΔA/Ā).100%…",
        "<b>Đúng/Sai 4 ý</b> xoay quanh một bài toán có số liệu (thường là bài hãm phanh hoặc "
        "chuyển động nhiều giai đoạn).",
        "<b>Tự luận 2 giai đoạn</b>: tăng tốc – đều – hãm phanh, hoặc ca nô xuôi/ngược dòng.",
    ])
    tt = Table([[left, right]], colWidths=[W / 2 - 6, W / 2 - 6])
    tt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (0, -1), 0),
                            ("LEFTPADDING", (1, 0), (1, -1), 14),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    o.append(tt)
    return o


# =========================================================================== D
def part_d():
    o = [PageBreak()]
    o.append(SectionBanner("PHẦN D", "Đề minh họa chuẩn ma trận",
                           "25 câu · 31 lệnh hỏi · 10 điểm · 50 phút · có đáp án ở mục E",
                           color=colors.HexColor("#B3261E"), height=88))
    o.append(Spacer(1, 8))
    info = [["Môn", "Vật lí – Lớp 10"], ["Hình thức", "70% trắc nghiệm + 30% tự luận"],
            ["Thời gian", "50 phút (không kể thời gian phát đề)"],
            ["Cấu trúc", "I: 18 câu TN · II: 2 câu Đúng/Sai (8 ý) · III: 2 câu trả lời ngắn · "
                         "IV: 3 câu tự luận"]]
    t = table(info, [3.2 * cm, 13.5 * cm], header=False, size=8.6,
              extra=[("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F3F7")),
                     ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
                     ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#C3CADC"))])
    o.append(t)
    o.append(Spacer(1, 5))
    o.append(P('<font size="7.6" color="#8A93AC">Ghi chú: nội dung trong ngoặc vuông [ ] chỉ rõ '
               'đơn vị kiến thức và mức độ – dùng để đối chiếu với ma trận, không có trong đề thi '
               'thật.</font>'))
    o.append(Spacer(1, 4))

    # ---- PHẦN I
    o.extend(_part_head("PHẦN I", "Trắc nghiệm nhiều phương án lựa chọn",
                        "Thí sinh trả lời từ câu 1 đến câu 18. Mỗi câu chỉ chọn một phương án. "
                        "(4,5 điểm)", PRIMARY))
    qs = _part1()
    for q in qs:
        o.append(Spacer(1, 3.5))
        o.append(q[0])
        for x in q[1]:
            o.append(x)

    # ---- PHẦN II
    o.append(PageBreak())
    o.extend(_part_head("PHẦN II", "Trắc nghiệm đúng – sai",
                        "Thí sinh trả lời 2 câu. Trong mỗi ý a), b), c), d) chọn Đúng hoặc Sai. "
                        "(2,0 điểm – 0,25 điểm/ý)", TEAL))
    o.append(P("Câu 1. Một người đi xe đạp xuất phát từ A, chuyển động thẳng theo chiều dương. "
               "Trong 2 giờ đầu người đi được 30 km; trong giờ thứ ba người dừng lại nghỉ; sau đó "
               "quay trở lại A và về đến A sau 3 giờ kể từ lúc bắt đầu quay lại. "
               "<font size=\"7\" color=\"#8A93AC\">[2.2 + 2.3]</font>", QW))
    o.append(Spacer(1, 2))
    o.append(_yesno([
        ("a", "Tốc độ trung bình của người trong 2 giờ đầu là 15 km/h.", "Biết"),
        ("b", "Trong giờ thứ ba, người chuyển động thẳng đều với vận tốc 30 km/h.", "Biết"),
        ("c", "Sau 6 giờ kể từ lúc xuất phát, độ dịch chuyển của người bằng 0 còn quãng đường "
              "đi được là 60 km.", "Biết"),
        ("d", "Vận tốc trung bình của người trên cả hành trình 6 giờ là 10 km/h.", "Biết"),
    ]))
    o.append(Spacer(1, 8))
    o.append(P("Câu 2. Một ô tô đang chạy với vận tốc 20 m/s thì người lái hãm phanh, ô tô chuyển "
               "động chậm dần đều với gia tốc có độ lớn 4 m/s² cho đến khi dừng hẳn. Chọn chiều "
               "dương là chiều chuyển động, gốc thời gian lúc bắt đầu hãm phanh. "
               "<font size=\"7\" color=\"#8A93AC\">[2.5]</font>", QW))
    o.append(Spacer(1, 2))
    o.append(_yesno([
        ("a", "Gia tốc của ô tô là a = −4 m/s².", "Biết"),
        ("b", "Ô tô dừng lại sau 5 s kể từ lúc hãm phanh.", "Biết"),
        ("c", "Quãng đường ô tô đi được từ lúc hãm phanh đến khi dừng là 50 m.", "Hiểu"),
        ("d", "Nếu vận tốc lúc hãm phanh tăng gấp đôi (40 m/s) thì quãng đường hãm phanh cũng "
              "tăng gấp đôi.", "Hiểu"),
    ]))

    # ---- PHẦN III
    o.append(Spacer(1, 10))
    o.extend(_part_head("PHẦN III", "Trả lời ngắn",
                        "Viết kết quả bằng một con số (kèm đơn vị nếu có). (0,5 điểm – 0,25 "
                        "điểm/câu)", colors.HexColor("#5B4B8A")))
    o.append(P("Câu 1. Một ô tô chạy được quãng đường 90 km trong 1,5 giờ. Tốc độ trung bình của "
               "ô tô là bao nhiêu km/h? <font size=\"7\" color=\"#8A93AC\">[2.2 – Biết]</font>", QW))
    o.append(Spacer(1, 6))
    o.append(P("Câu 2. Một vật được thả rơi tự do từ độ cao 45 m so với mặt đất. Lấy g = 10 m/s², "
               "bỏ qua lực cản của không khí. Vận tốc của vật khi chạm đất là bao nhiêu m/s? "
               "<font size=\"7\" color=\"#8A93AC\">[2.6 – Hiểu]</font>", QW))

    # ---- PHẦN IV
    o.append(Spacer(1, 10))
    o.extend(_part_head("PHẦN IV", "Tự luận",
                        "Trình bày lời giải đầy đủ: tóm tắt – công thức – thay số – kết quả có đơn "
                        "vị. (3,0 điểm – 1,0 điểm/câu)", AMBER))
    o.append(P("<b>Câu 1 (1,0 điểm).</b> Một ca nô chạy xuôi dòng từ bến A đến bến B cách nhau "
               "36 km mất 1,5 giờ. Biết vận tốc của dòng nước so với bờ là 4 km/h và không đổi. "
               "<font size=\"7\" color=\"#8A93AC\">[2.2 – Hiểu]</font>", QW))
    o.extend(bullets(["Tính vận tốc của ca nô so với nước.",
                      "Nếu ca nô chạy ngược dòng từ B về A thì mất bao nhiêu thời gian?"],
                     ParagraphStyle("sub", parent=QW, leftIndent=14, fontSize=9.6, bulletFontName="BVP-SB")))
    o.append(Spacer(1, 6))
    o.append(P("<b>Câu 2 (1,0 điểm).</b> Một xe khởi hành từ trạng thái nghỉ và chuyển động nhanh "
               "dần đều với gia tốc 2 m/s² trong 10 s. Sau đó xe chạy thẳng đều trong 20 s, cuối "
               "cùng hãm phanh chuyển động chậm dần đều và dừng lại sau 5 s. "
               "<font size=\"7\" color=\"#8A93AC\">[2.5 – Vận dụng]</font>", QW))
    o.extend(bullets(["Tính vận tốc lớn nhất mà xe đạt được.",
                      "Tính tổng quãng đường xe đã đi được."],
                     ParagraphStyle("sub2", parent=QW, leftIndent=14, fontSize=9.6, bulletFontName="BVP-SB")))
    o.append(Spacer(1, 6))
    o.append(P("<b>Câu 3 (1,0 điểm).</b> Từ mặt đất, một vật được ném thẳng đứng lên trên với vận "
               "tốc 20 m/s. Bỏ qua lực cản của không khí, lấy g = 10 m/s². "
               "<font size=\"7\" color=\"#8A93AC\">[2.5 – Vận dụng]</font>", QW))
    o.extend(bullets(["Tính độ cao lớn nhất mà vật đạt được.",
                      "Tính thời gian từ lúc ném đến khi vật trở về mặt đất và quãng đường vật "
                      "đã đi trong khoảng thời gian đó."],
                     ParagraphStyle("sub3", parent=QW, leftIndent=14, fontSize=9.6, bulletFontName="BVP-SB")))
    o.append(Spacer(1, 10))
    o.extend(box("Mẹo phân bổ 50 phút",
                 [P("Phần I: <b>18 phút</b> (1 phút/câu) · Phần II: <b>8 phút</b> · Phần III: "
                    "<b>4 phút</b> · Phần IV: <b>18 phút</b> (6 phút/câu) · Còn <b>2 phút</b> rà "
                    "lại đơn vị và dấu. Đừng dừng quá 2 phút ở một câu trắc nghiệm – đánh dấu "
                    "rồi quay lại.")], kind="amber"))
    return o


def _part_head(tag, title, sub, color):
    bar = Table([[P('<font color="#FFFFFF" size="11"><b>%s</b></font>&nbsp;&nbsp;'
                    '<font color="#FFFFFF" size="9.6">%s</font>' % (tag, title),
                    ParagraphStyle("ph", fontName="BVP", fontSize=10,
                                   leading=14, textColor=colors.white))]],
                colWidths=[W])
    bar.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), color),
                             ("LEFTPADDING", (0, 0), (-1, -1), 9),
                             ("TOPPADDING", (0, 0), (-1, -1), 6),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return [bar, Spacer(1, 3),
            P('<font size="7.8" color="#586180"><i>%s</i></font>' % sub), Spacer(1, 2)]


def _yesno(items):
    head = ["Ý", "NỘI DUNG", "ĐÚNG", "SAI"]
    data = [head]
    for row in items:
        k, txt = row[0], row[1]
        lvl = row[2] if len(row) > 2 else None
        if lvl:
            txt = '%s <font size="7" color="#8A93AC">[%s]</font>' % (txt, lvl)
        data.append([k + ")", txt, "☐", "☐"])
    t = table(data, [1.1 * cm, 12.9 * cm, 1.5 * cm, 1.5 * cm], size=8.8,
              align=[TA_CENTER, TA_LEFT, TA_CENTER, TA_CENTER],
              head_bg=colors.HexColor("#0E7C86"))
    return t


def _part1():
    Q = []
    Q.append((qnum(1, "Đối tượng nghiên cứu chủ yếu của Vật lí là", "Biết", "1.1"),
              [o for o in opts([
                  "A. các dạng vận động của vật chất (chất, trường) và năng lượng.",
                  "B. cấu tạo, chức năng của tế bào và các quá trình di truyền.",
                  "C. sự hình thành, phát triển của xã hội loài người.",
                  "D. các phản ứng hoá học xảy ra trong cơ thể sinh vật."])]))
    Q.append((qnum(2, "Trong phòng thực hành Vật lí, hành vi nào sau đây <b>vi phạm</b> quy tắc "
                      "an toàn?", "Biết", "1.2"),
              [o for o in opts([
                  "A. Đeo kính bảo hộ và găng tay khi làm việc với hoá chất.",
                  "B. Ăn nhẹ tại chỗ làm thí nghiệm cho đỡ đói.",
                  "C. Ngắt công tắc nguồn trước khi tháo lắp mạch điện.",
                  "D. Báo ngay cho giáo viên khi làm vỡ ống nghiệm."])]))
    Q.append((qnum(3, "Biển báo có dạng <b>hình tam giác đều, viền đen, nền vàng</b> thuộc loại "
                      "biển nào?", "Hiểu", "1.2"),
              [o for o in opts([
                  "A. Biển cấm.", "B. Biển cảnh báo.", "C. Biển bắt buộc.", "D. Biển chỉ dẫn."])]))
    Q.append((qnum(4, "Phép đo nào sau đây là <b>phép đo gián tiếp</b>?", "Biết", "1.3"),
              [o for o in opts([
                  "A. Đo chiều dài bàn bằng thước cuộn.",
                  "B. Đo thời gian rơi bằng đồng hồ hiện số.",
                  "C. Đo khối lượng riêng của hòn sỏi qua khối lượng và thể tích.",
                  "D. Đo nhiệt độ của nước bằng nhiệt kế."])]))
    Q.append((qnum(5, "Đại lượng nào sau đây là <b>đại lượng vectơ</b>?", "Biết", "2.1"),
              [o for o in opts([
                  "A. Quãng đường đi được.", "B. Độ dịch chuyển.",
                  "C. Tốc độ trung bình.", "D. Thời gian chuyển động."])]))
    Q.append((qnum(6, "Một người đi 6 m về phía đông rồi đi tiếp 8 m về phía bắc. Độ lớn độ dịch "
                      "chuyển của người là", "Hiểu", "2.1"),
              [o for o in opts([
                  "A. 2 m.", "B. 10 m.", "C. 14 m.", "D. 48 m."])]))
    Q.append((qnum(7, "Một vật chuyển động thẳng: đi 12 m theo chiều dương rồi quay lại đi 5 m. "
                      "Quãng đường và độ dịch chuyển của vật lần lượt là", "Hiểu", "2.1"),
              [o for o in opts([
                  "A. 17 m và 7 m.", "B. 7 m và 17 m.",
                  "C. 17 m và −7 m.", "D. 12 m và 5 m."])]))
    Q.append((qnum(8, "Công thức tính <b>tốc độ trung bình</b> của một vật chuyển động là", "Biết",
                   "2.2"),
              [o for o in opts([
                  "A. v<sub>tb</sub> = s/Δt.", "B. v<sub>tb</sub> = Δd/Δt.",
                  "C. v<sub>tb</sub> = Δt/s.", "D. v<sub>tb</sub> = s.Δt."])]))
    Q.append((qnum(9, "Trên đồ thị độ dịch chuyển – thời gian, đường biểu diễn <b>nằm ngang, song "
                      "song với trục Ot</b> cho biết vật", "Biết", "2.3"),
              [o for o in opts([
                  "A. đang đứng yên.", "B. chuyển động thẳng đều.",
                  "C. chuyển động nhanh dần đều.", "D. chuyển động chậm dần đều."])]))
    Q.append((qnum(10, "Đồ thị độ dịch chuyển – thời gian của một vật là đường thẳng đi qua gốc "
                       "toạ độ và điểm (5 s; 20 m). Tốc độ của vật là", "Hiểu", "2.3"),
              [o for o in opts([
                  "A. 0,25 m/s.", "B. 4 m/s.", "C. 5 m/s.", "D. 20 m/s."])]))
    Q.append((qnum(11, "Gia tốc của một chuyển động là đại lượng đặc trưng cho", "Biết", "2.4"),
              [o for o in opts([
                  "A. mức độ nhanh, chậm của chuyển động.",
                  "B. sự thay đổi nhanh hay chậm của vận tốc.",
                  "C. quãng đường vật đi được trong một giây.",
                  "D. thời gian vật đi hết một mét đường."])]))
    Q.append((qnum(12, "Một ô tô đang chạy với vận tốc 20 m/s thì giảm tốc đều, sau 6 s vận tốc "
                       "còn 8 m/s. Gia tốc của ô tô là", "Hiểu", "2.4"),
              [o for o in opts([
                  "A. 2 m/s².", "B. −2 m/s².", "C. 4,67 m/s².", "D. −4,67 m/s²."])]))
    Q.append((qnum(13, "Hệ thức liên hệ giữa vận tốc, gia tốc và độ dịch chuyển trong chuyển động "
                       "thẳng biến đổi đều là", "Biết", "2.5"),
              [o for o in opts([
                  "A. v² − v₀² = 2ad.", "B. v² + v₀² = 2ad.",
                  "C. v − v₀ = 2ad.", "D. v² − v₀² = ad."])]))
    Q.append((qnum(14, "Trong chuyển động thẳng <b>chậm dần đều</b>, vectơ gia tốc", "Biết", "2.5"),
              [o for o in opts([
                  "A. cùng chiều với vectơ vận tốc.", "B. ngược chiều với vectơ vận tốc.",
                  "C. vuông góc với vectơ vận tốc.", "D. luôn bằng không."])]))
    Q.append((qnum(15, "Một xe đang chạy với vận tốc 5 m/s thì tăng tốc đều, sau 4 s đạt vận tốc "
                       "15 m/s. Quãng đường xe đi được trong 4 s đó là", "Hiểu", "2.5"),
              [o for o in opts([
                  "A. 20 m.", "B. 40 m.", "C. 60 m.", "D. 80 m."])]))
    Q.append((qnum(16, "Sự rơi tự do là sự rơi của một vật chỉ dưới tác dụng của", "Biết", "2.6"),
              [o for o in opts([
                  "A. trọng lực.", "B. lực cản của không khí.",
                  "C. lực đàn hồi của lò xo.", "D. lực ma sát nghỉ."])]))
    Q.append((qnum(17, "Một vật được thả rơi tự do từ độ cao 20 m. Lấy g = 10 m/s². Thời gian vật "
                       "rơi đến khi chạm đất là", "Hiểu", "2.6"),
              [o for o in opts([
                  "A. 1 s.", "B. 2 s.", "C. 4 s.", "D. 20 s."])]))
    Q.append((qnum(18, "Trong một ống đã hút hết không khí (chân không), người ta thả đồng thời từ "
                       "cùng một độ cao một hòn bi chì và một chiếc lông chim. Kết luận đúng là",
                   "Hiểu", "2.6"),
              [o for o in opts([
                  "A. Hòn bi chạm đáy trước vì nặng hơn.",
                  "B. Lông chim chạm đáy trước vì nhẹ hơn.",
                  "C. Hai vật chạm đáy cùng một lúc.",
                  "D. Không xác định được vì phụ thuộc hình dạng."])]))
    return Q


# =========================================================================== E
def part_e():
    o = [CondPageBreak(12.5 * cm)]
    o.append(SectionBanner("PHẦN E", "Đáp án & lời giải chi tiết",
                           "Chấm bài – hiểu vì sao sai – nhớ lâu hơn",
                           color=colors.HexColor("#1B7A45"), height=88))
    o.append(Spacer(1, 8))

    o.extend(H2("1. Bảng đáp án nhanh – Phần I"))
    keys = ["A", "B", "B", "C", "B", "B", "A", "A", "A",
            "B", "B", "B", "A", "B", "B", "A", "B", "C"]
    rows = [["CÂU"] + [str(i + 1) for i in range(9)],
            ["ĐÁP ÁN"] + keys[:9],
            ["CÂU"] + [str(i + 10) for i in range(9)],
            ["ĐÁP ÁN"] + keys[9:]]
    w = [2.05 * cm] + [(W - 2.05 * cm) / 9] * 9
    o.append(table(rows, w, size=9.2,
                   align=[TA_CENTER] * 10, head_bg=colors.HexColor("#1B7A45"),
                   extra=[("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#EAF6EF")),
                          ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#EAF6EF")),
                          ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1B7A45")),
                          ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#1B7A45")),
                          ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                          ("TEXTCOLOR", (0, 2), (-1, 2), colors.white),
                          ("FONTNAME", (0, 1), (-1, 1), "BVP-B"),
                          ("FONTNAME", (0, 3), (-1, 3), "BVP-B")]))
    o.append(Spacer(1, 4))
    o.append(P("<b>Phần II:</b> Câu 1: a – <b>Đúng</b> · b – <b>Sai</b> · c – <b>Đúng</b> · "
               "d – <b>Sai</b>. &nbsp;&nbsp; <b>Câu 2:</b> a – <b>Đúng</b> · b – <b>Đúng</b> · "
               "c – <b>Đúng</b> · d – <b>Sai</b>."))
    o.append(P("<b>Phần III:</b> Câu 1 – <b>60</b> (km/h) · Câu 2 – <b>30</b> (m/s)."))
    o.append(P("<b>Phần IV:</b> Câu 1 – v<sub>ca nô/nước</sub> = 20 km/h; về ngược dòng mất "
               "<b>2,25 giờ</b> (2 giờ 15 phút) · Câu 2 – v<sub>max</sub> = 20 m/s; "
               "s = <b>550 m</b> · Câu 3 – h<sub>max</sub> = <b>20 m</b>; t = <b>4 s</b>; "
               "s = <b>40 m</b>."))

    o.extend(H2("2. Lời giải chi tiết – Phần I"))
    sol1 = [
        ("1", "A", "Đối tượng của Vật lí là các dạng vận động của vật chất (chất, trường) và năng "
                  "lượng. Tế bào – di truyền thuộc Sinh học; xã hội thuộc Khoa học xã hội; phản ứng "
                  "hoá học thuộc Hoá học.", "Bẫy: nhầm “mọi hiện tượng tự nhiên” là của Vật lí."),
        ("2", "B", "Tuyệt đối không ăn, uống trong phòng thực hành vì hoá chất độc có thể lẫn vào "
                   "thức ăn gây ngộ độc, và thức ăn có thể làm nhiễm bẩn mẫu thí nghiệm.", ""),
        ("3", "B", "Tam giác vàng viền đen = biển cảnh báo. Cấm là tròn viền đỏ; bắt buộc là tròn "
                   "xanh; chỉ dẫn là vuông xanh.", "Nhớ: tam – cảnh, tròn đỏ – cấm, tròn xanh – phải."),
        ("4", "C", "Khối lượng riêng D = m/V phải đo m và V rồi tính → gián tiếp. Ba phương án còn "
                   "lại đọc trực tiếp trên dụng cụ.", ""),
        ("5", "B", "Độ dịch chuyển là đại lượng vectơ (có hướng). Quãng đường, tốc độ, thời gian "
                   "đều là đại lượng vô hướng.", ""),
        ("6", "B", "Hai chặng vuông góc: |Δd| = √(6² + 8²) = √100 = 10 m. (Quãng đường là 14 m – "
                   "phương án C là bẫy.)", "Bẫy C: cộng độ dài hai chặng."),
        ("7", "A", "s = 12 + 5 = 17 m. Δd = +12 − 5 = +7 m (vẫn theo chiều dương). Phương án C sai "
                   "vì độ dịch chuyển ở đây dương.", "Bẫy C: gán dấu sai."),
        ("8", "A", "Tốc độ trung bình dùng <b>quãng đường</b>: v<sub>tb</sub> = s/Δt. Công thức "
                   "Δd/Δt là vận tốc trung bình.", "Bẫy B: đúng công thức nhưng sai đại lượng."),
        ("9", "A", "d không đổi theo thời gian → vật đứng yên, v = 0 (độ dốc bằng 0).", ""),
        ("10", "B", "v = Δd/Δt = (20 − 0)/(5 − 0) = 4 m/s.", "Bẫy A: lấy nghịch đảo Δt/Δd."),
        ("11", "B", "Gia tốc đặc trưng cho sự biến thiên của vận tốc; “mức nhanh chậm của chuyển "
                    "động” là của tốc độ.", "Bẫy A: định nghĩa của tốc độ."),
        ("12", "B", "a = (8 − 20)/6 = −2 m/s². Âm vì vận tốc giảm theo chiều dương.", ""),
        ("13", "A", "Từ v = v₀ + at và d = v₀t + ½at², khử t được v² − v₀² = 2ad.", ""),
        ("14", "B", "Chậm dần đều: a ngược chiều v (a.v &lt; 0).", "Bẫy A: đó là nhanh dần đều."),
        ("15", "B", "d = (v₀ + v).t/2 = (5 + 15).4/2 = 40 m. (Hoặc a = 2,5 m/s²; "
                    "d = 5.4 + ½.2,5.16 = 40 m.)", "Bẫy C: dùng nhầm d = v.t = 15.4."),
        ("16", "A", "Rơi tự do chỉ chịu tác dụng của trọng lực, bỏ qua lực cản.", ""),
        ("17", "B", "t = √(2h/g) = √(2.20/10) = 2 s.", "Bẫy C: quên lấy căn (2h/g = 4)."),
        ("18", "C", "Trong chân không không có lực cản, mọi vật rơi với cùng gia tốc g → chạm đáy "
                    "cùng lúc (thí nghiệm ống Newton).", "Bẫy A: tưởng vật nặng rơi nhanh hơn."),
    ]
    for num, ans, why, trap in sol1:
        paras = [P("<b>Câu %s — %s</b>" % (num, ans), ParagraphStyle(
            "s1", parent=BODY, fontName="BVP-B", textColor=PRIMARY, spaceAfter=1.5)),
            P(why, ParagraphStyle("s2", parent=BODY, fontSize=9.5, leading=13.8))]
        if trap:
            paras.append(P('<font color="#B3261E" size="8.6">⚠ %s</font>' % trap,
                           ParagraphStyle("s3", parent=SMALL, fontSize=8.6)))
        o.append(Spacer(1, 4))
        o.append(KeepTogether(paras))

    o.extend(H2("3. Lời giải chi tiết – Phần II"))
    o.append(H3("Câu 1 – Người đi xe đạp (6 giờ)"))
    data = [["Ý", "KẾT LUẬN", "GIẢI THÍCH"],
            ["a", "ĐÚNG", "2 giờ đầu đi 30 km → v<sub>tb</sub> = 30/2 = 15 km/h."],
            ["b", "SAI", "Giờ thứ ba người <b>nghỉ</b> nên vận tốc bằng 0, không phải 30 km/h."],
            ["c", "ĐÚNG", "Đi 30 km rồi quay lại đúng điểm A: Δd = 0; quãng đường "
                          "s = 30 + 30 = 60 km."],
            ["d", "SAI", "Vận tốc trung bình = Δd/Δt = 0/6 = 0 km/h. Giá trị 10 km/h là "
                         "<b>tốc độ</b> trung bình (60/6)."]]
    o.append(table(data, [1.0 * cm, 2.0 * cm, 13.7 * cm], size=8.5,
                   align=[TA_CENTER, TA_CENTER, TA_LEFT],
                   head_bg=colors.HexColor("#0E7C86")))
    o.append(Spacer(1, 3))
    o.append(P("<i>Bài học:</i> câu d là bẫy kinh điển của đơn vị 2.2 – khi vật quay về chỗ cũ, "
               "<b>tốc độ trung bình ≠ 0 nhưng vận tốc trung bình = 0</b>.", SMALL))
    o.append(Spacer(1, 6))
    o.append(H3("Câu 2 – Ô tô hãm phanh"))
    data = [["Ý", "KẾT LUẬN", "GIẢI THÍCH"],
            ["a", "ĐÚNG", "Xe chậm dần đều, chiều dương là chiều chuyển động → a = −4 m/s²."],
            ["b", "ĐÚNG", "t = (v − v₀)/a = (0 − 20)/(−4) = 5 s."],
            ["c", "ĐÚNG", "d = v₀t + ½at² = 20.5 + ½.(−4).25 = 100 − 50 = 50 m. "
                          "(Kiểm tra: v₀²/(2|a|) = 400/8 = 50 m.)"],
            ["d", "SAI", "d = v₀²/(2|a|) tỉ lệ với <b>bình phương</b> vận tốc → v₀ tăng 2 lần thì "
                         "quãng đường tăng <b>4 lần</b> (200 m)."]]
    o.append(table(data, [1.0 * cm, 2.0 * cm, 13.7 * cm], size=8.5,
                   align=[TA_CENTER, TA_CENTER, TA_LEFT],
                   head_bg=colors.HexColor("#0E7C86")))

    o.extend(H2("4. Lời giải chi tiết – Phần III"))
    o.append(P("<b>Câu 1.</b> v<sub>tb</sub> = s/t = 90/1,5 = <b>60 km/h</b>. "
               "(Nếu đổi ra m/s: 60 : 3,6 ≈ 16,7 m/s.)"))
    o.append(P("<b>Câu 2.</b> v = √(2gh) = √(2.10.45) = √900 = <b>30 m/s</b>. "
               "(Có thể tính t = √(2h/g) = 3 s rồi v = g.t = 30 m/s.)"))

    o.extend(H2("5. Lời giải chi tiết – Phần IV (có thang điểm)"))
    o.append(H3("Câu 1 – Ca nô xuôi dòng, ngược dòng (1,0 điểm)"))
    o.append(P("<i>Tóm tắt:</i> s = 36 km; t<sub>xuôi</sub> = 1,5 h; v<sub>nước</sub> = 4 km/h."))
    o.extend(numbered([
        "Vận tốc ca nô so với bờ khi xuôi dòng: v<sub>xuôi</sub> = s/t = 36/1,5 = <b>24 km/h</b>. "
        "<font color=\"#1B7A45\">(0,25 đ)</font>",
        "Công thức cộng vận tốc: v<sub>xuôi</sub> = v<sub>ca nô</sub> + v<sub>nước</sub> → "
        "v<sub>ca nô</sub> = 24 − 4 = <b>20 km/h</b>. <font color=\"#1B7A45\">(0,25 đ)</font>",
        "Khi ngược dòng: v<sub>ngược</sub> = 20 − 4 = <b>16 km/h</b>. "
        "<font color=\"#1B7A45\">(0,25 đ)</font>",
        "Thời gian về: t = 36/16 = <b>2,25 giờ</b> = 2 giờ 15 phút. "
        "<font color=\"#1B7A45\">(0,25 đ)</font>",
    ]))
    o.append(Spacer(1, 3))
    o.extend(box("Vì sao nhiều bạn làm sai câu này?",
                 [P("Đề cho “vận tốc ca nô so với nước” chứ không phải so với bờ. Nếu lấy ngay "
                    "24 km/h làm vận tốc ca nô thì bước 2 và 3 đều sai. Hãy luôn viết rõ "
                    "<b>vật nào so với vật nào</b> rồi mới áp dụng v₁₃ = v₁₂ + v₂₃.")], kind="red"))
    o.append(H3("Câu 2 – Xe ba giai đoạn (1,0 điểm)"))
    o.append(P("<i>Tóm tắt:</i> GĐ1: v₀ = 0, a₁ = 2 m/s², t₁ = 10 s. GĐ2: thẳng đều, t₂ = 20 s. "
               "GĐ3: chậm dần đều đến khi dừng, t₃ = 5 s."))
    o.extend(numbered([
        "Vận tốc lớn nhất (cuối GĐ1, cũng là vận tốc của GĐ2): v = v₀ + a₁t₁ = 0 + 2.10 = "
        "<b>20 m/s</b>. <font color=\"#1B7A45\">(0,25 đ)</font>",
        "GĐ1: s₁ = ½a₁t₁² = ½.2.100 = <b>100 m</b>. <font color=\"#1B7A45\">(0,25 đ)</font>",
        "GĐ2: s₂ = v.t₂ = 20.20 = <b>400 m</b>. <font color=\"#1B7A45\">(0,25 đ)</font>",
        "GĐ3: s₃ = (v + 0).t₃/2 = 20.5/2 = <b>50 m</b> → tổng s = 100 + 400 + 50 = "
        "<b>550 m</b>. <font color=\"#1B7A45\">(0,25 đ)</font>",
    ]))
    o.append(Spacer(1, 2))
    o.append(P("<i>Cách kiểm tra nhanh:</i> vẽ đồ thị v – t gồm một đoạn dốc lên (0 → 20 m/s trong "
               "10 s), một đoạn ngang (20 s) và một đoạn dốc xuống (20 → 0 trong 5 s). Diện tích "
               "hình thang + hình chữ nhật + tam giác = 100 + 400 + 50 = 550 m.", SMALL))
    o.append(H3("Câu 3 – Ném thẳng đứng lên (1,0 điểm)"))
    o.append(P("<i>Tóm tắt:</i> v₀ = 20 m/s hướng lên; g = 10 m/s² hướng xuống. Chọn chiều dương "
               "hướng lên → a = −g = −10 m/s²."))
    o.extend(numbered([
        "Tại độ cao lớn nhất v = 0: t<sub>lên</sub> = (0 − 20)/(−10) = <b>2 s</b>. "
        "<font color=\"#1B7A45\">(0,25 đ)</font>",
        "Độ cao lớn nhất: h = v₀t + ½at² = 20.2 + ½.(−10).4 = 40 − 20 = <b>20 m</b> "
        "(hoặc h = v₀²/2g = 400/20 = 20 m). <font color=\"#1B7A45\">(0,25 đ)</font>",
        "Thời gian rơi xuống từ độ cao 20 m bằng thời gian đi lên (2 s) → tổng thời gian "
        "<b>4 s</b>. <font color=\"#1B7A45\">(0,25 đ)</font>",
        "Quãng đường: lên 20 m + xuống 20 m = <b>40 m</b> (trong khi độ dịch chuyển = 0). "
        "<font color=\"#1B7A45\">(0,25 đ)</font>",
    ]))
    o.append(Spacer(1, 3))
    o.append(P("<i>Lưu ý:</i> nếu quên chọn chiều dương, nhiều bạn ra h = −20 m hoặc t âm. Hãy "
               "viết câu “Chọn chiều dương hướng lên” ngay đầu bài – đó cũng là một phần điểm "
               "trình bày.", SMALL))
    return o
