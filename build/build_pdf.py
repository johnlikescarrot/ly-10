# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doc_kit import *  # noqa
from reportlab.platypus import Spacer, NextPageTemplate, PageBreak
import content_front, content_theory1, content_theory2
import content_sheet, content_exam, content_key, content_plan

OUT = sys.argv[1] if len(sys.argv) > 1 else "De_cuong_on_tap_Giua_HKI_Vat_li_10_2026-2027.pdf"


def main():
    doc = StudyDoc(OUT)
    d = Doc()
    d.story.append(Spacer(1, 1))
    d.story.append(NextPageTemplate("body"))
    d.story.append(PageBreak())

    content_front.build(d)
    content_theory1.build(d)
    content_theory2.build(d)
    content_sheet.build(d)
    content_exam.build(d)
    content_key.build(d)
    content_plan.build(d)

    doc.multiBuild(d.story)
    print("built", OUT, "pages:", doc.page)


if __name__ == "__main__":
    main()
