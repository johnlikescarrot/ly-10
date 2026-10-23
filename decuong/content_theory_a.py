# -*- coding: utf-8 -*-
"""PHẦN 1 – Lý thuyết trọng tâm: Bài 1 → Bài 6."""
from style import *


def story():
    s = []
    s.append(H1("PHẦN 1 · LÝ THUYẾT TRỌNG TÂM (BÀI 1 → BÀI 10)"))
    s.append(P("Mỗi bài được trình bày theo cùng một khuôn: <b>khái niệm cốt lõi → công thức → "
               "ví dụ mẫu → mẹo nhớ → bẫy đề</b>. Bạn có thể học bài nào trước cũng được, nhưng "
               "hãy học theo đúng thứ tự túi điểm ở Mục 0.3 nếu thời gian gấp.", "lead"))

    # ================================================================= BÀI 1
    s.append(H1B("CHỦ ĐỀ 1 · MỞ ĐẦU"))
    s.append(H2("Bài 1. Làm quen với Vật lí"))
    s.append(H3("1. Đối tượng – mục tiêu – các lĩnh vực"))
    s.append(P("<b>Vật lí</b> là môn khoa học tự nhiên, có đối tượng nghiên cứu là <b>các dạng vận động "
               "của vật chất (chất, trường) và năng lượng</b>. Mục tiêu của môn học là giúp học sinh "
               "có được những kiến thức phổ thông cốt lõi, rèn luyện kĩ năng thực nghiệm và tư duy khoa học, "
               "biết vận dụng kiến thức vào thực tiễn."))
    s.append(P("<b>10 lĩnh vực nghiên cứu:</b> cơ học; điện học; điện từ học; quang học; âm học; nhiệt học; "
               "nhiệt động lực học; vật lí nguyên tử và hạt nhân; vật lí lượng tử; thuyết tương đối."))
    s.append(formula("Cơ · Điện · Điện từ · Quang · Âm · Nhiệt · Nhiệt động · "
                     "Nguyên tử &amp; hạt nhân · Lượng tử · Tương đối",
                     "Câu “thần chú” 10 cụm từ để kể tên đủ các lĩnh vực nghiên cứu"))

    s.append(H3("2. Quá trình phát triển của Vật lí (3 giai đoạn)"))
    s.append(table([
        ["Giai đoạn", "Thời gian", "Cách các nhà khoa học tìm hiểu tự nhiên"],
        ["<b>1</b>", "Từ khoảng 350 TCN đến thế kỉ XVI",
         "Dựa vào <b>quan sát và suy luận chủ quan</b> (triết học tự nhiên)"],
        ["<b>2</b>", "Thế kỉ XVII đến cuối thế kỉ XIX",
         "Dựa vào <b>phương pháp thực nghiệm</b> (Galilei mở đầu)"],
        ["<b>3</b>", "Cuối thế kỉ XIX đến nay",
         "Tập trung vào các <b>mô hình lí thuyết</b> để tìm hiểu thế giới vi mô, dùng <b>thí nghiệm để kiểm chứng</b>"],
    ], [44, 118, CONTENT_W - 162], font=8.2, align=["c", "l", "l"]))
    s.append(SP(4))

    s.append(H3("3. Vật lí với khoa học, kĩ thuật, công nghệ – 4 cuộc cách mạng công nghiệp"))
    s.append(table([
        ["CMCN", "Mốc thời gian", "Thành tựu Vật lí", "Đặc trưng"],
        ["<b>Lần 1</b>", "1765", "Nghiên cứu về <b>nhiệt</b> → James Watt chế tạo máy hơi nước",
         "Thay thế <b>sức lực cơ bắp</b> bằng sức lực máy móc"],
        ["<b>Lần 2</b>", "Cuối thế kỉ XIX (1831)",
         "Faraday phát hiện <b>cảm ứng điện từ</b> → máy phát điện",
         "Sử dụng ngày càng nhiều <b>thiết bị dùng điện</b>"],
        ["<b>Lần 3</b>", "Những năm 70 của thế kỉ XX",
         "<b>Điện tử, chất bán dẫn, vi mạch</b> (chip)",
         "<b>Tự động hoá</b> các quá trình sản xuất (dây chuyền tự động)"],
        ["<b>Lần 4</b>", "Đầu thế kỉ XXI",
         "Vật lí hiện đại: <b>trí tuệ nhân tạo, robot, internet toàn cầu, công nghệ nano</b>",
         "Thiết bị <b>thông minh</b>: điện thoại, nhà ở, nhà máy thông minh"],
    ], [50, 96, 190, CONTENT_W - 336], font=8.0))
    s.append(SP(4))
    s.append(box("<b>“MÁY – ĐIỆN – TỰ ĐỘNG – AI”</b><br/>"
                 "Lần 1 = <b>Máy</b> hơi nước (nhiệt) · Lần 2 = <b>Điện</b> (cảm ứng điện từ) · "
                 "Lần 3 = <b>Tự động</b> hoá (bán dẫn, vi mạch) · Lần 4 = <b>AI</b> – robot – internet.",
                 "meo"))

    s.append(H3("4. Phương pháp nghiên cứu Vật lí"))
    s.append(P("<b>a) Phương pháp thực nghiệm</b> – phương pháp quan trọng nhất của Vật lí, gồm 5 bước:"))
    s.append(table([
        ["Bước", "Nội dung", "Ví dụ (Galilei – sự rơi)"],
        ["1", "Xác định vấn đề cần nghiên cứu", "Vì sao vật nặng rơi nhanh hơn vật nhẹ?"],
        ["2", "Quan sát, thu thập thông tin", "Quan sát nhiều vật rơi khác khối lượng"],
        ["3", "Đưa ra dự đoán (giả thuyết)", "Mọi vật rơi nhanh như nhau nếu bỏ qua sức cản không khí"],
        ["4", "Thí nghiệm kiểm tra dự đoán", "Thả hai quả cầu khác khối lượng trong ống hút chân không"],
        ["5", "Kết luận", "Dự đoán đúng → chấp nhận; sai → đưa ra dự đoán mới và làm lại"],
    ], [34, 150, CONTENT_W - 184], font=8.2, align=["c", "l", "l"]))
    s.append(SP(4))
    s.append(P("<b>b) Phương pháp mô hình</b> – dùng mô hình (vật thật thu nhỏ, mô hình lí thuyết, "
               "mô hình toán học…) để nghiên cứu, giải thích tính chất của vật thật, gồm 4 bước: "
               "xác định đối tượng cần mô hình hoá → xây dựng mô hình (giả thuyết) → kiểm tra sự phù hợp "
               "của mô hình → kết luận."))
    s.append(P("<b>c) Phương pháp lí thuyết</b> – dùng ngôn ngữ toán học và suy luận lí thuyết để tìm ra "
               "kết quả mới; kết quả đó vẫn phải được kiểm chứng bằng thực nghiệm. Hai phương pháp "
               "thực nghiệm và lí thuyết hỗ trợ lẫn nhau, trong đó <b>thực nghiệm giữ vai trò quyết định</b>."))
    s.append(box("5 bước thực nghiệm: <b>XÁC định vấn đề – QUAN sát – ĐOÁN (dự đoán) – THÍ nghiệm – "
                 "KẾT luận</b> → “<b>XÁC – QUAN – ĐOÁN – THÍ – KẾT</b>”.<br/>"
                 "Galilei được coi là <b>“cha đẻ” của phương pháp thực nghiệm</b>.", "meo"))
    s.append(box("• Hỏi “phương pháp nào <b>quan trọng nhất</b> của Vật lí?” → <b>thực nghiệm</b>.<br/>"
                 "• Hỏi “thành tựu mở đầu CMCN lần 1” → nghiên cứu về <b>nhiệt</b> (máy hơi nước). "
                 "“CMCN lần 2” → <b>cảm ứng điện từ</b>.<br/>"
                 "• Đừng nhầm <b>đối tượng</b> nghiên cứu (các dạng vận động của vật chất và năng lượng) "
                 "với <b>mục tiêu</b> môn học (hình thành kiến thức, kĩ năng cho người học).", "bay"))

    # ================================================================= BÀI 2
    s.append(CondPageBreak(150))
    s.append(H2("Bài 2. Các quy tắc an toàn trong phòng thực hành Vật lí"))
    s.append(H3("1. An toàn khi sử dụng thiết bị thí nghiệm"))
    s.append(table([
        ["Nhóm thiết bị", "Nguy cơ", "Việc phải làm"],
        ["<b>Thiết bị điện</b> (nguồn, biến áp, đồng hồ đo…)",
         "Điện giật, chập điện, cháy nổ",
         "Đọc kĩ hướng dẫn và kí hiệu trên thiết bị; kiểm tra trước khi dùng; <b>tắt công tắc nguồn "
         "trước khi cắm/tháo</b>; chỉ cắm khi hiệu điện thế nguồn đúng với hiệu điện thế định mức; "
         "dây điện gọn gàng; không để nước, dung dịch dẫn điện gần thiết bị"],
        ["<b>Thiết bị nhiệt</b> (đèn cồn, bếp điện, cốc thuỷ tinh)",
         "Bỏng, nứt vỡ",
         "Không chạm tay trần vào vật nóng; dùng kẹp, găng chịu nhiệt; <b>không thổi tắt đèn cồn</b> "
         "(dùng nắp đậy); dùng cốc thuỷ tinh chịu nhiệt"],
        ["<b>Tia laser</b>, vật bắn ra", "Hỏng mắt, thương tích",
         "Không nhìn trực tiếp vào tia laser; giữ khoảng cách an toàn"],
        ["<b>Hoá chất</b>, vật sắc nhọn", "Bỏng hoá chất, ngộ độc, đứt tay",
         "Đeo găng tay, kính bảo hộ; <b>không nếm, không ngửi</b> hoá chất; dọn dẹp đúng nơi quy định"],
    ], [110, 86, CONTENT_W - 196], font=7.9))
    s.append(SP(5))

    s.append(H3("2. Những quy tắc an toàn cốt lõi (phải thuộc lòng)"))
    s.extend(BULL([
        "Đọc kĩ hướng dẫn sử dụng và <b>quan sát các chỉ dẫn, kí hiệu</b> trên thiết bị.",
        "Kiểm tra cẩn thận thiết bị, dụng cụ trước khi sử dụng.",
        "<b>Chỉ tiến hành thí nghiệm khi được sự cho phép</b> của giáo viên.",
        "<b>Tắt công tắc nguồn</b> trước khi cắm hoặc tháo thiết bị điện.",
        "Chỉ cắm phích khi hiệu điện thế nguồn <b>tương ứng với hiệu điện thế định mức</b> của dụng cụ.",
        "Bố trí dây điện gọn gàng, không vướng khi đi lại.",
        "Không tiếp xúc trực tiếp với vật/thiết bị có nhiệt độ cao khi không có dụng cụ bảo hộ.",
        "Không để nước và các dung dịch dẫn điện, dễ cháy gần thiết bị điện.",
        "Giữ khoảng cách an toàn khi nung nóng vật, khi thí nghiệm có vật bắn ra hoặc tia laser.",
        "Vệ sinh, sắp xếp gọn gàng; bỏ chất thải thí nghiệm đúng nơi quy định.",
    ]))
    s.append(box("Những điều <b>KHÔNG</b> được làm: ăn uống, đùa nghịch trong phòng thực hành; để tóc dài, "
                 "đi giày cao gót; tự làm thí nghiệm khi chưa được phép; nếm/ngửi hoá chất; cầm hoá chất "
                 "bằng tay không; thổi tắt đèn cồn; cắm phích điện khi tay ướt.", "bay"))

    s.append(H3("3. Biển báo trong phòng thực hành"))
    s.append(fig_safety())
    s.append(SP(3))
    s.append(table([
        ["Loại biển báo", "Hình dạng – màu sắc", "Ý nghĩa", "Ví dụ"],
        ["<b>Cấm</b>", "Hình tròn, <b>viền đỏ</b>, nền trắng, <b>gạch chéo đỏ</b>",
         "Cấm thực hiện hành vi", "Cấm lửa, cấm hút thuốc, cấm uống nước, cấm ăn uống"],
        ["<b>Cảnh báo nguy hiểm</b>", "Hình <b>tam giác đều</b>, viền đen hoặc đỏ, <b>nền vàng</b>",
         "Báo trước khu vực/nơi có nguy hiểm", "Nguy hiểm về điện, hoá chất ăn mòn, chất phóng xạ, "
         "nhiệt độ cao, vật sắc nhọn"],
        ["<b>Bắt buộc thực hiện</b>", "Hình tròn, <b>nền xanh</b> (dương), kí hiệu trắng",
         "Buộc phải làm theo", "Phải đội mũ, phải đeo kính, phải mang găng, phải nối đất"],
        ["<b>Chỉ dẫn / thông báo</b>", "Hình vuông hoặc chữ nhật, <b>nền xanh lá</b> (hoặc xanh dương)",
         "Chỉ dẫn vị trí, lối đi an toàn", "Lối thoát hiểm, vị trí bình chữa cháy, trạm sơ cứu"],
    ], [86, 132, 100, CONTENT_W - 318], font=7.9))
    s.append(SP(4))
    s.append(box("<b>ĐỎ – CẤM</b> · <b>VÀNG – CẢNH</b> (tam giác) · <b>XANH TRÒN – BẮT BUỘC</b> · "
                 "<b>XANH VUÔNG – CHỈ DẪN</b>. Chỉ cần nhớ 4 cặp màu – hình là làm được toàn bộ câu hỏi "
                 "về biển báo.", "meo"))

    s.append(H3("4. Xử lí khi xảy ra sự cố"))
    s.extend(BULL([
        "<b>Cháy trong phòng thực hành:</b> ngắt toàn bộ hệ thống điện → báo giáo viên, tổ chức thoát nạn, "
        "cứu người → đưa hoá chất, chất dễ cháy ra khu vực an toàn, chống cháy lan → dập lửa.",
        "<b>Không dùng nước</b> để dập đám cháy nơi có thiết bị điện, đám cháy dầu, cồn (chất lỏng nhẹ hơn nước).",
        "<b>Không dùng CO₂</b> để dập đám cháy quần áo trên người hoặc cháy kim loại kiềm (magie…).",
        "<b>Người bị điện giật:</b> nhanh chóng <b>ngắt nguồn điện</b> hoặc dùng vật cách điện tách nạn nhân "
        "ra khỏi nguồn — tuyệt đối không chạm tay trần vào người bị nạn.",
        "Mọi sự cố đều phải <b>báo ngay cho giáo viên</b> phụ trách phòng thực hành.",
    ]))

    # ================================================================= BÀI 3
    s.append(CondPageBreak(150))
    s.append(H2("Bài 3. Thực hành tính sai số trong phép đo. Ghi kết quả đo"))
    s.append(H3("1. Phép đo trực tiếp và phép đo gián tiếp"))
    s.append(table([
        ["", "Phép đo trực tiếp", "Phép đo gián tiếp"],
        ["Khái niệm", "Đọc <b>trực tiếp</b> giá trị của đại lượng trên dụng cụ đo",
         "Tính giá trị đại lượng qua <b>công thức</b> liên hệ với các đại lượng đo trực tiếp"],
        ["Ví dụ", "Dùng thước đo chiều dài, dùng cân đo khối lượng, dùng đồng hồ đo thời gian",
         "Đo tốc độ bằng <b>v = s/t</b> (đo s và t rồi tính), đo khối lượng riêng D = m/V"],
    ], [70, 200, CONTENT_W - 270], font=8.2))
    s.append(SP(5))

    s.append(H3("2. Hai loại sai số"))
    s.append(table([
        ["Tiêu chí", "<b>Sai số hệ thống</b> (sai số dụng cụ)", "<b>Sai số ngẫu nhiên</b>"],
        ["Nguyên nhân", "Do <b>cấu tạo, độ chính xác của dụng cụ</b>; do mẫu vật không chuẩn",
         "Do <b>thao tác chưa chuẩn</b>, điều kiện thí nghiệm không ổn định, giác quan hạn chế"],
        ["Biểu hiện", "Lặp lại như nhau ở mọi lần đo, <b>lệch về một phía</b>",
         "Mỗi lần đo cho giá trị <b>khác nhau, ngẫu nhiên</b> quanh giá trị thật"],
        ["Cách xử lí", "Hiệu chỉnh dụng cụ; lấy bằng <b>nửa độ chia nhỏ nhất (ĐCNN)</b> hoặc theo "
         "nhà sản xuất ghi trên dụng cụ", "Đo <b>nhiều lần</b> rồi lấy <b>trung bình</b>"],
    ], [66, 200, CONTENT_W - 266], font=8.0))
    s.append(SP(4))
    s.append(P("<b>Cấp chính xác</b> của dụng cụ (ghi trên mặt dụng cụ, ví dụ 0,5) cho biết sai số tỉ đối "
               "của dụng cụ đó; số càng nhỏ thì dụng cụ càng chính xác."))

    s.append(H3("3. Bộ công thức bắt buộc"))
    s.append(formula("Ā = (A₁ + A₂ + … + Aₙ) / n", "Giá trị trung bình của n lần đo"))
    s.append(formula("ΔAᵢ = |Ā − Aᵢ|  →  Δ̄A = (ΔA₁ + … + ΔAₙ) / n",
                     "Sai số tuyệt đối của từng lần đo → sai số ngẫu nhiên trung bình"))
    s.append(formula("ΔA = Δ̄A + ΔA<sub>đc</sub>", "Sai số tuyệt đối của phép đo = sai số ngẫu nhiên + sai số dụng cụ"))
    s.append(formula("δA = (ΔA / Ā) × 100%", "Sai số tỉ đối – cho biết <b>mức độ chính xác</b> của phép đo"))
    s.append(box("<b>δA càng nhỏ → phép đo càng chính xác.</b> Sai số tỉ đối không có đơn vị (đơn vị %). "
                 "Từ δA có thể tính ngược ΔA = δA × Ā.", "nho"))

    s.append(H3("4. Sai số của phép đo gián tiếp"))
    s.append(table([
        ["Dạng công thức", "Quy tắc", "Hệ thức"],
        ["A = B + C  hoặc  A = B − C", "Sai số tuyệt đối của tổng/hiệu bằng <b>tổng các sai số tuyệt đối</b>",
         "ΔA = ΔB + ΔC"],
        ["A = B × C  hoặc  A = B / C", "Sai số tỉ đối của tích/thương bằng <b>tổng các sai số tỉ đối</b>",
         "δA = δB + δC"],
    ], [150, 200, CONTENT_W - 350], font=8.2))
    s.append(SP(4))
    s.append(box("<b>“Cộng trừ thì cộng tuyệt đối – Nhân chia thì cộng tỉ đối.”</b> Nhớ đúng một câu này là "
                 "không bao giờ chọn sai quy tắc.", "meo"))

    s.append(H3("5. Cách ghi kết quả đo"))
    s.append(formula("A = Ā ± ΔA    hay    (Ā − ΔA) ≤ A ≤ (Ā + ΔA)"))
    s.extend(BULL([
        "ΔA được viết tới <b>số chữ số có nghĩa tương ứng với ĐCNN</b> của dụng cụ (thường 1–2 chữ số có nghĩa).",
        "Ā được viết tới <b>cùng bậc thập phân</b> với ΔA.",
        "<b>Làm tròn:</b> chữ số bỏ đi &lt; 5 thì giữ nguyên chữ số bên trái; ≥ 5 thì tăng chữ số bên trái thêm 1.",
        "Luôn kèm <b>đơn vị</b> và ghi đúng sai số của <b>từng đại lượng đo</b>, không ghi sai số cho đại lượng "
        "không đo.",
    ]))

    s.append(H3("6. Ví dụ mẫu 1 – đo trực tiếp"))
    s.append(P("Đo chiều dài một vật bằng thước có ĐCNN 1 mm, thu được 5 lần: 12,4; 12,6; 12,5; 12,4; 12,6 (cm). "
               "Tính giá trị trung bình, sai số và ghi kết quả."))
    s.append(P("<b>Giải.</b> Ā = (12,4 + 12,6 + 12,5 + 12,4 + 12,6)/5 = <b>12,50 cm</b>. "
               "Sai số từng lần: 0,10; 0,10; 0,00; 0,10; 0,10 → Δ̄A = 0,40/5 = <b>0,08 cm</b>. "
               "Sai số dụng cụ ΔA<sub>đc</sub> = 0,05 cm. Vậy ΔA = 0,08 + 0,05 = <b>0,13 cm</b>.<br/>"
               "Kết quả: <b>L = 12,50 ± 0,13 (cm)</b>; sai số tỉ đối δ = 0,13/12,50 ≈ <b>1,0%</b>."))

    s.append(H3("7. Ví dụ mẫu 2 – đo gián tiếp"))
    s.append(P("Đo quãng đường s = 50,0 ± 0,5 (cm) và thời gian t = 2,00 ± 0,02 (s). Tính tốc độ v = s/t."))
    s.append(P("<b>Giải.</b> v̄ = 50,0/2,00 = <b>25,0 cm/s</b>. Vì là phép chia nên cộng sai số tỉ đối:<br/>"
               "δv = δs + δt = (0,5/50,0)×100% + (0,02/2,00)×100% = 1% + 1% = <b>2%</b>.<br/>"
               "Δv = 2% × 25,0 = 0,5 cm/s → <b>v = 25,0 ± 0,5 (cm/s)</b>."))
    s.append(box("• Đừng nhầm “sai số tuyệt đối” (có đơn vị) với “sai số tỉ đối” (%).<br/>"
                 "• Đại lượng nào <b>không được đo</b> thì không có sai số riêng.<br/>"
                 "• Trong phép chia, nếu một đại lượng có sai số tỉ đối lớn thì nó quyết định độ chính xác "
                 "của kết quả.", "bay"))

    # ================================================================= BÀI 4
    s.append(CondPageBreak(150))
    s.append(H2("Bài 4. Độ dịch chuyển và quãng đường đi được"))
    s.append(H3("1. Hai khái niệm dễ nhầm nhất chương"))
    s.append(P("<b>Độ dịch chuyển</b> là đại lượng <b>vectơ</b>, đặc trưng cho sự <b>thay đổi vị trí</b> của vật: "
               "có gốc tại vị trí đầu, ngọn tại vị trí cuối. Kí hiệu <b>Δd</b> (hoặc Δx khi chuyển động thẳng)."))
    s.append(P("<b>Quãng đường đi được</b> là đại lượng <b>vô hướng</b>, bằng <b>tổng độ dài</b> của toàn bộ "
               "đường đi, luôn dương (hoặc bằng 0 khi vật không chuyển động). Kí hiệu <b>s</b>."))
    s.append(formula("Chuyển động thẳng: Δx = x₂ − x₁", "Dấu của Δx cho biết vật đi theo chiều dương (+) hay âm (−)"))
    s.append(SP(2))
    s.append(table([
        ["Tiêu chí", "Độ dịch chuyển", "Quãng đường"],
        ["Bản chất", "Đại lượng <b>vectơ</b>", "Đại lượng <b>vô hướng</b>"],
        ["Đặc trưng cho", "Sự <b>thay đổi vị trí</b>", "<b>Độ dài</b> đã đi được"],
        ["Phụ thuộc", "Chỉ phụ thuộc <b>điểm đầu và điểm cuối</b>", "Phụ thuộc <b>toàn bộ đường đi</b>"],
        ["Giá trị", "Có thể dương, âm hoặc bằng 0", "Luôn <b>≥ 0</b>"],
        ["Quan hệ", "Sai khác nhau khi vật <b>đổi chiều hoặc đi đường vòng</b>; d ≤ s",
         "Bằng độ lớn độ dịch chuyển <b>chỉ khi</b> vật chuyển động thẳng, không đổi chiều"],
    ], [70, 200, CONTENT_W - 270], font=8.2))
    s.append(SP(4))
    s.append(box("<b>Độ dịch chuyển = “đi từ đâu đến đâu”. Quãng đường = “đã đi bao xa”.</b> "
                 "Đi 3 km rồi quay về chỗ cũ: quãng đường 6 km nhưng độ dịch chuyển bằng 0.", "meo"))

    s.append(H3("2. Ba ví dụ kinh điển"))
    s.append(table([
        ["Tình huống", "Quãng đường s", "Độ dịch chuyển d"],
        ["Đi 3 km về phía đông rồi 4 km về phía bắc", "3 + 4 = <b>7 km</b>",
         "√(3² + 4²) = <b>5 km</b>, hướng đông–bắc"],
        ["Đi 5 km theo đường thẳng rồi quay lại điểm xuất phát", "<b>10 km</b>", "<b>0</b>"],
        ["Đi được 2/3 vòng tròn bán kính R", "(2/3)·2πR = <b>4πR/3</b>",
         "Dây cung chắn góc 240° → <b>R√3</b>"],
    ], [180, 120, CONTENT_W - 300], font=8.2))
    s.append(SP(4))
    s.append(box("Khi giải bài toán có <b>đổi chiều</b>, luôn tách thành từng đoạn rồi cộng <b>độ lớn</b> "
                 "để tính quãng đường; còn độ dịch chuyển thì chỉ lấy <b>vị trí cuối trừ vị trí đầu</b>. "
                 "Ví dụ: đi +4 m rồi −6 m → s = 10 m, Δx = −2 m.", "thi"))

    # ================================================================= BÀI 5
    s.append(CondPageBreak(150))
    s.append(H2("Bài 5. Tốc độ và vận tốc"))
    s.append(H3("1. Ba đại lượng và công thức"))
    s.append(table([
        ["Đại lượng", "Công thức", "Đơn vị", "Đặc điểm"],
        ["<b>Tốc độ trung bình</b>", "v<sub>tb</sub> = s / Δt", "m/s (hoặc km/h)",
         "<b>Vô hướng</b>, cho biết mức độ <b>nhanh – chậm</b> của chuyển động trên cả quãng đường"],
        ["<b>Tốc độ tức thời</b>", "v = Δs / Δt với Δt <b>rất nhỏ</b>", "m/s",
         "Cho biết tốc độ tại <b>một thời điểm</b>; là độ lớn của vận tốc tức thời"],
        ["<b>Vận tốc trung bình</b>", "v<sub>tb</sub> = Δd / Δt (vectơ)", "m/s",
         "<b>Vectơ</b>, cho biết cả <b>độ nhanh chậm và hướng</b> chuyển động"],
    ], [96, 118, 66, CONTENT_W - 280], font=8.0))
    s.append(SP(4))
    s.append(formula("1 m/s = 3,6 km/h    ⇔    1 km/h = 1/3,6 m/s ≈ 0,278 m/s"))
    s.append(SP(2))
    s.append(P("<b>Chuyển động thẳng đều:</b> vận tốc không đổi về độ lớn và hướng; "
               "quãng đường <b>s = v·t</b>; đồ thị s–t là một đường thẳng."))

    s.append(H3("2. Phân biệt tốc độ và vận tốc"))
    s.append(table([
        ["", "Tốc độ", "Vận tốc"],
        ["Loại đại lượng", "Vô hướng", "Vectơ"],
        ["Dấu", "Luôn ≥ 0", "Có thể âm (tuỳ chiều dương đã chọn)"],
        ["Cho biết", "Chỉ <b>nhanh hay chậm</b>", "Nhanh/chậm <b>và hướng</b>"],
        ["Ví dụ", "Xe chạy 60 km/h", "Xe chạy 60 km/h <b>về phía bắc</b>"],
    ], [80, 190, CONTENT_W - 270], font=8.2))
    s.append(SP(4))
    s.append(box("Đi 100 m rồi quay lại: tốc độ trung bình <b>khác 0</b>, nhưng vận tốc trung bình <b>bằng 0</b>. "
                 "Đây là câu hỏi “ăn điểm” quen thuộc.", "bay"))

    s.append(H3("3. Công thức cộng vận tốc"))
    s.append(formula("v̅<sub>13</sub> = v̅<sub>12</sub> + v̅<sub>23</sub>"))
    s.append(P("Trong đó: <b>1</b> – vật cần tính vận tốc; <b>2</b> – hệ quy chiếu chuyển động; "
               "<b>3</b> – hệ quy chiếu đứng yên. "
               "v₁₃ là <b>vận tốc tuyệt đối</b>, v₁₂ là <b>vận tốc tương đối</b>, "
               "v₂₃ là <b>vận tốc kéo theo</b>."))
    s.append(table([
        ["Trường hợp", "Độ lớn", "Hướng của v₁₃"],
        ["Cùng phương, <b>cùng chiều</b>", "v₁₃ = v₁₂ + v₂₃", "Cùng hướng với cả hai"],
        ["Cùng phương, <b>ngược chiều</b>", "v₁₃ = |v₁₂ − v₂₃|",
         "Cùng hướng với vectơ có <b>độ lớn lớn hơn</b>"],
        ["<b>Vuông góc</b>", "v₁₃ = √(v₁₂² + v₂₃²)", "Hợp với v₁₂ góc α với tanα = v₂₃/v₁₂"],
        ["Hợp với nhau góc α bất kì", "v₁₃ = √(v₁₂² + v₂₃² + 2v₁₂v₂₃cosα)", "Theo quy tắc hình bình hành"],
    ], [126, 190, CONTENT_W - 316], font=8.0))
    s.append(SP(4))
    s.append(box("Thuyền – nước – bờ: <b>v(thuyền/bờ) = v(thuyền/nước) + v(nước/bờ)</b>.<br/>"
                 "• Xuôi dòng: <b>cộng</b> (5 + 3 = 8 m/s). • Ngược dòng: <b>trừ</b> (5 − 3 = 2 m/s). "
                 "• Qua sông vuông góc: <b>Pitago</b> (√(5² + 3²) ≈ 5,8 m/s).", "meo"))

    s.append(H3("4. Ví dụ mẫu"))
    s.append(P("<b>Ví dụ 1.</b> Một ô tô đi nửa quãng đường đầu với 60 km/h, nửa quãng đường sau với 40 km/h. "
               "Tính tốc độ trung bình trên cả quãng đường."))
    s.append(P("<b>Giải.</b> Gọi nửa quãng đường là s. Thời gian: t₁ = s/60; t₂ = s/40. "
               "v<sub>tb</sub> = 2s/(s/60 + s/40) = 2/(1/60 + 1/40) = <b>48 km/h</b> — <b>không phải</b> "
               "trung bình cộng (50 km/h)."))
    s.append(P("<b>Ví dụ 2.</b> Một ca nô chạy với tốc độ 12 km/h so với nước, nước chảy với 4 km/h. "
               "Tính vận tốc ca nô so với bờ khi xuôi dòng và khi ngược dòng."))
    s.append(P("<b>Giải.</b> Xuôi dòng: 12 + 4 = <b>16 km/h</b>. Ngược dòng: |12 − 4| = <b>8 km/h</b>."))
    s.append(box("• Tốc độ trung bình <b>không bằng</b> trung bình cộng các tốc độ (trừ khi các đoạn có "
                 "<b>cùng thời gian</b>).<br/>"
                 "• Nếu hai đoạn có cùng <b>thời gian</b> thì v<sub>tb</sub> = (v₁ + v₂)/2; nếu cùng "
                 "<b>quãng đường</b> thì v<sub>tb</sub> = 2v₁v₂/(v₁ + v₂).", "bay"))

    # ================================================================= BÀI 6
    s.append(CondPageBreak(150))
    s.append(H2("Bài 6. Thực hành: Đo tốc độ của vật chuyển động"))
    s.append(box("<b>Chuyên đề này có trong đặc tả nhưng KHÔNG xuất hiện trong ma trận</b> — nghĩa là "
                 "không có câu hỏi trực tiếp. Chỉ cần đọc 1 trang này để phòng khi câu hỏi được lồng "
                 "ghép vào bài thực hành khác.", "thi", "MỨC ĐỘ XUẤT HIỆN"))
    s.append(H3("1. Hai phương án đo tốc độ"))
    s.append(table([
        ["Phương án", "Cách làm", "Ưu điểm", "Nhược điểm"],
        ["<b>1. Đồng hồ bấm giây</b> + thước",
         "Đo quãng đường s bằng thước; bấm đồng hồ khi vật xuất phát và khi tới đích; v = s/t",
         "Dễ thiết kế, đơn giản, rẻ tiền",
         "Sai số lớn do phản xạ bấm đồng hồ không khớp thời điểm xuất phát/kết thúc"],
        ["<b>2. Cổng quang điện</b> + đồng hồ đo thời gian hiện số",
         "Đặt 2 cổng cách nhau quãng đường s; vật đi qua cổng 1 thì đồng hồ chạy, qua cổng 2 thì dừng",
         "<b>Chính xác cao</b>, sai số nhỏ, đo được tới phần nghìn giây, loại bỏ sai số do con người",
         "Thiết bị <b>đắt</b>, cồng kềnh, lắp đặt phức tạp"],
    ], [96, 170, 105, CONTENT_W - 371], font=7.9))
    s.append(SP(5))
    s.append(H3("2. Những điểm cần nhớ"))
    s.extend(BULL([
        "<b>Ý nghĩa của hai cổng quang điện:</b> cổng thứ nhất đánh dấu <b>thời điểm bắt đầu</b>, "
        "cổng thứ hai đánh dấu <b>thời điểm kết thúc</b> → đo được khoảng thời gian vật đi hết quãng đường giữa hai cổng.",
        "Đo <b>tốc độ tức thời</b> tại một cổng: cho vật (viên bi) đi qua cổng, đo đường kính d của vật "
        "bằng thước kẹp; <b>v = d/t</b> (t là thời gian vật chắn cổng quang).",
        "Các chế độ của đồng hồ hiện số: <b>A</b> (đo thời gian qua cổng A), <b>B</b> (qua cổng B), "
        "<b>A+B</b> (tổng hai khoảng thời gian), <b>A↔B</b> (khoảng thời gian giữa hai cổng).",
        "Nguyên lí cổng quang: đèn phát tia hồng ngoại + cảm biến; vật cắt tia → tín hiệu bật/tắt đồng hồ.",
        "<b>Nguồn sai số:</b> thao tác đo quãng đường, sai số dụng cụ đo thời gian, vật không đi đúng "
        "phương chuyển động. <b>Cách giảm:</b> đo nhiều lần rồi lấy trung bình, đo cẩn thận.",
    ]))
    s.append(PageBreak())
    return s
