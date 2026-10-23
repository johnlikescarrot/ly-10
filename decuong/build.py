# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from style import *          # noqa
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, NextPageTemplate
from reportlab.lib.units import mm
import content_front, content_theory_a, content_theory_b
import content_tools, content_exam, content_cards

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "De_cuong_on_tap_Vat_li_10_GK1_2026.pdf")


# ------------------------------------------------------------------ cover art
def draw_cover(canv, doc):
    canv.saveState()
    W, H = PAGE_W, PAGE_H
    canv.setFillColor(colors.white)
    canv.rect(0, 0, W, H, stroke=0, fill=1)

    # ---------------- khối navy trên
    canv.setFillColor(NAVY)
    canv.rect(0, H - 268, W, 268, stroke=0, fill=1)
    canv.setFillColor(colors.HexColor("#274C74"))
    canv.circle(W - 54, H - 54, 70, stroke=0, fill=1)
    canv.setFillColor(colors.HexColor("#2F5A87"))
    canv.circle(W - 14, H - 138, 44, stroke=0, fill=1)
    canv.setFillColor(colors.HexColor("#203F63"))
    canv.circle(W - 96, H - 226, 26, stroke=0, fill=1)

    x = LM
    canv.setFont("DJSans-Bold", 8.4)
    canv.setFillColor(colors.HexColor("#F2B24A"))
    canv.drawString(x, H - 72, "TÀI LIỆU ÔN THI  ·  BÁM SÁT MA TRẬN VÀ ĐẶC TẢ ĐỀ KIỂM TRA")

    canv.setFont("DJSans-Bold", 36)
    canv.setFillColor(WHITE)
    canv.drawString(x, H - 128, "ĐỀ CƯƠNG ÔN TẬP")
    canv.setFont("DJSans-Bold", 24)
    canv.drawString(x, H - 164, "GIỮA HỌC KÌ I")

    canv.setStrokeColor(AMBER)
    canv.setLineWidth(2.6)
    canv.line(x, H - 182, x + 88, H - 182)

    canv.setFont("DJSans", 13)
    canv.setFillColor(colors.HexColor("#D6E3F0"))
    canv.drawString(x, H - 208, "MÔN VẬT LÍ  –  LỚP 10")
    canv.setFont("DJSans", 9.2)
    canv.setFillColor(colors.HexColor("#9FB8D2"))
    canv.drawString(x, H - 228, "Năm học 2026 – 2027  ·  Chương Mở đầu & Động học chất điểm")

    # ---------------- thẻ thông tin
    cy = H - 296
    card_h = 100
    canv.setFillColor(colors.HexColor("#F4F7FB"))
    canv.setStrokeColor(colors.HexColor("#E1E8F1"))
    canv.setLineWidth(0.8)
    canv.roundRect(LM, cy - card_h, W - LM - RM, card_h, 6, stroke=1, fill=1)
    canv.setFillColor(TEAL)
    canv.roundRect(LM, cy - card_h, 4.5, card_h, 2, stroke=0, fill=1)

    lines = [
        ("Hình thức", "70% trắc nghiệm  +  30% tự luận"),
        ("Thời gian", "50 phút"),
        ("Cấu trúc", "18 câu trắc nghiệm · 2 câu Đúng/Sai (8 ý) · 2 câu tự luận ngắn · 1 bài toán vận dụng"),
        ("Nội dung", "Bài 1 → Bài 10 – Chương Mở đầu & Động học chất điểm"),
    ]
    ty = cy - 20
    for k, v in lines:
        canv.setFont("DJSans-Bold", 8.0)
        canv.setFillColor(GREY)
        canv.drawString(LM + 16, ty, k.upper())
        canv.setFont("DJSerif", 9.2)
        canv.setFillColor(INK)
        canv.drawString(LM + 78, ty, v)
        ty -= 21

    # ---------------- 4 ô số liệu
    fy = cy - card_h - 92
    items = [
        ("10", "bài học cô đọng", "Lý thuyết – công thức – ví dụ mẫu"),
        ("1", "đề mô phỏng", "Khớp 100% ma trận, có thang điểm"),
        ("60", "thẻ nhớ nhanh", "Hỏi – đáp 1 dòng, học 8 phút"),
        ("31", "câu &amp; ý có lời giải", "18 TN + 8 Đ/S + 2 TL + 3 ý"),
    ]
    cw = (W - LM - RM - 3 * 9) / 4.0
    for i, (num, lab, sub) in enumerate(items):
        cx = LM + i * (cw + 9)
        canv.setFillColor(colors.white)
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.7)
        canv.roundRect(cx, fy, cw, 74, 5, stroke=1, fill=1)
        canv.setFillColor(NAVY)
        canv.setFont("DJSans-Bold", 20)
        canv.drawString(cx + 9, fy + 42, num)
        canv.setFillColor(TEAL)
        canv.setFont("DJSans-Bold", 7.4)
        canv.drawString(cx + 9, fy + 28, lab)
        canv.setFillColor(GREY)
        canv.setFont("DJSerif", 6.4)
        words, line, yy = sub.split(), "", fy + 17
        for w_ in words:
            test = (line + " " + w_).strip()
            if canv.stringWidth(test, "DJSerif", 6.4) > cw - 16:
                canv.drawString(cx + 9, yy, line)
                yy -= 8.2
                line = w_
            else:
                line = test
        canv.drawString(cx + 9, yy, line)

    # ---------------- cấu trúc tài liệu
    sy = fy - 44
    canv.setFont("DJSans-Bold", 8.6)
    canv.setFillColor(NAVY)
    canv.drawString(LM, sy, "TRONG TÀI LIỆU NÀY")
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.7)
    canv.line(LM + 120, sy + 3, W - RM, sy + 3)

    parts = [
        ("0", "Đọc vị đề thi", "Cấu trúc, ma trận, chiến lược 50 phút"),
        ("1", "Lý thuyết 10 bài", "Khái niệm – công thức – ví dụ – mẹo – bẫy"),
        ("2", "Sổ tay công thức", "26 công thức + cây quyết định giải bài"),
        ("3", "Đề mô phỏng & lời giải", "Đáp án, giải chi tiết, thang điểm"),
        ("4", "70 thẻ nhớ nhanh", "Hỏi – đáp theo 3 nhóm chuyên đề"),
        ("5", "Chống mất điểm", "12 lỗi kinh điển + quy trình 4 bước"),
        ("6", "Trang bỏ túi & phụ lục", "Ôn 15 phút cuối + đặc tả cần đạt"),
    ]
    py = sy - 20
    col_w = (W - LM - RM) / 2.0
    for i, (num, name, desc) in enumerate(parts):
        col = i % 2
        row = i // 2
        px = LM + col * col_w
        pyy = py - row * 33
        canv.setFillColor(NAVY)
        canv.circle(px + 7, pyy + 2, 7.4, stroke=0, fill=1)
        canv.setFillColor(WHITE)
        canv.setFont("DJSans-Bold", 7.6)
        canv.drawCentredString(px + 7, pyy - 0.6, num)
        canv.setFillColor(INK)
        canv.setFont("DJSans-Bold", 8.4)
        canv.drawString(px + 20, pyy, name)
        canv.setFillColor(GREY)
        canv.setFont("DJSerif", 7.2)
        canv.drawString(px + 20, pyy - 10, desc)

    # ---------------- dải kết
    qy = 128
    canv.setFillColor(AMBER_L)
    canv.roundRect(LM, qy, W - LM - RM, 46, 5, stroke=0, fill=1)
    canv.setFillColor(AMBER)
    canv.roundRect(LM, qy, 3.6, 46, 1.8, stroke=0, fill=1)
    canv.setFillColor(colors.HexColor("#6B4A12"))
    canv.setFont("DJSerif", 8.2)
    canv.drawString(LM + 14, qy + 27, "Học theo đúng thứ tự ưu tiên trong ma trận: 2.5 và 2.2 chiếm gần 2/3 số ý của đề.")
    canv.drawString(LM + 14, qy + 13, "Thuộc bảng – nhớ công thức – luyện 5 dạng bài: ba việc đó là đủ cho một điểm 9.")

    # ---------------- footer
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.7)
    canv.line(LM, 86, W - RM, 86)
    canv.setFillColor(INK)
    canv.setFont("DJSans-Bold", 7.8)
    canv.drawString(LM, 70, "Biên soạn dựa trên tài liệu:")
    canv.setFont("DJSerif", 8.2)
    canv.setFillColor(colors.HexColor("#44505F"))
    canv.drawString(LM, 58, "“MA TRẬN ĐẶC TẢ KTGK I L10 – 2026” (Vật lí 10, năm học 2026 – 2027)")
    canv.setFont("DJSerif", 7.2)
    canv.drawString(LM, 44, "Tài liệu lưu hành nội bộ phục vụ ôn tập. Nội dung được hệ thống hoá, "
                            "bổ sung ví dụ và lời giải chi tiết.")
    canv.setFont("DJSans-Bold", 7.8)
    canv.setFillColor(NAVY)
    canv.drawRightString(W - RM, 58, "PHIÊN BẢN 1.0")
    canv.restoreState()


