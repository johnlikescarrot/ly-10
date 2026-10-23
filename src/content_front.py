# -*- coding: utf-8 -*-
"""Trang bìa, hướng dẫn sử dụng, bản đồ đề thi."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (NextPageTemplate, PageBreak, Paragraph, Spacer,
                                Table, TableStyle)

from style import (AMBER, BODY, BODY_L, INK, LINE, LM, MUTED, PAGE_H, PAGE_W,
                   PAPER, PRIMARY, PRIMARY_L, RM, SMALL, TINT, TEAL, H2, H3, H2S,
                   P, box, bullets, formula, table)

W = PAGE_W - LM - RM


def _w(text, size, color="#FFFFFF", font="BVP-XB", align=TA_LEFT, leading=None):
    st = ParagraphStyle("cw", fontName=font, fontSize=size,
                        leading=leading or size * 1.16, textColor=colors.HexColor(color) if isinstance(color, str) else color,
                        alignment=align)
    return Paragraph(text, st)


def cover():
    out = [Spacer(1, 3.15 * cm)]
    inner = []

    chip = Table([[_w("TÀI LIỆU ÔN THI  ·  VẬT LÍ 10  ·  HỌC KÌ I", 7.6,
                      "#0C1733", "BVP-B")]],
                 colWidths=[9.6 * cm], rowHeights=[0.72 * cm])
    chip.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0B53C")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    inner.append(chip)
    inner.append(Spacer(1, 0.55 * cm))
    inner.append(_w("ĐỀ CƯƠNG", 40, "#FFFFFF", "BVP-XB", leading=44))
    inner.append(_w("ÔN TẬP GIỮA HỌC KÌ I", 20.5, "#C9D6F3", "BVP-SB",
                    leading=27))
    inner.append(Spacer(1, 0.18 * cm))
    inner.append(_w("VẬT LÍ 10", 46, "#F0B53C", "BVP-XB", leading=50))
    inner.append(Spacer(1, 0.42 * cm))
    inner.append(_w("Năm học 2026 – 2027  ·  Biên soạn bám sát <b>Ma trận đặc tả "
                    "KTGK I L10 – 2026</b>", 9.6, "#AEBBDD", "BVP", leading=15))

    out.append(Table([[inner]], colWidths=[W],
                     style=TableStyle([("LEFTPADDING", (0, 0), (-1, -1), LM),
                                       ("RIGHTPADDING", (0, 0), (-1, -1), RM),
                                       ("TOPPADDING", (0, 0), (-1, -1), 0),
                                       ("BOTTOMPADDING", (0, 0), (-1, -1), 0)])))

    # dải thông số
    stats = [[_w("50", 22, "#FFFFFF", "BVP-XB", TA_CENTER, 25),
              _w("70 / 30", 22, "#FFFFFF", "BVP-XB", TA_CENTER, 25),
              _w("18 + 8 + 2 + 3", 15, "#FFFFFF", "BVP-XB", TA_CENTER, 25)],
             [_w("phút làm bài", 7.6, "#93A3CC", "BVP-SB", TA_CENTER),
              _w("% trắc nghiệm / tự luận", 7.6, "#93A3CC", "BVP-SB", TA_CENTER),
              _w("câu hỏi – đủ 4 phần", 7.6, "#93A3CC", "BVP-SB", TA_CENTER)]]
    st = Table(stats, colWidths=[5.6 * cm, 6.4 * cm, 5.4 * cm],
               rowHeights=[1.25 * cm, 0.75 * cm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#132A5E")),
        ("LINEAFTER", (0, 0), (1, -1), 0.6, colors.HexColor("#2B4380")),
        ("VALIGN", (0, 0), (-1, 0), "BOTTOM"),
        ("VALIGN", (0, 1), (-1, 1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 8),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 0),
    ]))
    out.append(Spacer(1, 1.15 * cm))
    out.append(Table([[st]], colWidths=[W],
                     style=TableStyle([("LEFTPADDING", (0, 0), (-1, -1), LM),
                                       ("RIGHTPADDING", (0, 0), (-1, -1), RM),
                                       ("TOPPADDING", (0, 0), (-1, -1), 0),
                                       ("BOTTOMPADDING", (0, 0), (-1, -1), 0)])))

    out.append(Spacer(1, 1.0 * cm))
    cover_list = [
        "Lý thuyết cô đọng 10 đơn vị kiến thức, kèm mẹo nhớ và bẫy thường gặp",
        "Bảng công thức – sơ đồ tư duy – quy trình giải 4 dạng bài trọng tâm",
        "Đề minh họa lập đúng ma trận: 18 TN · 8 ý Đúng/Sai · 2 câu ngắn · 3 câu tự luận",
        "Đáp án có lời giải chi tiết từng câu + thang điểm và chiến lược 50 phút",
    ]
    items = []
    for s in cover_list:
        p = _w("·  " + s, 8.6, "#C2CEEA", "BVP", leading=13.4)
        items.append(p)
    out.append(Table([[items]], colWidths=[W],
                     style=TableStyle([("LEFTPADDING", (0, 0), (-1, -1), LM + 2),
                                       ("RIGHTPADDING", (0, 0), (-1, -1), RM),
                                       ("TOPPADDING", (0, 0), (-1, -1), 0),
                                       ("BOTTOMPADDING", (0, 0), (-1, -1), 0)])))

    out.append(Spacer(1, 1.1 * cm))
    note = _w("Nguồn học liệu: tệp <i>“MA TRẬN ĐẶC TẢ KTGK I L10 – 2026.docx”</i>. Tệp gốc "
              "chỉ chứa <b>ma trận đặc tả</b> (đơn vị kiến thức và mức độ nhận thức), "
              "không kèm đề và đáp án. Vì vậy, toàn bộ nội dung lý thuyết dưới đây được "
              "triển khai phủ kín 10 đơn vị kiến thức của ma trận, và mục D là "
              "<b>đề minh họa được lập đúng số câu – đúng mức độ – đúng đơn vị kiến thức</b> "
              "như ma trận yêu cầu, kèm đáp án và lời giải cho từng câu.", 7.6,
              "#7F8DB4", "BVP", leading=11.4)
    out.append(Table([[note]], colWidths=[W],
                     style=TableStyle([("LEFTPADDING", (0, 0), (-1, -1), LM),
                                       ("RIGHTPADDING", (0, 0), (-1, -1), RM + 8),
                                       ("TOPPADDING", (0, 0), (-1, -1), 10),
                                       ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                       ("LINEABOVE", (0, 0), (-1, 0), 0.6,
                                        colors.HexColor("#2B4380"))])))

    out.append(NextPageTemplate("body"))
    out.append(PageBreak())
    return out


def how_to_use():
    out = [Spacer(1, 6)]
    out.append(P("MỤC LỤC &amp; CÁCH DÙNG ĐỀ CƯƠNG",
                 ParagraphStyle("t", parent=H2S, fontSize=17, leading=22,
                                spaceBefore=0, spaceAfter=4)))
    out.append(P("Toàn bộ nội dung nằm trong 7 mục – đi theo đúng thứ tự là cách ôn "
                 "nhanh nhất.", SMALL))
    out.append(Spacer(1, 10))

    toc = [
        ("A", "Bản đồ đề thi", "Ma trận rút gọn: bài nào chiếm bao nhiêu câu, mức độ ra sao, "
                               "dạng câu dự đoán", "5 phút", "PHẦN A"),
        ("B", "Lý thuyết trọng tâm 10 bài", "Khái niệm – công thức – ví dụ mẫu – mẹo nhớ – bẫy, "
                                           "cho từng đơn vị kiến thức", "90 phút", "PHẦN B"),
        ("C", "Bộ công thức &amp; sơ đồ tư duy", "Một chỗ tra cứu nhanh toàn bộ công thức của "
                                                "chương Động học + sơ đồ tư duy", "15 phút", "PHẦN C"),
        ("D", "Đề minh họa chuẩn ma trận", "18 câu TN + 8 ý Đúng/Sai + 2 câu trả lời ngắn + "
                                          "3 câu tự luận, làm trong 50 phút", "50 phút", "PHẦN D"),
        ("E", "Đáp án &amp; lời giải chi tiết", "Đáp án từng câu, lời giải đầy đủ, chỉ rõ bẫy của "
                                              "từng phương án nhiễu", "40 phút", "PHẦN E"),
        ("F", "12 bẫy thường gặp", "Những lỗi mất điểm phổ biến nhất và cách phòng tránh",
         "10 phút", "PHẦN F"),
        ("G", "Checklist 48 giờ cuối", "Kế hoạch ôn tập 3 ngày, chiến thuật phòng thi 50 phút, "
                                      "thang điểm", "10 phút", "PHẦN G"),
    ]
    from style import page_of
    data = [["MỤC", "TRANG", "NỘI DUNG", "VIỆC CẦN LÀM", "THỜI GIAN"]]
    for k, t, d, tm, prefix in toc:
        data.append([k, page_of(prefix), t, d, tm])
    out.append(table(data, [1.2 * cm, 1.5 * cm, 3.7 * cm, 7.9 * cm, 1.7 * cm],
                     align=[TA_CENTER, TA_CENTER, TA_LEFT, TA_LEFT, TA_CENTER], size=8.5))
    out.append(Spacer(1, 8))
    out.append(P("Gợi ý: nếu chỉ còn 1 buổi tối, hãy đọc mục A (5 phút) → học mục C (15 phút) → "
                 "làm thẳng đề ở mục D (50 phút) → chấm bằng mục E và ghi lại lỗi vào mục F. "
                 "Cách này cho hiệu quả cao hơn nhiều so với đọc lý thuyết suông.", SMALL))
    return out


def roadmap():
    out = [Spacer(1, 8)]
    out.extend(H2("Kế hoạch ôn 3 ngày – 3 vòng"))
    out.append(P("Nguyên tắc: <b>vòng 1 hiểu – vòng 2 nhớ – vòng 3 thi thử</b>. Mỗi vòng ngắn hơn "
                 "vòng trước nhưng chủ động hơn.", BODY))
    days = [
        ("NGÀY 1", "Hiểu", "Đọc mục B (Bài 1 → Bài 10), tự tóm tắt mỗi bài bằng 5 dòng. "
                           "Chưa cần thuộc công thức, chỉ cần giải thích được bằng lời của mình.", "2 giờ"),
        ("NGÀY 2", "Nhớ", "Học thuộc bảng công thức mục C, làm lại các ví dụ mẫu trong mục B "
                          "mà không nhìn lời giải. Viết sơ đồ tư duy ra giấy A4 trắng.", "1,5 giờ"),
        ("NGÀY 3", "Thi", "Bấm giờ 50 phút làm trọn đề mục D. Chấm theo mục E, ghi mọi lỗi sai. "
                          "Đọc lại mục F và câu nào sai thì quay về đúng bài đó trong mục B.", "1,5 giờ"),
    ]
    data = [["", "MỤC TIÊU", "VIỆC LÀM", "THỜI LƯỢNG"]]
    for d in days:
        data.append(list(d))
    out.append(table(data, [1.9 * cm, 1.9 * cm, 10.4 * cm, 2.1 * cm],
                     align=[TA_CENTER, TA_CENTER, TA_LEFT, TA_CENTER], size=8.8,
                     head_bg=TEAL))
    out.append(Spacer(1, 6))
    out.extend(box("Đừng học theo kiểu đọc – gật gù",
                    [P("Cách duy nhất để điểm Vật lí tăng là <b>tự tay viết công thức và tự tay "
                       "bấm máy</b>. Mỗi công thức trong tài liệu này đều đi kèm một ví dụ số – hãy "
                       "che lời giải và làm lại. Nếu làm đúng mà không cần xem, đó mới là “đã nhớ”.")],
                    kind="amber"))
    return out
