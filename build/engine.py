"""
engine.py — Renderer cho đề cương ôn tập (fpdf2).
Bộ layout riêng: đo – ngắt dòng – vẽ theo từng run (bold/italic), bảng tự tính chiều cao.
"""
import re
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from fontTools.ttLib import TTFont


def _cmap(name):
    return set(TTFont(FONT_DIR + "/" + name).getBestCmap().keys())

# ---------------------------------------------------------------- palette
NAVY = (17, 56, 92)
NAVY_D = (10, 36, 60)
BLUE = (29, 104, 154)
BLUE_L = (216, 233, 245)
AMBER = (222, 124, 22)
AMBER_L = (253, 240, 219)
GREEN = (26, 118, 76)
GREEN_L = (223, 242, 232)
RED = (176, 48, 42)
RED_L = (251, 231, 229)
INK = (32, 39, 46)
GREY = (112, 122, 132)
GREY_L = (244, 246, 248)
WHITE = (255, 255, 255)
LINE = (203, 213, 222)

MARGIN = 16.0
W = 210.0
CONTENT_W = W - 2 * MARGIN  # 178

FONT_DIR = __file__.rsplit("/", 1)[0] + "/fonts"

BVP_CMAP = _cmap("BeVietnamPro-Regular.ttf")
BVP_B_CMAP = _cmap("BeVietnamPro-Bold.ttf")
MONO_CMAP = _cmap("RobotoMono-Regular.ttf")

TOKEN_RE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*", re.S)
WORD_RE = re.compile(r"\S+")


