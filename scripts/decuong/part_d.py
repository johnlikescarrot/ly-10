# -*- coding: utf-8 -*-
"""Phần D – Đề thi mô phỏng bám sát ma trận + đáp án, lời giải chi tiết."""
from __future__ import annotations

from reportlab.platypus import Spacer

from .style import (
    CONTENT_W, P, S, SPC, box, data_table, formula, numbered, question, rule,
)

MCQ = [
    # (số, mức, bài, đề, [A, B, C, D], đáp án, giải thích)
    (1, "Biết", "1.1",
     "Đối tượng nghiên cứu chủ yếu của Vật lí là",
     ["các dạng vận động của vật chất và những quy luật chi phối chúng.",
      "cấu tạo và tính chất của các hợp chất hoá học.",
      "sự sinh trưởng và phát triển của các loài sinh vật.",
      "các quy luật vận động của xã hội loài người."],
     "A", "Vật lí nghiên cứu vật chất, các dạng vận động của vật chất và quy luật của chúng."),
    (2, "Biết", "1.2",
     "Hành vi nào sau đây <b>vi phạm</b> quy tắc an toàn trong phòng thực hành?",
     ["Đeo kính bảo hộ khi làm thí nghiệm với hoá chất.",
      "Kiểm tra dây dẫn điện trước khi cắm điện.",
      "Tắt thiết bị và ngắt điện sau khi làm xong thí nghiệm.",
      "Tự ý lắp ráp và thử nghiệm thiết bị khi chưa được hướng dẫn."],
     "D", "Chỉ được sử dụng thiết bị khi đã đọc hướng dẫn và được giáo viên cho phép."),
    (3, "Hiểu", "1.2",
     "Biển báo hình tam giác đều, viền đỏ, nền vàng, ở giữa có hình tia chớp cảnh báo",
     ["khu vực có điện áp nguy hiểm.",
      "khu vực cấm sử dụng lửa.",
      "nơi có chất phóng xạ.",
      "vị trí đặt bình chữa cháy."],
     "A", "Tam giác viền đỏ nền vàng là biển cảnh báo; tia chớp = nguy hiểm về điện."),
    (4, "Biết", "1.3",
     "Phép đo nào sau đây là <b>phép đo gián tiếp</b>?",
     ["Dùng thước đo chiều dài của quyển sách.",
      "Dùng cân đo khối lượng của quả nặng.",
      "Đo quãng đường và thời gian rồi tính tốc độ.",
      "Dùng đồng hồ bấm giây đo thời gian chạy."],
     "C", "Tốc độ được tính qua công thức từ hai phép đo trực tiếp → phép đo gián tiếp."),
    (5, "Biết", "2.1",
     "Đại lượng nào sau đây là đại lượng <b>vectơ</b>?",
     ["Quãng đường.", "Tốc độ trung bình.", "Thời gian.", "Độ dịch chuyển."],
     "D", "Độ dịch chuyển có cả độ lớn và hướng → đại lượng vectơ."),
    (6, "Hiểu", "2.1",
     "Một người đi bộ từ A đến B dài 300 m rồi quay lại theo đường cũ 100 m. "
     "Quãng đường và độ lớn độ dịch chuyển của người đó là",
     ["400 m và 400 m.", "200 m và 400 m.", "400 m và 200 m.", "300 m và 200 m."],
     "C", "s = 300 + 100 = 400 m; |Δd| = 300 − 100 = 200 m."),
    (7, "Hiểu", "2.1",
     "Phát biểu nào sau đây <b>đúng</b>?",
     ["Độ lớn của độ dịch chuyển luôn bằng quãng đường đi được.",
      "Quãng đường là đại lượng vectơ.",
      "Độ dịch chuyển của vật không phụ thuộc vào hệ quy chiếu.",
      "Độ lớn của độ dịch chuyển không lớn hơn quãng đường đi được."],
     "D", "|Δd| ≤ s; dấu bằng chỉ khi vật chuyển động thẳng và không đổi chiều."),
    (8, "Biết", "2.2",
     "Công thức tính <b>tốc độ trung bình</b> của một vật chuyển động là",
     ["v = s/Δt.", "v = Δd/Δt.", "v = v<sub>0</sub> + a·t.", "a = Δv/Δt."],
     "A", "Tốc độ trung bình dùng quãng đường s; Δd/Δt là vận tốc trung bình."),
    (9, "Biết", "2.3",
     "Trên đồ thị độ dịch chuyển – thời gian của chuyển động thẳng, độ dốc của đường biểu diễn cho biết",
     ["gia tốc của vật.", "quãng đường vật đi được.", "vận tốc của vật.", "thời gian chuyển động."],
     "C", "Độ dốc = Δd/Δt = vận tốc."),
    (10, "Hiểu", "2.3",
     "Đồ thị độ dịch chuyển – thời gian của một vật có đoạn nằm ngang trong khoảng từ t = 2 s đến t = 6 s. "
     "Trong khoảng thời gian đó vật",
     ["chuyển động thẳng đều với vận tốc 4 m/s.", "đứng yên.",
      "chuyển động ngược chiều dương.", "chuyển động nhanh dần đều."],
     "B", "Độ dốc bằng 0 → vận tốc bằng 0 → vật đứng yên."),
    (11, "Biết", "2.4",
     "Đơn vị của gia tốc trong hệ SI là",
     ["m/s².", "m/s.", "m·s.", "m²/s."],
     "A", "a = Δv/Δt → (m/s)/s = m/s²."),
    (12, "Hiểu", "2.4",
     "Một xe đang chuyển động với vận tốc 10 m/s thì tăng tốc đều, sau 5 s đạt 20 m/s. Gia tốc của xe là",
     ["0,5 m/s².", "6 m/s².", "2 m/s².", "10 m/s²."],
     "C", "a = (20 − 10)/5 = 2 m/s²."),
    (13, "Biết", "2.5",
     "Chuyển động thẳng <b>chậm dần đều</b> là chuyển động có",
     ["gia tốc cùng chiều với vận tốc.", "gia tốc bằng 0.",
      "tốc độ không đổi theo thời gian.", "gia tốc ngược chiều với vận tốc."],
     "D", "Chậm dần ⇔ a ngược chiều v."),
    (14, "Biết", "2.5",
     "Hệ thức liên hệ giữa vận tốc, gia tốc và quãng đường trong chuyển động thẳng biến đổi đều là",
     ["v² + v<sub>0</sub>² = 2as.", "v² − v<sub>0</sub>² = 2as.",
      "v − v<sub>0</sub> = 2as.", "v² − v<sub>0</sub>² = as."],
     "B", "Công thức liên hệ không chứa thời gian: v² − v₀² = 2as."),
    (15, "Hiểu", "2.5",
     "Một vật bắt đầu chuyển động thẳng nhanh dần đều từ trạng thái đứng yên, sau 4 s đi được 8 m. "
     "Gia tốc của vật là",
     ["1 m/s².", "0,5 m/s².", "2 m/s².", "4 m/s²."],
     "A", "s = ½at² → 8 = ½·a·16 → a = 1 m/s²."),
    (16, "Biết", "2.6",
     "Sự rơi tự do là sự rơi của một vật chỉ dưới tác dụng của",
     ["lực cản của không khí.", "trọng lực.", "lực đẩy Ác-si-mét.", "lực ma sát."],
     "B", "Rơi tự do: chỉ chịu tác dụng của trọng lực."),
    (17, "Hiểu", "2.6",
     "Một vật rơi tự do từ độ cao 45 m. Lấy g = 10 m/s². Thời gian rơi của vật là",
     ["2 s.", "4,5 s.", "3 s.", "9 s."],
     "C", "t = √(2s/g) = √(90/10) = 3 s."),
    (18, "Hiểu", "2.6",
     "Hai vật có khối lượng khác nhau được thả rơi tự do từ cùng một độ cao (bỏ qua lực cản của không khí). "
     "Kết luận nào sau đây <b>đúng</b>?",
     ["Vật nặng chạm đất trước.", "Vật nhẹ chạm đất trước.",
      "Không thể so sánh được nếu không biết khối lượng.", "Hai vật chạm đất cùng lúc."],
     "D", "Rơi tự do có cùng gia tốc g, không phụ thuộc khối lượng."),
]

