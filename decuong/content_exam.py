# -*- coding: utf-8 -*-
"""PHẦN 3 – Đề ôn tập mô phỏng + đáp án & lời giải chi tiết."""
from style import *


def story():
    s = []
    s.append(H1("PHẦN 3 · ĐỀ ÔN TẬP MÔ PHỎNG SÁT MA TRẬN"))
    s.append(P("Đề dưới đây được thiết kế <b>khớp 100% với ma trận</b>: 18 câu trắc nghiệm "
               "(10 Biết + 8 Hiểu), 2 câu đúng/sai × 4 ý (6 Biết + 2 Hiểu), 2 câu tự luận ngắn "
               "(1 Biết + 1 Hiểu) và 1 bài toán tự luận (1 ý Hiểu + 2 ý Vận dụng). "
               "Hãy bấm đồng hồ <b>50 phút</b> và làm nghiêm túc như thi thật.", "lead"))

    # ------------------------------------------------------------- header đề
    head = Table([
        [Paragraph("<b>ĐỀ KIỂM TRA GIỮA HỌC KÌ I – NĂM HỌC 2026 – 2027</b><br/>"
                   "<b>MÔN: VẬT LÍ – LỚP 10</b>", st("eh", fontName="DJSans-Bold", fontSize=11,
                                                     leading=15, alignment=TA_CENTER, textColor=WHITE)),
         Paragraph("<b>Thời gian: 50 phút</b><br/>(không kể thời gian phát đề)<br/>"
                   "70% trắc nghiệm – 30% tự luận",
                   st("eh2", fontSize=8.4, leading=11.5, alignment=TA_CENTER, textColor=WHITE))],
    ], colWidths=[CONTENT_W * 0.66, CONTENT_W * 0.34])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEAFTER", (0, 0), (0, 0), 0.6, WHITE),
    ]))
    s.append(SP(4)); s.append(head); s.append(SP(8))

    # ------------------------------------------------------------- PHẦN I
    s.append(H2(toc=False, text="PHẦN I. TRẮC NGHIỆM (18 câu)"))
    s.append(P("Chọn một phương án đúng nhất cho mỗi câu.", "small"))
    s.append(SP(2))

    Q = []
    Q.append(("1", "Đối tượng nghiên cứu chủ yếu của Vật lí là",
              ["các dạng vận động của vật chất (chất, trường) và năng lượng.",
               "sự hình thành và phát triển của các tầng lớp trong xã hội.",
               "cấu tạo và hoạt động của các tế bào sống.",
               "sự phát triển của các ngành kinh tế – tài chính."]))
    Q.append(("2", "Khi sử dụng thiết bị điện trong phòng thực hành, việc làm nào sau đây là <b>đúng</b>?",
              ["Cắm phích điện vào ổ khi công tắc nguồn đang bật.",
               "Tắt công tắc nguồn thiết bị trước khi cắm hoặc tháo thiết bị điện.",
               "Dùng tay ướt để rút phích cắm cho nhanh.",
               "Để cốc nước cạnh ổ điện cho tiện sử dụng."]))
    Q.append(("3", "Biển báo có đặc điểm “hình tam giác đều, viền đen hoặc viền đỏ, nền vàng” thuộc nhóm",
              ["biển chỉ dẫn.", "biển báo cấm.",
               "biển cảnh báo nguy hiểm.", "biển bắt buộc thực hiện."]))
    Q.append(("4", "Phép đo nào sau đây là phép đo <b>gián tiếp</b>?",
              ["Dùng thước đo chiều dài mặt bàn học.",
               "Dùng cân đo khối lượng một quả cân.",
               "Đo quãng đường và thời gian rồi tính tốc độ của một xe chuyển động.",
               "Dùng nhiệt kế đo nhiệt độ của cốc nước."]))
    Q.append(("5", "Độ dịch chuyển của một vật là",
              ["đại lượng vô hướng, bằng tổng độ dài đường đi của vật.",
               "đại lượng vectơ, có gốc tại vị trí đầu và ngọn tại vị trí cuối của vật.",
               "quãng đường vật đi được trong một đơn vị thời gian.",
               "đại lượng luôn có giá trị bằng quãng đường đi được."]))
    Q.append(("6", "Một người đi 3 km về phía đông rồi 4 km về phía bắc. Quãng đường và độ lớn độ dịch "
              "chuyển của người đó lần lượt là",
              ["7 km và 5 km.", "5 km và 7 km.", "7 km và 1 km.", "7 km và 7 km."]))
    Q.append(("7", "Một người đi bộ từ A đến B cách A 100 m rồi quay trở lại A. Quãng đường đi được và "
              "độ dịch chuyển của người đó là",
              ["100 m và 100 m.", "0 và 200 m.", "200 m và 0.", "200 m và 200 m."]))
    Q.append(("8", "Công thức tính <b>tốc độ trung bình</b> của một vật chuyển động là",
              ["v = Δd/Δt (đại lượng vectơ).", "v = s/Δt.",
               "v = a·t.", "v = g·t."]))
    Q.append(("9", "Trên đồ thị độ dịch chuyển – thời gian, vật <b>đứng yên</b> được biểu diễn bằng",
              ["đường thẳng nằm ngang, song song với trục Ot.",
               "đường thẳng dốc lên.",
               "đường thẳng dốc xuống.",
               "đường cong đi qua gốc toạ độ."]))
    Q.append(("10", "Đồ thị độ dịch chuyển – thời gian của một vật là đường thẳng đi qua gốc toạ độ và "
               "điểm có toạ độ (4 s; 8 m). Tốc độ của vật là",
               ["0,5 m/s.", "2 m/s.", "4 m/s.", "8 m/s."]))
    Q.append(("11", "Đơn vị của gia tốc là",
               ["m/s.", "m/s².", "m·s.", "m²/s."]))
    Q.append(("12", "Một ô tô đang chuyển động với vận tốc 10 m/s thì tăng tốc đều, sau 4 s đạt vận tốc "
               "18 m/s. Gia tốc của ô tô là",
               ["2 m/s².", "4 m/s².", "7 m/s².", "0,5 m/s²."]))
    Q.append(("13", "Chuyển động thẳng biến đổi đều là chuyển động có",
               ["vận tốc không đổi theo thời gian.",
                "gia tốc không đổi theo thời gian.",
                "gia tốc tăng đều theo thời gian.",
                "quỹ đạo là đường cong và vận tốc tăng đều."]))
    Q.append(("14", "Công thức nào sau đây là công thức tính <b>quãng đường</b> của chuyển động thẳng "
               "biến đổi đều?",
               ["s = v·t.", "s = v₀t + ½at².", "s = v₀ + at.", "v² − v₀² = 2as."]))
    Q.append(("15", "Một vật chuyển động thẳng nhanh dần đều với vận tốc ban đầu 5 m/s và gia tốc "
               "2 m/s². Vận tốc của vật sau 3 s là",
               ["6 m/s.", "11 m/s.", "21 m/s.", "15 m/s."]))
    Q.append(("16", "Đặc điểm nào sau đây <b>đúng</b> với sự rơi tự do?",
               ["Vật rơi chậm dần đều.",
                "Vật rơi với vận tốc không đổi.",
                "Vật rơi nhanh dần đều với gia tốc g.",
                "Vật rơi theo quỹ đạo cong tuỳ khối lượng."]))
    Q.append(("17", "Một vật rơi tự do từ độ cao 20 m. Lấy g = 10 m/s². Thời gian rơi của vật là",
               ["1 s.", "2 s.", "3 s.", "4 s."]))
    Q.append(("18", "Một vật rơi tự do từ độ cao h, sau 2 s thì chạm đất. Lấy g = 10 m/s². Độ cao h là",
               ["10 m.", "20 m.", "40 m.", "5 m."]))
    for num, txt, opts in Q:
        s.extend(question(num, txt, opts))

    # ------------------------------------------------------------- PHẦN II
    s.append(SP(10))
    s.append(H2(toc=False, text="PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu, mỗi câu 4 ý)"))
    s.append(P("Với mỗi ý a), b), c), d), hãy ghi <b>Đ</b> nếu phát biểu đúng, ghi <b>S</b> nếu phát biểu sai.",
               "small"))
    s.append(SP(3))

    s.append(P("<b>Câu 1.</b> Cho một vật chuyển động trên một đường thẳng và đồ thị độ dịch chuyển – "
               "thời gian của nó. Xét các phát biểu:"))
    s.extend(BULL([
        "<b>a)</b> Tốc độ trung bình là đại lượng vô hướng, được tính bằng quãng đường đi được chia cho "
        "thời gian chuyển động.",
        "<b>b)</b> Vận tốc trung bình của vật luôn có độ lớn bằng tốc độ trung bình của nó.",
        "<b>c)</b> Trên đồ thị độ dịch chuyển – thời gian, độ dốc của đường biểu diễn cho biết vận tốc "
        "của vật.",
        "<b>d)</b> Đồ thị độ dịch chuyển – thời gian của vật chuyển động thẳng đều là một đường cong.",
    ], style="num", bullet="+"))
    s.append(SP(6))

    s.append(P("<b>Câu 2.</b> Một vật chuyển động thẳng biến đổi đều. Xét các phát biểu:"))
    s.extend(BULL([
        "<b>a)</b> Trong chuyển động thẳng nhanh dần đều, vectơ gia tốc cùng chiều với vectơ vận tốc.",
        "<b>b)</b> Công thức v = v₀ + a·t dùng được cho cả chuyển động nhanh dần đều và chậm dần đều, "
        "với quy ước dấu phù hợp.",
        "<b>c)</b> Nếu chọn chiều dương là chiều chuyển động ban đầu thì vật chuyển động chậm dần đều có "
        "gia tốc a &lt; 0.",
        "<b>d)</b> Một vật có gia tốc a = −2 m/s² và vận tốc v = −5 m/s đang chuyển động chậm dần đều.",
    ], style="num", bullet="+"))

    # ------------------------------------------------------------- PHẦN III
    s.append(SP(8))
    s.append(H2(toc=False, text="PHẦN III. TỰ LUẬN NGẮN (2 câu)"))
    s.append(P("<b>Câu 1 (2,0 điểm).</b> Nêu định nghĩa vận tốc và viết công thức cộng vận tốc. "
               "Cho biết tên gọi của từng vận tốc trong công thức và cách tính độ lớn trong hai trường hợp: "
               "hai vận tốc cùng phương cùng chiều, hai vận tốc vuông góc."))
    s.append(P("<b>Câu 2 (1,0 điểm).</b> Vì sao trong không khí, hòn sỏi và chiếc lá thả cùng lúc từ cùng "
               "một độ cao lại rơi khác nhau, còn trong chân không thì rơi như nhau? Khi nào ta coi "
               "chuyển động rơi của một vật là rơi tự do?"))

    # ------------------------------------------------------------- PHẦN IV
    s.append(SP(8))
    s.append(H2(toc=False, text="PHẦN IV. BÀI TOÁN (3 ý)"))
    s.append(P("<b>Bài toán.</b> Một ô tô đang chạy trên một đường thẳng với vận tốc 36 km/h thì người "
               "lái xe tăng tốc. Ô tô chuyển động nhanh dần đều với gia tốc 2 m/s² trong 10 s. "
               "Sau đó người lái hãm phanh để ô tô chuyển động chậm dần đều và dừng lại sau khi đi thêm "
               "được 90 m."))
    s.extend(BULL([
        "<b>a)</b> Đổi 36 km/h ra m/s. Tính tốc độ trung bình của ô tô trong 10 s tăng tốc và so sánh "
        "với trung bình cộng của tốc độ đầu và tốc độ cuối trong 10 s đó.",
        "<b>b)</b> Tính vận tốc của ô tô sau 10 s và quãng đường ô tô đi được trong 10 s tăng tốc.",
        "<b>c)</b> Tính gia tốc của ô tô trong giai đoạn hãm phanh và thời gian từ lúc hãm phanh đến khi "
        "ô tô dừng hẳn.",
    ], style="num", bullet="+"))
    s.append(SP(3))
    s.append(P("<i>(Gợi ý trình bày: tóm tắt → chọn chiều dương → công thức chữ → thay số → kết quả có đơn vị.)</i>",
               "small"))

    # ============================================================ ĐÁP ÁN
    s.append(PageBreak())
    s.append(H1("PHẦN 3B · ĐÁP ÁN & LỜI GIẢI CHI TIẾT"))
    s.append(H2(toc=False, text="A. Đáp án nhanh"))
    s.append(table([
        ["Câu"] + [str(i) for i in range(1, 10)],
        ["Đáp án"] + ["A", "B", "C", "C", "B", "A", "C", "B", "A"],
        ["Câu"] + [str(i) for i in range(10, 19)],
        ["Đáp án"] + ["B", "B", "A", "B", "B", "B", "C", "B", "B"],
    ], [46] + [(CONTENT_W - 46) / 9] * 9, font=8.6, align=["c"] * 10, zebra=False))
    s.append(SP(5))
    s.append(table([
        ["Câu", "a", "b", "c", "d"],
        ["Câu 1", "Đ", "S", "Đ", "S"],
        ["Câu 2", "Đ", "Đ", "Đ", "S"],
    ], [80, 70, 70, 70, 70], font=8.8, align=["c"] * 5))
    s.append(SP(4))
    s.append(box("Nếu bạn sai từ 3 câu trở lên trong một nhóm (ví dụ nhóm bài 2.1 hoặc 2.5), hãy quay lại "
                 "đúng mục lý thuyết tương ứng ở Phần 1 trước khi làm lại đề.", "thi"))

    # ------------------------------------------------------------- giải I
    s.append(H2(toc=False, text="B. Lời giải chi tiết – Phần I"))
    sol = [
        ("1", "A", "Định nghĩa: Vật lí nghiên cứu các dạng vận động của vật chất và năng lượng. "
                  "Các phương án B, C, D thuộc khoa học xã hội, sinh học, kinh tế."),
        ("2", "B", "Quy tắc an toàn: <b>tắt công tắc nguồn trước khi cắm/tháo</b> thiết bị điện. "
                   "A, C, D đều là thao tác gây nguy cơ điện giật."),
        ("3", "C", "Tam giác đều – viền đen/đỏ – nền vàng là kí hiệu <b>cảnh báo nguy hiểm</b>. "
                   "Biển cấm: tròn viền đỏ; bắt buộc: tròn nền xanh; chỉ dẫn: vuông nền xanh."),
        ("4", "C", "Đo tốc độ qua công thức v = s/t là phép đo <b>gián tiếp</b> (phải đo s và t rồi tính). "
                   "A, B, D là phép đo trực tiếp."),
        ("5", "B", "Độ dịch chuyển là vectơ nối vị trí đầu với vị trí cuối; quãng đường mới là đại lượng "
                   "vô hướng bằng tổng độ dài đường đi."),
        ("6", "A", "s = 3 + 4 = <b>7 km</b>. Hai đoạn vuông góc nên d = √(3² + 4²) = <b>5 km</b>."),
        ("7", "C", "Đi 100 m rồi về 100 m: s = 200 m; vị trí cuối trùng vị trí đầu nên d = 0."),
        ("8", "B", "Tốc độ trung bình = quãng đường/thời gian, là đại lượng vô hướng. "
                   "Công thức Δd/Δt là vận tốc trung bình (vectơ)."),
        ("9", "A", "Vật đứng yên thì độ dịch chuyển không đổi theo thời gian → đồ thị là đường nằm ngang."),
        ("10", "B", "v = Δx/Δt = (8 − 0)/(4 − 0) = <b>2 m/s</b>."),
        ("11", "B", "a = Δv/Δt → đơn vị (m/s)/s = <b>m/s²</b>."),
        ("12", "A", "a = (18 − 10)/4 = <b>2 m/s²</b>."),
        ("13", "B", "Chuyển động thẳng biến đổi đều có <b>gia tốc không đổi</b>; nhanh dần đều hay chậm dần "
                    "đều là hai trường hợp riêng."),
        ("14", "B", "s = v₀t + ½at². Phương án A là chuyển động đều, C là công thức vận tốc, "
                    "D là hệ thức liên hệ (không phải công thức quãng đường)."),
        ("15", "B", "v = v₀ + at = 5 + 2·3 = <b>11 m/s</b>."),
        ("16", "C", "Rơi tự do là chuyển động thẳng nhanh dần đều với gia tốc g, không phụ thuộc khối lượng."),
        ("17", "B", "t = √(2h/g) = √(2·20/10) = √4 = <b>2 s</b>."),
        ("18", "B", "h = ½gt² = ½·10·2² = <b>20 m</b>."),
    ]
    rows = [["Câu", "ĐA", "Lời giải"]]
    for num, ans, txt in sol:
        rows.append([num, "<b>%s</b>" % ans, txt])
    s.append(table(rows, [28, 26, CONTENT_W - 54], font=7.9, align=["c", "c", "l"]))
    s.append(SP(6))

    # ------------------------------------------------------------- giải II
    s.append(H2(toc=False, text="C. Lời giải chi tiết – Phần II"))
    s.append(table([
        ["Câu", "Ý", "Đ/S", "Giải thích"],
        ["1", "a", "<b>Đ</b>", "Tốc độ trung bình = s/Δt, là đại lượng vô hướng."],
        ["1", "b", "<b>S</b>", "Chỉ bằng nhau khi vật chuyển động thẳng và <b>không đổi chiều</b>. "
                                "Nếu đi rồi quay về, độ dịch chuyển bằng 0 nên vận tốc trung bình bằng 0, "
                                "còn tốc độ trung bình vẫn dương."],
        ["1", "c", "<b>Đ</b>", "v = Δx/Δt chính là độ dốc (hệ số góc) của đồ thị s–t."],
        ["1", "d", "<b>S</b>", "Chuyển động thẳng đều có v không đổi nên đồ thị s–t là <b>đường thẳng</b>, "
                                "không phải đường cong."],
        ["2", "a", "<b>Đ</b>", "Nhanh dần đều: a̅ cùng chiều v̅."],
        ["2", "b", "<b>Đ</b>", "Công thức v = v₀ + at là công thức vectơ viết dưới dạng đại số; "
                                "dấu của a và v₀ cho biết chiều, nên dùng được cho cả hai trường hợp."],
        ["2", "c", "<b>Đ</b>", "Khi chiều dương là chiều chuyển động ban đầu (v₀ &gt; 0) thì chậm dần đều "
                                "ứng với a trái dấu v₀, tức a &lt; 0."],
        ["2", "d", "<b>S</b>", "a = −2 và v = −5 <b>cùng dấu âm</b> → vận tốc có độ lớn tăng dần, "
                                "vật chuyển động <b>nhanh dần đều</b>, không phải chậm dần."],
    ], [30, 22, 28, CONTENT_W - 80], font=7.9, align=["c", "c", "c", "l"]))
    s.append(SP(6))

    # ------------------------------------------------------------- giải III
    s.append(H2(toc=False, text="D. Lời giải chi tiết – Phần III"))
    s.append(P("<b>Câu 1.</b>"))
    s.extend(BULL([
        "<b>Định nghĩa:</b> Vận tốc là đại lượng vectơ đặc trưng cho mức độ nhanh, chậm và hướng của "
        "chuyển động; vận tốc trung bình bằng độ dịch chuyển chia cho thời gian thực hiện độ dịch chuyển: "
        "v̅<sub>tb</sub> = Δd̅/Δt. Đơn vị: m/s.",
        "<b>Công thức cộng vận tốc:</b> v̅<sub>13</sub> = v̅<sub>12</sub> + v̅<sub>23</sub>, trong đó v₁₃ là <b>vận tốc tuyệt đối</b> "
        "(vật 1 so với hệ quy chiếu đứng yên 3), v₁₂ là <b>vận tốc tương đối</b> (vật 1 so với hệ quy chiếu "
        "chuyển động 2), v₂₃ là <b>vận tốc kéo theo</b> (hệ quy chiếu 2 so với 3).",
        "<b>Cùng phương, cùng chiều:</b> v₁₃ = v₁₂ + v₂₃.",
        "<b>Vuông góc:</b> v₁₃ = √(v₁₂² + v₂₃²).",
    ]))
    s.append(P("<b>Câu 2.</b>"))
    s.extend(BULL([
        "Trong <b>không khí</b>, ngoài trọng lực, mỗi vật còn chịu <b>lực cản của không khí</b>. Lực cản "
        "này phụ thuộc hình dạng, diện tích bề mặt và tốc độ của vật: chiếc lá có diện tích lớn, khối lượng "
        "nhỏ nên lực cản rất đáng kể so với trọng lượng, rơi chậm và lắc lư; hòn sỏi nhỏ, khối lượng riêng "
        "lớn nên lực cản không đáng kể, rơi nhanh.",
        "Trong <b>chân không</b> không có không khí nên <b>không có lực cản</b>; mọi vật chỉ chịu tác dụng "
        "của trọng lực và rơi với cùng gia tốc g, không phụ thuộc khối lượng.",
        "Ta coi chuyển động rơi của một vật là <b>rơi tự do</b> khi <b>bỏ qua được sức cản của không khí</b> "
        "(sức cản rất nhỏ so với trọng lượng), ví dụ hòn sỏi, chìa khoá rơi từ độ cao vài mét.",
    ]))
    s.append(SP(4))

    # ------------------------------------------------------------- giải IV
    s.append(H2(toc=False, text="E. Lời giải chi tiết – Phần IV"))
    s.append(P("<b>Tóm tắt:</b> v₀ = 36 km/h; a₁ = 2 m/s²; t₁ = 10 s; giai đoạn hãm: v₂ = 0 sau khi đi "
               "thêm s₂ = 90 m. Chọn chiều dương là chiều chuyển động."))
    s.append(P("<b>a)</b> 36 km/h = 36/3,6 = <b>10 m/s</b>.<br/>"
               "Sau 10 s: v = v₀ + a₁t₁ = 10 + 2·10 = 30 m/s.<br/>"
               "Quãng đường: s₁ = v₀t₁ + ½a₁t₁² = 10·10 + ½·2·10² = 100 + 100 = <b>200 m</b>.<br/>"
               "Tốc độ trung bình: v<sub>tb</sub> = s₁/t₁ = 200/10 = <b>20 m/s</b>.<br/>"
               "Trung bình cộng hai tốc độ đầu – cuối: (10 + 30)/2 = <b>20 m/s</b> → <b>bằng nhau</b>. "
               "Điều này đúng cho chuyển động có gia tốc không đổi, nhưng <b>không đúng</b> khi gia tốc "
               "thay đổi hoặc khi vật đổi chiều."))
    s.append(P("<b>b)</b> Vận tốc sau 10 s: <b>v = 30 m/s</b> (như trên). Quãng đường trong 10 s tăng tốc: "
               "<b>s₁ = 200 m</b>. Có thể kiểm tra bằng hệ thức: v² − v₀² = 30² − 10² = 800 = 2·2·200 (khớp)."))
    s.append(P("<b>c)</b> Giai đoạn hãm phanh: vận tốc đầu 30 m/s, vận tốc cuối 0, quãng đường 90 m.<br/>"
               "Áp dụng v² − v₀² = 2a₂s₂: 0 − 30² = 2·a₂·90 → a₂ = −900/180 = <b>−5 m/s²</b>.<br/>"
               "Gia tốc có độ lớn 5 m/s², ngược chiều chuyển động (chậm dần đều).<br/>"
               "Thời gian hãm: t₂ = (v − v₀)/a₂ = (0 − 30)/(−5) = <b>6 s</b>."))
    s.append(box("<b>Chốt đáp số:</b> a) 10 m/s; v<sub>tb</sub> = 20 m/s = trung bình cộng. "
                 "b) v = 30 m/s; s₁ = 200 m. c) a₂ = −5 m/s²; t₂ = 6 s.", "nho", "ĐÁP SỐ"))
    s.append(SP(5))

    s.append(H2(toc=False, text="F. Thang điểm gợi ý"))
    s.append(table([
        ["Phần", "Số ý", "Điểm mỗi ý", "Tổng", "Ghi chú chấm"],
        ["I – Trắc nghiệm", "18", "0,25", "4,5",
         "Chỉ chọn 1 phương án; tô 2 phương án không được điểm"],
        ["II – Đúng/Sai", "8", "0,25", "2,0", "Đúng mỗi ý 0,25 điểm"],
        ["III – Tự luận ngắn", "2", "2,0 + 1,0", "3,0", "Đúng định nghĩa + công thức: 1,0; lấy ví dụ/ý phụ: 1,0"],
        ["IV – Bài toán", "3", "0,75 + 1,0 + 1,25", "3,0",
         "Có công thức đúng: 0,25/ý; thay số và đơn vị đúng: phần còn lại"],
        ["<b>Tổng</b>", "", "", "<b>12,5</b>", "Quy đổi theo quy chế của trường"],
    ], [90, 40, 78, 46, CONTENT_W - 254], font=7.9, align=["l", "c", "c", "c", "l"]))
    s.append(SP(4))
    s.append(P("Bảng điểm trên chỉ mang tính tham khảo để bạn tự chấm và biết mình đang ở đâu; "
               "điểm chính thức do giáo viên quyết định theo hướng dẫn của nhà trường.", "small"))
    s.append(SP(10))

    s.append(H2(toc=False, text="G. Sổ ghi lỗi – điền sau mỗi lần làm đề"))
    s.append(P("Đây là phần quan trọng nhất của việc luyện đề. Mỗi câu sai, hãy ghi lại <b>lý do sai</b> "
               "(không thuộc bài / nhớ nhầm công thức / đọc sai đề / tính toán) và <b>mục cần học lại</b>. "
               "Sau 3 lần làm đề, bạn sẽ thấy lỗi của mình lặp lại ở đúng một vài chỗ – đó chính là "
               "những điểm cần dồn sức.", "body"))
    rows = [["Lần", "Câu sai", "Dạng lỗi", "Mục lý thuyết cần học lại", "Đã sửa chưa?"]]
    rows += [["1", "", "", "", "[   ]"] for _ in range(3)]
    rows += [["2", "", "", "", "[   ]"] for _ in range(3)]
    rows += [["3", "", "", "", "[   ]"] for _ in range(3)]
    s.append(table(rows, [36, 66, CONTENT_W * 0.26, CONTENT_W * 0.32, CONTENT_W - 36 - 66 - CONTENT_W * 0.58],
                   font=8.0, align=["c", "c", "l", "l", "c"], pad=8))
    s.append(SP(6))
    s.append(box("<b>Quy tắc chữa lỗi:</b> một câu sai phải được chữa theo 3 bước – "
                 "(1) đọc lại đúng mục lý thuyết; (2) tự giải lại <b>không nhìn đáp án</b>; "
                 "(3) sau 24 giờ làm lại câu đó. Chỉ khi làm đúng ở bước 3 mới coi là đã sửa.", "thi"))
    s.append(PageBreak())
    return s
