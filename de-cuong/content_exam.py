# -*- coding: utf-8 -*-
"""PHẦN B – Đề mẫu đúng 100% ma trận + đáp án & lời giải chi tiết."""
from helpers import (P, h1, h2, h3, sp, hr, callout, styled_table, question,
                     tf_question, answer_block, tag, make_dt_graph,
                     BG_TEAL, BG_GREEN, BG_YELLOW, TEAL, GREEN, ORANGE)
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether


def get_story():
    s = []
    s.append(h1("PHẦN B \u00b7 ĐỀ MẪU ĐÚNG MA TRẬN \u2014 LÀM TRONG 50 PHÚT"))
    s.append(callout("\u2605 Đọc trước khi làm",
                     ["Đề mẫu dưới đây được biên soạn <b>mới</b> để bám đúng từng ô của ma trận (xem Phần 0): "
                      "Phần I = 18 câu (10 Biết + 8 Hiểu), Phần II = 2 câu Đúng/Sai (8 ý), Phần III = 2 câu trả lời ngắn, Phần IV = 3 câu tự luận. "
                      "Mỗi câu đều gắn nhãn [đơn vị \u00b7 mức độ] để em đối chiếu ngược về Phần A.",
                      "<b>Cách làm:</b> Bấm giờ 50 phút, làm một mạch không xem đáp án. Hết giờ mới sang mục B2 chấm điểm và đọc lời giải. "
                      "Tài liệu gốc <b>không công bố điểm số từng phần</b>, nên đề mẫu không tự gán điểm \u2014 chỉ cần đếm số ý đúng để tự đánh giá."],
                     bg=BG_YELLOW, accent=ORANGE))
    s.append(sp(3))

    # ---------------------------------------------------------- PHẦN I
    s.append(h2("B1. ĐỀ MẪU"))
    s.append(h3("PHẦN I \u2014 Câu trắc nghiệm nhiều phương án lựa chọn (18 câu). Mỗi câu chỉ chọn một phương án."))
    qs = [
        question(1, "Đối tượng nghiên cứu chủ yếu của Vật lí là", ["các dạng vận động của vật chất (chất, trường) và năng lượng.",
                 "các chất và sự biến đổi của các chất.", "sự sinh trưởng, phát triển của các loài sinh vật.",
                 "cấu tạo của Trái Đất và bầu khí quyển."], "1.1", "Biết"),
        question(2, "Thao tác đúng trước khi cắm hoặc tháo thiết bị điện trong phòng thực hành là",
                 ["cắm phích điện khi công tắc nguồn vẫn bật để kiểm tra nhanh.",
                  "dùng tay còn ướt cầm phích điện cho chắc.",
                  "tắt công tắc nguồn thiết bị điện trước khi cắm hoặc tháo.",
                  "cắm vào nguồn có hiệu điện thế bất kì, miễn phích vừa ổ cắm."], "1.2", "Biết"),
        question(3, "Một biển báo hình tam giác đều, viền đen, nền vàng trong phòng thực hành cho biết",
                 ["điều cấm thực hiện.", "cảnh báo khu vực nguy hiểm.", "nguy hại do hoá chất gây ra.", "chỉ dẫn thực hiện."], "1.2", "Hiểu"),
        question(4, "Sai số tỉ đối của phép đo đại lượng A được tính bằng công thức",
                 ["\u03b4A = (\u0100/\u0394A) \u00d7 100%.", "\u03b4A = (\u0394A + \u0100) \u00d7 100%.",
                  "\u03b4A = (\u0100 \u2212 \u0394A) \u00d7 100%.", "\u03b4A = (\u0394A/\u0100) \u00d7 100%."], "1.3", "Biết"),
        question(5, "Độ dịch chuyển là", ["đại lượng vectơ có hướng từ vị trí đầu đến vị trí cuối của chuyển động.",
                 "độ dài quỹ đạo mà vật đi được.", "đại lượng vô hướng luôn dương.",
                 "quãng đường vật đi được trong một đơn vị thời gian."], "2.1", "Biết"),
        question(6, "Một người đi 60 m về phía Đông rồi quay lại 20 m về phía Tây. Chọn chiều dương là chiều về phía Đông. "
                    "Quãng đường đi được và độ dịch chuyển của người đó là",
                 ["s = 40 m; d = 80 m.", "s = 80 m; d = 40 m về phía Đông.",
                  "s = 80 m; d = 20 m về phía Đông.", "s = 40 m; d = 40 m về phía Đông."], "2.1", "Hiểu"),
        question(7, "Một vật đi 100 m về phía Đông rồi quay trở lại đúng vị trí xuất phát sau khi đi 100 m về phía Tây. "
                    "Quãng đường và độ lớn độ dịch chuyển của vật là",
                 ["s = 0; |d| = 200 m.", "s = 200 m; |d| = 200 m.", "s = 200 m; |d| = 0.", "s = 0; |d| = 0."], "2.1", "Hiểu"),
        question(8, "Tốc độ trung bình của một chuyển động được xác định bằng",
                 ["v = s/t.", "v = s\u00b7t.", "v = t/s.", "v = s \u2212 t."], "2.2", "Biết"),
        question(9, "Đồ thị độ dịch chuyển \u2013 thời gian của một vật là đoạn thẳng nằm ngang, song song với trục thời gian. Vật đang",
                 ["chuyển động nhanh dần đều.", "chuyển động chậm dần đều.",
                  "chuyển động thẳng đều với vận tốc lớn.", "đứng yên."], "2.3", "Biết"),
        question(10, "Đồ thị độ dịch chuyển \u2013 thời gian của một chuyển động thẳng là đoạn thẳng đi qua gốc toạ độ và điểm (10 s; 50 m) "
                     "(xem Hình B1). Vận tốc của vật là",
                 ["2 m/s.", "5 m/s.", "10 m/s.", "0,2 m/s."], "2.3", "Hiểu"),
        question(11, "Gia tốc của chuyển động biến đổi được tính bằng công thức nào sau đây, và có đơn vị là gì?",
                 ["a = \u0394t/\u0394v; đơn vị m/s.", "a = \u0394v\u00b7\u0394t; đơn vị m/s.",
                  "a = \u0394v/\u0394t; đơn vị m/s\u00b2.", "a = v\u00b7t; đơn vị m/s\u00b2."], "2.4", "Biết"),
        question(12, "Một xe tăng vận tốc từ 5 m/s lên 15 m/s trong 5 s. Gia tốc của xe là",
                 ["2 m/s\u00b2.", "4 m/s\u00b2.", "0,5 m/s\u00b2.", "10 m/s\u00b2."], "2.4", "Hiểu"),
        question(13, "Chuyển động thẳng biến đổi đều là chuyển động",
                 ["thẳng có gia tốc thay đổi đều theo thời gian.", "cong có gia tốc không đổi.",
                  "thẳng có vận tốc không đổi.", "thẳng có gia tốc không đổi theo thời gian."], "2.5", "Biết"),
        question(14, "Hệ thức liên hệ giữa vận tốc, gia tốc và độ dịch chuyển (không chứa thời gian) trong chuyển động thẳng biến đổi đều là",
                 ["v = v\u2080 + at.", "v\u00b2 \u2212 v\u2080\u00b2 = 2ad.",
                  "d = v\u2080t + \u00bdat\u00b2.", "x = x\u2080 + v\u2080t + \u00bdat\u00b2."], "2.5", "Biết"),
        question(15, "Một vật chuyển động thẳng biến đổi đều với v\u2080 = 10 m/s, a = 2 m/s\u00b2. Độ dịch chuyển của vật sau 3 s là",
                 ["30 m.", "33 m.", "39 m.", "48 m."], "2.5", "Hiểu"),
        question(16, "Sự rơi tự do là", ["sự rơi chỉ dưới tác dụng của trọng lực.",
                 "sự rơi của mọi vật trong không khí.", "sự rơi có vận tốc ban đầu khác không.",
                 "sự rơi với gia tốc thay đổi theo thời gian."], "2.6", "Biết"),
        question(17, "Thả rơi tự do một vật, lấy g = 9,8 m/s\u00b2. Vận tốc của vật sau 2 s là",
                 ["9,8 m/s.", "19,6 m/s.", "29,4 m/s.", "4,9 m/s."], "2.6", "Hiểu"),
        question(18, "Thả rơi tự do một vật, lấy g = 9,8 m/s\u00b2. Quãng đường vật rơi được sau 3 s là",
                 ["14,7 m.", "29,4 m.", "88,2 m.", "44,1 m."], "2.6", "Hiểu"),
    ]
    for i, qq in enumerate(qs):
        s.append(qq)
        if i == 9:  # sau Câu 10 chèn hình
            s.append(make_dt_graph([(0, 0), (10, 50)], x_ticks=[(10, "10")], y_ticks=[(50, "50")]))
            s.append(P("<i>Hình B1.</i> Đồ thị d\u2013t cho Câu 10.", "Caption"))
        s.append(sp(2))

    # ---------------------------------------------------------- PHẦN II
    s.append(h3("PHẦN II \u2014 Câu trắc nghiệm Đúng/Sai (2 câu, mỗi câu 4 ý). Trong mỗi ý, chọn Đúng hoặc Sai."))
    s.append(tf_question(1, "Một vật chuyển động thẳng có đồ thị độ dịch chuyển \u2013 thời gian như Hình B2.",
                         ["Tốc độ là đại lượng vectơ vì được xác định bằng độ dịch chuyển chia cho thời gian.",
                          "Vận tốc trung bình bằng độ dịch chuyển chia cho thời gian thực hiện độ dịch chuyển đó.",
                          "Trong 10 s đầu, đồ thị dốc lên nên vật chuyển động theo chiều dương.",
                          "Từ 10 s đến 15 s, đồ thị nằm ngang nên vật chuyển động thẳng đều với vận tốc khác không."], "2.2 + 2.3"))
    s.append(make_dt_graph([(0, 0), (10, 40), (15, 40)], x_ticks=[(10, "10"), (15, "15")], y_ticks=[(40, "40")]))
    s.append(P("<i>Hình B2.</i> Đồ thị d\u2013t cho Phần II \u2013 Câu 1.", "Caption"))
    s.append(tf_question(2, "Một ô tô chuyển động thẳng với vận tốc ban đầu v\u2080 = 20 m/s và gia tốc a = \u22122 m/s\u00b2 "
                            "(chiều dương là chiều chuyển động ban đầu).",
                         ["Chuyển động thẳng biến đổi đều là chuyển động thẳng có gia tốc không đổi theo thời gian.",
                          "Độ dịch chuyển được tính bằng công thức d = v\u2080t + at\u00b2.",
                          "Sau 4 s, vận tốc của ô tô là 12 m/s.",
                          "Độ dịch chuyển của ô tô sau 4 s là 80 m."], "2.5"))
    s.append(sp(2))

    # ---------------------------------------------------------- PHẦN III
    s.append(h3("PHẦN III \u2014 Câu trắc nghiệm trả lời ngắn (2 câu). Chỉ ghi kết quả kèm đơn vị."))
    s.append(question(1, "Một vật đi được quãng đường 150 m trong 10 s. Tốc độ trung bình của vật là bao nhiêu?", None, "2.2", "Biết"))
    s.append(question(2, "Thả rơi tự do một vật từ độ cao 45 m, lấy g = 10 m/s\u00b2. Thời gian để vật chạm đất là bao nhiêu?", None, "2.6", "Hiểu"))

    # ---------------------------------------------------------- PHẦN IV
    s.append(h3("PHẦN IV \u2014 Tự luận (3 câu). Trình bày lời giải rõ ràng, có đổi đơn vị và kết luận."))
    s.append(question(1, "Một chiếc thuyền chuyển động so với nước với vận tốc 8 m/s hướng về phía Bắc. "
                          "Dòng nước chảy so với bờ với vận tốc 6 m/s hướng về phía Đông. Xác định độ lớn và hướng của vận tốc "
                          "của thuyền so với bờ (vẽ sơ đồ vectơ).", None, "2.2", "Hiểu"))
    s.append(question(2, "Một ô tô đang chuyển động với vận tốc 36 km/h thì tăng tốc đều với gia tốc 2 m/s\u00b2. "
                          "a) Tính vận tốc của ô tô sau 5 s. b) Tính quãng đường ô tô đi được trong 5 s đó. "
                          "c) Sau bao lâu ô tô đạt vận tốc 30 m/s?", None, "2.5", "Vận dụng"))
    s.append(question(3, "Một ô tô đang chuyển động với vận tốc 72 km/h thì người lái thấy chướng ngại vật cách xe 50 m "
                          "nên hãm phanh. Xe chuyển động chậm dần đều với gia tốc có độ lớn 5 m/s\u00b2. "
                          "a) Tính thời gian từ lúc hãm phanh đến khi xe dừng hẳn. b) Tính quãng đường xe đi được đến khi dừng. "
                          "c) Xe có dừng kịp trước chướng ngại vật không? Vì sao?", None, "2.5", "Vận dụng"))
    s.append(sp(2))
    s.append(callout("\u2605 Tự chấm nhanh trước khi xem lời giải",
                     ["Đếm: Phần I đúng \u2026/18 \u00b7 Phần II đúng \u2026/8 ý \u00b7 Phần III đúng \u2026/2 \u00b7 Phần IV tự đánh giá \u2026/3 câu. "
                      "Ghi lại <b>mã đơn vị</b> của mọi ý sai (ví dụ 2.5) \u2014 đó chính là bài A cần đọc lại trong Phần A."],
                     bg=BG_TEAL, accent=TEAL))

    # ---------------------------------------------------------- ĐÁP ÁN
    s.append(h2("B2. ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT \u2014 PHẦN I"))
    s.append(styled_table([
        ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        ["Đáp án", "A", "C", "B", "D", "A", "B", "C", "A", "D"],
        ["Câu", "10", "11", "12", "13", "14", "15", "16", "17", "18"],
        ["Đáp án", "B", "C", "A", "D", "B", "C", "A", "B", "D"],
    ], [22 * mm] + [13.2 * mm] * 9, align_center_cols=set(range(10))))
    s.append(sp(3))
    explanations = [
        ("1 \u2013 A", "Đối tượng của Vật lí là vận động của vật chất (chất, trường) và năng lượng. Các phương án còn lại thuộc Hoá học, Sinh học, Địa lí."),
        ("2 \u2013 C", "Quy tắc điện cơ bản: tắt công tắc nguồn <i>trước</i> khi cắm/tháo; tay phải khô, phích phải đúng điện áp định mức."),
        ("3 \u2013 B", "Tam giác + nền vàng = cảnh báo khu vực nguy hiểm (\u201cTam vàng coi chừng\u201d). Tròn đỏ = cấm; vuông cam = hoá chất; chữ nhật = chỉ dẫn."),
        ("4 \u2013 D", "\u03b4A = \u0394A/\u0100 \u00d7 100%. \u0394A mang đơn vị, \u03b4A là % \u2014 càng nhỏ càng chính xác."),
        ("5 \u2013 A", "Độ dịch chuyển là vectơ đầu \u2192 cuối; độ dài quỹ đạo là quãng đường (vô hướng)."),
        ("6 \u2013 B", "s = 60 + 20 = 80 m (cộng dồn). d = 60 \u2212 20 = +40 m, dấu + nghĩa là còn ở phía Đông so với điểm đầu."),
        ("7 \u2013 C", "Về đúng điểm xuất phát nên d = 0, nhưng đường đã đi vẫn là s = 100 + 100 = 200 m. Đây là bẫy \u201cquay lại \u2192 d = 0\u201d."),
        ("8 \u2013 A", "Tốc độ trung bình dùng <i>quãng đường</i>: v = s/t. Công thức d/t là của vận tốc."),
        ("9 \u2013 D", "Đồ thị d\u2013t nằm ngang: d không đổi theo t \u2192 vật đứng yên, v = 0."),
        ("10 \u2013 B", "v = \u0394d/\u0394t = 50/10 = 5 m/s (độ dốc của đồ thị)."),
        ("11 \u2013 C", "a = \u0394v/\u0394t, đơn vị (m/s)/s = m/s\u00b2. Kiểm tra đơn vị loại ngay được 2 phương án."),
        ("12 \u2013 A", "a = (15 \u2212 5)/5 = 10/5 = 2 m/s\u00b2."),
        ("13 \u2013 D", "Đủ hai ý: <b>thẳng</b> và <b>gia tốc không đổi</b>. Thiếu một ý là sai định nghĩa."),
        ("14 \u2013 B", "Chỉ v\u00b2 \u2212 v\u2080\u00b2 = 2ad không chứa t \u2014 \u201ccông thức không chứa t\u201d."),
        ("15 \u2013 C", "d = v\u2080t + \u00bdat\u00b2 = 10\u00b73 + \u00bd\u00b72\u00b73\u00b2 = 30 + 9 = 39 m."),
        ("16 \u2013 A", "Rơi tự do: <b>chỉ</b> chịu trọng lực (bỏ qua sức cản). Rơi trong không khí thường còn sức cản nên chưa chắc là rơi tự do."),
        ("17 \u2013 B", "v = gt = 9,8\u00b72 = 19,6 m/s."),
        ("18 \u2013 D", "s = \u00bdgt\u00b2 = \u00bd\u00b79,8\u00b73\u00b2 = \u00bd\u00b79,8\u00b79 = 44,1 m."),
    ]
    for title, text in explanations:
        s.append(P(f"<b>Câu {title}.</b> {text}", "Ans"))
    s.append(sp(2))

    s.append(h2("B3. ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT \u2014 PHẦN II, III, IV"))
    s.append(h3("Phần II \u2013 Đúng/Sai"))
    s.append(styled_table([
        ["Câu", "Ý a", "Ý b", "Ý c", "Ý d"],
        ["1 (2.2 + 2.3)", "SAI", "ĐÚNG", "ĐÚNG", "SAI"],
        ["2 (2.5)", "ĐÚNG", "SAI", "ĐÚNG", "SAI"],
    ], [32 * mm, 31 * mm, 31 * mm, 31 * mm, 31 * mm], align_center_cols={1, 2, 3, 4}))
    s.append(sp(2))
    s.append(P("<b>Câu 1a \u2013 Sai:</b> tốc độ là đại lượng <b>vô hướng</b> (dùng quãng đường); đại lượng vectơ xác định bằng độ dịch chuyển là <b>vận tốc</b>. "
               "<b>1b \u2013 Đúng:</b> đúng định nghĩa vận tốc trung bình. "
               "<b>1c \u2013 Đúng:</b> d tăng theo t, đúng chiều dương. "
               "<b>1d \u2013 Sai:</b> đồ thị nằm ngang \u2192 d không đổi \u2192 vật <b>đứng yên</b> (v = 0), không phải chuyển động thẳng đều với v \u2260 0.", "Ans"))
    s.append(P("<b>Câu 2a \u2013 Đúng:</b> đúng định nghĩa CĐTBĐĐ. "
               "<b>2b \u2013 Sai:</b> thiếu hệ số \u00bd; đúng là d = v\u2080t + \u00bdat\u00b2. "
               "<b>2c \u2013 Đúng:</b> v = 20 + (\u22122)\u00b74 = 12 m/s (a âm, v giảm \u2014 chậm dần đều nhưng chưa dừng). "
               "<b>2d \u2013 Sai:</b> d = 20\u00b74 + \u00bd(\u22122)\u00b74\u00b2 = 80 \u2212 16 = 64 m, không phải 80 m (80 m là khi quên số hạng gia tốc).", "Ans"))
    s.append(h3("Phần III \u2013 Trả lời ngắn"))
    s.append(answer_block("Câu 1: 15 m/s", "v = s/t = 150/10 = 15 m/s. Ghi thiếu đơn vị vẫn nên tự trừ ý khi tự chấm \u2014 thói quen ghi đơn vị cứu điểm ở mọi dạng câu hỏi."))
    s.append(sp(2))
    s.append(answer_block("Câu 2: 3 s", "Từ s = \u00bdgt\u00b2 với s = h = 45 m: t = \u221a(2h/g) = \u221a(2\u00b745/10) = \u221a9 = 3 s."))
    s.append(sp(2))
    s.append(h3("Phần IV \u2013 Tự luận (lời giải mẫu; thang ý chỉ là gợi ý tự chấm)"))
    s.append(P("<b>Câu 1 [2.2 \u00b7 Hiểu].</b> Gọi (1) thuyền, (2) nước, (3) bờ. Công thức cộng vận tốc: vectơ v<sub>1,3</sub> = vectơ v<sub>1,2</sub> + vectơ v<sub>2,3</sub>. "
               "Hai thành phần vuông góc (Bắc \u22a5 Đông) nên độ lớn: v<sub>1,3</sub> = \u221a(8\u00b2 + 6\u00b2) = \u221a100 = <b>10 m/s</b>. "
               "Hướng: hợp với hướng Bắc về phía Đông một góc \u03b1 với tan\u03b1 = 6/8 = 0,75 \u2192 \u03b1 \u2248 37\u00b0. "
               "Sơ đồ vectơ: vẽ vectơ 6 (Đông) nối tiếp vectơ 8 (Bắc), vectơ tổng là cạnh huyền (mô hình 6\u20138\u201310).", "Ans"))
    s.append(P("<b>Câu 2 [2.5 \u00b7 Vận dụng].</b> Đổi 36 km/h = 10 m/s. Chọn chiều dương là chiều chuyển động, a = +2 m/s\u00b2. "
               "a) v = v\u2080 + at = 10 + 2\u00b75 = <b>20 m/s</b> (72 km/h). "
               "b) d = v\u2080t + \u00bdat\u00b2 = 10\u00b75 + \u00bd\u00b72\u00b75\u00b2 = 50 + 25 = <b>75 m</b> (đi một chiều nên quãng đường cũng là 75 m). "
               "c) t = (v \u2212 v\u2080)/a = (30 \u2212 10)/2 = <b>10 s</b>.", "Ans"))
    s.append(P("<b>Câu 3 [2.5 \u00b7 Vận dụng].</b> Đổi 72 km/h = 20 m/s. Chọn chiều dương là chiều chuyển động \u2192 a = \u22125 m/s\u00b2, khi dừng v = 0. "
               "a) t = (0 \u2212 20)/(\u22125) = <b>4 s</b>. "
               "b) Cách 1 (không chứa t): d = (v\u00b2 \u2212 v\u2080\u00b2)/(2a) = (0 \u2212 400)/(\u221210) = <b>40 m</b>. Cách 2 kiểm tra: d = 20\u00b74 \u2212 \u00bd\u00b75\u00b74\u00b2 = 80 \u2212 40 = 40 m. "
               "c) 40 m &lt; 50 m nên xe <b>dừng kịp</b>, còn cách chướng ngại vật 10 m (chưa tính thời gian phản xạ của người lái).", "Ans"))
    s.append(sp(2))
    s.append(callout("\u2605 Sau khi chấm xong, đừng dừng ở điểm số",
                     ["Khoanh tròn <b>kĩ năng</b> đã làm em mất điểm nhất (đổi đơn vị? dấu của a? đọc đồ thị? thiếu \u00bd?) rồi làm lại đúng dạng đó ở Phần C. "
                      "Mỗi lỗi được sửa ở Phần C thường đáng giá hơn làm thêm một đề mới."],
                     bg=BG_GREEN, accent=GREEN))
    return s
