# -*- coding: utf-8 -*-
"""Phần B – Lý thuyết trọng tâm (Bài 1 → Bài 5)."""
from __future__ import annotations

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from .figures import fig_displacement
from .style import (
    CONTENT_W, P, S, SPC, bullets, box, data_table, formula, lesson_header, numbered, rule,
)


# =========================================================================== #
def bai1():
    f = []
    f += lesson_header("1", "Làm quen với Vật lí", "Ma trận: 1 câu – mức Biết")

    f.append(P("<b>1. Đối tượng nghiên cứu của Vật lí</b>", "h3"))
    f.append(P(
        "Vật lí học nghiên cứu <b>các dạng vận động của vật chất</b> (cơ học, nhiệt, điện, từ, "
        "quang, âm, hạt nhân…) và <b>các quy luật chi phối</b> các dạng vận động đó. Vì vậy Vật lí "
        "là cơ sở của nhiều ngành khoa học, kĩ thuật và công nghệ.", "body"))
    f.append(P(
        "Các lĩnh vực chính: <b>cơ học</b> – <b>nhiệt học</b> – <b>điện từ học</b> – <b>quang học</b> – "
        "<b>âm học</b> – <b>vật lí lượng tử</b> – <b>vật lí hạt nhân</b> – <b>vật lí chất rắn</b>…", "body"))

    f.append(P("<b>2. Vật lí với bốn cuộc cách mạng công nghiệp</b>", "h3"))
    f.append(data_table(
        ["Cuộc CMCN", "Thời gian", "Thành tựu tiêu biểu", "Vật lí gắn với"],
        [
            ["Lần thứ nhất", "Cuối TK XVIII", "Máy hơi nước, cơ khí hoá sản xuất", "Cơ học cổ điển (Newton)"],
            ["Lần thứ hai", "Cuối TK XIX – đầu TK XX", "Điện năng, động cơ điện, thông tin liên lạc", "Điện từ học (Faraday – Maxwell)"],
            ["Lần thứ ba", "Nửa sau TK XX", "Máy tính, tự động hoá, laser, chất bán dẫn", "Vật lí lượng tử, vật lí chất rắn"],
            ["Lần thứ tư", "Đầu TK XXI", "Trí tuệ nhân tạo, IoT, dữ liệu lớn, năng lượng tái tạo", "Vật lí hiện đại, vật liệu mới"],
        ],
        [72, 96, 208, 135], align=["LEFT", "LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(5))

    f.append(P("<b>3. Phương pháp nghiên cứu Vật lí</b>", "h3"))
    f.append(P("<b>a) Phương pháp thực nghiệm</b> – quan sát hiện tượng, đặt câu hỏi, nêu giả thuyết, "
               "thiết kế và tiến hành thí nghiệm, thu thập – xử lí số liệu rồi rút ra kết luận.", "body"))
    f.append(P("<b>b) Phương pháp lí thuyết</b> – xây dựng mô hình, dùng công cụ toán học để suy luận, "
               "tiên đoán kết quả mới, sau đó kiểm chứng bằng thực nghiệm.", "body"))
    f.append(P("Hai phương pháp <b>bổ trợ cho nhau</b>: lí thuyết đề xuất – thực nghiệm kiểm chứng; "
               "thực nghiệm phát hiện – lí thuyết giải thích.", "body"))

    f.append(box("Quá trình phát triển của Vật lí (3 chặng)", [
        P("<b>Vật lí cổ đại</b> (trước TK XVII): A-ri-xtốt, Ác-si-mét – chủ yếu quan sát, suy luận.", "box_item"),
        P("<b>Vật lí cổ điển</b> (TK XVII – XIX): Ga-li-lê, Niu-tơn, Fa-ra-đây, Mác-xoen – hình thành "
          "cơ học, điện từ học.", "box_item"),
        P("<b>Vật lí hiện đại</b> (TK XX – nay): Anh-xtanh, Bo, … – thuyết tương đối, cơ học lượng tử.", "box_item"),
    ], "def"))

    f.append(box("Mẹo nhớ 4 cuộc cách mạng", [
        P("<b>“Nước – Điện – Máy tính – Trí tuệ”</b>: hơi <b>nước</b> → <b>điện</b> khí hoá → "
          "<b>máy tính</b>/tự động hoá → <b>trí tuệ</b> nhân tạo.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("“Vật lí chỉ nghiên cứu chuyển động cơ học” → <b>Sai</b>: còn nhiệt, điện, từ, quang, hạt nhân…", "box_item"),
        P("“Toán học là đối tượng nghiên cứu của Vật lí” → <b>Sai</b>: toán là <i>công cụ</i>.", "box_item"),
        P("“Thực nghiệm không cần lí thuyết” → <b>Sai</b>: hai phương pháp bổ trợ nhau.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai2():
    f = []
    f += lesson_header("2", "Các quy tắc an toàn trong phòng thực hành Vật lí",
                       "Ma trận: 1 câu Biết + 1 câu Hiểu")

    f.append(P("<b>1. Các nguy cơ mất an toàn</b>", "h3"))
    f.append(P("Điện giật (dây hở, tay ướt, chạm kim loại trần) · cháy – nổ (dung môi, khí gas, bình áp suất) · "
               "bỏng nhiệt hoặc bỏng hoá chất · nhiễm độc, ăn mòn · vết cắt do thuỷ tinh vỡ · "
               "bức xạ, tia laser · tiếng ồn · trượt ngã, chấn thương cơ học.", "body"))

    f.append(P("<b>2. Quy tắc an toàn cốt lõi</b>", "h3"))
    f += bullets([
        "<b>Trang bị bảo hộ</b>: áo blouse, kính bảo vệ, găng tay; buộc gọn tóc, không đi dép lê.",
        "<b>Đọc kĩ hướng dẫn</b> và chỉ tiến hành khi được giáo viên cho phép.",
        "<b>Kiểm tra thiết bị</b> trước khi dùng; báo ngay dây điện hở, dụng cụ nứt, hoá chất hết hạn.",
        "<b>Không ăn – uống – đùa nghịch</b>; không để chất lỏng gần thiết bị điện; tay khô khi thao tác điện.",
        "<b>Sắp xếp ngăn nắp</b>, dán nhãn hoá chất, không để lẫn hoá chất với thực phẩm.",
        "<b>Xử lí chất thải</b> đúng quy định; tắt thiết bị, ngắt điện, vệ sinh sau khi làm.",
        "<b>Báo ngay</b> cho giáo viên khi xảy ra sự cố; không tự ý dập lửa bằng nước nếu có điện.",
    ])

    f.append(P("<b>3. Biển báo trong phòng thí nghiệm</b>", "h3"))
    f.append(data_table(
        ["Loại biển báo", "Hình dạng – màu sắc", "Ý nghĩa"],
        [
            ["Biển cấm", "Hình tròn, viền đỏ, gạch chéo đỏ", "Cấm hành vi nguy hiểm (cấm lửa, cấm hút thuốc…)"],
            ["Biển cảnh báo", "Tam giác đều, viền đỏ, nền vàng", "Cảnh báo nguy cơ: điện cao áp, độc, dễ cháy, bức xạ…"],
            ["Biển chỉ dẫn", "Hình chữ nhật/hình tròn, nền xanh", "Chỉ dẫn an toàn: lối thoát, vị trí bình chữa cháy…"],
        ],
        [86, 176, 249], align=["LEFT", "LEFT", "LEFT"],
    ))
    f.append(SPC(5))

    f.append(P("<b>4. Một số biểu tượng cần nhận ra</b>", "h3"))
    f.append(P("Tia chớp trong tam giác vàng = <b>nguy hiểm về điện</b> · đầu lâu xương chéo = <b>chất độc</b> · "
               "ngọn lửa = <b>dễ cháy</b> · ba vòng tròn cắt nhau = <b>nguy hiểm sinh học</b> · "
               "cánh quạt ba lá (vàng – đen) = <b>phóng xạ</b>.", "body"))

    f.append(box("Mẹo nhớ màu biển báo", [
        P("<b>ĐỎ = CẤM</b> – <b>VÀNG = CẢNH BÁO</b> – <b>XANH = CHỈ DẪN/AN TOÀN</b>.", "box_item"),
        P("Câu hỏi hay gặp: “Biển tam giác vàng” là cảnh báo, <b>không phải</b> biển cấm.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("“Được tự ý lắp đặt, thử nghiệm thiết bị khi chưa có hướng dẫn” → <b>Sai</b>.", "box_item"),
        P("“Đeo kính bảo hộ là nguy cơ mất an toàn” → <b>Sai</b>, đó là biện pháp an toàn.", "box_item"),
        P("“Có thể dùng nước dập đám cháy do điện” → <b>Rất nguy hiểm</b>: phải ngắt điện trước.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai3():
    f = []
    f += lesson_header("3", "Thực hành tính sai số trong phép đo. Ghi kết quả đo",
                       "Ma trận: 1 câu – mức Biết")

    f.append(P("<b>1. Phép đo trực tiếp và phép đo gián tiếp</b>", "h3"))
    f += bullets([
        "<b>Phép đo trực tiếp</b>: so sánh trực tiếp đại lượng cần đo với dụng cụ đo (thước đo chiều dài, "
        "cân đo khối lượng, đồng hồ đo thời gian).",
        "<b>Phép đo gián tiếp</b>: đo các đại lượng trực tiếp rồi <b>tính</b> đại lượng cần tìm qua công thức "
        "(ví dụ đo s và t rồi tính v = s/Δt).",
    ])

    f.append(P("<b>2. Hai loại sai số</b>", "h3"))
    f.append(data_table(
        ["Tiêu chí", "Sai số hệ thống", "Sai số ngẫu nhiên"],
        [
            ["Nguyên nhân", "Dụng cụ chế tạo không chuẩn, điểm 0 lệch, chia độ không đều",
             "Thao tác người đo, giác quan, điều kiện môi trường thay đổi"],
            ["Đặc điểm", "Lặp lại giống nhau ở mọi lần đo; có thể hiệu chỉnh được",
             "Mỗi lần đo một giá trị khác nhau; không loại bỏ hoàn toàn"],
            ["Cách xử lí", "Hiệu chỉnh dụng cụ; lấy bằng nửa ĐCNN hoặc theo nhà sản xuất",
             "Đo nhiều lần, lấy giá trị trung bình"],
        ],
        [64, 216, 231], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(5))

    f.append(P("<b>3. Công thức tính sai số của phép đo trực tiếp</b>", "h3"))
    f += formula("Ā = (A<sub>1</sub> + A<sub>2</sub> + … + A<sub>n</sub>) / n")
    f += formula("ΔA<sub>i</sub> = |Ā − A<sub>i</sub>|   →   ΔĀ = (ΔA<sub>1</sub> + … + ΔA<sub>n</sub>) / n",
                 "ΔA<sub>i</sub>: sai số tuyệt đối của lần đo thứ i; ΔĀ: sai số ngẫu nhiên tuyệt đối trung bình")
    f += formula("ΔA = ΔĀ + ΔA<sub>dc</sub>", "sai số tuyệt đối của phép đo = sai số ngẫu nhiên + sai số dụng cụ")
    f += formula("δA = (ΔA / Ā) × 100%", "sai số tỉ đối – cho biết độ chính xác của phép đo; δ càng nhỏ càng chính xác")
    f += formula("A = Ā ± ΔA", "kết quả đo được viết dưới dạng khoảng giá trị: Ā − ΔA ≤ A ≤ Ā + ΔA")

    f.append(box("Cách ghi kết quả đúng (rất hay hỏi)", [
        P("<b>ΔA</b> viết đến <b>1 hoặc 2 chữ số có nghĩa</b>, cùng bậc với ĐCNN của dụng cụ.", "box_item"),
        P("<b>Ā</b> được viết đến <b>cùng bậc thập phân</b> với ΔA (ví dụ 12,5 ± 0,1 cm, không viết 12,53 ± 0,1).", "box_item"),
        P("Làm tròn: chữ số bỏ đi <b>≥ 5</b> thì tăng chữ số bên trái thêm 1; <b>< 5</b> thì giữ nguyên.", "box_item"),
        P("<b>ΔA<sub>dc</sub></b> thường lấy bằng <b>nửa ĐCNN</b> (thước ĐCNN 1 mm → 0,5 mm) hoặc theo thông số nhà sản xuất.", "box_item"),
    ], "def"))

    f.append(P("<b>4. Sai số của phép đo gián tiếp</b>", "h3"))
    f.append(data_table(
        ["Phép tính", "Cách tính sai số", "Ví dụ"],
        [
            ["Tổng – hiệu: A = B ± C", "ΔA = ΔB + ΔC (cộng sai số tuyệt đối)", "s = s₁ + s₂ → Δs = Δs₁ + Δs₂"],
            ["Tích – thương: A = B·C", "δA = δB + δC (cộng sai số tỉ đối)", "v = s/t → δv = δs + δt"],
            ["Luỹ thừa: A = B<super>n</super>", "δA = n·δB", "d = 2r → δd = δr"],
        ],
        [126, 192, 193], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(5))

    f.append(P("<b>5. Ví dụ mẫu có lời giải</b>", "h3"))
    f.append(box("Đo chiều dài một vật bằng thước có ĐCNN 0,1 cm, thu được 5 giá trị: "
                 "12,4 – 12,5 – 12,4 – 12,6 – 12,6 (cm).", [
        P("<b>Bước 1 – Giá trị trung bình:</b> Ā = (12,4 + 12,5 + 12,4 + 12,6 + 12,6)/5 = <b>12,5 cm</b>.", "box_item"),
        P("<b>Bước 2 – Sai số từng lần:</b> 0,1 ; 0 ; 0,1 ; 0,1 ; 0,1 (cm).", "box_item"),
        P("<b>Bước 3 – Sai số ngẫu nhiên trung bình:</b> ΔĀ = (0,1 + 0 + 0,1 + 0,1 + 0,1)/5 = 0,08 cm.", "box_item"),
        P("<b>Bước 4 – Sai số dụng cụ:</b> ΔA<sub>dc</sub> = 0,1/2 = 0,05 cm.", "box_item"),
        P("<b>Bước 5 – Sai số tuyệt đối:</b> ΔA = 0,08 + 0,05 = 0,13 ≈ <b>0,1 cm</b>.", "box_item"),
        P("<b>Kết quả:</b> L = <b>12,5 ± 0,1 cm</b>; sai số tỉ đối δ = 0,13/12,5 ≈ <b>1,0%</b>.", "box_item"),
    ], "ex"))

    f.append(box("Mẹo nhớ quy trình 5 bước", [
        P("<b>“Trung bình → lệch từng lần → lệch trung bình → cộng dụng cụ → chia – nhân 100”</b>", "box_item"),
        P("Tức là: Ā → ΔA<sub>i</sub> → ΔĀ → + ΔA<sub>dc</sub> → δA.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("Quên <b>cộng sai số dụng cụ</b> → thiếu ΔA<sub>dc</sub>.", "box_item"),
        P("Tính δ = ΔA/Ā rồi quên <b>× 100%</b>.", "box_item"),
        P("Viết Ā = 12,53 ± 0,1 cm → <b>sai bậc</b>, phải là 12,5 ± 0,1 cm.", "box_item"),
        P("Nhầm phép đo trực tiếp với gián tiếp: tính v từ s, t là <b>gián tiếp</b>.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai4():
    f = []
    f += lesson_header("4", "Độ dịch chuyển và quãng đường đi được",
                       "Ma trận: 1 câu Biết + 2 câu Hiểu")

    f.append(P("<b>1. Xác định vị trí của vật</b>", "h3"))
    f.append(P("Muốn xác định vị trí của vật ta cần: <b>vật làm mốc</b> + <b>hệ toạ độ</b> + <b>mốc thời gian</b> "
               "(gộp lại gọi là <b>hệ quy chiếu</b>) và một <b>thước đo</b>, một <b>đồng hồ</b>.", "body"))

    f.append(P("<b>2. Độ dịch chuyển</b>", "h3"))
    f += bullets([
        "Là <b>đại lượng vectơ</b> nối vị trí đầu với vị trí cuối của chuyển động, cho biết cả <b>độ lớn</b> và <b>hướng</b> sự thay đổi vị trí.",
        "Trên trục Ox: Δd = d<sub>2</sub> − d<sub>1</sub> (có thể dương, âm hoặc bằng 0).",
        "Độ lớn độ dịch chuyển là <b>khoảng cách ngắn nhất</b> từ điểm đầu đến điểm cuối, <b>không phụ thuộc đường đi</b>.",
        "Đơn vị: mét (m).",
    ])

    f.append(P("<b>3. Quãng đường đi được</b>", "h3"))
    f.append(P("Là <b>tổng độ dài quỹ đạo</b> mà vật đã vạch ra, là <b>đại lượng vô hướng</b>, luôn dương hoặc bằng 0 "
               "và <b>phụ thuộc vào đường đi</b>. Đơn vị: mét (m).", "body"))

    f.append(P("<b>4. So sánh hai đại lượng</b>", "h3"))
    f.append(data_table(
        ["Tiêu chí", "Độ dịch chuyển", "Quãng đường"],
        [
            ["Bản chất", "Đại lượng <b>vectơ</b>", "Đại lượng <b>vô hướng</b>"],
            ["Đặc trưng", "Độ lớn + hướng", "Chỉ có độ lớn"],
            ["Phụ thuộc", "Chỉ phụ thuộc vị trí đầu – cuối", "Phụ thuộc toàn bộ đường đi"],
            ["Giá trị", "Có thể dương, âm, bằng 0", "Luôn ≥ 0"],
            ["Liên hệ", "|Δd| ≤ s", "s ≥ |Δd|"],
        ],
        [80, 216, 215], align=["LEFT", "LEFT", "LEFT"],
    ))
    f.append(SPC(5))
    f.append(P("<b>Dấu bằng |Δd| = s</b> xảy ra khi vật chuyển động <b>thẳng và không đổi chiều</b>. "
               "Nếu vật đi vòng kín trở về chỗ cũ: <b>Δd = 0</b> nhưng <b>s ≠ 0</b>.", "body"))
    f.append(SPC(2))
    f.append(fig_displacement())
    f.append(P("Quãng đường (nét đứt) luôn “dài hơn hoặc bằng” độ dịch chuyển (mũi tên liền)", "cap"))
    f.append(SPC(6))

    f.append(box("Ví dụ mẫu", [
        P("Một người đi 3 km về hướng Đông rồi 4 km về hướng Bắc. Tính quãng đường và độ lớn độ dịch chuyển.", "box_item"),
        P("<b>Giải:</b> s = 3 + 4 = <b>7 km</b>. Hai đoạn vuông góc nên d = √(3² + 4²) = <b>5 km</b>, "
          "hướng Đông – Bắc (hợp với hướng Đông góc 53°).", "box_item"),
    ], "ex"))

    f.append(box("Mẹo nhớ", [
        P("<b>“Quãng đường = độ dài đường đi; Độ dịch chuyển = mũi tên nối đầu – cuối”</b>.", "box_item"),
        P("Thấy chữ “vòng tròn”, “quay về chỗ cũ” → độ dịch chuyển <b>bằng 0</b>.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("“Độ dịch chuyển luôn dương” → <b>Sai</b>: có thể âm tuỳ chiều dương đã chọn.", "box_item"),
        P("“Độ lớn độ dịch chuyển luôn bằng quãng đường” → <b>Sai</b>, chỉ bằng khi thẳng và không đổi chiều.", "box_item"),
        P("“Quãng đường là vectơ” → <b>Sai</b>.", "box_item"),
    ], "warn"))
    return f


# =========================================================================== #
def bai5():
    f = []
    f += lesson_header("5", "Tốc độ và vận tốc",
                       "Ma trận: 1 câu Biết (P.I) + 1 câu Biết (P.III) + 1 ý Hiểu (P.IV) + 2 ý Đúng/Sai")

    f.append(P("<b>1. Tốc độ trung bình</b>", "h3"))
    f.append(P("Tốc độ trung bình cho biết <b>mức độ nhanh, chậm</b> của chuyển động trên cả quãng đường đã đi:", "body"))
    f += formula("v<sub>tb</sub> = s / Δt", "s: quãng đường (m); Δt: thời gian đi hết quãng đường (s); đơn vị m/s hoặc km/h")
    f.append(P("Tốc độ trung bình là <b>đại lượng vô hướng</b>, <b>không</b> phải trung bình cộng của các tốc độ.", "body"))

    f.append(P("<b>2. Tốc độ tức thời</b>", "h3"))
    f.append(P("Là tốc độ tại một thời điểm (hoặc một vị trí) xác định, đo được trong khoảng thời gian <b>rất nhỏ</b>. "
               "Số chỉ trên đồng hồ tốc độ của xe máy, ô tô là tốc độ tức thời.", "body"))

    f.append(P("<b>3. Vận tốc</b>", "h3"))
    f += bullets([
        "<b>Vận tốc trung bình</b>: <b>v</b><sub>tb</sub> = Δ<b>d</b>/Δt – là <b>đại lượng vectơ</b>, đặc trưng cho "
        "sự thay đổi vị trí theo thời gian.",
        "<b>Vận tốc tức thời</b>: vectơ tại một thời điểm, có <b>phương tiếp tuyến với quỹ đạo</b>, "
        "<b>chiều là chiều chuyển động</b>; <b>độ lớn bằng tốc độ tức thời</b>.",
        "Đơn vị: m/s; đổi 1 km/h = 1/3,6 m/s ≈ 0,278 m/s; 36 km/h = 10 m/s.",
    ])
    f.append(SPC(3))
    f.append(data_table(
        ["Tiêu chí", "Tốc độ", "Vận tốc"],
        [
            ["Loại đại lượng", "Vô hướng", "Vectơ"],
            ["Công thức", "v = s/Δt (quãng đường)", "v = Δd/Δt (độ dịch chuyển)"],
            ["Ý nghĩa", "Mức nhanh – chậm", "Nhanh – chậm + hướng"],
            ["So sánh", "Luôn ≥ |vận tốc trung bình|", "|v| ≤ tốc độ trung bình"],
        ],
        [86, 200, 225], align=["LEFT", "LEFT", "LEFT"],
    ))
    f.append(SPC(6))

    f.append(P("<b>4. Công thức cộng vận tốc</b>", "h3"))
    f.append(P("Với (1) là vật chuyển động, (2) là hệ quy chiếu chuyển động (dòng nước, gió, băng tải…), "
               "(3) là hệ quy chiếu đứng yên (bờ):", "body"))
    f += formula("<b>v</b><sub>13</sub> = <b>v</b><sub>12</sub> + <b>v</b><sub>23</sub>")
    f.append(data_table(
        ["Trường hợp", "Độ lớn vận tốc tổng hợp", "Ví dụ"],
        [
            ["Hai vận tốc <b>cùng phương, cùng chiều</b>", "v<sub>13</sub> = v<sub>12</sub> + v<sub>23</sub>", "Thuyền xuôi dòng"],
            ["Hai vận tốc <b>cùng phương, ngược chiều</b>", "v<sub>13</sub> = |v<sub>12</sub> − v<sub>23</sub>|", "Thuyền ngược dòng"],
            ["Hai vận tốc <b>vuông góc</b>", "v<sub>13</sub> = √(v<sub>12</sub>² + v<sub>23</sub>²)", "Thuyền sang ngang sông"],
        ],
        [186, 168, 157], align=["LEFT", "LEFT", "LEFT"],
    ))
    f.append(SPC(5))

    f.append(box("Ví dụ mẫu", [
        P("Ca nô chạy với tốc độ 8 m/s so với nước; nước chảy với tốc độ 6 m/s so với bờ. Tính tốc độ của ca nô so với bờ khi:", "box_item"),
        P("a) ca nô chạy <b>xuôi dòng</b>: v = 8 + 6 = <b>14 m/s</b>.", "box_item"),
        P("b) ca nô chạy <b>ngược dòng</b>: v = |8 − 6| = <b>2 m/s</b>.", "box_item"),
        P("c) ca nô chạy <b>vuông góc</b> với dòng nước: v = √(8² + 6²) = <b>10 m/s</b>.", "box_item"),
    ], "ex"))

    f.append(box("Mẹo nhớ", [
        P("<b>“Tốc độ đo đường – Vận tốc đo độ dời”</b>. Vận tốc có thêm mũi tên chỉ hướng.", "box_item"),
        P("Cộng vectơ: <b>cùng chiều thì cộng – ngược chiều thì trừ – vuông góc thì Py-ta-go</b>.", "box_item"),
    ], "tip"))

    f.append(box("Bẫy thường gặp", [
        P("Tính “vận tốc trung bình = quãng đường/thời gian” → đó là <b>tốc độ</b> trung bình.", "box_item"),
        P("Tính tốc độ trung bình bằng <b>trung bình cộng</b> hai tốc độ → chỉ đúng khi hai đoạn <b>dài bằng nhau</b>.", "box_item"),
        P("Vật đi vòng tròn đều: tốc độ không đổi nhưng <b>vận tốc luôn đổi</b> (đổi hướng).", "box_item"),
    ], "warn"))
    return f
