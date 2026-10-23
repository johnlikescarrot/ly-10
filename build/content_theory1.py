# -*- coding: utf-8 -*-
"""PHẦN A – Lý thuyết chuyên đề 1 → 5."""

from reportlab.lib.units import cm
from doc_kit import *  # noqa


def build(d: Doc):
    # ================================================================= PART A
    d.pb()
    d.h1("LÝ THUYẾT TRỌNG TÂM – 10 CHUYÊN ĐỀ", kicker="Phần A")
    d.lead("Học theo thứ tự ưu tiên: chắc 2.5 trước, rồi 2.2 – 2.6, cuối cùng là phần mở đầu.")
    d.p("Mỗi chuyên đề gồm: khung <b>Cần nhớ</b> (khái niệm + công thức), <b>Ví dụ mẫu</b> có lời giải từng bước, "
        "<b>Bẫy thường gặp</b> và <b>Mẹo nhớ</b>. Hãy học theo vòng lặp: đọc → gấp tài liệu → tự viết lại công thức "
        "trên giấy nháp → mở ra kiểm tra. Làm được 3 vòng như vậy, công thức sẽ “thuộc tay”.")

    d.h2("Bản đồ 10 chuyên đề và trọng số")
    d.table(
        ["#", "Chuyên đề", "Số đơn vị hỏi", "Mức cao nhất", "Ưu tiên"],
        [
            ["01", "Làm quen với Vật lí", "1", "Nhận biết", "★"],
            ["02", "Quy tắc an toàn phòng thực hành", "2", "Thông hiểu", "★"],
            ["03", "Sai số phép đo – ghi kết quả", "1", "Thông hiểu", "★★"],
            ["04", "Độ dịch chuyển và quãng đường", "3", "Thông hiểu", "★★"],
            ["05", "Tốc độ và vận tốc", "5", "Vận dụng (P.IV)", "★★★★"],
            ["06", "Thực hành đo tốc độ", "0 (nằm trong đặc tả)", "Thông hiểu", "★"],
            ["07", "Đồ thị độ dịch chuyển – thời gian", "4", "Thông hiểu", "★★★"],
            ["08", "Chuyển động biến đổi. Gia tốc", "2", "Thông hiểu", "★★"],
            ["09", "Chuyển động thẳng biến đổi đều", "9", "Vận dụng (P.IV)", "★★★★★"],
            ["10", "Sự rơi tự do", "4", "Thông hiểu", "★★★"],
        ],
        widths=[1.0 * cm, 7.2 * cm, 3.0 * cm, 3.4 * cm, 2.4 * cm],
        aligns=["C", "L", "C", "C", "C"], font_size=8.2)
    d.p("<i>Chuyên đề 06 (thực hành đo tốc độ) có trong đặc tả nhưng không có câu riêng trong ma trận; "
        "nội dung của nó được hỏi lồng trong chuyên đề 05 và 07 (cách đo, ưu nhược điểm cổng quang điện).</i>", "Small")
    d.box("tip",
          "Thứ tự ôn tối ưu: <b>09 → 05 → 10 → 07 → 04 → 03 → 08 → 02 → 01</b>. "
          "Hai chuyên đề 09 và 05 chiếm gần 40% số đơn vị hỏi và toàn bộ phần tự luận vận dụng.",
          title="THỨ TỰ ÔN KHUYẾN NGHỊ")

    d.h2("Mạch kiến thức: học theo dòng chảy, không học rời rạc")
    d.table(
        ["Chặng", "Câu hỏi trung tâm", "Chuyên đề", "Sản phẩm bạn phải có"],
        [
            ["<b>1. Đo đạc</b>", "Làm sao biết một đại lượng chính xác đến đâu?",
             "01 – 02 – 03", "Biết đọc dụng cụ, ghi kết quả kèm sai số"],
            ["<b>2. Mô tả chuyển động</b>", "Vật ở đâu, đi bao xa, nhanh hay chậm?",
             "04 – 05 – 06", "Phân biệt được quãng đường / độ dịch chuyển, tốc độ / vận tốc"],
            ["<b>3. Biểu diễn chuyển động</b>", "Đồ thị kể câu chuyện gì?",
             "07", "Đọc – vẽ – tính được từ đồ thị d–t"],
            ["<b>4. Giải thích sự biến đổi</b>", "Vì sao vận tốc thay đổi?",
             "08 – 09 – 10", "Dùng 4 công thức CĐTBĐĐ và 3 công thức rơi tự do"],
        ],
        widths=[3.4 * cm, 5.6 * cm, 2.9 * cm, 5.4 * cm], font_size=8.2)

    # ================================================================= BÀI 1
    d.h1("LÀM QUEN VỚI VẬT LÍ", kicker="Chuyên đề 01 · Bài 1 SGK · 1 đơn vị hỏi (Nhận biết)")

    d.h2("1.1 · Đối tượng nghiên cứu của Vật lí")
    d.p("Vật lí nghiên cứu <b>các sự vật, hiện tượng của tự nhiên</b> ở mức độ đơn giản nhất: các dạng vận động "
        "của vật chất, năng lượng và sự tương tác giữa chúng. Nói ngắn gọn: Vật lí trả lời câu hỏi "
        "<b>“thế giới vận hành như thế nào”</b> ở tầng cơ bản nhất.")
    d.table(
        ["Lĩnh vực", "Đối tượng nghiên cứu", "Ví dụ ứng dụng"],
        [
            ["Cơ học", "Chuyển động, lực, cân bằng", "Ô tô, cầu, máy bay"],
            ["Nhiệt học", "Nhiệt độ, sự truyền nhiệt, động cơ nhiệt", "Điều hoà, tủ lạnh, động cơ"],
            ["Điện – từ học", "Điện tích, dòng điện, từ trường", "Máy phát điện, động cơ điện, sóng wifi"],
            ["Quang học", "Ánh sáng, thấu kính, hiện tượng quang", "Kính hiển vi, camera, cáp quang"],
            ["Vật lí hạt nhân", "Cấu trúc hạt nhân, phóng xạ", "Điện hạt nhân, y học hạt nhân"],
            ["Thiên văn", "Hành tinh, sao, vũ trụ", "Vệ tinh, dự báo thời tiết"],
        ],
        widths=[3.3 * cm, 7.2 * cm, 6.6 * cm])

    d.box("remember",
          "• Đối tượng của Vật lí là <b>tự nhiên – vật chất – năng lượng</b>, không phải con người, xã hội, "
          "lịch sử hay sinh vật ở góc độ sinh học.\n\n"
          "• Vật lí là <b>khoa học thực nghiệm</b>: mọi kết luận phải được kiểm chứng bằng thí nghiệm hoặc "
          "quan sát, không dựa vào cảm tính.",
          title="CẦN NHỚ")

    d.h2("1.2 · Bốn cuộc cách mạng công nghiệp gắn với thành tựu Vật lí")
    d.table(
        ["Cuộc CMCN", "Thời gian", "Thành tựu Vật lí then chốt", "Công nghệ tiêu biểu"],
        [
            ["<b>Lần 1</b>", "Cuối TK XVIII", "Cơ học Newton, nhiệt động lực học", "Máy hơi nước, đầu máy xe lửa"],
            ["<b>Lần 2</b>", "Cuối TK XIX – đầu TK XX", "Điện từ học (Faraday – Maxwell)", "Động cơ điện, máy phát điện, điện thoại"],
            ["<b>Lần 3</b>", "Khoảng 1970", "Vật lí chất rắn, bán dẫn, lượng tử", "Transistor, máy tính, laser, tự động hoá"],
            ["<b>Lần 4</b>", "Đầu TK XXI", "Vật liệu mới, cảm biến, công nghệ lượng tử", "AI, IoT, big data, năng lượng tái tạo"],
        ],
        widths=[2.3 * cm, 3.5 * cm, 6.0 * cm, 5.3 * cm], font_size=8.2)
    d.p("Cần nhớ <b>cặp “thành tựu – công nghệ”</b>: hơi nước → CMCN 1; điện → CMCN 2; điện tử – máy tính → CMCN 3; "
        "số hoá – trí tuệ nhân tạo → CMCN 4.")

    d.h2("1.3 · Phương pháp nghiên cứu Vật lí")
    d.p("Vật lí dùng hai phương pháp bổ trợ nhau:")
    d.bullets([
        "<b>Phương pháp thực nghiệm:</b> quan sát hiện tượng → đặt câu hỏi → xây dựng giả thuyết → thiết kế "
        "phương án thí nghiệm → tiến hành, thu thập và xử lí số liệu → kết luận (chấp nhận hoặc bác bỏ giả thuyết).",
        "<b>Phương pháp lí thuyết:</b> dùng mô hình, định luật, công cụ toán học để suy luận, dự đoán kết quả "
        "rồi đối chiếu với thực nghiệm.",
    ])
    d.table(
        ["Bước", "Nội dung", "Ví dụ: nghiên cứu sự rơi"],
        [
            ["1. Quan sát", "Ghi nhận hiện tượng cần tìm hiểu", "Vật nặng rơi nhanh hơn vật nhẹ?"],
            ["2. Câu hỏi – giả thuyết", "Đặt câu hỏi, nêu dự đoán có thể kiểm chứng", "Nếu bỏ qua lực cản thì mọi vật rơi như nhau"],
            ["3. Thí nghiệm", "Thiết kế, tiến hành, đo đạc", "Thả bi và lông chim trong ống hút chân không"],
            ["4. Xử lí – kết luận", "Phân tích số liệu, rút ra quy luật", "Hai vật chạm đáy cùng lúc"],
            ["5. Báo cáo", "Trình bày, kiểm tra chéo, ứng dụng", "Viết báo cáo, mở rộng cho chuyển động rơi tự do"],
        ],
        widths=[3.0 * cm, 6.6 * cm, 7.5 * cm], font_size=8.2)

    d.h2("1.4 · Vai trò của Vật lí")
    d.bullets([
        "Là <b>nền tảng</b> của nhiều ngành khoa học: hoá học, sinh học, thiên văn, địa chất.",
        "Là <b>cơ sở</b> của kĩ thuật – công nghệ: điện, điện tử, giao thông, năng lượng, vật liệu.",
        "Ứng dụng trực tiếp trong <b>y học</b> (X-quang, MRI, xạ trị), <b>nông nghiệp</b>, <b>môi trường</b>, "
        "<b>an ninh – quốc phòng</b>.",
        "Góp phần hình thành <b>tư duy khoa học</b>: khách quan, logic, biết đặt giả thuyết và kiểm chứng.",
    ])

    d.box("example",
          "<b>Ví dụ.</b> Công trình nào sau đây là thành tựu của Vật lí gắn với cuộc cách mạng công nghiệp lần thứ ba?\n"
          "A. Máy hơi nước.   B. Máy phát điện.   C. Transistor bán dẫn.   D. Trí tuệ nhân tạo.\n\n"
          "<b>Giải.</b> CMCN lần 3 gắn với điện tử – máy tính – bán dẫn → chọn <b>C</b>. Máy hơi nước là CMCN 1, "
          "máy phát điện là CMCN 2, trí tuệ nhân tạo là CMCN 4.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Nhầm “đối tượng nghiên cứu của Vật lí” với của Hoá học (chất, phản ứng) hay Sinh học (sự sống).\n"
          "• Nhầm mốc của các cuộc cách mạng công nghiệp – hãy nhớ theo cặp <b>hơi nước – điện – điện tử – số hoá</b>.\n"
          "• Cho rằng Vật lí chỉ là lí thuyết suông: Vật lí là khoa học thực nghiệm, kết luận phải kiểm chứng.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip", "<b>“1 – 2 – 3 – 4”</b>: Một quy trình, Hai phương pháp, Ba nhóm ứng dụng (khoa học – kĩ thuật – đời sống), "
                "Bốn cuộc cách mạng. Câu hỏi bài này hầu như chỉ hỏi đúng 4 ý đó.", title="MẸO NHỚ")

    # ================================================================= BÀI 2
    d.h1("CÁC QUY TẮC AN TOÀN TRONG PHÒNG THỰC HÀNH", kicker="Chuyên đề 02 · Bài 2 SGK · 2 đơn vị hỏi (1 Biết + 1 Hiểu)")

    d.h2("2.1 · Nguy cơ mất an toàn trong phòng thực hành")
    d.table(
        ["Nhóm nguy cơ", "Tình huống điển hình", "Cách phòng tránh"],
        [
            ["<b>Điện</b>", "Chạm dây hở, tay ướt cầm phích cắm, dùng quá hiệu điện thế", "Kiểm tra dây, khô tay, ngắt nguồn khi sửa"],
            ["<b>Nhiệt</b>", "Bỏng khi đun, chạm bếp, đèn cồn cháy", "Kẹp gắp, găng chịu nhiệt, không để gần vật dễ cháy"],
            ["<b>Hoá chất</b>", "Chất ăn mòn, độc, bay hơi", "Găng, kính, tủ hút, không nếm – ngửi trực tiếp"],
            ["<b>Bức xạ</b>", "Tia laser, tia tử ngoại, nguồn phóng xạ", "Kính bảo hộ, tấm chắn, giảm thời gian tiếp xúc"],
            ["<b>Cơ học</b>", "Vật nặng rơi, dụng cụ sắc nhọn, thuỷ tinh vỡ", "Sắp xếp gọn, dùng găng, thu dọn đúng cách"],
            ["<b>Cháy nổ</b>", "Đèn cồn bị đổ, bình khí nén", "Không để lửa gần hoá chất dễ cháy, biết vị trí bình cứu hoả"],
        ],
        widths=[2.6 * cm, 7.0 * cm, 7.5 * cm], font_size=8.2)

    d.h2("2.2 · Các quy tắc an toàn")
    d.p("Hãy nhớ theo <b>ba thời điểm: TRƯỚC – TRONG – SAU</b> buổi thực hành.")
    d.table(
        ["Thời điểm", "Quy tắc"],
        [
            ["<b>Trước</b>", "Đọc kĩ hướng dẫn và hiểu rõ thiết bị; kiểm tra dụng cụ, dây dẫn, nguồn điện; "
             "mặc áo bảo hộ, đeo kính, buộc gọn tóc; chỉ bắt đầu khi có sự đồng ý của giáo viên."],
            ["<b>Trong</b>", "Làm đúng trình tự; không tự ý thay đổi thí nghiệm; không ăn uống, không đùa nghịch; "
             "không dùng tay ướt chạm công tắc; không ngửi, nếm hoá chất; giữ khoảng cách với nguồn nhiệt, tia laser."],
            ["<b>Sau</b>", "Ngắt điện, tắt thiết bị; thu dọn, vệ sinh dụng cụ; đổ chất thải đúng nơi quy định; "
             "rửa tay; báo cáo sự cố cho giáo viên."],
        ],
        widths=[2.4 * cm, 14.7 * cm], font_size=8.4)

    d.h2("2.3 · Biển báo an toàn – nhận diện trong 2 giây")
    d.table(
        ["Nhóm biển báo", "Hình dạng – màu sắc", "Ý nghĩa", "Ví dụ"],
        [
            ["<b>Cấm</b>", "Hình tròn, viền đỏ, nền trắng, gạch chéo đỏ", "Cấm một hành vi", "Cấm lửa, cấm hút thuốc, cấm ăn uống"],
            ["<b>Cảnh báo nguy hiểm</b>", "Hình tam giác đều, viền đen, nền vàng", "Chú ý nguy cơ", "Điện cao áp, chất độc, dễ cháy, laser"],
            ["<b>Bắt buộc</b>", "Hình tròn, nền xanh, ký hiệu trắng", "Phải thực hiện", "Đeo kính, đeo găng, đội mũ"],
            ["<b>Chỉ dẫn / an toàn</b>", "Hình chữ nhật/vuông, nền xanh lá", "Chỉ nơi, lối thoát, thiết bị an toàn", "Lối thoát hiểm, bình cứu hoả, vòi rửa mắt"],
        ],
        widths=[3.3 * cm, 5.2 * cm, 3.6 * cm, 5.0 * cm], font_size=8.2)
    d.box("tip", "<b>“Đỏ tròn – CẤM; Vàng tam giác – CẢNH BÁO; Xanh tròn – BẮT BUỘC; Xanh lá – CHỈ DẪN.”</b> "
                "Chỉ cần nhớ 4 cụm màu – hình là làm được câu hỏi biển báo.", title="MẸO NHỚ")

    d.h2("2.4 · Sử dụng thiết bị thí nghiệm")
    d.bullets([
        "<b>Đồng hồ đo thời gian hiện số:</b> chọn chế độ đo (MODE), chọn thang thời gian (ms/s), nhấn RESET về 0 "
        "trước mỗi lần đo, đọc kết quả trên màn hình số.",
        "<b>Cổng quang điện:</b> gồm bộ phát tia hồng ngoại và bộ thu; khi vật đi qua che chùm tia, bộ thu mất tín hiệu "
        "và đồng hồ ghi nhận thời điểm → đo được thời gian chuyển động giữa hai cổng.",
        "<b>Ampe kế – vôn kế:</b> mắc ampe kế <b>nối tiếp</b>, vôn kế <b>song song</b>; chọn thang đo lớn hơn giá trị cần đo; "
        "kiểm tra chiều dòng điện và cực (+) (–).",
        "<b>Dụng cụ đo độ dài, khối lượng, nhiệt độ:</b> đọc theo ĐCNN, mắt nhìn vuông góc với vạch chia để tránh sai số thị sai.",
    ])

    d.box("example",
          "<b>Ví dụ.</b> Trước khi tiến hành thí nghiệm với đèn cồn, học sinh cần làm gì?\n"
          "A. Đổ đầy cồn lên miệng đèn.   B. Kiểm tra bấc, mức cồn và để xa vật dễ cháy.\n"
          "C. Dùng đèn cồn để hơ trực tiếp ống nghiệm.   D. Thổi tắt đèn bằng miệng.\n\n"
          "<b>Giải.</b> B – kiểm tra lượng cồn (không quá 2/3 bầu), bấc phẳng, khu vực xung quanh không có vật dễ cháy. "
          "Không đổ cồn khi đèn đang cháy, không thổi tắt bằng miệng (dùng nắp đậy).",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Nhầm <b>biển cảnh báo (tam giác vàng)</b> với <b>biển cấm (tròn đỏ)</b> – đây là bẫy phổ biến nhất.\n"
          "• Câu hỏi “hành vi nào SAI/không an toàn” thường có 3 phương án đúng hiển nhiên và 1 phương án nguy hiểm "
          "(nếm hoá chất, dùng tay ướt, tự ý đổi thí nghiệm). Đọc kĩ chữ <b>“sai”</b> hoặc <b>“không”</b>.",
          title="BẪY THƯỜNG GẶP")

    # ================================================================= BÀI 3
    d.h1("THỰC HÀNH TÍNH SAI SỐ TRONG PHÉP ĐO", kicker="Chuyên đề 03 · Bài 3 SGK · 1 đơn vị hỏi + kỹ năng nền cho mọi bài toán")

    d.h2("3.1 · Phép đo trực tiếp và phép đo gián tiếp")
    d.table(
        ["Loại phép đo", "Định nghĩa", "Ví dụ"],
        [
            ["<b>Trực tiếp</b>", "So sánh trực tiếp đại lượng cần đo với dụng cụ đo, đọc kết quả ngay trên dụng cụ.",
             "Đo chiều dài bằng thước, đo thời gian bằng đồng hồ, đo khối lượng bằng cân."],
            ["<b>Gián tiếp</b>", "Đo các đại lượng trực tiếp rồi <b>tính</b> đại lượng cần tìm qua công thức.",
             "Đo vận tốc: đo s bằng thước, t bằng đồng hồ rồi tính v = s/t. Đo khối lượng riêng D = m/V."],
        ],
        widths=[3.2 * cm, 7.6 * cm, 6.3 * cm], font_size=8.4)

    d.h2("3.2 · Hai loại sai số")
    d.table(
        ["Tiêu chí", "Sai số hệ thống", "Sai số ngẫu nhiên"],
        [
            ["Nguyên nhân", "Dụng cụ không chuẩn, điểm 0 lệch, thang chia sai, cách đọc lệch hệ thống",
             "Thao tác, phản xạ bấm giây, rung lắc, nhiệt độ, gió, ánh sáng"],
            ["Quy luật", "Lặp lại như nhau ở mọi lần đo, <b>cùng một phía</b>",
             "Không theo quy luật, lúc cao lúc thấp"],
            ["Cách giảm", "Hiệu chỉnh dụng cụ, kiểm tra điểm 0, chọn dụng cụ phù hợp",
             "Đo <b>nhiều lần</b> rồi lấy trung bình"],
        ],
        widths=[2.8 * cm, 7.4 * cm, 7.9 * cm], font_size=8.3)
    d.p("<b>Nguyên nhân gây sai số khác:</b> giới hạn của dụng cụ (ĐCNN), giác quan người đo, điều kiện môi trường, "
        "đại lượng đo không ổn định.")

    d.h2("3.3 · Bộ công thức bắt buộc")
    d.f("Ā = (A_1 + A_2 + … + A_n) / n", "giá trị trung bình của n lần đo")
    d.f("ΔA_i = |Ā − A_i|", "sai số tuyệt đối của lần đo thứ i")
    d.f("ΔĀ = (ΔA_1 + ΔA_2 + … + ΔA_n) / n", "sai số ngẫu nhiên trung bình")
    d.f("ΔA = ΔĀ + ΔA_dc", "sai số tuyệt đối của phép đo (ΔA_dc là sai số dụng cụ)")
    d.f("δA = (ΔA / Ā) · 100%", "sai số tỉ đối – cho biết độ chính xác tương đối")
    d.p("<b>Sai số dụng cụ</b> ΔA(dc) thường lấy bằng <b>một độ chia nhỏ nhất (ĐCNN)</b> của dụng cụ "
        "(một số tài liệu lấy nửa ĐCNN với thước có vạch chia – khi làm bài, hãy theo quy ước giáo viên đã dạy).")

    d.h2("3.4 · Cách ghi kết quả đo")
    d.box("remember",
          "<b>Quy tắc 1.</b> Sai số tuyệt đối chỉ viết <b>1 hoặc 2 chữ số có nghĩa</b> (thường 1 chữ số).\n\n"
          "<b>Quy tắc 2.</b> Giá trị trung bình được làm tròn đến <b>cùng hàng</b> với chữ số có nghĩa cuối của sai số.\n\n"
          "<b>Quy tắc 3.</b> Kết quả luôn viết dạng: <b>A = Ā ± ΔA</b> (kèm đơn vị).\n\n"
          "Ví dụ: ΔA = 0,19 cm → Ā = 12,14 cm → <b>L = 12,14 ± 0,19 cm</b>. "
          "Nếu lấy ΔA = 0,2 cm thì <b>L = 12,1 ± 0,2 cm</b>.",
          title="CẦN NHỚ")

    d.h2("3.5 · Sai số của phép đo gián tiếp")
    d.table(
        ["Phép tính", "Cách tính sai số", "Ghi nhớ"],
        [
            ["Tổng, hiệu: A = x ± y", "ΔA = Δx + Δy", "Cộng sai số tuyệt đối"],
            ["Tích, thương: A = x·y ; A = x/y", "δA = δx + δy", "Cộng sai số tỉ đối"],
            ["Luỹ thừa: A = x^n", "δA = n·δx", "Nhân số mũ"],
            ["Căn bậc hai: A = √x", "δA = ½·δx", "Chia đôi sai số tỉ đối"],
            ["Hằng số: A = k·x", "δA = δx", "Hằng số không gây sai số"],
        ],
        widths=[5.4 * cm, 6.4 * cm, 5.3 * cm], font_size=8.4)

    d.box("example",
          "<b>Ví dụ 1.</b> Đo chiều dài một bút chì bằng thước có ĐCNN 0,1 cm, thu được 5 lần: "
          "12,1; 12,2; 12,0; 12,3; 12,1 (cm). Hãy tính và ghi kết quả.\n\n"
          "<b>Giải.</b>\n"
          "• Trung bình: Ā = (12,1 + 12,2 + 12,0 + 12,3 + 12,1)/5 = <b>12,14 cm</b>.\n"
          "• Sai số từng lần: 0,04; 0,06; 0,14; 0,16; 0,04 (cm) → ΔĀ = 0,44/5 = <b>0,088 cm</b>.\n"
          "• Sai số dụng cụ: ΔA(dc) = 0,1 cm → ΔA = 0,088 + 0,1 = 0,188 ≈ <b>0,19 cm</b>.\n"
          "• Kết quả: <b>L = 12,14 ± 0,19 cm</b>. Sai số tỉ đối: δ = 0,19/12,14 ≈ <b>1,6%</b>.\n\n"
          "<b>Ví dụ 2.</b> Đo tốc độ: s = 2,00 ± 0,01 m; t = 0,50 ± 0,01 s. Tính v và sai số.\n"
          "• v = 2,00/0,50 = 4,00 m/s. δ(s) = 0,5%; δ(t) = 2% → δ(v) = 2,5%.\n"
          "• Δv = 2,5% × 4,00 = 0,10 m/s → <b>v = 4,00 ± 0,10 m/s</b>.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• <b>Quên cộng sai số dụng cụ</b> – thiếu bước ΔA = ΔĀ + ΔA(dc) là mất điểm cả câu.\n"
          "• <b>Làm tròn sai</b>: sai số 0,188 không được viết 0,1880 hay 0,2 khi giá trị trung bình còn 2 chữ số thập phân.\n"
          "• Nhầm <b>sai số tuyệt đối</b> (có đơn vị, cm) với <b>sai số tỉ đối</b> (%, không đơn vị).\n"
          "• Tính trung bình cộng các sai số có dấu: sai số tuyệt đối luôn <b>lấy trị tuyệt đối</b> nên không âm.\n"
          "• Với phép đo gián tiếp dạng tích/thương, <b>không</b> cộng sai số tuyệt đối mà phải cộng sai số tỉ đối.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip",
          "<b>“Cộng trừ thì cộng tuyệt đối – Nhân chia thì cộng tỉ đối – Luỹ thừa n thì nhân n.”</b> "
          "Đọc thành nhịp 3 – 3 – 3 là nhớ.", title="MẸO NHỚ")

    # ================================================================= BÀI 4
    d.h1("ĐỘ DỊCH CHUYỂN VÀ QUÃNG ĐƯỜNG ĐI ĐƯỢC", kicker="Chuyên đề 04 · Bài 4 SGK · 3 đơn vị hỏi (1 Biết + 2 Hiểu)")

    d.h2("4.1 · Vị trí và hệ quy chiếu")
    d.p("Muốn xác định một vật đang ở đâu, ta cần chọn <b>vật mốc</b>, <b>hệ trục toạ độ</b> và <b>gốc thời gian</b> – "
        "gọi chung là <b>hệ quy chiếu</b>. Trên một trục Ox, vị trí của vật được xác định bằng toạ độ x.")

    d.h2("4.2 · Độ dịch chuyển")
    d.box("remember",
          "<b>Độ dịch chuyển</b> là đại lượng <b>vectơ</b> nối vị trí đầu với vị trí cuối của vật: "
          "<b>Δd = d₂ − d₁</b> (trên trục Ox: Δx = x₂ − x₁).\n\n"
          "• Đặc trưng bởi: <b>độ lớn</b> (khoảng cách thẳng từ điểm đầu đến điểm cuối) và <b>hướng</b> (từ điểm đầu đến điểm cuối).\n"
          "• Đơn vị: mét (m).\n"
          "• Có thể <b>dương, âm hoặc bằng 0</b> tuỳ chiều dương đã chọn và vị trí đầu – cuối.\n"
          "• Chỉ phụ thuộc <b>điểm đầu và điểm cuối</b>, không phụ thuộc đường đi.",
          title="CẦN NHỚ")

    d.h2("4.3 · Quãng đường đi được")
    d.p("<b>Quãng đường</b> (kí hiệu s) là <b>độ dài quỹ đạo</b> mà vật đã vạch ra. Đây là đại lượng <b>vô hướng</b>, "
        "luôn <b>không âm</b> và <b>không bao giờ giảm</b> trong quá trình chuyển động.")

    d.h2("4.4 · So sánh – bảng “nhìn một lần là nhớ”")
    d.table(
        ["Tiêu chí", "Độ dịch chuyển (Δd)", "Quãng đường (s)"],
        [
            ["Bản chất", "Đại lượng vectơ", "Đại lượng vô hướng"],
            ["Phụ thuộc", "Điểm đầu và điểm cuối", "Toàn bộ quỹ đạo đã đi"],
            ["Giá trị", "Có thể dương, âm hoặc 0", "Luôn ≥ 0"],
            ["Đơn vị", "mét (m)", "mét (m)"],
            ["Quan hệ", "<b>|Δd| ≤ s</b>; dấu “=” xảy ra khi chuyển động thẳng, không đổi chiều", "s ≥ |Δd|"],
            ["Ý nghĩa", "Vị trí thay đổi bao xa, theo hướng nào", "Đã đi tổng cộng bao xa"],
        ],
        widths=[2.7 * cm, 8.0 * cm, 6.4 * cm], font_size=8.4)
    d.p("<b>Hệ quả cần nhớ:</b> đi rồi quay về điểm xuất phát → s &gt; 0 nhưng <b>Δd = 0</b>. "
        "Đây chính là câu hỏi “đặc điểm nào chỉ có ở quãng đường, không có ở độ dịch chuyển” "
        "(đáp án: <i>không thể bằng 0</i>).")

    d.box("example",
          "<b>Ví dụ 1.</b> Một người đi 3 km về phía đông rồi 4 km về phía bắc. Tính quãng đường và độ dịch chuyển.\n"
          "• Quãng đường: s = 3 + 4 = <b>7 km</b>.\n"
          "• Độ dịch chuyển: hai đoạn vuông góc → |Δd| = √(3² + 4²) = <b>5 km</b>, hướng đông – bắc "
          "(lệch 53° so với hướng đông).\n\n"
          "<b>Ví dụ 2.</b> Vật đi từ A đến B cách 10 m rồi quay lại A.\n"
          "• s = 10 + 10 = <b>20 m</b>; Δd = <b>0</b> (trùng điểm đầu – cuối).\n\n"
          "<b>Ví dụ 3 (vận dụng cao).</b> Trên trục Ox, vật đi từ x = 2 m đến x = 12 m rồi quay lại đến x = 5 m.\n"
          "• s = 10 + 7 = <b>17 m</b>.\n"
          "• Δx = 5 − 2 = <b>+3 m</b> (độ lớn 3 m, hướng theo chiều dương).\n"
          "• Nhận xét: |Δx| = 3 m &lt; s = 17 m vì vật đã đổi chiều.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Nhầm <b>độ lớn độ dịch chuyển</b> với quãng đường trong bài có đổi chiều → sai ngay từ bước đầu.\n"
          "• Cho rằng độ dịch chuyển luôn dương: nếu vật đi ngược chiều dương, Δx &lt; 0.\n"
          "• Đơn vị: km và m lẫn lộn khi tính tổng hợp vectơ – phải đổi về cùng đơn vị.\n"
          "• Câu hỏi “độ dịch chuyển có thể bằng 0 không?” → <b>có</b> (khi trở về vị trí đầu).",
          title="BẪY THƯỜNG GẶP")
    d.box("tip",
          "<b>“Đầu – cuối nối thẳng là dịch chuyển; đi bao xa là quãng đường.”</b>\n"
          "Hình dung: độ dịch chuyển là <b>mũi tên</b> cắm từ điểm xuất phát tới điểm dừng; quãng đường là "
          "<b>sợi dây</b> đo theo vết bánh xe.", title="MẸO NHỚ")

    # ================================================================= BÀI 5
    d.h1("TỐC ĐỘ VÀ VẬN TỐC", kicker="Chuyên đề 05 · Bài 5 SGK · 5 đơn vị hỏi · Có mặt ở cả 4 phần của đề")

    d.h2("5.1 · Tốc độ trung bình")
    d.box("remember",
          "<b>Tốc độ trung bình</b> cho biết mức độ nhanh, chậm của chuyển động, được tính bằng quãng đường "
          "chia cho thời gian đi hết quãng đường đó:\n\n"
          "&nbsp;&nbsp;&nbsp;&nbsp;<b>v = s / Δt</b>&nbsp;&nbsp;&nbsp;(đơn vị: m/s hoặc km/h)\n\n"
          "• Đây là đại lượng <b>vô hướng, không âm</b>.\n"
          "• <b>Tốc độ tức thời</b> là tốc độ tại một thời điểm (hoặc trong khoảng thời gian rất nhỏ): "
          "v = Δs/Δt với Δt → 0. Số chỉ trên đồng hồ tốc kế của xe máy là tốc độ tức thời.",
          title="CẦN NHỚ")
    d.p("<b>Đổi đơn vị:</b> 1 m/s = 3,6 km/h → km/h sang m/s thì <b>chia 3,6</b>; m/s sang km/h thì <b>nhân 3,6</b>. "
        "Đây là bước đổi đơn vị “mất điểm oan” nhiều nhất trong bài kiểm tra.")

    d.h2("5.2 · Vận tốc")
    d.box("remember",
          "<b>Vận tốc trung bình</b> là đại lượng <b>vectơ</b>, đặc trưng cho sự nhanh chậm và <b>hướng</b> chuyển động:\n\n"
          "&nbsp;&nbsp;&nbsp;&nbsp;<b>v = Δd / Δt</b>&nbsp;&nbsp;&nbsp;(v là vectơ; độ lớn v = |Δd| / Δt)\n\n"
          "• <b>Vận tốc tức thời</b> là vectơ vận tốc tại một thời điểm; có phương tiếp tuyến với quỹ đạo, "
          "chiều là chiều chuyển động.\n"
          "• Trên trục Ox: v > 0 khi vật đi theo chiều dương, v &lt; 0 khi đi ngược chiều dương.",
          title="CẦN NHỚ")

    d.h2("5.3 · Phân biệt tốc độ và vận tốc")
    d.table(
        ["Tiêu chí", "Tốc độ", "Vận tốc"],
        [
            ["Loại đại lượng", "Vô hướng", "Vectơ"],
            ["Công thức gốc", "v = s/Δt (quãng đường)", "v = Δd/Δt (độ dịch chuyển, vectơ)"],
            ["Dấu", "Luôn ≥ 0", "Có thể âm, dương hoặc 0"],
            ["Cho biết", "Đi nhanh hay chậm", "Nhanh/chậm và <b>theo hướng nào</b>"],
            ["Trường hợp đặc biệt", "Không bao giờ bằng 0 khi vật đang chuyển động", "Bằng 0 khi vật trở về vị trí đầu"],
        ],
        widths=[3.2 * cm, 6.8 * cm, 7.1 * cm], font_size=8.4)

    d.h2("5.4 · Công thức cộng vận tốc")
    d.p("Kí hiệu: <b>v₁₃</b> là vận tốc của vật (1) so với hệ quy chiếu đứng yên (3); <b>v₁₂</b> là vận tốc của vật (1) "
        "so với hệ quy chiếu chuyển động (2); <b>v₂₃</b> là vận tốc của hệ (2) so với hệ (3).")
    d.f("v_13 = v_12 + v_23", "công thức cộng vận tốc (dạng vectơ) – quy tắc hình bình hành")
    d.table(
        ["Trường hợp", "Công thức độ lớn", "Ví dụ"],
        [
            ["Cùng phương, <b>cùng chiều</b>", "v₁₃ = v₁₂ + v₂₃", "Ca nô xuôi dòng; người đi về phía đầu tàu"],
            ["Cùng phương, <b>ngược chiều</b>", "v₁₃ = |v₁₂ − v₂₃|", "Ca nô ngược dòng; người đi về phía đuôi tàu"],
            ["<b>Vuông góc</b>", "v₁₃ = √(v₁₂² + v₂₃²)", "Ca nô bơi ngang qua sông có nước chảy"],
            ["Hợp với nhau góc α", "v₁₃² = v₁₂² + v₂₃² + 2v₁₂v₂₃·cosα", "Trường hợp tổng quát"],
        ],
        widths=[4.4 * cm, 6.6 * cm, 6.1 * cm], font_size=8.4)
    d.p("Với trường hợp vuông góc, hướng của vận tốc tổng hợp lệch so với v₁₂ một góc α thoả "
        "<b>tanα = v₂₃/v₁₂</b>.")

    d.h2("5.5 · Cách đo tốc độ")
    d.bullets([
        "Trong đời sống: <b>tốc kế</b> trên xe, camera giao thông, ứng dụng GPS.",
        "Trong phòng thí nghiệm: đo quãng đường bằng <b>thước</b>, đo thời gian bằng <b>đồng hồ hiện số + cổng quang điện</b>, "
        "rồi tính v = s/t.",
    ])

    d.box("example",
          "<b>Ví dụ 1.</b> Một xe đi 60 km trong 1,5 h, nghỉ 0,5 h, sau đó đi tiếp 40 km trong 1 h. Tính tốc độ trung bình.\n"
          "• Tổng quãng đường: s = 60 + 40 = 100 km. Tổng thời gian: Δt = 1,5 + 0,5 + 1 = 3 h.\n"
          "• v = 100/3 ≈ <b>33,3 km/h</b>. (Thời gian nghỉ vẫn tính vào thời gian chuyển động của cả hành trình.)\n\n"
          "<b>Ví dụ 2.</b> Ca nô chạy với vận tốc 8 m/s so với nước, nước chảy 6 m/s so với bờ, ca nô bơi "
          "<b>vuông góc</b> với dòng chảy. Tính vận tốc ca nô so với bờ.\n"
          "• v₁₃ = √(8² + 6²) = <b>10 m/s</b>.\n"
          "• Lệch góc α so với phương bơi: tanα = 6/8 = 0,75 → α ≈ <b>37°</b> về phía hạ lưu.\n\n"
          "<b>Ví dụ 3.</b> Ca nô có vận tốc 36 km/h so với nước, nước chảy 3,6 km/h.\n"
          "• Đổi: 36 km/h = 10 m/s; 3,6 km/h = 1 m/s.\n"
          "• Xuôi dòng: v = 10 + 1 = <b>11 m/s</b>. Ngược dòng: v = 10 − 1 = <b>9 m/s</b>.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• <b>Tốc độ trung bình KHÔNG phải trung bình cộng các tốc độ</b> (chỉ bằng trung bình cộng khi các quãng "
          "đường bằng nhau và thời gian bằng nhau). Luôn dùng công thức s/Δt.\n"
          "• Quên đổi km/h → m/s (chia 3,6) trước khi cộng vectơ.\n"
          "• Nhầm “vận tốc trung bình” (dùng độ dịch chuyển) với “tốc độ trung bình” (dùng quãng đường).\n"
          "• Với bài ngược chiều, phải lấy <b>trị tuyệt đối</b> của hiệu, không được để vận tốc âm.\n"
          "• Với bài vuông góc, không được cộng đại số hai vận tốc.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip",
          "<b>“1 – 2 – 3”</b>: 1 là vật cần tính, 2 là hệ quy chiếu chuyển động, 3 là hệ quy chiếu đứng yên → "
          "luôn viết v₁₃ = v₁₂ + v₂₃.\n"
          "<b>“Xuôi cộng – Ngược trừ – Vuông Pythagore”</b>.", title="MẸO NHỚ")
