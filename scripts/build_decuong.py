# -*- coding: utf-8 -*-
"""Build the PDF revision outline for the Grade-10 Physics mid-term exam."""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Frame, NextPageTemplate, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)
from reportlab.pdfgen import canvas as rl_canvas

from decuong.style import (
    ACCENT, BG_SOFT, CONTENT_W, FONT, FONT_B, INK, LINE, MARGIN_B, MARGIN_L,
    MARGIN_R, MARGIN_T, MUTED, PAGE_H, PAGE_W, P, PRIMARY, PRIMARY_D, PRIMARY_L,
    S, SPC, box, bullets, data_table, formula, numbered, register_fonts,
)
from decuong.part_a import part_a
from decuong.part_b1 import bai1, bai2, bai3, bai4, bai5
from decuong.part_b2 import bai10, bai6, bai7, bai8, bai9, tong_ket_b
from decuong.part_c import part_c, part_c2
from decuong.part_d import part_d, part_d2
from decuong.part_e import part_e
from decuong.part_f import part_f
from decuong.appendix import appendix

OUT = os.path.join(os.path.dirname(HERE), "DE-CUONG-ON-TAP-GK1-VAT-LI-10.pdf")
TITLE = "Đề cương ôn tập giữa kì I – Vật lí 10 – Năm học 2026–2027"


