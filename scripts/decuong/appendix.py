# -*- coding: utf-8 -*-
"""PHỤ LỤC – Trang bỏ túi: một trang A4 duy nhất để đọc trước giờ thi."""
from __future__ import annotations

from reportlab.lib import colors
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

from .style import (
    ACCENT, BG_AMBER, BG_BLUE, BG_GREEN, BG_SOFT, CONTENT_W, FONT_B, INK, LINE,
    MUTED, P, PRIMARY, PRIMARY_D, S, SPC, box, data_table, formula, rule,
)


def _mini(title, lines, accent=PRIMARY, bg=BG_SOFT):
    inner = [Paragraph(f'<font color="{accent.hexval()}"><b>{title}</b></font>', S["box_title"])]
    for ln in lines:
        inner.append(Paragraph(ln, S["mini"]))
    t = Table([[inner]], colWidths=[CONTENT_W / 2 - 8])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def appendix():
    f = []
    f.append(P("PHỤ LỤC · TRANG BỎ TÚI – ĐỌC 10 PHÚT TRƯỚC KHI VÀO PHÒNG THI", "h1"))
    f.append(P("Trang này gom <b>toàn bộ thứ cần nhớ</b> vào một tờ. Em có thể in riêng trang này, gấp đôi và bỏ túi.", "small"))
    f.append(SPC(4))

    # Row 1
    left = _mini("1 · ĐỘ DỊCH CHUYỂN & QUÃNG ĐƯỜNG", [
        "d: <b>vectơ</b>, nối điểm đầu → điểm cuối",
        "s: <b>vô hướng</b>, tổng độ dài đường đi",
        "<b>|Δd| ≤ s</b>; bằng nhau khi thẳng & không đổi chiều",
        "Đi vòng kín: Δd = 0 nhưng s ≠ 0",
    ], colors.HexColor("#1F5F99"), BG_BLUE)
    right = _mini("2 · TỐC ĐỘ & VẬN TỐC", [
        "v<sub>tb</sub> = s/Δt  (tốc độ – vô hướng)",
        "v<sub>tb</sub> = Δd/Δt  (vận tốc – vectơ)",
        "1 km/h = 1/3,6 m/s",
        "v₁₃ = v₁₂ + v₂₃: cùng chiều <b>+</b>, ngược chiều <b>−</b>, vuông góc <b>√(a²+b²)</b>",
    ], colors.HexColor("#1D6B4C"), BG_GREEN)
    f.append(Table([[left, "", right]], colWidths=[CONTENT_W / 2 - 8, 16, CONTENT_W / 2 - 8],
                   style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                     ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                     ("RIGHTPADDING", (0, 0), (-1, -1), 0)])))
    f.append(SPC(7))

    # Row 2
    left = _mini("3 · ĐỒ THỊ d – t", [
        "<b>Độ dốc = vận tốc</b>",
        "Nằm ngang → v = 0 (đứng yên)",
        "Dốc xuống → đi ngược chiều dương",
        "Tung độ = vị trí tại thời điểm t",
    ], colors.HexColor("#5B3E96"), colors.HexColor("#F1ECF8"))
    right = _mini("4 · GIA TỐC", [
        "a = Δv/Δt = (v − v₀)/t   (m/s²)",
        "a cùng chiều v → <b>nhanh dần</b>",
        "a ngược chiều v → <b>chậm dần</b>",
        "a = 0 → thẳng đều",
    ], colors.HexColor("#A8332A"), colors.HexColor("#FBEDEB"))
    f.append(Table([[left, "", right]], colWidths=[CONTENT_W / 2 - 8, 16, CONTENT_W / 2 - 8],
                   style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                     ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                     ("RIGHTPADDING", (0, 0), (-1, -1), 0)])))
    f.append(SPC(7))

    # Big formula block
    f.append(P("5 · BỐN CÔNG THỨC XƯƠNG SỐNG", "h3"))
    rows = [
        [Paragraph("v = v<sub>0</sub> + a·t", S["formula"]),
         Paragraph("<font color='#5A6B7B'>khi không có s</font>", S["formula_note"])],
        [Paragraph("s = v<sub>0</sub>·t + ½·a·t²", S["formula"]),
         Paragraph("<font color='#5A6B7B'>khi không có v</font>", S["formula_note"])],
        [Paragraph("v² − v<sub>0</sub>² = 2·a·s", S["formula"]),
         Paragraph("<font color='#5A6B7B'>khi không có t</font>", S["formula_note"])],
        [Paragraph("s = (v<sub>0</sub> + v)·t / 2", S["formula"]),
         Paragraph("<font color='#5A6B7B'>khi không có a</font>", S["formula_note"])],
    ]
    t = Table(rows, colWidths=[CONTENT_W / 2, CONTENT_W / 2], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BG_SOFT),
        ("LINEBEFORE", (0, 0), (0, -1), 2.4, PRIMARY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ]))
    f.append(t)
    f.append(SPC(7))

    # Row 3
    left = _mini("6 · RƠI TỰ DO  (v₀ = 0, a = g)", [
        "v = g·t  ·  s = ½·g·t²",
        "v² = 2·g·s  ·  t = √(2s/g)",
        "Quãng đường 1 s – 2 s – 3 s: <b>1 : 4 : 9</b>",
        "Các giây liên tiếp: <b>1 : 3 : 5 : 7</b>",
        "Chỉ dùng khi <b>bỏ qua lực cản</b>",
    ], colors.HexColor("#B87410"), BG_AMBER)
    right = _mini("7 · SAI SỐ PHÉP ĐO", [
        "Ā = ΣA<sub>i</sub>/n ; ΔA<sub>i</sub> = |Ā − A<sub>i</sub>|",
        "ΔA = ΔĀ + ΔA<sub>dc</sub>  (ΔA<sub>dc</sub> = ½ ĐCNN)",
        "δA = (ΔA/Ā)·100%",
        "Ghi: <b>A = Ā ± ΔA</b> – cùng bậc thập phân",
    ], colors.HexColor("#0E4C6B"), BG_BLUE)
    f.append(Table([[left, "", right]], colWidths=[CONTENT_W / 2 - 8, 16, CONTENT_W / 2 - 8],
                   style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                     ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                     ("RIGHTPADDING", (0, 0), (-1, -1), 0)])))
    f.append(SPC(7))

    # Final reminder strip
    f.append(box("Ba giây kiểm tra cuối bài", [
        P("<b>1. Đơn vị</b> – mọi kết quả phải có đơn vị, và đơn vị phải đúng hệ (m, s, m/s, m/s²).", "box_item"),
        P("<b>2. Dấu</b> – chiều dương đã chọn là gì? a âm hay dương? v₀ âm hay dương?", "box_item"),
        P("<b>3. Câu hỏi</b> – đề hỏi <i>quãng đường</i> hay <i>độ dịch chuyển</i>, <i>tốc độ</i> hay <i>vận tốc</i>?", "box_item"),
    ], "tip"))
    f.append(SPC(6))

    f.append(P("Chúc em bình tĩnh – tự tin – làm bài chắc từng câu!", "body_c"))
    f.append(SPC(2))
    f.append(P("Đọc kĩ đề · Viết công thức trước · Không bỏ trống câu nào", "cap"))
    return f