def draw_body(canv, doc):
    canv.saveState()
    W, H = PAGE_W, PAGE_H
    canv.setFont("DJSans", 7.4)
    canv.setFillColor(GREY)
    canv.drawString(LM, H - 26, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  VẬT LÍ 10")
    canv.drawRightString(W - RM, H - 26, "Năm học 2026 – 2027")
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.6)
    canv.line(LM, H - 32, W - RM, H - 32)

    canv.line(LM, 34, W - RM, 34)
    canv.setFont("DJSerif", 7.2)
    canv.drawString(LM, 22, "Hệ thống hoá từ ma trận – đặc tả đề kiểm tra giữa kì I môn Vật lí 10")
    # số trang
    canv.setFillColor(NAVY)
    canv.roundRect(W - RM - 42, 18, 42, 12, 3, stroke=0, fill=1)
    canv.setFillColor(WHITE)
    canv.setFont("DJSans-Bold", 7.4)
    canv.drawCentredString(W - RM - 21, 21.5, "%d" % (doc.page - 1))
    canv.restoreState()


class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập giữa kì I – Vật lí 10 (2026–2027)",
                                 author="Tài liệu ôn tập",
                                 subject="Vật lí 10 – Giữa học kì I")
        fw = PAGE_W - LM - RM
        cover_frame = Frame(LM, BM, fw, PAGE_H - BM - 100, id="cover")
        body_frame = Frame(LM, BM, fw, PAGE_H - TM - BM - 8, id="body")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
            PageTemplate(id="body", frames=[body_frame], onPage=draw_body),
        ])

    def afterFlowable(self, flowable):
        toc = getattr(flowable, "_toc", None)
        if toc:
            level, text = toc
            self.notify("TOCEntry", (level, text, self.page - 1))
            self._seq = getattr(self, "_seq", 0) + 1
            key = "h%d" % self._seq
            plain = text.replace("<b>", "").replace("</b>", "")
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(plain, key, level=min(level, 2), closed=(level == 0))


