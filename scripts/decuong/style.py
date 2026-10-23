# -*- coding: utf-8 -*-
"""Typography, colour palette and reusable flowables for the revision outline."""
from __future__ import annotations

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    CondPageBreak,
    Flowable,
    KeepTogether,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# --------------------------------------------------------------------------- #
#  Fonts
# --------------------------------------------------------------------------- #
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
FONT = "DV"
FONT_B = "DV-Bold"
FONT_M = "DV-Mono"

_registered = False


def register_fonts() -> None:
    global _registered
    if _registered:
        return
    pdfmetrics.registerFont(TTFont(FONT, os.path.join(FONT_DIR, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_B, os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_M, os.path.join(FONT_DIR, "DejaVuSansMono.ttf")))
    pdfmetrics.registerFontFamily(
        FONT, normal=FONT, bold=FONT_B, italic=FONT, boldItalic=FONT_B
    )
    pdfmetrics.registerFontFamily(
        FONT_M, normal=FONT_M, bold=FONT_M, italic=FONT_M, boldItalic=FONT_M
    )
    _registered = True


# --------------------------------------------------------------------------- #
#  Palette
# --------------------------------------------------------------------------- #
INK = colors.HexColor("#152B3A")
MUTED = colors.HexColor("#5A6B7B")
PRIMARY = colors.HexColor("#0E4C6B")
PRIMARY_D = colors.HexColor("#0A3550")
PRIMARY_L = colors.HexColor("#2E7DA6")
ACCENT = colors.HexColor("#D9861F")
ACCENT_L = colors.HexColor("#F2B455")
RED = colors.HexColor("#A8332A")
GREEN = colors.HexColor("#1D6B4C")
BLUE = colors.HexColor("#1F5F99")
PURPLE = colors.HexColor("#5B3E96")
LINE = colors.HexColor("#D3DDE6")
BG_SOFT = colors.HexColor("#F3F7FA")
BG_BLUE = colors.HexColor("#E9F1F9")
BG_AMBER = colors.HexColor("#FDF3E2")
BG_RED = colors.HexColor("#FBEDEB")
BG_GREEN = colors.HexColor("#E9F4EE")
BG_PURPLE = colors.HexColor("#F1ECF8")
BG_DARK = colors.HexColor("#0E4C6B")

PAGE_W, PAGE_H = A4
MARGIN_L = 42
MARGIN_R = 42
MARGIN_T = 62
MARGIN_B = 46
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R  # 511.3 pt


# --------------------------------------------------------------------------- #
#  Paragraph styles
# --------------------------------------------------------------------------- #
def ps(name, **kw):
    base = dict(
        fontName=FONT,
        fontSize=9.2,
        leading=13.4,
        textColor=INK,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=0,
    )
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "body": ps("body", alignment=TA_JUSTIFY, spaceAfter=3),
    "body_c": ps("body_c", alignment=TA_CENTER),
    "small": ps("small", fontSize=8.2, leading=11.6, textColor=MUTED),
    "small_j": ps("small_j", fontSize=8.2, leading=11.8, alignment=TA_JUSTIFY, textColor=INK),
    "bullet": ps("bullet", alignment=TA_JUSTIFY, leftIndent=13, bulletIndent=2, spaceAfter=2.2),
    "bullet_sub": ps(
        "bullet_sub", alignment=TA_JUSTIFY, leftIndent=26, bulletIndent=14,
        fontSize=8.9, leading=12.8, spaceAfter=1.8, textColor=colors.HexColor("#2B3F4E"),
    ),
    "num": ps("num", alignment=TA_JUSTIFY, leftIndent=16, bulletIndent=1, spaceAfter=2.2),
    "h1": ps(
        "h1", fontName=FONT_B, fontSize=15.5, leading=21, textColor=colors.white,
        backColor=PRIMARY, borderPadding=(5, 8, 6, 8), alignment=TA_LEFT,
        spaceBefore=2, spaceAfter=10,
    ),
    "h2": ps(
        "h2", fontName=FONT_B, fontSize=11.6, leading=15.5, textColor=PRIMARY,
        spaceBefore=9, spaceAfter=4,
    ),
    "lesson": ps(
        "lesson", fontName=FONT_B, fontSize=12.6, leading=17, textColor=PRIMARY,
        spaceBefore=13, spaceAfter=3,
    ),
    "h3": ps(
        "h3", fontName=FONT_B, fontSize=9.9, leading=13.5, textColor=PRIMARY_D,
        spaceBefore=6, spaceAfter=2.5,
    ),
    "box_title": ps("box_title", fontName=FONT_B, fontSize=9.2, leading=12.5, spaceAfter=2.5),
    "box_body": ps("box_body", fontSize=8.9, leading=12.6, alignment=TA_JUSTIFY, spaceAfter=2),
    "box_item": ps("box_item", fontSize=8.9, leading=12.6, alignment=TA_JUSTIFY,
                   leftIndent=11, bulletIndent=1, spaceAfter=1.6),
    "formula": ps("formula", fontName=FONT_B, fontSize=10.4, leading=15, alignment=TA_CENTER),
    "formula_note": ps("formula_note", fontSize=8.1, leading=11.2, alignment=TA_CENTER,
                       textColor=MUTED),
    "tbl_head": ps("tbl_head", fontName=FONT_B, fontSize=8.3, leading=11.2,
                   textColor=colors.white),
    "tbl": ps("tbl", fontSize=8.3, leading=11.4, alignment=TA_LEFT),
    "tbl_c": ps("tbl_c", fontSize=8.3, leading=11.4, alignment=TA_CENTER),
    "tbl_small": ps("tbl_small", fontSize=7.7, leading=10.4, alignment=TA_LEFT),
    "toc1": ps("toc1", fontName=FONT_B, fontSize=8.9, leading=12.2, textColor=PRIMARY),
    "toc1_pg": ps("toc1_pg", fontName=FONT_B, fontSize=8.9, leading=12.2,
                  textColor=PRIMARY, alignment=2),
    "toc2": ps("toc2", fontSize=8.2, leading=11.6, textColor=INK, leftIndent=12),
    "part_tag": ps("part_tag", fontName=FONT_B, fontSize=13, leading=15, textColor=PRIMARY),
    "part_desc": ps("part_desc", fontSize=8.3, leading=11.4, textColor=INK),
    "toc_pg": ps("toc_pg", fontSize=8.2, leading=11.6, textColor=MUTED, alignment=2),
    "q": ps("q", fontSize=8.9, leading=12.7, alignment=TA_JUSTIFY, spaceAfter=1.4),
    "opt": ps("opt", fontSize=8.6, leading=12, leftIndent=10, spaceAfter=0.6),
    "sol": ps("sol", fontSize=8.6, leading=12.4, alignment=TA_JUSTIFY, spaceAfter=2.5),
    "mini": ps("mini", fontSize=8.1, leading=11.6, textColor=INK, spaceAfter=1.6),
    "cap": ps("cap", fontSize=7.9, leading=10.6, alignment=TA_CENTER, textColor=MUTED),
}


