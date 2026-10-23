# -*- coding: utf-8 -*-
"""Hình vẽ vector nhỏ (đồ thị d–t và v–t)."""

from reportlab.graphics.shapes import Drawing, Line, String, Polygon, Rect, Circle
from reportlab.lib import colors

NAVY = colors.HexColor("#15315B")
BLUE = colors.HexColor("#1F5FA8")
RED = colors.HexColor("#B03A2E")
GREEN = colors.HexColor("#1E8449")
AMBER = colors.HexColor("#B9770E")
GRAY = colors.HexColor("#5F6B7A")
LIGHT = colors.HexColor("#EDF2F9")


def _axes(dr, x0, y0, x1, y1, xlabel, ylabel):
    dr.add(Line(x0, y0, x1, y0, strokeColor=GRAY, strokeWidth=1))
    dr.add(Line(x0, y0, x0, y1, strokeColor=GRAY, strokeWidth=1))
    # mũi tên
    dr.add(Polygon([x1, y0, x1 - 6, y0 + 3, x1 - 6, y0 - 3], fillColor=GRAY, strokeColor=GRAY))
    dr.add(Polygon([x0, y1, x0 - 3, y1 - 6, x0 + 3, y1 - 6], fillColor=GRAY, strokeColor=GRAY))
    dr.add(String(x1 - 4, y0 - 13, xlabel, fontName="VNSans", fontSize=7.5,
                  fillColor=GRAY, textAnchor="end"))
    dr.add(String(x0 - 8, y1 - 4, ylabel, fontName="VNSans", fontSize=7.5,
                  fillColor=GRAY, textAnchor="end"))
    dr.add(String(x0 - 5, y0 - 12, "O", fontName="VNSans", fontSize=7.5, fillColor=GRAY))


def fig_dt():
    """Ba dạng đồ thị độ dịch chuyển – thời gian."""
    w, h = 470, 158
    dr = Drawing(w, h)
    x0, y0, x1, y1 = 48, 30, 300, 132
    _axes(dr, x0, y0, x1, y1, "t", "d")
    sx, sy = 25.0, 9.4  # px / đơn vị

    def P(t, dd):
        return x0 + t * sx, y0 + dd * sy

    # (1) đứng yên
    a, b = P(0, 6), P(8, 6)
    dr.add(Line(a[0], a[1], b[0], b[1], strokeColor=BLUE, strokeWidth=2))
    # (2) thẳng đều cùng chiều dương
    a, b = P(0, 0), P(8, 9)
    dr.add(Line(a[0], a[1], b[0], b[1], strokeColor=GREEN, strokeWidth=2))
    # (3) thẳng đều ngược chiều dương
    a, b = P(0, 9), P(8, 2)
    dr.add(Line(a[0], a[1], b[0], b[1], strokeColor=RED, strokeWidth=2, strokeDashArray=[4, 3]))

    # chú giải
    lx = 316
    for i, (c, txt) in enumerate([
            (BLUE, "d không đổi: vật đứng yên"),
            (GREEN, "dốc lên: đi theo chiều dương"),
            (RED, "dốc xuống: đi ngược chiều dương")]):
        yy = h - 42 - i * 26
        dr.add(Line(lx, yy + 3, lx + 20, yy + 3, strokeColor=c, strokeWidth=2.2))
        dr.add(String(lx + 26, yy, txt, fontName="VNSans", fontSize=7.2, fillColor=GRAY))

    return dr


def fig_vt():
    """Đồ thị vận tốc – thời gian của chuyển động thẳng biến đổi đều."""
    w, h = 470, 168
    dr = Drawing(w, h)
    x0, y0, x1, y1 = 52, 28, 330, 140
    _axes(dr, x0, y0, x1, y1, "t (s)", "v (m/s)")
    sx, sy = 34.0, 4.6

    def P(t, v):
        return x0 + t * sx, y0 + v * sy

    # vùng diện tích
    p0 = P(0, 0)
    p1 = P(0, 5)
    p2 = P(5, 15)
    p3 = P(5, 0)
    dr.add(Polygon([p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]],
                   fillColor=LIGHT, strokeColor=None))
    dr.add(Line(p1[0], p1[1], p2[0], p2[1], strokeColor=NAVY, strokeWidth=2.2))

    # đường gióng
    dr.add(Line(p1[0] - 4, p1[1], p1[0] + 4, p1[1], strokeColor=GRAY, strokeWidth=0.8))
    dr.add(Line(p2[0], p2[1], p2[0] + 4, p2[1], strokeColor=GRAY, strokeWidth=0.8))
    dr.add(String(p2[0] + 9, p2[1] + 2, "B", fontName="VNSans-Bold", fontSize=8, fillColor=NAVY))
    dr.add(String(p2[0] - 16, y0 - 12, "t", fontName="VNSans", fontSize=8, fillColor=NAVY))
    dr.add(String(x0 - 30, p1[1] - 3, "v₀", fontName="VNSans", fontSize=8, fillColor=NAVY))

    # chú thích
    dr.add(String(x0 + 118, y0 + 34, "Diện tích hình thang", fontName="VNSans-Bold",
                  fontSize=8.4, fillColor=BLUE))
    dr.add(String(x0 + 118, y0 + 21, "= độ dịch chuyển d", fontName="VNSans",
                  fontSize=8.2, fillColor=BLUE))
    dr.add(String(x1 + 10, 128, "hệ số góc", fontName="VNSans", fontSize=7.6, fillColor=GRAY))
    dr.add(String(x1 + 10, 118, "của đường thẳng", fontName="VNSans", fontSize=7.6, fillColor=GRAY))
    dr.add(String(x1 + 10, 108, "= gia tốc a", fontName="VNSans-Bold", fontSize=8.4, fillColor=RED))
    return dr
