# -*- coding: utf-8 -*-
"""Khung trình bày (layout engine) cho đề cương PDF – ReportLab/Platypus."""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame,
                                KeepTogether, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table,
                                TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "assets", "fonts")

# ----------------------------------------------------------------------------- fonts
F = lambda n: os.path.join(FONT_DIR, n)
pdfmetrics.registerFont(TTFont("BVP", F("BeVietnamPro-Regular.ttf")))
pdfmetrics.registerFont(TTFont("BVP-It", F("BeVietnamPro-Italic.ttf")))
pdfmetrics.registerFont(TTFont("BVP-SB", F("BeVietnamPro-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("BVP-B", F("BeVietnamPro-Bold.ttf")))
pdfmetrics.registerFont(TTFont("BVP-BI", F("BeVietnamPro-BoldItalic.ttf")))
pdfmetrics.registerFont(TTFont("BVP-XB", F("BeVietnamPro-ExtraBold.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu", F("DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVu-B", F("DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("BVP", normal="BVP", bold="BVP-B",
                              italic="BVP-It", boldItalic="BVP-BI")

_CMAP = pdfmetrics.getFont("BVP").face.charToGlyph
_TAG = re.compile(r"(<[^<>]+>)")


def _fontify(chunk, bold=False):
    """Bọc các ký tự không có trong font chính bằng font dự phòng DejaVu."""
    out, buf, mode = [], [], None
    for ch in chunk:
        m = (ord(ch) in _CMAP)
        if m != mode:
            if buf:
                txt = "".join(buf)
                out.append(txt if mode else '<font name="%s">%s</font>'
                           % ("DejaVu-B" if bold else "DejaVu", txt))
            buf, mode = [ch], m
        else:
            buf.append(ch)
    if buf:
        txt = "".join(buf)
        out.append(txt if mode else '<font name="%s">%s</font>'
                   % ("DejaVu-B" if bold else "DejaVu", txt))
    return "".join(out)


def mix(s, bold=False):
    """Chuẩn hoá markup: escape < > rời, thay ký tự thiếu font."""
    s = re.sub(r"\s<\s", " &lt; ", s)
    s = re.sub(r"\s>\s", " &gt; ", s)
    parts = _TAG.split(s)
    res = []
    for p in parts:
        if p.startswith("<") and p.endswith(">") and _TAG.fullmatch(p):
            res.append(p)
        else:
            res.append(_fontify(p, bold))
    return "".join(res)


# ----------------------------------------------------------------------------- palette
INK = colors.HexColor("#111A33")
MUTED = colors.HexColor("#586180")
PRIMARY = colors.HexColor("#16357A")       # xanh navy
PRIMARY_L = colors.HexColor("#3E63C4")
TEAL = colors.HexColor("#0E7C86")
AMBER = colors.HexColor("#C2831A")
RED = colors.HexColor("#B3261E")
GREEN = colors.HexColor("#1B7A45")
PAPER = colors.HexColor("#FBFAF7")
LINE = colors.HexColor("#D8DCE8")

TINT = {
    "primary": colors.HexColor("#EDF1FB"),
    "teal": colors.HexColor("#E7F4F5"),
    "amber": colors.HexColor("#FDF5E3"),
    "red": colors.HexColor("#FCEDEC"),
    "green": colors.HexColor("#EAF6EF"),
    "grey": colors.HexColor("#F2F3F7"),
}

PAGE_W, PAGE_H = A4
LM, RM, TM, BM = 1.85 * cm, 1.85 * cm, 2.05 * cm, 1.75 * cm

# ----------------------------------------------------------------------------- styles
BODY = ParagraphStyle("body", fontName="BVP", fontSize=10.0, leading=14.6,
                      textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5.0)
BODY_L = ParagraphStyle("body_l", parent=BODY, alignment=TA_LEFT)
SMALL = ParagraphStyle("small", parent=BODY, fontSize=8.6, leading=12.4,
                       textColor=MUTED)
TINY = ParagraphStyle("tiny", parent=BODY, fontSize=7.8, leading=10.5,
                      textColor=MUTED)
H2S = ParagraphStyle("h2", fontName="BVP-B", fontSize=14.2, leading=18.5,
                     textColor=PRIMARY, spaceBefore=14, spaceAfter=6,
                     alignment=TA_LEFT)
H3S = ParagraphStyle("h3", fontName="BVP-B", fontSize=10.9, leading=15,
                     textColor=INK, spaceBefore=9, spaceAfter=3.5,
                     alignment=TA_LEFT)
BULLET = ParagraphStyle("bullet", parent=BODY, leftIndent=13, bulletIndent=2,
                        spaceAfter=2.6, alignment=TA_LEFT,
                        bulletFontName="BVP-SB", bulletFontSize=9.5)
CENTER = ParagraphStyle("center", parent=BODY, alignment=TA_CENTER)
FORMULA = ParagraphStyle("formula", parent=BODY, alignment=TA_CENTER,
                         fontSize=11.2, leading=17, textColor=PRIMARY,
                         spaceAfter=2, spaceBefore=2)
QSTYLE = ParagraphStyle("q", parent=BODY, alignment=TA_LEFT, spaceAfter=2,
                        leading=14.8)


def cond(space):
    """Chỉ ngắt trang khi còn ít hơn `space` điểm."""
    return [CondPageBreak(space)]


def P(text, style=BODY, **kw):
    return Paragraph(mix(text, bold=kw.pop("bold", False)), style)


def H2(text):
    t = Table([[P('<font color="#C2831A">■</font>&nbsp;&nbsp;' + text, H2S)]],
              colWidths=[PAGE_W - LM - RM])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 1, colors.HexColor("#E7D9BC")),
    ]))
    return [Spacer(1, 8), t, Spacer(1, 5)]


def H3(text):
    return P(text, H3S)


def bullets(items, style=BULLET, bullet="•"):
    return [Paragraph(mix(i), style, bulletText=bullet) for i in items]


def numbered(items, style=None):
    style = style or ParagraphStyle("num", parent=BULLET, leftIndent=17,
                                    bulletIndent=3)
    return [Paragraph(mix(t), style, bulletText="%d." % (i + 1))
            for i, t in enumerate(items)]


def body(text):
    return P(text)


# ----------------------------------------------------------------------------- boxes
def box(title, content, kind="primary", icon=None, width=None):
    """Khối thông tin có thanh màu bên trái; content là list flowable hoặc str."""
    color = {"primary": PRIMARY, "teal": TEAL, "amber": AMBER, "red": RED,
             "green": GREEN, "grey": MUTED}[kind]
    tint = TINT[kind]
    if isinstance(content, str):
        content = [P(content)]
    inner = []
    if title:
        tstyle = ParagraphStyle("boxtitle", fontName="BVP-B", fontSize=9.9,
                                leading=13.6, textColor=color,
                                spaceAfter=3, alignment=TA_LEFT)
        inner.append(Paragraph(mix(title.upper() if False else title,
                                   bold=True), tstyle))
    inner.extend(content)
    w = width or (PAGE_W - LM - RM)
    t = Table([["", inner]], colWidths=[4.2, w - 4.2])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), tint),
        ("BACKGROUND", (0, 0), (0, -1), color),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 10),
        ("RIGHTPADDING", (1, 0), (1, -1), 10),
        ("TOPPADDING", (1, 0), (1, -1), 7.5),
        ("BOTTOMPADDING", (1, 0), (1, -1), 7.5),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]