def build():
    story = [NextPageTemplate("body"), PageBreak()]

    # ---- trang mục lục
    story.append(Paragraph("MỤC LỤC", st("toct", fontName="DJSans-Bold", fontSize=17,
                                         leading=22, textColor=NAVY, spaceAfter=3,
                                         alignment=TA_LEFT)))
    story.append(Paragraph("Bấm theo số trang để tra cứu nhanh khi ôn tập.",
                           st("tocsub", fontSize=8.4, leading=11, textColor=GREY,
                              spaceAfter=7)))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("TOC0", fontName="DJSans-Bold", fontSize=8.9, leading=10.9,
                       textColor=NAVY, spaceBefore=1.4, leftIndent=0, firstLineIndent=0),
        ParagraphStyle("TOC1", fontName="DJSerif", fontSize=8.2, leading=9.9,
                       textColor=INK, leftIndent=16, firstLineIndent=0),
    ]
    toc.dotsMinLevel = 0
    story.append(toc)

    story.append(PageBreak())

    story.append(Spacer(1, 10))
    story.append(CondPageBreak(200))
    story += content_front.story()
    story += content_theory_a.story()
    story += content_theory_b.story()
    story += content_tools.story()
    story += content_exam.story()
    story += content_cards.story()

    def flatten(x):
        out = []
        for it in x:
            if isinstance(it, (list, tuple)):
                out.extend(flatten(it))
            else:
                out.append(it)
        return out

    story = flatten(story)
    doc = Doc(OUT)
    doc.multiBuild(story)
    print("OK ->", OUT)


if __name__ == "__main__":
    build()
