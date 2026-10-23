# -*- coding: utf-8 -*-
"""Phần E – Ngân hàng câu hỏi tự luyện + đáp án."""
from __future__ import annotations

from reportlab.platypus import Spacer, Table, TableStyle

from .style import (
    BG_SOFT, CONTENT_W, LINE, P, S, SPC, box, data_table, question,
)

BANK = [
    # (số, bài, đề, [4 phương án], đáp án)
    (1, "Bài 1", "Lĩnh vực nào sau đây <b>không</b> thuộc Vật lí?",
     ["Cơ học.", "Nhiệt học.", "Di truyền học.", "Quang học."], "C"),
    (2, "Bài 1", "Trí tuệ nhân tạo và Internet vạn vật gắn liền với cuộc cách mạng công nghiệp lần thứ",
     ["nhất.", "hai.", "ba.", "tư."], "D"),
    (3, "Bài 1", "Cách tiếp cận “quan sát – nêu giả thuyết – làm thí nghiệm – rút ra kết luận” thuộc phương pháp",
     ["thực nghiệm.", "lí thuyết.", "mô hình hoá.", "toán học."], "A"),
    (4, "Bài 2", "Việc làm nào sau đây <b>đảm bảo</b> an toàn trong phòng thực hành?",
     ["Dùng tay ướt cắm phích điện.", "Nếm thử hoá chất để nhận biết.",
      "Đeo găng tay khi tiếp xúc với hoá chất.", "Đùa nghịch trong phòng thí nghiệm."], "C"),
    (5, "Bài 2", "Biển báo hình tam giác đều, viền đỏ, nền vàng có ý nghĩa là biển",
     ["cấm.", "chỉ dẫn.", "bắt buộc.", "cảnh báo."], "D"),
    (6, "Bài 2", "Khi xảy ra cháy do chập điện, việc đầu tiên cần làm là",
     ["ngắt nguồn điện rồi dùng bình chữa cháy.", "dùng nước dập lửa ngay.",
      "chạy ra ngoài và không báo ai.", "mở toang cửa cho khói thoát ra."], "A"),
    (7, "Bài 3", "Phép đo nào sau đây là phép đo <b>trực tiếp</b>?",
     ["Dùng thước đo chiều dài của vật.", "Đo s và t rồi tính vận tốc.",
      "Đo khối lượng và thể tích rồi tính khối lượng riêng.", "Đo đường kính rồi tính chu vi."], "A"),
    (8, "Bài 3", "Thước có độ chia nhỏ nhất 1 mm. Sai số dụng cụ của thước thường được lấy bằng",
     ["1 mm.", "2 mm.", "0,5 mm.", "0,1 mm."], "C"),
    (9, "Bài 3", "Một phép đo có sai số tuyệt đối ΔA = 0,2 cm và giá trị trung bình Ā = 10,0 cm. "
                 "Sai số tỉ đối của phép đo là",
     ["0,2%.", "2%.", "20%.", "5%."], "B"),
    (10, "Bài 4", "Một vật đi 4 km về hướng Đông rồi 3 km về hướng Nam. Quãng đường và độ lớn độ dịch chuyển là",
     ["7 km và 7 km.", "7 km và 5 km.", "5 km và 7 km.", "4 km và 3 km."], "B"),
    (11, "Bài 4", "Một vật chuyển động trên đường tròn bán kính 7 m và đi được nửa vòng. "
                  "Quãng đường và độ lớn độ dịch chuyển là",
     ["22 m và 14 m.", "14 m và 22 m.", "44 m và 0.", "22 m và 0."], "A"),
    (12, "Bài 4", "Phát biểu nào sau đây <b>đúng</b>?",
     ["Độ dịch chuyển luôn dương.", "Độ lớn độ dịch chuyển luôn bằng quãng đường.",
      "Quãng đường luôn dương hoặc bằng 0.", "Độ dịch chuyển là đại lượng vô hướng."], "C"),
    (13, "Bài 5", "Vận tốc 54 km/h bằng",
     ["5,4 m/s.", "15 m/s.", "54 m/s.", "150 m/s."], "B"),
    (14, "Bài 5", "Một người đi 30 m trong 10 s rồi đi tiếp 20 m trong 5 s. Tốc độ trung bình của người đó là",
     ["3,33 m/s.", "3 m/s.", "4 m/s.", "2,5 m/s."], "A"),
    (15, "Bài 5", "Thuyền đi ngược dòng với tốc độ 12 km/h so với bờ, nước chảy với tốc độ 3 km/h. "
                  "Tốc độ của thuyền so với nước là",
     ["9 km/h.", "4 km/h.", "12 km/h.", "15 km/h."], "D"),
    (16, "Bài 6", "Để đo khoảng thời gian vật đi từ cổng quang A đến cổng quang B, ta chọn chế độ",
     ["MODE A.", "MODE B.", "MODE A + B.", "MODE A ↔ B."], "D"),
    (17, "Bài 6", "Ưu điểm chính của cổng quang điện so với đồng hồ bấm giây là",
     ["giá thành rẻ hơn.", "giảm sai số do phản xạ của người đo.",
      "không cần nguồn điện.", "đo được mọi vật ở mọi kích thước."], "B"),
    (18, "Bài 6", "Để đo tốc độ tức thời của vật tại một cổng quang điện, người ta dùng",
     ["thước dây.", "cân điện tử.", "tấm chắn sáng có bề rộng d.", "nhiệt kế."], "C"),
    (19, "Bài 7", "Đồ thị độ dịch chuyển – thời gian của một vật đứng yên là",
     ["đường thẳng dốc lên.", "đường nằm ngang.", "đường thẳng dốc xuống.", "đường cong."], "B"),
    (20, "Bài 7", "Trên đồ thị độ dịch chuyển – thời gian, một đoạn thẳng dốc xuống cho biết vật",
     ["đứng yên.", "chuyển động nhanh dần đều.", "chuyển động ngược chiều dương.", "chuyển động chậm dần đều."], "C"),
    (21, "Bài 7", "Đồ thị độ dịch chuyển – thời gian là đường thẳng đi qua gốc toạ độ; tại t = 5 s thì d = 25 m. "
                  "Vận tốc của vật là",
     ["2 m/s.", "25 m/s.", "125 m/s.", "5 m/s."], "D"),
    (22, "Bài 8", "Một xe tăng tốc từ 2 m/s lên 8 m/s trong 3 s. Gia tốc của xe là",
     ["2 m/s².", "3 m/s².", "6 m/s².", "10 m/s²."], "A"),
    (23, "Bài 8", "Xe đang chạy với vận tốc 10 m/s thì hãm phanh, chuyển động chậm dần đều với gia tốc −2 m/s². "
                  "Thời gian từ lúc hãm đến khi dừng là",
     ["2 s.", "5 s.", "10 s.", "20 s."], "B"),
    (24, "Bài 8", "Phát biểu nào sau đây <b>đúng</b>?",
     ["Gia tốc luôn cùng chiều với vận tốc.", "Gia tốc luôn dương.",
      "Vật chuyển động chậm dần thì gia tốc luôn âm.",
      "Gia tốc đặc trưng cho mức độ thay đổi của vận tốc."], "D"),
    (25, "Bài 9", "Một vật bắt đầu chuyển động nhanh dần đều từ trạng thái đứng yên với a = 2 m/s². "
                  "Sau 3 s, vận tốc và quãng đường của vật là",
     ["6 m/s và 9 m.", "6 m/s và 18 m.", "3 m/s và 9 m.", "2 m/s và 6 m."], "A"),
    (26, "Bài 9", "Ô tô đang chạy với vận tốc 10 m/s thì hãm phanh, chuyển động chậm dần đều với a = −2 m/s². "
                  "Quãng đường xe đi được đến khi dừng là",
     ["10 m.", "20 m.", "25 m.", "50 m."], "C"),
    (27, "Bài 9", "Vật chuyển động nhanh dần đều với vận tốc đầu bằng 0, gia tốc 2 m/s². "
                  "Quãng đường vật đi được trong giây thứ 2 là",
     ["1 m.", "4 m.", "3 m.", "5 m."], "C"),
    (28, "Bài 10", "Một vật rơi tự do trong 5 s. Lấy g = 10 m/s². Quãng đường rơi và vận tốc khi kết thúc 5 s là",
     ["125 m và 50 m/s.", "50 m và 125 m/s.", "250 m và 50 m/s.", "125 m và 25 m/s."], "A"),
    (29, "Bài 10", "Một vật rơi tự do từ độ cao 20 m. Lấy g = 10 m/s². Thời gian rơi của vật là",
     ["1 s.", "2 s.", "4 s.", "20 s."], "B"),
    (30, "Bài 10", "Quãng đường rơi tự do trong 1 s, 2 s, 3 s đầu tiên tỉ lệ với",
     ["1 : 2 : 3.", "1 : 3 : 5.", "1 : 4 : 9.", "1 : 1 : 1."], "C"),
]

