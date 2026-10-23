#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh (generate) ĐỀ CƯƠNG ÔN TẬP — VẬT LÝ LỚP 10 — KIỂM TRA GIỮA KÌ I (2026–2027)
Dựa trên tài liệu: MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I (Môn Vật lý lớp 10).
Output: PDF (fpdf2 + DejaVu Sans, hỗ trợ đầy đủ tiếng Việt & ký hiệu vật lý).
"""

from fpdf import FPDF

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
REG = FONT_DIR + "/DejaVuSans.ttf"
BOLD = FONT_DIR + "/DejaVuSans-Bold.ttf"

# ---- Palette ----
C_PRIMARY = (26, 58, 110)      # deep navy
C_ACCENT = (0, 110, 170)       # blue
C_TEXT = (45, 45, 45)
C_MUTED = (110, 110, 110)
C_FORMULA = (228, 238, 252)    # light blue
C_ANSWER = (232, 246, 232)     # light green
C_QUESTION = (255, 247, 224)   # light amber
C_TIP = (240, 230, 250)        # light violet
C_TABLE_HEAD = (40, 90, 140)
C_TABLE_ROW = (245, 248, 252)
C_BORDER = (180, 195, 215)
C_WARN = (180, 60, 30)

MARGIN = 15
PAGE_W = 210


class GuidePDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.set_auto_page_break(True, margin=16)
        self.add_font("DejaVu", "", REG)
        self.add_font("DejaVu", "B", BOLD)
        self.set_margins(MARGIN, 14, MARGIN)

    # ---------- low level ----------
    def set_font_pack(self, style="", size=10.5):
        self.set_font("DejaVu", style, size)

    def body(self, text, style="", size=10.5, color=C_TEXT, lh=5.4):
        self.set_font_pack(style, size)
        self.set_text_color(*color)
        self.multi_cell(0, lh, text, new_x="LMARGIN", new_y="NEXT")

    def hr(self, color=C_BORDER, width=0.3):
        self.set_draw_color(*color)
        self.set_line_width(width)
        self.line(MARGIN, self.get_y(), PAGE_W - MARGIN, self.get_y())

    # ---------- structural helpers ----------
    def section(self, title, level=0):
        """Colored section bar; registers a TOC entry."""
        self.start_section(title, level=level)
        self.ln(2)
        self.set_font_pack("B", 13)
        self.set_fill_color(*C_PRIMARY)
        self.set_text_color(255, 255, 255)
        self.cell(0, 9.5, title, border=0, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2.5)

    def sub(self, title):
        self.start_section(title, level=1)
        self.set_font_pack("B", 11)
        self.set_text_color(*C_PRIMARY)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*C_BORDER)
        self.set_line_width(0.3)
        y = self.get_y()
        self.line(MARGIN, y, PAGE_W - MARGIN, y)
        self.ln(2)

    def sub_sub(self, title):
        self.set_font_pack("B", 10.5)
        self.set_text_color(*C_ACCENT)
        self.cell(0, 6.5, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def tip_box(self, title, text, fill=C_TIP):
        self.set_fill_color(*fill)
        self.set_draw_color(*C_BORDER)
        self.set_font_pack("B", 10)
        self.set_text_color(*C_PRIMARY)
        x0, y0 = MARGIN, self.get_y()
        self.cell(0, 7, "  " + title, border="LR", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_font_pack("", 9.8)
        self.set_text_color(*C_TEXT)
        self.multi_cell(0, 5.2, text, border="LRB", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2.5)

    def formula_box(self, lines, title="Công thức cần nhớ"):
        self.set_fill_color(*C_FORMULA)
        self.set_draw_color(*C_BORDER)
        self.set_font_pack("B", 10)
        self.set_text_color(*C_PRIMARY)
        self.cell(0, 7, "  " + title, border="LR", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_font_pack("", 10.5)
        self.set_text_color(*C_TEXT)
        for ln in lines:
            self.multi_cell(0, 5.6, "      " + ln, border="LRB", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2.5)

    def qa_block(self, q, a, level="Biết", fill_q=C_QUESTION, fill_a=C_ANSWER):
        self.set_fill_color(*fill_q)
        self.set_draw_color(*C_BORDER)
        self.set_font_pack("B", 10.2)
        self.set_text_color(*C_TEXT)
        self.multi_cell(0, 5.6, "CÂU HỎI (mức độ: " + level + "): " + q,
                        border="LR", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(*fill_a)
        self.set_font_pack("", 9.8)
        self.set_text_color(*C_TEXT)
        self.multi_cell(0, 5.4, "ĐÁP ÁN: " + a, border="LRB", fill=True,
                        new_x="LMARGIN", new_y="NEXT")
        self.ln(2.5)

    def bullets(self, items, size=10.2, lh=5.4, indent=5):
        for it in items:
            self.set_font_pack("", size)
            self.set_text_color(*C_TEXT)
            self.cell(indent, lh, "•", new_x="RIGHT", new_y="TOP")
            self.multi_cell(0, lh, it, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def info_table(self, rows, head, widths, head_fill=C_TABLE_HEAD, size=9.5):
        """Simple grid table."""
        self.set_font_pack("B", size)
        self.set_fill_color(*head_fill)
        self.set_text_color(255, 255, 255)
        self.set_draw_color(*C_BORDER)
        self.set_line_width(0.2)
        x0 = MARGIN
        for i, h in enumerate(head):
            self.multi_cell(widths[i], 4.4, h, border=1, fill=True, align="C",
                            new_x="RIGHT", new_y="TOP")
        self.ln()
        self.set_font_pack("", size)
        self.set_text_color(*C_TEXT)
        for r in rows:
            self.set_fill_color(*C_TABLE_ROW)
            max_h = 5.5
            for i, cell in enumerate(r):
                # estimate row height by wrapping
                w = widths[i] - 3
                nb = self.get_string_width(cell) / w
                lines = max(1, int(nb) + (1 if nb > int(nb) else 0))
                max_h = max(max_h, lines * 4.8)
            for i, cell in enumerate(r):
                self.cell(widths[i], max_h, cell, border=1, fill=True, align="L")
            self.ln()
        self.ln(2)

    def footer(self):
        self.set_y(-13)
        self.set_font_pack("", 8)
        self.set_text_color(*C_MUTED)
        self.cell(0, 6, "Đề cương ôn tập Vật lý lớp 10 – Giữa kỳ I (2026–2027)   |   Trang " + str(self.page_no()),
                  align="C")

    # ---------- TOC ----------
    def render_toc(self, pdf, outline):
        pdf.set_xy(MARGIN, 14)
        pdf.set_font_pack("B", 15)
        pdf.set_text_color(*C_PRIMARY)
        pdf.cell(0, 10, "MỤC LỤC", new_x="LMARGIN", new_y="NEXT")
        pdf.hr(C_PRIMARY, 0.5)
        pdf.ln(3)
        for sec in outline:
            if sec.level == 0:
                self.set_font_pack("B", 10.8)
                self.set_text_color(*C_TEXT)
            else:
                self.set_font_pack("", 10)
                self.set_text_color(*C_MUTED)
            self.cell(0, 6.6, sec.name + "  ..........  trang " + str(sec.page_number),
                      new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_font_pack("", 9)
        self.set_text_color(*C_MUTED)
        self.multi_cell(0, 5, "Đề cương này được biên soạn dựa trên toàn bộ nội dung của tài liệu "
                              "“MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I – MÔN VẬT LÝ LỚP 10, NĂM HỌC 2026–2027”, "
                              "bao gồm đầy đủ 10 đơn vị kiến thức, các yêu cầu mức độ nhận thức "
                              "(Nhận biết / Thông hiểu / Vận dụng) và các câu hỏi ôn tập kèm đáp án cho từng đơn vị.",
                        new_x="LMARGIN", new_y="NEXT")


def build():
    pdf = GuidePDF()

    # ================= COVER =================
    pdf.add_page()
    pdf.set_fill_color(*C_PRIMARY)
    pdf.rect(0, 0, PAGE_W, 78, style="F")
    pdf.set_font_pack("B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 16)
    pdf.cell(0, 12, "ĐỀ CƯƠNG ÔN TẬP", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_pack("B", 16)
    pdf.set_xy(0, 30)
    pdf.cell(0, 9, "MÔN VẬT LÝ – LỚP 10", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_pack("", 12)
    pdf.set_xy(0, 42)
    pdf.cell(0, 8, "KIỂM TRA GIỮA KÌ I – NĂM HỌC 2026–2027", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font_pack("", 10)
    pdf.set_xy(0, 54)
    pdf.cell(0, 7, "Toàn diện • Chất lượng cao • Dễ ghi nhớ", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(0, 66)
    pdf.cell(0, 7, "Dựa trên tài liệu: MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(92)
    pdf.set_font_pack("B", 12)
    pdf.set_text_color(*C_PRIMARY)
    pdf.cell(0, 7, "THÔNG TIN BÀI KIỂM TRA", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(*C_PRIMARY)
    pdf.set_line_width(0.4)
    pdf.line(MARGIN + 30, pdf.get_y(), PAGE_W - MARGIN - 30, pdf.get_y())
    pdf.ln(4)
    info_rows = [
        ("Môn", "Vật lý"),
        ("Lớp", "10"),
        ("Năm học", "2026–2027"),
        ("Hình thức", "70% trắc nghiệm + 30% tự luận"),
        ("Thời gian", "50 phút"),
    ]
    pdf.set_font_pack("", 10.5)
    pdf.set_text_color(*C_TEXT)
    for k, v in info_rows:
        pdf.set_font_pack("B", 10.5)
        pdf.set_text_color(*C_PRIMARY)
        pdf.cell(60, 8, k, new_x="RIGHT", new_y="TOP")
        pdf.set_font_pack("", 10.5)
        pdf.set_text_color(*C_TEXT)
        pdf.cell(0, 8, v, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_font_pack("", 9.5)
    pdf.set_text_color(*C_MUTED)
    pdf.multi_cell(0, 5.5,
        "Đề cương ôn tập này bao gồm TẤT CẢ các nội dung kiến thức và yêu cầu đánh giá "
        "được nêu trong bài kiểm tra giữa kỳ I: 10 đơn vị kiến thức (từ làm quen với Vật lí đến rơi tự do), "
        "cấu trúc đề, mức độ nhận thức và hệ thống câu hỏi ôn tập kèm đáp án.",
        new_x="LMARGIN", new_y="NEXT")

    # ================= TOC =================
    pdf.add_page()
    pdf.insert_toc_placeholder(pdf.render_toc)

    # ================= PHẦN 1: TỔNG QUAN =================
    pdf.section("PHẦN 1. TỔNG QUAN VỀ BÀI KIỂM TRA GIỮA KÌ I")

    pdf.sub("1.1. Thông tin chung")
    pdf.body("Bài kiểm tra giữa kỳ I môn Vật lý lớp 10 (năm học 2026–2027) được tổ chức theo hình thức "
             "kết hợp: 70% câu hỏi trắc nghiệm (PHẦN 1 – 18 câu) và 30% câu hỏi tự luận (PHẦN II, III, IV). "
             "Thời gian làm bài: 50 phút.")

    pdf.sub("1.2. Cấu trúc đề kiểm tra")
    pdf.info_table(
        rows=[
            ["PHẦN 1", "Trắc nghiệm", "18 câu", "Biết (10 câu) + Hiểu (8 câu)"],
            ["PHẦN II", "Tự luận", "2 câu, mỗi câu 4 ý", "Biết (6 ý) + Hiểu (2 ý)"],
            ["PHẦN III", "Tự luận", "2 câu", "Biết (1 câu) + Hiểu (1 câu)"],
            ["PHẦN IV", "Tự luận", "—", "Hiểu (1 ý) + Vận dụng (2 ý)"],
        ],
        head=["PHẦN", "LOẠI HÌNH", "SỐ LƯỢNG", "PHÂN BỔ MỨC ĐỘ"],
        widths=[25, 32, 45, 78],
    )

    pdf.sub("1.3. Ma trận phân bổ đơn vị kiến thức (theo tài liệu)")
    pdf.body("Bảng sau tóm tắt số câu hỏi theo từng đơn vị kiến thức và mức độ nhận thức trong tài liệu gốc:",
             size=9.5, color=C_MUTED)
    pdf.info_table(
        rows=[
            ["1.1 Làm quen với Vật lí", "1", "", "", "", "", "", "", ""],
            ["1.2 Quy tắc an toàn trong phòng thực hành", "1", "1", "", "", "", "", "", ""],
            ["1.3 Thực hành tính sai số trong phép đo", "1", "", "", "", "", "", "", ""],
            ["2.1 Độ dịch chuyển và quãng đường", "1", "2", "", "", "", "", "", ""],
            ["2.2 Tốc độ và vận tốc", "1", "", "2-I", "", "1", "", "1", ""],
            ["2.3 Đồ thị độ dịch chuyển – thời gian", "1", "1", "2-I", "", "", "", "", ""],
            ["2.4 Chuyển động biến đổi. Gia tốc", "1", "1", "", "", "", "", "", ""],
            ["2.5 Chuyển động thẳng biến đổi đều", "2", "1", "2-II", "2-II", "", "", "", "2"],
            ["2.6 Sự rơi tự do", "1", "2", "", "", "", "1", "", ""],
            ["TỔNG", "10", "8", "6", "2", "1", "1", "1", "2"],
        ],
        head=["ĐƠN VỊ KIẾN THỨC", "Biết\n(P1)", "Hiểu\n(P1)", "Biết\n(P2)", "Hiểu\n(P2)",
              "Biết\n(P3)", "Hiểu\n(P3)", "Hiểu\n(P4)", "Vận dụng\n(P4)"],
        widths=[62, 14, 14, 14, 14, 14, 14, 14, 16],
        size=8.8,
    )
    pdf.body("Ghi chú: P1 = PHẦN 1 (trắc nghiệm), P2 = PHẦN II, P3 = PHẦN III, P4 = PHẦN IV. "
             "Mức độ nhận thức: Biết = Nhận biết, Hiểu = Thông hiểu, Vận dụng = Vận dụng.",
             size=8.8, color=C_MUTED)

    pdf.tip_box("LƯU Ý ÔN TẬP",
        "Trọng tâm ôn tập là các đơn vị 2.2–2.6 (động học) vì chiếm nhiều câu hỏi nhất. "
        "Mức độ “Biết” chiếm 10/18 câu trắc nghiệm — hãy ôn kỹ định nghĩa, công thức, đơn vị. "
        "Mức độ “Vận dụng” chủ yếu nằm ở đơn vị 2.5 (chuyển động thẳng biến đổi đều) và 2.6 (rơi tự do).")

    # ================= PHẦN 2: 10 ĐƠN VỊ =================
    pdf.section("PHẦN 2. ĐỀ CƯƠNG 10 ĐƠN VỊ KIẾN THỨC")

    # ---- Đơn vị 1 ----
    pdf.sub("Đơn vị 1: Làm quen với Vật lí")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Nêu được đối tượng nghiên cứu chủ yếu của vật lí; biết được các thành tựu "
             "nghiên cứu của vật lí tương ứng với các cuộc cách mạng công nghiệp; nêu được các quá trình "
             "phát triển của vật lí; nêu được phương pháp nghiên cứu vật lí.", size=9.8)
    pdf.body("• Thông hiểu: Hiểu được quá trình nghiên cứu của vật lí.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Đối tượng nghiên cứu của Vật lí: nghiên cứu sự chuyển động của vật chất và các hiện tượng tự nhiên, "
        "nhằm tìm ra các quy luật khách quan của tự nhiên.",
        "Thành tựu nghiên cứu tương ứng với các cuộc cách mạng công nghiệp:",
        "   • Cách mạng công nghiệp lần 1 (cuối thế kỷ 18): máy móc cơ khí, động cơ nhiệt → cơ học, nhiệt học phát triển.",
        "   • Cách mạng công nghiệp lần 2 (cuối thế kỷ 19): điện khí hóa → điện từ học phát triển.",
        "   • Cách mạng công nghiệp lần 3 (đầu thế kỷ 20): công nghệ thông tin, điện tử → vật lí hiện đại "
        "(thuyết tương đối, cơ học lượng tử).",
        "Các quá trình phát triển của vật lí: cổ điển (thế kỷ 17–19: cơ học Newton, điện từ Maxwell, nhiệt động lực học) "
        "→ hiện đại (đầu thế kỷ 20: thuyết tương đối, cơ học lượng tử) → hiện nay (vật lí hạt nhân, vật lí chất rắn, "
        "vật lí thiên văn...).",
        "Phương pháp nghiên cứu vật lí: thực nghiệm (thí nghiệm), phương pháp lý thuyết (toán học), phương pháp quan sát.",
        "Quá trình nghiên cứu của vật lí: quan sát/thực nghiệm → đặt giả thuyết → kiểm chứng → rút ra quy luật → "
        "áp dụng vào thực tiễn.",
    ], size=9.8)

    pdf.formula_box([
        "Phương pháp nghiên cứu vật lí = THỰC NGHIỆM + LÝ THUYẾT (toán học) + QUAN SÁT",
    ])

    pdf.qa_block("Đối tượng nghiên cứu chủ yếu của Vật lí là gì?",
        "Vật lí nghiên cứu sự chuyển động của vật chất và các hiện tượng tự nhiên, nhằm tìm ra các quy luật "
        "khách quan của tự nhiên.", level="Biết")
    pdf.qa_block("Thành tựu nào của vật lí gắn liền với cuộc cách mạng công nghiệp lần 2?",
        "Điện khí hóa; sự phát triển mạnh mẽ của điện từ học (nhờ các nhà khoa học như Faraday, Maxwell).",
        level="Biết")
    pdf.qa_block("Nêu các giai đoạn phát triển của vật lí từ thế kỷ 17 đến nay.",
        "1) Vật lí cổ điển (thế kỷ 17–19): cơ học Newton, điện từ Maxwell, nhiệt động lực học; "
        "2) Vật lí hiện đại (đầu thế kỷ 20): thuyết tương đối, cơ học lượng tử; "
        "3) Hiện nay: vật lí hạt nhân, vật lí chất rắn, vật lí thiên văn... gắn với công nghệ hiện đại.",
        level="Hiểu")

    # ---- Đơn vị 2 ----
    pdf.sub("Đơn vị 2: Các quy tắc an toàn trong phòng thực hành Vật lí")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Nêu được các nguy cơ mất an toàn trong sử dụng thiết bị thí nghiệm vật lí; nêu được "
             "các quy tắc an toàn trong phòng thực hành.", size=9.8)
    pdf.body("• Thông hiểu: Hiểu và sử dụng được các thiết bị thí nghiệm; hiểu và sử dụng các biển báo.",
             size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Các nguy cơ mất an toàn:",
        "   • Điện giật (nguồn điện, dây dẫn hở, thiết bị điện không đúng quy cách);",
        "   • Bỏng do nhiệt (bếp điện, đun nóng);",
        "   • Vết cắt, vết thương do đồ kim loại sắc (dao, que kim loại);",
        "   • Rơi vỡ, đập vỡ (thủy tinh, kính);",
        "   • Tai nạn do máy móc quay (động cơ).",
        "Các quy tắc an toàn trong phòng thực hành:",
        "   • Không tự ý sử dụng thiết bị khi chưa có hướng dẫn của giáo viên;",
        "   • Báo cáo ngay cho giáo viên nếu thiết bị bị hư hỏng;",
        "   • Không chạm vào thiết bị đang có điện khi không có hướng dẫn;",
        "   • Đeo kính bảo hộ, găng tay khi cần thiết;",
        "   • Không ăn uống trong phòng thí nghiệm;",
        "   • Dọn dẹp và để thiết bị đúng nơi quy định sau khi làm xong.",
        "Sử dụng thiết bị thí nghiệm: đúng mục đích, đúng quy trình; đọc số đo đúng cách; bảo quản sau khi sử dụng.",
        "Các biển báo an toàn: nhận biết và tuân thủ các biển báo nguy hiểm (điện giật, dễ cháy, độc hại, ăn mòn...).",
    ], size=9.8)

    pdf.qa_block("Liệt kê ít nhất ba nguy cơ mất an toàn khi làm thí nghiệm vật lí.",
        "Điện giật, bỏng do nhiệt, vết cắt do đồ kim loại sắc, rơi vỡ thủy tinh, tai nạn do máy móc quay.",
        level="Biết")
    pdf.qa_block("Khi phát hiện thiết bị thí nghiệm bị hư hỏng, em nên làm gì?",
        "Báo cáo ngay cho giáo viên; không tự ý sửa chữa hoặc tiếp tục sử dụng thiết bị hư hỏng.",
        level="Biết")
    pdf.qa_block("Nêu hai quy tắc an toàn khi sử dụng thiết bị điện trong phòng thí nghiệm.",
        "Không chạm vào thiết bị đang có điện khi không có hướng dẫn; kiểm tra dây dẫn, nguồn điện trước khi sử dụng.",
        level="Hiểu")

    # ---- Đơn vị 3 ----
    pdf.sub("Đơn vị 3: Thực hành tính sai số trong phép đo. Ghi kết quả đo")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Nêu được phép đo trực tiếp và phép đo gián tiếp; biết được các loại sai số của phép đo; "
             "nêu được một số nguyên nhân gây ra sai số khi tiến hành thí nghiệm vật lí; biết được công thức giá trị "
             "trung bình, sai số tỉ đối, sai số tuyệt đối.", size=9.8)
    pdf.body("• Thông hiểu: Cách ghi đúng kết quả phép đo và sai số phép đo; tính được sai số tuyệt đối và sai số "
             "tỉ đối của phép đo.", size=9.8)
    pdf.body("• Vận dụng: Tính giá trị đo; tính sai số của phép đo.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Phép đo trực tiếp: đo trực tiếp giá trị của đại lượng bằng dụng cụ (ví dụ: dùng thước đo chiều dài, "
        "đồng hồ đo thời gian).",
        "Phép đo gián tiếp: tính giá trị của đại lượng từ các đại lượng đo trực tiếp (ví dụ: diện tích S = a·b).",
        "Các loại sai số của phép đo:",
        "   • Sai số của dụng cụ đo (sai số thiết bị): do dụng cụ không chính xác;",
        "   • Sai số quan sát (sai số của người đo): do thị lực, phản xạ khi đọc số;",
        "   • Sai số môi trường: do nhiệt độ, độ ẩm, áp suất thay đổi;",
        "   • Sai số phương pháp: do phương pháp đo không chính xác.",
        "Một số nguyên nhân gây sai số: dụng cụ không chính xác; môi trường thay đổi; người đo đọc sai; "
        "phương pháp đo không phù hợp...",
    ], size=9.8)

    pdf.formula_box([
        "Giá trị trung bình của n lần đo:  x̄ = (x₁ + x₂ + ... + xₙ) / n",
        "Sai số tuyệt đối:  Δx = |x − x̄|  (độ lệch giữa một lần đo và giá trị trung bình)",
        "Sai số tương đối (tỉ đối):  δ = Δx / |x̄|  (hay Δx / x)",
        "Kết quả đo ghi:  x = x̄ ± Δx",
    ])

    pdf.qa_block("Đo chiều dài của một que bằng thước là phép đo gì? Tính diện tích S = a·b với a, b đo bằng thước là phép đo gì?",
        "Đo chiều dài que bằng thước là phép đo TRỰC TIẾP. Tính diện tích S = a·b là phép đo GIÁN TIẾP.",
        level="Biết")
    pdf.qa_block("Một học sinh đo chiều dài que 3 lần được: 10,1 cm; 10,2 cm; 9,9 cm. Tính giá trị trung bình.",
        "x̄ = (10,1 + 10,2 + 9,9) / 3 = 30,2 / 3 ≈ 10,07 cm.",
        level="Hiểu")
    pdf.qa_block("Với giá trị trung bình x̄ = 10,07 cm và sai số tuyệt đối Δx = 0,1 cm, tính sai số tương đối.",
        "δ = Δx / x̄ = 0,1 / 10,07 ≈ 0,01 = 1%. Kết quả đo ghi: x = (10,07 ± 0,1) cm.",
        level="Vận dụng")

    # ---- Đơn vị 4 ----
    pdf.sub("Đơn vị 4: Độ dịch chuyển và quãng đường đi được")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Nêu được độ dịch chuyển là gì; so sánh được độ dịch chuyển và quãng đường đi được.",
             size=9.8)
    pdf.body("• Thông hiểu: Xác định được độ dịch chuyển và quãng đường đi được.", size=9.8)
    pdf.body("• Vận dụng: Tính độ dịch chuyển. Vận dụng cao: Tính được độ dịch chuyển và quãng đường trong các bài toán.",
             size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Độ dịch chuyển (Δr): vectơ nối từ điểm đầu đến điểm cuối của quãng đường mà vật đi được; có phương, "
        "chiều và độ lớn. Δr = r₂ − r₁.",
        "Quãng đường (s): độ dài quỹ đạo mà vật đi được; là đại lượng vô hướng, luôn không âm (s ≥ 0).",
        "So sánh: độ dịch chuyển là vectơ; quãng đường là vô hướng. Độ lớn của độ dịch chuyển ≤ quãng đường.",
        "Khi chuyển động thẳng không đổi hướng: độ lớn độ dịch chuyển = quãng đường.",
        "Tính toán: khi đi xuôi rồi ngược, độ dịch chuyển = tổng có dấu (theo chiều đã chọn); "
        "quãng đường = tổng các độ dài tuyệt đối.",
        "Đơn vị: mét (m), kilômét (km).",
    ], size=9.8)

    pdf.formula_box([
        "Độ dịch chuyển:  Δr = r₂ − r₁   (vectơ)",
        "Quãng đường:  s ≥ 0   (vô hướng, độ dài quỹ đạo)",
        "Khi vật đi xuôi rồi ngược:  |Δr| = |s₁ − s₂|,  s = |s₁| + |s₂|",
    ])

    pdf.qa_block("Định nghĩa độ dịch chuyển? Nó có tính chất gì khác quãng đường?",
        "Độ dịch chuyển là vectơ nối từ điểm đầu đến điểm cuối của quãng đường. Nó là vectơ (có phương, chiều), "
        "còn quãng đường là đại lượng vô hướng (độ dài quãng đường).",
        level="Biết")
    pdf.qa_block("Một người đi từ A đến B (20 m) rồi quay về A. Tính độ dịch chuyển và quãng đường đi được.",
        "Độ dịch chuyển = 0 (vật quay về đúng vị trí ban đầu). Quãng đường = 20 + 20 = 40 m.",
        level="Vận dụng")
    pdf.qa_block("Khi nào độ lớn của độ dịch chuyển bằng quãng đường đi được?",
        "Khi vật chuyển động thẳng và không đổi hướng.",
        level="Hiểu")

    # ---- Đơn vị 5 ----
    pdf.sub("Đơn vị 5: Tốc độ và vận tốc")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Biết được ý nghĩa và công thức của tốc độ trung bình; biết tốc độ tức thời; biết cách đo "
             "tốc độ trong cuộc sống và trong phòng thí nghiệm; nêu được định nghĩa vận tốc và viết được công thức "
             "tính vận tốc; biết được công thức cộng vận tốc.", size=9.8)
    pdf.body("• Thông hiểu: Tính được tốc độ trung bình; phân biệt được tốc độ và vận tốc; xác định được vectơ vận tốc.",
             size=9.8)
    pdf.body("• Vận dụng: Giải được các bài toán về tổng hợp hai vận tốc cùng phương và hai vận tốc vuông góc với nhau.",
             size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Tốc độ trung bình: v̄ = s/t (quãng đường đi được / thời gian); đơn vị m/s hoặc km/h. "
        "1 km/h = 1/3,6 m/s.",
        "Tốc độ tức thời: giới hạn của tốc độ trung bình khi khoảng thời gian t → 0; v = ds/dt.",
        "Đo tốc độ trong cuộc sống: công tơ mét (đồng hồ tốc độ) trên xe ô tô; radar của cảnh sát giao thông.",
        "Đo tốc độ trong phòng thí nghiệm: đồng hồ bấm giờ, cổng quang điện.",
        "Vận tốc: vectơ; v = Δr/Δt (độ dịch chuyển / thời gian); có phương, chiều.",
        "Phân biệt tốc độ và vận tốc: tốc độ là đại lượng vô hướng (chỉ độ lớn); vận tốc là vectơ (có cả phương, chiều).",
    ], size=9.8)

    pdf.formula_box([
        "Tốc độ trung bình:  v̄ = s / t",
        "Vận tốc:  v = Δr / Δt   (vectơ)",
        "Cộng vận tốc cùng phương, cùng chiều:  v = v₁ + v₂",
        "Cộng vận tốc cùng phương, ngược chiều:  v = |v₁ − v₂|",
        "Cộng vận tốc vuông góc:  v = √(v₁² + v₂²);  tan α = v₂ / v₁",
        "Đổi đơn vị:  1 km/h = 1/3,6 m/s ≈ 0,278 m/s",
    ])

    pdf.qa_block("Tốc độ trung bình của một xe đi 180 km trong 2 giờ là bao nhiêu? Đổi sang m/s.",
        "v̄ = 180 / 2 = 90 km/h. Đổi sang m/s: 90 × 1/3,6 = 25 m/s.",
        level="Hiểu")
    pdf.qa_block("Phân biệt tốc độ và vận tốc.",
        "Tốc độ là đại lượng vô hướng (chỉ có độ lớn, không có phương, chiều); vận tốc là vectơ "
        "(có cả độ lớn, phương và chiều).",
        level="Biết")
    pdf.qa_block("Một máy bay bay với vận tốc 200 km/h về phía Bắc, gió thổi với vận tốc 100 km/h về phía Đông. "
                 "Tính vận tốc thực của máy bay (tốc độ và hướng).",
        "v = √(200² + 100²) = √(40000 + 10000) = √50000 ≈ 223,6 km/h. "
        "tan α = v₂/v₁ = 100/200 = 0,5 → α ≈ 26,6° về phía Đông so với hướng Bắc (tức bay về hướng Bắc-Đông).",
        level="Vận dụng")

    # ---- Đơn vị 6 ----
    pdf.sub("Đơn vị 6: Thực hành: Đo tốc độ của vật chuyển động")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Nêu được ưu điểm và nhược điểm khi sử dụng đồng hồ đo thời gian hiện số và cổng quang điện; "
             "cách sử dụng đồng hồ đo thời gian hiện số; ý nghĩa của việc sử dụng hai cổng quang điện.", size=9.8)
    pdf.body("• Thông hiểu: Đo được tốc độ bằng dụng cụ thực hành.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Đồng hồ đo thời gian hiện số (đồng hồ bấm giờ):",
        "   • Ưu điểm: kết quả hiện ngay trên màn hình; chính xác hơn đồng hồ cơ; dễ sử dụng.",
        "   • Nhược điểm: vẫn phải bấm tay (có sai số do phản xạ); không tự động.",
        "Cổng quang điện:",
        "   • Ưu điểm: tự động bấm thời gian khi vật cản đường tia sáng; chính xác cao; đo được khoảng thời gian rất ngắn.",
        "   • Nhược điểm: giá thành cao; cần vật cản (tấm chắn) và vị trí đặt đúng.",
        "Cách sử dụng đồng hồ đo thời gian hiện số: bấm nút bấm khi vật bắt đầu đi qua điểm cần đo; bấm lại khi "
        "vật đi qua điểm kết thúc; đọc kết quả thời gian.",
        "Ý nghĩa của hai cổng quang điện: đặt hai cổng cách nhau một đoạn d; khi xe đi qua cổng 1, đồng hồ bắt đầu "
        "tính giờ; khi xe đi qua cổng 2, đồng hồ dừng lại. Thời gian đo được là thời gian để xe đi từ cổng 1 đến "
        "cổng 2 → tính được tốc độ trung bình giữa hai cổng: v̄ = d/t.",
    ], size=9.8)

    pdf.formula_box([
        "Tốc độ trung bình giữa hai cổng quang điện:  v̄ = d / t",
        "(d = khoảng cách giữa hai cổng; t = thời gian xe đi từ cổng 1 đến cổng 2)",
    ])

    pdf.qa_block("So sánh ưu điểm của cổng quang điện và đồng hồ bấm giờ hiện số.",
        "Cổng quang điện: tự động bấm thời gian, chính xác rất cao, đo được thời gian ngắn. "
        "Đồng hồ bấm giờ hiện số: dễ sử dụng, kết quả hiện ngay nhưng vẫn phải bấm tay → sai số do phản xạ.",
        level="Biết")
    pdf.qa_block("Hai cổng quang điện cách nhau 10 cm, xe đi qua mất 0,2 s. Tính tốc độ trung bình của xe.",
        "d = 10 cm = 0,1 m; v̄ = d/t = 0,1 / 0,2 = 0,5 m/s.",
        level="Vận dụng")

    # ---- Đơn vị 7 ----
    pdf.sub("Đơn vị 7: Đồ thị độ dịch chuyển – thời gian")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Mô tả được chuyển động của vật dựa vào đồ thị dịch chuyển – thời gian.", size=9.8)
    pdf.body("• Thông hiểu: Tính được tốc độ từ độ dốc của đồ thị độ dịch chuyển – thời gian; xác định được vị trí "
             "và vận tốc của vật ở bất kì thời điểm nào dựa vào đồ thị.", size=9.8)
    pdf.body("• Vận dụng: Vẽ được đồ thị độ dịch chuyển – thời gian trong chuyển động thẳng. Xác định được quãng "
             "đường đi được và độ dịch chuyển của vật.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Đồ thị x – t (độ dịch chuyển – thời gian):",
        "   • Đường ngang (x = const): vật đứng yên;",
        "   • Đường xiên thẳng: chuyển động thẳng đều (vận tốc không đổi);",
        "   • Đường cong: chuyển động biến đổi.",
        "Tốc độ từ độ dốc của đồ thị: v = Δx/Δt — độ dốc của tiếp tuyến tại thời điểm t cho vận tốc tức thời.",
        "Xác định vị trí và vận tốc tại bất kỳ thời điểm nào: vị trí = giá trị x trên trục tung; vận tốc = độ dốc "
        "của tiếp tuyến tại thời điểm đó.",
        "Vẽ đồ thị trong chuyển động thẳng:",
        "   • Chuyển động đều: đường thẳng;",
        "   • Chuyển động biến đổi đều: đường parabol (x = x₀ + v₀t + ½at²).",
        "Xác định quãng đường và độ dịch chuyển: quãng đường = tổng độ dài các đoạn; độ dịch chuyển = x(t₂) − x(t₁).",
    ], size=9.8)

    pdf.formula_box([
        "Vận tốc từ đồ thị x – t:  v = Δx / Δt   (độ dốc của tiếp tuyến)",
        "Chuyển động thẳng biến đổi đều:  x = x₀ + v₀t + ½at²",
    ])

    pdf.qa_block("Trên đồ thị x – t, đoạn đường ngang biểu diễn điều gì?",
        "Vật đứng yên (vị trí không đổi theo thời gian).", level="Biết")
    pdf.qa_block("Làm thế nào để tính vận tốc của vật tại thời điểm t từ đồ thị x – t?",
        "Vận tốc bằng độ dốc của tiếp tuyến tại thời điểm t: v = dx/dt.", level="Hiểu")
    pdf.qa_block("Một vật chuyển động thẳng đều với vận tốc v = 2 m/s, vị trí ban đầu x₀ = 4 m. Viết phương trình "
                 "chuyển động và xác định vị trí sau 3 s.",
        "Phương trình: x = x₀ + vt = 4 + 2t (m). Sau 3 s: x = 4 + 2×3 = 10 m.",
        level="Vận dụng")

    # ---- Đơn vị 8 ----
    pdf.sub("Đơn vị 8: Chuyển động biến đổi. Gia tốc")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Biết được thế nào là chuyển động biến đổi; biết được quan hệ về phương và chiều của gia "
             "tốc với vận tốc; biết được khái niệm gia tốc, công thức tính gia tốc và đơn vị của gia tốc.", size=9.8)
    pdf.body("• Thông hiểu: Tính được độ biến thiên vận tốc, gia tốc của chuyển động; phân biệt được chuyển động "
             "nhanh dần và chậm dần dựa vào vận tốc và gia tốc.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Chuyển động biến đổi: chuyển động mà vận tốc thay đổi theo thời điểm (có thể thay đổi độ lớn hoặc hướng).",
        "Gia tốc: đại lượng đặc trưng cho sự thay đổi vận tốc; a = Δv/Δt = (v − v₀)/Δt; là vectơ; đơn vị m/s².",
        "Quan hệ phương và chiều của gia tốc với vận tốc:",
        "   • a cùng phương, cùng chiều với v: chuyển động nhanh dần (tăng tốc) — độ lớn vận tốc tăng;",
        "   • a cùng phương, ngược chiều với v: chuyển động chậm dần (giảm tốc) — độ lớn vận tốc giảm;",
        "   • a vuông góc với v: chuyển động cong (thay đổi hướng).",
        "Phân biệt chuyển động nhanh dần và chậm dần dựa vào vận tốc và gia tốc: nhanh dần khi a cùng chiều v "
        "(v và a cùng dấu); chậm dần khi a ngược chiều v (v và a trái dấu).",
    ], size=9.8)

    pdf.formula_box([
        "Gia tốc:  a = Δv / Δt = (v − v₀) / Δt",
        "Đơn vị:  m/s²",
        "Nhanh dần:  a cùng chiều v  →  |v| tăng",
        "Chậm dần:  a ngược chiều v  →  |v| giảm",
    ])

    pdf.qa_block("Định nghĩa gia tốc? Đơn vị của gia tốc là gì?",
        "Gia tốc là đại lượng đặc trưng cho sự thay đổi vận tốc của vật: a = Δv/Δt. Đơn vị: m/s².",
        level="Biết")
    pdf.qa_block("Một vật có vận tốc ban đầu 5 m/s, sau 2 s vận tốc thành 13 m/s. Tính gia tốc của vật.",
        "a = (v − v₀)/Δt = (13 − 5)/2 = 8/2 = 4 m/s².", level="Hiểu")
    pdf.qa_block("Khi nào vật chuyển động nhanh dần? Khi nào chuyển động chậm dần?",
        "Nhanh dần khi gia tốc cùng chiều với vận tốc (a và v cùng dấu); chậm dần khi gia tốc ngược chiều với "
        "vận tốc (a và v trái dấu).", level="Hiểu")

    # ---- Đơn vị 9 ----
    pdf.sub("Đơn vị 9: Chuyển động thẳng biến đổi đều")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Biết được định nghĩa của chuyển động thẳng biến đổi đều; biết được định nghĩa chuyển động "
             "nhanh dần đều và chuyển động chậm dần đều; biết được các công thức của chuyển động thẳng biến đổi đều.",
             size=9.8)
    pdf.body("• Thông hiểu: Sử dụng được các công thức để tính được vận tốc, gia tốc, độ dịch chuyển của vật.",
             size=9.8)
    pdf.body("• Vận dụng: Vận dụng giải các bài toán cơ bản về chuyển động thẳng biến đổi đều. "
             "Vận dụng cao: Vận dụng giải các bài toán nâng cao về chuyển động thẳng biến đổi đều.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Chuyển động thẳng biến đổi đều (CSTBĐ): chuyển động có quỹ đạo thẳng và gia tốc không đổi "
        "(a = const, a ≠ 0).",
        "Chuyển động nhanh dần đều: a cùng chiều với chuyển động; vận tốc tăng đều theo thời gian.",
        "Chuyển động chậm dần đều: a ngược chiều với chuyển động; vận tốc giảm đều theo thời gian.",
        "Lưu ý khi giải bài toán: chọn chiều dương hợp lý; quy ước dấu của a; đổi đơn vị đúng (km/h ↔ m/s).",
    ], size=9.8)

    pdf.formula_box([
        "Vận tốc:  v = v₀ + at",
        "Độ dịch chuyển:  x = v₀t + ½at²",
        "Mối liên hệ:  v² − v₀² = 2ax",
        "Vận tốc trung bình (với chuyển động biến đổi đều):  v̄ = (v₀ + v) / 2",
        "Quãng đường/độ dịch chuyển:  x = v̄·t",
    ])

    pdf.qa_block("Một xe xuất phát với vận tốc v₀ = 2 m/s, gia tốc a = 3 m/s². Tính vận tốc sau 5 s.",
        "v = v₀ + at = 2 + 3×5 = 17 m/s.", level="Hiểu")
    pdf.qa_block("Tính độ dịch chuyển của xe sau 5 s trong bài trên.",
        "x = v₀t + ½at² = 2×5 + ½×3×25 = 10 + 37,5 = 47,5 m.", level="Vận dụng")
    pdf.qa_block("Một xe chuyển động chậm dần đều với v₀ = 10 m/s và a = −2 m/s². Thời gian để xe dừng hẳn? "
                 "Quãng đường xe đi được trước khi dừng?",
        "Thời gian dừng: 0 = v₀ + at → t = 10/2 = 5 s. Quãng đường: v² − v₀² = 2ax → 0 − 100 = 2×(−2)×x → x = 25 m.",
        level="Vận dụng")
    pdf.qa_block("Một xe đi với v₀ = 20 m/s, phanh với a = −4 m/s². Quãng đường đi được trước khi dừng hẳn?",
        "v² − v₀² = 2ax → 0 − 400 = 2×(−4)×x → x = 400/8 = 50 m.", level="Vận dụng")

    # ---- Đơn vị 10 ----
    pdf.sub("Đơn vị 10: Rơi tự do")
    pdf.sub_sub("Yêu cầu theo tài liệu")
    pdf.body("• Nhận biết: Biết được định nghĩa rơi tự do; biết được đặc điểm của chuyển động rơi trong không khí; "
             "biết được các công thức của rơi tự do.", size=9.8)
    pdf.body("• Thông hiểu: Phân biệt được vật rơi gần đúng tự do và không phải rơi tự do; áp dụng các công thức rơi "
             "tự do tính toán các bài đơn giản.", size=9.8)
    pdf.body("• Vận dụng: Vận dụng giải quyết các bài toán về rơi tự do.", size=9.8)

    pdf.sub_sub("Kiến thức trọng tâm")
    pdf.bullets([
        "Rơi tự do: chuyển động của một vật nặng (không có sức cản của không khí), chỉ chịu tác dụng của trọng lực, "
        "xuất phát từ trạng thái nghỉ (v₀ = 0), theo phương thẳng đứng hướng xuống.",
        "Điều kiện rơi tự do: không có sức cản không khí; chỉ chịu tác dụng của trọng lực; xuất phát từ trạng thái nghỉ (v₀ = 0).",
        "Đặc điểm của chuyển động rơi trong không khí: có sức cản không khí → chuyển động không còn là biến đổi đều; "
        "vận tốc tăng chậm lại; cuối cùng đạt vận tốc giới hạn.",
        "Phân biệt rơi gần đúng tự do và không phải rơi tự do:",
        "   • Rơi gần đúng tự do: vật nặng, khối lượng lớn so với diện tích (viên đá, viên đạn) — bỏ qua được sức cản không khí;",
        "   • Không phải rơi tự do: lá cây, lông chim, tờ giấy — chịu ảnh hưởng lớn của sức cản không khí.",
    ], size=9.8)

    pdf.formula_box([
        "Vận tốc:  v = gt",
        "Độ cao rơi được:  h = ½gt²",
        "Mối liên hệ:  v² = 2gh",
        "Vận tốc trung bình:  v̄ = v / 2 = gt / 2",
        "(g ≈ 9,8 m/s²; hướng xuống)",
    ])

    pdf.qa_block("Điều kiện để một chuyển động được gọi là rơi tự do là gì?",
        "Không có sức cản của không khí; chỉ chịu tác dụng của trọng lực; xuất phát từ trạng thái nghỉ (v₀ = 0).",
        level="Biết")
    pdf.qa_block("Một vật rơi tự do từ độ cao h = 45 m (g = 10 m/s²). Tính thời gian rơi và vận tốc khi chạm đất.",
        "t = √(2h/g) = √(2×45/10) = √9 = 3 s. v = gt = 10×3 = 30 m/s.", level="Vận dụng")
    pdf.qa_block("Một vật rơi tự do, sau 2 s vận tốc của nó là bao nhiêu? Độ cao rơi được là bao nhiêu? "
                 "(g = 10 m/s²)",
        "v = gt = 10×2 = 20 m/s. h = ½gt² = ½×10×4 = 20 m.", level="Vận dụng")
    pdf.qa_block("Viên đá và lá cây thả cùng lúc từ cùng độ cao. Vật nào chạm đất trước? Vì sao?",
        "Viên đá chạm đất trước. Lá cây chịu ảnh hưởng lớn của sức cản không khí, không phải là rơi tự do; "
        "viên đá nặng, khối lượng lớn so với diện tích → rơi gần đúng tự do.", level="Hiểu")

    # ================= PHẦN 3: BẢNG CÔNG THỨC =================
    pdf.add_page()
    pdf.section("PHẦN 3. BẢNG CÔNG THỨC TỔNG HỢP")
    pdf.body("Bảng tổng hợp các công thức quan trọng nhất cần nhớ để ôn tập và làm bài kiểm tra giữa kỳ I:",
             size=9.8, color=C_MUTED)
    pdf.info_table(
        rows=[
            ["Đơn vị 3: Sai số phép đo", "Giá trị trung bình: x̄ = (x₁ + x₂ + ... + xₙ)/n; Sai số tuyệt đối: Δx = |x − x̄|; Sai số tương đối: δ = Δx/|x̄|"],
            ["Đơn vị 4: Độ dịch chuyển, quãng đường", "Δr = r₂ − r₁ (vectơ); s ≥ 0 (vô hướng); |Δr| ≤ s"],
            ["Đơn vị 5: Tốc độ, vận tốc", "v̄ = s/t; v = Δr/Δt; cộng vận tốc cùng phương: v = v₁ ± v₂; vuông góc: v = √(v₁² + v₂²)"],
            ["Đơn vị 6: Đo tốc độ thực hành", "v̄ = d/t (d = khoảng cách giữa hai cổng quang điện)"],
            ["Đơn vị 7: Đồ thị x – t", "v = Δx/Δt (độ dốc); chuyển động biến đổi đều: x = x₀ + v₀t + ½at²"],
            ["Đơn vị 8: Gia tốc", "a = Δv/Δt = (v − v₀)/Δt; đơn vị m/s²"],
            ["Đơn vị 9: Chuyển động thẳng biến đổi đều", "v = v₀ + at; x = v₀t + ½at²; v² − v₀² = 2ax; v̄ = (v₀ + v)/2"],
            ["Đơn vị 10: Rơi tự do", "v = gt; h = ½gt²; v² = 2gh; v̄ = v/2; g ≈ 9,8 m/s²"],
        ],
        head=["ĐƠN VỊ / NỘI DUNG", "CÔNG THỨC"],
        widths=[55, 125],
        size=9,
    )

    # ================= PHẦN 4: LỜI KHUYÊN =================
    pdf.section("PHẦN 4. LỜI KHUYÊN ÔN TẬP")
    pdf.tip_box("1. ÔN THEO MA TRẬN, CÓ CHỦ ĐICH",
        "PHẦN 1 (trắc nghiệm, 18 câu) chiếm 70% điểm số. Hãy ôn theo thứ tự các đơn vị kiến thức trong tài liệu, "
        "đặc biệt là các đơn vị 2.2–2.6. Mức độ “Biết” chiếm 10/18 câu trắc nghiệm — ôn kỹ định nghĩa, công thức, đơn vị.")
    pdf.tip_box("2. NẮM VỮNG CÔNG THỨC",
        "Viết tất cả công thức ra giấy, ôn hằng ngày. Đặc biệt chú ý: công thức chuyển động thẳng biến đổi đều "
        "(đơn vị 9) và công thức rơi tự do (đơn vị 10) — hai đơn vị có nhiều câu Vận dụng.")
    pdf.tip_box("3. LUYỆN BÀI TẬP, GIẢI Từng bước",
        "Làm bài tập nhóm, giải từng bước rõ ràng: chọn chiều dương → viết công thức → thay số → tính toán → "
        "đơn vị. Chú ý quy ước dấu của gia tốc trong chuyển động chậm dần đều.")
    pdf.tip_box("4. ÔN THỰC HÀNH",
        "Ghi nhớ quy trình sử dụng đồng hồ bấm giờ và cổng quang điện; cách ghi kết quả đo (x = x̄ ± Δx); "
        "cách đọc số trên dụng cụ đo.")
    pdf.tip_box("5. KIỂM TRA LẠI TRƯỚC KHI NỘP BÀI",
        "Kiểm tra đơn vị (km/h ↔ m/s), dấu của gia tốc, độ chính xác của số đo và sai số. "
        "Ngủ đủ giấc, ăn uống hợp lý trước ngày thi.")

    pdf.ln(4)
    pdf.set_font_pack("B", 11)
    pdf.set_text_color(*C_PRIMARY)
    pdf.cell(0, 7, "ĐÁP ÁN TÓM TẮT — TỐT NGUYÊN!", align="C", new_x="LMARGIN", new_y="NEXT")

    out = "/home/user/ly-10/Đề cương ôn tập Vật lý lớp 10 - Giữa kỳ I.pdf"
    pdf.output(out)
    print("PDF written:", out, "| pages:", pdf.page_no())


if __name__ == "__main__":
    build()
