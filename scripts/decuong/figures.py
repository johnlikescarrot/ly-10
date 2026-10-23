# -*- coding: utf-8 -*-
"""Small vector figures drawn with reportlab.graphics (no external images)."""
from __future__ import annotations

import math

from reportlab.graphics.shapes import Circle, Drawing, Line, Polygon, Rect, String
from reportlab.lib import colors

from .style import ACCENT, BLUE, GREEN, INK, LINE, MUTED, PRIMARY, RED, FONT

GRID = colors.HexColor("#E3EAF1")


def _arrow(d, x1, y1, x2, y2, color=PRIMARY, w=1.4, head=6.0):
    ang = math.atan2(y2 - y1, x2 - x1)
    xb = x2 - head * 0.92 * math.cos(ang)
    yb = y2 - head * 0.92 * math.sin(ang)
    d.add(Line(x1, y1, xb, yb, strokeColor=color, strokeWidth=w))
    p1 = (x2, y2)
    p2 = (xb + head * 0.42 * math.sin(ang), yb - head * 0.42 * math.cos(ang))
    p3 = (xb - head * 0.42 * math.sin(ang), yb + head * 0.42 * math.cos(ang))
    d.add(Polygon([p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]],
                  fillColor=color, strokeColor=color, strokeWidth=0.4))


def _txt(d, x, y, s, color=INK, size=7.6, anchor="middle", bold=False):
    d.add(String(x, y, s, fontName=FONT, fontSize=size, fillColor=color,
                 textAnchor=anchor))


# --------------------------------------------------------------------------- #
def fig_displacement(w=250, h=118):
    """Quãng đường (đường cong) vs độ dịch chuyển (mũi tên thẳng)."""
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))
    ax, ay = 34, 34
    bx, by = 208, 84
    # curved path via polyline points (quadratic-ish arc)
    pts = []
    for i in range(41):
        t = i / 40
        x = ax + (bx - ax) * t
        y = ay + (by - ay) * t + 26 * math.sin(math.pi * t)
        pts += [x, y]
    from reportlab.graphics.shapes import PolyLine
    d.add(PolyLine(pts, strokeColor=ACCENT, strokeWidth=1.6, strokeDashArray=[3, 2.2]))
    _arrow(d, ax, ay, bx, by, PRIMARY, 1.7, 7)
    d.add(Circle(ax, ay, 3.2, fillColor=PRIMARY, strokeColor=colors.white, strokeWidth=1))
    d.add(Circle(bx, by, 3.2, fillColor=PRIMARY, strokeColor=colors.white, strokeWidth=1))
    _txt(d, ax - 9, ay - 9, "A", PRIMARY, 8.6)
    _txt(d, bx + 4, by + 6, "B", PRIMARY, 8.6)
    _txt(d, (ax + bx) / 2 - 4, (ay + by) / 2 + 39, "quãng đường s", ACCENT, 7.4)
    _txt(d, (ax + bx) / 2 - 2, (ay + by) / 2 - 12, "độ dịch chuyển d", PRIMARY, 7.4)
    return d


# --------------------------------------------------------------------------- #
def _axes(d, x0, y0, x1, y1, xlab="", ylab=""):
    _arrow(d, x0, y0, x1, y0, MUTED, 1.0, 5)
    _arrow(d, x0, y0, x0, y1, MUTED, 1.0, 5)
    _txt(d, x1 - 8, y0 - 11, xlab, MUTED, 7.4)
    _txt(d, x0 - 14, y1 - 4, ylab, MUTED, 7.4)


def fig_dt_graph(w=252, h=132):
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))
    ox, oy, ex, ey = 34, 26, 234, 112
    for gy in range(oy + 6, ey, 16):
        d.add(Line(ox, gy, ex, gy, strokeColor=GRID, strokeWidth=0.5))
    _axes(d, ox, oy, ex, ey, "t (s)", "d (m)")
    # segment 1: rise
    d.add(Line(ox, oy + 8, ox + 62, oy + 52, strokeColor=PRIMARY, strokeWidth=1.8))
    # segment 2: flat
    d.add(Line(ox + 62, oy + 52, ox + 118, oy + 52, strokeColor=GREEN, strokeWidth=1.8))
    # segment 3: fall
    d.add(Line(ox + 118, oy + 52, ox + 172, oy + 18, strokeColor=RED, strokeWidth=1.8))
    _txt(d, ox + 26, oy + 40, "đi nhanh", PRIMARY, 7.0)
    _txt(d, ox + 90, oy + 59, "đứng yên", GREEN, 7.0)
    _txt(d, ox + 152, oy + 30, "đi ngược", RED, 7.0)
    for x in (ox, ox + 62, ox + 118):
        d.add(Line(x, oy - 2.5, x, oy + 2.5, strokeColor=MUTED, strokeWidth=0.8))
    return d


