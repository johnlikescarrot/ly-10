#!/usr/bin/env python3
"""Tạo các hình minh họa vector-like ở độ phân giải cao cho đề cương."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import os

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)


def find_font_dir() -> Path:
    candidates = [
        Path(os.environ.get("DEJAVU_FONT_DIR", "")),
        Path("/usr/share/fonts/truetype/dejavu"),
        Path("/usr/local/share/fonts/dejavu"),
        ROOT / "assets" / "fonts",
    ]
    for directory in candidates:
        if (directory / "DejaVuSans.ttf").is_file() and (directory / "DejaVuSans-Bold.ttf").is_file():
            return directory
    raise FileNotFoundError(
        "Không tìm thấy DejaVu Sans. Đặt DEJAVU_FONT_DIR tới thư mục chứa "
        "DejaVuSans.ttf và DejaVuSans-Bold.ttf."
    )


FONT_DIR = find_font_dir()
FONT_REG = FONT_DIR / "DejaVuSans.ttf"
FONT_BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"

NAVY = "#123B5D"
BLUE = "#147D92"
TEAL = "#1B9AAA"
ORANGE = "#E87722"
INK = "#172B3A"
MUTED = "#5D6B78"
GRID = "#D8E2E8"
LIGHT = "#EAF6F6"
WHITE = "#FFFFFF"


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


def canvas():
    return Image.new("RGB", (1600, 900), WHITE)


def text_center(draw, xy, text, fnt, fill=INK):
    box = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=8, align="center")
    w, h = box[2] - box[0], box[3] - box[1]
    draw.multiline_text((xy[0] - w / 2, xy[1] - h / 2), text, font=fnt, fill=fill, spacing=8, align="center")


def arrow(draw, start, end, fill=BLUE, width=8, head=22):
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    a1 = angle + math.pi * 0.84
    a2 = angle - math.pi * 0.84
    p1 = (end[0] + head * math.cos(a1), end[1] + head * math.sin(a1))
    p2 = (end[0] + head * math.cos(a2), end[1] + head * math.sin(a2))
    draw.polygon([end, p1, p2], fill=fill)


def graph_base(title, xlabel, ylabel, xmax, ymax, xticks, yticks):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.text((90, 45), title, font=font(43, True), fill=NAVY)
    left, top, right, bottom = 185, 150, 1470, 745
    for value in xticks:
        x = left + (right - left) * value / xmax
        d.line((x, top, x, bottom), fill=GRID, width=2)
        text_center(d, (x, bottom + 43), str(value).replace(".", ","), font(26), MUTED)
    for value in yticks:
        y = bottom - (bottom - top) * value / ymax
        d.line((left, y, right, y), fill=GRID, width=2)
        text_center(d, (left - 55, y), str(value).replace(".", ","), font(26), MUTED)
    arrow(d, (left, bottom), (right + 35, bottom), fill=INK, width=5, head=18)
    arrow(d, (left, bottom), (left, top - 35), fill=INK, width=5, head=18)
    d.text((right - 15, bottom + 72), xlabel, font=font(30, True), fill=INK)
    d.text((left + 10, top - 45), ylabel, font=font(26, True), fill=INK)
    return im, d, (left, top, right, bottom)


def point_mapper(bounds, xmax, ymax):
    left, top, right, bottom = bounds
    return lambda x, y: (left + (right - left) * x / xmax, bottom - (bottom - top) * y / ymax)


def make_dt():
    xmax, ymax = 27, 24
    im, d, bounds = graph_base(
        "Đồ thị độ dịch chuyển – thời gian (ví dụ)",
        "t (s)", "d (m)", xmax, ymax, [0, 5, 10, 15, 20, 25], [0, 5, 10, 15, 20]
    )
    d.rectangle((70, 40, 1530, 115), fill=WHITE)
    d.text((90, 45), "Đồ thị độ dịch chuyển – thời gian (ví dụ)", font=font(43, True), fill=NAVY)
    p = point_mapper(bounds, xmax, ymax)
    pts = [p(0, 0), p(10, 20), p(15, 20), p(25, 0)]
    d.line(pts, fill=BLUE, width=10, joint="curve")
    for xy, label, dx, dy in zip(pts, ["O", "A", "B", "C"], [-25, 0, 0, 25], [20, -42, -42, 20]):
        x, y = xy
        d.ellipse((x - 10, y - 10, x + 10, y + 10), fill=ORANGE)
        text_center(d, (x + dx, y + dy), label, font(28, True), NAVY)
    d.rounded_rectangle((940, 180, 1430, 300), radius=18, fill=LIGHT)
    text_center(d, (1185, 240), "Độ dốc = vận tốc\nOA: +2 m/s  •  BC: −2 m/s", font(27, True), NAVY)
    im.save(OUT / "do-thi-do-dich-chuyen.png", optimize=True)


def make_vt():
    xmax, ymax = 6.5, 11
    im, d, bounds = graph_base(
        "Đồ thị vận tốc – thời gian khi hãm xe",
        "t (s)", "v (m/s)", xmax, ymax, [0, 1, 2, 3, 4, 5, 6], [0, 2, 4, 6, 8, 10]
    )
    d.rectangle((70, 40, 1530, 115), fill=WHITE)
    d.text((90, 45), "Đồ thị vận tốc – thời gian khi hãm xe", font=font(43, True), fill=NAVY)
    p = point_mapper(bounds, xmax, ymax)
    area = [p(0, 0), p(0, 10), p(5, 0)]
    d.polygon(area, fill="#D8F0F0")
    d.line([p(0, 10), p(5, 0)], fill=BLUE, width=11)
    d.line([p(5, 0), p(6, 0)], fill=NAVY, width=9)
    for x, y in [(0, 10), (5, 0)]:
        px, py = p(x, y)
        d.ellipse((px - 10, py - 10, px + 10, py + 10), fill=ORANGE)
    d.rounded_rectangle((690, 360, 1260, 475), radius=18, fill=WHITE, outline=TEAL, width=3)
    text_center(d, (975, 417), "Diện tích có dấu = độ dịch chuyển\nd = ½ · 5 · 10 = 25 m", font(28, True), NAVY)
    d.text((275, 205), "v = 10 − 2t", font=font(32, True), fill=BLUE)
    im.save(OUT / "do-thi-van-toc.png", optimize=True)


def make_relative_velocity():
    im = canvas()
    d = ImageDraw.Draw(im)
    d.text((90, 55), "Cộng vận tốc khi hai thành phần vuông góc", font=font(42, True), fill=NAVY)
    o = (390, 675)
    vx = (840, 675)
    vy = (390, 225)
    r = (840, 225)
    d.line([vy, r, vx], fill="#9AB0BE", width=4)
    arrow(d, o, vy, fill=TEAL, width=11, head=28)
    arrow(d, o, vx, fill=ORANGE, width=11, head=28)
    arrow(d, o, r, fill=BLUE, width=12, head=30)
    d.ellipse((o[0] - 10, o[1] - 10, o[0] + 10, o[1] + 10), fill=INK)
    d.rounded_rectangle((70, 330, 350, 475), radius=18, fill=LIGHT)
    text_center(d, (210, 402), "v thuyền/nước\n= 2 m/s", font(30, True), NAVY)
    d.rounded_rectangle((475, 710, 950, 815), radius=18, fill="#FFF3E8")
    text_center(d, (712, 762), "v nước/bờ = 1,5 m/s", font(30, True), NAVY)
    d.rounded_rectangle((850, 320, 1500, 475), radius=18, fill="#EAF0FA")
    text_center(d, (1175, 397), "v thuyền/bờ = √(2² + 1,5²)\n= 2,5 m/s", font(31, True), NAVY)
    d.text((390, 130), "v⃗₁,₃ = v⃗₁,₂ + v⃗₂,₃", font=font(35, True), fill=INK)
    im.save(OUT / "cong-van-toc.png", optimize=True)


def make_method():
    im = canvas()
    d = ImageDraw.Draw(im)
    d.text((90, 55), "Phương pháp thực nghiệm: chuỗi 5 bước", font=font(43, True), fill=NAVY)
    labels = [
        ("1", "Xác định\nvấn đề"),
        ("2", "Quan sát,\nthu thập\nthông tin"),
        ("3", "Dự đoán\n(giả thuyết)"),
        ("4", "Thí nghiệm\nkiểm tra"),
        ("5", "Kết luận"),
    ]
    xs = [175, 485, 795, 1105, 1415]
    for i, ((num, label), x) in enumerate(zip(labels, xs)):
        fill = LIGHT if i % 2 == 0 else "#EAF0FA"
        d.rounded_rectangle((x - 130, 300, x + 130, 570), radius=28, fill=fill, outline=TEAL, width=4)
        d.ellipse((x - 38, 245, x + 38, 321), fill=ORANGE)
        text_center(d, (x, 283), num, font(35, True), WHITE)
        text_center(d, (x, 435), label, font(26, True), NAVY)
        if i < 4:
            arrow(d, (x + 140, 435), (xs[i + 1] - 140, 435), fill=BLUE, width=7, head=20)
    d.rounded_rectangle((180, 675, 1420, 790), radius=22, fill="#FFF3E8")
    text_center(d, (800, 732), "Kết quả không phù hợp? Kiểm tra phép đo, điều chỉnh dự đoán và thử lại.", font(26, True), INK)
    im.save(OUT / "phuong-phap-thuc-nghiem.png", optimize=True)


if __name__ == "__main__":
    make_dt()
    make_vt()
    make_relative_velocity()
    make_method()
    for path in sorted(OUT.glob("*.png")):
        print(path.relative_to(ROOT), path.stat().st_size)
