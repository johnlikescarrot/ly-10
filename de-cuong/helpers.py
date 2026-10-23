# -*- coding: utf-8 -*-
"""Helpers dùng chung để dựng PDF đề cương (ReportLab Platypus)."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, HRFlowable, PageBreak)
from reportlab.graphics.shapes import Drawing, Line, String, Polygon, Rect, Circle
from reportlab.lib.colors import HexColor

# ---------------------------------------------------------------- fonts
_FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Sans", os.path.join(_FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Sans-Bold", os.path.join(_FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("SansMono", os.path.join(_FONT_DIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFont(TTFont("Serif", os.path.join(_FONT_DIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Bold", os.path.join(_FONT_DIR, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif", boldItalic="Serif-Bold")

# ---------------------------------------------------------------- colours
NAVY = HexColor("#16365C")
NAVY2 = HexColor("#1F4E79")
TEAL = HexColor("#0E7C7B")
TEAL_D = HexColor("#0A5E5D")
ORANGE = HexColor("#D96C27")
GREEN = HexColor("#2E7D32")
RED = HexColor("#B03A2E")
PURPLE = HexColor("#5B4CAD")
GREY_D = HexColor("#333333")
GREY_M = HexColor("#6B7280")
BG = HexColor("#EEF3F8")
BG_TEAL = HexColor("#E6F2F2")
BG_ORANGE = HexColor("#FDF0E4")
BG_GREEN = HexColor("#EAF4EA")
BG_RED = HexColor("#FBEAEA")
BG_PURPLE = HexColor("#EFEDF8")
BG_YELLOW = HexColor("#FFF7DB")
LINE = HexColor("#C9D4E0")

PAGE_W, PAGE_H = A4

# ---------------------------------------------------------------- styles
S = {}
S["Body"] = ParagraphStyle("Body", fontName="Serif", fontSize=9.6, leading=14.2,
                           alignment=TA_JUSTIFY, textColor=GREY_D, spaceAfter=5)
S["BodySmall"] = ParagraphStyle("BodySmall", parent=S["Body"], fontSize=8.8, leading=12.8)
S["Bullet"] = ParagraphStyle("Bullet", parent=S["Body"], leftIndent=13, firstLineIndent=0,
                             bulletIndent=5, spaceAfter=3, alignment=TA_LEFT)
S["H1"] = ParagraphStyle("H1", fontName="Sans-Bold", fontSize=16, leading=20,
                         textColor=NAVY, spaceBefore=14, spaceAfter=8, keepWithNext=1)
S["H2"] = ParagraphStyle("H2", fontName="Sans-Bold", fontSize=12.2, leading=15.5,
                         textColor=NAVY2, spaceBefore=11, spaceAfter=5, keepWithNext=1)
S["H3"] = ParagraphStyle("H3", fontName="Sans-Bold", fontSize=10.4, leading=13.5,
                         textColor=TEAL_D, spaceBefore=8, spaceAfter=4, keepWithNext=1)
S["Caption"] = ParagraphStyle("Caption", fontName="Sans", fontSize=7.8, leading=10.5,
                              textColor=GREY_M, alignment=TA_CENTER, spaceBefore=2, spaceAfter=7)
S["Cell"] = ParagraphStyle("Cell", fontName="Sans", fontSize=8.2, leading=11,
                           textColor=GREY_D, alignment=TA_LEFT)
S["CellC"] = ParagraphStyle("CellC", parent=S["Cell"], alignment=TA_CENTER)
S["CellH"] = ParagraphStyle("CellH", fontName="Sans-Bold", fontSize=8.2, leading=11,
                            textColor=colors.white, alignment=TA_CENTER)
S["Q"] = ParagraphStyle("Q", parent=S["Body"], fontName="Serif", alignment=TA_LEFT, spaceAfter=3)
S["Opt"] = ParagraphStyle("Opt", parent=S["Body"], fontName="Serif", fontSize=9.3, leading=13,
                          alignment=TA_LEFT, leftIndent=14, spaceAfter=2)
S["Ans"] = ParagraphStyle("Ans", fontName="Sans", fontSize=8.9, leading=13.2, textColor=GREY_D, alignment=TA_LEFT, spaceAfter=3)
S["Formula"] = ParagraphStyle("Formula", fontName="Serif-Bold", fontSize=10.6, leading=15,
                              textColor=NAVY, alignment=TA_CENTER, spaceAfter=2)
S["TOCItem"] = ParagraphStyle("TOCItem", fontName="Sans", fontSize=9.5, leading=14, textColor=NAVY)


def P(text, style="Body"):
    return Paragraph(text, S[style])


def h1(text):
    return Paragraph(text, S["H1"])


def h2(text):
    return Paragraph(text, S["H2"])


def h3(text):
    return Paragraph(text, S["H3"])


def bullets(items, style="Bullet"):
    return [Paragraph(t, S[style], bulletText="\u2022") for t in items]


def numbered(items, style="Bullet"):
    out = []
    for i, t in enumerate(items, 1):
        out.append(Paragraph(t, S[style], bulletText=f"{i}."))
    return out


def sp(h=4):
    return Spacer(1, h)


def hr():
    return HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=4, spaceAfter=7)


def callout(title, body_items, bg=BG, accent=NAVY, title_color=None):
    """Hộp nhấn mạnh: tiêu đề + các đoạn/danh sách. body_items: list[str|Flowable]."""
    inner = [Paragraph(f"<b>{title}</b>", ParagraphStyle(
        "ct", fontName="Sans-Bold", fontSize=9.4, leading=12.5,
        textColor=title_color or accent, spaceAfter=4))]
    for it in body_items:
        if isinstance(it, str):
            inner.append(Paragraph(it, S["Ans"]))
        else:
            inner.append(it)
    t = Table([[inner]], colWidths=[PAGE_W - 34 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.7, accent),
        ("LINEBELOW", (0, 0), (-1, 0), 0, bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    return t


def formula(text, note=None):
    items = [Paragraph(text, S["Formula"])]
    if note:
        items.append(Paragraph(note, ParagraphStyle(
            "fn", fontName="Sans", fontSize=7.9, leading=10.5, textColor=GREY_M, alignment=TA_CENTER)))
    t = Table([[items]], colWidths=[PAGE_W - 34 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_YELLOW),
        ("BOX", (0, 0), (-1, -1), 0.7, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    return t


def styled_table(data, col_widths, header=True, align_center_cols=None, fontsize=8.2):
    """data: list of rows of str (đã có markup). Tự bọc Paragraph."""
    align_center_cols = set(align_center_cols or [])
    rows = []
    for r, row in enumerate(data):
        out_row = []
        for c, cell in enumerate(row):
            if isinstance(cell, str):
                if r == 0 and header:
                    sty = S["CellH"]
                elif c in align_center_cols:
                    sty = S["CellC"]
                else:
                    sty = S["Cell"]
                out_row.append(Paragraph(cell, sty))
            else:
                out_row.append(cell)
        rows.append(out_row)
    t = Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), NAVY),
                  ("TEXTCOLOR", (0, 0), (-1, 0), colors.white)]
        for r in range(1, len(rows)):
            if r % 2 == 0:
                style.append(("BACKGROUND", (0, r), (-1, r), BG))
    t.setStyle(TableStyle(style))
    return t


def tag(unit, level):
    return (f"<font name=\"Sans\" size=\"7.2\" color=\"#0A5E5D\">[{unit} \u00b7 {level}]</font>")


def question(num, stem, options=None, unit="", level=""):
    """Câu trắc nghiệm 4 lựa chọn."""
    head = f"<b>Câu {num}.</b> {(' ' + tag(unit, level)) if unit else ''} {stem}"
    items = [Paragraph(head, S["Q"])]
    if options:
        for letter, opt in zip("ABCD", options):
            items.append(Paragraph(f"<b>{letter}.</b> {opt}", S["Opt"]))
    return KeepTogether(items)


def tf_question(num, stem, statements, unit=""):
    head = f"<b>Câu {num}.</b> {(' ' + tag(unit, 'Đúng/Sai')) if unit else ''} {stem}"
    items = [Paragraph(head, S["Q"])]
    for letter, st in zip("abcd", statements):
        items.append(Paragraph(f"<b>{letter})</b> {st}", S["Opt"]))
    return KeepTogether(items)


def answer_block(answer, explanation):
    return callout(f"\u0110áp án: {answer}", [explanation], bg=BG_GREEN, accent=GREEN)


# ---------------------------------------------------------------- drawings
def _axes(d, x0, y0, w, h, xlabel, ylabel, xmax_label="", ymax_label=""):
    d.add(Line(x0, y0, x0 + w, y0, strokeColor=GREY_D, strokeWidth=0.9))
    d.add(Line(x0, y0, x0, y0 + h, strokeColor=GREY_D, strokeWidth=0.9))
    # arrow heads
    d.add(Polygon([x0 + w, y0, x0 + w - 5, y0 - 2.2, x0 + w - 5, y0 + 2.2], fillColor=GREY_D, strokeColor=GREY_D))
    d.add(Polygon([x0, y0 + h, x0 - 2.2, y0 + h - 5, x0 + 2.2, y0 + h - 5], fillColor=GREY_D, strokeColor=GREY_D))
    d.add(String(x0 + w - 8, y0 - 13, xlabel, fontName="Sans", fontSize=7.5, fillColor=GREY_D))
    d.add(String(x0 + 4, y0 + h - 3, ylabel, fontName="Sans", fontSize=7.5, fillColor=GREY_D))
    d.add(String(x0 - 9, y0 - 5, "O", fontName="Sans", fontSize=7, fillColor=GREY_D))
    if xmax_label:
        d.add(String(x0 + w - 12, y0 + 4, xmax_label, fontName="Sans", fontSize=6.8, fillColor=GREY_M))
    if ymax_label:
        d.add(String(x0 - 20, y0 + h - 12, ymax_label, fontName="Sans", fontSize=6.8, fillColor=GREY_M))


def make_dt_graph(points, xlabel="t (s)", ylabel="d (m)", w=250, h=150,
                  x_ticks=None, y_ticks=None, dashed_to_axes=True):
    """Đồ thị độ dịch chuyển - thời gian dạng gấp khúc qua các điểm (x,y) đã chuẩn hoá."""
    d = Drawing(w, h)
    x0, y0, gw, gh = 42, 26, w - 68, h - 48
    xs = [p[0] for p in points] + [0]
    ys = [p[1] for p in points] + [0]
    xmax, ymax = max(xs) * 1.12, max(ys) * 1.18
    def X(v): return x0 + gw * v / xmax
    def Y(v): return y0 + gh * v / ymax
    _axes(d, x0, y0, gw, gh, xlabel, ylabel)
    # grid nhẹ tại ticks
    for xv, lab in (x_ticks or []):
        d.add(Line(X(xv), y0, X(xv), Y(points[-1][1]) if False else y0 + gh, strokeColor=HexColor("#E5EBF1"), strokeWidth=0.4))
        d.add(String(X(xv) - 4, y0 - 12, str(lab), fontName="Sans", fontSize=6.8, fillColor=GREY_M))
        d.add(Line(X(xv), y0 - 2, X(xv), y0 + 2, strokeColor=GREY_D, strokeWidth=0.6))
    for yv, lab in (y_ticks or []):
        d.add(Line(x0, Y(yv), x0 + gw, Y(yv), strokeColor=HexColor("#E5EBF1"), strokeWidth=0.4))
        d.add(String(x0 - 22, Y(yv) - 3, str(lab), fontName="Sans", fontSize=6.8, fillColor=GREY_M))
        d.add(Line(x0 - 2, Y(yv), x0 + 2, Y(yv), strokeColor=GREY_D, strokeWidth=0.6))
    for i in range(len(points) - 1):
        d.add(Line(X(points[i][0]), Y(points[i][1]), X(points[i + 1][0]), Y(points[i + 1][1]),
                   strokeColor=NAVY2, strokeWidth=1.8))
    for (xv, yv) in points:
        d.add(Circle(X(xv), Y(yv), 2.4, fillColor=ORANGE, strokeColor=ORANGE))
    if dashed_to_axes and len(points) >= 2:
        lx, ly = points[-1]
        if ly > 0:
            d.add(Line(X(lx), Y(ly), X(lx), y0, strokeColor=ORANGE, strokeWidth=0.6))
    return d


def make_vt_graph(v0, v1, tmax, xlabel="t (s)", ylabel="v (m/s)", w=250, h=150, shade=True):
    d = Drawing(w, h)
    x0, y0, gw, gh = 42, 26, w - 68, h - 48
    ymax = max(v0, v1) * 1.25
    def X(v): return x0 + gw * v / (tmax * 1.1)
    def Y(v): return y0 + gh * v / ymax
    _axes(d, x0, y0, gw, gh, xlabel, ylabel)
    if shade:
        d.add(Polygon([X(0), y0, X(tmax), y0, X(tmax), Y(v1), X(0), Y(v0)],
                      fillColor=HexColor("#DCE9F5"), strokeColor=None))
    d.add(Line(X(0), Y(v0), X(tmax), Y(v1), strokeColor=NAVY2, strokeWidth=1.8))
    d.add(Circle(X(0), Y(v0), 2.4, fillColor=ORANGE, strokeColor=ORANGE))
    d.add(Circle(X(tmax), Y(v1), 2.4, fillColor=ORANGE, strokeColor=ORANGE))
    d.add(String(X(tmax) - 5, y0 - 12, f"{tmax:g}", fontName="Sans", fontSize=6.8, fillColor=GREY_M))
    d.add(String(x0 - 24, Y(v0) - 3, f"{v0:g}", fontName="Sans", fontSize=6.8, fillColor=GREY_M))
    if v1 != v0:
        d.add(String(x0 - 24, Y(v1) - 3, f"{v1:g}", fontName="Sans", fontSize=6.8, fillColor=GREY_M))
    d.add(String(x0 + gw * 0.32, y0 + gh * 0.28, "diện tích = độ dịch chuyển",
                 fontName="Sans", fontSize=6.6, fillColor=NAVY2))
    return d


def make_vector_diagram(w=250, h=150):
    """Sơ đồ cộng hai vận tốc vuông góc 3-4-5."""
    d = Drawing(w, h)
    ox, oy = 48, 32
    sx, sy = 34, 26  # tỉ lệ: 3 -> đông (x), 4 -> bắc (y) thu nhỏ
    ex, ny = 3 * sx, 4 * sy
    d.add(Line(ox, oy, ox + 170, oy, strokeColor=GREY_M, strokeWidth=0.6))
    d.add(Line(ox, oy, ox, oy + 118, strokeColor=GREY_M, strokeWidth=0.6))
    d.add(String(ox + 158, oy - 13, "Đông", fontName="Sans", fontSize=7, fillColor=GREY_M))
    d.add(String(ox + 5, oy + 108, "Bắc", fontName="Sans", fontSize=7, fillColor=GREY_M))
    # v nuoc (dong)
    d.add(Line(ox, oy, ox + ex, oy, strokeColor=TEAL, strokeWidth=2))
    d.add(Polygon([ox + ex, oy, ox + ex - 6, oy - 2.5, ox + ex - 6, oy + 2.5], fillColor=TEAL, strokeColor=TEAL))
    d.add(String(ox + ex / 2 - 16, oy - 14, "v(nước/bờ) = 3", fontName="Sans", fontSize=7, fillColor=TEAL_D))
    # v thuyen/nuoc (bac) tu dau mui vecto nuoc
    d.add(Line(ox + ex, oy, ox + ex, oy + ny, strokeColor=ORANGE, strokeWidth=2))
    d.add(Polygon([ox + ex, oy + ny, ox + ex - 2.5, oy + ny - 6, ox + ex + 2.5, oy + ny - 6], fillColor=ORANGE, strokeColor=ORANGE))
    d.add(String(ox + ex + 7, oy + ny / 2, "v(thuyền/nước) = 4", fontName="Sans", fontSize=7, fillColor=ORANGE))
    # v tong
    d.add(Line(ox, oy, ox + ex, oy + ny, strokeColor=NAVY, strokeWidth=2.2))
    d.add(Polygon([ox + ex, oy + ny, ox + ex - 8, oy + ny - 3, ox + ex - 2, oy + ny - 9], fillColor=NAVY, strokeColor=NAVY))
    d.add(String(ox + ex / 2 - 34, oy + ny / 2 + 8, "v(thuyền/bờ) = 5", fontName="Sans-Bold", fontSize=7.5, fillColor=NAVY))
    return d


def make_path_diagram(w=250, h=150):
    """Sơ đồ quãng đường (gấp khúc) vs độ dịch chuyển (đường thẳng) 30-40-50."""
    d = Drawing(w, h)
    ox, oy = 40, 30
    ex, ny = 110, 82
    d.add(Circle(ox, oy, 3, fillColor=NAVY, strokeColor=NAVY))
    d.add(String(ox - 14, oy - 13, "Nhà", fontName="Sans", fontSize=7.5, fillColor=NAVY))
    d.add(Line(ox, oy, ox + ex, oy, strokeColor=TEAL, strokeWidth=2))
    d.add(String(ox + ex / 2 - 22, oy - 13, "30 m (Đông)", fontName="Sans", fontSize=7, fillColor=TEAL_D))
    d.add(Line(ox + ex, oy, ox + ex, oy + ny, strokeColor=ORANGE, strokeWidth=2))
    d.add(String(ox + ex + 7, oy + ny / 2, "40 m (Bắc)", fontName="Sans", fontSize=7, fillColor=ORANGE))
    d.add(Circle(ox + ex, oy + ny, 3, fillColor=NAVY, strokeColor=NAVY))
    d.add(String(ox + ex - 8, oy + ny + 8, "Trường", fontName="Sans", fontSize=7.5, fillColor=NAVY))
    d.add(Line(ox, oy, ox + ex, oy + ny, strokeColor=NAVY, strokeWidth=1.6))
    # đứt đoạn mô phỏng vecto
    d.add(String(ox + 18, oy + 44, "độ dịch chuyển 50 m", fontName="Sans-Bold", fontSize=7.5, fillColor=NAVY))
    d.add(String(ox + 18, oy + 33, "quãng đường 70 m", fontName="Sans", fontSize=7, fillColor=GREY_D))
    return d
