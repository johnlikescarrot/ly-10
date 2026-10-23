# -*- coding: utf-8 -*-
"""PHẦN 3 (đề minh hoạ) và PHẦN 4 (đáp án, lời giải) + PHỤ LỤC."""

from dsl import T, F, P, C


def blocks_c():
    B = []

    # =====================================================================
    # PHẦN 3
    # =====================================================================
    B += [
        ("h1", "PHẦN 3 · ĐỀ MINH HOẠ BÁM MA TRẬN"),
        P("Tài liệu gốc là **ma trận đặc tả**, không kèm đề bài. Vì vậy để bảo đảm yêu cầu “có đầy đủ câu hỏi và "
              "đáp án của bài kiểm tra giữa kì”, phần này dựng **một đề minh hoạ hoàn chỉnh**, phân bổ **chính xác "
              "từng câu – từng ý** theo đúng ma trận: 18 câu Phần I, 2 câu × 4 ý Phần II, 2 câu Phần III, 2 câu Phần IV. "
              "Toàn bộ đáp án và lời giải chi tiết nằm ở **Phần 4**."),

        ("h2", "Bảng kiểm tra độ phủ ma trận"),
        P("Bảng dưới đây chứng minh **không một ô nào của ma trận bị bỏ sót**: mỗi con số ở Phần 0.2 đều được "
              "ánh xạ tới một câu hỏi cụ thể trong đề minh hoạ."),
        T(
         ["Đơn vị kiến thức", "Mức độ", "Vị trí trong đề", "Số ý"],
         [["1.1. Làm quen với Vật lí", "Nhận biết", "Câu I.1", "1"],
          ["1.2. Quy tắc an toàn", "Nhận biết / Thông hiểu", "Câu I.2 / Câu I.3", "2"],
          ["1.3. Sai số trong phép đo", "Nhận biết", "Câu I.4", "1"],
          ["2.1. Độ dịch chuyển – quãng đường", "Nhận biết", "Câu I.5", "1"],
          ["2.1. Độ dịch chuyển – quãng đường", "Thông hiểu", "Câu I.6, I.7", "2"],
          ["2.2. Tốc độ và vận tốc", "Nhận biết", "Câu I.8 · II.1a · II.1b · III.1", "4"],
          ["2.2. Tốc độ và vận tốc", "Thông hiểu", "Câu IV.1", "1"],
          ["2.3. Đồ thị độ dịch chuyển – thời gian", "Nhận biết", "Câu I.9 · II.1c · II.1d", "3"],
          ["2.3. Đồ thị độ dịch chuyển – thời gian", "Thông hiểu", "Câu I.10", "1"],
          ["2.4. Chuyển động biến đổi – gia tốc", "Nhận biết", "Câu I.11", "1"],
          ["2.4. Chuyển động biến đổi – gia tốc", "Thông hiểu", "Câu I.12", "1"],
          ["2.5. Chuyển động thẳng biến đổi đều", "Nhận biết", "Câu I.13, I.14 · II.2a · II.2b", "4"],
          ["2.5. Chuyển động thẳng biến đổi đều", "Thông hiểu", "Câu I.15 · II.2c · II.2d", "3"],
          ["2.5. Chuyển động thẳng biến đổi đều", "Vận dụng", "Câu IV.2 (ý a, b)", "2"],
          ["2.6. Sự rơi tự do", "Nhận biết", "Câu I.16", "1"],
          ["2.6. Sự rơi tự do", "Thông hiểu", "Câu I.17, I.18 · III.2", "3"],
          ["**Tổng**", "", "", "**31**"]],
         [40, 24, 28, 8],
         size=8.0, align=["LEFT", "LEFT", "LEFT", "CENTER"]),

        ("h2", "ĐỀ BÀI"),
        C("note", "Thông tin đề",
         "**Thời gian làm bài: 50 phút** · Không kể thời gian phát đề · Học sinh không được sử dụng tài liệu. "
         "Điểm tối đa: **10,00** (Phần I: 4,50 · Phần II: 2,00 · Phần III: 0,50 · Phần IV: 3,00)."),

        ("h3", "PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (18 câu · 4,50 điểm)"),
        P("*Chọn một phương án đúng nhất trong bốn phương án A, B, C, D.*", italic=True),

        ("mcq", {"n": 1, "tag": "1.1 · Nhận biết",
                 "stem": "Đối tượng nghiên cứu chủ yếu của Vật lí là",
                 "opts": ["các dạng vận động của vật chất và năng lượng.",
                          "cấu tạo và tính chất của các hợp chất hữu cơ.",
                          "sự phát triển của xã hội loài người.",
                          "các quy luật của tư duy và nhận thức."]}),
        ("mcq", {"n": 2, "tag": "1.2 · Nhận biết",
                 "stem": "Thao tác nào sau đây **KHÔNG** tuân thủ quy tắc an toàn trong phòng thực hành Vật lí?",
                 "opts": ["Tắt công tắc nguồn trước khi cắm hoặc tháo thiết bị điện.",
                          "Dùng tay trần cầm trực tiếp cốc thuỷ tinh vừa đun trên đèn cồn.",
                          "Đọc kĩ hướng dẫn sử dụng và quan sát các kí hiệu trên thiết bị.",
                          "Bố trí dây điện gọn gàng, không để vướng khi đi lại."]}),
        ("mcq", {"n": 3, "tag": "1.2 · Thông hiểu",
                 "stem": "Biển báo có nền xanh, hình tròn, bên trong là kí hiệu màu trắng thường dùng để",
                 "opts": ["cảnh báo nguy hiểm.",
                          "cấm thực hiện.",
                          "chỉ dẫn vị trí thiết bị.",
                          "bắt buộc phải thực hiện."]}),
        ("mcq", {"n": 4, "tag": "1.3 · Nhận biết",
                 "stem": "Trường hợp nào sau đây là **sai số hệ thống**?",
                 "opts": ["Sai số do người đo đọc lệch kết quả khác nhau ở mỗi lần đo.",
                          "Sai số do thời tiết thay đổi trong các lần đo.",
                          "Sai số do rung tay khi bấm đồng hồ.",
                          "Sai số do kim đồng hồ chưa chỉ đúng vạch số 0 khi chưa đo."]}),
        ("mcq", {"n": 5, "tag": "2.1 · Nhận biết",
                 "stem": "Phát biểu nào sau đây **đúng**?",
                 "opts": ["Độ dịch chuyển là đại lượng vô hướng và luôn dương.",
                          "Độ dịch chuyển là vectơ nối vị trí đầu với vị trí cuối của vật.",
                          "Quãng đường đi được là đại lượng vectơ.",
                          "Độ lớn của độ dịch chuyển luôn lớn hơn quãng đường đi được."]}),
        ("mcq", {"n": 6, "tag": "2.1 · Thông hiểu",
                 "stem": "Một người đi xe đạp từ A đến B cách A 3 km về phía Bắc, rồi từ B đi tiếp 4 km về phía Đông đến C. "
                         "Quãng đường và độ lớn độ dịch chuyển của người đó lần lượt là",
                 "opts": ["7 km và 7 km.", "5 km và 7 km.", "7 km và 5 km.", "5 km và 5 km."]}),
        ("mcq", {"n": 7, "tag": "2.1 · Thông hiểu",
                 "stem": "Một vận động viên chạy đúng một vòng quanh sân hình tròn bán kính 50 m rồi dừng lại tại điểm "
                         "xuất phát. Lấy π = 3,14. Quãng đường và độ lớn độ dịch chuyển của vận động viên là",
                 "opts": ["314 m và 0 m.", "314 m và 314 m.", "157 m và 0 m.", "0 m và 0 m."]}),
        ("mcq", {"n": 8, "tag": "2.2 · Nhận biết",
                 "stem": "Công thức tính tốc độ trung bình của một vật chuyển động là",
                 "opts": ["v_tb = Δd / Δt", "v_tb = Δt / s", "v_tb = s · Δt", "v_tb = s / Δt"]}),
        ("mcq", {"n": 9, "tag": "2.3 · Nhận biết",
                 "stem": "Trên đồ thị độ dịch chuyển – thời gian của một vật chuyển động thẳng, đoạn đồ thị nằm ngang "
                         "song song với trục thời gian cho biết",
                 "opts": ["vật đang đứng yên.",
                          "vật chuyển động thẳng đều.",
                          "vật chuyển động nhanh dần đều.",
                          "vật đang đổi chiều chuyển động."]}),
        ("mcq", {"n": 10, "tag": "2.3 · Thông hiểu",
                 "stem": "Đồ thị độ dịch chuyển – thời gian của một ô tô là đường thẳng đi qua gốc toạ độ và điểm có "
                         "toạ độ (t = 2 h; d = 120 km). Tốc độ của ô tô là",
                 "opts": ["240 km/h.", "120 km/h.", "60 km/h.", "30 km/h."]}),
        ("mcq", {"n": 11, "tag": "2.4 · Nhận biết",
                 "stem": "Gia tốc của một chuyển động là đại lượng",
                 "opts": ["vô hướng, đặc trưng cho mức độ nhanh chậm của chuyển động.",
                          "vectơ, đặc trưng cho độ lớn vận tốc của vật.",
                          "vô hướng, có đơn vị là m/s.",
                          "vectơ, đặc trưng cho sự biến thiên của vận tốc theo thời gian."]}),
        ("mcq", {"n": 12, "tag": "2.4 · Thông hiểu",
                 "stem": "Một xe đang chạy với vận tốc 10 m/s thì tăng tốc và sau 5 s đạt vận tốc 20 m/s. "
                         "Gia tốc của xe là",
                 "opts": ["0,5 m/s².", "4 m/s².", "2 m/s².", "6 m/s²."]}),
        ("mcq", {"n": 13, "tag": "2.5 · Nhận biết",
                 "stem": "Trong chuyển động thẳng nhanh dần đều thì",
                 "opts": ["vectơ gia tốc cùng chiều với vectơ vận tốc.",
                          "gia tốc luôn có giá trị dương.",
                          "vectơ gia tốc ngược chiều với vectơ vận tốc.",
                          "gia tốc luôn có giá trị âm."]}),
        ("mcq", {"n": 14, "tag": "2.5 · Nhận biết",
                 "stem": "Công thức liên hệ giữa vận tốc, gia tốc và độ dịch chuyển của chuyển động thẳng biến đổi đều "
                         "(**không** chứa thời gian) là",
                 "opts": ["v = v₀ + a·t.", "d = v₀·t + ½·a·t².", "v² − v₀² = 2·a·d.", "d = (v₀ + v)·t/2."]}),
        ("mcq", {"n": 15, "tag": "2.5 · Thông hiểu",
                 "stem": "Một vật chuyển động thẳng chậm dần đều. Chọn chiều dương là chiều chuyển động của vật. "
                         "Nhận xét nào sau đây **đúng**?",
                 "opts": ["v > 0 và a > 0.", "v < 0 và a > 0.", "v < 0 và a < 0.", "v > 0 và a < 0."]}),
        ("mcq", {"n": 16, "tag": "2.6 · Nhận biết",
                 "stem": "Sự rơi tự do là sự rơi của một vật",
                 "opts": ["chỉ dưới tác dụng của trọng lực.",
                          "trong không khí và có lực cản nhỏ không đáng kể.",
                          "chỉ dưới tác dụng của lực cản của không khí.",
                          "có vận tốc ban đầu khác không."]}),
        ("mcq", {"n": 17, "tag": "2.6 · Thông hiểu",
                 "stem": "Một vật được thả rơi tự do từ độ cao h. Lấy g = 10 m/s². Quãng đường vật rơi được trong "
                         "2 s đầu tiên là",
                 "opts": ["5 m.", "20 m.", "10 m.", "40 m."]}),
        ("mcq", {"n": 18, "tag": "2.6 · Thông hiểu",
                 "stem": "Hai vật có khối lượng khác nhau được thả rơi tự do từ cùng một độ cao, tại cùng một thời điểm, "
                         "bỏ qua sức cản của không khí. Nhận xét nào sau đây **đúng**?",
                 "opts": ["Vật có khối lượng lớn hơn chạm đất trước.",
                          "Vật có khối lượng nhỏ hơn chạm đất trước.",
                          "Không đủ dữ kiện để so sánh.",
                          "Hai vật chạm đất cùng lúc."]}),

        ("h3", "PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu · 8 ý · 2,00 điểm)"),
        P("*Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn **Đúng** hoặc **Sai**.*", italic=True),
        ("tf", {"n": 1, "tag": "2.2 Tốc độ và vận tốc · 2.3 Đồ thị độ dịch chuyển – thời gian",
                "lead": "Một ô tô chuyển động thẳng đều trên một đường thẳng với tốc độ 54 km/h. Chọn gốc toạ độ tại vị trí "
                        "xuất phát, chiều dương là chiều chuyển động, gốc thời gian là lúc ô tô xuất phát.",
                "items": [("a", "Tốc độ 54 km/h tương ứng với 15 m/s."),
                          ("b", "Vận tốc của ô tô là đại lượng vectơ, còn tốc độ là đại lượng vô hướng."),
                          ("c", "Đồ thị độ dịch chuyển – thời gian của ô tô là một đường thẳng nằm ngang song song với trục Ot."),
                          ("d", "Sau 30 s kể từ lúc xuất phát, độ dịch chuyển của ô tô là 1620 m.")]}),
        ("tf", {"n": 2, "tag": "2.5 Chuyển động thẳng biến đổi đều",
                "lead": "Một xe máy đang chuyển động thẳng với vận tốc 36 km/h thì người lái hãm phanh, xe chuyển động "
                        "chậm dần đều với gia tốc có độ lớn 2 m/s² cho đến khi dừng hẳn. Chọn chiều dương là chiều chuyển động, "
                        "gốc thời gian là lúc bắt đầu hãm phanh.",
                "items": [("a", "Vận tốc ban đầu của xe là 10 m/s."),
                          ("b", "Gia tốc của xe là a = −2 m/s²."),
                          ("c", "Xe dừng lại sau 10 s kể từ lúc bắt đầu hãm phanh."),
                          ("d", "Quãng đường xe đi được từ lúc hãm phanh đến khi dừng hẳn là 25 m.")]}),

        ("h3", "PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (2 câu · 0,50 điểm)"),
        P("*Viết đáp án bằng một con số kèm đơn vị (nếu có) vào ô trả lời.*", italic=True),
        ("short", {"n": 1, "tag": "2.2 · Nhận biết",
                   "stem": "Một người đi bộ với tốc độ không đổi 1,5 m/s. Tính quãng đường người đó đi được trong 2 phút "
                           "(theo đơn vị mét)."}),
        ("short", {"n": 2, "tag": "2.6 · Thông hiểu",
                   "stem": "Một vật được thả rơi tự do từ độ cao 20 m so với mặt đất. Lấy g = 10 m/s². "
                           "Tính thời gian rơi của vật (theo đơn vị giây)."}),

        ("h3", "PHẦN IV. TỰ LUẬN (2 câu · 3,00 điểm)"),
        ("essay", {"n": 1, "points": "1,50 điểm", "tag": "2.2 · Thông hiểu",
                   "stem": "Một ca nô chạy xuôi dòng từ bến A đến bến B cách nhau 36 km. Vận tốc của ca nô khi nước yên "
                           "lặng là 15 km/h, vận tốc của dòng nước so với bờ là 3 km/h.",
                   "parts": ["**a)** Tính vận tốc của ca nô so với bờ và thời gian ca nô đi từ A đến B.",
                             "**b)** Nếu ca nô chạy ngược dòng từ B về A với cùng vận tốc so với nước thì mất bao nhiêu thời gian?"]}),
        ("essay", {"n": 2, "points": "1,50 điểm", "tag": "2.5 · Vận dụng",
                   "stem": "Một ô tô đang chạy với vận tốc 20 m/s thì tăng tốc, chuyển động nhanh dần đều với gia tốc "
                           "2 m/s². Chọn chiều dương là chiều chuyển động, gốc thời gian là lúc bắt đầu tăng tốc.",
                   "parts": ["**a)** Viết công thức tính vận tốc của ô tô theo thời gian và tính vận tốc của ô tô sau 5 s.",
                             "**b)** Tính quãng đường ô tô đi được trong 5 s đó và quãng đường ô tô đi được trong giây thứ 5."]}),
        C("note", "Hết đề",
         "Thí sinh không được trao đổi bài. Đáp án và lời giải chi tiết ở **Phần 4** (trang sau)."),
    ]

    # =====================================================================
    # PHẦN 4
    # =====================================================================
    B += [
        ("h1", "PHẦN 4 · ĐÁP ÁN & LỜI GIẢI CHI TIẾT"),

        ("h2", "4.1. Bảng đáp án nhanh"),
        P("**Phần I – 18 câu trắc nghiệm (mỗi câu 0,25 điểm):**"),
        T(
         ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
         [["**Đáp án**", "**A**", "**B**", "**D**", "**D**", "**B**", "**C**", "**A**", "**D**", "**A**"]],
         [13] + [9.6] * 9, size=8.6, align=["LEFT"] + ["CENTER"] * 9, zebra=False),
        T(
         ["Câu", "10", "11", "12", "13", "14", "15", "16", "17", "18"],
         [["**Đáp án**", "**C**", "**D**", "**C**", "**A**", "**C**", "**D**", "**A**", "**B**", "**D**"]],
         [13] + [9.6] * 9, size=8.6, align=["LEFT"] + ["CENTER"] * 9, zebra=False),
        P("**Phần II – Đúng/Sai:**"),
        T(
         ["Câu", "a", "b", "c", "d", "Điểm tối đa"],
         [["**Câu 1**", "Đúng", "Đúng", "**Sai**", "**Sai**", "1,00"],
          ["**Câu 2**", "Đúng", "Đúng", "**Sai**", "Đúng", "1,00"]],
         [14, 16, 16, 16, 16, 22],
         align=["LEFT", "CENTER", "CENTER", "CENTER", "CENTER", "CENTER"]),
        P("**Phần III – Trả lời ngắn:** Câu 1: **180 m**. Câu 2: **2 s**."),
        P("**Phần IV:** Câu 1: a) 18 km/h và 2 h; b) 3 h. Câu 2: a) v = 20 + 2t, v(5 s) = 30 m/s; "
              "b) 125 m và 29 m."),

        ("h2", "4.2. Lời giải chi tiết Phần I"),

        ("h3", "Câu 1 – A"),
        P("Vật lí nghiên cứu các **dạng vận động của vật chất** (chất và trường) và **năng lượng**. "
              "Các phương án B, C, D lần lượt thuộc Hoá học, Xã hội học và Triết học."),

        ("h3", "Câu 2 – B"),
        P("Cốc thuỷ tinh vừa đun trên đèn cồn có **nhiệt độ rất cao**; cầm trực tiếp bằng tay trần sẽ gây **bỏng**. "
              "Quy tắc an toàn yêu cầu **không tiếp xúc trực tiếp** với vật có nhiệt độ cao khi không có dụng cụ bảo hộ. "
              "Ba phương án còn lại đều là thao tác an toàn."),

        ("h3", "Câu 3 – D"),
        P("Quy ước biển báo: **tam giác vàng** = cảnh báo nguy hiểm; **tròn xanh, kí hiệu trắng** = **bắt buộc** "
              "thực hiện; **tròn đỏ, gạch chéo** = cấm; **vuông/chữ nhật xanh** = chỉ dẫn."),

        ("h3", "Câu 4 – D"),
        P("**Sai số hệ thống** do **dụng cụ** gây ra, lặp lại như nhau ở mọi lần đo – ví dụ kim đồng hồ **chưa chỉ "
              "đúng vạch 0**. Các phương án A, C là sai số ngẫu nhiên (do thao tác người đo); B cũng là ngẫu nhiên "
              "(do điều kiện môi trường)."),

        ("h3", "Câu 5 – B"),
        P("Độ dịch chuyển là **vectơ** nối vị trí đầu với vị trí cuối, có thể **dương, âm hoặc bằng 0** → A sai. "
              "Quãng đường là **vô hướng** → C sai. Độ lớn độ dịch chuyển **không lớn hơn** quãng đường → D sai."),

        ("h3", "Câu 6 – C"),
        F([
            "s = 3 + 4 = 7 km",
            "|Δd| = √(3² + 4²) = 5 km        (hai hướng vuông góc → Pitago)",
        ]),
        P("Thứ tự đáp án là **quãng đường trước, độ dịch chuyển sau** → 7 km và 5 km."),

        ("h3", "Câu 7 – A"),
        F([
            "s = 2πR = 2 · 3,14 · 50 = 314 m",
            "Δd = 0   (vì vật quay về đúng điểm xuất phát)",
        ]),
        P("Đây là ví dụ kinh điển: **đi rất xa nhưng lệch bằng 0**."),

        ("h3", "Câu 8 – D"),
        P("Tốc độ trung bình = **quãng đường / thời gian** → v_tb = s/Δt. "
              "Phương án A là công thức **vận tốc** trung bình (dùng độ dịch chuyển)."),

        ("h3", "Câu 9 – A"),
        P("Đồ thị d–t nằm ngang nghĩa là **độ dịch chuyển không đổi theo thời gian** → vật **đứng yên**. "
              "Chuyển động thẳng đều cho đường **thẳng xiên**."),

        ("h3", "Câu 10 – C"),
        F(["v = Δd/Δt = (120 − 0)/(2 − 0) = 60 km/h"]),
        P("Độ dốc của đồ thị d–t chính là vận tốc. Lưu ý đơn vị: km và h nên kết quả là km/h."),

        ("h3", "Câu 11 – D"),
        P("Gia tốc là **vectơ**, đơn vị **m/s²**, đặc trưng cho **sự biến thiên của vận tốc theo thời gian** "
              "(nhanh hay chậm, và theo hướng nào)."),

        ("h3", "Câu 12 – C"),
        F(["a = (v − v₀)/Δt = (20 − 10)/5 = 2 m/s²"]),

        ("h3", "Câu 13 – A"),
        P("Nhanh dần đều: **vectơ gia tốc cùng chiều với vectơ vận tốc**. "
              "Lưu ý bẫy: gia tốc **không** nhất thiết dương – nếu vật chuyển động theo chiều âm và nhanh dần thì "
              "cả v và a đều âm (cùng dấu)."),

        ("h3", "Câu 14 – C"),
        P("Hệ thức **v² − v₀² = 2ad** được suy ra bằng cách khử t từ hai công thức v = v₀ + at và d = v₀t + ½at². "
              "Đây là công thức **duy nhất không chứa t** trong bốn công thức."),

        ("h3", "Câu 15 – D"),
        P("Chậm dần đều → gia tốc **ngược chiều** vận tốc. Vật đang chuyển động theo chiều dương nên **v > 0**, "
              "do đó **a < 0**. Quy tắc: **trái dấu thì chậm dần**."),

        ("h3", "Câu 16 – A"),
        P("Định nghĩa chuẩn: rơi tự do là sự rơi **chỉ dưới tác dụng của trọng lực**. "
              "Phương án B mô tả sự rơi **gần đúng** tự do (vẫn có lực cản), không phải định nghĩa."),

        ("h3", "Câu 17 – B"),
        F(["s = ½gt² = ½ · 10 · 2² = 20 m"]),
        P("Bẫy: nếu dùng s = v·t với v = gt sẽ ra 40 m – sai, vì vận tốc **thay đổi liên tục**, không phải hằng số."),

        ("h3", "Câu 18 – D"),
        P("Trong chân không (bỏ qua lực cản), mọi vật rơi với **cùng gia tốc g**, không phụ thuộc khối lượng → "
              "**chạm đất cùng lúc**. Đây là kết luận nổi tiếng từ thí nghiệm của Newton với ống hút chân không."),

        ("h2", "4.3. Lời giải chi tiết Phần II"),

        ("h3", "Câu 1"),
        ("bullets", [
            "**a) ĐÚNG.** 54 km/h = 54 : 3,6 = 15 m/s.",
            "**b) ĐÚNG.** Vận tốc là vectơ (có hướng), tốc độ là vô hướng (chỉ có độ lớn).",
            "**c) SAI.** Ô tô chuyển động **thẳng đều** nên đồ thị d–t là **đường thẳng xiên** đi qua gốc toạ độ, "
            "không phải đường nằm ngang. Đường nằm ngang ứng với vật **đứng yên**.",
            "**d) SAI.** d = v·t = 15 m/s × 30 s = **450 m**. Con số 1620 m là kết quả của việc quên đổi đơn vị "
            "(54 × 30 = 1620).",
        ]),

        ("h3", "Câu 2"),
        ("bullets", [
            "**a) ĐÚNG.** 36 km/h = 36 : 3,6 = 10 m/s.",
            "**b) ĐÚNG.** Xe **chậm dần đều** và chuyển động theo chiều dương → gia tốc **ngược dấu** vận tốc → a = −2 m/s².",
            "**c) SAI.** Thời gian dừng: t = −v₀/a = −10/(−2) = **5 s**, không phải 10 s.",
            "**d) ĐÚNG.** v² − v₀² = 2ad → 0 − 100 = 2·(−2)·d → d = **25 m**.",
        ]),

        ("h2", "4.4. Lời giải chi tiết Phần III"),
        ("h3", "Câu 1 – 180 m"),
        F([
            "t = 2 phút = 120 s",
            "s = v · t = 1,5 · 120 = 180 m",
        ]),
        ("h3", "Câu 2 – 2 s"),
        F([
            "h = ½gt²  →  t = √(2h/g) = √(2·20/10) = √4 = 2 s",
        ]),

        ("h2", "4.5. Lời giải chi tiết Phần IV"),

        ("h3", "Câu 1 (1,50 điểm)"),
        P("**Tóm tắt:** s_AB = 36 km; v_ca nô/nước = 15 km/h; v_nước/bờ = 3 km/h."),
        P("**a) Xuôi dòng** – ca nô và nước chuyển động **cùng chiều**:"),
        F([
            "v_xuôi = v_ca nô/nước + v_nước/bờ = 15 + 3 = 18 km/h",
            "t_xuôi = s/v = 36/18 = 2 h",
        ]),
        P("**b) Ngược dòng** – ca nô và nước chuyển động **ngược chiều**:"),
        F([
            "v_ngược = 15 − 3 = 12 km/h",
            "t_ngược = 36/12 = 3 h",
        ]),
        P("**Đáp số:** a) 18 km/h và 2 h; b) 3 h."),
        C("warn", "Lỗi thường gặp",
         "Nhiều bài làm chỉ viết đáp số mà **không nêu công thức cộng vận tốc** – mất điểm trình bày. "
         "Cần ghi rõ: *“Ca nô xuôi dòng nên vận tốc so với bờ là tổng hai vận tốc thành phần”*."),

        ("h3", "Câu 2 (1,50 điểm)"),
        P("**Tóm tắt:** v₀ = 20 m/s; a = 2 m/s²; chọn chiều dương là chiều chuyển động."),
        P("**a) Công thức vận tốc và vận tốc sau 5 s:**"),
        F([
            "v = v₀ + a·t = 20 + 2t   (m/s)",
            "Tại t = 5 s:  v = 20 + 2·5 = 30 m/s",
        ]),
        P("**b) Quãng đường trong 5 s:**"),
        F([
            "d₅ = v₀t + ½at² = 20·5 + ½·2·5² = 100 + 25 = 125 m",
        ]),
        P("**Quãng đường trong giây thứ 5** = quãng đường sau 5 s trừ quãng đường sau 4 s:"),
        F([
            "d₄ = 20·4 + ½·2·4² = 80 + 16 = 96 m",
            "Δs = d₅ − d₄ = 125 − 96 = 29 m",
            "",
            "Kiểm tra: v(4 s) = 28 m/s ; v(5 s) = 30 m/s → v_tb = 29 m/s → Δs = 29 m ✓",
        ]),
        P("**Đáp số:** a) v = 20 + 2t (m/s), v(5 s) = 30 m/s; b) 125 m và 29 m."),
        C("tip", "Cách trình bày ăn trọn điểm tự luận",
         "Với mỗi ý, viết theo đúng ba bước: **(1)** công thức dạng chữ → **(2)** thay số → **(3)** kết quả kèm đơn vị. "
         "Ba bước này thường ứng với ba mức điểm 0,25 – 0,25 – 0,25. Chỉ ghi đáp số: mất 2/3 số điểm của ý đó."),

        ("h2", "4.6. Bảng quy đổi điểm tham khảo"),
        T(
         ["Phần", "Số ý đúng", "Điểm"],
         [["I", "18/18", "4,50"],
          ["I", "15/18", "3,75"],
          ["I", "12/18", "3,00"],
          ["II (mỗi câu)", "4/4 · 3/4 · 2/4 · 1/4", "1,00 · 0,50 · 0,25 · 0,10"],
          ["III", "2/2 · 1/2", "0,50 · 0,25"],
          ["IV", "Trọn vẹn 2 câu", "3,00"]],
         [26, 42, 32], align=["CENTER", "CENTER", "CENTER"]),
    ]

    # =====================================================================
    # PHỤ LỤC
    # =====================================================================
    B += [
        ("h1", "PHỤ LỤC · CHECKLIST TRƯỚC GIỜ THI"),
        ("h2", "A. Danh sách kiểm tra kiến thức"),
        P("Tự đánh dấu ✔ vào ô vuông nếu bạn có thể **nói ra thành lời** nội dung đó mà không cần mở vở."),
        T(
         ["✓", "Nội dung cần kiểm tra"],
         [["☐", "Kể tên 4 cuộc cách mạng công nghiệp kèm thành tựu Vật lí tương ứng"],
          ["☐", "Nêu 5 bước của phương pháp thực nghiệm"],
          ["☐", "Kể được ít nhất 6 nguy cơ mất an toàn và cách phòng tránh"],
          ["☐", "Đọc đúng 4 loại biển báo"],
          ["☐", "Viết đúng 6 dòng công thức sai số và quy tắc ghi kết quả"],
          ["☐", "Phân biệt độ dịch chuyển và quãng đường bằng bảng so sánh"],
          ["☐", "Đổi thành thạo km/h ↔ m/s (36 · 54 · 72)"],
          ["☐", "Viết và áp dụng công thức cộng vận tốc cho 3 trường hợp"],
          ["☐", "Nêu ưu – nhược điểm của cổng quang điện, giải thích vì sao cần 2 cổng"],
          ["☐", "Đọc độ dốc đồ thị d–t ra vận tốc"],
          ["☐", "Xác định dấu của gia tốc trong 4 tình huống thường gặp"],
          ["☐", "Viết đúng 4 công thức chuyển động thẳng biến đổi đều"],
          ["☐", "Giải thành thạo bài hãm phanh (kể cả khi t > t_dừng)"],
          ["☐", "Viết đúng 4 công thức rơi tự do và nhớ dãy 5 – 20 – 45 – 80"],
          ["☐", "Đọc lại bảng 15 bẫy ở mục 2.3"]],
         [6, 94], size=8.6, align=["CENTER", "LEFT"]),

        ("h2", "B. Danh sách kiểm tra dụng cụ"),
        ("bullets", [
            "Máy tính bỏ túi (không có chức năng soạn thảo văn bản), bút chì, tẩy, thước kẻ.",
            "Bút mực để ghi phần tự luận; **bút chì 2B** để tô trắc nghiệm.",
            "Giấy nháp – dùng để tóm tắt và tính toán, nhất là phần tự luận.",
            "Đồng hồ đeo tay để tự phân bổ thời gian (nếu được phép).",
        ]),

        ("h2", "C. Mười lời nhắc cuối cùng"),
        ("numbers", [
            "**Đọc lướt toàn đề 60 giây** trước khi làm – biết chỗ nào dễ, chỗ nào khó.",
            "Làm **Phần I trước**, mỗi câu tối đa 60 giây; câu nào lâu hơn thì đánh dấu quay lại.",
            "**Khoanh tròn đơn vị** trong đề khi đọc – đây là nơi bẫy nhiều nhất.",
            "Với bài tính toán, **viết công thức chữ trước** khi thay số.",
            "Kiểm tra **dấu của gia tốc** ngay sau khi xác định chiều dương.",
            "Bài hãm phanh: **luôn kiểm tra t có vượt quá t_dừng không**.",
            "Bài rơi tự do: nhớ quãng đường tỉ lệ với **bình phương** thời gian.",
            "Phần II: đừng bỏ trống ý nào – **đúng 3/4 vẫn được 0,5 điểm**.",
            "Phần IV: **không được bỏ trắng** – viết công thức vẫn có điểm.",
            "Dành **2 phút cuối** kiểm tra phiếu tô và đơn vị.",
        ]),

        ("h2", "D. Nguồn tham chiếu"),
        ("bullets", [
            "**Tài liệu gốc:** “MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I – MÔN VẬT LÍ LỚP 10 – NĂM HỌC 2026–2027” "
            "(file .docx do giáo viên cung cấp). Toàn bộ cấu trúc, số câu, mức độ và trọng số trong tài liệu này "
            "được lấy trực tiếp từ đó.",
            "**Chương trình:** Vật lí 10 – Chương trình GDPT 2018, bộ sách *Kết nối tri thức với cuộc sống* "
            "(Chương I: Bài 1–3; Chương II: Bài 4–10). Cấu trúc 10 đơn vị kiến thức trong ma trận khớp hoàn toàn "
            "với cấu trúc 10 bài của sách.",
            "**Quy chế chấm thi:** Cấu trúc định dạng đề thi và cách tính điểm phần trắc nghiệm Đúng–Sai theo "
            "Quyết định 764/QĐ-BGDĐT ngày 08/3/2024 của Bộ GD&ĐT (áp dụng từ kì thi 2025).",
        ]),
        P("*Tài liệu được biên soạn nhằm mục đích ôn tập. Đề minh hoạ ở Phần 3 được dựng bám sát ma trận gốc "
              "nhưng không phải đề thi chính thức.*", italic=True, color=(112, 122, 132)),
    ]
    return B