# --------------------------------------------------------------------------- #
def draw_cover(c: rl_canvas.Canvas, doc):
    W, H = PAGE_W, PAGE_H
    c.saveState()
    c.setFillColor(colors.white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    band_h = 330
    c.setFillColor(PRIMARY)
    c.rect(0, H - band_h, W, band_h, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#12597D"))
    c.circle(W - 12, H - 18, 120, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#0B3D57"))
    c.circle(W + 40, H - 246, 96, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.rect(0, H - band_h - 5, W, 5, fill=1, stroke=0)

    x = 46
    c.setFillColor(colors.HexColor("#9CC7DC"))
    c.setFont(FONT_B, 8.6)
    c.drawString(x, H - 62, "T À I   L I Ệ U   T Ự   H Ọ C   ·   K H Ố I   1 0")

    c.setFillColor(colors.white)
    c.setFont(FONT_B, 39)
    c.drawString(x, H - 122, "ĐỀ CƯƠNG ÔN TẬP")
    c.setFillColor(colors.HexColor("#F2B455"))
    c.setFont(FONT_B, 25)
    c.drawString(x, H - 162, "GIỮA KÌ I – VẬT LÍ 10")
    c.setFillColor(colors.HexColor("#D8E9F2"))
    c.setFont(FONT, 12)
    c.drawString(x, H - 190, "Năm học 2026 – 2027  ·  Thời gian làm bài 50 phút  ·  70% TN + 30% TL")

    # chips
    chips = ["10 bài học", "18 câu trắc nghiệm", "2 câu đúng – sai", "Đề mô phỏng + đáp án"]
    cx = x
    cy = H - 238
    for label in chips:
        w = pdfmetrics.stringWidth(label, FONT_B, 8.4) + 20
        c.setFillColor(colors.HexColor("#155A7C"))
        c.roundRect(cx, cy, w, 21, 10.5, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(FONT_B, 8.4)
        c.drawString(cx + 10, cy + 6.6, label)
        cx += w + 8

    # "inside" block
    y = H - 380
    c.setFillColor(PRIMARY)
    c.setFont(FONT_B, 10)
    c.drawString(x, y, "TRONG TÀI LIỆU NÀY CÓ GÌ?")
    c.setStrokeColor(ACCENT)
    c.setLineWidth(2)
    c.line(x, y - 7, x + 42, y - 7)

    items = [
        ("01", "Ma trận & bản đặc tả được “dịch” thành kế hoạch ôn 7 ngày"),
        ("02", "Lý thuyết 10 bài: bảng so sánh, công thức, mẹo nhớ, bẫy thường gặp"),
        ("03", "Sổ tay công thức và kỹ năng đọc đồ thị – tính sai số"),
        ("04", "Đề mô phỏng đúng cấu trúc + đáp án và lời giải chi tiết từng câu"),
        ("05", "30 câu trắc nghiệm và 8 bài tự luận tự luyện kèm đáp số"),
        ("06", "Checklist “đã thuộc bài” và 10 lỗi làm mất điểm oan"),
    ]
    y -= 26
    for num, text in items:
        c.setFillColor(ACCENT)
        c.setFont(FONT_B, 9)
        c.drawString(x, y, num)
        c.setFillColor(INK)
        c.setFont(FONT, 10)
        c.drawString(x + 26, y, text)
        c.setStrokeColor(colors.HexColor("#E7EEF3"))
        c.setLineWidth(0.6)
        c.line(x, y - 7, W - 46, y - 7)
        y -= 25

    # formula card
    card_y = 96
    card_h = 110
    c.setFillColor(BG_SOFT)
    c.roundRect(x, card_y, W - 2 * x, card_h, 8, fill=1, stroke=0)
    c.setFillColor(PRIMARY)
    c.rect(x, card_y, 4, card_h, fill=1, stroke=0)
    c.setFillColor(PRIMARY)
    c.setFont(FONT_B, 8.6)
    c.drawString(x + 16, card_y + card_h - 20, "BA CÔNG THỨC XƯƠNG SỐNG CỦA CHƯƠNG")
    c.setFillColor(INK)
    c.setFont(FONT_B, 13)
    c.drawString(x + 16, card_y + 54, "v = v₀ + a·t")
    c.drawString(x + 150, card_y + 54, "s = v₀·t + ½·a·t²")
    c.drawString(x + 300, card_y + 54, "v² − v₀² = 2·a·s")
    c.setFillColor(MUTED)
    c.setFont(FONT, 8.6)
    c.drawString(x + 16, card_y + 26,
                 "Rơi tự do: v = g·t   ·   s = ½·g·t²   ·   v² = 2·g·s   ·   t = √(2s/g)")

    # footer note
    c.setFillColor(MUTED)
    c.setFont(FONT, 8)
    c.drawString(x, 56, "Biên soạn bám sát: “MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I – MÔN VẬT LÍ LỚP 10”")
    c.drawString(x, 42, "Năm học 2026 – 2027 · Hình thức: 70% trắc nghiệm + 30% tự luận · Thời gian: 50 phút")
    c.setFillColor(PRIMARY)
    c.setFont(FONT_B, 8)
    c.drawRightString(W - 46, 56, "de-cuong-vat-li-10")
    c.restoreState()


def draw_header_footer(c: rl_canvas.Canvas, doc):
    W, H = PAGE_W, PAGE_H
    c.saveState()
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(MARGIN_L, H - 40, W - MARGIN_R, H - 40)
    c.setFont(FONT, 7.4)
    c.setFillColor(MUTED)
    c.drawString(MARGIN_L, H - 33, "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I  ·  VẬT LÍ 10")
    c.drawRightString(W - MARGIN_R, H - 33, "Năm học 2026 – 2027")
    c.setFillColor(PRIMARY)
    c.rect(MARGIN_L, H - 37.6, 26, 2.2, fill=1, stroke=0)

    c.setStrokeColor(LINE)
    c.line(MARGIN_L, 34, W - MARGIN_R, 34)
    c.setFont(FONT, 7.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN_L, 22, "Biên soạn từ ma trận & bản đặc tả đề kiểm tra giữa kì I – Vật lí 10")
    c.restoreState()


class NumberedCanvas(rl_canvas.Canvas):
    def __init__(self, *args, **kwargs):
        rl_canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.setFont(FONT_B, 8)
                self.setFillColor(PRIMARY)
                self.drawRightString(PAGE_W - MARGIN_R, 22, f"Trang {self._pageNumber} / {total}")
            rl_canvas.Canvas.showPage(self)
        rl_canvas.Canvas.save(self)


class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        BaseDocTemplate.__init__(self, fn, **kw)
        self._toc_idx = 0
        self.collected = []
        frame_cover = Frame(0, 0, PAGE_W, PAGE_H, id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        frame_body = Frame(
            MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B, id="body",
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_cover], onPage=draw_cover),
            PageTemplate(id="body", frames=[frame_body], onPage=draw_header_footer),
        ])

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        name = flowable.style.name
        if name == "h1":
            level = 0
        elif name in ("lesson", "h2"):
            level = 1
        else:
            return
        text = flowable.getPlainText()
        self._toc_idx += 1
        key = f"toc{self._toc_idx}"
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=False)
        self.collected.append((level, text, self.page, key))


SKIP_TOC = {"Sáu phần của tài liệu", "Mục lục chi tiết",
            "Ký hiệu dùng trong tài liệu", "Bảng tra nhanh: đề hỏi gì – mở trang nào",
            "Bảng “mỗi bài một dòng” – dùng để tự kiểm tra chéo"}

TOC_LABEL = {
    "PHẦN A · HIỂU ĐỀ ĐỂ ÔN ĐÚNG TRỌNG TÂM": "PHẦN A · Hiểu đề – ôn đúng trọng tâm",
    "PHẦN B · LÝ THUYẾT TRỌNG TÂM 10 BÀI": "PHẦN B · Lý thuyết trọng tâm 10 bài",
    "PHẦN C · SỔ TAY CÔNG THỨC & KỸ NĂNG": "PHẦN C · Sổ tay công thức & kỹ năng",
    "PHẦN D · ĐỀ THI MÔ PHỎNG GIỮA KÌ I": "PHẦN D · Đề thi mô phỏng + lời giải",
    "PHẦN E · NGÂN HÀNG 30 CÂU TỰ LUYỆN THEO BÀI": "PHẦN E · 30 câu tự luyện theo bài",
    "PHẦN F · CHECKLIST “ĐÃ THUỘC BÀI” & LỖI CẦN TRÁNH": "PHẦN F · Checklist & lỗi cần tránh",
    "SƠ ĐỒ TƯ DUY TỔNG KẾT CHƯƠNG II – ĐỘNG HỌC": "Sơ đồ tư duy tổng kết Chương II",
    "PHẦN II. TRẮC NGHIỆM ĐÚNG – SAI (2 câu, mỗi câu 4 ý)": "Phần II. Trắc nghiệm đúng – sai (8 ý)",
    "PHẦN III. TỰ LUẬN NGẮN (2 câu)": "Phần III. Tự luận ngắn (2 câu)",
    "PHẦN IV. TỰ LUẬN VẬN DỤNG (3 ý)": "Phần IV. Tự luận vận dụng (3 ý)",
    "PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (18 câu)": "Phần I. Trắc nghiệm (18 câu)",
    "C7. 12 câu đúng – sai “kinh điển” (tự trả lời trước khi xem đáp án)": "C7. 12 câu đúng – sai “kinh điển”",
    "BÀI 2 · Các quy tắc an toàn trong phòng thực hành Vật lí": "BÀI 2 · Quy tắc an toàn phòng thực hành",
    "BÀI 3 · Thực hành tính sai số trong phép đo. Ghi kết quả đo": "BÀI 3 · Sai số phép đo – ghi kết quả",
    "BÀI 6 · Thực hành: Đo tốc độ của vật chuyển động": "BÀI 6 · Thực hành đo tốc độ",
    "PHẦN E2 · 8 BÀI TỰ LUẬN TỰ LUYỆN": "E2. 8 bài tự luận tự luyện",
}


def toc_block(entries):
    """Two independent two-column tables of contents placed side by side."""
    rows = [(lvl, TOC_LABEL.get(t, t), pg) for lvl, t, pg, _ in entries
            if not t.startswith("MỤC LỤC") and t not in SKIP_TOC]
    if not rows:
        return []

    def weight(r):
        kind, text, _ = r
        return len(text) * (1.0 if kind == 0 else 0.86) + (14 if kind == 0 else 0)

    total = sum(weight(r) for r in rows)
    acc, cut = 0.0, len(rows)
    for i, r in enumerate(rows):
        acc += weight(r)
        if acc >= total / 2:
            cut = i + 1
            break
    while cut < len(rows) and rows[cut][0] != 0:
        cut += 1
    left, right = rows[:cut], rows[cut:]

    def build(cells, width):
        data, cmds = [], [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 1.3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.3),
            ("ALIGN", (1, 0), (1, -1), "RIGHT"),
            ("VALIGN", (1, 0), (1, -1), "BOTTOM"),
        ]
        for i, (kind, text, page) in enumerate(cells):
            if kind == 0:
                data.append([Paragraph(f'<b>{text}</b>', S["toc1"]),
                             Paragraph(str(page), S["toc1_pg"])])
                cmds.append(("LINEBELOW", (0, i), (1, i), 0.7, PRIMARY_L))
                cmds.append(("TOPPADDING", (0, i), (1, i), 7 if i else 1))
            else:
                data.append([Paragraph(text, S["toc2"]),
                             Paragraph(str(page), S["toc_pg"])])
        t = Table(data, colWidths=[width - 24, 24], hAlign="LEFT")
        t.setStyle(TableStyle(cmds))
        return t

    w = (CONTENT_W - 20) / 2
    outer = Table([[build(left, w), "", build(right, w)]],
                  colWidths=[w, 20, w], hAlign="LEFT")
    outer.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return [outer]


def part_index():
    """Six-part overview on the contents page."""
    items = [
        ("A", "Hiểu đề: ma trận, thang điểm, lộ trình 7 ngày", "#0E4C6B"),
        ("B", "Lý thuyết trọng tâm 10 bài + sơ đồ tư duy", "#1F5F99"),
        ("C", "Sổ tay công thức, kỹ năng, 6 dạng bài", "#1D6B4C"),
        ("D", "Đề mô phỏng 50 phút + đáp án, lời giải", "#A8332A"),
        ("E", "30 câu trắc nghiệm + 8 bài tự luận", "#5B3E96"),
        ("F", "Checklist thuộc bài + 10 lỗi thường gặp", "#B87410"),
    ]
    cells = []
    for tag, desc, col in items[:3]:
        cells.append([Paragraph(f'<font color="{col}"><b>{tag}</b></font>', S["part_tag"]),
                      Paragraph(desc, S["part_desc"])])
    cells2 = []
    for tag, desc, col in items[3:]:
        cells2.append([Paragraph(f'<font color="{col}"><b>{tag}</b></font>', S["part_tag"]),
                       Paragraph(desc, S["part_desc"])])

    w1, w2 = CONTENT_W / 2 - 8, CONTENT_W / 2 - 8
    left = Table([[c[0], c[1]] for c in cells], colWidths=[20, w1 - 20], hAlign="LEFT")
    right = Table([[c[0], c[1]] for c in cells2], colWidths=[20, w2 - 20], hAlign="LEFT")
    style = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#E7EEF3")),
    ]
    left.setStyle(TableStyle(style))
    right.setStyle(TableStyle(style))
    outer = Table([[left, "", right]], colWidths=[w1, 16, w2], hAlign="LEFT")
    outer.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return outer


