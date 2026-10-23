# -*- coding: utf-8 -*-
"""Khung dựng tài liệu PDF (ReportLab) cho đề cương ôn tập Vật lí 10."""

import os
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether,
                                PageBreak, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

# --------------------------------------------------------------------------
# Font
# --------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("VNSans", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("VNSans-Bold", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("VNSerif", os.path.join(FONT_DIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("VNSerif-Bold", os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")))
from reportlab.pdfbase.pdfmetrics import registerFontFamily

registerFontFamily("VNSans", normal="VNSans", bold="VNSans-Bold",
                   italic="VNSans", boldItalic="VNSans-Bold")

# --------------------------------------------------------------------------
# Bảng màu
# --------------------------------------------------------------------------
NAVY = colors.HexColor("#15315B")
NAVY_L = colors.HexColor("#2B4F86")
BLUE = colors.HexColor("#1F5FA8")
BLUE_BG = colors.HexColor("#EBF2FB")
TEAL = colors.HexColor("#0E7C86")
TEAL_BG = colors.HexColor("#E6F4F5")
GREEN = colors.HexColor("#1E8449")
GREEN_BG = colors.HexColor("#EAF6EE")
AMBER = colors.HexColor("#B9770E")
AMBER_BG = colors.HexColor("#FEF6E4")
RED = colors.HexColor("#B03A2E")
RED_BG = colors.HexColor("#FBEDEB")
GRAY = colors.HexColor("#5F6B7A")
GRAY_BG = colors.HexColor("#F1F3F6")
INK = colors.HexColor("#1C2430")
LINE = colors.HexColor("#D5DCE5")
SOFT = colors.HexColor("#F7F9FC")

PAGE_W, PAGE_H = A4
LM, RM = 1.9 * cm, 1.9 * cm
TM, BM = 2.15 * cm, 1.95 * cm


SUB = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
    "n": "ₙ", "x": "ₓ", "i": "ᵢ", "a": "ₐ", "v": "ᵥ", "u": "ᵤ", "t": "t", "0dc": "₀",
}
SUP = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "n": "ⁿ",
}


def _sub_token(tok):
    if tok.lower() == "dc":
        return "(dc)"
    out = []
    for ch in tok:
        out.append(SUB.get(ch, ch))
    return "".join(out)


def _sup_token(tok):
    return "".join(SUP.get(ch, ch) for ch in tok)


def F(s):
    """Chuyển 'v_0 t + ½at^2' thành ký hiệu Unicode (₀, ², …)."""
    s = s.replace("_{dc}", "(dc)").replace("_dc", "(dc)")
    s = re.sub(r"\^\{([^}]*)\}", lambda m: _sup_token(m.group(1)), s)
    s = re.sub(r"\^(\w)", lambda m: _sup_token(m.group(1)), s)
    s = re.sub(r"_\{([^}]*)\}", lambda m: _sub_token(m.group(1)), s)
    s = re.sub(r"_(\w)", lambda m: _sub_token(m.group(1)), s)
    return s