# --------------------------------------------------------------------------- #
def fig_vt_graph(w=252, h=132):
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))
    ox, oy, ex, ey = 34, 26, 234, 112
    for gy in range(oy + 6, ey, 16):
        d.add(Line(ox, gy, ex, gy, strokeColor=GRID, strokeWidth=0.5))
    _axes(d, ox, oy, ex, ey, "t (s)", "v (m/s)")
    # nhanh dần đều
    x1, y1 = ox + 6, oy + 10
    x2, y2 = ox + 92, oy + 74
    d.add(Polygon([x1, y1, x2, y2, x2, y1], fillColor=colors.HexColor("#E9F1F9"),
                  strokeColor=None))
    d.add(Line(x1, y1, x2, y2, strokeColor=PRIMARY, strokeWidth=1.8))
    _txt(d, ox + 74, oy + 50, "nhanh dần", PRIMARY, 7.2)
    # chậm dần đều
    x3, y3 = ox + 116, oy + 72
    x4, y4 = ox + 196, oy + 14
    d.add(Line(x3, y3, x4, y4, strokeColor=RED, strokeWidth=1.8))
    _txt(d, ox + 156, oy + 56, "chậm dần", RED, 7.2)
    _txt(d, ox + 48, oy + 4, "S = diện tích", MUTED, 6.6)
    return d


# --------------------------------------------------------------------------- #
def fig_vector_cases(w=470, h=96):
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))
    base_y = 32
    labels = ["cùng chiều", "ngược chiều", "vuông góc"]
    centers = [78, 235, 392]
    # case 1
    x = centers[0] - 52
    _arrow(d, x, base_y, x + 46, base_y, BLUE, 1.4, 6)
    _arrow(d, x + 46, base_y, x + 92, base_y, ACCENT, 1.4, 6)
    _txt(d, x + 46, base_y + 9, "a", BLUE, 7.4)
    _txt(d, x + 70, base_y - 12, "b", ACCENT, 7.4)
    # case 2
    x = centers[1] - 52
    _arrow(d, x, base_y, x + 30, base_y, BLUE, 1.4, 6)
    _arrow(d, x + 88, base_y, x + 44, base_y, ACCENT, 1.4, 6)
    _txt(d, x + 12, base_y + 9, "a", BLUE, 7.4)
    _txt(d, x + 62, base_y + 9, "b", ACCENT, 7.4)
    # case 3
    x = centers[2] - 46
    _arrow(d, x, base_y - 8, x + 52, base_y - 8, BLUE, 1.4, 6)
    _arrow(d, x, base_y - 8, x, base_y + 40, ACCENT, 1.4, 6)
    d.add(Line(x + 6, base_y - 2, x + 10, base_y - 2, strokeColor=MUTED, strokeWidth=0.7))
    d.add(Line(x + 10, base_y - 2, x + 10, base_y - 8, strokeColor=MUTED, strokeWidth=0.7))
    _txt(d, x + 26, base_y - 16, "a", BLUE, 7.4)
    _txt(d, x - 8, base_y + 16, "b", ACCENT, 7.4)
    for i, lab in enumerate(labels):
        _txt(d, centers[i], 8, lab, MUTED, 7.2)
    return d


def fig_dt_slope(w=250, h=120):
    """Độ dốc của đồ thị d–t = vận tốc."""
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))
    ox, oy, ex, ey = 34, 24, 226, 100
    _axes(d, ox, oy, ex, ey, "t (s)", "d (m)")
    x1, y1 = ox + 20, oy + 14
    x2, y2 = ox + 120, oy + 66
    d.add(Line(x1, y1, x2, y2, strokeColor=PRIMARY, strokeWidth=1.8))
    d.add(Line(x1, y1, x2, y1, strokeColor=ACCENT, strokeWidth=1.0, strokeDashArray=[2, 2]))
    d.add(Line(x2, y1, x2, y2, strokeColor=ACCENT, strokeWidth=1.0, strokeDashArray=[2, 2]))
    _txt(d, (x1 + x2) / 2, y1 - 10, "Δt", ACCENT, 7.2)
    _txt(d, x2 + 12, (y1 + y2) / 2, "Δd", ACCENT, 7.2)
    _txt(d, x1 + 46, y1 + 34, "độ dốc = v", PRIMARY, 7.4)
    return d