def legend_block():
    """Explain the symbol system used throughout the document."""
    from decuong.style import ACCENT, BG_AMBER, BG_BLUE, BG_GREEN, BG_PURPLE, BG_RED, RED, GREEN, PURPLE
    items = [
        ("◆", PRIMARY_L, BG_BLUE, "Định nghĩa / kiến thức chuẩn – phải phát biểu lại được"),
        ("★", ACCENT, BG_AMBER, "Mẹo nhớ – câu “thần chú” để tái hiện kiến thức"),
        ("⚠", RED, BG_RED, "Bẫy thường gặp – chỗ đề hay gài, đọc trước khi thi"),
        ("▶", GREEN, BG_GREEN, "Ví dụ mẫu – có lời giải từng bước"),
        ("✎", PURPLE, BG_PURPLE, "Ghi chú – mở rộng, lưu ý khi làm bài"),
    ]
    rows = []
    for icon, col, bg, text in items:
        rows.append([Paragraph(f'<font color="{col.hexval()}" size="11"><b>{icon}</b></font>', S["toc2"]),
                     Paragraph(text, S["part_desc"])])
    t = Table(rows, colWidths=[24, CONTENT_W / 2 - 24], hAlign="LEFT")
    style = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("LEFTPADDING", (0, 0), (-1, -1), 2),
             ("RIGHTPADDING", (0, 0), (-1, -1), 2),
             ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    t.setStyle(TableStyle(style))

    tags = [
        ("[Bài 9]", "bài học tương ứng của chương trình"),
        ("(Biết)", "chỉ cần nhận ra, phát biểu lại"),
        ("(Hiểu)", "cần giải thích, phân biệt, so sánh"),
        ("(Vận dụng)", "cần tính toán, trình bày lời giải"),
        ("Đ / S", "Đúng / Sai – dạng câu hỏi phần II"),
    ]
    rows2 = []
    for tg, text in tags:
        rows2.append([Paragraph(f'<font color="#8A6A2F"><b>{tg}</b></font>', S["toc2"]),
                      Paragraph(text, S["part_desc"])])
    t2 = Table(rows2, colWidths=[62, CONTENT_W / 2 - 62 - 8], hAlign="LEFT")
    t2.setStyle(TableStyle(style))

    outer = Table([["", t, "", "", t2, ""]],
                  colWidths=[0, CONTENT_W / 2 - 8, 16, 0, CONTENT_W / 2 - 16, 0],
                  hAlign="LEFT")
    outer.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return outer