def formula(lines, label=None, width=None):
    """Hộp công thức căn giữa."""
    w = width or (PAGE_W - LM - RM)
    paras = []
    if label:
        paras.append(P(label, ParagraphStyle("flabel", parent=SMALL,
                                             textColor=AMBER,
                                             fontName="BVP-SB",
                                             alignment=TA_CENTER)))
    if isinstance(lines, str):
        lines = [lines]
    for ln in lines:
        paras.append(P(ln, FORMULA))
    t = Table([[paras]], colWidths=[w])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F5F7FD")),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#CBD5EE")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 7)]


def table(data, widths, header=True, size=8.9, align=None, zebra=True,
          head_bg=PRIMARY, wrap_header=True, extra=None):
    rows = []
    for r, row in enumerate(data):
        cells = []
        for c, cell in enumerate(row):
            if isinstance(cell, str):
                st = ParagraphStyle("tc", parent=BODY, fontSize=size,
                                    leading=size * 1.35,
                                    alignment=(align[c] if align else TA_LEFT),
                                    textColor=colors.white if (header and r == 0)
                                    else INK,
                                    fontName="BVP-SB" if (header and r == 0)
                                    else "BVP",
                                    spaceAfter=0)
                cells.append(Paragraph(mix(cell), st))
            else:
                cells.append(cell)
        rows.append(cells)
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, LINE),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#C3CADC")),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), head_bg),
                  ("LINEBELOW", (0, 0), (-1, 0), 0.7, head_bg)]
    if zebra:
        for i in range(1 if header else 0, len(rows)):
            if (i % 2 == 0):
                style.append(("BACKGROUND", (0, i), (-1, i),
                              colors.HexColor("#F6F7FB")))
    if extra:
        style += extra
    t.setStyle(TableStyle(style))
    return t


