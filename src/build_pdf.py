# -*- coding: utf-8 -*-
"""Lắp ráp đề cương PDF."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import content_exam as exam
import content_front as front
import content_theory as th
import content_toolkit as tk
from style import Doc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "De_cuong_on_tap_GK1_Vat_li_10_2026-2027.pdf")


def story():
    s = []
    s += front.cover()
    s += front.how_to_use()
    s += front.roadmap()
    s += exam.part_a()
    for fn in (th.b1, th.b2, th.b3, th.b4, th.b5, th.b6, th.b7, th.b8, th.b9, th.b10):
        s += fn()
    s += tk.banner_c()
    s += tk.mindmap()
    s += exam.part_d()
    s += exam.part_e()
    s += tk.traps()
    s += tk.checklist()
    return s


def main():
    import pymupdf
    import style

    style.BANNERS.clear()
    doc = Doc(OUT)
    doc.build_twice(story)
    print("pages:", doc.total_pages, "->", OUT)

    # tạo bookmark + metadata
    toc = [[1, "Bìa & mục lục", 1]]
    seen = set()
    for kicker, title, page in style.BANNERS:
        title = title.replace("&amp;", "&")
        key = (kicker, title)
        if key in seen:
            continue
        seen.add(key)
        toc.append([1, "%s – %s" % (kicker, title), page])
    pdf = pymupdf.open(OUT)
    toc = [t for t in toc if t[2] <= pdf.page_count]
    pdf.set_toc(toc)
    pdf.set_metadata({
        "title": "Đề cương ôn tập Giữa học kì I – Vật lí 10 (2026–2027)",
        "author": "Biên soạn theo Ma trận đặc tả KTGK I L10 – 2026",
        "subject": "Ôn tập Vật lí 10 – Giữa học kì I: lý thuyết, công thức, đề minh họa và đáp án",
        "keywords": "Vật lí 10, giữa kì 1, đề cương, ma trận đặc tả, động học, rơi tự do",
    })
    pdf.saveIncr()
    pdf.close()
    print("bookmarks:", len(toc))


if __name__ == "__main__":
    main()