def quick_index(entries):
    """Where to look for each exam part – page numbers resolved from the real layout."""
    pages = {}
    for lvl, title, pg, key in entries:
        pages.setdefault(title, pg)
    b_start = pages.get("PHẦN B · LÝ THUYẾT TRỌNG TÂM 10 BÀI", "?")
    b_end = pages.get("PHẦN C · SỔ TAY CÔNG THỨC & KỸ NĂNG", "?")
    try:
        b_range = f"{b_start} – {int(b_end) - 1}"
    except (TypeError, ValueError):
        b_range = f"{b_start} – {b_end}"
    rows = [
        ["Câu lý thuyết về định nghĩa, quy tắc, đơn vị", "Phần B – bài tương ứng", b_range],
        ["Câu phân biệt hai khái niệm (tốc độ/vận tốc, a và v…)",
         "C5. Những cặp khái niệm dễ nhầm", str(pages.get("C5. Những cặp khái niệm dễ nhầm", "?"))],
        ["Câu hỏi “công thức nào đúng”", "C1. Toàn bộ công thức trong học kì I",
         str(pages.get("C1. Toàn bộ công thức trong học kì I", "?"))],
        ["Câu đọc – vẽ đồ thị",
         "Bài 7 + C4. Kỹ năng đọc – vẽ đồ thị",
         f'{pages.get("BÀI 7 · Đồ thị độ dịch chuyển – thời gian", "?")}, '
         f'{pages.get("C4. Kỹ năng đọc – vẽ đồ thị", "?")}'],
        ["Câu đúng/sai (phần II)", "C7. 12 câu đúng – sai “kinh điển”",
         str(pages.get("C7. 12 câu đúng – sai “kinh điển” (tự trả lời trước khi xem đáp án)", "?"))],
        ["Bài toán cộng vận tốc, hãm phanh, rơi tự do", "C6. Sáu dạng bài vận dụng",
         str(pages.get("C6. Sáu dạng bài vận dụng phải làm được", "?"))],
        ["Câu hỏi thực hành, cổng quang điện", "Bài 6 + Bài 3",
         f'{pages.get("BÀI 6 · Thực hành: Đo tốc độ của vật chuyển động", "?")}, '
         f'{pages.get("BÀI 3 · Thực hành tính sai số trong phép đo. Ghi kết quả đo", "?")}'],
        ["Cần tự kiểm tra trước khi thi", "F1. Checklist 30 mục",
         str(pages.get("F1. Checklist 30 mục", "?"))],
    ]
    return data_table(
        ["Khi đề hỏi…", "Mở ngay", "Trang"],
        rows, [230, 205, 76], align=["LEFT", "LEFT", "CENTER"], font="tbl_small",
    )