# --------------------------------------------------------------------------
# Paragraph styles
# --------------------------------------------------------------------------
def st(name, **kw):
    base = dict(fontName="VNSans", fontSize=9.3, leading=14.2, textColor=INK,
                alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "Body": st("Body", leading=15.2, spaceAfter=4.5),
    "BodyTight": st("BodyTight", spaceAfter=2),
    "Lead": st("Lead", fontSize=10.2, leading=16.2, textColor=NAVY,
               fontName="VNSans-Bold", spaceAfter=6),
    "H1": st("H1", fontName="VNSans-Bold", fontSize=15, leading=19,
             textColor=colors.white, alignment=TA_LEFT),
    "H2": st("H2", fontName="VNSans-Bold", fontSize=11.4, leading=15,
             textColor=NAVY, alignment=TA_LEFT, spaceBefore=8, spaceAfter=3),
    "H3": st("H3", fontName="VNSans-Bold", fontSize=10, leading=14,
             textColor=TEAL, alignment=TA_LEFT, spaceBefore=4, spaceAfter=2),
    "Bullet": st("Bullet", spaceAfter=2.2),
    "Formula": st("Formula", fontName="VNSerif", fontSize=10.4, leading=21,
                  alignment=TA_CENTER, textColor=NAVY),
    "TblHead": st("TblHead", fontName="VNSans-Bold", fontSize=8.5, leading=11,
                  textColor=colors.white, alignment=TA_CENTER),
    "TblCell": st("TblCell", fontSize=8.4, leading=12.6, alignment=TA_LEFT),
    "TblCellC": st("TblCellC", fontSize=8.4, leading=11.8, alignment=TA_CENTER),
    "Small": st("Small", fontSize=7.9, leading=11, textColor=GRAY),
    "Caption": st("Caption", fontSize=8, leading=11, textColor=GRAY,
                  alignment=TA_CENTER, spaceBefore=2, spaceAfter=6),
    "BoxTitle": st("BoxTitle", fontName="VNSans-Bold", fontSize=9.4, leading=13,
                   alignment=TA_LEFT, spaceAfter=1.5),
    "BoxBody": st("BoxBody", fontSize=8.9, leading=14.4, spaceAfter=2),
    "TOC0": st("TOC0", fontName="VNSans-Bold", fontSize=9.8, leading=17,
               textColor=NAVY, alignment=TA_LEFT),
    "TOC1": st("TOC1", fontSize=9, leading=14, textColor=INK,
               alignment=TA_LEFT, leftIndent=14, firstLineIndent=-0),
}

BOX_STYLE = {
    "remember": (BLUE, BLUE_BG, "CẦN NHỚ"),
    "trap": (RED, RED_BG, "BẪY THƯỜNG GẶP"),
    "tip": (AMBER, AMBER_BG, "MẸO NHỚ"),
    "example": (GREEN, GREEN_BG, "VÍ DỤ MẪU"),
    "note": (GRAY, GRAY_BG, "LƯU Ý"),
}


class KeepTable(Table):
    """Bảng không để lại quá ít dòng ở trang sau (tránh “dòng mồ côi”)."""

    def split(self, availWidth, availHeight):
        parts = Table.split(self, availWidth, availHeight)
        if parts and len(parts) == 2:
            head = getattr(self, "repeatRows", 0) or 0
            try:
                nrows = len(parts[0]._cellvalues)
            except Exception:
                nrows = 99
            if nrows - head <= 1:
                return []
        return parts


