# -*- coding: utf-8 -*-
"""Style kit cho đề cương PDF (ReportLab)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle, KeepTogether,
                                PageBreak, Flowable, CondPageBreak)
from reportlab.graphics.shapes import Drawing, Line, String, Polygon, PolyLine, Rect
from reportlab.platypus.tableofcontents import TableOfContents

# ----------------------------------------------------------------- fonts
F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DJSerif", F + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DJSerif-Bold", F + "DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJSans", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJSans-Bold", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJMono", F + "DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DJMono-Bold", F + "DejaVuSansMono-Bold.ttf"))
pdfmetrics.registerFontFamily("DJSerif", normal="DJSerif", bold="DJSerif-Bold",
                              italic="DJSerif", boldItalic="DJSerif-Bold")
pdfmetrics.registerFontFamily("DJSans", normal="DJSans", bold="DJSans-Bold",
                              italic="DJSans", boldItalic="DJSans-Bold")

# ----------------------------------------------------------------- palette
NAVY   = colors.HexColor("#1B3A5C")
NAVY_D = colors.HexColor("#12283F")
TEAL   = colors.HexColor("#0F6E6E")
AMBER  = colors.HexColor("#C97B14")
AMBER_L= colors.HexColor("#FDF3E3")
RED    = colors.HexColor("#A32B2B")
RED_L  = colors.HexColor("#FBEDED")
GREEN  = colors.HexColor("#276749")
GREEN_L= colors.HexColor("#EDF7F0")
BLUE_L = colors.HexColor("#EDF3FA")
GREY_L = colors.HexColor("#F3F5F8")
GREY   = colors.HexColor("#8A94A2")
LINE   = colors.HexColor("#C9D3DE")
WHITE  = colors.white
INK    = colors.HexColor("#1D2430")

PAGE_W, PAGE_H = A4
LM = RM = 15.5 * mm
TM = 19 * mm
BM = 17 * mm
CONTENT_W = PAGE_W - LM - RM

# ----------------------------------------------------------------- styles
def st(name, **kw):
    base = dict(fontName="DJSerif", fontSize=9.4, leading=13.6, textColor=INK,
                spaceBefore=0, spaceAfter=0, alignment=TA_JUSTIFY)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {}
S["body"]   = st("body", spaceAfter=3.4)
S["body_c"] = st("body_c", alignment=TA_CENTER)
S["lead"]   = st("lead", fontSize=10.2, leading=15.4, textColor=NAVY_D)
S["small"]  = st("small", fontSize=8.2, leading=11.4, textColor=colors.HexColor("#44505F"))
S["tiny"]   = st("tiny", fontSize=7.4, leading=10)
S["h1"]     = st("h1", fontName="DJSans-Bold", fontSize=15.5, leading=20,
                 textColor=WHITE, backColor=NAVY, alignment=TA_LEFT,
                 borderPadding=(7, 9, 6, 9), spaceBefore=6, spaceAfter=11)
S["h1b"]    = st("h1b", fontName="DJSans-Bold", fontSize=13.5, leading=18,
                 textColor=WHITE, backColor=TEAL, alignment=TA_LEFT,
                 borderPadding=(6, 9, 5, 9), spaceBefore=8, spaceAfter=9)
S["h2"]     = st("h2", fontName="DJSans-Bold", fontSize=11.6, leading=15,
                 textColor=NAVY, spaceBefore=9, spaceAfter=4, alignment=TA_LEFT)
S["h3"]     = st("h3", fontName="DJSans-Bold", fontSize=9.9, leading=13.4,
                 textColor=TEAL, spaceBefore=6, spaceAfter=2.5, alignment=TA_LEFT)
S["bullet"] = st("bullet", leftIndent=11, bulletIndent=2, spaceAfter=1.8,
                 bulletFontName="DJSans", bulletFontSize=8)
S["num"]    = st("num", leftIndent=15, bulletIndent=2, spaceAfter=1.8)
S["formula"]= st("formula", fontName="DJSerif-Bold", fontSize=10.6, leading=15,
                 alignment=TA_CENTER, textColor=NAVY_D)
S["box_t"]  = st("box_t", fontName="DJSans-Bold", fontSize=8.5, leading=11,
                 textColor=WHITE, alignment=TA_LEFT)
S["box_b"]  = st("box_b", fontSize=9.0, leading=12.8, alignment=TA_LEFT)
S["tbl"]    = st("tbl", fontSize=8.3, leading=11.2, alignment=TA_LEFT)
S["tbl_c"]  = st("tbl_c", fontSize=8.3, leading=11.2, alignment=TA_CENTER)
S["tbl_h"]  = st("tbl_h", fontName="DJSans-Bold", fontSize=8.4, leading=11,
                 textColor=WHITE, alignment=TA_CENTER)
S["tbl_s"]  = st("tbl_s", fontSize=7.6, leading=10.2, alignment=TA_LEFT)
S["q"]      = st("q", fontSize=9.4, leading=13.2, alignment=TA_JUSTIFY,
                 spaceBefore=5, spaceAfter=1.5, leftIndent=0)
S["opt"]    = st("opt", fontSize=9.1, leading=12.5, alignment=TA_LEFT,
                 leftIndent=14, spaceAfter=0.3)
S["ans"]    = st("ans", fontSize=9.0, leading=12.6, alignment=TA_JUSTIFY,
                 textColor=colors.HexColor("#0B3D2E"))
S["toc0"]   = st("toc0", fontName="DJSans-Bold", fontSize=10.2, leading=15.5,
                 textColor=NAVY, spaceBefore=5)
S["toc1"]   = st("toc1", fontSize=9.0, leading=13.2, leftIndent=14, textColor=INK)
S["toc2"]   = st("toc2", fontSize=8.6, leading=12.4, leftIndent=28,
                 textColor=colors.HexColor("#44505F"))


# ----------------------------------------------------------------- helpers
def P(text, style="body"):
    return Paragraph(text, S[style] if isinstance(style, str) else style)


def H1(text, toc=True):
    p = Paragraph(text, S["h1"])
    p._toc = (0, text) if toc else None
    return p


def H1B(text, toc=True):
    p = Paragraph(text, S["h1b"])
    p._toc = (1, text) if toc else None
    return p


def H2(text, toc=True):
    p = Paragraph(text, S["h2"])
    if toc:
        p._toc = (1, text)
    return p


def H3(text):
    return Paragraph(text, S["h3"])


def BULL(items, style="bullet", bullet="•"):
    out = []
    for it in items:
        out.append(Paragraph(it, S[style], bulletText=bullet))
    return out


def SP(h=4):
    return Spacer(1, h)


def hr(color=LINE, thickness=0.7, space_before=4, space_after=4):
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[0.1])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), thickness, color)]))
    return [Spacer(1, space_before), t, Spacer(1, space_after)]


def _keep_spaces(t):
    import re as _re
    return _re.sub(r" {2,}", lambda m: "&nbsp;" * len(m.group(0)), t)


def formula(expr, note=None):
    """Hộp công thức nổi bật."""
    expr = _keep_spaces(expr)
    inner = [[Paragraph(expr, S["formula"])]]
    if note:
        inner.append([Paragraph(note, st("fn", fontSize=8.1, leading=11,
                                         alignment=TA_CENTER,
                                         textColor=colors.HexColor("#44505F")))] )
    t = Table(inner, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_L),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return [Spacer(1, 2), t, Spacer(1, 5)]


_THEMES = {
    "meo":    ("MẸO NHỚ", AMBER, AMBER_L),
    "bay":    ("BẪY ĐỀ", RED, RED_L),
    "nho":    ("GHI NHỚ", GREEN, GREEN_L),
    "vd":     ("VÍ DỤ MẪU", TEAL, BLUE_L),
    "thi":    ("LƯU Ý KHI THI", NAVY, GREY_L),
}


def box(text, theme="nho", title=None, width=None):
    """Hộp ghi chú có tiêu đề màu."""
    label, c_main, c_bg = _THEMES[theme]
    label = title or label
    head = Table([[Paragraph(label, S["box_t"])]], colWidths=[width or CONTENT_W])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), c_main),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    body = Table([[Paragraph(text, S["box_b"])]], colWidths=[width or CONTENT_W])
    body.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), c_bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [Spacer(1, 3), KeepTogether([head, body]), Spacer(1, 5)]


def table(rows, widths, header=True, align=None, zebra=True, font=8.3,
          small=False, hdr_bg=NAVY, first_col_bold=False, pad=3.2, valign="TOP"):
    """rows: list of list (str hoặc flowable)."""
    key = "tbl_s" if small else "tbl"
    data = []
    for ri, row in enumerate(rows):
        out = []
        for ci, cell in enumerate(row):
            if isinstance(cell, Flowable):
                out.append(cell)
                continue
            if header and ri == 0:
                style = S["tbl_h"]
            elif align and ci < len(align) and align[ci] == "c":
                style = S["tbl_c"]
            else:
                style = S[key]
            style = ParagraphStyle("t%d%d" % (ri, ci), parent=style, fontSize=font,
                                   leading=font * 1.34) if font != style.fontSize else style
            txt = str(cell).replace("\n", "<br/>")
            if first_col_bold and ci == 0 and not (header and ri == 0):
                txt = "<b>%s</b>" % txt
            out.append(Paragraph(txt, style))
        data.append(out)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), valign),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("TOPPADDING", (0, 0), (-1, -1), pad),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), hdr_bg),
                 ("VALIGN", (0, 0), (-1, 0), "MIDDLE")]
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(data)):
            if (i - start) % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), GREY_L))
    t.setStyle(TableStyle(cmds))
    return t


def question(num, text, opts=None, sub=None):
    """Câu trắc nghiệm: số câu + nội dung + 4 phương án."""
    out = [Paragraph("<b>Câu %s.</b> %s" % (num, text), S["q"])]
    if opts:
        for lab, o in zip("ABCD", opts):
            out.append(Paragraph("<b>%s.</b> %s" % (lab, o), S["opt"]))
    if sub:
        out.extend([Paragraph(x, S["opt"]) for x in sub])
    out.append(Spacer(1, 2))
    return out


def answer_line(text):
    return Paragraph(text, S["ans"])


def kv_row(k, v):
    return [k, v]


# ----------------------------------------------------------------- figures
def _axes(d, x0, y0, w, h, xlab, ylab, xmax, ymax, xticks, yticks, ylab_dx=0, ylab_dy=6):
    ax = Line(x0, y0, x0 + w, y0, strokeColor=INK, strokeWidth=0.9)
    ay = Line(x0, y0, x0, y0 + h, strokeColor=INK, strokeWidth=0.9)
    d.add(ax); d.add(ay)
    d.add(Polygon([x0 + w, y0, x0 + w - 6, y0 + 3, x0 + w - 6, y0 - 3],
                  fillColor=INK, strokeColor=INK))
    d.add(Polygon([x0, y0 + h, x0 - 3, y0 + h - 6, x0 + 3, y0 + h - 6],
                  fillColor=INK, strokeColor=INK))
    d.add(String(x0 + w + 2, y0 - 26, xlab, fontName="DJSerif", fontSize=8.5,
                 fillColor=INK, textAnchor="end"))
    d.add(String(x0 + ylab_dx - 4, y0 + h + ylab_dy, ylab, fontName="DJSerif",
                 fontSize=8.5, fillColor=INK))
    for t in xticks:
        px = x0 + w * t[0] / xmax
        d.add(Line(px, y0, px, y0 - 3, strokeColor=INK, strokeWidth=0.7))
        d.add(String(px, y0 - 12, t[1], fontName="DJSerif", fontSize=7.2,
                     fillColor=INK, textAnchor="middle"))
    for t in yticks:
        py = y0 + h * t[0] / ymax
        d.add(Line(x0, py, x0 - 3, py, strokeColor=INK, strokeWidth=0.7))
        d.add(String(x0 - 5, py - 2.5, t[1], fontName="DJSerif", fontSize=7.2,
                     fillColor=INK, textAnchor="end"))


def fig_st():
    """Đồ thị độ dịch chuyển – thời gian minh hoạ 3 giai đoạn."""
    W, H = CONTENT_W, 168
    d = Drawing(W, H)
    x0, y0, w, h = 40, 32, W - 90, H - 62
    _axes(d, x0, y0, w, h, "t (s)", "x (m)", 10, 12,
          [(0, "O"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
          [(0, "0"), (4, "4"), (8, "8"), (12, "12")], ylab_dx=16, ylab_dy=-4)
    pts = [(0, 0), (4, 8), (6, 8), (10, 0)]
    xy = []
    for (t, x) in pts:
        xy += [x0 + w * t / 10.0, y0 + h * x / 12.0]
    d.add(PolyLine(xy, strokeColor=NAVY, strokeWidth=1.9))
    for (t, x) in pts:
        cx, cy = x0 + w * t / 10.0, y0 + h * x / 12.0
        d.add(Polygon([cx, cy + 2.6, cx + 2.6, cy, cx, cy - 2.6, cx - 2.6, cy],
                      fillColor=NAVY, strokeColor=NAVY))
    notes = [("(1) đi đều, v > 0", 4.15, 8.9, "start"),
             ("(2) đứng yên", 6.05, 10.4, "middle"),
             ("(3) đi ngược chiều, v < 0", 6.55, 1.2, "start")]
    for txt, tx, ty, anc in notes:
        d.add(String(x0 + w * tx / 10.0, y0 + h * ty / 12.0, txt, fontName="DJSerif",
                     fontSize=7.4, fillColor=TEAL, textAnchor=anc))
    return d


def fig_vt():
    """Đồ thị vận tốc – thời gian (nhanh dần đều) + diện tích."""
    W, H = CONTENT_W, 158
    d = Drawing(W, H)
    x0, y0, w, h = 44, 30, W - 96, H - 58
    _axes(d, x0, y0, w, h, "t (s)", "v (m/s)", 10, 20,
          [(0, "O"), (5, "5"), (10, "10")],
          [(0, "0"), (10, "10"), (20, "20")], ylab_dx=22, ylab_dy=-4)
    v0, a = 4.0, 1.6
    p0 = (x0, y0 + h * v0 / 20.0)
    p1 = (x0 + w, y0 + h * (v0 + a * 10) / 20.0)
    d.add(Polygon([x0, y0] + [p0[0], p0[1], p1[0], p1[1], p1[0], y0],
                  fillColor=colors.HexColor("#E7EFF7"), strokeColor=None))
    d.add(Line(p0[0], p0[1], p1[0], p1[1], strokeColor=NAVY, strokeWidth=1.8))
    d.add(Line(p0[0], p0[1], p0[0], y0, strokeColor=NAVY, strokeWidth=0.8,
               strokeDashArray=[2, 2]))
    d.add(String(p0[0] - 4, p0[1] - 2.5, "v₀", fontName="DJSerif", fontSize=8,
                 fillColor=NAVY, textAnchor="end"))
    d.add(String(x0 + w * 0.36, y0 + h * 0.30, "Diện tích = độ dịch chuyển d",
                 fontName="DJSerif", fontSize=7.8, fillColor=TEAL))
    return d


def fig_safety():
    """Bảng ký hiệu biển báo vẽ bằng hình học."""
    W, H = CONTENT_W, 86
    d = Drawing(W, H)
    specs = [
        ("CẤM", "circle", RED),
        ("CẢNH BÁO", "tri", AMBER),
        ("BẮT BUỘC", "bfill", TEAL),
        ("CHỈ DẪN", "square", colors.HexColor("#1F6FB2")),
    ]
    step = W / 4.0
    for i, (lab, shape, col) in enumerate(specs):
        cx = step * i + step / 2 - 10
        cy = H / 2 + 8
        if shape == "circle":
            d.add(Polygon([cx + 20, cy + 0, cx + 20, cy + 0], fillColor=None,
                          strokeColor=None))  # placeholder
            d.add(Line(cx, cy, cx + 40, cy, strokeColor=col, strokeWidth=0))
            from reportlab.graphics.shapes import Circle
            d.add(Circle(cx + 20, cy, 17, fillColor=WHITE, strokeColor=col,
                         strokeWidth=2.2))
            d.add(Line(cx + 8, cy - 12, cx + 32, cy + 12, strokeColor=col,
                       strokeWidth=2.2))
        elif shape == "tri":
            d.add(Polygon([cx + 20, cy + 17, cx + 3, cy - 12, cx + 37, cy - 12],
                          fillColor=colors.HexColor("#FBE7A2"), strokeColor=col,
                          strokeWidth=2.0))
            d.add(String(cx + 20, cy - 8, "!", fontName="DJSans-Bold", fontSize=11,
                         fillColor=INK, textAnchor="middle"))
        elif shape == "bfill":
            from reportlab.graphics.shapes import Circle
            d.add(Circle(cx + 20, cy, 17, fillColor=col, strokeColor=col,
                         strokeWidth=1))
            d.add(String(cx + 20, cy - 4, "i", fontName="DJSans-Bold", fontSize=12,
                         fillColor=WHITE, textAnchor="middle"))
        else:
            d.add(Rect(cx + 3, cy - 13, 34, 26, fillColor=col, strokeColor=col))
            d.add(String(cx + 20, cy - 4, "→", fontName="DJSans-Bold", fontSize=12,
                         fillColor=WHITE, textAnchor="middle"))
        d.add(String(cx + 20, cy - 34, lab, fontName="DJSans-Bold", fontSize=7.6,
                     fillColor=INK, textAnchor="middle"))
    return d