def make_story(toc_entries=None):
    story = []
    story.append(NextPageTemplate("body"))
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # ---------------- page 2 : how to use + TOC ----------------
    story.append(P("MỤC LỤC & CÁCH DÙNG TÀI LIỆU", "h1"))
    story.append(box("Dùng tài liệu này thế nào cho hiệu quả?", [
        P("<b>Bước 1.</b> Đọc <b>Phần A</b> (trang kế tiếp) để biết bài nào ra nhiều câu, phần nào chiếm nhiều điểm.", "box_item"),
        P("<b>Bước 2.</b> Học <b>Phần B</b> theo đúng thứ tự 10 bài; mỗi bài chỉ cần 15 – 20 phút: đọc lý thuyết → "
          "tự trả lời câu hỏi trong hộp “Bẫy thường gặp” → làm ví dụ mẫu.", "box_item"),
        P("<b>Bước 3.</b> Trước ngày thi 1 – 2 hôm, học thuộc <b>Phần C</b> (sổ tay công thức).", "box_item"),
        P("<b>Bước 4.</b> Bấm đồng hồ 50 phút làm trọn <b>Phần D</b>, tự chấm bằng đáp án; sai câu nào quay lại bài đó.", "box_item"),
        P("<b>Bước 5.</b> Làm <b>Phần E</b> để phủ kín kiến thức và <b>Phần F</b> để tự kiểm tra lần cuối.", "box_item"),
    ], "def"))
    story.append(SPC(6))
    story.append(P("Sáu phần của tài liệu", "h2"))
    story.append(part_index())
    story.append(SPC(8))
    story.append(P("Ký hiệu dùng trong tài liệu", "h2"))
    story.append(legend_block())
    story.append(PageBreak())

    # ---------------- page 3 : detailed contents ----------------
    story.append(P("MỤC LỤC CHI TIẾT", "h1"))
    story.append(SPC(4))
    story += toc_block(toc_entries)
    story.append(SPC(12))
    story.append(P("Bảng tra nhanh: đề hỏi gì – mở trang nào", "h2"))
    story.append(quick_index(toc_entries))
    story.append(PageBreak())

    # ---------------- content ----------------
    story += part_a()

    story.append(PageBreak())
    story.append(P("PHẦN B · LÝ THUYẾT TRỌNG TÂM 10 BÀI", "h1"))
    story.append(P("Mỗi bài được trình bày theo cùng một cấu trúc: <b>đề hỏi gì → kiến thức cốt lõi → công thức → "
                   "ví dụ mẫu → mẹo nhớ → bẫy thường gặp</b>. Những chỗ được tô màu là những chỗ đề hay “gài” nhất.", "body"))
    story.append(SPC(4))
    for fn in (bai1, bai2, bai3, bai4, bai5, bai6, bai7, bai8, bai9, bai10, tong_ket_b):
        story += fn()

    story.append(PageBreak())
    story += part_c()
    story += part_c2()
    story.append(PageBreak())
    story += part_d()
    story.append(PageBreak())
    story += part_e()
    story.append(PageBreak())
    story += part_f()
    story.append(PageBreak())
    story += appendix()
    return story


def run_pass(entries, out_path):
    doc = Doc(
        out_path, pagesize=A4,
        leftMargin=MARGIN_L, rightMargin=MARGIN_R, topMargin=MARGIN_T, bottomMargin=MARGIN_B,
        title=TITLE, subject="Ôn tập giữa kì I môn Vật lí lớp 10",
        author="Đề cương biên soạn tự động", creator="reportlab",
    )
    doc.build(make_story(entries), canvasmaker=NumberedCanvas)
    return doc.collected


def build():
    register_fonts()
    tmp = os.path.join("/tmp", "decuong_pass.pdf")
    entries = []
    for _ in range(4):
        new = run_pass(entries, tmp)
        if new == entries:
            break
        entries = new
    run_pass(entries, OUT)
    print("Wrote", OUT, "with", len(entries), "TOC entries")


if __name__ == "__main__":
    build()