# --------------------------------------------------------------------------- #
def fig_mindmap_ch2(w=511, h=250):
    """Sơ đồ tư duy tổng kết Chương II – Động học chất điểm."""
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))

    cx, cy = w / 2, h / 2
    nodes = [
        (0,   "ĐỘ DỊCH CHUYỂN", ["d: vectơ, nối đầu – cuối", "s: vô hướng, theo đường đi", "|Δd| ≤ s"], "#1F5F99"),
        (60,  "TỐC ĐỘ – VẬN TỐC", ["v = s/Δt (tốc độ)", "v = Δd/Δt (vận tốc)", "v₁₃ = v₁₂ + v₂₃"], "#1D6B4C"),
        (120, "ĐỒ THỊ d – t", ["độ dốc = vận tốc", "ngang → đứng yên", "dốc xuống → ngược chiều"], "#5B3E96"),
        (180, "GIA TỐC", ["a = Δv/Δt  (m/s²)", "a cùng chiều v: nhanh dần", "a ngược chiều v: chậm dần"], "#A8332A"),
        (240, "THẲNG BIẾN ĐỔI ĐỀU", ["v = v₀ + at", "s = v₀t + ½at²", "v² − v₀² = 2as"], "#0E4C6B"),
        (300, "RƠI TỰ DO", ["chỉ chịu trọng lực, a = g", "v = gt ; s = ½gt²", "v² = 2gs ; t = √(2s/g)"], "#B87410"),
    ]

    # connectors first (behind nodes)
    for ang, *_ in nodes:
        a = math.radians(ang)
        x2 = cx + 166 * math.cos(a)
        y2 = cy + 86 * math.sin(a)
        d.add(Line(cx, cy, x2, y2, strokeColor=colors.HexColor("#C9D6E0"),
                   strokeWidth=1.2, strokeDashArray=[2.5, 2.5]))

    # centre
    d.add(Rect(cx - 74, cy - 25, 148, 50, rx=25, ry=25, fillColor=PRIMARY,
               strokeColor=colors.white, strokeWidth=2))
    _txt(d, cx, cy + 5, "ĐỘNG HỌC", colors.white, 12.5, "middle", True)
    _txt(d, cx, cy - 12, "chất điểm", colors.HexColor("#BFDCEC"), 7.8)

    bw, bh = 146, 52
    for ang, title, lines, col in nodes:
        a = math.radians(ang)
        x = cx + 166 * math.cos(a)
        y = cy + 86 * math.sin(a)
        x0, y0 = x - bw / 2, y - bh / 2
        c = colors.HexColor(col)
        d.add(Rect(x0, y0, bw, bh, rx=7, ry=7, fillColor=colors.white,
                   strokeColor=c, strokeWidth=1.3))
        d.add(Rect(x0, y0, 3.4, bh, rx=1.7, ry=1.7, fillColor=c, strokeColor=c))
        _txt(d, x, y0 + bh - 13, title, c, 7.6, "middle", True)
        for i, ln in enumerate(lines):
            _txt(d, x, y0 + bh - 26 - i * 9.4, ln, colors.HexColor("#33475B"), 6.6)
    return d


# --------------------------------------------------------------------------- #
def fig_matrix_bars(w=511, h=178):
    """Horizontal bars: số câu/ý theo từng đơn vị kiến thức."""
    d = Drawing(w, h)
    d.add(Rect(0, 0, w, h, fillColor=colors.white, strokeColor=None))

    data = [
        ("1.1 Làm quen với Vật lí", 1),
        ("1.2 Quy tắc an toàn", 2),
        ("1.3 Sai số phép đo", 1),
        ("2.1 Độ dịch chuyển – quãng đường", 3),
        ("2.2 Tốc độ và vận tốc", 5),
        ("2.3 Đồ thị d – t", 4),
        ("2.4 Gia tốc", 2),
        ("2.5 Chuyển động thẳng BĐĐ", 9),
        ("2.6 Sự rơi tự do", 4),
    ]
    x0 = 216          # left edge of bars
    maxv = 9
    bar_max = w - x0 - 34
    top = h - 20
    step = (h - 48) / len(data)
    bh = step * 0.62

    d.add(Line(x0, top + 6, x0, 12, strokeColor=colors.HexColor("#C9D6E0"), strokeWidth=0.8))
    for gv in range(0, maxv + 1, 3):
        gx = x0 + bar_max * gv / maxv
        d.add(Line(gx, top + 6, gx, 12, strokeColor=GRID, strokeWidth=0.6))
        _txt(d, gx, 3, str(gv), MUTED, 6.4)

    for i, (label, val) in enumerate(data):
        y = top - i * step - step / 2
        c = ACCENT if val >= 4 else (colors.HexColor("#2E7DA6") if val >= 2 else colors.HexColor("#9FB4C4"))
        bw = bar_max * val / maxv
        d.add(Rect(x0, y - bh / 2, bw, bh, rx=2, ry=2, fillColor=c, strokeColor=None))
        _txt(d, x0 + bw + 5, y - 2.4, str(val), c if val >= 4 else MUTED, 7.2, "start", val >= 4)
        _txt(d, x0 - 7, y - 2.6, label, INK, 6.6, "end")

    _txt(d, x0, h - 8, "Số câu / số ý trong đề", MUTED, 6.8, "start")
    return d
