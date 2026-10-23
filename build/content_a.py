# -*- coding: utf-8 -*-
"""Nội dung PHẦN 0 và PHẦN 1 (Bài 1 – Bài 5)."""

from dsl import T, F, P, C

DASH = "–"


def blocks_a():
    B = []

    # =====================================================================
    # PHẦN 0
    # =====================================================================
    B += [
        ("h1", "PHẦN 0 · GIẢI MÃ MA TRẬN ĐỀ"),
        P("Tài liệu gốc bạn cung cấp là **ma trận + bản đặc tả** của đề kiểm tra giữa học kì I môn Vật lí 10. "
              "Nó không phải là đề bài, mà là *bản thiết kế* của đề: quy định chính xác bài nào ra mấy câu, ở mức độ "
              "nhận thức nào, thuộc phần trắc nghiệm hay tự luận. Vì vậy, muốn ôn đúng – ôn trúng, việc đầu tiên là "
              "**đọc được bản thiết kế đó**. Toàn bộ Phần 0 dưới đây làm đúng việc ấy."),

        ("h2", "0.1. Đề thi cho biết những gì?"),
        T(
         ["Hạng mục", "Thông tin"],
         [["Môn / Lớp", "Vật lí 10 – Chương trình GDPT 2018"],
          ["Thời điểm", "Kiểm tra giữa học kì I, năm học 2026 – 2027"],
          ["Hình thức", "**70% trắc nghiệm + 30% tự luận**"],
          ["Thời gian", "**50 phút**"],
          ["Cấu trúc", "4 phần: I (18 câu TN 4 lựa chọn) · II (2 câu Đúng–Sai, mỗi câu 4 ý) · III (2 câu trả lời ngắn) · IV (2 câu tự luận)"],
          ["Phạm vi", "Chương I – Mở đầu (3 bài) + Chương II – Động học (7 bài). **Không** có phần Lực và chuyển động."]],
         [26, 74]),
        C("key", "Điều quan trọng nhất",
         "Toàn bộ đề nằm gọn trong **10 đơn vị kiến thức**, và **9 trên 10 đơn vị là Động học** (từ Bài 4 đến Bài 10). "
         "Nói cách khác: học kĩ phần Động học là đã nắm trong tay khoảng **85% số điểm**."),

        ("h2", "0.2. Ma trận hai chiều (nguyên bản, đã chuẩn hoá)"),
        P("Bảng dưới đây là ma trận trong tài liệu gốc, được chuẩn hoá lại cho dễ đọc. Kí hiệu: "
              "**I** = Phần I (TN 4 lựa chọn), **II** = Phần II (Đúng–Sai), **III** = Phần III (trả lời ngắn), "
              "**IV** = Phần IV (tự luận); **NB** = Nhận biết, **TH** = Thông hiểu, **VD** = Vận dụng."),
        T(
         ["Đơn vị kiến thức", "I-NB", "I-TH", "II-NB", "II-TH", "III-NB", "III-TH", "IV-TH", "IV-VD", "Tổng"],
         [["1.1. Làm quen với Vật lí", "1", DASH, DASH, DASH, DASH, DASH, DASH, DASH, "1"],
          ["1.2. Quy tắc an toàn trong phòng thực hành", "1", "1", DASH, DASH, DASH, DASH, DASH, DASH, "2"],
          ["1.3. Sai số trong phép đo. Ghi kết quả đo", "1", DASH, DASH, DASH, DASH, DASH, DASH, DASH, "1"],
          ["2.1. Độ dịch chuyển và quãng đường đi được", "1", "2", DASH, DASH, DASH, DASH, DASH, DASH, "3"],
          ["2.2. Tốc độ và vận tốc", "1", DASH, "2", DASH, "1", DASH, "1", DASH, "5"],
          ["2.3. Đồ thị độ dịch chuyển – thời gian", "1", "1", "2", DASH, DASH, DASH, DASH, DASH, "4"],
          ["2.4. Chuyển động biến đổi. Gia tốc", "1", "1", DASH, DASH, DASH, DASH, DASH, DASH, "2"],
          ["2.5. Chuyển động thẳng biến đổi đều", "2", "1", "2", "2", DASH, DASH, DASH, "2", "9"],
          ["2.6. Sự rơi tự do", "1", "2", DASH, DASH, DASH, "1", DASH, DASH, "4"],
          ["**Tổng**", "**10**", "**8**", "**6**", "**2**", "**1**", "**1**", "**1**", "**2**", "**31**"]],
         [42, 8.2, 8.2, 9.2, 9.2, 10.4, 10.4, 9.2, 9.2, 7],
         size=7.3, align=["LEFT"] + ["CENTER"] * 9),
        C("note", "Đọc bảng này thế nào?",
         "Mỗi con số là **một câu (hoặc một ý) hỏi** về đơn vị kiến thức ở cột dọc, thuộc phần và mức độ ở hàng ngang. "
         "Ví dụ dòng 2.5 – Chuyển động thẳng biến đổi đều: có 2 câu Nhận biết và 1 câu Thông hiểu ở Phần I, "
         "4 ý ở Phần II (2 Biết + 2 Hiểu), và 2 ý Vận dụng ở Phần IV. Cộng lại **9 lượt hỏi – nhiều nhất đề**."),

        ("h2", "0.3. Quy đổi ra thang điểm 10"),
        T(
         ["Phần", "Dạng câu hỏi", "Số câu", "Điểm / câu", "Tổng điểm", "Tỉ lệ"],
         [["**I**", "Trắc nghiệm 4 lựa chọn", "18", "0,25", "4,50", "45%"],
          ["**II**", "Trắc nghiệm Đúng – Sai (4 ý/câu)", "2", "1,00", "2,00", "20%"],
          ["**III**", "Trắc nghiệm trả lời ngắn", "2", "0,25", "0,50", "5%"],
          ["**IV**", "Tự luận", "2", "–", "3,00", "30%"],
          ["**Tổng**", "", "**24 câu + 8 ý**", "", "**10,00**", "**100%**"]],
         [10, 40, 14, 12, 12, 12],
         align=["CENTER", "LEFT", "CENTER", "CENTER", "CENTER", "CENTER"]),
        C("key", "70 / 30 khớp chính xác",
         "Trắc nghiệm (Phần I + II + III) = 4,50 + 2,00 + 0,50 = **7,00 điểm = 70%**. "
         "Tự luận (Phần IV) = **3,00 điểm = 30%**. Con số này xác nhận cách quy đổi trên là đúng, "
         "và cho thấy **Phần IV chỉ có 2 câu nhưng đáng 3 điểm** – tức 1,5 điểm mỗi câu, gấp 6 lần một câu trắc nghiệm."),
        P("**Cách chấm Phần II (Đúng–Sai)** theo đúng quy định của Bộ GD&ĐT áp dụng từ 2025: mỗi câu 4 ý, "
              "chọn đúng 1 ý được 0,10 điểm; đúng 2 ý được 0,25; đúng 3 ý được 0,50; đúng cả 4 ý được 1,00. "
              "Nghĩa là **điểm không chia đều** – làm đúng 3/4 ý vẫn chỉ được nửa số điểm của câu đó."),
        C("warn", "Hệ quả chiến thuật của cách chấm Phần II",
         "Đừng \"bỏ\" một ý chỉ vì khó. Nhưng cũng đừng đoán bừa: nếu chắc chắn 3 ý, hãy suy luận ý còn lại từ "
         "chính 3 ý kia – vì 4 ý trong một câu thường liên quan chặt với nhau. Đúng 4/4 được 1,00 điểm, "
         "đúng 3/4 chỉ được 0,50 – **chênh gấp đôi**."),

        ("h2", "0.4. Trọng số từng bài – học gì trước?"),
        T(
         ["Đơn vị kiến thức", "Số lượt hỏi", "Tỉ lệ", "Ưu tiên"],
         [["2.5. Chuyển động thẳng biến đổi đều", "9", "29,0%", "★★★★★"],
          ["2.2. Tốc độ và vận tốc", "5", "16,1%", "★★★★★"],
          ["2.3. Đồ thị độ dịch chuyển – thời gian", "4", "12,9%", "★★★★"],
          ["2.6. Sự rơi tự do", "4", "12,9%", "★★★★"],
          ["2.1. Độ dịch chuyển và quãng đường", "3", "9,7%", "★★★"],
          ["1.2. Quy tắc an toàn phòng thực hành", "2", "6,5%", "★★"],
          ["2.4. Chuyển động biến đổi. Gia tốc", "2", "6,5%", "★★"],
          ["1.1. Làm quen với Vật lí", "1", "3,2%", "★"],
          ["1.3. Sai số trong phép đo", "1", "3,2%", "★"]],
         [46, 16, 14, 24],
         align=["LEFT", "CENTER", "CENTER", "CENTER"]),
        C("tip", "Quy tắc 80/20 áp dụng cho đề này",
         "Ba bài **2.5 – 2.2 – 2.3** chiếm **18/31 lượt hỏi (58%)** và gần như toàn bộ 3 điểm tự luận. "
         "Nếu chỉ còn một buổi tối để ôn, hãy học đúng ba bài này."),

        ("h2", "0.5. Chiến lược làm bài trong 50 phút"),
        T(
         ["Thứ tự", "Việc cần làm", "Thời gian", "Mẹo"],
         [["1", "Phần I – 18 câu trắc nghiệm", "18 – 20 phút", "Làm một lượt, câu nào quá 60 giây thì đánh dấu bỏ qua"],
          ["2", "Phần III – 2 câu trả lời ngắn", "4 phút", "Đọc kỹ đơn vị và số chữ số thập phân đề yêu cầu"],
          ["3", "Phần II – 2 câu Đúng–Sai", "8 phút", "Mỗi câu 4 phút: đọc hết 4 ý rồi mới phán đoán"],
          ["4", "Phần IV – 2 câu tự luận", "16 phút", "Câu 1 (8 phút) → Câu 2 (8 phút); luôn viết công thức trước khi thay số"],
          ["5", "Rà soát", "2 phút", "Kiểm tra phiếu tô, đơn vị, dấu của gia tốc"]],
         [10, 38, 20, 50],
         align=["CENTER", "LEFT", "CENTER", "LEFT"]),
        C("warn", "Ba sai lầm khiến mất điểm oan",
         "**(1)** Đổi đơn vị sai: 54 km/h phải là 15 m/s, không phải 54. "
         "**(2)** Quên dấu gia tốc trong chuyển động chậm dần đều – dẫn đến quãng đường sai hoàn toàn. "
         "**(3)** Trình bày tự luận chỉ có đáp số: mất điểm trình bày dù kết quả đúng."),

        ("h2", "0.6. Lộ trình ôn 7 ngày"),
        T(
         ["Ngày", "Nội dung", "Mục tiêu kiểm chứng"],
         [["1", "Bài 1, 2, 3 (Chương I)", "Nhớ 4 cuộc cách mạng công nghiệp; 9 quy tắc an toàn; viết đúng A = Ā ± ΔA"],
          ["2", "Bài 4, 5 (Độ dịch chuyển, Tốc độ – Vận tốc)", "Phân biệt s và Δd; đổi km/h ↔ m/s thành thạo; cộng vận tốc"],
          ["3", "Bài 6, 7 (Thực hành, Đồ thị)", "Đọc độ dốc ra vận tốc; đọc MODE đồng hồ hiện số"],
          ["4", "Bài 8, 9 (Gia tốc, CĐTBĐ)", "Viết đúng 4 công thức; xác định dấu a; giải bài hãm phanh"],
          ["5", "Bài 10 (Rơi tự do) + ôn lại 8, 9", "Ba công thức rơi tự do; bài toán thả vật – ném xuống"],
          ["6", "Làm trọn đề minh hoạ (Phần 3)", "Bấm giờ 50 phút, không xem đáp án"],
          ["7", "Chữa đề + đọc lại Phần 2 (bảng công thức, 15 bẫy)", "Ghi ra giấy 5 lỗi mình hay mắc nhất"]],
         [10, 52, 56],
         align=["CENTER", "LEFT", "LEFT"]),
    ]

    # =====================================================================
    # PHẦN 1
    # =====================================================================
    B += [
        ("h1", "PHẦN 1 · LÝ THUYẾT TRỌNG TÂM"),
        P("Mỗi bài dưới đây được trình bày theo cùng một khuôn: **Cần nhớ** (kiến thức tối thiểu) → "
              "**Công thức** (đóng khung) → **Bảng so sánh / phân biệt** → **Mẹo nhớ** → **Bẫy thường gặp** → "
              "**Tự kiểm tra 60 giây**. Phần tự kiểm tra có đáp án ngay bên dưới, hãy che lại và trả lời trước."),

        # ---------------------------------------------------------------- BÀI 1
        ("h2", "Bài 1 · Làm quen với Vật lí"),
        P("*Mức độ xuất hiện trong đề: 1 câu trắc nghiệm – Nhận biết (3,2%).*"),
        ("h3", "1. Đối tượng và mục tiêu của Vật lí"),
        ("bullets", [
            "**Đối tượng nghiên cứu:** các dạng **vận động của vật chất** (chất và trường) và **năng lượng**.",
            "**Các lĩnh vực:** cơ học, điện học, điện từ học, quang học, âm học, nhiệt học, nhiệt động lực học, "
            "vật lí nguyên tử và hạt nhân, vật lí lượng tử, thuyết tương đối.",
            "**Mục tiêu môn Vật lí:** cung cấp kiến thức nền tảng về vật chất – năng lượng; rèn kĩ năng thực nghiệm, "
            "mô hình hoá, tính toán và năng lực giải quyết vấn đề; bồi dưỡng thái độ khoa học, trung thực, khách quan.",
        ]),
        ("h3", "2. Bốn cuộc cách mạng công nghiệp – bảng \"ăn điểm\" của cả nước"),
        T(
         ["Cuộc CMCN", "Thời gian", "Thành tựu Vật lí then chốt", "Đặc trưng"],
         [["**Lần 1**", "Giữa TK XVIII (1765)", "Máy hơi nước của **James Watt**, dựa trên nghiên cứu về **Nhiệt**",
           "Thay thế sức lực cơ bắp bằng sức lực máy móc"],
          ["**Lần 2**", "Cuối TK XIX", "**Faraday** phát hiện hiện tượng **cảm ứng điện từ** (1831) → máy phát điện ra đời",
           "Các thiết bị sử dụng điện xuất hiện ngày càng nhiều"],
          ["**Lần 3**", "Những năm 70 TK XX", "Thành tựu về **điện tử, chất bán dẫn, vi mạch**",
           "**Tự động hoá** các quá trình sản xuất"],
          ["**Lần 4**", "Đầu TK XXI", "**Trí tuệ nhân tạo, robot, internet toàn cầu, công nghệ nano**, thiết bị thông minh",
           "Sản xuất thông minh, vạn vật kết nối"]],
         [13, 22, 40, 35]),
        C("tip", "Mẹo nhớ 4 cuộc cách mạng",
         "Đọc thành một câu: **“MÁY – ĐIỆN – TỰ ĐỘNG – TRÍ TUỆ”**. "
         "Máy hơi nước (lần 1) → Điện (lần 2) → Tự động hoá (lần 3) → Trí tuệ nhân tạo (lần 4). "
         "Bốn từ khoá này đi theo đúng thứ tự 1–2–3–4, không bao giờ lẫn."),
        ("h3", "3. Các mốc phát triển của Vật lí"),
        T(
         ["Thời kì", "Nhân vật tiêu biểu", "Dấu ấn"],
         [["Thời cổ đại (TK III TCN)", "Aristotle (A-ri-xtốt)", "Quan sát và suy luận; từng cho rằng *vật nặng rơi nhanh hơn vật nhẹ* (sai lầm tồn tại gần 2000 năm)"],
          ["Thế kỉ XVII", "**Galilei** (Ga-li-lê)", "Đặt **nền móng phương pháp thực nghiệm**; thí nghiệm về sự rơi và con lắc"],
          ["TK XVII – XVIII", "**Newton**", "Xây dựng **cơ học cổ điển**: ba định luật Newton, định luật vạn vật hấp dẫn"],
          ["Thế kỉ XIX", "**Faraday, Maxwell**; Joule, Carnot, Kelvin", "**Điện từ học**; **nhiệt động lực học**"],
          ["Thế kỉ XX", "**Einstein**; Planck, Bohr…", "**Thuyết tương đối**; **vật lí lượng tử** – mở ra vật lí hiện đại"]],
         [22, 30, 58]),
        ("h3", "4. Hai phương pháp nghiên cứu Vật lí"),
        P("**Phương pháp thực nghiệm** – phương pháp quan trọng nhất, gồm 5 bước:"),
        ("numbers", [
            "Xác định **vấn đề** cần nghiên cứu.",
            "Đề xuất **giả thuyết** (dự đoán khoa học).",
            "Thiết kế **phương án thí nghiệm**.",
            "Tiến hành thí nghiệm, **thu thập số liệu**.",
            "**Xử lí số liệu**, kiểm tra giả thuyết và **rút ra kết luận**.",
        ]),
        P("**Phương pháp mô hình:** xây dựng mô hình (vật lí hoặc toán học) → kiểm tra mô hình bằng thực nghiệm → "
              "dùng mô hình để giải thích, dự đoán hiện tượng. **Phương pháp lí thuyết:** dùng suy luận toán học "
              "trên các định luật đã biết để rút ra hệ quả mới."),
        C("warn", "Bẫy: đừng nhầm người với phương pháp",
         "**Galilei** → phương pháp **thực nghiệm**. **Newton** → cơ học cổ điển (kết hợp cả lí thuyết và thực nghiệm). "
         "Đề hay hỏi: *“Galilei sử dụng phương pháp nào?”* – đáp án luôn là **thực nghiệm**, không phải thống kê hay mô hình."),
        ("qa", [
            ("Thành tựu nào mở đầu cuộc cách mạng công nghiệp lần thứ hai?",
             "Hiện tượng **cảm ứng điện từ** do Faraday phát hiện (1831)."),
            ("Đặc trưng của cuộc cách mạng công nghiệp lần thứ ba là gì?",
             "**Tự động hoá** các quá trình sản xuất, nhờ điện tử – chất bán dẫn – vi mạch."),
            ("Ai đặt nền móng cho phương pháp thực nghiệm?",
             "**Galilei**."),
        ]),

        # ---------------------------------------------------------------- BÀI 2
        ("h2", "Bài 2 · Các quy tắc an toàn trong phòng thực hành Vật lí"),
        P("*Mức độ xuất hiện trong đề: 2 câu trắc nghiệm (1 Nhận biết + 1 Thông hiểu) – 6,5%.*"),
        ("h3", "1. Bản đồ nguy cơ – nhóm theo thiết bị"),
        T(
         ["Nhóm thiết bị", "Thao tác / tình huống nguy hiểm", "Hậu quả"],
         [["**Điện**", "Tay chạm phần kim loại dẫn điện của phích khi cắm", "Điện giật"],
          ["**Điện**", "Cầm vào **dây điện** (thay vì phích) khi rút phích", "Đứt dây, hở mạch, giật"],
          ["**Điện**", "Cầm vào chỗ dây bị sờn, dây trần", "Điện giật"],
          ["**Điện**", "Để các **kẹp điện gần nhau**; vật dễ cháy gần mạch điện; dùng quá công suất", "Chập điện, phóng tia lửa, **cháy nổ**"],
          ["**Nhiệt & thuỷ tinh**", "Đun cốc thuỷ tinh chịu nhiệt kém trên đèn cồn; để lửa quá to, kẹp cốc quá gần đèn", "Nứt vỡ, bỏng, hỏng thiết bị"],
          ["**Nhiệt**", "Không dùng găng/dụng cụ bảo hộ khi tiếp xúc vật nóng; **thổi trực tiếp** để tắt đèn cồn", "Bỏng, lửa bùng to"],
          ["**Quang học**", "Nhìn trực tiếp vào **tia laser** công suất lớn", "Hỏng mắt"],
          ["**Hoá chất**", "Để hoá chất lộn xộn, dính vào quần áo; để nước/dung dịch dễ cháy gần thiết bị điện", "Cháy, bỏng, nhiễm độc"]],
         [20, 52, 28]),
        ("h3", "2. Chín quy tắc an toàn – nhóm theo trình tự thao tác"),
        P("**Trước khi làm thí nghiệm**"),
        ("bullets", [
            "Đọc kĩ **hướng dẫn sử dụng** thiết bị và quan sát các **kí hiệu, chỉ dẫn** trên thiết bị.",
            "**Kiểm tra** cẩn thận thiết bị, dụng cụ trước khi sử dụng.",
            "Chỉ tiến hành thí nghiệm khi **được sự cho phép của giáo viên**.",
        ]),
        P("**Trong khi làm thí nghiệm**"),
        ("bullets", [
            "**Tắt công tắc nguồn** trước khi cắm hoặc tháo thiết bị điện.",
            "Chỉ cắm phích khi **hiệu điện thế nguồn phù hợp với hiệu điện thế định mức** của dụng cụ.",
            "Bố trí **dây điện gọn gàng**, không để vướng khi đi lại.",
            "**Không tiếp xúc trực tiếp** với vật/thiết bị có nhiệt độ cao khi không có dụng cụ bảo hộ.",
            "**Không nhìn trực tiếp** vào tia laser.",
        ]),
        P("**Sau khi làm thí nghiệm**"),
        ("bullets", [
            "Tắt thiết bị, thu dọn dụng cụ, để nơi khô thoáng, tránh ẩm thấp và chất gây cháy nổ.",
            "**Không bỏ thiết bị vào thùng rác**; xử lí hoá chất đúng quy định.",
        ]),
        ("h3", "3. Đọc biển báo – dạng câu hỏi \"ăn điểm\" của phần Thông hiểu"),
        T(
         ["Hình dạng / màu", "Ý nghĩa"],
         [["**Tam giác** vàng, viền đen", "**Cảnh báo** nguy hiểm"],
          ["**Tròn** xanh, kí hiệu trắng", "**Bắt buộc** phải thực hiện"],
          ["**Tròn** đỏ, gạch chéo", "**Cấm** thực hiện"],
          ["**Vuông / chữ nhật** xanh", "**Chỉ dẫn** (vị trí, hướng đi, lối thoát)"]],
         [34, 66]),
        ("h3", "4. Khi có sự cố cháy trong phòng thực hành"),
        ("numbers", [
            "**Ngắt toàn bộ hệ thống điện.**",
            "Đưa toàn bộ hoá chất, chất dễ cháy ra khu vực an toàn.",
            "Dùng bình chữa cháy **CO₂** hoặc bình bột để dập lửa.",
            "Báo ngay cho giáo viên phụ trách.",
        ]),
        C("warn", "Ba điều CẤM khi chữa cháy",
         "**(1)** Không dùng **nước** dập đám cháy nơi có thiết bị điện, đám cháy hydrocacbon hoặc chất lỏng nhẹ hơn nước "
         "(dầu, cồn) – nước làm dầu/cồn loang rộng và gây giật. "
         "**(2)** Không dùng **CO₂** dập đám cháy **quần áo trên người** hoặc cháy kim loại kiềm (magnesium…). "
         "**(3)** Không **thổi trực tiếp** để tắt ngọn lửa đèn cồn."),
        ("qa", [
            ("Rút phích điện bằng cách nắm vào dây điện có an toàn không?",
             "**Không.** Phải nắm vào **phích điện**; nắm dây dễ làm đứt dây, hở mạch và bị điện giật."),
            ("Vì sao phải tắt công tắc nguồn trước khi cắm/tháo thiết bị điện?",
             "Để tránh **phóng tia lửa điện**, chập mạch và bảo vệ người khỏi bị giật."),
        ]),

        # ---------------------------------------------------------------- BÀI 3
        ("h2", "Bài 3 · Thực hành tính sai số trong phép đo. Ghi kết quả đo"),
        P("*Mức độ xuất hiện trong đề: 1 câu trắc nghiệm – Nhận biết (3,2%). "
              "Tuy ít câu nhưng công thức ở bài này được dùng lại trong bài thực hành đo tốc độ (Bài 6).*"),
        ("h3", "1. Phép đo trực tiếp và phép đo gián tiếp"),
        T(
         ["Loại phép đo", "Cách tiến hành", "Ví dụ"],
         [["**Trực tiếp**", "So sánh trực tiếp đại lượng cần đo với dụng cụ đo", "Dùng thước đo chiều dài, cân đo khối lượng, nhiệt kế đo nhiệt độ"],
          ["**Gián tiếp**", "Đo các đại lượng trực tiếp, rồi **tính** đại lượng cần tìm qua công thức", "Đo s và t rồi tính v = s/t; đo đường kính rồi tính chu vi"]],
         [20, 40, 40]),
        ("h3", "2. Hai loại sai số - bảng phân biệt kinh điển"),
        T(
         ["Tiêu chí", "Sai số **hệ thống**", "Sai số **ngẫu nhiên**"],
         [["Nguyên nhân", "Dụng cụ chưa chuẩn (kim lệch số 0), thang chia sai, do cấu tạo dụng cụ", "Thao tác của người đo, điều kiện môi trường thay đổi"],
          ["Tính chất", "**Lặp lại như nhau** ở mọi lần đo, cùng chiều và cùng độ lớn", "**Khác nhau** mỗi lần đo, không theo quy luật"],
          ["Cách khắc phục", "**Hiệu chỉnh** dụng cụ, chọn dụng cụ chính xác hơn", "**Đo nhiều lần** và lấy giá trị trung bình"]],
         [18, 41, 41]),
        ("h3", "3. Bộ công thức gốc"),
        F([
            "Ā = (A₁ + A₂ + … + Aₙ) / n                    (giá trị trung bình)",
            "ΔAᵢ = |Aᵢ − Ā|                                (sai số tuyệt đối lần đo thứ i)",
            "ΔĀ = (ΔA₁ + ΔA₂ + … + ΔAₙ) / n                (sai số ngẫu nhiên trung bình)",
            "ΔA = ΔĀ + ΔA_dc                              (sai số tuyệt đối của phép đo)",
            "δA = (ΔA / Ā) × 100%                          (sai số tỉ đối)",
            "A = Ā ± ΔA                                    (kết quả đo)",
        ], title="Sáu dòng cần thuộc lòng"),
        C("tip", "Mẹo nhớ chuỗi tính",
         "**“Trung bình → lệch từng lần → lệch trung bình → cộng dụng cụ → chia phần trăm → viết ±”.** "
         "Sáu bước, sáu dòng, không được nhảy bước. Đặc biệt **ΔA luôn = ΔĀ + ΔA_dc** – quên cộng sai số dụng cụ là lỗi phổ biến nhất."),
        P("Trong chương trình Kết nối tri thức, **sai số dụng cụ ΔA_dc thường lấy bằng nửa độ chia nhỏ nhất (ĐCNN)** "
              "của dụng cụ; một số dụng cụ đặc biệt lấy bằng một ĐCNN. Đề bài sẽ ghi rõ nếu có quy ước khác."),
        ("h3", "4. Quy tắc ghi kết quả đo"),
        ("bullets", [
            "**ΔA** chỉ viết đến **1 hoặc 2 chữ số có nghĩa**, và thường lấy tới hàng của ĐCNN.",
            "**Ā** được làm tròn đến **cùng bậc thập phân** với ΔA.",
            "Viết dạng **A = Ā ± ΔA**, đơn vị ghi **một lần** ở cuối.",
            "Có thể viết dưới dạng khoảng: (Ā − ΔA) ≤ A ≤ (Ā + ΔA).",
        ]),
        ("h3", "5. Ví dụ mẫu hoàn chỉnh – dạng bài chắc chắn xuất hiện"),
        P("Đo chiều dài con lắc 5 lần, thu được: 20,0 ; 20,1 ; 20,0 ; 20,2 ; 19,9 (cm). Thước có ĐCNN 0,1 cm. "
              "Hãy tính giá trị trung bình, sai số tuyệt đối, sai số tỉ đối và viết kết quả."),
        F([
            "Ā = (20,0 + 20,1 + 20,0 + 20,2 + 19,9)/5 = 100,2/5 = 20,04 cm",
            "ΔA₁ = 0,04 ; ΔA₂ = 0,06 ; ΔA₃ = 0,04 ; ΔA₄ = 0,16 ; ΔA₅ = 0,14 (cm)",
            "ΔĀ = (0,04+0,06+0,04+0,16+0,14)/5 = 0,44/5 = 0,088 cm",
            "ΔA_dc = 0,1/2 = 0,05 cm  →  ΔA = 0,088 + 0,05 = 0,138 ≈ 0,1 cm",
            "δ = (0,138/20,04) × 100% ≈ 0,7%",
            "Kết quả:  ℓ = 20,0 ± 0,1 (cm)",
        ]),
        C("warn", "Vì sao Ā = 20,04 lại viết thành 20,0?",
         "Vì ΔA đã làm tròn đến **hàng phần mười** (0,1 cm). Theo quy tắc, Ā phải làm tròn đến **cùng bậc** – "
         "tức hàng phần mười. Viết *20,04 ± 0,1* là **sai quy tắc** dù phép tính đúng."),
        ("h3", "6. Sai số của phép đo gián tiếp – ba quy tắc vàng"),
        T(
         ["Phép tính", "Quy tắc sai số", "Ví dụ"],
         [["**Tổng / hiệu**", "Sai số tuyệt đối **cộng lại**: ΔA = Δa + Δb", "d = a − b với Δa = 0,2; Δb = 0,1 → Δd = 0,3"],
          ["**Tích / thương**", "Sai số tỉ đối **cộng lại**: δA = δa + δb", "v = s/t → δv = δs + δt"],
          ["**Luỹ thừa**", "δ(Aⁿ) = n · δA", "g = 2h/t² → δg = δh + 2δt"]],
         [22, 48, 30]),
        ("h3", "7. Chữ số có nghĩa (significant figures)"),
        ("bullets", [
            "Các chữ số **khác 0** luôn có nghĩa; các số 0 **nằm giữa** luôn có nghĩa; các số 0 **ở cuối phần thập phân** có nghĩa.",
            "Số 0 ở **đầu** (bên trái) **không** có nghĩa: 0,00230 có **3** chữ số có nghĩa (2, 3, 0).",
            "**Nhân / chia:** kết quả giữ số chữ số có nghĩa bằng **thừa số ít nhất**.",
            "**Cộng / trừ:** kết quả giữ số chữ số **thập phân** ít nhất.",
        ]),
        ("qa", [
            ("Sai số tỉ đối càng lớn thì phép đo càng chính xác hay càng kém chính xác?",
             "Càng **kém** chính xác. δ càng **nhỏ** thì phép đo càng chính xác."),
            ("Sai số tuyệt đối và sai số tỉ đối khác nhau ở đơn vị thế nào?",
             "Sai số tuyệt đối có **cùng đơn vị** với đại lượng đo; sai số tỉ đối là **phần trăm** (không đơn vị)."),
        ]),

        # ---------------------------------------------------------------- BÀI 4
        ("h2", "Bài 4 · Độ dịch chuyển và quãng đường đi được"),
        P("*Mức độ xuất hiện trong đề: 3 câu trắc nghiệm (1 Nhận biết + 2 Thông hiểu) – 9,7%.*"),
        ("h3", "1. Hai khái niệm, một khác biệt cốt lõi"),
        P("**Độ dịch chuyển** là **vectơ** nối vị trí đầu với vị trí cuối của vật. Trên một trục toạ độ Ox, "
              "độ dịch chuyển được tính bằng **hiệu các toạ độ**: Δx = x₂ − x₁. "
              "**Quãng đường** là **độ dài quỹ đạo** mà vật đã đi qua."),
        F([
            "Δx = x₂ − x₁        (độ dịch chuyển trên trục Ox)",
            "d = |Δx|            (độ lớn độ dịch chuyển)",
            "s  : quãng đường    (luôn ≥ 0)",
            "Hệ quả:  |Δx| ≤ s   (dấu \"=\" khi chuyển động thẳng, không đổi chiều)",
        ]),
        ("h3", "2. Bảng so sánh – dạng câu hỏi Nhận biết hay ra nhất"),
        T(
         ["Tiêu chí", "Độ dịch chuyển", "Quãng đường"],
         [["Bản chất", "Đại lượng **vectơ**", "Đại lượng **vô hướng**"],
          ["Định nghĩa", "Vectơ nối vị trí **đầu** và vị trí **cuối**", "**Độ dài quỹ đạo** đã đi"],
          ["Giá trị", "Dương, âm hoặc bằng 0", "**Luôn dương** hoặc bằng 0"],
          ["Phụ thuộc", "Chỉ phụ thuộc **điểm đầu – điểm cuối**", "Phụ thuộc **toàn bộ đường đi**"],
          ["Quan hệ", "|Δx| **≤** s", "s **≥** |Δx|"],
          ["Bằng nhau khi", "Vật chuyển động **thẳng và không đổi chiều**", "cùng điều kiện"]],
         [22, 40, 38]),
        C("tip", "Một câu để nhớ mãi",
         "**“Đi được bao xa” là quãng đường – “lệch bao xa so với chỗ cũ” là độ dịch chuyển.** "
         "Đi một vòng sân rồi về chỗ cũ: **đi được rất xa, nhưng lệch bằng 0**."),
        ("h3", "3. Ba ví dụ vàng (học thuộc để làm trắc nghiệm trong 10 giây)"),
        T(
         ["Tình huống", "Quãng đường s", "Độ lớn độ dịch chuyển |Δx|"],
         [["Đi 3 km về hướng Bắc, rồi 4 km về hướng Đông", "3 + 4 = **7 km**", "√(3² + 4²) = **5 km**"],
          ["Đi đúng một vòng tròn bán kính R rồi dừng", "2πR", "**0**"],
          ["Đi từ A đến B dài 10 km rồi quay lại A", "**20 km**", "**0**"],
          ["Đi thẳng 5 km, không đổi chiều", "**5 km**", "**5 km**"]],
         [52, 24, 24]),
        C("warn", "Bẫy kinh điển",
         "Đề cho “đi 3 km Bắc rồi 4 km Đông” và hỏi **độ dịch chuyển**. Rất nhiều bạn chọn 7 km vì quen cộng. "
         "Nhớ: hai hướng **vuông góc** → dùng **Pitago**, không cộng số học."),
        ("qa", [
            ("Một vật đi từ x = 2 m đến x = 10 m rồi quay về x = 4 m. Tính quãng đường và độ dịch chuyển.",
             "s = 8 + 6 = **14 m**; Δx = 4 − 2 = **+2 m**."),
            ("Khi nào quãng đường bằng độ lớn độ dịch chuyển?",
             "Khi vật chuyển động **thẳng và không đổi chiều**."),
        ]),

        # ---------------------------------------------------------------- BÀI 5
        ("h2", "Bài 5 · Tốc độ và vận tốc"),
        P("*Mức độ xuất hiện trong đề: 5 lượt hỏi (1 câu TN + 2 ý Đúng–Sai + 1 câu trả lời ngắn + 1 câu tự luận) – 16,1%, "
              "đứng thứ hai toàn đề.*"),
        ("h3", "1. Tốc độ"),
        ("bullets", [
            "**Tốc độ trung bình** cho biết mức độ nhanh chậm của chuyển động trên cả quãng đường: **v_tb = s / Δt**. "
            "Đây là đại lượng **vô hướng**, luôn **không âm**.",
            "**Tốc độ tức thời** là tốc độ tại **một thời điểm** (hoặc trong một khoảng thời gian rất ngắn). "
            "Số chỉ trên **tốc kế** của ô tô, xe máy chính là tốc độ tức thời.",
        ]),
        ("h3", "2. Vận tốc"),
        P("**Vận tốc** là đại lượng **vectơ**, được xác định bằng **độ dịch chuyển chia cho thời gian**: "
              "**vectơ v** = **vectơ Δd** / Δt (dấu vectơ thể hiện ở hướng). Vận tốc cho biết **hướng** và **mức độ nhanh chậm** của chuyển động."),
        F([
            "Tốc độ trung bình:   v_tb = s / Δt              (vô hướng, ≥ 0)",
            "Vận tốc trung bình:  v_tb = Δd / Δt            (vectơ, có dấu ±)",
            "Đổi đơn vị:          1 m/s = 3,6 km/h",
            "                     1 km/h = 1/3,6 m/s ≈ 0,278 m/s",
        ]),
        ("h3", "3. Bảng phân biệt tốc độ – vận tốc"),
        T(
         ["Tiêu chí", "Tốc độ", "Vận tốc"],
         [["Loại đại lượng", "**Vô hướng**", "**Vectơ**"],
          ["Tử số của công thức", "**Quãng đường** s", "**Độ dịch chuyển** Δd"],
          ["Dấu", "Luôn **≥ 0**", "Dương, âm hoặc 0"],
          ["Cho biết", "Chỉ mức độ nhanh chậm", "Mức độ nhanh chậm **và hướng**"],
          ["Đơn vị", "m/s ; km/h", "m/s ; km/h"]],
         [24, 38, 38]),
        C("tip", "Đổi đơn vị trong 3 giây",
         "**km/h → m/s: chia 3,6.  m/s → km/h: nhân 3,6.** "
         "Nhớ sẵn 3 mốc: **36 km/h = 10 m/s · 54 km/h = 15 m/s · 72 km/h = 20 m/s**. "
         "Ba mốc này xuất hiện trong đa số đề kiểm tra."),
        ("h3", "4. Công thức cộng vận tốc"),
        F([
            "v₁₃ = v₁₂ + v₂₃",
            "",
            "1 = vật chuyển động · 2 = môi trường (nước, gió) · 3 = vật mốc (bờ, đất)",
        ], title="Công thức gốc"),
        T(
         ["Trường hợp hai vận tốc thành phần", "Công thức độ lớn", "Ví dụ"],
         [["**Cùng phương, cùng chiều**", "v₁₃ = v₁₂ + v₂₃", "Ca nô xuôi dòng: 15 + 3 = 18 km/h"],
          ["**Cùng phương, ngược chiều**", "v₁₃ = |v₁₂ − v₂₃|", "Ca nô ngược dòng: 15 − 3 = 12 km/h"],
          ["**Vuông góc**", "v₁₃ = √(v₁₂² + v₂₃²)", "Thuyền qua sông có nước chảy"],
          ["**Hợp với nhau góc α**", "v₁₃² = v₁₂² + v₂₃² + 2v₁₂v₂₃cosα", "Trường hợp tổng quát"]],
         [34, 40, 26]),
        C("tip", "Mẹo nhớ chỉ số",
         "Nhìn **chỉ số giữa**: v₁₃ = v₁₂ + v₂₃ – hai chỉ số **2** gặp nhau thì “dính” lại. "
         "Nếu chỉ số giữa **không trùng** (ví dụ v₁₂ và v₃₂), hãy đổi chiều: v₃₂ = −v₂₃ rồi mới cộng."),
        ("h3", "5. Cách đo tốc độ"),
        T(
         ["Bối cảnh", "Dụng cụ / cách làm"],
         [["**Trong phòng thí nghiệm**", "Đồng hồ bấm giây + thước đo; hoặc **cổng quang điện + đồng hồ đo thời gian hiện số** (chính xác hơn)"],
          ["**Trong đời sống**", "**Tốc kế** (đồng hồ tốc độ) trên ô tô, xe máy; thiết bị **GPS**; **súng bắn tốc độ** của cảnh sát giao thông (dùng sóng radar/laser)"]],
         [30, 70]),
        ("h3", "6. Ví dụ mẫu có lời giải"),
        P("**Đề:** Một ca nô chạy xuôi dòng từ A đến B dài 36 km. Vận tốc của ca nô so với nước là 15 km/h, "
              "vận tốc dòng nước so với bờ là 3 km/h. "
              "a) Tính vận tốc ca nô so với bờ và thời gian đi từ A đến B. "
              "b) Nếu ca nô chạy ngược dòng từ B về A với cùng vận tốc so với nước thì mất bao lâu?"),
        F([
            "a) Xuôi dòng (cùng chiều): v = 15 + 3 = 18 km/h",
            "   t = s/v = 36/18 = 2 h",
            "b) Ngược dòng (ngược chiều): v = 15 − 3 = 12 km/h",
            "   t = 36/12 = 3 h",
        ]),
        C("warn", "Bẫy: đừng cộng vận tốc khi ngược chiều",
         "Khi ngược dòng, nước **cản** thuyền nên vận tốc **giảm**: lấy hiệu, không lấy tổng. "
         "Và nhớ: vận tốc ca nô **so với nước** không đổi, chỉ vận tốc **so với bờ** thay đổi."),
        ("qa", [
            ("Một ô tô đi 120 km trong 2 giờ. Tốc độ trung bình là bao nhiêu?",
             "v = 120/2 = **60 km/h** ≈ 16,7 m/s."),
            ("Máy bay bay với vận tốc 200 m/s so với không khí, gió thổi ngược chiều 20 m/s. Vận tốc so với mặt đất?",
             "200 − 20 = **180 m/s**."),
        ]),
    ]
    return B