TF = [
    (1, "Tốc độ và vận tốc; Đồ thị d – t", [
        ("Tốc độ trung bình là đại lượng vectơ.", False,
         "Tốc độ trung bình là đại lượng vô hướng; chỉ vận tốc mới là vectơ."),
        ("Vận tốc trung bình được xác định bằng thương số giữa độ dịch chuyển và khoảng thời gian chuyển động.", True,
         "v<sub>tb</sub> = Δd/Δt."),
        ("Trên đồ thị độ dịch chuyển – thời gian của chuyển động thẳng đều, đường biểu diễn càng dốc thì vật chuyển động càng nhanh.", True,
         "Độ dốc càng lớn → |v| càng lớn."),
        ("Trên đồ thị độ dịch chuyển – thời gian, một đoạn thẳng nằm ngang ứng với vật đang chuyển động thẳng đều.", False,
         "Đoạn nằm ngang có độ dốc 0 → vật đứng yên."),
    ]),
    (2, "Chuyển động thẳng biến đổi đều", [
        ("Chuyển động thẳng biến đổi đều có gia tốc không đổi.", True,
         "Đó chính là định nghĩa của chuyển động thẳng biến đổi đều."),
        ("Trong chuyển động thẳng nhanh dần đều, vectơ gia tốc cùng chiều với vectơ vận tốc.", True,
         "Cùng chiều → tốc độ tăng đều."),
        ("Một ô tô đang chạy với vận tốc 10 m/s thì hãm phanh và dừng lại sau 5 s. Gia tốc của ô tô là 2 m/s².", False,
         "a = (0 − 10)/5 = −2 m/s² (ngược chiều dương)."),
        ("Trong chuyển động thẳng nhanh dần đều không vận tốc đầu, quãng đường đi được trong những khoảng thời gian bằng nhau liên tiếp tăng dần đều.", True,
         "Các quãng đường liên tiếp tỉ lệ 1 : 3 : 5 : 7… → tăng đều một lượng a·Δt²."),
    ]),
]


