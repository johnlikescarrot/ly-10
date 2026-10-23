# -*- coding: utf-8 -*-
"""Nội dung PHẦN 1 (Bài 6 – Bài 10) và PHẦN 2 (Tổng hợp – ghi nhớ nhanh)."""

from dsl import T, F, P, C


def blocks_b():
    B = []

    # ---------------------------------------------------------------- BÀI 6
    B += [
        ("h2", "Bài 6 · Thực hành: Đo tốc độ của vật chuyển động"),
        P("*Mức độ xuất hiện trong đề: 1 câu trắc nghiệm Nhận biết + 1 câu trả lời ngắn Thông hiểu – 12,9% "
              "(cùng nhóm với Bài 7).*"),
        ("h3", "1. Đồng hồ đo thời gian hiện số – các MODE cần nhớ"),
        T(
         ["Chế độ", "Chức năng"],
         [["**MODE A**", "Đo thời gian vật **đi qua cổng A** (từ lúc vật đi vào đến khi ra khỏi cổng)"],
          ["**MODE B**", "Đo thời gian vật **đi qua cổng B**"],
          ["**MODE A↔B**", "Đo thời gian vật **đi từ cổng A đến cổng B** (A bật đồng hồ, B tắt đồng hồ)"],
          ["**MODE T**", "Đo **chu kì T** của một dao động"],
          ["**Nút RESET**", "Đưa chỉ số đồng hồ về **0,000**"]],
         [22, 78]),
        ("h3", "2. Cổng quang điện và ưu – nhược điểm của phương án này"),
        P("**Cổng quang điện** là cảm biến quang: khi vật đi qua, chùm tia bị chắn và cảm biến ghi nhận, "
              "kích hoạt đồng hồ đếm thời gian."),
        T(
         ["Ưu điểm", "Nhược điểm"],
         [["Độ chính xác **cao** (đo tới mili giây), cảm biến có độ nhạy rất cao",
           "**Chi phí đắt** – giá thiết bị cao"],
          ["**Tự động**, loại bỏ sai số phản xạ khi bấm đồng hồ bằng tay",
           "Thiết bị **cồng kềnh**, lắp đặt phức tạp"],
          ["Kết quả **khách quan**, lặp lại được nhiều lần",
           "Đòi hỏi **căn chỉnh chính xác** khoảng cách và độ cao hai cổng"]],
         [50, 50]),
        ("h3", "3. Vì sao cần HAI cổng quang điện?"),
        ("bullets", [
            "Cổng thứ nhất **bật** đồng hồ, cổng thứ hai **tắt** đồng hồ → đo được **chính xác khoảng thời gian** "
            "vật đi hết đoạn đường giữa hai cổng.",
            "Khoảng cách giữa hai cổng (đọc trên thước gắn giá đỡ) chính là **quãng đường s** → tính được **tốc độ trung bình** v = s/t.",
            "Khi chuyển về MODE A hoặc MODE B, mỗi cổng đo thời gian vật **đi qua chính nó** → đo được "
            "**tốc độ tức thời** v = d/t với d là đường kính vật.",
        ]),
        ("h3", "4. Quy trình đo"),
        T(
         ["Mục tiêu", "Các bước"],
         [["**Đo tốc độ trung bình** giữa hai cổng",
           "① Đo khoảng cách hai cổng bằng thước → s. ② Chọn MODE A↔B. ③ Thả vật, đọc thời gian t. "
           "④ Lặp lại ≥ 5 lần. ⑤ v = s/t, lấy trung bình."],
          ["**Đo tốc độ tức thời** tại một cổng",
           "① Đo **đường kính d** của vật bằng **thước kẹp**. ② Chọn MODE A (hoặc B). ③ Thả vật, đọc thời gian t "
           "vật đi qua cổng. ④ v = d/t."]],
         [28, 72]),
        C("warn", "Phân biệt hai chữ t",
         "**Tốc độ trung bình** dùng **s** (khoảng cách hai cổng) chia cho **t** ở MODE A↔B. "
         "**Tốc độ tức thời** dùng **d** (đường kính vật) chia cho **t** ở MODE A. "
         "Đề hay đánh tráo hai chữ này – đọc kỹ đề trước khi thay số."),
        ("h3", "5. Nguồn sai số và cách khắc phục"),
        T(
         ["Nguồn sai số", "Cách khắc phục"],
         [["Đọc và đặt khoảng cách hai cổng chưa chính xác", "Căn chỉnh bằng thước, kiểm tra lại trước khi đo"],
          ["Sai số của dụng cụ đo thời gian", "Chọn thang đo phù hợp, kiểm tra pin, RESET về 0 trước mỗi lần đo"],
          ["Ma sát trên máng, vật không đi đúng tâm cổng", "Lau sạch máng, đặt vật đúng rãnh"],
          ["Chỉ đo một lần", "**Đo ít nhất 5 lần** rồi lấy giá trị trung bình, tính cả sai số"]],
         [45, 55]),
        ("qa", [
            ("Ưu điểm lớn nhất của đồng hồ hiện số + cổng quang điện so với đồng hồ bấm giây là gì?",
             "**Độ chính xác cao** và **loại bỏ sai số phản xạ** của người bấm."),
            ("Muốn đo tốc độ tức thời của viên bi khi đi qua cổng, cần đo thêm đại lượng nào?",
             "**Đường kính d** của viên bi (bằng thước kẹp)."),
        ]),

        # ---------------------------------------------------------------- BÀI 7
            ("h2", "Bài 7 · Đồ thị độ dịch chuyển – thời gian"),
            P("*Mức độ xuất hiện trong đề: 2 câu trắc nghiệm (1 Nhận biết + 1 Thông hiểu) + 2 ý Đúng–Sai – 12,9%.*"),
            ("h3", "1. Cách dựng đồ thị"),
            ("bullets", [
                "**Trục tung:** độ dịch chuyển d (m). **Trục hoành:** thời gian t (s).",
                "Lập **bảng giá trị (t, d)** từ số liệu đo → chọn **tỉ lệ xích** phù hợp → xác định các điểm → **nối** các điểm.",
            ]),
            ("h3", "2. Đọc đồ thị – bảng \"dịch\" hình dạng ra ý nghĩa"),
            T(
             ["Dạng đồ thị", "Ý nghĩa chuyển động"],
             [["Đường **nằm ngang** (song song trục Ot)", "Vật **đứng yên** – độ dịch chuyển không đổi"],
              ["Đường **thẳng xiên lên**", "Chuyển động **thẳng đều theo chiều dương**, v > 0"],
              ["Đường **thẳng xiên xuống**", "Chuyển động **thẳng đều ngược chiều dương**, v < 0"],
              ["Đường **cong** (parabol)", "Chuyển động **biến đổi đều** (vận tốc thay đổi)"],
              ["Hai đồ thị **cắt nhau**", "Hai vật **gặp nhau**: cùng vị trí, cùng thời điểm"],
              ["Đồ thị **trùng trục Ot** (d = 0)", "Vật đứng yên tại gốc toạ độ"]],
             [40, 60]),
            ("h3", "3. Độ dốc của đồ thị chính là vận tốc"),
            F([
                "v = Δd / Δt = (d₂ − d₁) / (t₂ − t₁)        (độ dốc của đồ thị d – t)",
                "",
                "Độ dốc dương  → v > 0 (đi theo chiều dương)",
                "Độ dốc âm    → v < 0 (đi ngược chiều dương)",
                "Độ dốc bằng 0 → v = 0 (đứng yên)",
            ], title="Công thức quan trọng nhất của bài"),
            C("tip", "Đọc đồ thị bằng mắt trong 5 giây",
             "Chọn **hai điểm** nằm đúng trên lưới ô vuông của đồ thị, đọc toạ độ rồi lấy **chênh lệch tung chia chênh lệch hoành**. "
             "Đừng bao giờ lấy toạ độ một điểm chia cho chính nó – chỉ đúng khi đồ thị đi qua gốc toạ độ."),
            ("h3", "4. Từ đồ thị suy ra quãng đường và độ dịch chuyển"),
            ("bullets", [
                "**Độ dịch chuyển** trong khoảng thời gian Δt: lấy **d cuối − d đầu**.",
                "**Quãng đường**: nếu đồ thị **gấp khúc** (vật đổi chiều), phải **cộng giá trị tuyệt đối** của từng đoạn: "
                "s = |Δd₁| + |Δd₂| + …",
            ]),
            P("**Ví dụ mẫu.** Đồ thị độ dịch chuyển – thời gian của một ô tô là đường thẳng đi qua gốc toạ độ và điểm "
                  "(t = 2 h; d = 120 km). Tính tốc độ của ô tô."),
            F([
                "v = (120 − 0) / (2 − 0) = 60 km/h",
            ]),
            P("**Ví dụ ngược.** Một vật chuyển động thẳng đều với vận tốc 5 m/s, xuất phát từ gốc toạ độ lúc t = 0. "
                  "Viết phương trình độ dịch chuyển và cho biết đồ thị có dạng gì."),
            F([
                "d = v·t = 5t   (m)   →   đồ thị là đường thẳng đi qua gốc, độ dốc 5",
            ]),
            C("warn", "Bẫy: đơn vị thời gian",
             "Đề rất hay cho thời gian bằng **phút** hoặc **giờ** nhưng vận tốc bằng **m/s**. "
             "Luôn đổi về **một hệ đơn vị** trước khi chia. 2 h = 7200 s; 30 phút = 1800 s."),
            ("qa", [
                ("Trên đồ thị d – t, vật đứng yên được biểu diễn thế nào?",
                 "Bằng một **đường thẳng nằm ngang** song song với trục thời gian."),
                ("Độ dốc của đồ thị d – t cho biết đại lượng nào?",
                 "**Vận tốc** của vật."),
            ]),

            # ------------------------------------------------------------ BÀI 8
            ("h2", "Bài 8 · Chuyển động biến đổi. Gia tốc"),
            P("*Mức độ xuất hiện trong đề: 2 câu trắc nghiệm (1 Nhận biết + 1 Thông hiểu) – 6,5%. "
                  "Đây là bài \"bản lề\": hiểu gia tốc mới hiểu được Bài 9 và Bài 10.*"),
            ("h3", "1. Chuyển động biến đổi"),
            P("**Chuyển động biến đổi** là chuyển động có **vận tốc thay đổi theo thời gian** – thay đổi về "
                  "**độ lớn**, về **phương**, **chiều**, hoặc cả ba."),
            ("h3", "2. Gia tốc"),
            P("**Gia tốc** là đại lượng **vectơ**, đặc trưng cho **sự biến thiên nhanh hay chậm của vận tốc**."),
            F([
                "a = Δv / Δt = (v − v₀) / (t − t₀)",
                "",
                "Đơn vị: m/s²   ·   Ý nghĩa: 1 m/s² nghĩa là mỗi giây vận tốc biến thiên 1 m/s",
            ], title="Định nghĩa gia tốc"),
            ("h3", "3. Quan hệ phương – chiều giữa gia tốc và vận tốc"),
            T(
             ["Quan hệ (chuyển động thẳng)", "Độ lớn vận tốc", "Loại chuyển động"],
             [["vectơ a **cùng chiều** với vectơ v", "**tăng đều**", "**Nhanh dần đều**"],
              ["vectơ a **ngược chiều** với vectơ v", "**giảm đều**", "**Chậm dần đều**"],
              ["a = 0 (hoặc a cùng phương, độ lớn 0)", "**không đổi**", "**Thẳng đều**"]],
             [40, 25, 35]),
            C("tip", "Quy tắc dấu – chỉ cần nhớ một câu",
             "**“Cùng dấu thì nhanh dần, trái dấu thì chậm dần.”** "
             "Xét dấu của v và a **trong hệ quy chiếu đã chọn**: v > 0 và a > 0 → nhanh dần; "
             "v > 0 và a < 0 → chậm dần; v < 0 và a < 0 → nhanh dần (theo chiều âm)."),
            T(
             ["Trường hợp", "v", "a", "Kết luận"],
             [["Xe tăng tốc theo chiều dương", "+", "+", "Nhanh dần đều"],
              ["Xe hãm phanh đang chạy theo chiều dương", "+", "−", "Chậm dần đều"],
              ["Vật rơi tự do (chiều dương hướng xuống)", "+", "+", "Nhanh dần đều"],
              ["Vật ném thẳng đứng lên (chiều dương hướng lên)", "+", "−", "Chậm dần đều"]],
             [46, 10, 10, 34],
             align=["LEFT", "CENTER", "CENTER", "LEFT"]),
            ("h3", "4. Ví dụ mẫu"),
            P("**Đề:** Một xe đang chạy với vận tốc 10 m/s thì tăng tốc, sau 5 s đạt 20 m/s. Tính gia tốc của xe."),
            F([
                "a = (v − v₀)/Δt = (20 − 10)/5 = 2 m/s²",
            ]),
            P("**Đề ngược:** Một xe đang chạy 20 m/s thì hãm phanh, sau 4 s vận tốc còn 8 m/s. Tính gia tốc."),
            F([
                "a = (8 − 20)/4 = −3 m/s²   →  a < 0, v > 0: xe chậm dần đều",
            ]),
            ("qa", [
                ("Gia tốc là đại lượng vô hướng hay vectơ?",
                 "**Vectơ.** Đặc trưng cho sự biến thiên của vận tốc theo thời gian."),
                ("Đơn vị của gia tốc là gì?",
                 "**m/s²** (mét trên giây bình phương)."),
            ]),

            # ------------------------------------------------------------ BÀI 9
            ("h2", "Bài 9 · Chuyển động thẳng biến đổi đều"),
            P("*Mức độ xuất hiện trong đề: **9 lượt hỏi (29,0%) – lớn nhất toàn đề**, gồm 3 câu trắc nghiệm, "
                  "4 ý Đúng–Sai và 2 ý tự luận Vận dụng. Đây là bài quyết định điểm số.*"),
            ("h3", "1. Định nghĩa"),
            ("bullets", [
                "**Chuyển động thẳng biến đổi đều:** quỹ đạo là **đường thẳng** và **gia tốc không đổi** "
                "(vận tốc biến thiên đều theo thời gian).",
                "**Nhanh dần đều:** a cùng chiều v, độ lớn vận tốc **tăng đều**.",
                "**Chậm dần đều:** a ngược chiều v, độ lớn vận tốc **giảm đều**.",
            ]),
            ("h3", "2. Bốn công thức – học như học bảng cửu chương"),
            T(
             ["Đại lượng", "Công thức", "Khi nào dùng"],
             [["**Vận tốc**", "v = v₀ + a·t", "Khi biết thời gian"],
              ["**Độ dịch chuyển**", "d = v₀·t + ½·a·t²", "Khi biết thời gian"],
              ["**Hệ thức độc lập thời gian**", "v² − v₀² = 2·a·d", "Khi **không** cho thời gian"],
              ["**Vận tốc trung bình**", "v_tb = (v₀ + v)/2 ;  d = (v₀ + v)·t/2", "Chỉ đúng khi a không đổi"]],
             [30, 40, 30]),
            C("tip", "Mẹo chọn công thức trong 5 giây",
             "Nhìn xem đề **cho gì** và **hỏi gì**, rồi chọn công thức **không chứa đại lượng không có** trong đề. "
             "Đề không cho t → dùng **v² − v₀² = 2ad**. Đề cho t và hỏi v → dùng **v = v₀ + at**. "
             "Đây là kỹ năng quan trọng hơn việc học thuộc lòng."),
            ("h3", "3. Hai lưu ý sống còn khi thay số"),
            ("bullets", [
                "**Chọn chiều dương** trước, rồi mới gán dấu cho v₀, v, a, d. Chậm dần đều → **a trái dấu v₀**.",
                "Khi vật **không đổi chiều**, quãng đường **s = |d|**. Nếu vật đổi chiều, phải chia thành hai giai đoạn.",
                "Khi vật **dừng lại** ở bài hãm phanh: v = 0, thời gian dừng **t_dừng = −v₀/a** (a âm nên t dương). "
                "**Không** dùng công thức cho thời gian lớn hơn t_dừng – vật đã đứng yên.",
            ]),
            C("warn", "Bẫy chết người của bài hãm phanh",
             "Xe chạy 10 m/s, hãm với a = −2 m/s². Hỏi quãng đường đi được trong **10 s**? "
             "Nhiều bạn thay t = 10: d = 10·10 − ½·2·100 = 0 m → sai! Thực tế xe **dừng sau 5 s** và đi được **25 m**. "
             "Khi t > t_dừng, phải dùng t = t_dừng."),
            ("h3", "4. Quãng đường đi trong giây thứ n"),
            F([
                "Δs(n) = s(n) − s(n − 1)              (quãng đường trong giây thứ n)",
                "",
                "Riêng khi v₀ = 0:   Δs(n) = ½·a·(2n − 1)   →  tỉ lệ 1 : 3 : 5 : 7 …",
            ]),
            ("h3", "5. Đồ thị vận tốc – thời gian (v – t)"),
            ("bullets", [
                "Là **đường thẳng** (vì a không đổi). **Độ dốc = gia tốc a**.",
                "**Diện tích** phần giới hạn bởi đồ thị và trục Ot **= độ dịch chuyển**.",
                "Đồ thị **cắt trục Ot** tại thời điểm vật **đổi chiều** chuyển động.",
            ]),
            ("h3", "6. Ba dạng bài mẫu – chép vào vở, thuộc lòng"),
            P("**Dạng 1 – Tăng tốc.** Xe đang chạy 20 m/s thì tăng tốc với a = 2 m/s². Tính vận tốc sau 5 s, "
                  "quãng đường đi được trong 5 s và trong giây thứ 5."),
            F([
                "v = v₀ + at = 20 + 2·5 = 30 m/s",
                "d = v₀t + ½at² = 20·5 + ½·2·25 = 100 + 25 = 125 m",
                "s(4) = 20·4 + ½·2·16 = 80 + 16 = 96 m",
                "Δs(giây thứ 5) = 125 − 96 = 29 m    (kiểm tra: v_tb = (28+30)/2 = 29 ✓)",
            ]),
            P("**Dạng 2 – Hãm phanh.** Xe chạy 10 m/s, hãm phanh với a = −2 m/s². Tính thời gian và quãng đường "
                  "từ lúc hãm đến khi dừng hẳn."),
            F([
                "Thời gian dừng:  v = v₀ + at = 0  →  t = −v₀/a = −10/(−2) = 5 s",
                "Quãng đường:     v² − v₀² = 2ad  →  0 − 100 = 2·(−2)·d  →  d = 25 m",
                "(hoặc d = v₀t + ½at² = 10·5 − ½·2·25 = 50 − 25 = 25 m)",
            ]),
            P("**Dạng 3 – Vận dụng cao.** Xe đang chạy 20 m/s thì hãm phanh với a = −0,5 m/s². "
                  "a) Bao lâu thì dừng? b) Đi được bao xa đến khi dừng? c) Quãng đường đi trong 10 s đầu?"),
            F([
                "a) t = −v₀/a = −20/(−0,5) = 40 s",
                "b) d = v₀t + ½at² = 20·40 − ½·0,5·1600 = 800 − 400 = 400 m",
                "c) Sau 10 s: d = 20·10 − ½·0,5·100 = 200 − 25 = 175 m   (10 s < 40 s nên công thức còn đúng)",
            ]),
            ("h3", "7. Bảng tra nhanh: cho gì – hỏi gì – dùng công thức nào"),
            T(
             ["Đề cho", "Đề hỏi", "Dùng"],
             [["v₀, a, t", "v", "v = v₀ + at"],
              ["v₀, a, t", "d, s", "d = v₀t + ½at²"],
              ["v₀, a, d", "v", "v² − v₀² = 2ad"],
              ["v₀, v, t", "d", "d = (v₀ + v)t/2"],
              ["v₀, a", "quãng đường đến khi dừng", "s = v₀²/(2|a|) ; t = v₀/|a|"]],
             [26, 30, 44]),
            ("qa", [
                ("Trong chuyển động thẳng nhanh dần đều, vectơ gia tốc cùng chiều hay ngược chiều vectơ vận tốc?",
                 "**Cùng chiều**."),
                ("Công thức nào dùng khi đề không cho thời gian?",
                 "**v² − v₀² = 2ad**."),
            ]),

            # ------------------------------------------------------------ BÀI 10
            ("h2", "Bài 10 · Sự rơi tự do"),
            P("*Mức độ xuất hiện trong đề: 3 câu trắc nghiệm (1 Nhận biết + 2 Thông hiểu) + 1 câu trả lời ngắn – 12,9%.*"),
            ("h3", "1. Định nghĩa và đặc điểm"),
            ("bullets", [
                "**Sự rơi tự do** là sự rơi của một vật **chỉ dưới tác dụng của trọng lực**.",
                "**Phương:** thẳng đứng. **Chiều:** từ trên xuống. **Tính chất:** **chuyển động nhanh dần đều** "
                "với gia tốc rơi tự do **g**.",
                "**Độ lớn g** phụ thuộc vĩ độ địa lí, độ cao và cấu trúc địa chất. Ở mặt đất, thường lấy "
                "**g ≈ 9,8 m/s²**, trong bài tập hay làm tròn **g = 10 m/s²**.",
            ]),
            ("h3", "2. Rơi tự do và rơi trong không khí"),
            T(
             ["Bối cảnh", "Đặc điểm", "Kết quả"],
             [["**Trong không khí**", "Có **lực cản** của không khí tác dụng", "Vật **nặng rơi nhanh hơn** vật nhẹ, cùng hình dạng. Tờ giấy vo tròn rơi nhanh hơn tờ giấy để phẳng"],
              ["**Trong ống chân không**", "**Không có** lực cản", "**Mọi vật rơi như nhau**, bất kể khối lượng (thí nghiệm Newton với lông chim và đồng xu)"]],
             [24, 26, 50]),
            C("key", "Kết luận cần nhớ",
             "Sự khác nhau về tốc độ rơi của các vật **không phải do khối lượng**, mà do **lực cản của không khí**. "
             "Khi loại bỏ lực cản, mọi vật rơi tự do **cùng một gia tốc g** – đây là dạng câu hỏi rất hay xuất hiện."),
            ("h3", "3. Bộ công thức (chọn chiều dương hướng xuống, v₀ = 0)"),
            F([
                "Vận tốc:            v = g·t",
                "Quãng đường:        s = h = ½·g·t²",
                "Liên hệ v – h:      v² = 2·g·h   →   v = √(2gh)",
                "Thời gian rơi:      t = √(2h/g)",
            ], title="Bốn công thức của rơi tự do"),
            P("Nếu vật được **ném thẳng đứng xuống** với vận tốc ban đầu v₀ thì dùng lại bộ công thức của "
                  "chuyển động nhanh dần đều: **v = v₀ + gt** và **h = v₀t + ½gt²**."),
            ("h3", "4. Ví dụ mẫu"),
            P("**Đề:** Thả một vật rơi tự do từ độ cao 45 m. Lấy g = 10 m/s². Tính thời gian rơi và vận tốc "
                  "của vật khi chạm đất."),
            F([
                "t = √(2h/g) = √(2·45/10) = √9 = 3 s",
                "v = g·t = 10·3 = 30 m/s     (hoặc v = √(2gh) = √900 = 30 m/s)",
            ]),
            P("**Đề ngược:** Một vật rơi tự do, sau 2 s chạm đất. Tính độ cao thả vật và vận tốc khi chạm đất (g = 10 m/s²)."),
            F([
                "h = ½gt² = ½·10·4 = 20 m",
                "v = gt = 20 m/s",
            ]),
            ("h3", "5. Ứng dụng: đo độ sâu của giếng"),
            P("Thả một hòn đá xuống giếng và bấm đồng hồ. Thời gian từ lúc thả đến khi **nghe tiếng vọng** "
                  "gồm **thời gian rơi** và **thời gian âm truyền lên**. Nếu bỏ qua thời gian truyền âm (giếng nông), "
                  "độ sâu tính bằng **h = ½gt²**."),
            C("warn", "Bẫy: nhầm công thức rơi tự do với chuyển động thẳng đều",
             "Rơi tự do là **nhanh dần đều**, nên quãng đường tỉ lệ với **t²**, không tỉ lệ với t. "
             "Sau 1 s rơi 5 m, sau 2 s rơi 20 m (không phải 10 m), sau 3 s rơi 45 m. "
             "Dãy **5 – 20 – 45 – 80** là dãy rất hay được hỏi."),
            ("qa", [
                ("Hai vật khác khối lượng, thả cùng lúc từ cùng độ cao trong chân không. Vật nào chạm đất trước?",
                 "**Cả hai chạm đất cùng lúc** – gia tốc rơi không phụ thuộc khối lượng."),
                ("Vận tốc của vật rơi tự do sau 3 s là bao nhiêu (g = 10 m/s²)?",
                 "v = gt = **30 m/s**."),
            ]),
        ]

    # =====================================================================
    # PHẦN 2
    # =====================================================================
    B += [
        ("h1", "PHẦN 2 · TỔNG HỢP & GHI NHỚ NHANH"),
        P("Phần này là \"trang cứu sinh\" trước giờ thi. Nếu chỉ còn 15 phút, hãy đọc đúng Phần 2."),

        ("h2", "2.1. Toàn bộ công thức trên một trang"),
        T(
         ["Chủ đề", "Công thức", "Ghi chú"],
         [["Giá trị trung bình", "Ā = (A₁ + … + Aₙ)/n", "n lần đo"],
          ["Sai số tuyệt đối", "ΔA = ΔĀ + ΔA_dc", "**Đừng quên ΔA_dc**"],
          ["Sai số tỉ đối", "δA = (ΔA/Ā)·100%", "δ nhỏ → đo chính xác"],
          ["Kết quả đo", "A = Ā ± ΔA", "Cùng bậc thập phân"],
          ["Tổng/hiệu (gián tiếp)", "ΔA = Δa + Δb", "Sai số tuyệt đối cộng"],
          ["Tích/thương (gián tiếp)", "δA = δa + δb", "Sai số tỉ đối cộng"],
          ["Tốc độ trung bình", "v_tb = s/Δt", "Vô hướng"],
          ["Vận tốc trung bình", "v = Δd/Δt", "Vectơ"],
          ["Đổi đơn vị", "1 m/s = 3,6 km/h", "km/h → m/s: ÷ 3,6"],
          ["Cộng vận tốc", "v₁₃ = v₁₂ + v₂₃", "Cùng chiều +, ngược chiều −"],
          ["Vuông góc", "v₁₃ = √(v₁₂² + v₂₃²)", "Pitago"],
          ["Gia tốc", "a = Δv/Δt = (v − v₀)/Δt", "m/s²"],
          ["Vận tốc CĐTBĐ", "v = v₀ + at", ""],
          ["Độ dịch chuyển", "d = v₀t + ½at²", ""],
          ["Không có t", "v² − v₀² = 2ad", ""],
          ["v_tb khi a không đổi", "v_tb = (v₀ + v)/2", "d = (v₀+v)t/2"],
          ["Rơi tự do – vận tốc", "v = gt", "v₀ = 0"],
          ["Rơi tự do – quãng đường", "h = ½gt²", ""],
          ["Rơi tự do – liên hệ", "v² = 2gh", ""],
          ["Rơi tự do – thời gian", "t = √(2h/g)", ""]],
         [26, 44, 30], size=8.2),

        ("h2", "2.2. Sơ đồ tư duy Động học"),
        P("Đọc sơ đồ theo chiều từ trên xuống: mỗi nhánh là một câu hỏi mà đề có thể đặt ra."),
        T(
         ["Tầng", "Nội dung", "Câu hỏi đề hay hỏi"],
         [["**① Mô tả chuyển động**", "Vị trí → Độ dịch chuyển / Quãng đường → Tốc độ / Vận tốc",
           "Đi được bao xa? Lệch bao xa? Nhanh hay chậm?"],
          ["**② Biểu diễn**", "Đồ thị d – t (độ dốc = vận tốc) · Đồ thị v – t (độ dốc = gia tốc, diện tích = độ dịch chuyển)",
           "Đọc/ vẽ đồ thị; tính vận tốc từ độ dốc"],
          ["**③ Nguyên nhân biến đổi**", "Gia tốc a = Δv/Δt; cùng chiều → nhanh dần, ngược chiều → chậm dần",
           "Xác định dấu a; phân loại chuyển động"],
          ["**④ Ba mô hình chuyển động**", "Thẳng đều (a = 0) · Thẳng biến đổi đều (a = const) · Rơi tự do (a = g)",
           "Chọn công thức phù hợp, giải bài toán"]],
         [24, 46, 30]),
        F([
            "ĐỘNG HỌC",
            "├── Đều:            v = const,  s = v·t",
            "├── Biến đổi đều:   v = v₀ + at ;  d = v₀t + ½at² ;  v² − v₀² = 2ad",
            "│   ├── Nhanh dần đều:  a cùng chiều v",
            "│   └── Chậm dần đều:   a ngược chiều v",
            "└── Rơi tự do:      a = g, v₀ = 0  →  v = gt ; h = ½gt² ; v² = 2gh",
        ], title="Cây công thức"),

        ("h2", "2.3. 15 bẫy thường gặp – đọc trước khi vào phòng thi"),
        T(
         ["#", "Cái bẫy", "Điều đúng"],
         [["1", "Cộng quãng đường để tìm độ dịch chuyển khi hai hướng vuông góc", "Dùng **Pitago**: |Δd| = √(d₁² + d₂²)"],
          ["2", "Cho rằng độ dịch chuyển luôn dương", "Độ dịch chuyển có thể **âm hoặc bằng 0**"],
          ["3", "Nhầm tốc độ (vô hướng) với vận tốc (vectơ)", "Tốc độ dùng **s**, vận tốc dùng **Δd**"],
          ["4", "Quên đổi km/h sang m/s", "**Chia 3,6**: 54 km/h = 15 m/s"],
          ["5", "Cộng vận tốc khi ngược chiều", "Ngược chiều phải **trừ**: v = |v₁ − v₂|"],
          ["6", "Cho rằng vật nặng rơi nhanh hơn trong chân không", "Trong chân không **mọi vật rơi như nhau**"],
          ["7", "Nghĩ quãng đường rơi tự do tỉ lệ với t", "Tỉ lệ với **t²**: 5 – 20 – 45 – 80 m"],
          ["8", "Quên dấu âm của a khi hãm phanh", "Chậm dần đều → **a trái dấu v₀**"],
          ["9", "Dùng t > t_dừng trong bài hãm phanh", "Xe đã dừng → chỉ tính đến **t_dừng**"],
          ["10", "Nhầm độ dốc đồ thị d–t với gia tốc", "Độ dốc đồ thị **d–t** là **vận tốc**"],
          ["11", "Nhầm độ dốc đồ thị v–t với vận tốc", "Độ dốc đồ thị **v–t** là **gia tốc**"],
          ["12", "Viết ΔA mà quên cộng sai số dụng cụ", "**ΔA = ΔĀ + ΔA_dc**"],
          ["13", "Cho rằng sai số tỉ đối lớn thì đo chính xác", "**Ngược lại**: δ nhỏ mới chính xác"],
          ["14", "Làm tròn Ā khác bậc thập phân với ΔA", "Ā làm tròn **cùng bậc** với ΔA"],
          ["15", "Đọc đồ thị bằng một điểm duy nhất", "Lấy **chênh lệch hai điểm**: Δd/Δt"]],
         [5, 50, 45], size=8.2, align=["CENTER", "LEFT", "LEFT"]),

        ("h2", "2.4. Bảng đổi đơn vị nhanh"),
        T(
         ["Đại lượng", "Đơn vị SI", "Quy đổi thường dùng"],
         [["Quãng đường, độ dịch chuyển", "mét (m)", "1 km = 1000 m ; 1 cm = 0,01 m"],
          ["Thời gian", "giây (s)", "1 min = 60 s ; 1 h = 3600 s"],
          ["Vận tốc", "m/s", "1 m/s = 3,6 km/h ; 36 km/h = 10 m/s"],
          ["Gia tốc", "m/s²", "1 cm/s² = 0,01 m/s²"],
          ["Gia tốc rơi tự do", "m/s²", "g ≈ 9,8 m/s² (bài tập thường lấy 10)"]],
         [34, 22, 44]),
    ]
    return B