EXERCISES = [
    ("Đổi đơn vị: 90 km/h ra m/s; 15 m/s ra km/h.",
     "90 km/h = 25 m/s; 15 m/s = 54 km/h."),
    ("Một người đi 6 km về hướng Đông rồi 8 km về hướng Bắc. Tính quãng đường và độ lớn độ dịch chuyển.",
     "s = 14 km; d = √(6² + 8²) = 10 km (hướng Đông – Bắc)."),
    ("Ca nô chạy 10 m/s so với nước, nước chảy 4 m/s so với bờ. Tính tốc độ ca nô so với bờ khi xuôi dòng, "
     "ngược dòng và khi chạy vuông góc với dòng nước.",
     "Xuôi: 14 m/s; ngược: 6 m/s; vuông góc: √(10² + 4²) ≈ 10,8 m/s."),
    ("Xe đạp đang chạy 5 m/s thì tăng tốc đều với a = 2 m/s². Tính vận tốc và quãng đường sau 6 s.",
     "v = 5 + 2·6 = 17 m/s; s = 5·6 + ½·2·36 = 66 m."),
    ("Ô tô đang chạy 72 km/h thì hãm phanh, chuyển động chậm dần đều với a = −4 m/s². "
     "Tính thời gian hãm và quãng đường đi được đến khi dừng.",
     "72 km/h = 20 m/s; t = 20/4 = 5 s; s = 20²/(2·4) = 50 m."),
    ("Vật rơi tự do từ độ cao 80 m, g = 10 m/s². Tính thời gian rơi, vận tốc chạm đất và quãng đường "
     "rơi trong giây cuối.",
     "t = √(2·80/10) = 4 s; v = 40 m/s; giây cuối: 80 − ½·10·3² = 80 − 45 = 35 m."),
    ("Đồ thị d – t gồm các đoạn: (0 s; 0 m) → (2 s; 10 m) → (5 s; 10 m) → (7 s; 0 m). "
     "Tính vận tốc từng đoạn, quãng đường và độ dịch chuyển trong 7 s.",
     "v₁ = 5 m/s; v₂ = 0; v₃ = −5 m/s. s = 10 + 0 + 10 = 20 m; Δd = 0 m."),
    ("Đo chiều dài 5 lần được 2,45; 2,47; 2,46; 2,45; 2,47 (m), thước có ĐCNN 0,01 m. "
     "Tính giá trị trung bình, sai số tuyệt đối và viết kết quả đo.",
     "Ā = 2,46 m; ΔĀ = 0,008 m; ΔA<sub>dc</sub> = 0,005 m; ΔA = 0,013 ≈ 0,01 m. "
     "Kết quả: L = 2,46 ± 0,01 m; δ ≈ 0,53%."),
]