# --------------------------------------------------------------------------- #
def _exam_header():
    f = []
    f.append(P("PHẦN D · ĐỀ THI MÔ PHỎNG GIỮA KÌ I", "h1"))
    f.append(P(
        "<b>MÔN: VẬT LÍ 10</b> – Thời gian làm bài: <b>50 phút</b> (không kể thời gian phát đề) – "
        "Cấu trúc: 18 câu trắc nghiệm + 2 câu đúng/sai + 2 câu tự luận ngắn + 3 ý tự luận vận dụng.", "body"))
    f.append(P(
        "Đề dưới đây được biên soạn <b>đúng theo ma trận và bản đặc tả</b> của đề kiểm tra giữa kì I: đủ 18 câu "
        "phần I (10 Biết + 8 Hiểu), 2 câu phần II (mỗi câu 4 ý), 2 câu phần III và 3 ý phần IV, phân bổ theo "
        "từng đơn vị kiến thức như bảng A2. Hãy <b>bấm đồng hồ 50 phút</b> và làm nghiêm túc như thi thật.", "body"))
    f.append(SPC(3))
    return f


def exam_part():
    f = _exam_header()

    f.append(P("PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (18 câu)", "h2"))
    f.append(P("<i>Thí sinh trả lời từ câu 1 đến câu 18. Mỗi câu chỉ chọn một phương án.</i>", "small"))
    f.append(SPC(2))
    for num, level, lesson, stem, opts, ans, _ in MCQ:
        f += question(num, stem, opts, cols=2)

    f.append(SPC(4))
    f.append(P("PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu, mỗi câu 4 ý)", "h2"))
    f.append(P("<i>Trong mỗi ý a), b), c), d), thí sinh chọn Đúng hoặc Sai.</i>", "small"))
    from reportlab.platypus import KeepTogether
    for num, topic, items in TF:
        block = [SPC(3), P(f"<b>Câu {num}.</b> Xét các phát biểu sau về <b>{topic.lower()}</b>:", "q")]
        for i, (text, _, _) in enumerate(items):
            block.append(P(f"<b>{'abcd'[i]})</b> {text}", "opt"))
        f.append(KeepTogether(block))

    f.append(SPC(4))
    f.append(KeepTogether([
        P("PHẦN III. TỰ LUẬN NGẮN (2 câu)", "h2"),
        P("<b>Câu 1.</b> Phân biệt tốc độ và vận tốc về: khái niệm, công thức, tính chất vectơ/vô hướng và đơn vị. "
          "Viết công thức tính tốc độ trung bình và vận tốc trung bình.", "q"),
        P("<b>Câu 2.</b> Cùng một tờ giấy, khi để phẳng thì rơi chậm, khi vo tròn lại thì rơi nhanh hơn. "
          "Giải thích hiện tượng. Khi nào chuyển động rơi của một vật được coi là rơi tự do?", "q"),
    ]))

    f.append(SPC(4))
    f.append(P("PHẦN IV. TỰ LUẬN VẬN DỤNG (3 ý)", "h2"))
    f.append(KeepTogether([
        P("<b>Câu 2 (1,0 điểm).</b> Một xe máy đang chạy với vận tốc 36 km/h thì tăng tốc đều, sau 5 s đạt 54 km/h.", "q"),
        P("a) Tính gia tốc của xe.   b) Tính quãng đường xe đi được trong 5 s đó.", "opt"),
        P("c) Sau bao lâu kể từ lúc bắt đầu tăng tốc thì xe đạt 72 km/h và khi đó xe đã đi được bao xa?", "opt"),
        Spacer(1, 4),
    ]))
    f.append(KeepTogether([
        P("<b>Câu 3 (1,0 điểm).</b> Một ô tô đang chạy với vận tốc 20 m/s thì tài xế hãm phanh cho xe chuyển động "
          "chậm dần đều, xe dừng lại sau khi đi thêm được 40 m.", "q"),
        P("a) Tính gia tốc của ô tô.   b) Tính thời gian hãm phanh.", "opt"),
        P("c) Tính quãng đường ô tô đi được trong giây cuối cùng trước khi dừng.", "opt"),
        Spacer(1, 4),
    ]))

    f.append(KeepTogether([
        P("<b>Câu 1 (1,0 điểm).</b> Một ca nô chạy với tốc độ 8 m/s so với mặt nước, nước chảy với tốc độ 6 m/s "
          "so với bờ. Tính tốc độ của ca nô so với bờ khi ca nô:", "q"),
        P("a) chạy xuôi dòng;   b) chạy ngược dòng;   c) chạy vuông góc với dòng nước.", "opt"),
        Spacer(1, 5),
    ]))

    f.append(SPC(6))
    f.append(rule(color=None) if False else rule())
    f.append(P("— HẾT —", "body_c"))
    f.append(SPC(6))
    return f


