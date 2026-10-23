#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renderer for the Physics-10 mid-term-I review outline (de cuong on tap).

Reads lightweight markup files (see README of tools/) and produces a single,
typeset, Vietnamese-correct PDF using Be Vietnam Pro + DejaVu fallback glyphs.

Usage:
    python3 tools/render.py <content_dir> <output.pdf>
"""

from __future__ import annotations

import os
import sys

from fpdf import FPDF, FontFace
from fpdf.enums import XPos, YPos

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(ROOT, "assets", "fonts")
DEJAVU_DIR = "/usr/share/fonts/truetype/dejavu"

# --------------------------------------------------------------------------
# Palette
# --------------------------------------------------------------------------
INK       = (26, 32, 44)
INK_SOFT  = (92, 102, 122)
BRAND     = (20, 55, 116)
BRAND_MID = (47, 96, 178)
BRAND_L   = (232, 240, 254)
ACCENT    = (190, 104, 4)
ACCENT_L  = (255, 250, 238)
GREEN     = (18, 114, 56)
GREEN_L   = (238, 250, 243)
RED       = (176, 30, 30)
RED_L     = (254, 243, 243)
VIOLET    = (108, 51, 168)
VIOLET_L  = (247, 242, 254)
SLATE     = (100, 114, 136)
SLATE_L   = (245, 247, 251)
RULE      = (216, 222, 232)

PAGE_W, PAGE_H = 210.0, 297.0
L_MARGIN = 16.0
R_MARGIN = 16.0
T_MARGIN = 19.0
B_MARGIN = 16.0
CONTENT_W = PAGE_W - L_MARGIN - R_MARGIN  # 178 mm

TITLE_MAIN = "ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA KÌ I"
TITLE_SUB = "MÔN: VẬT LÍ – LỚP 10 · NĂM HỌC 2026 – 2027"
RUNNING = "Đề cương ôn tập KTGK I – Vật lí 10 (2026–2027)"


def split_label(group):
    """Allow `![LABEL] text` to override the default callout heading."""
    import re as _re
    m = _re.match(r"^\[([^\]]+)\]\s*(.*)$", group[0])
    if not m:
        return None, group
    label, rest = m.group(1).strip(), m.group(2).strip()
    body = ([rest] if rest else []) + list(group[1:])
    return label.upper(), body


# --------------------------------------------------------------------------
# Markdown-ish block parser
# --------------------------------------------------------------------------
def parse(lines):
    """Turn raw markup lines into a list of (kind, payload) blocks."""
    blocks = []
    para = []
    table = []

    def flush_para():
        if para:
            blocks.append(("P", " ".join(x.strip() for x in para)))
            para.clear()

    def flush_table():
        if table:
            blocks.append(("TABLE", list(table)))
            table.clear()

    for raw in lines:
        line = raw.rstrip("\n").rstrip()
        stripped = line.strip()

        if stripped.startswith(";;"):
            continue

        if not stripped:
            flush_para()
            flush_table()
            continue

        head2 = stripped[:2]
        if head2 == "==" or stripped.startswith("== "):
            flush_para(); flush_table()
            blocks.append(("PART", stripped.strip("=").strip()))
            continue
        if stripped.startswith("= ") or (stripped.startswith("=") and not stripped.startswith("==")):
            flush_para(); flush_table()
            blocks.append(("H2", stripped.strip("=").strip()))
            continue
        if stripped.startswith("--"):
            flush_para(); flush_table()
            blocks.append(("H4", stripped[2:].strip().strip("-=").strip()))
            continue
        if stripped.startswith("-"):
            flush_para(); flush_table()
            blocks.append(("H3", stripped[1:].strip().strip("-=").strip()))
            continue

        if stripped.startswith("|"):
            flush_para()
            table.append(stripped)
            continue

        code = head2[0] if head2 else ""
        rest = stripped[1:].strip() if code in "*#~!?@QO KES" else ""

        if head2 == "* ":
            flush_para(); flush_table()
            blocks.append(("UL", stripped[1:].strip()))
        elif stripped.startswith("** "):
            flush_para(); flush_table()
            blocks.append(("UL2", stripped[2:].strip()))
        elif head2 == "# ":
            flush_para(); flush_table()
            blocks.append(("NUM", stripped[1:].strip()))
        elif head2 == "~ " or stripped == "~":
            flush_para(); flush_table()
            blocks.append(("FORM", stripped[1:].strip()))
        elif head2 == "! ":
            flush_para(); flush_table()
            blocks.append(("TIP", stripped[1:].strip()))
        elif head2 == "? ":
            flush_para(); flush_table()
            blocks.append(("WARN", stripped[1:].strip()))
        elif head2 == "@ ":
            flush_para(); flush_table()
            blocks.append(("KEY", stripped[1:].strip()))
        elif head2 == "Q ":
            flush_para(); flush_table()
            blocks.append(("Q", stripped[1:].strip()))
        elif head2 == "O ":
            flush_para(); flush_table()
            blocks.append(("OPT", stripped[1:].strip()))
        elif head2 == "K ":
            flush_para(); flush_table()
            blocks.append(("ANS", stripped[1:].strip()))
        elif head2 == "E ":
            flush_para(); flush_table()
            blocks.append(("EXP", stripped[1:].strip()))
        elif head2 == "S ":
            flush_para(); flush_table()
            blocks.append(("SOL", stripped[1:].strip()))
        elif stripped == "///":
            flush_para(); flush_table()
            blocks.append(("BREAK", ""))
        else:
            flush_table()
            para.append(stripped)

    flush_para()
    flush_table()
    return blocks


# --------------------------------------------------------------------------
# Document
# --------------------------------------------------------------------------
class Doc(FPDF):
    def __init__(self, collect_toc=False, toc_shift=0):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.collect_toc = collect_toc
        self.toc_shift = toc_shift
        self.toc_entries = []
        self.cur_part = ""
        self.cur_section = ""
        self.no_chrome_pages = set()
        self.on_cover = False
        self.on_toc = False
        self.font_ready = False
        self.set_margins(L_MARGIN, T_MARGIN, R_MARGIN)
        self.set_auto_page_break(True, B_MARGIN)
        self._register_fonts()
        self.set_font("bv", size=10.2)
        self.set_text_color(*INK)

    # -- fonts ---------------------------------------------------------
    def _register_fonts(self):
        self.add_font("dejavu", "", os.path.join(DEJAVU_DIR, "DejaVuSans.ttf"))
        self.add_font("dejavu", "B", os.path.join(DEJAVU_DIR, "DejaVuSans-Bold.ttf"))
        self.add_font("bv", "", os.path.join(FONT_DIR, "BeVietnamPro-Regular.ttf"))
        self.add_font("bv", "B", os.path.join(FONT_DIR, "BeVietnamPro-Bold.ttf"))
        self.add_font("bv", "I", os.path.join(FONT_DIR, "BeVietnamPro-Italic.ttf"))
        self.add_font("bv", "BI", os.path.join(FONT_DIR, "BeVietnamPro-BoldItalic.ttf"))
        self.add_font("bvsb", "", os.path.join(FONT_DIR, "BeVietnamPro-SemiBold.ttf"))
        self.add_font("bvsb", "B", os.path.join(FONT_DIR, "BeVietnamPro-Bold.ttf"))
        self.add_font("bvsb", "I", os.path.join(FONT_DIR, "BeVietnamPro-Italic.ttf"))
        self.add_font("bvsb", "BI", os.path.join(FONT_DIR, "BeVietnamPro-BoldItalic.ttf"))
        self.set_fallback_fonts(["dejavu"])
        self.font_ready = True

    # -- chrome --------------------------------------------------------
    def header(self):
        if self.on_cover or self.on_toc or not self.font_ready:
            return
        self.set_font("bv", size=7.8)
        self.set_text_color(*SLATE)
        self.set_xy(L_MARGIN, 9)
        left = self.cur_part or ""
        right = self.cur_section or ""
        left = left if len(left) <= 74 else left[:71] + "..."
        right = right if len(right) <= 40 else right[:37] + "..."
        self.cell(CONTENT_W - 62, 5, left, align="L")
        self.set_text_color(*BRAND_MID)
        self.cell(62, 5, right, align="R")
        # hairline
        self.set_draw_color(*RULE)
        self.set_line_width(0.25)
        self.line(L_MARGIN, 14.6, PAGE_W - R_MARGIN, 14.6)
        self.set_y(max(self.get_y(), T_MARGIN))

    def footer(self):
        if self.on_cover or self.page_no() in self.no_chrome_pages:
            return
        self.set_draw_color(*RULE)
        self.set_line_width(0.22)
        self.line(L_MARGIN, PAGE_H - 13.5, PAGE_W - R_MARGIN, PAGE_H - 13.5)
        self.set_y(-12.4)
        self.set_font("bv", size=7.8)
        self.set_text_color(*SLATE)
        self.cell(CONTENT_W / 2, 5, RUNNING, align="L")
        self.set_font("bvsb", size=8.4)
        self.set_text_color(*BRAND)
        self.cell(CONTENT_W / 2, 5, f"Trang {self.page_no()}", align="R")

    # -- helpers -------------------------------------------------------
    def _ensure(self, h):
        """Page-break if `h` mm will not fit."""
        if self.get_y() + h > PAGE_H - B_MARGIN - 2:
            self.add_page()

    def _bar(self, y0, y1, color, w=1.1, x=None):
        x = L_MARGIN if x is None else x
        self.set_fill_color(*color)
        self.rect(x, y0, w, max(y1 - y0, 0.1), style="F")

    def _boxed(self, text, fill, bar_color, size=9.6, lh=5.0,
               pad=(2.0, 2.6), style="", gap=2.0, label=None, label_color=None):
        """Paragraph inside a filled box with a left accent bar."""
        eff_w = CONTENT_W
        self.set_font("bv", style, size)
        # estimate height for page-break safety
        approx = self.multi_cell(eff_w, lh, text, markdown=True, dry_run=True,
                                 output="LINES", padding=pad)
        need = len(approx) * lh + 2 * pad[0 if isinstance(pad, (list, tuple)) else 0]
        if label:
            need += lh + 2 * pad[0]
        self._ensure(need + 3)
        y0 = self.get_y()
        if label:
            self.set_font("bvsb", size=size - 0.3)
            self.set_text_color(*(label_color or bar_color))
            self.multi_cell(eff_w, lh - 0.4, f"**{label}**", markdown=True,
                            padding=(pad[0], pad[1], 0, pad[1]),
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("bv", style, size)
        self.set_text_color(*INK)
        self.set_fill_color(*fill)
        self.multi_cell(eff_w, lh, text, markdown=True, padding=pad,
                        fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y1 = self.get_y()
        self._bar(y0, y1, bar_color)
        self.set_y(y1 + gap)

    def _fit(self, text, max_w):
        """Truncate `text` with an ellipsis so it fits within `max_w` mm."""
        if self.get_string_width(text) <= max_w:
            return text
        s = text
        while s and self.get_string_width(s + "…") > max_w:
            s = s[:-1]
        return (s + "…") if s else ""

    # -- cover ---------------------------------------------------------
    def cover(self, meta_rows):
        self.on_cover = True
        self.add_page()
        self.no_chrome_pages.add(self.page_no())
        # full-bleed banner
        self.set_fill_color(*BRAND)
        self.rect(0, 0, PAGE_W, 118, style="F")
        self.set_fill_color(*ACCENT)
        self.rect(0, 118, PAGE_W, 4.2, style="F")
        # decorative arcs
        self.set_draw_color(255, 255, 255)
        self.set_line_width(0.5)
        for r in (58, 78, 98):
            self.set_draw_color(255, 255, 255)
            self.ellipse(PAGE_W - 52 - r / 2, -18, r, r, style=None)
        self.set_fill_color(255, 255, 255)

        self.set_xy(L_MARGIN + 4, 26)
        self.set_text_color(255, 255, 255)
        self.set_font("bv", size=9.5)
        self.cell(CONTENT_W - 8, 5.5, "BỘ SÁCH: KẾT NỐI TRI THỨC VỚI CUỘC SỐNG", align="L")

        self.set_xy(L_MARGIN + 4, 40)
        self.set_font("bv", "B", 27)
        self.multi_cell(CONTENT_W - 8, 12.4, TITLE_MAIN, align="L")

        self.set_xy(L_MARGIN + 4, self.get_y() + 2)
        self.set_font("bvsb", size=13.5)
        self.set_text_color(255, 214, 150)
        self.multi_cell(CONTENT_W - 8, 7.4, TITLE_SUB, align="L")

        self.set_xy(L_MARGIN + 4, self.get_y() + 3)
        self.set_font("bv", size=9.8)
        self.set_text_color(216, 226, 245)
        self.multi_cell(CONTENT_W - 8, 5.6,
                        "Tài liệu được xây dựng **bám sát 100%** Ma trận & Bản đặc tả đề kiểm tra "
                        "giữa kì I của nhà trường (tệp .docx gốc trong kho lưu trữ này).",
                        markdown=True)

        # meta card
        y = 132
        self.set_fill_color(*SLATE_L)
        self.rect(L_MARGIN, y, CONTENT_W, 10 + len(meta_rows) * 7.0, style="F")
        self.set_fill_color(*ACCENT)
        self.rect(L_MARGIN, y, 1.6, 10 + len(meta_rows) * 7.0, style="F")
        self.set_xy(L_MARGIN + 5, y + 3.4)
        self.set_font("bv", "B", 10.4)
        self.set_text_color(*BRAND)
        self.cell(CONTENT_W - 10, 5.4, "THÔNG TIN BÀI KIỂM TRA", align="L")
        yy = y + 11.4
        for k, v in meta_rows:
            self.set_xy(L_MARGIN + 5, yy)
            self.set_font("bv", size=9.4)
            self.set_text_color(*SLATE)
            self.cell(46, 6, k, align="L")
            self.set_font("bvsb", size=9.6)
            self.set_text_color(*INK)
            self.multi_cell(CONTENT_W - 52, 6, v, markdown=True,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            yy = self.get_y() + 0.6

        # how-to-use
        y2 = yy + 3
        self._ensure(46)
        self.set_xy(L_MARGIN, y2)
        self.set_font("bv", "B", 10.4)
        self.set_text_color(*BRAND)
        self.cell(CONTENT_W, 5.4, "CÁCH DÙNG TÀI LIỆU HIỆU QUẢ (4 BƯỚC)", align="L")
        steps = [
            ("Bước 1", "Đọc **Phần A** để nắm cấu trúc đề và tỉ trọng điểm của từng phần.", BRAND),
            ("Bước 2", "Học **Phần B** theo 10 đơn vị kiến thức; chỉ cần nhớ các hộp **Cần nhớ** và **Mẹo nhớ**.", GREEN),
            ("Bước 3", "Làm thử **Phần C** trong 50 phút, không xem đáp án. Sau đó đối chiếu **bảng đáp án nhanh**.", ACCENT),
            ("Bước 4", "Đọc **Phần D** để hiểu bản chất từng câu sai, rồi luyện thêm **Phần E** theo đơn vị kiến thức.", VIOLET),
        ]
        yy = self.get_y() + 3.2
        for tag, txt, col in steps:
            self.set_fill_color(*SLATE_L)
            self.rect(L_MARGIN, yy, CONTENT_W, 9.2, style="F")
            self.set_fill_color(*col)
            self.rect(L_MARGIN, yy, 1.6, 9.2, style="F")
            self.set_xy(L_MARGIN + 5, yy + 1.5)
            self.set_font("bv", "B", 8.6)
            self.set_text_color(*col)
            self.cell(19, 5, tag.upper(), align="L")
            self.set_font("bv", size=9.2)
            self.set_text_color(*INK)
            self.multi_cell(CONTENT_W - 26, 5.6, txt, markdown=True,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            yy += 10.4
        self.on_cover = False

    # -- table of contents ---------------------------------------------
    def toc(self):
        self.on_toc = True
        self.add_page()
        self.set_y(T_MARGIN)
        self.set_font("bv", "B", 16)
        self.set_text_color(*BRAND)
        self.cell(CONTENT_W, 9, "MỤC LỤC", align="L")
        self.ln(1)
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.9)
        self.line(L_MARGIN, self.get_y(), L_MARGIN + 26, self.get_y())
        self.ln(5)

        col_w = (CONTENT_W - 8) / 2
        xs = [L_MARGIN, L_MARGIN + col_w + 8]
        top = self.get_y()
        bottom = PAGE_H - B_MARGIN - 4
        col = 0
        y = top
        entries = self.toc_entries
        half = (len(entries) + 1) // 2
        order = [(0, entries[:half]), (1, entries[half:])]
        for ci, group in order:
            y = top
            for kind, label, page in group:
                x = xs[ci]
                if kind == "PART":
                    y += 2.4
                    self.set_xy(x, y)
                    self.set_font("bv", "B", 9.4)
                    self.set_text_color(*BRAND)
                    self.cell(col_w - 11, 5.2, self._fit(label, col_w - 11), align="L")
                    if page:
                        self.set_font("bv", "B", 9.0)
                        self.cell(11, 5.2, str(page), align="R")
                    y += 5.6
                    self.set_draw_color(*RULE)
                    self.set_line_width(0.2)
                    self.line(x, y - 0.8, x + col_w, y - 0.8)
                    y += 0.6
                elif kind == "H3":
                    self.set_xy(x + 7.0, y)
                    self.set_font("bv", size=8.2)
                    self.set_text_color(*SLATE)
                    self.cell(col_w - 18.0, 4.7, self._fit(label, col_w - 18.0),
                              align="L")
                    if page:
                        self.set_font("bv", size=7.9)
                        self.cell(11, 4.7, str(page), align="R")
                    y += 4.7
                else:
                    self.set_xy(x + 3.5, y)
                    self.set_font("bv", size=8.6)
                    self.set_text_color(*INK_SOFT)
                    self.cell(col_w - 14.5, 5.0, self._fit(label, col_w - 14.5),
                              align="L")
                    if page:
                        self.set_font("bv", size=8.2)
                        self.set_text_color(*SLATE)
                        self.cell(11, 5.0, str(page), align="R")
                    y += 5.0
        self.on_toc = False

    # -- content -------------------------------------------------------
    def render(self, blocks):
        num_counter = [0]
        idx = 0
        n = len(blocks)
        while idx < n:
            kind, payload = blocks[idx]

            # group consecutive same-kind simple blocks
            if kind in ("FORM", "TIP", "WARN", "KEY", "UL", "UL2", "NUM", "SOL", "EXP", "OPT"):
                j = idx
                group = []
                while j < n and blocks[j][0] == kind:
                    group.append(blocks[j][1])
                    j += 1
                self._render_group(kind, group, num_counter)
                idx = j
                continue

            self._render_one(kind, payload, num_counter)
            if kind not in ("P",):
                num_counter[0] = 0
            idx += 1

    def _render_group(self, kind, group, counter):
        if kind == "OPT":
            for item in group:
                self._opt(item)
            return
        if kind == "UL":
            for item in group:
                self._bullet(item)
            self.ln(1.2)
            return
        if kind == "UL2":
            for item in group:
                self._bullet(item, level=2)
            self.ln(1.2)
            return
        if kind == "NUM":
            for item in group:
                counter[0] += 1
                self._bullet(f"**{counter[0]}.** {item}")
            self.ln(1.2)
            return
        if kind == "SOL":
            for item in group:
                self._sol(item)
            return
        if kind == "EXP":
            for item in group:
                self._exp(item)
            return
        if kind == "FORM":
            self._formula(group)
            return
        if kind == "TIP":
            label, body = split_label(group)
            self._boxed("\n".join(body), GREEN_L, GREEN,
                        label=label or "MẸO NHỚ", label_color=GREEN)
            return
        if kind == "WARN":
            label, body = split_label(group)
            self._boxed("\n".join(body), ACCENT_L, ACCENT,
                        label=label or "LƯU Ý", label_color=ACCENT)
            return
        if kind == "KEY":
            label, body = split_label(group)
            self._boxed("\n".join(body), BRAND_L, BRAND_MID,
                        label=label or "CẦN NHỚ", label_color=BRAND)
            return

    def _render_one(self, kind, payload, counter):
        if kind == "PART":
            self.add_page()
            self.set_y(T_MARGIN + 2)
            self.set_fill_color(*BRAND)
            self.rect(L_MARGIN, self.get_y(), CONTENT_W, 13.5, style="F")
            self.set_fill_color(*ACCENT)
            self.rect(L_MARGIN, self.get_y(), 2.2, 13.5, style="F")
            self.set_xy(L_MARGIN + 6, self.get_y() + 3.6)
            self.set_font("bv", "B", 13.2)
            self.set_text_color(255, 255, 255)
            self.cell(CONTENT_W - 12, 6.4, payload, align="L")
            self.set_y(self.get_y() + 8.6)
            self.cur_part = payload
            self.cur_section = ""
            if self.collect_toc:
                self.toc_entries.append(("PART", payload, self.page_no()))
            return

        if kind == "H2":
            self._ensure(20)
            self.ln(2.6)
            self.set_font("bv", "B", 11.6)
            self.set_text_color(*BRAND)
            self.multi_cell(CONTENT_W, 6.2, payload, align="L",
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_draw_color(*ACCENT)
            self.set_line_width(0.55)
            self.line(L_MARGIN, self.get_y() + 0.4, L_MARGIN + 30, self.get_y() + 0.4)
            self.ln(2.6)
            self.cur_section = payload
            if self.collect_toc:
                self.toc_entries.append(("H2", payload, self.page_no()))
            return

        if kind == "H3":
            self._ensure(16)
            self.ln(1.8)
            self.set_font("bvsb", size=10.6)
            self.set_text_color(*BRAND)
            y0 = self.get_y()
            self.multi_cell(CONTENT_W, 5.8, payload, align="L",
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_fill_color(*BRAND_L)
            self.rect(L_MARGIN, y0 + 5.6, CONTENT_W, 0.9, style="F")
            self.ln(2.8)
            self.cur_section = payload
            if self.collect_toc:
                self.toc_entries.append(("H3", payload, self.page_no()))
            return

        if kind == "H4":
            self._ensure(12)
            self.ln(1.0)
            self.set_font("bvsb", size=9.9)
            self.set_text_color(*INK)
            self.multi_cell(CONTENT_W, 5.4, payload, align="L",
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(1.2)
            return

        if kind == "P":
            self.set_font("bv", size=9.9)
            self.set_text_color(*INK)
            self.multi_cell(CONTENT_W, 5.5, payload, align="J", markdown=True,
                            new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.ln(1.6)
            return

        if kind == "BREAK":
            self.add_page()
            return

        if kind == "TABLE":
            self._table(payload)
            return

        if kind == "Q":
            self._question(payload)
            return

        if kind == "ANS":
            self._answer(payload)
            return

    # -- primitives ----------------------------------------------------
    def _bullet(self, text, level=1):
        indent = 5.0 if level == 1 else 11.0
        bullet = "•" if level == 1 else "–"
        self.set_font("bv", size=9.9)
        self.set_text_color(*INK)
        x = L_MARGIN + indent
        w = CONTENT_W - indent
        self._ensure(6)
        y0 = self.get_y()
        self.set_x(x)
        self.set_font("bvsb", size=9.4)
        self.set_text_color(*BRAND_MID)
        self.cell(3.6, 5.4, bullet, align="L")
        self.set_font("bv", size=9.9)
        self.set_text_color(*INK)
        self.set_xy(x + 3.6, y0)
        self.multi_cell(w - 3.6, 5.4, text, align="J", markdown=True,
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(self.get_y() + 0.4)

    def _formula(self, lines):
        body = "\n".join(lines)
        eff_w = CONTENT_W - 8
        self.set_font("bv", size=10.4)
        approx = self.multi_cell(eff_w, 6.0, body, markdown=True, dry_run=True,
                                 output="LINES", padding=(2.4, 3.0))
        self._ensure(len(approx) * 6.0 + 8)
        y0 = self.get_y()
        self.set_fill_color(*SLATE_L)
        self.set_draw_color(*RULE)
        self.set_line_width(0.25)
        h = len(approx) * 6.0 + 2 * 2.4
        self.rect(L_MARGIN + 4, y0, CONTENT_W - 8, h, style="DF")
        self.set_fill_color(*BRAND_MID)
        self.rect(L_MARGIN + 4, y0, 1.4, h, style="F")
        self.set_xy(L_MARGIN + 4, y0)
        self.set_text_color(*INK)
        self.multi_cell(eff_w, 6.0, body, align="C", markdown=True,
                        padding=(2.4, 3.0, 2.4, 6.0),
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(y0 + h + 2.6)

    def _table(self, rows):
        parsed = []
        for r in rows:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            parsed.append(cells)
        if not parsed:
            return
        # strip separator rows like --- | ---
        parsed = [r for r in parsed if not all(set(c) <= set("-: ") for c in r)]
        if not parsed:
            return
        header, body = parsed[0], parsed[1:]
        ncol = max(len(r) for r in parsed)
        header += [""] * (ncol - len(header))
        for r in body:
            r += [""] * (ncol - len(r))

        # column widths proportional to content length
        maxlen = [1] * ncol
        for r in parsed:
            for i, c in enumerate(r):
                maxlen[i] = max(maxlen[i], len(c))
        total = sum(maxlen)
        widths = [CONTENT_W * m / total for m in maxlen]
        # clamp: no column below 9mm
        minw = 9.0
        for i, w in enumerate(widths):
            if w < minw:
                widths[i] = minw
        s = sum(widths)
        widths = [w * CONTENT_W / s for w in widths]

        self.set_font("bv", size=8.9)
        approx = 0
        for r in parsed:
            approx += 5.4 + 1.6
        self._ensure(min(approx, 60))

        head_style = FontFace(emphasis="BOLD", color=(255, 255, 255),
                              fill_color=BRAND, size_pt=8.6)
        try:
            with self.table(col_widths=tuple(widths),
                            text_align=("CENTER",) + ("LEFT",) * (ncol - 1),
                            headings_style=head_style,
                            line_height=5.2,
                            padding=(1.5, 2.2),
                            borders_layout="ALL",
                            cell_fill_color=(255, 255, 255),
                            cell_fill_mode="ROWS",
                            alternate_row_fill=((245, 247, 251), (255, 255, 255)),
                            ) as tbl:
                row = tbl.row()
                for c in header:
                    row.cell(c)
                for r in body:
                    row = tbl.row()
                    for c in r:
                        row.cell(c)
        except Exception:
            # ultra-simple fallback
            self.set_font("bvsb", size=8.8)
            for r in parsed:
                self.multi_cell(CONTENT_W, 5.0, "  ".join(r), markdown=True,
                                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*INK)
        self.ln(2.6)

    def _question(self, text):
        self._ensure(20)
        self.ln(1.6)
        y0 = self.get_y()
        self.set_font("bvsb", size=9.9)
        self.set_text_color(*INK)
        self.set_fill_color(*BRAND_L)
        self.multi_cell(CONTENT_W, 5.6, text, align="J", markdown=True,
                        fill=True, padding=(2.0, 2.6),
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y1 = self.get_y()
        self._bar(y0, y1, BRAND_MID)
        self.ln(1.2)

    def _opt(self, text):
        self._ensure(8)
        self.set_font("bv", size=9.7)
        self.set_text_color(*INK)
        self.set_x(L_MARGIN + 6)
        self.multi_cell(CONTENT_W - 6, 5.4, text, align="J", markdown=True,
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(self.get_y() + 0.5)

    def _answer(self, text):
        self._ensure(14)
        self.ln(1.0)
        y0 = self.get_y()
        self.set_font("bvsb", size=9.7)
        self.set_text_color(*GREEN)
        self.set_fill_color(*GREEN_L)
        self.multi_cell(CONTENT_W, 5.5, text, align="J", markdown=True,
                        fill=True, padding=(1.9, 2.6),
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y1 = self.get_y()
        self._bar(y0, y1, GREEN)
        self.ln(2.0)

    def _exp(self, text):
        self.set_font("bv", size=9.3)
        self.set_text_color(*INK_SOFT)
        x = L_MARGIN + 6
        y0 = self.get_y()
        self.set_xy(x, y0)
        self.multi_cell(CONTENT_W - 6, 5.1, text, align="J", markdown=True,
                        padding=(1.4, 2.4),
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*INK)
        self.set_y(self.get_y() + 0.4)

    def _sol(self, text):
        self.set_font("bv", size=9.7)
        self.set_text_color(*INK)
        x = L_MARGIN + 6
        y0 = self.get_y()
        self.set_xy(x, y0)
        self.multi_cell(CONTENT_W - 6, 5.4, text, align="J", markdown=True,
                        padding=(1.5, 2.6),
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self._bar(y0, self.get_y(), BRAND_MID, w=0.9, x=x)
        self.set_y(self.get_y() + 0.6)


# --------------------------------------------------------------------------
def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    content_dir, out_path = sys.argv[1], sys.argv[2]

    files = sorted(f for f in os.listdir(content_dir) if f.endswith(".md"))
    all_lines = []
    for f in files:
        with open(os.path.join(content_dir, f), encoding="utf-8") as fh:
            all_lines.extend(fh.readlines())
    blocks = parse(all_lines)

    # Pass 1: discover page numbers for the TOC
    meta = [("Hình thức", "70 % trắc nghiệm + 30 % tự luận"),
            ("Thời gian làm bài", "50 phút"),
            ("Cấu trúc", "Phần I (18 câu) · Phần II (2 câu × 4 ý) · Phần III (2 câu) · Phần IV (3 câu)"),
            ("Phạm vi kiến thức", "Chủ đề 1 & 2 – SGK Vật lí 10 (Kết nối tri thức)"),
            ("Chuẩn đầu ra", "Nhận biết · Thông hiểu · Vận dụng")]
    probe = Doc(collect_toc=True)
    probe.cover(meta)
    probe.render(blocks)
    entries = [(k, l, p + 1) for (k, l, p) in probe.toc_entries]  # +1 for the TOC page

    # Pass 2: real document with TOC
    doc = Doc(collect_toc=False)
    doc.toc_entries = entries
    doc.cover(meta)
    doc.toc()
    doc.render(blocks)
    doc.output(out_path)
    print(f"OK -> {out_path}  ({len(doc.pages)} pages, {len(blocks)} blocks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