# --------------------------------------------------------------------------- #
#  Small helpers
# --------------------------------------------------------------------------- #
def P(text: str, style: str = "body") -> Paragraph:
    return Paragraph(text, S[style])


def SPC(h: float) -> Spacer:
    return Spacer(1, h)


def bullets(items, style: str = "bullet", mark: str = "•", color: str | None = None):
    out = []
    for it in items:
        if color:
            it = f'<font color="{color}">{mark}</font> {it}'
            out.append(Paragraph(it, S[style], bulletText=""))
        else:
            out.append(Paragraph(it, S[style], bulletText=mark))
    return out


def numbered(items, style: str = "num", start: int = 1, color: str = "#0E4C6B"):
    out = []
    for i, it in enumerate(items, start):
        out.append(
            Paragraph(
                f'<font color="{color}"><b>{i}.</b></font> {it}', S[style], bulletText=""
            )
        )
    return out


# --------------------------------------------------------------------------- #
#  Call-out box
# --------------------------------------------------------------------------- #
KINDS = {
    "def": (PRIMARY_L, BG_BLUE, "◆"),
    "tip": (ACCENT, BG_AMBER, "★"),
    "warn": (RED, BG_RED, "⚠"),
    "ex": (GREEN, BG_GREEN, "▶"),
    "note": (PURPLE, BG_PURPLE, "✎"),
}