# ----------------------------------------------------------------------------- banners
BANNERS = []   # (level, title, page) – dùng để tạo bookmark PDF


def page_of(kicker_prefix):
    """Số trang của banner đầu tiên có kicker bắt đầu bằng tiền tố cho trước."""
    for kicker, title, page in BANNERS:
        if kicker.startswith(kicker_prefix):
            return str(page)
    return "—"


class SectionBanner(Flowable):
    def __init__(self, kicker, title, subtitle=None, color=PRIMARY,
                 height=118, width=PAGE_W - LM - RM):
        Flowable.__init__(self)
        self.kicker, self.title, self.subtitle = kicker, title, subtitle
        self.color, self.height, self.width = color, height, width

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        BANNERS.append((self.kicker, self.title, c.getPageNumber()))
        c.setFillColor(self.color)
        c.roundRect(0, 0, w, h, 8, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#0F2456"))
        c.roundRect(0, 0, 120, h, 8, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("BVP-SB", 8.2)
        c.drawString(20, h - 26, self.kicker.upper().replace("&amp;", "&"))
        title = self.title.replace("&amp;", "&")
        size = 21.0
        while size > 12 and c.stringWidth(title, "BVP-XB", size) > w - 34:
            size -= 0.5
        c.setFont("BVP-XB", size)
        c.drawString(20, h - 62, title)
        if self.subtitle:
            c.setFont("BVP", 8.6)
            c.setFillColor(colors.HexColor("#D5DEF7"))
            # vẽ subtitle trong vùng phải
            from reportlab.platypus import Paragraph as _P
            st = ParagraphStyle("sb", fontName="BVP", fontSize=8.4, leading=11.4,
                                textColor=colors.HexColor("#D5DEF7"))
            p = _P(mix(self.subtitle), st)
            pw, ph = p.wrap(w - 160, h)
            p.drawOn(c, 133, h - 30 - ph + 14)


class Divider(Flowable):
    """Đường kẻ mảnh có nhãn giữa."""
    def __init__(self, text="", width=PAGE_W - LM - RM):
        Flowable.__init__(self)
        self.text, self.width = text, width
        self.height = 16

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setStrokeColor(LINE)
        c.setLineWidth(0.7)
        c.line(0, 8, self.width, 8)
        if self.text:
            c.setFillColor(PAPER)
            c.setFont("BVP-SB", 7.6)
            tw = c.stringWidth(self.text, "BVP-SB", 7.6)
            c.rect(self.width / 2 - tw / 2 - 6, 1, tw + 12, 14, stroke=0,
                   fill=1)
            c.setFillColor(MUTED)
            c.drawCentredString(self.width / 2, 4.5, self.text)


# ----------------------------------------------------------------------------- questions
def q_head(num, tag=None, level=None):
    """Badge số câu + nhãn mức độ."""
    label = "<b>Câu %s.</b>" % num
    extra = ""
    if tag:
        extra += '&nbsp;&nbsp;<font size="7.6" color="#586180">%s</font>' % tag
    return P(label + extra, ParagraphStyle("qh", parent=QSTYLE,
                                           fontName="BVP-B", spaceBefore=6))


def badge_row(num, content_flowables, color=PRIMARY, tag=None):
    numstyle = ParagraphStyle("num", fontName="BVP-B", fontSize=10.5,
                              textColor=colors.white, alignment=TA_CENTER)
    head = [Paragraph(str(num), numstyle)]
    t = Table([[head, content_flowables]], colWidths=[21, PAGE_W - LM - RM - 21])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), color),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("TOPPADDING", (0, 0), (0, 0), 2.5),
        ("BOTTOMPADDING", (0, 0), (0, 0), 2.5),
        ("LEFTPADDING", (1, 0), (1, 0), 9),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("TOPPADDING", (1, 0), (1, 0), 0),
        ("BOTTOMPADDING", (1, 0), (1, 0), 0),
    ]))
    out = [Spacer(1, 5), t]
    if tag:
        out.append(Spacer(1, 1.5))
        out.append(P('<font size="7.4" color="#7A839C">%s</font>' % tag,
                     ParagraphStyle("tg", parent=SMALL, fontSize=7.4,
                                    leading=9.6, leftIndent=30)))
    return out


