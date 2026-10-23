# -*- coding: utf-8 -*-
"""build.py — lắp ráp tài liệu."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fpdf.enums import XPos, YPos
from engine import (DeCuong, MARGIN, CONTENT_W, W, NAVY, NAVY_D, BLUE, BLUE_L, AMBER,
                    AMBER_L, GREEN, GREEN_L, RED, RED_L, INK, GREY, GREY_L, WHITE, LINE)
from content_a import blocks_a
from content_b import blocks_b
from content_c import blocks_c

BLOCKS = blocks_a() + blocks_b() + blocks_c()


# ------------------------------------------------------------------ cover
def cover(doc):
    doc.add_page()
    # nền trên
    doc.set_fill_color(*NAVY)
    doc.rect(0, 0, W, 176, style="F")
    doc.set_fill_color(*AMBER)
    doc.rect(0, 176, W, 2.2, style="F")

    doc.set_font("BVP", "B", 8.2)
    doc.set_text_color(150, 190, 220)
    doc.set_xy(MARGIN, 20)
    doc.cell(0, 5, "VẬT LÍ 10  ·  CHƯƠNG TRÌNH GDPT 2018  ·  NĂM HỌC 2026 – 2027")

    doc.set_draw_color(90, 140, 180)
    doc.set_line_width(0.4)
    doc.line(MARGIN, 30, MARGIN + 26, 30)

    doc.set_xy(MARGIN, 44)
    doc.set_font("BVP", "B", 15)
    doc.set_text_color(*AMBER)
    doc.cell(0, 9, "ĐỀ CƯƠNG ÔN TẬP")

    doc.set_xy(MARGIN, 56)
    doc.set_font("BVP", "B", 40)
    doc.set_text_color(*WHITE)
    doc.cell(0, 17, "GIỮA HỌC KÌ I")

    doc.set_xy(MARGIN, 78)
    doc.set_font("BVP", "", 18)
    doc.set_text_color(200, 222, 240)
    doc.cell(0, 10, "MÔN VẬT LÍ  ·  LỚP 10")

    doc.set_xy(MARGIN, 98)
    doc.set_font("BVP", "", 10.5)
    doc.set_text_color(170, 205, 232)
    doc.multi_cell(150, 6.0,
                   "Bám sát ma trận đặc tả của đề kiểm tra giữa học kì I — "
                   "hệ thống đầy đủ lý thuyết, công thức, mẹo nhớ, "
                   "đề minh hoạ và lời giải chi tiết cho cả 31 lượt hỏi.",
                   align="L")

    # hàng thẻ số liệu
    stats = [("10", "bài học"), ("31", "lượt hỏi"), ("50", "phút"), ("10", "điểm")]
    bx, by, bw, bh, gap = MARGIN, 128, 41.5, 30, 4.0
    for i, (num, lab) in enumerate(stats):
        x = bx + i * (bw + gap)
        doc.set_fill_color(28, 72, 112)
        doc.rect(x, by, bw, bh, style="F")
        doc.set_fill_color(*AMBER)
        doc.rect(x, by, bw, 1.4, style="F")
        doc.set_xy(x, by + 6.5)
        doc.set_font("BVP", "B", 20)
        doc.set_text_color(*WHITE)
        doc.cell(bw, 10, num, align="C")
        doc.set_xy(x, by + 18.5)
        doc.set_font("BVP", "", 8.2)
        doc.set_text_color(170, 205, 232)
        doc.cell(bw, 5, lab, align="C")

    # khối dưới
    doc.set_y(190)
    doc.set_x(MARGIN)
    doc.set_font("BVP", "B", 9.5)
    doc.set_text_color(*NAVY)
    doc.cell(0, 6, "NỘI DUNG TÀI LIỆU")

    items = [
        ("Phần 0", "Giải mã ma trận: cấu trúc đề, thang điểm, trọng số từng bài, chiến lược 50 phút"),
        ("Phần 1", "Lý thuyết trọng tâm 10 bài — công thức, bảng so sánh, mẹo nhớ, bẫy thường gặp"),
        ("Phần 2", "Tổng hợp công thức một trang · sơ đồ tư duy · 15 bẫy · bảng đổi đơn vị"),
        ("Phần 3", "Đề minh hoạ bám đúng ma trận (18 TN + 8 ý Đ/S + 2 TLN + 2 tự luận)"),
        ("Phần 4", "Đáp án và lời giải chi tiết từng câu"),
    ]
    y = 198
    for tag, desc in items:
        doc.set_xy(MARGIN, y)
        doc.set_font("BVP", "B", 8.4)
        doc.set_text_color(*AMBER)
        doc.cell(17, 5.4, tag)
        doc.set_xy(MARGIN + 17, y)
        doc.set_font("BVP", "", 8.6)
        doc.set_text_color(*INK)
        doc.multi_cell(CONTENT_W - 17, 5.4, desc)
        y = max(y + 5.4, doc.get_y()) + 2.2

    doc.set_draw_color(*LINE)
    doc.set_line_width(0.3)
    doc.line(MARGIN, 264, W - MARGIN, 264)
    doc.set_xy(MARGIN, 267)
    doc.set_font("BVP", "", 7.8)
    doc.set_text_color(*GREY)
    doc.multi_cell(CONTENT_W, 4.6,
                   "Nguồn: “MA TRẬN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I – MÔN VẬT LÍ LỚP 10 – NĂM HỌC 2026–2027”. "
                   "Tài liệu biên soạn phục vụ ôn tập; đề minh hoạ bám sát ma trận gốc nhưng không phải đề thi chính thức.",
                   align="L")


# ------------------------------------------------------------------ toc
def toc_entries():
    out = []
    for kind, payload in BLOCKS:
        if kind == "h1":
            out.append((1, payload))
        elif kind == "h2":
            out.append((2, payload))
    return out


def toc(doc):
    doc.add_page()
    doc.set_xy(MARGIN, 22)
    doc.set_font("BVP", "B", 16)
    doc.set_text_color(*NAVY)
    doc.cell(0, 9, "MỤC LỤC")
    doc.set_fill_color(*AMBER)
    doc.rect(MARGIN, 34.5, 22, 1.6, style="F")
    y = 42

    for lvl, text in toc_entries():
        pg = doc.toc_pages.get(text, "")
        if lvl == 1:
            y += 3.2
            doc.set_xy(MARGIN, y)
            doc.set_font("BVP", "B", 9.6)
            doc.set_text_color(*NAVY)
            doc.cell(CONTENT_W - 12, 5.6, text)
            doc.set_text_color(*AMBER)
            doc.set_xy(MARGIN + CONTENT_W - 12, y)
            doc.cell(12, 5.6, str(pg), align="R")
            y += 5.6
            doc.set_draw_color(*LINE)
            doc.set_line_width(0.2)
            doc.line(MARGIN, y + 0.6, W - MARGIN, y + 0.6)
        else:
            y += 0.4
            doc.set_xy(MARGIN + 5, y)
            doc.set_font("BVP", "", 8.6)
            doc.set_text_color(*INK)
            doc.cell(CONTENT_W - 17, 5.2, text)
            doc.set_text_color(*GREY)
            doc.set_xy(MARGIN + CONTENT_W - 12, y)
            doc.cell(12, 5.2, str(pg), align="R")
            y += 5.2


# ------------------------------------------------------------------ blocks
def render_qa(doc, items):
    doc._ensure(16)
    doc.set_y(doc.get_y() + 1.0)
    doc.set_x(MARGIN)
    doc.set_font("BVP", "B", 7.6)
    doc.set_text_color(*GREEN)
    doc.cell(0, 4.4, "TỰ KIỂM TRA 60 GIÂY")
    doc.set_y(doc.get_y() + 5.0)
    for q, a in items:
        doc._ensure(12)
        y0 = doc.get_y()
        doc.set_xy(MARGIN + 0.5, y0)
        doc.set_font("BVP", "B", 8.6)
        doc.set_text_color(*AMBER)
        doc.cell(4.6, 4.9, "▸")
        doc.set_xy(MARGIN + 5.2, y0)
        doc.set_font("BVP", "B", 9.0)
        doc.set_text_color(*NAVY)
        doc.multi_cell(CONTENT_W - 5.2, 4.9, q, markdown=True,
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y1 = doc.get_y()
        doc.set_xy(MARGIN + 5.2, y1)
        doc.set_font("BVP", "", 9.0)
        doc.set_text_color(*INK)
        doc.multi_cell(CONTENT_W - 5.2, 4.9, "→ " + a, markdown=True,
                       new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        doc.set_y(doc.get_y() + 1.6)
    doc.set_y(doc.get_y() + 1.4)


def _badge(doc, n, y0, color=NAVY):
    doc.set_fill_color(*color)
    doc.ellipse(MARGIN, y0 + 0.4, 5.4, 5.4, style="F")
    doc.set_font("BVP", "B", 7.6)
    doc.set_text_color(*WHITE)
    doc.text(MARGIN + (2.7 - doc.get_string_width(str(n)) / 2), y0 + 4.2, str(n))
    doc.set_text_color(*INK)


def _tag(doc, text):
    doc.rich(text, size=7.2, lh=4.0, color=GREY, align="L", italic=True,
             x=MARGIN + 7.4, width=CONTENT_W - 7.4)
    doc.set_y(doc.get_y() + 1.2)


def render_mcq(doc, d):
    n_opts = len(d["opts"])
    doc._ensure(14 + n_opts * 6)
    y0 = doc.get_y()
    _badge(doc, d["n"], y0)
    doc.rich(d["stem"], size=9.3, lh=5.0, align="L", x=MARGIN + 7.4,
             width=CONTENT_W - 7.4)
    _tag(doc, d["tag"])
    for i, opt in enumerate(d["opts"]):
        doc._ensure(12)
        y = doc.get_y()
        doc.set_font("BVP", "B", 8.9)
        doc.set_text_color(*BLUE)
        doc.text(MARGIN + 9.0, doc._baseline(y, 4.9), "ABCD"[i] + ".")
        doc.rich(opt, size=9.0, lh=4.9, align="L", x=MARGIN + 14.2,
                 width=CONTENT_W - 14.2)
        doc.set_y(doc.get_y() + 0.5)
    doc.set_y(doc.get_y() + 2.6)


def render_tf(doc, d):
    doc._ensure(24)
    y0 = doc.get_y()
    _badge(doc, d["n"], y0)
    doc.rich(d["lead"], size=9.3, lh=5.0, align="J", x=MARGIN + 7.4,
             width=CONTENT_W - 7.4)
    _tag(doc, d["tag"])
    rows = [[lab + ")", txt, "☐ Đúng    ☐ Sai"] for lab, txt in d["items"]]
    doc.table(["Ý", "Phát biểu", "Lựa chọn"], rows, [6, 64, 30],
              size=8.7, align=["CENTER", "LEFT", "CENTER"])


def render_short(doc, d):
    doc._ensure(20)
    y0 = doc.get_y()
    _badge(doc, d["n"], y0)
    doc.rich(d["stem"], size=9.3, lh=5.0, align="J", x=MARGIN + 7.4,
             width=CONTENT_W - 7.4)
    _tag(doc, d["tag"])
    doc.set_y(doc.get_y() + 2.4)


def render_essay(doc, d):
    doc._ensure(40)
    y0 = doc.get_y()
    doc.set_fill_color(*AMBER)
    doc.rect(MARGIN, y0, 2.2, 11.0, style="F")
    doc.set_font("BVP", "B", 10.6)
    doc.set_text_color(*NAVY)
    doc.text(MARGIN + 5.5, y0 + 6.0, f"Câu {d['n']}")
    doc.set_font("BVP", "", 8.6)
    doc.set_text_color(*RED)
    doc.text(MARGIN + 22, y0 + 6.0, f"({d['points']})")
    doc.set_font("BVP", "I", 7.4)
    doc.set_text_color(*GREY)
    doc.text(MARGIN + 44, y0 + 6.0, d["tag"])
    doc.set_text_color(*INK)
    doc.set_y(y0 + 9.6)

    doc.rich(d["stem"], size=9.3, lh=5.0, align="J", x=MARGIN + 5.5,
             width=CONTENT_W - 5.5)
    doc.set_y(doc.get_y() + 1.2)
    for p in d["parts"]:
        doc._ensure(10)
        doc.rich(p, size=9.3, lh=5.0, align="J", x=MARGIN + 5.5,
                 width=CONTENT_W - 5.5)
    doc.set_y(doc.get_y() + 3.6)


TABLE_KEYS = {"size", "align", "head_color", "first_col_bold", "zebra"}


def render_block(doc, kind, payload):
    if kind == "h1":
        doc.h1(payload)
    elif kind == "h2":
        doc.h2(payload)
    elif kind == "h3":
        doc.h3(payload)
    elif kind == "p":
        text, kw = payload
        if len(text) > 1 and text.startswith("*") and text.endswith("*") and not text.startswith("**"):
            text = text[1:-1]
            kw = dict(kw)
            kw["italic"] = True
        doc.p(text, **kw)
    elif kind == "bullets":
        doc.bullets(payload)
    elif kind == "numbers":
        doc.numbers(payload)
    elif kind == "formula":
        doc.formula(payload["lines"], payload.get("title"))
    elif kind == "callout":
        doc.callout(*payload)
    elif kind == "table":
        head, rows, widths, kw = payload
        doc.table(head, rows, widths, **kw)
    elif kind == "qa":
        render_qa(doc, payload)
    elif kind == "mcq":
        render_mcq(doc, payload)
    elif kind == "tf":
        render_tf(doc, payload)
    elif kind == "short":
        render_short(doc, payload)
    elif kind == "essay":
        render_essay(doc, payload)
    else:
        raise ValueError("unknown block: " + kind)


# ------------------------------------------------------------------ build
def build(path, pages, collect):
    doc = DeCuong(toc_pages=pages)
    doc.collect = collect
    doc.alias_nb_pages()
    cover(doc)
    toc(doc)
    for kind, payload in BLOCKS:
        render_block(doc, kind, payload)
    doc.output(path)
    return doc


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/out.pdf"
    pages = {}
    d1 = build("/tmp/_pass1.pdf", pages, collect=True)
    print("pass1 pages:", d1.page_no(), "toc entries:", len(pages))
    d2 = build(out, pages, collect=False)
    print("final pages:", d2.page_no(), "->", out, os.path.getsize(out), "bytes")