class Doc:
    """Bộ dựng nội dung: cung cấp các hàm viết tắt cho flowable."""

    def __init__(self):
        self.story = []
        self._h1 = 0
        self._h2 = 0

    # ---------------- headings ----------------
    def h1(self, title, kicker=None, toc=True):
        if self._h1 > 0:
            from reportlab.platypus import CondPageBreak
            self.story.append(CondPageBreak(235))
        self._h1 += 1
        self._h2 = 0
        cells = []
        if kicker:
            cells.append(Paragraph(
                '<font size="7.6" color="#9CC3EA">%s</font>' % kicker.upper(), S["H1"]))
        cells.append(Paragraph(title, S["H1"]))
        t = Table([[cells]], colWidths=[PAGE_W - LM - RM])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), NAVY),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ("LINEBEFORE", (0, 0), (0, -1), 4, colors.HexColor("#4C9BE8")),
        ]))
        if toc:
            t._toc_text = title
        self.story += [Spacer(1, 6), t, Spacer(1, 8)]
        return t

    def h2(self, title):
        from reportlab.platypus import CondPageBreak, KeepTogether
        p = Paragraph('<font color="#1F5FA8" size="11">▍</font> %s' % title, S["H2"])
        rule = Table([[""]], colWidths=[PAGE_W - LM - RM], rowHeights=[1.2])
        rule.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), LINE)]))
        self.story += [CondPageBreak(118),
                       KeepTogether([Spacer(1, 3), p, rule]), Spacer(1, 5)]
        return p

    def h3(self, title):
        from reportlab.platypus import CondPageBreak
        self.story.append(CondPageBreak(80))
        p = Paragraph(title, S["H3"])
        self.story.append(p)
        return p

    # ---------------- text ----------------
    def p(self, text, style="Body"):
        p = Paragraph(text, S[style])
        self.story.append(p)
        return p

    def lead(self, text):
        p = Paragraph(text, S["Lead"])
        self.story.append(p)
        return p

    def f(self, formula, note=None):
        txt = F(formula)
        if note:
            txt += '&nbsp;&nbsp;<font size="7.6" color="#5F6B7A">(%s)</font>' % F(note)
        t = Table([[Paragraph(txt, S["Formula"])]], colWidths=[PAGE_W - LM - RM])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7FC")),
            ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#DCE5F1")),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        self.story += [Spacer(1, 1.5), t, Spacer(1, 5)]

    def bullets(self, items, bullet="•", indent=12):
        for it in items:
            self.story.append(Paragraph(
                '<para leftIndent="%d" firstLineIndent="-8">'
                '<font color="#1F5FA8"><b>%s</b></font>&nbsp;&nbsp;%s</para>'
                % (indent, bullet, F(it)), S["Bullet"]))
        self.story.append(Spacer(1, 2))

    def nums(self, items, indent=14):
        for i, it in enumerate(items, 1):
            self.story.append(Paragraph(
                '<para leftIndent="%d" firstLineIndent="-11">'
                '<font color="#0E7C86"><b>%d.</b></font>&nbsp;&nbsp;%s</para>'
                % (indent, i, F(it)), S["Bullet"]))
        self.story.append(Spacer(1, 2))

    # ---------------- box ----------------
    def box(self, kind, body, title=None):
        accent, bg, default_title = BOX_STYLE[kind]
        title = title if title is not None else default_title
        rows = []
        if title:
            rows.append([Paragraph(
                '<font color="%s">■</font>&nbsp;&nbsp;%s'
                % (accent.hexval().replace("0x", "#"), title), S["BoxTitle"])])
        if isinstance(body, str):
            items = []
            buf = []
            for line in body.split("\n"):
                if not line.strip():
                    if buf:
                        items.append(("p", " ".join(buf)))
                        buf = []
                    items.append(("gap", ""))
                elif line.startswith("• ") or re.match(r"^\d\.\s", line):
                    if buf:
                        items.append(("p", " ".join(buf)))
                        buf = []
                    items.append(("b", line))
                else:
                    buf.append(line.strip())
            if buf:
                items.append(("p", " ".join(buf)))
        else:
            items = [("p", b) if isinstance(b, str) else ("f", b) for b in body]

        rows = []
        if title:
            rows.append([Paragraph(
                '<font color="%s">■</font>&nbsp;&nbsp;%s'
                % (accent.hexval().replace("0x", "#"), title), S["BoxTitle"])])
        accent_hex = accent.hexval().replace("0x", "#")
        for kind, val in items:
            if kind == "gap":
                rows.append([Spacer(1, 3)])
            elif kind == "f":
                rows.append([val])
            elif kind == "b":
                if val.startswith("• "):
                    para = '<para leftIndent="11" firstLineIndent="-7">' \
                           '<font color="%s">•</font>&nbsp;&nbsp;%s</para>' % (accent_hex, F(val[2:]))
                else:
                    para = '<para leftIndent="13" firstLineIndent="-11">%s</para>' % F(val)
                rows.append([Paragraph(para, S["BoxBody"])])
            else:
                rows.append([Paragraph(F(val), S["BoxBody"])])
        t = Table(rows, colWidths=[PAGE_W - LM - RM])
        style = [
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 2.6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]
        if title:
            style += [("TOPPADDING", (0, 0), (0, 0), 7),
                      ("BOTTOMPADDING", (0, 0), (0, 0), 3)]
        else:
            style += [("TOPPADDING", (0, 0), (-1, 0), 7)]
        style += [("BOTTOMPADDING", (0, -1), (-1, -1), 7)]
        t.setStyle(TableStyle(style))
        try:
            h = t.wrap(PAGE_W - LM - RM, 10000)[1]
        except Exception:
            h = 999
        if h < 360:
            self.story += [KeepTogether([Spacer(1, 2.5), t, Spacer(1, 6)])]
        else:
            self.story += [Spacer(1, 2.5), t, Spacer(1, 6)]

    # ---------------- table ----------------
    def table(self, header, rows, widths, aligns=None, head_bg=NAVY,
              font_size=8.4, zebra=True, first_col_bold=False):
        ncol = len(widths)
        data = []
        if header:
            data.append([Paragraph(h, S["TblHead"]) if h else "" for h in header])
        for r in rows:
            line = []
            for i, c in enumerate(r):
                if isinstance(c, str):
                    style = S["TblCellC"] if (aligns and aligns[i] == "C") else S["TblCell"]
                    if first_col_bold and i == 0:
                        c = "<b>%s</b>" % c
                    line.append(Paragraph(F(c), style))
                else:
                    line.append(c)
            data.append(line)
        t = KeepTable(data, colWidths=widths, repeatRows=1 if header else 0)
        style = [
            ("GRID", (0, 0), (-1, -1), 0.4, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 3.6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
        ]
        if header:
            style += [("BACKGROUND", (0, 0), (-1, 0), head_bg)]
        if zebra:
            for i in range(1 if header else 0, len(data)):
                if (i % 2 == 0):
                    style.append(("BACKGROUND", (0, i), (-1, i), SOFT))
        t.setStyle(TableStyle(style))
        self.story += [Spacer(1, 2), t, Spacer(1, 7)]
        return t

    def callout(self, text, color=TEAL, bg=TEAL_BG, size=9.0):
        t = Table([[Paragraph(F(text).replace("\n", "<br/>"), st("co", fontSize=size, leading=13.4,
                                         textColor=INK))]],
                  colWidths=[PAGE_W - LM - RM])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("LINEBEFORE", (0, 0), (0, -1), 3, color),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        self.story += [Spacer(1, 2), t, Spacer(1, 6)]

    def gap(self, h=6):
        self.story.append(Spacer(1, h))

    def writebox(self, lines=6, label="PHẦN TRÌNH BÀY BÀI LÀM"):
        """Khung kẻ dòng để học sinh viết bài."""
        rows = [[Paragraph('<font size="7.4" color="#8A96A6"><b>%s</b></font>' % label,
                           st("wl", fontSize=7.4, leading=8, alignment=TA_LEFT))]]
        hh = 15 * lines + 12
        t = Table(rows, colWidths=[PAGE_W - LM - RM], rowHeights=[hh])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FCFDFE")),
            ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D5DCE5")),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#D5DCE5")),
        ]))
        self.story += [Spacer(1, 4), t, Spacer(1, 8)]

    def condbreak(self, h=180):
        from reportlab.platypus import CondPageBreak
        self.story.append(CondPageBreak(h))

    def pb(self):
        if self.story and isinstance(self.story[-1], PageBreak):
            return
        self.story.append(PageBreak())

    def keep(self, flows):
        self.story.append(KeepTogether(flows))