def box(title: str, flowables, kind: str = "def", title_color=None, keep: bool = False):
    """A coloured call-out with a thick left rule."""
    accent, bg, icon = KINDS[kind]
    inner = []
    if title:
        inner.append(
            Paragraph(
                f'<font color="{accent.hexval()}">{icon}</font> '
                f'<font color="{(title_color or accent).hexval()}">{title}</font>',
                S["box_title"],
            )
        )
    if isinstance(flowables, str):
        flowables = [P(flowables, "box_body")]
    inner.extend(flowables)
    t = Table([[inner]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("LINEBEFORE", (0, 0), (0, -1), 2.6, accent),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 5.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    t.spaceAfter = 5
    t.keepWithNext = keep
    return t


def formula(text: str, note: str | None = None):
    """Centred formula strip."""
    inner = [Paragraph(text, S["formula"])]
    if note:
        inner.append(Paragraph(note, S["formula_note"]))
    t = Table([[inner]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BG_SOFT),
                ("LINEBEFORE", (0, 0), (0, -1), 2.4, PRIMARY_L),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
            ]
        )
    )
    return [t, Spacer(1, 4.5)]


# --------------------------------------------------------------------------- #
#  Tables
# --------------------------------------------------------------------------- #
def data_table(
    header,
    rows,
    widths,
    align=None,
    zebra: bool = True,
    head_bg=PRIMARY,
    font: str = "tbl",
    pad: float = 4.0,
):
    align = align or ["LEFT"] * len(header)
    data = [[Paragraph(str(h), S["tbl_head"]) for h in header]]
    for r in rows:
        data.append(
            [
                Paragraph(str(c), S["tbl_c"] if align[i] == "CENTER" else S[font])
                for i, c in enumerate(r)
            ]
        )
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), head_bg),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), pad),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), BG_SOFT))
    t.setStyle(TableStyle(cmds))
    return t


# --------------------------------------------------------------------------- #
#  Question blocks
# --------------------------------------------------------------------------- #
def question(num, stem: str, options=None, cols: int = 4, tag: str | None = None):
    """MCQ block: number + stem + options laid out in a table."""
    head = f'<font color="#0E4C6B"><b>Câu {num}.</b></font> '
    if tag:
        head += f'<font color="#8A6A2F" size="7.6"><b>[{tag}]</b></font> '
    out = [Paragraph(head + stem, S["q"])]
    if options:
        letters = "ABCD"
        width = CONTENT_W / cols
        cells = []
        for i, o in enumerate(options):
            cells.append(Paragraph(f"<b>{letters[i]}.</b> {o}", S["opt"]))
        # pad
        while len(cells) % cols:
            cells.append(Paragraph("", S["opt"]))
        rows = [cells[i : i + cols] for i in range(0, len(cells), cols)]
        t = Table(rows, colWidths=[width] * cols, hAlign="LEFT")
        t.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
                ]
            )
        )
        out += [t, Spacer(1, 4.2)]
    else:
        out.append(Spacer(1, 3))
    return [KeepTogether(out)]


class Rule(Flowable):
    """Thin horizontal rule that can sit inside frames."""

    def __init__(self, width=CONTENT_W, thickness=0.7, color=LINE, space=3):
        super().__init__()
        self.width, self.thickness, self.color, self.space = width, thickness, color, space
        self.height = thickness + 2 * space

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.space, self.width, self.space)


def rule(width=CONTENT_W, thickness=0.7, color=LINE, space=3):
    return Rule(width, thickness, color, space)


def keep(*flowables):
    return KeepTogether(list(flowables))


def cond(h: float):
    return CondPageBreak(h)


# --------------------------------------------------------------------------- #
#  Lesson header (Bài 1, Bài 2, ...)
# --------------------------------------------------------------------------- #
def lesson_header(num: str, title: str, matrix: str, extra: str = ""):
    out = [CondPageBreak(150),
        Paragraph(f"BÀI {num} · {title}", S["lesson"]),
        Rule(color=PRIMARY, thickness=1.0, space=1),
        Paragraph(f'<font color="#5A6B7B">▸ {matrix}</font>', S["small"]),
        Spacer(1, 4),
    ]
    if extra:
        out.insert(3, Paragraph(extra, S["small"]))
    return out
