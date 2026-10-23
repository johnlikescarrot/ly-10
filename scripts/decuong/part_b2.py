# -*- coding: utf-8 -*-
"""Phần B – Lý thuyết trọng tâm (Bài 6 → Bài 10)."""
from __future__ import annotations

from .figures import fig_dt_graph, fig_dt_slope, fig_vt_graph, fig_vector_cases
from .style import P, S, SPC, bullets, box, data_table, formula, lesson_header, numbered


# =========================================================================== #
def bai6():
    f = []
    f += lesson_header("6", "Thực hành: Đo tốc độ của vật chuyển động",
                       "Có trong đặc tả – cần nắm để làm câu hỏi thực hành")

    f.append(P("<b>1. Bộ dụng cụ</b>", "h3"))
    f.append(P("Giá đỡ – máng (hoặc đường ray) nghiêng · xe trượt (hoặc viên bi) · <b>hai cổng quang điện</b> E, F · "
               "<b>đồng hồ đo thời gian hiện số</b> · thước đo độ dài.", "body"))

    f.append(P("<b>2. Nguyên tắc đo</b>", "h3"))
    f.append(P("Đo quãng đường s giữa hai cổng và thời gian Δt vật đi hết quãng đường đó, rồi tính:", "body"))
    f += formula("v = s / Δt", "đây là <b>tốc độ trung bình</b> trên đoạn đường giữa hai cổng quang điện")

    f.append(P("<b>3. Các chế độ (MODE) của đồng hồ hiện số</b>", "h3"))
    f.append(data_table(
        ["MODE", "Chức năng", "Dùng để đo"],
        [
            ["A", "Đo thời gian vật chắn cổng quang nối với ổ A", "Tốc độ <b>tức thời</b> tại cổng A"],
            ["B", "Đo thời gian vật chắn cổng quang nối với ổ B", "Tốc độ <b>tức thời</b> tại cổng B"],
            ["A + B", "Đo <b>tổng</b> hai khoảng thời gian vật chắn cổng A và cổng B", "Kiểm tra, so sánh"],
            ["A ↔ B", "Đo thời gian vật đi <b>từ cổng A đến cổng B</b>", "Tốc độ <b>trung bình</b> trên đoạn AB"],
        ],
        [56, 300, 155], align=["CENTER", "LEFT", "LEFT"],
    ))
    f.append(SPC(5))
    f.append(P("Muốn đo tốc độ tức thời tại cổng, dùng một <b>tấm chắn sáng</b> có bề rộng d và tính "
               "v ≈ d/Δt, với Δt là thời gian tấm chắn che cổng quang.", "body"))

    f.append(P("<b>4. Ưu điểm – Nhược điểm</b>", "h3"))
    f.append(data_table(
        ["Ưu điểm", "Nhược điểm"],
        [
            ["Đo được khoảng thời gian rất ngắn với độ chia 0,001 s – độ chính xác cao.",
             "Giá thành cao hơn đồng hồ bấm giây."],
            ["Tự động bật – tắt đồng hồ, loại bỏ sai số phản xạ của người đo.",
             "Cần nguồn điện, cần hiệu chỉnh trước khi đo."],
            ["Kết quả khách quan, lặp lại được.", "Dễ nhiễu do ánh sáng môi trường chiếu vào cảm biến."],
            ["Thao tác đơn giản sau khi lắp đặt.", "Chỉ đo được vật có kích thước phù hợp; vật trong suốt có thể không chắn được tia."],
        ],
        [255, 256], align=["LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(5))

    f.append(P("<b>5. Tiến trình thí nghiệm</b>", "h3"))
    f += numbered([
        "Lắp máng nghiêng, đặt hai cổng quang E, F cách nhau một khoảng s; nối cổng với đồng hồ.",
        "Chọn thang đo thời gian phù hợp (ví dụ 9,999 s – 0,001 s) và chọn <b>MODE A ↔ B</b>.",
        "Đặt xe tại điểm xuất phát, thả cho xe chuyển động qua hai cổng.",
        "Đọc thời gian Δt trên đồng hồ; dùng thước đo s (đo khoảng cách giữa hai cổng).",
        "Lặp lại 3 – 5 lần, ghi bảng số liệu, tính giá trị trung bình và sai số.",
    ])
    f.append(box("Lưu ý khi xử lí số liệu", [
        P("Tính tốc độ cho từng lần đo rồi lấy trung bình, hoặc tính tốc độ từ giá trị trung bình của s và Δt.", "box_item"),
        P("Khoảng cách s phải đo <b>đúng giữa hai cổng quang</b>; thời gian Δt phải là thời gian <b>đi từ A đến B</b>.", "box_item"),
        P("Nếu kết quả giữa các lần lệch nhiều → kiểm tra độ nghiêng của máng và ánh sáng môi trường.", "box_item"),
    ], "note"))
    return f


# =========================================================================== #
def bai7():
    f = []
    f += lesson_header("7", "Đồ thị độ dịch chuyển – thời gian",
                       "Ma trận: 1 câu Biết + 1 câu Hiểu + 2 ý Đúng/Sai")

    f.append(P("<b>1. Cách vẽ đồ thị</b>", "h3"))
    f.append(P("Trục hoành biểu diễn <b>thời gian t</b> (s), trục tung biểu diễn <b>độ dịch chuyển d</b> (m). "
               "Lập bảng giá trị (t; d) → xác định các điểm trên mặt phẳng toạ độ → nối các điểm. "
               "Với chuyển động <b>thẳng đều</b>, đồ thị là một <b>đường thẳng</b>.", "body"))
    f.append(SPC(2))
    f.append(fig_dt_graph())
    f.append(P("Ba trạng thái trên một đồ thị d – t: đi nhanh (dốc lên) – đứng yên (nằm ngang) – đi ngược chiều dương (dốc xuống)", "cap"))
    f.append(SPC(6))

    f.append(P("<b>2. Đọc đồ thị</b>", "h3"))
    f += bullets([
        "<b>Độ dốc</b> của đồ thị d – t bằng <b>vận tốc</b>: v = Δd/Δt = (d₂ − d₁)/(t₂ − t₁).",
        "Độ dốc <b>dương</b> → vật đi theo chiều dương; độ dốc <b>âm</b> → đi ngược chiều dương.",
        "Đường <b>nằm ngang</b> (độ dốc 0) → vật <b>đứng yên</b>.",
        "Độ dốc <b>càng lớn</b> → vật chuyển động <b>càng nhanh</b>.",
        "Tung độ tại thời điểm t cho biết <b>vị trí</b> của vật tại thời điểm đó.",
        "Độ dịch chuyển trong khoảng thời gian = <b>hiệu tung độ</b>; quãng đường = tổng các |Δd| của từng đoạn.",
    ])
    f.append(SPC(4))
    f.append(fig_dt_slope())
    f.append(P("Độ dốc = Δd/Δt chính là vận tốc của vật", "cap"))
    f.append(SPC(6))

    f.append(box("Ví dụ đọc đồ thị", [
        P("Một vật chuyển động thẳng có đồ thị d – t là đường thẳng qua gốc toạ độ, tại t = 4 s thì d = 20 m.", "box_item"),
        P("<b>Vận tốc:</b> v = Δd/Δt = (20 − 0)/(4 − 0) = <b>5 m/s</b>.", "box_item"),
        P("Tại t = 6 s: d = v·t = 5·6 = <b>30 m</b>; quãng đường trong 6 s đầu là <b>30 m</b>.", "box_item"),
        P("Nếu từ t = 4 s đến t = 8 s đồ thị nằm ngang → trong khoảng đó vật <b>dừng lại</b>.", "box_item"),
    ], "ex"))

    f.append(box("Mẹo nhớ", [
        P("<b>“Dốc nhiều – chạy nhanh; nằm ngang – đứng yên; dốc xuống – quay đầu”</b>.", "box_item"),
        P("Đồ thị d – t <b>không phải</b> là quỹ đạo của vật; nó chỉ mô tả vị trí theo thời gian.", "box_item"),
        P("Chuyển động thẳng đều → đường thẳng; chuyển động biến đổi đều → đường <b>cong (parabol)</b>.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("Nhầm <b>độ dốc</b> với <b>độ cao</b> của đồ thị → phải lấy Δd/Δt.", "box_item"),
        P("Cho rằng đường đi xuống là “đi chậm lại” → thực chất là <b>đi ngược chiều dương</b>.", "box_item"),
        P("Tính quãng đường bằng hiệu tung độ khi vật <b>đổi chiều</b> → phải cộng độ lớn từng đoạn.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai8():
    f = []
    f += lesson_header("8", "Chuyển động biến đổi. Gia tốc",
                       "Ma trận: 1 câu Biết + 1 câu Hiểu")

    f.append(P("<b>1. Chuyển động biến đổi</b>", "h3"))
    f.append(P("Là chuyển động có <b>vận tốc thay đổi</b> (thay đổi về độ lớn, về hướng hoặc cả hai) theo thời gian. "
               "Ví dụ: xe khởi hành, xe hãm phanh, vật rơi, ô tô vào cua.", "body"))

    f.append(P("<b>2. Gia tốc</b>", "h3"))
    f.append(P("Gia tốc là đại lượng <b>vectơ</b> đặc trưng cho <b>mức độ thay đổi nhanh hay chậm của vận tốc</b>:", "body"))
    f += formula("a = Δv / Δt = (v − v<sub>0</sub>) / (t − t<sub>0</sub>)", "đơn vị: m/s² (mét trên giây bình phương)")
    f.append(P("<b>Ý nghĩa:</b> a = 2 m/s² nghĩa là mỗi giây vận tốc thay đổi 2 m/s.", "body"))

    f.append(P("<b>3. Quan hệ về phương, chiều giữa gia tốc và vận tốc</b>", "h3"))
    f.append(data_table(
        ["Trường hợp", "Đặc điểm chuyển động", "Ví dụ"],
        [
            ["<b>a</b> cùng chiều với <b>v</b>", "Chuyển động <b>nhanh dần</b> (tốc độ tăng)", "Xe tăng tốc khi đạp ga"],
            ["<b>a</b> ngược chiều với <b>v</b>", "Chuyển động <b>chậm dần</b> (tốc độ giảm)", "Xe hãm phanh"],
            ["a = 0", "Chuyển động <b>thẳng đều</b> (v không đổi)", "Xe chạy đều trên đường thẳng"],
        ],
        [130, 200, 181], align=["LEFT", "LEFT", "LEFT"],
    ))
    f.append(SPC(5))

    f.append(box("Ví dụ mẫu", [
        P("Một ô tô đang chạy với vận tốc 10 m/s thì tăng tốc, sau 5 s đạt 20 m/s.", "box_item"),
        P("Độ biến thiên vận tốc: Δv = 20 − 10 = 10 m/s.", "box_item"),
        P("Gia tốc: a = Δv/Δt = 10/5 = <b>2 m/s²</b> (cùng chiều chuyển động nên xe <b>nhanh dần</b>).", "box_item"),
        P("Nếu xe hãm phanh từ 20 m/s xuống 0 trong 4 s: a = (0 − 20)/4 = <b>−5 m/s²</b> "
          "(ngược chiều dương → <b>chậm dần</b>).", "box_item"),
    ], "ex"))

    f.append(box("Mẹo nhớ dấu của gia tốc", [
        P("<b>“Cùng chiều thì nhanh, ngược chiều thì chậm”</b> – chỉ cần so hướng, không cần so độ lớn.", "box_item"),
        P("a âm <b>không</b> có nghĩa là chậm: phải xét dấu của a so với v. Nếu v cũng âm thì a âm là <b>nhanh dần</b>.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("“Gia tốc là vận tốc” → <b>Sai</b>: gia tốc là <i>tốc độ thay đổi</i> của vận tốc.", "box_item"),
        P("“a âm thì vật luôn chuyển động chậm dần” → <b>Sai</b>, phải so sánh dấu với v.", "box_item"),
        P("Đơn vị m/s² không phải m/s.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai9():
    f = []
    f += lesson_header("9", "Chuyển động thẳng biến đổi đều",
                       "Ma trận: 2 câu Biết + 1 câu Hiểu + 4 ý Đúng/Sai + 2 câu Vận dụng (P.IV)")

    f.append(P("<b>1. Định nghĩa</b>", "h3"))
    f.append(P("Chuyển động thẳng biến đổi đều là chuyển động có <b>quỹ đạo là đường thẳng</b> và <b>gia tốc không đổi</b> "
               "(vận tốc tăng hoặc giảm đều theo thời gian).", "body"))
    f += bullets([
        "<b>Nhanh dần đều</b>: a cùng chiều với v, tốc độ tăng đều.",
        "<b>Chậm dần đều</b>: a ngược chiều với v, tốc độ giảm đều.",
    ])

    f.append(P("<b>2. Hệ thống công thức</b>", "h3"))
    f += formula("v = v<sub>0</sub> + a·t")
    f += formula("s = v<sub>0</sub>·t + ½·a·t²")
    f += formula("v² − v<sub>0</sub>² = 2·a·s")
    f += formula("x = x<sub>0</sub> + v<sub>0</sub>·t + ½·a·t²", "phương trình toạ độ (chuyển động thẳng biến đổi đều)")
    f.append(P("<b>Chú ý:</b> các công thức trên viết cho chiều dương đã chọn; a và v<sub>0</sub> mang dấu đại số. "
               "Nếu vật <b>không đổi chiều</b> thì quãng đường s = |Δx|.", "body"))

    f.append(P("<b>3. Các trường hợp đặc biệt cần nhớ</b>", "h3"))
    f.append(data_table(
        ["Trường hợp", "Công thức rút gọn"],
        [
            ["Xuất phát từ trạng thái đứng yên (v<sub>0</sub> = 0)", "v = a·t ; s = ½a·t² ; v² = 2a·s"],
            ["Vật chuyển động chậm dần rồi <b>dừng lại</b> (v = 0)", "Thời gian dừng: t = v<sub>0</sub>/|a| ; Quãng đường: s = v<sub>0</sub>²/(2|a|)"],
            ["Quãng đường đi trong <b>giây thứ n</b>", "Δs = v<sub>0</sub> + a·(n − 0,5)  (với v<sub>0</sub> = 0: Δs = a(n − 0,5))"],
            ["Quãng đường trong n giây và trong (n − 1) giây", "Δs = s(n) − s(n − 1)"],
        ],
        [200, 311], align=["LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(5))

    f.append(P("<b>4. Đồ thị vận tốc – thời gian (v – t)</b>", "h3"))
    f.append(fig_vt_graph())
    f.append(P("Đồ thị v – t là đường thẳng: độ dốc = gia tốc; diện tích dưới đồ thị = độ dịch chuyển", "cap"))
    f.append(SPC(5))
    f.append(P("Trên đồ thị v – t: <b>độ dốc</b> cho gia tốc, <b>diện tích</b> hình giới hạn bởi đồ thị và trục thời gian "
               "cho độ dịch chuyển (quãng đường nếu không đổi chiều).", "body"))

    f.append(box("Quy trình 4 bước giải bài toán", [
        P("<b>Bước 1.</b> Chọn chiều dương (thường là chiều chuyển động), chọn gốc thời gian lúc bắt đầu khảo sát.", "box_item"),
        P("<b>Bước 2.</b> Tóm tắt, <b>đổi đơn vị</b> về m/s, m, s; xác định dấu của v<sub>0</sub>, a.", "box_item"),
        P("<b>Bước 3.</b> Chọn công thức phù hợp: thiếu đại lượng nào tránh dùng công thức chứa đại lượng đó.", "box_item"),
        P("<b>Bước 4.</b> Thay số, kiểm tra dấu và đơn vị; kết luận bằng câu trả lời có nghĩa vật lí.", "box_item"),
    ], "def"))

    f.append(P("<b>5. Hai bài toán mẫu điển hình</b>", "h3"))
    f.append(box("Mẫu 1 – Tăng tốc", [
        P("Xe máy đang chạy 36 km/h thì tăng tốc đều, sau 5 s đạt 54 km/h. Tính gia tốc và quãng đường trong 5 s.", "box_item"),
        P("Đổi: v<sub>0</sub> = 10 m/s; v = 15 m/s.", "box_item"),
        P("a = (v − v<sub>0</sub>)/t = (15 − 10)/5 = <b>1 m/s²</b>.", "box_item"),
        P("s = v<sub>0</sub>t + ½at² = 10·5 + ½·1·25 = <b>62,5 m</b>.", "box_item"),
    ], "ex"))
    f.append(box("Mẫu 2 – Hãm phanh (chậm dần đều)", [
        P("Ô tô đang chạy 20 m/s thì hãm phanh, dừng lại sau khi đi thêm 40 m. Tính gia tốc và thời gian hãm.", "box_item"),
        P("Áp dụng v² − v<sub>0</sub>² = 2as: 0 − 20² = 2·a·40 → a = <b>−5 m/s²</b>.", "box_item"),
        P("Thời gian: t = (v − v<sub>0</sub>)/a = (0 − 20)/(−5) = <b>4 s</b>.", "box_item"),
        P("Quãng đường trong giây cuối: s(4) − s(3) = 40 − (20·3 − ½·5·9) = 40 − 37,5 = <b>2,5 m</b>.", "box_item"),
    ], "ex"))

    f.append(box("Mẹo nhớ", [
        P("<b>“Vận tốc – Quãng đường – Liên hệ”</b>: v = v₀ + at · s = v₀t + ½at² · v² − v₀² = 2as.", "box_item"),
        P("Bài nào <b>không cho thời gian</b> → dùng công thức liên hệ v² − v₀² = 2as.", "box_item"),
        P("Bài nào <b>không cho gia tốc</b> → dùng s = (v₀ + v)·t/2 (trung bình cộng vận tốc).", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("Quên đổi km/h → m/s (chia 3,6).", "box_item"),
        P("Thay số a âm vào s = v₀t + ½at² mà quên dấu → ra quãng đường sai.", "box_item"),
        P("Dùng công thức v = v₀ + at cho vật <b>đã dừng</b> rồi tiếp tục → vật không chuyển động ngược lại.", "box_item"),
        P("Nhầm “giây thứ n” với “n giây”: giây thứ n là khoảng từ t = n − 1 đến t = n.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai10():
    f = []
    f += lesson_header("10", "Sự rơi tự do",
                       "Ma trận: 1 câu Biết + 2 câu Hiểu + 1 câu Hiểu (P.III)")

    f.append(P("<b>1. Định nghĩa và đặc điểm</b>", "h3"))
    f.append(P("Sự rơi tự do là sự rơi của một vật <b>chỉ dưới tác dụng của trọng lực</b>.", "body"))
    f += bullets([
        "Phương: <b>thẳng đứng</b>; chiều: <b>từ trên xuống</b>.",
        "Chuyển động: <b>thẳng nhanh dần đều</b> với gia tốc rơi tự do <b>g</b>.",
        "Tại một nơi trên Trái Đất, g có giá trị như nhau cho mọi vật: thường lấy <b>g ≈ 9,8 m/s²</b> (nhiều bài lấy 10 m/s²).",
        "Trong chân không, mọi vật rơi nhanh như nhau, <b>không phụ thuộc khối lượng</b>.",
    ])

    f.append(P("<b>2. Công thức</b> (chọn chiều dương hướng xuống, v<sub>0</sub> = 0, a = g)", "h3"))
    f += formula("v = g·t        |        s = ½·g·t²", "s là quãng đường rơi (độ cao đã rơi)")
    f += formula("v² = 2·g·s        |        t = √(2s/g)", "v là tốc độ khi rơi được quãng đường s")
    f.append(P("Quãng đường rơi trong <b>giây thứ n</b>: Δs = g(n − 0,5). "
               "Quãng đường trong n giây: s<sub>n</sub> = ½g·n².", "body"))

    f.append(P("<b>3. Vật rơi trong không khí</b>", "h3"))
    f.append(P("Lực cản của không khí phụ thuộc vào <b>hình dạng, kích thước và tốc độ</b> của vật. Vì vậy:", "body"))
    f += bullets([
        "Tờ giấy <b>để phẳng</b> có lực cản lớn nên rơi chậm; tờ giấy <b>vo tròn</b> có lực cản nhỏ nên rơi nhanh hơn – "
        "dù khối lượng không đổi.",
        "Chuyển động rơi được <b>coi gần đúng là rơi tự do</b> khi lực cản không khí <b>rất nhỏ</b> so với trọng lực: "
        "vật nặng, chắc; quãng đường rơi ngắn; hình dạng khí động học.",
        "Trong chân không (hoặc khi bỏ qua lực cản), mọi vật rơi với cùng gia tốc g.",
    ])

    f.append(box("Ví dụ mẫu", [
        P("Một vật rơi tự do từ độ cao 45 m. Lấy g = 10 m/s². Tính thời gian rơi và tốc độ khi chạm đất.", "box_item"),
        P("Thời gian: t = √(2s/g) = √(2·45/10) = √9 = <b>3 s</b>.", "box_item"),
        P("Tốc độ chạm đất: v = g·t = 10·3 = <b>30 m/s</b> (hoặc v = √(2gs) = 30 m/s).", "box_item"),
        P("Quãng đường rơi trong giây thứ 3: Δs = g(n − 0,5) = 10·2,5 = <b>25 m</b> "
          "(kiểm tra: s₃ − s₂ = 45 − 20 = 25 m).", "box_item"),
    ], "ex"))

    f.append(box("Mở rộng – ném thẳng đứng", [
        P("Ném thẳng đứng <b>lên</b> với vận tốc đầu v<sub>0</sub>, chọn chiều dương hướng lên: a = −g.", "box_item"),
        P("Thời gian lên đến điểm cao nhất: t = v<sub>0</sub>/g; độ cao cực đại: h = v<sub>0</sub>²/(2g).", "box_item"),
        P("Thời gian từ lúc ném đến lúc về lại điểm ném = 2v<sub>0</sub>/g (bỏ qua lực cản).", "box_item"),
    ], "note"))

    f.append(box("Mẹo nhớ", [
        P("<b>“Rơi tự do = nhanh dần đều với a = g, v₀ = 0”</b>.", "box_item"),
        P("Tỉ lệ quãng đường rơi sau 1 s, 2 s, 3 s… là <b>1 : 4 : 9</b> (vì s ~ t²).", "box_item"),
        P("Quãng đường trong các giây liên tiếp: <b>1 : 3 : 5 : 7</b> (số lẻ liên tiếp).", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("“Vật nặng rơi nhanh hơn vật nhẹ” → <b>Sai</b> khi bỏ qua lực cản.", "box_item"),
        P("Cho rằng mọi vật rơi trong không khí đều là rơi tự do → <b>Sai</b>, phải thoả mãn lực cản rất nhỏ.", "box_item"),
        P("Dùng s = ½gt² khi vật có vận tốc đầu khác 0 → phải dùng s = v₀t + ½gt².", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def tong_ket_b():
    """Sơ đồ tư duy tổng kết + bảng tra nhanh toàn bộ chương."""
    from .figures import fig_mindmap_ch2

    from .style import CondPageBreak
    f = [CondPageBreak(420)]
    f.append(P("SƠ ĐỒ TƯ DUY TỔNG KẾT CHƯƠNG II – ĐỘNG HỌC", "h2"))
    f.append(P("Nhìn một lượt là thấy cả chương: từ <b>độ dịch chuyển</b> → <b>tốc độ, vận tốc</b> → "
               "<b>đồ thị</b> → <b>gia tốc</b> → <b>chuyển động thẳng biến đổi đều</b> → <b>rơi tự do</b>. "
               "Hãy tự vẽ lại sơ đồ này ra giấy trắng – nếu vẽ được không cần nhìn là em đã nắm chắc cả chương.", "body"))
    f.append(SPC(3))
    f.append(fig_mindmap_ch2())
    f.append(P("Sơ đồ tư duy Chương II – mỗi nhánh là một nhóm công thức và một nhóm câu hỏi của đề", "cap"))
    f.append(SPC(6))

    f.append(box("Cách dùng sơ đồ để ôn nhanh trong 10 phút", [
        P("<b>1.</b> Che các ô, chỉ nhìn tên nhánh và đọc to công thức của nhánh đó.", "box_item"),
        P("<b>2.</b> Với mỗi nhánh, tự đặt <b>một câu hỏi “bẫy”</b> rồi trả lời (ví dụ: “thẳng đều thì vận tốc có đổi không?”).", "box_item"),
        P("<b>3.</b> Nhánh nào không nhớ → mở lại đúng bài đó, không học lại cả chương.", "box_item"),
    ], "tip"))
    f.append(SPC(4))

    f.append(P("Bảng “mỗi bài một dòng” – dùng để tự kiểm tra chéo", "h2"))
    f.append(data_table(
        ["Bài", "Câu chốt", "Sai lầm chết người"],
        [
            ["1", "Vật lí = vật chất + các dạng vận động + quy luật", "Nhầm 4 cuộc CMCN"],
            ["2", "Đỏ cấm – vàng cảnh báo – xanh chỉ dẫn", "Nghĩ tam giác vàng là biển cấm"],
            ["3", "ΔA = ΔĀ + ΔA<sub>dc</sub>; A = Ā ± ΔA", "Quên cộng sai số dụng cụ"],
            ["4", "|Δd| ≤ s; bằng nhau khi thẳng, không đổi chiều", "Cho rằng độ dịch chuyển luôn dương"],
            ["5", "Tốc độ theo quãng đường, vận tốc theo độ dịch chuyển", "Dùng s/Δt để tính vận tốc"],
            ["6", "A ↔ B: đo thời gian đi từ cổng A đến cổng B", "Nhầm A + B với A ↔ B"],
            ["7", "Độ dốc đồ thị d – t = vận tốc", "Đọc độ cao thay vì độ dốc"],
            ["8", "a = Δv/Δt; cùng chiều v thì nhanh dần", "Cho rằng a âm là chậm dần"],
            ["9", "v = v₀ + at; s = v₀t + ½at²; v² − v₀² = 2as", "Quên đổi km/h sang m/s"],
            ["10", "Rơi tự do: v₀ = 0, a = g, s = ½gt²", "Nghĩ vật nặng rơi nhanh hơn"],
        ],
        [26, 288, 197], align=["CENTER", "LEFT", "LEFT"], font="tbl_small",
    ))
    return f