# --------------------------------------------------------------------------- #
def answer_key():
    f = []
    f.append(P("D1. ĐÁP ÁN NHANH", "h2"))
    rows = []
    for i in range(0, 18, 6):
        chunk = MCQ[i : i + 6]
        rows.append([f"Câu {n}" for n, *_ in chunk])
        rows.append([f"<b>{a}</b>" for _, _, _, _, _, a, _ in chunk])
    t = data_table(["", "", "", "", "", ""], rows, [CONTENT_W / 6] * 6,
                   align=["CENTER"] * 6, head_bg=None)
    # rebuild without header row
    from reportlab.platypus import Table, TableStyle
    from .style import BG_SOFT, FONT_B, INK, LINE as LN, PRIMARY
    data = [[P(c, "tbl_c") for c in r] for r in rows]
    t = Table(data, colWidths=[CONTENT_W / 6] * 6, hAlign="LEFT")
    cmds = [("GRID", (0, 0), (-1, -1), 0.5, LN), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for r in range(0, len(data), 2):
        cmds.append(("BACKGROUND", (0, r), (-1, r), BG_SOFT))
    t.setStyle(TableStyle(cmds))
    f.append(t)
    f.append(SPC(4))

    f.append(P("<b>Phần II.</b> Câu 1: a) <b>Sai</b> – b) <b>Đúng</b> – c) <b>Đúng</b> – d) <b>Sai</b>. &nbsp;&nbsp; "
               "Câu 2: a) <b>Đúng</b> – b) <b>Đúng</b> – c) <b>Sai</b> – d) <b>Đúng</b>.", "body"))
    f.append(SPC(2))
    return f


def solutions():
    f = []
    f.append(P("D2. LỜI GIẢI CHI TIẾT PHẦN I", "h2"))
    for num, level, lesson, stem, opts, ans, why in MCQ:
        idx = "ABCD".index(ans)
        f.append(P(f"<b>Câu {num} – {ans}.</b> <font color='#5A6B7B'>({lesson} · {level})</font> {why}", "sol"))

    f.append(SPC(4))
    f.append(P("D3. LỜI GIẢI CHI TIẾT PHẦN II", "h2"))
    for num, topic, items in TF:
        f.append(P(f"<b>Câu {num}.</b>", "sol"))
        for i, (text, val, why) in enumerate(items):
            mark = "<font color='#1D6B4C'><b>ĐÚNG</b></font>" if val else "<font color='#A8332A'><b>SAI</b></font>"
            f.append(P(f"<b>{'abcd'[i]})</b> {mark} – {why}", "sol"))

    f.append(SPC(4))
    f.append(P("D4. LỜI GIẢI PHẦN III", "h2"))
    f.append(P("<b>Câu 1.</b>", "sol"))
    f.append(data_table(
        ["Tiêu chí", "Tốc độ", "Vận tốc"],
        [
            ["Khái niệm", "Mức độ nhanh, chậm của chuyển động trên quãng đường đã đi",
             "Sự thay đổi vị trí của vật theo thời gian (có hướng)"],
            ["Công thức", "v = s/Δt (s: quãng đường)", "v = Δd/Δt (Δd: độ dịch chuyển)"],
            ["Loại đại lượng", "Vô hướng", "Vectơ"],
            ["Đơn vị", "m/s (hoặc km/h)", "m/s (hoặc km/h)"],
        ],
        [80, 216, 215], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(P("Hệ quả: tốc độ trung bình luôn <b>lớn hơn hoặc bằng</b> độ lớn vận tốc trung bình; "
               "hai giá trị bằng nhau khi vật chuyển động thẳng, không đổi chiều.", "sol"))
    f.append(SPC(2))
    f.append(P("<b>Câu 2.</b>", "sol"))
    f.append(P("– Tờ giấy để phẳng có <b>diện tích tiếp xúc với không khí lớn</b> nên lực cản của không khí lớn, "
               "gần bằng hoặc đáng kể so với trọng lực → vật rơi chậm. Khi vo tròn, diện tích tiếp xúc giảm mạnh "
               "nên lực cản nhỏ → vật rơi nhanh hơn. Khối lượng tờ giấy không đổi, chỉ lực cản thay đổi.", "sol"))
    f.append(P("– Chuyển động rơi của vật được coi là <b>rơi tự do</b> khi lực cản của không khí <b>rất nhỏ</b> so với "
               "trọng lực (vật nặng, chắc; độ cao rơi không quá lớn; hình dạng khí động học). Khi đó vật rơi "
               "thẳng nhanh dần đều với gia tốc g, không phụ thuộc khối lượng.", "sol"))

    f.append(SPC(4))
    f.append(P("D5. LỜI GIẢI PHẦN IV", "h2"))
    f.append(P("<b>Câu 1.</b> Gọi (1) là ca nô, (2) là nước, (3) là bờ: v<sub>13</sub> = v<sub>12</sub> + v<sub>23</sub>, "
               "với v<sub>12</sub> = 8 m/s, v<sub>23</sub> = 6 m/s.", "sol"))
    f.append(P("a) Xuôi dòng (cùng chiều): v<sub>13</sub> = 8 + 6 = <b>14 m/s</b>.", "sol"))
    f.append(P("b) Ngược dòng (ngược chiều): v<sub>13</sub> = |8 − 6| = <b>2 m/s</b>.", "sol"))
    f.append(P("c) Vuông góc: v<sub>13</sub> = √(8² + 6²) = √100 = <b>10 m/s</b>.", "sol"))
    f.append(SPC(2))
    f.append(P("<b>Câu 2.</b> Đổi v<sub>0</sub> = 36 km/h = 10 m/s; v = 54 km/h = 15 m/s; 72 km/h = 20 m/s.", "sol"))
    f.append(P("a) Gia tốc: a = (v − v<sub>0</sub>)/Δt = (15 − 10)/5 = <b>1 m/s²</b>.", "sol"))
    f.append(P("b) Quãng đường: s = v<sub>0</sub>t + ½at² = 10·5 + ½·1·5² = 50 + 12,5 = <b>62,5 m</b>.", "sol"))
    f.append(P("c) Thời gian đạt 20 m/s: t = (20 − 10)/1 = <b>10 s</b>. Quãng đường khi đó: "
               "s = 10·10 + ½·1·10² = 100 + 50 = <b>150 m</b>.", "sol"))
    f.append(SPC(2))
    f.append(P("<b>Câu 3.</b> Chọn chiều dương là chiều chuyển động; v<sub>0</sub> = 20 m/s; khi dừng v = 0; s = 40 m.", "sol"))
    f.append(P("a) Từ v² − v<sub>0</sub>² = 2as: 0 − 20² = 2·a·40 → a = −400/80 = <b>−5 m/s²</b> "
               "(gia tốc ngược chiều chuyển động).", "sol"))
    f.append(P("b) Thời gian hãm: t = (v − v<sub>0</sub>)/a = (0 − 20)/(−5) = <b>4 s</b>.", "sol"))
    f.append(P("c) Quãng đường sau 3 s: s<sub>3</sub> = 20·3 + ½·(−5)·9 = 60 − 22,5 = 37,5 m. "
               "Quãng đường trong giây cuối: Δs = 40 − 37,5 = <b>2,5 m</b>.", "sol"))
    f.append(SPC(2))
    return f


def part_d():
    return exam_part() + answer_key() + solutions() + part_d2()


def part_d2():
    f0 = []
    """Bảng tự chấm điểm sau khi làm đề mô phỏng."""
    f = []
    f.append(P("D6. Bảng tự chấm & chẩn đoán sau khi làm đề", "h2"))
    f.append(P("Sau khi làm xong, hãy điền số câu đúng vào bảng dưới đây để biết mình đang mất điểm ở đâu.", "body"))
    f.append(data_table(
        ["Phần", "Số câu/ý", "Điểm mỗi đơn vị", "Điểm tối đa", "Điểm của em"],
        [
            ["I. Trắc nghiệm", "18 câu", "0,25 điểm/câu", "4,5", "………"],
            ["II. Đúng – sai", "2 câu (8 ý)", "theo số ý đúng (0,1 → 1,0)", "2,0", "………"],
            ["III. Tự luận ngắn", "2 câu", "0,25 điểm/câu", "0,5", "………"],
            ["IV. Tự luận vận dụng", "3 ý", "1,0 điểm/câu", "3,0", "………"],
            ["<b>Tổng</b>", "—", "—", "<b>10,0</b>", "………"],
        ],
        [116, 88, 148, 78, 81],
        align=["LEFT", "CENTER", "LEFT", "CENTER", "CENTER"], font="tbl_small",
    ))
    f.append(SPC(6))
    f.append(data_table(
        ["Nếu điểm của em…", "Nghĩa là…", "Việc cần làm ngay"],
        [
            ["< 5", "Hổng kiến thức nền ở nhiều bài", "Học lại Phần B từ Bài 3 → Bài 10, làm lại ví dụ mẫu"],
            ["5 – 6,5", "Nhớ định nghĩa nhưng chưa tính được", "Luyện 6 dạng bài ở C6, mỗi dạng 3 bài"],
            ["6,5 – 8", "Tính được nhưng còn sai dấu, đơn vị", "Làm lại đề, ghi riêng các lỗi sai; học F2"],
            ["8 – 9", "Khá tốt, còn lỗi cẩn thận", "Đọc kĩ đề, luyện phần đúng – sai và câu chữ “không/ngoại trừ”"],
            ["> 9", "Đã sẵn sàng", "Giữ nhịp: mỗi ngày 15 phút ôn công thức + 10 câu trắc nghiệm"],
        ],
        [86, 190, 235], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(10))
    f.append(box("Cách chữa đề hiệu quả nhất (quan trọng hơn làm nhiều đề)", [
        P("Với <b>mỗi câu sai</b>, ghi vào 3 cột: (1) lỗi là gì, (2) nguyên nhân (không biết / nhớ nhầm / tính sai / đọc sai đề), "
          "(3) cách tránh.", "box_item"),
        P("Sau 3 ngày, làm lại <b>đúng những câu đã sai</b>. Nếu vẫn sai → đó là lỗ hổng thật, phải học lại bài.", "box_item"),
        P("Chỉ khi tái làm đúng 100% câu từng sai, em mới chuyển sang đề mới.", "box_item"),
    ], "note"))
    f.append(SPC(6))

    f.append(P("D7. Nhật ký lỗi sai của em (in ra và điền tay)", "h2"))
    f.append(P("Đây là phần quan trọng nhất của cả tài liệu: mỗi dòng điền đúng là một điểm được cứu trong bài thi thật.", "body"))
    rows = [[f"<b>{i}</b>", "", "", "", ""] for i in range(1, 11)]
    t = data_table(
        ["#", "Câu / bài", "Em đã làm sai thế nào", "Nguyên nhân", "Cách sửa (1 dòng)"],
        rows, [24, 74, 150, 110, 153], align=["CENTER", "LEFT", "LEFT", "LEFT", "LEFT"],
        font="tbl_small", pad=7.5,
    )
    f.append(t)
    return f