# --------------------------------------------------------------------------
# Doc template
# --------------------------------------------------------------------------
class StudyDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập Giữa học kì I – Vật lí 10 – 2026-2027",
                                 author="Tài liệu ôn tập Vật lí 10",
                                 subject="Đề cương ôn tập bám sát ma trận đặc tả",
                                 **kw)
        frame = Frame(LM, BM, PAGE_W - LM - RM, PAGE_H - TM - BM, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._draw_cover),
            PageTemplate(id="body", frames=[frame], onPage=self._draw_body),
        ])

    # -- page decorations ---------------------------------------------------
    def _draw_body(self, canv, doc):
        canv.saveState()
        # header
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.5)
        canv.line(LM, PAGE_H - TM + 14, PAGE_W - RM, PAGE_H - TM + 14)
        canv.setFont("VNSans-Bold", 7.4)
        canv.setFillColor(NAVY)
        canv.drawString(LM, PAGE_H - TM + 20, "VẬT LÍ 10  ·  ÔN TẬP GIỮA HỌC KÌ I")
        canv.setFont("VNSans", 7.4)
        canv.setFillColor(GRAY)
        canv.drawRightString(PAGE_W - RM, PAGE_H - TM + 20, "Năm học 2026 – 2027")
        # footer
        canv.line(LM, BM - 12, PAGE_W - RM, BM - 12)
        canv.setFont("VNSans", 7.2)
        canv.setFillColor(GRAY)
        canv.drawString(LM, BM - 22, "Đề cương bám sát Ma trận – Đặc tả đề kiểm tra giữa kì I")
        # page number badge
        canv.setFillColor(NAVY)
        canv.circle(PAGE_W - RM - 6, BM - 21, 8.5, stroke=0, fill=1)
        canv.setFillColor(colors.white)
        canv.setFont("VNSans-Bold", 7.8)
        canv.drawCentredString(PAGE_W - RM - 6, BM - 23.6, str(canv.getPageNumber()))
        canv.restoreState()

    def _draw_cover(self, canv, doc):
        canv.saveState()
        # nền trên
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - 9.4 * cm, PAGE_W, 9.4 * cm, stroke=0, fill=1)
        # dải màu
        canv.setFillColor(colors.HexColor("#1F5FA8"))
        canv.rect(0, PAGE_H - 9.4 * cm, PAGE_W, 0.22 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#0E7C86"))
        canv.rect(0, PAGE_H - 9.75 * cm, PAGE_W, 0.12 * cm, stroke=0, fill=1)
        # vòng tròn trang trí
        canv.setFillColor(colors.HexColor("#1C4272"))
        canv.circle(PAGE_W - 1.6 * cm, PAGE_H - 1.6 * cm, 3.2 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#22508A"))
        canv.circle(1.1 * cm, PAGE_H - 7.4 * cm, 2.1 * cm, stroke=0, fill=1)

        canv.setFillColor(colors.HexColor("#8FC3F0"))
        canv.setFont("VNSans-Bold", 9.5)
        canv.drawString(1.9 * cm, PAGE_H - 3.1 * cm, "TÀI LIỆU TỰ HỌC  ·  BÁM SÁT MA TRẬN ĐẶC TẢ")

        canv.setFillColor(colors.white)
        canv.setFont("VNSans-Bold", 27)
        canv.drawString(1.9 * cm, PAGE_H - 4.6 * cm, "ĐỀ CƯƠNG ÔN TẬP")
        canv.drawString(1.9 * cm, PAGE_H - 6.0 * cm, "GIỮA HỌC KÌ I")
        canv.setFillColor(colors.HexColor("#BBD9F5"))
        canv.setFont("VNSans-Bold", 17)
        canv.drawString(1.9 * cm, PAGE_H - 7.35 * cm, "VẬT LÍ 10")
        canv.setFillColor(colors.HexColor("#8FC3F0"))
        canv.setFont("VNSans", 11)
        canv.drawString(1.9 * cm, PAGE_H - 8.25 * cm, "Năm học 2026 – 2027")

        # khối thông tin
        y = PAGE_H - 11.4 * cm
        canv.setFillColor(NAVY)
        canv.setFont("VNSans-Bold", 10.5)
        canv.drawString(1.9 * cm, y, "NỘI DUNG TÀI LIỆU")
        canv.setStrokeColor(colors.HexColor("#0E7C86"))
        canv.setLineWidth(2)
        canv.line(1.9 * cm, y - 6, 4.4 * cm, y - 6)

        items = [
            ("01", "Phân tích ma trận – đặc tả", "Biết chính xác cấu trúc đề, trọng số từng bài."),
            ("02", "10 chuyên đề lý thuyết trọng tâm", "Công thức, ví dụ mẫu, bẫy và mẹo nhớ."),
            ("03", "Bộ đề luyện bám 1:1 ma trận", "18 TN + 2 câu đúng/sai + 2 tự luận + 3 câu vận dụng."),
            ("04", "Đáp án, lời giải & chiến lược", "Giải chi tiết, kế hoạch ôn 7 ngày, phòng thi 50 phút."),
        ]
        yy = y - 0.75 * cm
        for num, title, desc in items:
            canv.setFillColor(colors.HexColor("#EEF4FC"))
            canv.roundRect(1.9 * cm, yy - 0.78 * cm, 0.92 * cm, 0.78 * cm, 3, stroke=0, fill=1)
            canv.setFillColor(NAVY)
            canv.setFont("VNSans-Bold", 10)
            canv.drawCentredString(1.9 * cm + 0.46 * cm, yy - 0.5 * cm, num)
            canv.setFillColor(INK)
            canv.setFont("VNSans-Bold", 9.8)
            canv.drawString(3.05 * cm, yy - 0.27 * cm, title)
            canv.setFillColor(GRAY)
            canv.setFont("VNSans", 8.4)
            canv.drawString(3.05 * cm, yy - 0.6 * cm, desc)
            yy -= (0.78 + 0.42) * cm

        # hộp số liệu
        box_y = 3.95 * cm
        canv.setFillColor(colors.HexColor("#F1F5FA"))
        canv.roundRect(1.9 * cm, box_y, PAGE_W - 3.8 * cm, 1.62 * cm, 6, stroke=0, fill=1)
        stats = [("50", "phút làm bài"), ("70%", "trắc nghiệm"),
                 ("30%", "tự luận"), ("10", "đơn vị kiến thức")]
        w = (PAGE_W - 3.8 * cm) / 4
        for i, (big, small) in enumerate(stats):
            cx = 1.9 * cm + w * i + w / 2
            canv.setFillColor(NAVY)
            canv.setFont("VNSans-Bold", 18)
            canv.drawCentredString(cx, box_y + 0.78 * cm, big)
            canv.setFillColor(GRAY)
            canv.setFont("VNSans", 7.6)
            canv.drawCentredString(cx, box_y + 0.40 * cm, small)
            if i:
                canv.setStrokeColor(colors.HexColor("#D5DCE5"))
                canv.setLineWidth(0.5)
                canv.line(1.9 * cm + w * i, box_y + 0.28 * cm, 1.9 * cm + w * i, box_y + 1.34 * cm)

        canv.setFillColor(GRAY)
        canv.setFont("VNSans", 7.6)
        canv.drawString(1.9 * cm, 2.2 * cm,
                        "Biên soạn dựa trên “MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I – MÔN VẬT LÝ LỚP 10”, năm học 2026 – 2027.")
        canv.setStrokeColor(LINE)
        canv.line(1.9 * cm, 1.85 * cm, PAGE_W - 1.9 * cm, 1.85 * cm)
        canv.setFillColor(colors.HexColor("#8A96A6"))
        canv.setFont("VNSans", 7.2)
        canv.drawString(1.9 * cm, 1.45 * cm,
                        "Tài liệu lưu hành nội bộ – dùng cho học sinh ôn thi giữa học kì I.")
        canv.restoreState()

    def beforeDocument(self):
        self._keyn = 0

    def afterFlowable(self, flowable):
        text = getattr(flowable, "_toc_text", None)
        if text:
            self._keyn += 1
            key = "h1-%d" % self._keyn
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text[:90], key, level=0, closed=False)
            self.notify("TOCEntry", (0, text, self.page, key))
            return
        if not isinstance(flowable, Paragraph):
            return
        name = flowable.style.name
        if name == "H2":
            text = flowable.getPlainText().replace("▍", "").strip()
            self._keyn += 1
            key = "h2-%d" % self._keyn
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text[:90], key, level=1, closed=False)


def build_toc():
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(name="TOC0", fontName="VNSans-Bold", fontSize=9.6, leading=16,
                       textColor=NAVY, leftIndent=6, firstLineIndent=0),
        ParagraphStyle(name="TOC1", fontName="VNSans", fontSize=8.8, leading=13.4,
                       textColor=INK, leftIndent=22),
    ]
    toc.dotsMinLevel = 0
    return toc
