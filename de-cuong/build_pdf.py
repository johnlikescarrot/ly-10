# -*- coding: utf-8 -*-
"""
Dựng PDF: Đề cương ôn tập giữa kì I Vật lí 10 (từ ma trận + đặc tả trong repo).

Chạy:  /tmp/venv/bin/python de-cuong/build_pdf.py
Đầu ra: DE-CUONG-ON-TAP-GIUA-KI-I-VAT-LI-10.pdf  (thư mục gốc của repo)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, NextPageTemplate, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

from helpers import (P, h1, h2, h3, bullets, sp, hr, callout, styled_table,
                     NAVY, NAVY2, TEAL, ORANGE, BG, BG_TEAL, BG_YELLOW, GREY_M, S)
import content_theory
import content_exam
import content_practice

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "DE-CUONG-ON-TAP-GIUA-KI-I-VAT-LI-10.pdf")
PAGE_W, PAGE_H = A4


class Doc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style = flowable.style.name
            if style in ("H1", "H2"):
                text = flowable.getPlainText()
                # Mục lục dùng tiêu đề rút gọn (phần sau dấu — là ghi chú mức độ)
                toc_text = text.split("\u2014")[0].strip() if style == "H2" else text
                level = 0 if style == "H1" else 1
                self.notify("TOCEntry", (level, toc_text, self.page))
                self.canv.bookmarkPage(f"bm-{self.page}-{abs(hash(text)) % 99999}")
                self.canv.addOutlineEntry(text, f"bm-{self.page}-{abs(hash(text)) % 99999}",
                                          level=level, closed=(level > 0))


def _header_footer(canv, doc):
    canv.saveState()
    if doc.page > 1:
        canv.setStrokeColor(colors.HexColor("#C9D4E0"))
        canv.setLineWidth(0.6)
        canv.line(17 * mm, PAGE_H - 14 * mm, PAGE_W - 17 * mm, PAGE_H - 14 * mm)
        canv.setFont("Sans", 7.2)
        canv.setFillColor(GREY_M)
        canv.drawString(17 * mm, PAGE_H - 11.5 * mm,
                        "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I \u00b7 VẬT LÍ 10 \u00b7 2026\u20132027")
        canv.drawRightString(PAGE_W - 17 * mm, PAGE_H - 11.5 * mm, "70% trắc nghiệm + 30% tự luận \u00b7 50 phút")
        canv.setFont("Sans", 7.5)
        canv.drawCentredString(PAGE_W / 2, 11 * mm, f"\u2014 Trang {doc.page} \u2014")
    canv.restoreState()


def _cover_bg(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY)
    canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canv.setFillColor(NAVY2)
    canv.rect(0, PAGE_H - 62 * mm, PAGE_W, 62 * mm, stroke=0, fill=1)
    canv.setFillColor(TEAL)
    canv.rect(0, 58 * mm, PAGE_W, 3.2 * mm, stroke=0, fill=1)
    # motif đồ thị d-t trang trí
    canv.setStrokeColor(colors.HexColor("#7FB3D5"))
    canv.setLineWidth(1.4)
    x0, y0 = 30 * mm, 118 * mm
    canv.line(x0, y0, x0 + 150 * mm, y0)
    canv.line(x0, y0, x0, y0 + 38 * mm)
    canv.setStrokeColor(ORANGE)
    canv.setLineWidth(2.2)
    canv.line(x0, y0, x0 + 70 * mm, y0 + 30 * mm)
    canv.line(x0 + 70 * mm, y0 + 30 * mm, x0 + 115 * mm, y0 + 30 * mm)
    canv.setFillColor(ORANGE)
    for (dx, dy) in [(0, 0), (70 * mm, 30 * mm), (115 * mm, 30 * mm)]:
        canv.circle(x0 + dx, y0 + dy, 3, stroke=0, fill=1)
    canv.setFont("Sans", 7.5)
    canv.setFillColor(colors.HexColor("#BFD7EA"))
    canv.drawString(x0 + 152 * mm, y0 - 4, "t")
    canv.drawString(x0 + 4, y0 + 38 * mm, "d")
    canv.restoreState()


def build():
    doc = Doc(OUT, pagesize=A4,
              leftMargin=17 * mm, rightMargin=17 * mm,
              topMargin=18 * mm, bottomMargin=15 * mm,
              title="Đề cương ôn tập giữa kì I \u2013 Vật lí lớp 10 (2026\u20132027)",
              author="Biên soạn từ Ma trận đặc tả KTGK I L10 \u2013 2026",
              subject="Vật lí 10 \u2013 Giữa kì I: Mở đầu + Động học (KNTT Bài 1\u201310)",
              creator="ly-10 study guide builder")
    cover_frame = Frame(17 * mm, 15 * mm, PAGE_W - 34 * mm, PAGE_H - 30 * mm, id="cover")
    main_frame = Frame(17 * mm, 15 * mm, PAGE_W - 34 * mm, PAGE_H - 33 * mm, id="main")
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cover_frame], onPage=_cover_bg),
        PageTemplate(id="Main", frames=[main_frame], onPage=_header_footer),
    ])

    story = []
    # ------------------------------------------------------------ BÌA
    story.append(Spacer(1, 52 * mm))
    story.append(Paragraph("VẬT LÍ LỚP 10",
                           ParagraphStyle("ct1", fontName="Sans-Bold", fontSize=13, leading=16,
                                          textColor=colors.HexColor("#F5B041"), alignment=1)))
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph("ĐỀ CƯƠNG ÔN TẬP<br/>GIỮA KÌ I",
                           ParagraphStyle("ct2", fontName="Sans-Bold", fontSize=34, leading=40,
                                          textColor=colors.white, alignment=1)))
    story.append(Spacer(1, 6 * mm))
    story.append(Paragraph("Đầy đủ \u00b7 Đúng ma trận \u00b7 Dễ ghi nhớ \u2014 kèm đề mẫu và đáp án chi tiết",
                           ParagraphStyle("ct3", fontName="Sans", fontSize=11.5, leading=15,
                                          textColor=colors.HexColor("#D6EAF8"), alignment=1)))
    story.append(Spacer(1, 62 * mm))
    cover_info = Table([
        [Paragraph("<b><font color=\"#FFFFFF\">Hình thức</font></b>", S["Cell"]),
         Paragraph("<font color=\"#FFFFFF\">70% trắc nghiệm + 30% tự luận</font>", S["Cell"])],
        [Paragraph("<b><font color=\"#FFFFFF\">Thời gian</font></b>", S["Cell"]),
         Paragraph("<font color=\"#FFFFFF\">50 phút</font>", S["Cell"])],
        [Paragraph("<b><font color=\"#FFFFFF\">Phạm vi</font></b>", S["Cell"]),
         Paragraph("<font color=\"#FFFFFF\">Chương I: Mở đầu (Bài 1\u20133) + Chương II: Động học (Bài 4\u201310) \u2014 SGK Kết nối tri thức</font>", S["Cell"])],
        [Paragraph("<b><font color=\"#FFFFFF\">Căn cứ</font></b>", S["Cell"]),
         Paragraph("<font color=\"#FFFFFF\">Ma trận đặc tả đề kiểm tra giữa kì I \u2013 Môn Vật lí lớp 10, năm học 2026\u20132027</font>", S["Cell"])],
    ], colWidths=[32 * mm, 118 * mm])
    cover_info.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1F4E79")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#7FB3D5")),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#2E6DA4")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(cover_info)
    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph("Tài liệu tự học dành cho học sinh lớp 10 \u00b7 Có thể in ra và học trực tiếp trên giấy",
                           ParagraphStyle("ct4", fontName="Sans", fontSize=8.5, leading=11,
                                          textColor=colors.HexColor("#AED6F1"), alignment=1)))
    story.append(NextPageTemplate("Main"))
    story.append(PageBreak())

    # ------------------------------------------------------------ HƯỚNG DẪN + MỤC LỤC
    story.append(h1("ĐỌC TRANG NÀY TRƯỚC \u2014 ĐỀ CƯƠNG NÀY ĐƯỢC LÀM NHƯ THẾ NÀO?"))
    story.append(callout("\u2605 Một sự thật cần nói rõ ngay từ đầu (để em học đúng cách)",
                         ["Tài liệu gốc trong kho là <b>ma trận + bản đặc tả</b> của đề kiểm tra \u2014 tức là \u201cbản thiết kế\u201d cho biết đề thi sẽ hỏi "
                          "<b>chủ đề nào, bao nhiêu câu, ở mức độ nào</b> \u2014 chứ <b>không chứa sẵn các câu hỏi cụ thể của đề thi thật</b>. "
                          "Vì vậy, không ai có thể chép lại \u201cnguyên văn đề thi\u201d từ tài liệu đó, và bất kì tài liệu nào hứa như vậy đều không trung thực.",
                          "Cách đề cương này bảo đảm tính <b>đầy đủ</b>: (1) giải mã 100% các ô của ma trận (Phần 0); "
                          "(2) dạy đủ 100% yêu cầu của bản đặc tả (Phần A, Phụ lục đối chiếu); "
                          "(3) cho em làm một <b>đề mẫu đúng y hệt cấu trúc</b> \u2014 18 + 8 + 2 + 3 mục (Phần B, có đáp án chi tiết); "
                          "(4) luyện thêm 30 câu đổi dạng theo từng đơn vị (Phần C, có đáp án). "
                          "Câu hỏi thật dù đổi số, đổi tình huống đến đâu cũng vẫn nằm trong các ô đã học này."],
                         bg=BG_YELLOW, accent=ORANGE))
    story.append(sp(3))
    story.append(h3("Cách dùng đề cương trong 4 bước"))
    story.extend(bullets([
        "<b>Bước 1 (5 phút):</b> Đọc <b>Phần 0</b> để biết đề thi trông như thế nào và bài nào chiếm nhiều câu nhất.",
        "<b>Bước 2 (trọng tâm):</b> Học <b>Phần A</b> theo thứ tự \u2014 mỗi bài chỉ cần thuộc hộp NHỚ NHANH, hiểu bảng so sánh và làm được ví dụ mẫu.",
        "<b>Bước 3 (luyện):</b> Làm <b>Phần C</b> theo từng đơn vị, sửa lỗi ngay bằng hộp đáp án dưới mỗi đơn vị.",
        "<b>Bước 4 (thử thật):</b> Bấm giờ 50 phút làm <b>Phần B</b>, chấm bằng B2\u2013B3, tối trước ngày thi chỉ đọc lại <b>Phần D</b>.",
    ]))
    story.append(h3("Đề cương gồm những gì?"))
    story.append(styled_table([
        ["Phần", "Nội dung", "Em nhận được gì"],
        ["0", "Giải mã ma trận trong 5 phút", "Biết đề có 25 câu / 31 mục, bài nào nhiều câu nhất"],
        ["A", "Kiến thức cốt lõi A1\u2013A9", "Hộp nhớ nhanh + bảng so sánh + mẹo + bẫy + ví dụ mẫu cho từng bài"],
        ["B", "Đề mẫu đúng ma trận + đáp án chi tiết", "18 câu Phần I, 2 câu Đúng/Sai, 2 câu trả lời ngắn, 3 câu tự luận \u2014 có lời giải từng ý"],
        ["C", "Ngân hàng 30 câu luyện thêm theo đơn vị", "Đổi dạng câu hỏi để chống học vẹt, đáp án ngay dưới mỗi đơn vị"],
        ["D + Phụ lục", "Tổng ôn trước ngày thi + bảng đối chiếu", "Phiếu công thức 1 trang, lộ trình ôn, chứng minh phủ 100% đặc tả"],
    ], [22 * mm, 58 * mm, 76 * mm]))
    story.append(sp(3))
    story.append(h3("Mục lục"))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc1", fontName="Sans-Bold", fontSize=10, leading=15, textColor=NAVY, leftIndent=2),
        ParagraphStyle("toc2", fontName="Sans", fontSize=9, leading=12.5, textColor=colors.HexColor("#333333"), leftIndent=12),
    ]
    toc.dotsMinLevel = 0
    story.append(toc)
    story.append(PageBreak())

    # ------------------------------------------------------------ PHẦN 0
    story.append(h1("PHẦN 0 \u00b7 GIẢI MÃ MA TRẬN TRONG 5 PHÚT"))
    story.append(P("Đề kiểm tra giữa kì I \u2013 Vật lí 10 (năm học 2026\u20132027): <b>hình thức 70% trắc nghiệm + 30% tự luận, "
                   "thời gian làm bài 50 phút</b>. Ma trận chia đề thành 4 phần. Đếm đúng số mục phải làm:"))
    story.append(styled_table([
        ["Phần", "Dạng câu hỏi", "Số lượng", "Mức độ trong ma trận", "Đơn vị kiến thức xuất hiện"],
        ["I", "Trắc nghiệm nhiều lựa chọn (4 phương án)", "18 câu", "10 Biết + 8 Hiểu", "Cả 9 đơn vị 1.1\u20132.6"],
        ["II", "Trắc nghiệm Đúng/Sai (2 câu \u00d7 4 ý)", "8 ý", "6 Biết + 2 Hiểu", "Câu 1: 2.2 + 2.3 \u00b7 Câu 2: 2.5"],
        ["III", "Trắc nghiệm trả lời ngắn", "2 câu", "1 Biết + 1 Hiểu", "2.2 (Biết) \u00b7 2.6 (Hiểu)"],
        ["IV", "Tự luận", "3 câu", "1 Hiểu + 2 Vận dụng", "2.2 (Hiểu) \u00b7 2.5 (Vận dụng \u00d7 2)"],
        ["<b>Tổng</b>", "", "<b>25 câu / 31 mục chấm</b>", "<b>17 Biết \u00b7 12 Hiểu \u00b7 2 Vận dụng</b>", ""],
    ], [16 * mm, 52 * mm, 32 * mm, 36 * mm, 30 * mm], align_center_cols={0, 2}))
    story.append(sp(2))
    story.append(P("<i>Ghi chú:</i> ma trận dùng chữ \u201cPhần 1\u201d (số Ả Rập) trong bảng nhưng đề cương thống nhất viết Phần I\u2013IV cho dễ đọc. "
                   "Kí hiệu \u201c2-I\u201d trong ma trận nghĩa là 2 ý thuộc Câu 1 của Phần II; \u201c2-II\u201d là 2 ý thuộc Câu 2. "
                   "Tài liệu gốc <b>không ghi điểm số cho từng phần/câu</b> \u2014 đề cương không tự suy diễn điểm số.", "BodySmall"))
    story.append(h2("Bài nào chiếm bao nhiêu câu? \u2014 Học theo tỉ trọng, đừng học đều"))
    story.append(styled_table([
        ["Đơn vị kiến thức", "Phần I", "Phần II", "Phần III", "Phần IV", "Tổng mục", "Tỉ trọng"],
        ["1.1 Làm quen với Vật lí", "1", "\u2014", "\u2014", "\u2014", "1", "3%"],
        ["1.2 An toàn phòng thực hành", "2", "\u2014", "\u2014", "\u2014", "2", "6%"],
        ["1.3 Sai số trong phép đo", "1", "\u2014", "\u2014", "\u2014", "1", "3%"],
        ["2.1 Độ dịch chuyển & quãng đường", "3", "\u2014", "\u2014", "\u2014", "3", "10%"],
        ["2.2 Tốc độ và vận tốc (+ đo tốc độ)", "1", "2 ý", "1", "1", "5", "16%"],
        ["2.3 Đồ thị độ dịch chuyển \u2013 thời gian", "2", "2 ý", "\u2014", "\u2014", "4", "13%"],
        ["2.4 Chuyển động biến đổi. Gia tốc", "2", "\u2014", "\u2014", "\u2014", "2", "6%"],
        ["<b>2.5 Chuyển động thẳng biến đổi đều</b>", "<b>3</b>", "<b>4 ý</b>", "\u2014", "<b>2</b>", "<b>9</b>", "<b>29%</b>"],
        ["2.6 Sự rơi tự do", "3", "\u2014", "1", "\u2014", "4", "13%"],
        ["<b>Tổng</b>", "<b>18</b>", "<b>8 ý</b>", "<b>2</b>", "<b>3</b>", "<b>31</b>", "<b>100%</b>"],
    ], [52 * mm, 16 * mm, 16 * mm, 16 * mm, 16 * mm, 20 * mm, 20 * mm], align_center_cols={1, 2, 3, 4, 5, 6}))
    story.append(sp(2))
    story.append(callout("\u2605 Kết luận chiến lược (quan trọng nhất của Phần 0)",
                         ["<b>2.5 \u2013 Chuyển động thẳng biến đổi đều là \u201cmỏ điểm\u201d:</b> 9/31 mục (29%), xuất hiện ở cả 3 phần I, II, IV. Học yếu bài này là mất gần một phần ba bài kiểm tra.",
                          "<b>Nhóm thứ hai (2.2 + 2.3 + 2.6 + 2.1):</b> 16/31 mục. Đây là phần Động học cơ bản \u2014 thuộc công thức và đọc được đồ thị là lấy trọn.",
                          "<b>Chương I (1.1\u20131.3):</b> chỉ 4/31 mục, toàn ở mức Biết/Hiểu \u2014 học bằng hộp NHỚ NHANH trong 20 phút là đủ, đừng tốn cả buổi.",
                          "Mức độ toàn đề: <b>Biết 17 \u2013 Hiểu 12 \u2013 Vận dụng 2</b>. Nghĩa là đề nghiêng mạnh về thuộc bài + hiểu bản chất; phần Vận dụng chỉ tập trung ở tự luận 2.5. Các yêu cầu \u201cvận dụng / vận dụng cao\u201d ghi trong đặc tả (sai số, độ dịch chuyển, CĐTBĐĐ, rơi tự do) vẫn được luyện ở Phần C để em không bỡ ngỡ nếu đề thật ra khó hơn ma trận gợi ý."],
                         bg=BG_TEAL, accent=TEAL))
    story.append(sp(2))
    story.append(h2("Phân bổ 50 phút trong phòng thi (gợi ý, không phải quy định)"))
    story.append(styled_table([
        ["Chặng", "Thời gian gợi ý", "Chiến thuật"],
        ["Phần I (18 câu)", "15 phút", "Câu Biết làm ngay; câu tính toán quá 1 phút chưa ra thì đánh dấu, quay lại sau"],
        ["Phần II (8 ý)", "8 phút", "Đọc từng ý độc lập; ý chứa \u201cluôn luôn / chỉ / mọi\u201d thường là ý Sai \u2014 kiểm tra kĩ"],
        ["Phần III (2 câu)", "5 phút", "Tính nháp cẩn thận, ghi <b>kèm đơn vị</b>; đây là 2 câu \u201cngắn nhưng dễ mất vì ẩu\u201d"],
        ["Phần IV (3 câu)", "20 phút", "Ghi công thức \u2192 thay số \u2192 kết quả + đơn vị + kết luận; đổi km/h \u00f7 3,6 ngay từ dòng đầu"],
        ["Soát bài", "2 phút", "Kiểm tra: đã tô/ghi đủ 18 + 8 + 2 chưa; đơn vị và dấu của gia tốc đã đúng chưa"],
    ], [34 * mm, 28 * mm, 94 * mm]))
    story.append(PageBreak())

    # ------------------------------------------------------------ CÁC PHẦN CHÍNH
    story.extend(content_theory.get_story())
    story.append(PageBreak())
    story.extend(content_exam.get_story())
    story.append(PageBreak())
    story.extend(content_practice.get_story())

    doc.multiBuild(story)
    print(f"OK -> {OUT} ({os.path.getsize(OUT)/1024:.0f} KB)")


if __name__ == "__main__":
    build()