def part_e():
    f = []
    f.append(P("PHẦN E · NGÂN HÀNG 30 CÂU TỰ LUYỆN THEO BÀI", "h1"))
    f.append(P("Làm hết 30 câu này (mỗi bài 3 câu) là em đã phủ kín toàn bộ nội dung có thể ra trong đề. "
               "Đáp án in ngay bên dưới – hãy che lại khi làm.", "body"))
    for num, lesson, stem, opts, ans in BANK:
        f += question(num, f"<font color='#5A6B7B'>[{lesson}]</font> {stem}", opts, cols=2)

    f.append(SPC(4))
    f.append(P("E1. Đáp án 30 câu tự luyện", "h2"))
    rows = []
    for i in range(0, 30, 5):
        chunk = BANK[i : i + 5]
        rows.append([f"Câu {n}" for n, *_ in chunk])
        rows.append([f"<b>{a}</b>" for *_, a in chunk])
    data = [[P(c, "tbl_c") for c in r] for r in rows]
    t = Table(data, colWidths=[CONTENT_W / 5] * 5, hAlign="LEFT")
    cmds = [("GRID", (0, 0), (-1, -1), 0.5, LINE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for r in range(0, len(data), 2):
        cmds.append(("BACKGROUND", (0, r), (-1, r), BG_SOFT))
    t.setStyle(TableStyle(cmds))
    f.append(t)
    f.append(SPC(8))

    from .style import cond
    f.append(cond(470))
    f.append(P("PHẦN E2 · 8 BÀI TỰ LUẬN TỰ LUYỆN", "h2"))
    f.append(P("Trình bày ra giấy theo đúng 4 bước: chọn chiều dương – tóm tắt và đổi đơn vị – viết công thức – "
               "thay số và kết luận.", "body"))
    for i, (q, _) in enumerate(EXERCISES, 1):
        f.append(P(f"<b>Bài {i}.</b> {q}", "q"))
    f.append(SPC(4))
    f.append(P("E3. Đáp số", "h2"))
    for i, (_, a) in enumerate(EXERCISES, 1):
        f.append(P(f"<b>Bài {i}.</b> {a}", "sol"))
    f.append(SPC(4))
    return f