# ----------------------------------------------------------------------------- dok
class Doc(BaseDocTemplate):
    def __init__(self, path, canvasmaker=None, **kw):
        self._real_path = path
        BaseDocTemplate.__init__(self, path, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập Giữa kì I – Vật lí 10",
                                 author="Tổng hợp từ Ma trận đặc tả KTGK I L10 – 2026",
                                 subject="Ôn tập Vật lí 10 – Giữa học kì I",
                                 **kw)
        frame_cover = Frame(0, 0, PAGE_W, PAGE_H, id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0,
                            bottomPadding=0)
        frame_body = Frame(LM, BM, PAGE_W - LM - RM, PAGE_H - TM - BM,
                           id="body", leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_cover], onPage=draw_cover_bg),
            PageTemplate(id="body", frames=[frame_body], onPage=draw_header),
        ])
        self.total_pages = 0

    def build_twice(self, story_fn):
        import io
        self.build(story_fn())          # lượt 1: đếm số trang
        self.total_pages = self.page
        self.filename = self._real_path
        self.build(story_fn())          # lượt 2: in đúng "Trang x / y"


def draw_header(canvas, doc):
    c = canvas
    c.saveState()
    # dải màu trên cùng
    c.setFillColor(PRIMARY)
    c.rect(0, PAGE_H - 0.62 * cm, PAGE_W, 0.62 * cm, stroke=0, fill=1)
    c.setFillColor(AMBER)
    c.rect(0, PAGE_H - 0.62 * cm, 3.4 * cm, 0.62 * cm, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("BVP-SB", 7.4)
    c.drawString(LM, PAGE_H - 0.42 * cm, "VẬT LÍ 10  ·  GIỮA HỌC KÌ I")
    c.setFont("BVP", 7.4)
    c.drawRightString(PAGE_W - RM, PAGE_H - 0.42 * cm,
                      "Đề cương ôn tập 2026 – 2027")
    # chân trang
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(LM, 1.15 * cm, PAGE_W - RM, 1.15 * cm)
    c.setFillColor(MUTED)
    c.setFont("BVP", 7.2)
    c.drawString(LM, 0.75 * cm, "Biên soạn dựa trên Ma trận đặc tả KTGK I – L10 (2026)")
    total = getattr(doc, "total_pages", 0)
    txt = "Trang %d" % canvas.getPageNumber()
    if total:
        txt += " / %d" % total
    c.setFillColor(PRIMARY)
    c.setFont("BVP-SB", 7.6)
    c.drawRightString(PAGE_W - RM, 0.75 * cm, txt)
    c.restoreState()


def draw_cover_bg(canvas, doc):
    c = canvas
    c.saveState()
    c.setFillColor(colors.HexColor("#0C1733"))
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    # hoạ tiết
    c.setFillColor(colors.HexColor("#14265A"))
    c.circle(PAGE_W * 0.92, PAGE_H * 0.86, 5.4 * cm, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#16357A"))
    c.circle(PAGE_W * 0.95, PAGE_H * 0.93, 2.9 * cm, stroke=0, fill=1)
    # dải "3 vòng ôn tập" ở đáy bìa
    c.setFillColor(colors.HexColor("#8C99BE"))
    c.setFont("BVP-SB", 7.6)
    c.drawString(LM, 6.28 * cm, "LỘ TRÌNH 3 VÒNG")
    steps = [("1", "HIỂU", "đọc mục B"), ("2", "NHỚ", "học mục C"),
             ("3", "THI", "làm mục D – E")]
    x = LM
    bw = (PAGE_W - LM - RM - 0.6 * cm) / 3
    for num, label, sub in steps:
        c.setFillColor(colors.HexColor("#132A5E"))
        c.roundRect(x, 4.58 * cm, bw - 0.25 * cm, 1.32 * cm, 5, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#F0B53C"))
        c.setFont("BVP-XB", 15)
        c.drawString(x + 10, 5.15 * cm, num)
        c.setFillColor(colors.white)
        c.setFont("BVP-B", 9.2)
        c.drawString(x + 28, 5.28 * cm, label)
        c.setFillColor(colors.HexColor("#93A3CC"))
        c.setFont("BVP", 7.4)
        c.drawString(x + 28, 4.85 * cm, sub)
        x += bw
    c.setFillColor(colors.HexColor("#F0B53C"))
    c.rect(LM, 4.28 * cm, 2.2 * cm, 0.1 * cm, stroke=0, fill=1)
    c.restoreState()


# ----------------------------------------------------------------------------- graph
class GraphSketch(Flowable):
    """Vẽ nhanh một đồ thị minh hoạ trên hệ trục."""

    def __init__(self, series, xlabel="t (s)", ylabel="d (m)", width=250,
                 height=155, xmax=10, ymax=10, caption=None, marks=None,
                 guides=None, color=PRIMARY):
        Flowable.__init__(self)
        self.series = series      # list of dicts: pts, color, dash, label
        self.xlabel, self.ylabel = xlabel, ylabel
        self.width, self.height = width, height
        self.xmax, self.ymax = xmax, ymax
        self.caption = caption
        self.marks = marks or []  # [(x, y, text)]
        self.guides = guides or []  # [(x1,y1,x2,y2)]
        self.color = color

    def wrap(self, aw, ah):
        return self.width, self.height + (14 if self.caption else 0)

    def draw(self):
        c = self.canv
        ox, oy = 34, 24
        w, h = self.width - 46, self.height - 34
        sx, sy = w / self.xmax, h / self.ymax

        def X(v):
            return ox + v * sx

        def Y(v):
            return oy + v * sy

        c.setStrokeColor(colors.HexColor("#C3CADC"))
        c.setLineWidth(0.7)
        c.line(ox, oy, ox + w + 6, oy)
        c.line(ox, oy, ox, oy + h + 6)
        # arrow heads
        c.setFillColor(colors.HexColor("#C3CADC"))
        p = c.beginPath()
        p.moveTo(ox + w + 10, oy)
        p.lineTo(ox + w + 4, oy + 2.2)
        p.lineTo(ox + w + 4, oy - 2.2)
        p.close()
        c.drawPath(p, stroke=0, fill=1)
        p = c.beginPath()
        p.moveTo(ox, oy + h + 10)
        p.lineTo(ox + 2.2, oy + h + 4)
        p.lineTo(ox - 2.2, oy + h + 4)
        p.close()
        c.drawPath(p, stroke=0, fill=1)

        c.setFillColor(MUTED)
        c.setFont("BVP", 6.6)
        c.drawString(ox + w - 4, oy - 11, self.xlabel)
        c.drawString(ox - 26, oy + h + 2, self.ylabel)
        c.drawString(ox - 9, oy - 9, "O")

        # guides
        c.setStrokeColor(colors.HexColor("#DCE1EE"))
        c.setDash(2, 2)
        c.setLineWidth(0.6)
        for (x1, y1, x2, y2) in self.guides:
            c.line(X(x1), Y(y1), X(x2), Y(y2))
        c.setDash()

        for s in self.series:
            c.setStrokeColor(s.get("color", self.color))
            c.setLineWidth(s.get("lw", 1.9))
            if s.get("dash"):
                c.setDash(3, 2)
            pts = s["pts"]
            p = c.beginPath()
            p.moveTo(X(pts[0][0]), Y(pts[0][1]))
            for (x, y) in pts[1:]:
                p.lineTo(X(x), Y(y))
            c.drawPath(p, stroke=1, fill=0)
            c.setDash()
            # markers
            c.setFillColor(s.get("color", self.color))
            for (x, y) in pts:
                c.circle(X(x), Y(y), 1.9, stroke=0, fill=1)

        for (x, y, txt) in self.marks:
            c.setFillColor(INK)
            c.setFont("BVP-SB", 6.4)
            c.drawString(X(x) + 3, Y(y) + 3, txt)

        if self.caption:
            c.setFillColor(MUTED)
            c.setFont("BVP-It", 6.8)
            c.drawCentredString(self.width / 2, 2, self.caption)