class DeCuong(FPDF):
    def __init__(self, toc_pages=None):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.toc_pages = toc_pages if toc_pages is not None else {}
        self.collect = toc_pages is None
        self.set_margins(MARGIN, 20, MARGIN)
        self.set_auto_page_break(False)
        self.set_title("Đề cương ôn tập Giữa học kì I — Vật lí 10 (2026–2027)")
        self.set_author("Biên soạn bám sát ma trận đặc tả KTGK I")
        self.set_subject("Vật lí 10 — Động học — Ôn thi giữa học kì I")
        self.set_creator("Arena Agent")
        self._fonts()
        self.chapter = ""
        self._wc = {}
        self._base = "BVP"

    # =============================================================== fonts
    def _fonts(self):
        f = FONT_DIR
        self.add_font("BVP", "", f + "/BeVietnamPro-Regular.ttf")
        self.add_font("BVP", "B", f + "/BeVietnamPro-Bold.ttf")
        self.add_font("BVP", "I", f + "/BeVietnamPro-Italic.ttf")
        self.add_font("BVP", "BI", f + "/BeVietnamPro-BoldItalic.ttf")
        self.add_font("DJV", "", f + "/DejaVuSans.ttf")
        self.add_font("DJV", "B", f + "/DejaVuSans-Bold.ttf")
        self.add_font("MONO", "", f + "/RobotoMono-Regular.ttf")
        self.add_font("MONO", "B", f + "/RobotoMono-Bold.ttf")
        self.set_fallback_fonts(["DJV"], exact_match=False)

    def F(self, style="", size=9.5, family="BVP"):
        self.set_font(family, style, size)

    # ============================================================ measuring
    def segments(self, text, base="BVP"):
        """Tách text theo font thực sự chứa glyph: BVP / MONO / DJV."""
        if base == "MONO" and not all(ord(c) in MONO_CMAP for c in text):
            base = "BVP"
        out = []
        for ch in text:
            ok = (ord(ch) in MONO_CMAP) if base == "MONO" else (ord(ch) in BVP_CMAP)
            fam = base if ok else "DJV"
            if out and out[-1][1] == fam:
                out[-1][0] += ch
            else:
                out.append([ch, fam])
        return out

    def _w(self, text, style, size, base="BVP"):
        key = (text, style, size, base)
        v = self._wc.get(key)
        if v is None:
            v = 0.0
            for seg, fam in self.segments(text, base):
                self.set_font(fam, "" if fam == "DJV" else style, size)
                v += self.get_string_width(seg)
            self._wc[key] = v
        return v

    def _space(self, style, size):
        return self._w(" ", style, size)

    def parse(self, text):
        """'**bold** và *italic*' -> [(txt, style)]"""
        runs, pos = [], 0
        for m in TOKEN_RE.finditer(text):
            if m.start() > pos:
                runs.append((text[pos:m.start()], ""))
            if m.group(1) is not None:
                runs.append((m.group(1), "B"))
            else:
                runs.append((m.group(2), "I"))
            pos = m.end()
        if pos < len(text):
            runs.append((text[pos:], ""))
        return runs or [("", "")]

    def tokens(self, text, size, base="BVP", first_style=""):
        """[(word, style, width, glue)] — glue=True nghĩa là KHÔNG có dấu cách trước từ."""
        toks = []
        last = ""            # kí tự cuối cùng đã xử lí trong toàn bộ chuỗi

        def push(seg, st):
            nonlocal last
            if not seg:
                return
            st = (first_style + st) if first_style else st
            st = "".join(sorted(set(st), key="BI".index)) if st else ""
            for m in WORD_RE.finditer(seg):
                word = m.group(0)
                if m.start() > 0:
                    gap = seg[m.start() - 1].isspace()
                else:
                    gap = (last == "") or last.isspace()
                toks.append([word, st, self._w(word, st, size, base), not gap])
            last = seg[-1]

        pos = 0
        for m in TOKEN_RE.finditer(text):
            if m.start() > pos:
                push(text[pos:m.start()], "")
            if m.group(1) is not None:
                push(m.group(1), "B")
            else:
                push(m.group(2), "I")
            pos = m.end()
        if pos < len(text):
            push(text[pos:], "")
        return toks

    def layout(self, text, width, size, first_style="", base="BVP"):
        """Trả về list dòng; mỗi dòng là [(word, style, w, glue)]."""
        toks = self.tokens(text, size, base, first_style)
        if not toks:
            return [[]]

        lines, cur, curw = [], [], 0.0
        for word, st, w, glue in toks:
            spw = self._space(st, size)
            if w > width:  # tách từ quá dài
                if cur:
                    lines.append(cur)
                    cur, curw = [], 0.0
                buf, bw = "", 0.0
                for ch in word:
                    cw = self._w(ch, st, size, base)
                    if bw + cw > width and buf:
                        lines.append([(buf, st, bw, True)])
                        buf, bw = "", 0.0
                    buf += ch
                    bw += cw
                if buf:
                    cur, curw = [(buf, st, bw, True)], bw
                continue
            if not cur:
                cur, curw = [(word, st, w, True)], w
            elif glue:
                cur.append((word, st, w, False))
                curw += w
            elif curw + spw + w > width:
                lines.append(cur)
                cur, curw = [(word, st, w, True)], w
            else:
                cur.append((" ", st, spw, True))
                cur.append((word, st, w, True))
                curw += spw + w
        if cur:
            lines.append(cur)
        return lines

    # ============================================================== drawing
    def _baseline(self, y, lh):
        return y + lh * 0.735

    def draw_line(self, x, y, line, size, lh, width=None, align="L", justify=False, base="BVP"):
        if not line:
            return
        total = sum(t[2] for t in line)
        start = x
        extra_gap = 0.0
        if width:
            if align == "C":
                start = x + (width - total) / 2
            elif align == "R":
                start = x + width - total
            elif justify and align == "J":
                gaps = sum(1 for t in line if t[0] == " ")
                if gaps:
                    extra_gap = min((width - total) / gaps, 2.6)
        cx = start
        for tok in line:
            txt, st, w = tok[0], tok[1], tok[2]
            for seg, fam in self.segments(txt, base):
                self.set_font(fam, "" if fam == "DJV" else st, size)
                self.text(cx, self._baseline(y, lh), seg)
                cx += self.get_string_width(seg)
            cx += extra_gap if txt == " " else 0.0

    def rich(self, text, size=9.5, lh=5.0, color=INK, align="J", italic=False,
             x=None, width=None, indent=0.0, bullet=None, bullet_color=None,
             keep=2, style_prefix=""):
        """Vẽ một đoạn rich-text, tự động sang trang."""
        x = MARGIN + indent if x is None else x
        width = CONTENT_W - indent if width is None else width
        if italic:
            style_prefix = "I" + style_prefix
        lines = self.layout(text, width, size, first_style=style_prefix)
        self.set_text_color(*color)

        first = True
        i = 0
        bottom = self.h - 17
        while i < len(lines):
            if self.get_y() + lh > bottom:
                self.add_page()
            y = self.get_y()
            n_fit = max(1, int((bottom - y) // lh))
            chunk = lines[i:i + n_fit]
            n_total = len(lines)
            for j, line in enumerate(chunk):
                gi = i + j
                yy = y + j * lh
                if first and bullet is not None:
                    self.set_font("BVP", "B", size)
                    self.set_text_color(*(bullet_color or AMBER))
                    self.text(x - indent + 0.6, self._baseline(yy, lh), bullet)
                    self.set_text_color(*color)
                    first = False
                self.draw_line(x, yy, line, size, lh, width=width, align=align,
                               justify=(gi < n_total - 1))
            self.set_y(y + len(chunk) * lh)
            i += n_fit
            first = False

    # =============================================================== chrome
    def header(self):
        if self.page_no() == 1:
            return
        self.F("", 7.2)
        self.set_text_color(*GREY)
        self.set_xy(MARGIN, 8.5)
        self.cell(CONTENT_W * 0.62, 5, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  VẬT LÍ 10", align="L")
        self.set_xy(MARGIN + CONTENT_W * 0.62, 8.5)
        self.cell(CONTENT_W * 0.38, 5, "NĂM HỌC 2026 – 2027", align="R")
        self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        self.line(MARGIN, 14.2, W - MARGIN, 14.2)
        self.set_y(20)
        self.set_text_color(*INK)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        self.line(MARGIN, self.h - 14, W - MARGIN, self.h - 14)
        self.F("", 7.6)
        self.set_text_color(*GREY)
        self.set_xy(MARGIN, self.h - 12)
        self.cell(CONTENT_W / 2, 5, "Biên soạn bám sát ma trận đặc tả KTGK I – môn Vật lí 10", align="L")
        self.set_xy(MARGIN + CONTENT_W / 2, self.h - 12)
        self.cell(CONTENT_W / 2, 5, f"Trang {self.page_no()} / {{nb}}", align="R")

    # ============================================================== helpers
    def _ensure(self, h):
        if self.get_y() + h > self.h - 17:
            self.add_page()

    def save_toc(self, text):
        if self.collect and text not in self.toc_pages:
            self.toc_pages[text] = self.page_no()

    def space(self, h=3.0):
        self.set_y(self.get_y() + h)

    # ================================================================ heads
    def h1(self, text):
        self.add_page()
        self.save_toc(text)
        y = 19.0
        self.set_fill_color(*NAVY)
        self.rect(0, y - 1.5, W, 17.0, style="F")
        self.set_fill_color(*AMBER)
        self.rect(0, y - 1.5, 5.5, 17.0, style="F")
        self.set_xy(MARGIN, y + 3.0)
        self.F("B", 13.2)
        self.set_text_color(*WHITE)
        self.cell(0, 8, text)
        self.set_text_color(*INK)
        self.set_y(y + 21)

    def h2(self, text):
        self.save_toc(text)
        self._ensure(22)
        self.set_y(self.get_y() + 2.0)
        y = self.get_y()
        self.set_fill_color(*NAVY)
        self.rect(MARGIN, y + 1.2, 2.4, 7.4, style="F")
        self.rich(text, size=12.2, lh=6.4, color=NAVY, align="L", x=MARGIN + 6.4,
                  width=CONTENT_W - 6.4, style_prefix="B")
        self.set_draw_color(*LINE)
        self.set_line_width(0.25)
        self.line(MARGIN + 6, self.get_y() + 1.2, W - MARGIN, self.get_y() + 1.2)
        self.set_y(self.get_y() + 4.0)

    def h3(self, text):
        self._ensure(24)
        self.set_y(self.get_y() + 3.4)
        self.rich(text, size=9.8, lh=5.0, color=BLUE, align="L", style_prefix="B")
        self.set_y(self.get_y() + 1.4)

    # ================================================================= text
    def p(self, text, size=9.5, lh=5.05, color=INK, align="J", italic=False):
        self._ensure(lh * 2)
        self.rich(text, size=size, lh=lh, color=color, align=align, italic=italic)
        self.set_y(self.get_y() + 0.5)

    def bullets(self, items, size=9.5, lh=5.0, glyph="▪", gcolor=AMBER, indent=4.4):
        for it in items:
            self._ensure(lh * 2)
            y0 = self.get_y()
            self.set_font("DJV", "B", size)
            self.set_text_color(*gcolor)
            self.text(MARGIN + 0.8, self._baseline(y0, lh), glyph)
            self.set_y(y0)
            self.rich(it, size=size, lh=lh, x=MARGIN + indent, width=CONTENT_W - indent,
                      align="L")
            self.set_y(self.get_y() + 0.55)
        self.set_y(self.get_y() + 0.9)

    def numbers(self, items, size=9.5, lh=5.0):
        for i, it in enumerate(items, 1):
            self._ensure(lh * 2)
            y0 = self.get_y()
            self.set_font("BVP", "B", size)
            self.set_text_color(*BLUE)
            self.text(MARGIN + 4.6 - self.get_string_width(f"{i}."),
                      self._baseline(y0, lh), f"{i}.")
            self.set_y(y0)
            self.rich(it, size=size, lh=lh, x=MARGIN + 6.8, width=CONTENT_W - 6.8, align="L")
        self.set_y(self.get_y() + 0.9)

    # =============================================================== boxes
    def formula(self, lines, title=None):
        avail = CONTENT_W - 8
        size = 9.6
        widest = 0.0
        for ln in lines:
            self.set_font("MONO", "", size)
            widest = max(widest, self.get_string_width(ln))
        if widest > avail:
            size = max(7.0, size * avail / widest)
        lh = size * 0.56 + 1.6
        hgt = lh * len(lines) + 6.2 + (4.6 if title else 0.0)
        self._ensure(hgt + 2)
        y = self.get_y()
        self.set_fill_color(*BLUE_L)
        self.rect(MARGIN, y, CONTENT_W, hgt, style="F")
        self.set_fill_color(*BLUE)
        self.rect(MARGIN, y, 2.0, hgt, style="F")
        yy = y + 3.0
        if title:
            self.set_xy(MARGIN + 6.5, yy)
            self.F("B", 8.0)
            self.set_text_color(*BLUE)
            self.cell(0, 4.2, title.upper())
            yy += 4.6
        for ln in lines:
            self.set_text_color(*NAVY_D)
            cx = MARGIN + 6.5
            for seg, fam in self.segments(ln, "MONO"):
                self.set_font(fam, "", size)
                self.text(cx, yy + lh * 0.72, seg)
                cx += self.get_string_width(seg)
            yy += lh
        self.set_y(y + hgt + 2.2)
        self.set_text_color(*INK)

    def callout(self, kind, title, text):
        cfg = {
            "tip":  (GREEN, GREEN_L, "MẸO NHỚ"),
            "warn": (RED, RED_L, "CẨN THẬN – DỄ SAI"),
            "key":  (AMBER, AMBER_L, "ĐIỂM ĂN ĐIỂM"),
            "note": (BLUE, BLUE_L, "GHI NHỚ"),
        }[kind]
        col, bg, default = cfg
        title = title or default
        lines = self.layout(text, CONTENT_W - 12, 9.1)
        hgt = 7.4 + 4.8 * len(lines) + 1.6
        self._ensure(hgt + 2)
        y = self.get_y()
        self.set_fill_color(*bg)
        self.rect(MARGIN, y, CONTENT_W, hgt, style="F")
        self.set_fill_color(*col)
        self.rect(MARGIN, y, 2.0, hgt, style="F")
        self.set_xy(MARGIN + 6, y + 2.2)
        self.F("B", 7.8)
        self.set_text_color(*col)
        self.cell(0, 4.0, title)
        yy = y + 7.2
        for line in lines:
            self.draw_line(MARGIN + 6, yy, line, 9.1, 4.8, width=CONTENT_W - 12, align="J")
            yy += 4.8
        self.set_text_color(*INK)
        self.set_y(y + hgt + 2.2)

    # ============================================================== tables
    def table(self, head, rows, widths, size=8.4, align=None, head_color=NAVY,
              first_col_bold=False, zebra=True, pad=1.7, lh=None, head_size=None):
        total = sum(widths)
        cols = [w * CONTENT_W / total for w in widths]
        align = align or ["LEFT"] * len(cols)
        align = ["L" if a == "LEFT" else "C" if a == "CENTER" else "R" for a in align]
        lh = lh or size * 0.56
        hs = head_size or size
        bottom = self.h - 17

        def cell_lines(text, i, bold):
            style = "B" if (bold or (first_col_bold and i == 0)) else ""
            return self.layout(str(text), cols[i] - 2 * pad, size, first_style=style)

        head_lines = [self.layout(str(h), cols[i] - 2 * pad, hs, first_style="B")
                      for i, h in enumerate(head)]
        head_h = max(len(l) for l in head_lines) * lh + 2 * pad

        pref = []
        for r in rows:
            cl = [cell_lines(c, i, False) for i, c in enumerate(r)]
            hh = max(len(l) for l in cl) * lh + 2 * pad
            pref.append((cl, hh))

        def draw_head(y):
            self.set_fill_color(*head_color)
            self.rect(MARGIN, y, CONTENT_W, head_h, style="F")
            x = MARGIN
            for i, lines in enumerate(head_lines):
                yy = y + pad + (head_h - 2 * pad - len(lines) * lh) / 2
                for line in lines:
                    self.set_text_color(*WHITE)
                    self.draw_line(x + pad, yy, line, hs, lh,
                                   width=cols[i] - 2 * pad, align=align[i])
                    yy += lh
                x += cols[i]

        self._ensure(head_h + 14)
        y = self.get_y()
        draw_head(y)
        y += head_h

        for k, (cl, hh) in enumerate(pref):
            if y + hh > bottom:
                self.add_page()
                y = self.get_y()
                draw_head(y)
                y += head_h
            if zebra and k % 2 == 1:
                self.set_fill_color(*GREY_L)
                self.rect(MARGIN, y, CONTENT_W, hh, style="F")
            x = MARGIN
            for i, lines in enumerate(cl):
                yy = y + pad
                for line in lines:
                    self.set_text_color(*INK)
                    self.draw_line(x + pad, yy, line, size, lh,
                                   width=cols[i] - 2 * pad, align=align[i])
                    yy += lh
                x += cols[i]
            y += hh

        # kẻ khung
        self.set_draw_color(*LINE)
        self.set_line_width(0.2)
        self.rect(MARGIN, y - sum(h for _, h in pref) - head_h, CONTENT_W,
                  sum(h for _, h in pref) + head_h)
        self.set_y(y + 3.0)
        self.set_text_color(*INK)
