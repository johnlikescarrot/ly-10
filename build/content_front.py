# -*- coding: utf-8 -*-
"""Phần mở đầu: hướng dẫn sử dụng + phân tích ma trận."""

from reportlab.lib.units import cm
from doc_kit import *  # noqa
from reportlab.platypus import Paragraph, Spacer, PageBreak, NextPageTemplate, Table, TableStyle


def build(d: Doc):
    # ---------------------------------------------------------------- TOC
    d.h1("MỤC LỤC", kicker="ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I · VẬT LÍ 10", toc=False)
    d.story.append(build_toc())
    d.p("<i>Mẹo: bấm vào một dòng trong mục lục để nhảy tới đúng trang (bản PDF có bookmark).</i>",
        "Small")
    d.pb()

    # ------------------------------------------------------- hướng dẫn
    d.h1("HƯỚNG DẪN SỬ DỤNG TÀI LIỆU", kicker="Mở đầu")
    d.lead("Một tài liệu – bốn lớp công cụ: hiểu bản chất, nhớ công thức, tránh bẫy, luyện đúng dạng.")
    d.p("Tài liệu này được biên soạn bám sát <b>Ma trận và Đặc tả đề kiểm tra giữa học kì I – môn Vật lí lớp 10, "
        "năm học 2026 – 2027</b>. Mọi đơn vị kiến thức, mức độ nhận thức và số lượng câu hỏi trong tài liệu đều "
        "được đối chiếu với văn bản gốc, để bạn không học thừa và không bỏ sót.")

    d.box("note",
          "Văn bản gốc bạn cung cấp là <b>ma trận + đặc tả</b> (quy định nội dung, mức độ và số câu của từng phần), "
          "không kèm danh sách câu hỏi cụ thể. Vì vậy <b>Phần C</b> của tài liệu là bộ câu hỏi được biên soạn "
          "<b>bám 1:1 theo đúng ma trận</b> (đủ 18 câu Phần I, 2 câu đúng/sai × 4 ý, 2 câu Phần III, 3 câu Phần IV), "
          "kèm đáp án và lời giải chi tiết. Nếu thầy/cô phát đề chính thức, bạn chỉ cần ghép nội dung tương ứng "
          "vào đúng ô của ma trận là có ngay lời giải.",
          title="VỀ NGUỒN TÀI LIỆU")

    d.table(
        ["Lớp nội dung", "Bạn dùng để…", "Cách học hiệu quả"],
        [
            ["<b>1. Phân tích ma trận</b>", "Biết đề gồm những phần nào, bài nào chiếm nhiều điểm.",
             "Đọc 1 lần đầu, quay lại khi lập kế hoạch ôn."],
            ["<b>2. Lý thuyết 10 chuyên đề</b>", "Hiểu bản chất + nhớ công thức + xem ví dụ mẫu.",
             "Mỗi ngày 2 chuyên đề: đọc – gấp sách – tự viết lại công thức."],
            ["<b>3. Bảng công thức & bẫy</b>", "Ôn nhanh 10 phút trước khi luyện đề và trước giờ thi.",
             "In riêng 2 trang này để cầm tay."],
            ["<b>4. Bộ đề luyện + lời giải</b>", "Tập đúng áp lực: 50 phút, đúng cấu trúc 4 phần.",
             "Làm bài trước, chỉ mở lời giải sau khi hết giờ."],
        ],
        widths=[4.4 * cm, 6.6 * cm, 6.1 * cm])

    d.h2("Quy ước mức độ nhận thức")
    d.table(
        ["Kí hiệu", "Mức độ", "Nghĩa là bạn phải…", "Dạng câu thường gặp"],
        [
            ["<b>NB</b>", "Nhận biết", "Nhớ – phát biểu lại – nhận ra", "Định nghĩa, đơn vị, công thức, biển báo"],
            ["<b>TH</b>", "Thông hiểu", "Giải thích – so sánh – áp dụng 1 bước", "Tính toán đơn giản, đọc đồ thị, phân biệt"],
            ["<b>VD</b>", "Vận dụng", "Giải bài toán 2–3 bước", "Hãm phanh, gặp nhau, tổng hợp vận tốc"],
            ["<b>VDC</b>", "Vận dụng cao", "Bài toán tổng hợp, nhiều đại lượng", "Đổi chiều chuyển động, bài toán kết hợp"],
        ],
        widths=[1.9 * cm, 2.9 * cm, 5.6 * cm, 6.7 * cm], aligns=["C", "C", "L", "L"])

    d.h2("Từ viết tắt dùng trong tài liệu")
    d.table(
        ["Viết tắt", "Nghĩa", "Viết tắt", "Nghĩa"],
        [
            ["<b>NB / TH</b>", "Nhận biết / Thông hiểu", "<b>VD / VDC</b>", "Vận dụng / Vận dụng cao"],
            ["<b>P.I – P.IV</b>", "Phần I → Phần IV của đề", "<b>ĐCNN</b>", "Độ chia nhỏ nhất của dụng cụ đo"],
            ["<b>CĐTBĐĐ</b>", "Chuyển động thẳng biến đổi đều", "<b>Δd, Δx</b>", "Độ dịch chuyển"],
        ],
        widths=[2.6 * cm, 5.6 * cm, 2.6 * cm, 6.3 * cm],
        aligns=["C", "L", "C", "L"], font_size=8.2)

    d.h2("Bốn loại hộp bạn sẽ gặp")
    d.table(
        ["Hộp", "Chứa gì", "Cách dùng"],
        [
            ["<font color='#1F5FA8'><b>■ CẦN NHỚ</b></font>",
             "Khái niệm, định nghĩa, công thức gốc", "Gấp tài liệu, tự phát biểu lại"],
            ["<font color='#1E8449'><b>■ VÍ DỤ MẪU</b></font>",
             "Bài giải mẫu từng bước", "Che lời giải, tự làm rồi đối chiếu"],
            ["<font color='#B03A2E'><b>■ BẪY THƯỜNG GẶP</b></font>",
             "Lỗi mất điểm phổ biến nhất", "Đọc lại ngay trước khi làm đề"],
            ["<font color='#B9770E'><b>■ MẸO NHỚ</b></font>",
             "Câu chữ ngắn, hình ảnh hoá", "Học thuộc để tái hiện nhanh"],
        ],
        widths=[4.5 * cm, 6.4 * cm, 6.2 * cm], font_size=8.2)

    d.h2("Tự chẩn đoán trước khi học: bạn đang ở đâu?")
    d.p("Đọc 8 câu hỏi dưới đây và tự trả lời <b>“làm được ngay, không cần xem tài liệu”</b> hay <b>“chưa chắc”</b>. "
        "Mỗi câu “chưa chắc” tương ứng một chuyên đề cần học kĩ – hãy đánh dấu vào cột cuối để lập lộ trình riêng.")
    d.table(
        ["#", "Câu hỏi tự kiểm tra", "Nếu “chưa chắc”, học ở"],
        [
            ["1", "Kể được 4 cuộc cách mạng công nghiệp gắn với thành tựu Vật lí nào?", "Chuyên đề 01"],
            ["2", "Phân biệt 4 nhóm biển báo an toàn chỉ bằng hình dạng và màu sắc?", "Chuyên đề 02"],
            ["3", "Ghi kết quả đo dạng A = Ā ± ΔA và tính sai số tỉ đối?", "Chuyên đề 03"],
            ["4", "Nêu một ví dụ vật đi rồi quay lại: quãng đường khác độ dịch chuyển thế nào?", "Chuyên đề 04"],
            ["5", "Ca nô xuôi dòng 10 m/s, nước chảy 2 m/s — vận tốc so với bờ bằng bao nhiêu?", "Chuyên đề 05"],
            ["6", "Nhìn đồ thị d–t, nói ngay vật đứng yên hay chuyển động, nhanh hay chậm?", "Chuyên đề 07"],
            ["7", "Viết 4 công thức của chuyển động thẳng biến đổi đều, không nhìn tài liệu?", "Chuyên đề 09"],
            ["8", "Vật rơi 45 m mất bao lâu? Quãng đường trong giây cuối là bao nhiêu?", "Chuyên đề 10"],
        ],
        widths=[0.9 * cm, 10.9 * cm, 5.3 * cm],
        aligns=["C", "L", "L"], font_size=8.3)
    d.box("tip",
          "Nếu “chưa chắc” từ 5 câu trở lên: đừng làm đề ngay. Hãy đi theo kế hoạch 7 ngày ở Phần E, "
          "mỗi ngày 2 chuyên đề. Nếu chỉ “chưa chắc” 1 – 2 câu: học lại đúng chuyên đề đó rồi làm đề luyện "
          "tập ngay trong 50 phút.",
          title="ĐỌC KẾT QUẢ THẾ NÀO")

    d.pb()

    # ------------------------------------------------------- ma trận
    d.h1("PHÂN TÍCH MA TRẬN & ĐẶC TẢ ĐỀ", kicker="Phần 0 · Hiểu “bản thiết kế” của đề")
    d.lead("Biết đề ra bao nhiêu câu ở mỗi bài = biết dồn sức vào đâu. Đây là bước quan trọng nhất trước khi học.")

    d.h2("0.1 · Cấu trúc đề thi")
    d.table(
        ["Phần", "Hình thức", "Số lượng", "Mức độ", "Ghi chú"],
        [
            ["<b>I</b>", "Trắc nghiệm nhiều lựa chọn", "18 câu", "10 Biết + 8 Hiểu",
             "Mỗi câu chọn 1 phương án đúng (A/B/C/D)"],
            ["<b>II</b>", "Trắc nghiệm đúng – sai", "2 câu × 4 ý", "6 Biết + 2 Hiểu",
             "Mỗi ý chọn Đúng hoặc Sai"],
            ["<b>III</b>", "Tự luận ngắn", "2 câu", "1 Biết + 1 Hiểu", "Trình bày lời giải"],
            ["<b>IV</b>", "Tự luận vận dụng", "3 ý/câu", "1 Hiểu + 2 Vận dụng", "Bài toán tổng hợp"],
        ],
        widths=[1.3 * cm, 5.2 * cm, 2.7 * cm, 3.5 * cm, 4.4 * cm], aligns=["C", "L", "C", "C", "L"])
    d.p("<b>Tổng:</b> 18 + 8 + 2 + 3 = <b>31 đơn vị hỏi</b> · Thời gian 50 phút · Tỉ lệ 70% trắc nghiệm – 30% tự luận.")

    d.h2("0.2 · Phân bố câu hỏi theo từng đơn vị kiến thức")
    d.p("Bảng dưới đây là số liệu <b>nguyên văn</b> từ ma trận của đề. Cột “Tổng” cho biết bài nào “nặng” nhất.")
    hdr1 = ["<b>Đơn vị kiến thức</b>", "<b>PHẦN I</b>", "", "<b>PHẦN II</b>", "", "<b>PHẦN III</b>", "",
            "<b>PHẦN IV</b>", "", "<b>Tổng</b>"]
    hdr2 = ["", "Biết", "Hiểu", "Biết", "Hiểu", "Biết", "Hiểu", "Hiểu", "Vận<br/>dụng", ""]
    data = [hdr1, hdr2]
    body_rows = [
        ["1.1 Làm quen với Vật lí", "1", "", "", "", "", "", "", "", "<b>1</b>"],
        ["1.2 Quy tắc an toàn phòng thực hành", "1", "1", "", "", "", "", "", "", "<b>2</b>"],
        ["1.3 Sai số phép đo – ghi kết quả", "1", "", "", "", "", "", "", "", "<b>1</b>"],
        ["2.1 Độ dịch chuyển &amp; quãng đường", "1", "2", "", "", "", "", "", "", "<b>3</b>"],
        ["2.2 Tốc độ và vận tốc", "1", "", "2", "", "1", "", "1", "", "<b>5</b>"],
        ["2.3 Đồ thị độ dịch chuyển – thời gian", "1", "1", "2", "", "", "", "", "", "<b>4</b>"],
        ["2.4 Chuyển động biến đổi. Gia tốc", "1", "1", "", "", "", "", "", "", "<b>2</b>"],
        ["2.5 Chuyển động thẳng biến đổi đều", "2", "1", "2", "2", "", "", "", "2", "<b>9</b>"],
        ["2.6 Sự rơi tự do", "1", "2", "", "", "", "1", "", "", "<b>4</b>"],
        ["<b>TỔNG</b>", "<b>10</b>", "<b>8</b>", "<b>6</b>", "<b>2</b>", "<b>1</b>", "<b>1</b>", "<b>1</b>",
         "<b>2</b>", "<b>31</b>"],
    ]
    data += body_rows

    bst = st("bst", fontSize=8.0, leading=10.6, alignment=TA_CENTER)
    hsm = st("hsm", fontName="VNSans-Bold", fontSize=7.5, leading=9.4,
             textColor=colors.white, alignment=TA_CENTER)
    lc = st("lc", fontSize=8.0, leading=10.6, alignment=TA_LEFT)
    tbl_data = []
    for ri, row in enumerate(data):
        line = []
        for ci, cell in enumerate(row):
            if cell == "":
                line.append("")
            elif ri == 0:
                line.append(Paragraph(cell, hsm))
            elif ri == 1:
                line.append(Paragraph("<b>%s</b>" % cell, hsm))
            else:
                line.append(Paragraph(F(cell), lc if ci == 0 else bst))
        tbl_data.append(line)

    widths_m = [5.15 * cm] + [1.14 * cm] * 8 + [1.30 * cm]
    t = Table(tbl_data, colWidths=widths_m, repeatRows=2)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 1), NAVY),
        ("SPAN", (0, 0), (0, 1)),
        ("SPAN", (1, 0), (2, 0)), ("SPAN", (3, 0), (4, 0)), ("SPAN", (5, 0), (6, 0)),
        ("SPAN", (7, 0), (8, 0)), ("SPAN", (9, 0), (9, 1)),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, len(tbl_data) - 1), (-1, len(tbl_data) - 1), BLUE_BG),
        ("LINEABOVE", (0, len(tbl_data) - 1), (-1, len(tbl_data) - 1), 0.9, NAVY),
    ]
    for i in range(2, len(tbl_data) - 1):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), SOFT))
    t.setStyle(TableStyle(style))
    d.story += [Spacer(1, 2), t, Spacer(1, 7)]
    d.p("<i>Ghi chú: “2” ở cột P.II là 2 ý thuộc cùng một câu đúng/sai; “2” ở cột P.IV.VD là 2 ý vận dụng.</i>", "Small")

    d.h2("0.3 · Ba nhận xét quyết định cách ôn")
    d.box("remember",
          "• <b>Động học chiếm 27/31 đơn vị hỏi</b> (87%). Phần “Mở đầu” (bài 1 – 3) chỉ có 4 câu, đều ở mức Biết – Hiểu, "
          "học 1 buổi là đủ điểm.\n\n"
          "• <b>Chuyển động thẳng biến đổi đều (2.5) là “xương sống”</b>: 9 đơn vị hỏi (nhiều nhất), gồm 2 ý đúng/sai ở "
          "Phần II và 2 ý vận dụng ở Phần IV – nơi phân loại điểm 9 và 10. Bắt buộc phải làm thành thạo 4 công thức và "
          "dạng bài hãm phanh.\n\n"
          "• <b>Tốc độ – vận tốc (2.2)</b> xuất hiện ở cả 4 phần, gồm công thức cộng vận tốc và bài toán hai vận tốc vuông góc. "
          "Đây là câu “chắc chắn có” ở phần tự luận vận dụng.",
          title="BA ĐIỂM MẤU CHỐT")

    d.h2("0.4 · Yêu cầu cần đạt rút gọn từ đặc tả")
    d.table(
        ["Bài", "Nhận biết (phải phát biểu được)", "Thông hiểu / Vận dụng (phải làm được)"],
        [
            ["1. Làm quen với Vật lí", "Đối tượng nghiên cứu; thành tựu gắn 4 cuộc cách mạng công nghiệp; "
             "các giai đoạn phát triển; phương pháp nghiên cứu.",
             "Hiểu và mô tả lại được quá trình nghiên cứu Vật lí."],
            ["2. An toàn phòng thực hành", "Nguy cơ mất an toàn; các quy tắc an toàn.",
             "Sử dụng được thiết bị thí nghiệm; đọc và hiểu biển báo."],
            ["3. Sai số phép đo", "Phép đo trực tiếp/gián tiếp; loại sai số; nguyên nhân; công thức giá trị trung bình, "
             "sai số tuyệt đối, sai số tỉ đối.",
             "Ghi đúng kết quả đo; tính sai số tuyệt đối và tỉ đối; tính giá trị đo."],
            ["4. Độ dịch chuyển &amp; quãng đường", "Định nghĩa độ dịch chuyển; so sánh với quãng đường.",
             "Xác định độ dịch chuyển, quãng đường; tính trong bài toán có đổi chiều."],
            ["5. Tốc độ và vận tốc", "Tốc độ trung bình, tốc độ tức thời, cách đo tốc độ; định nghĩa và công thức vận tốc; "
             "công thức cộng vận tốc.",
             "Tính tốc độ trung bình; phân biệt tốc độ – vận tốc; tổng hợp hai vận tốc cùng phương và vuông góc."],
            ["6. Thực hành đo tốc độ", "Ưu, nhược điểm của đồng hồ hiện số + cổng quang điện; cách sử dụng; "
             "ý nghĩa của hai cổng quang.",
             "Đo được tốc độ bằng dụng cụ thực hành."],
            ["7. Đồ thị độ dịch chuyển – thời gian", "Mô tả chuyển động từ đồ thị.",
             "Tính tốc độ từ độ dốc; xác định vị trí, vận tốc tại thời điểm bất kì; vẽ đồ thị."],
            ["8. Chuyển động biến đổi. Gia tốc", "Khái niệm chuyển động biến đổi; quan hệ phương – chiều của a và v; "
             "khái niệm, công thức, đơn vị gia tốc.",
             "Tính độ biến thiên vận tốc, gia tốc; phân biệt nhanh dần – chậm dần."],
            ["9. Chuyển động thẳng biến đổi đều", "Định nghĩa CĐTBĐĐ, nhanh dần đều, chậm dần đều; các công thức.",
             "Tính v, a, d; giải bài toán cơ bản và nâng cao."],
            ["10. Sự rơi tự do", "Định nghĩa; đặc điểm chuyển động rơi trong không khí; các công thức.",
             "Phân biệt rơi gần đúng tự do; tính thời gian, vận tốc, quãng đường, độ cao."],
        ],
        widths=[3.7 * cm, 6.9 * cm, 6.5 * cm], font_size=7.9)


