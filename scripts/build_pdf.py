#!/usr/bin/env python3
"""Dựng PDF đề cương từ Markdown bằng ReportLab (không cần trình duyệt)."""
from __future__ import annotations

import argparse
import html
import os
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "de-cuong-on-tap-giua-ki-i-vat-ly-10.md"
DEFAULT_OUTPUT = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_I_VAT_LY_10_2026-2027.pdf"

NAVY = colors.HexColor("#123B5D")
BLUE = colors.HexColor("#147D92")
TEAL = colors.HexColor("#1B9AAA")
ORANGE = colors.HexColor("#D9651A")
INK = colors.HexColor("#172B3A")
MUTED = colors.HexColor("#526372")
GRID = colors.HexColor("#CBD8E0")
PALE = colors.HexColor("#F3F7FA")
PALE_BLUE = colors.HexColor("#EAF0FA")
PALE_TEAL = colors.HexColor("#EAF6F6")
PALE_ORANGE = colors.HexColor("#FFF3E8")
WHITE = colors.white


def register_fonts() -> None:
    candidates = [
        Path(os.environ.get("DEJAVU_FONT_DIR", "")),
        Path("/usr/share/fonts/truetype/dejavu"),
        Path("/usr/local/share/fonts/dejavu"),
        ROOT / "assets" / "fonts",
    ]
    for directory in candidates:
        if (directory / "DejaVuSans.ttf").is_file():
            pdfmetrics.registerFont(TTFont("DVS", str(directory / "DejaVuSans.ttf")))
            pdfmetrics.registerFont(TTFont("DVSB", str(directory / "DejaVuSans-Bold.ttf")))
            pdfmetrics.registerFont(TTFont("DVM", str(directory / "DejaVuSansMono.ttf")))
            pdfmetrics.registerFont(TTFont("DVMB", str(directory / "DejaVuSansMono-Bold.ttf")))
            pdfmetrics.registerFontFamily(
                "DVS", normal="DVS", bold="DVSB", italic="DVS", boldItalic="DVSB"
            )
            pdfmetrics.registerFontFamily(
                "DVM", normal="DVM", bold="DVMB", italic="DVM", boldItalic="DVMB"
            )
            return
    raise FileNotFoundError(
        "Không tìm thấy DejaVu Sans. Đặt DEJAVU_FONT_DIR tới thư mục chứa "
        "DejaVuSans.ttf và DejaVuSans-Bold.ttf."
    )


def make_styles():
    sample = getSampleStyleSheet()
    styles = {}
    styles["Body"] = ParagraphStyle(
        "Body",
        parent=sample["BodyText"],
        fontName="DVS",
        fontSize=9.7,
        leading=14.1,
        textColor=INK,
        spaceAfter=5.5,
        splitLongWords=True,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["H1"] = ParagraphStyle(
        "H1",
        parent=styles["Body"],
        fontName="DVSB",
        fontSize=16.5,
        leading=21,
        textColor=NAVY,
        spaceBefore=7,
        spaceAfter=9,
        keepWithNext=True,
    )
    styles["H2"] = ParagraphStyle(
        "H2",
        parent=styles["Body"],
        fontName="DVSB",
        fontSize=12.4,
        leading=16.5,
        textColor=BLUE,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True,
    )
    styles["H3"] = ParagraphStyle(
        "H3",
        parent=styles["Body"],
        fontName="DVSB",
        fontSize=10.6,
        leading=14.5,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True,
    )
    styles["Bullet"] = ParagraphStyle(
        "Bullet",
        parent=styles["Body"],
        leftIndent=14,
        firstLineIndent=0,
        bulletIndent=2,
        spaceAfter=3.2,
    )
    styles["Option"] = ParagraphStyle(
        "Option",
        parent=styles["Body"],
        leftIndent=11,
        spaceAfter=3.2,
    )
    styles["Caption"] = ParagraphStyle(
        "Caption",
        parent=styles["Body"],
        fontSize=8.4,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=MUTED,
        spaceBefore=3,
        spaceAfter=9,
    )
    styles["Callout"] = ParagraphStyle(
        "Callout",
        parent=styles["Body"],
        fontSize=9.2,
        leading=13.6,
        spaceAfter=0,
    )
    styles["Table"] = ParagraphStyle(
        "Table",
        parent=styles["Body"],
        fontSize=8.15,
        leading=11.1,
        spaceAfter=0,
    )
    styles["TableHead"] = ParagraphStyle(
        "TableHead",
        parent=styles["Table"],
        fontName="DVSB",
        textColor=WHITE,
        alignment=TA_LEFT,
    )
    styles["TOCHeader"] = ParagraphStyle(
        "TOCHeader",
        parent=styles["H1"],
        fontSize=20,
        leading=25,
        alignment=TA_CENTER,
        spaceAfter=15,
    )
    styles["CoverKicker"] = ParagraphStyle(
        "CoverKicker",
        parent=styles["Body"],
        fontName="DVSB",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=TEAL,
        spaceAfter=13,
    )
    styles["CoverTitle"] = ParagraphStyle(
        "CoverTitle",
        parent=styles["Body"],
        fontName="DVSB",
        fontSize=25,
        leading=32,
        alignment=TA_CENTER,
        textColor=NAVY,
        spaceAfter=9,
    )
    styles["CoverSub"] = ParagraphStyle(
        "CoverSub",
        parent=styles["Body"],
        fontName="DVSB",
        fontSize=16,
        leading=22,
        alignment=TA_CENTER,
        textColor=BLUE,
        spaceAfter=15,
    )
    styles["CoverBody"] = ParagraphStyle(
        "CoverBody",
        parent=styles["Body"],
        fontSize=10.6,
        leading=16,
        alignment=TA_CENTER,
        textColor=MUTED,
        spaceAfter=12,
    )
    return styles


def inline_markup(text: str) -> str:
    """Chuyển một tập con Markdown inline sang markup của Paragraph."""
    text = text.replace(r"\|", "|")
    escaped = html.escape(text, quote=False)

    # Bảo vệ code span trước khi xử lí bold/italic.
    code_tokens: list[str] = []

    def save_code(match):
        code_tokens.append(match.group(1))
        return f"@@CODE{len(code_tokens) - 1}@@"

    escaped = re.sub(r"`([^`]+)`", save_code, escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", escaped)

    def link(match):
        label, url = match.group(1), match.group(2)
        return f'<link href="{url}" color="#147D92"><u>{label}</u></link>'

    escaped = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", link, escaped)
    for index, code in enumerate(code_tokens):
        escaped = escaped.replace(
            f"@@CODE{index}@@", f'<font name="DVS" color="#0C6673">{code}</font>'
        )
    return escaped


def plain_text(text: str) -> str:
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return text.replace(r"\|", "|").strip()


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.strip()) for c in cells)


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith(r"\|"):
        line = line[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", line)]


def table_widths(headers: list[str], rows: list[list[str]], total_width: float) -> list[float]:
    n = len(headers)
    first = plain_text(headers[0]).lower()
    if n == 9:
        fractions = [0.28] + [0.09] * 8
    elif n == 3 and first == "câu":
        fractions = [0.08, 0.12, 0.80]
    elif n == 3 and first == "ý":
        fractions = [0.08, 0.10, 0.82]
    elif n == 3 and first == "stt":
        fractions = [0.07, 0.32, 0.61]
    elif n == 3 and first == "kí hiệu":
        fractions = [0.18, 0.52, 0.30]
    elif n == 2:
        fractions = [0.29, 0.71]
    else:
        all_rows = [headers] + rows
        weights = []
        for col in range(n):
            lengths = [min(len(plain_text(row[col])) if col < len(row) else 0, 60) for row in all_rows]
            longest = max(lengths) if lengths else 8
            average = sum(lengths) / len(lengths) if lengths else 8
            weights.append(max(7.0, min(42.0, 0.55 * longest + 0.45 * average)))
        weight_sum = sum(weights)
        fractions = [w / weight_sum for w in weights]
    return [total_width * f for f in fractions]


class ReviewDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, styles, **kwargs):
        super().__init__(filename, **kwargs)
        self.styles = styles
        self._bookmark_id = 0

    def beforeDocument(self):
        self._bookmark_id = 0

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name not in ("H1", "H2"):
            return
        level = 0 if style_name == "H1" else 1
        title = flowable.getPlainText()
        key = f"section-{self._bookmark_id}"
        self._bookmark_id += 1
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(title, key, level=level, closed=(level == 0))
        if level == 0:
            self.notify("TOCEntry", (level, title, self.page, key))


def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setTitle("Đề cương ôn tập giữa kì I — Vật lí 10 — 2026–2027")
    canvas.setAuthor("Tài liệu học tập biên soạn từ ma trận nguồn")
    canvas.setSubject("Ôn tập Vật lí 10: lý thuyết, 99 câu hỏi–đáp án, đề minh họa và lời giải")
    width, height = A4
    if doc.page > 1:
        canvas.setStrokeColor(GRID)
        canvas.setLineWidth(0.45)
        canvas.line(17 * mm, height - 14 * mm, width - 17 * mm, height - 14 * mm)
        canvas.setFont("DVS", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawString(17 * mm, height - 11.5 * mm, "VẬT LÍ 10  •  GIỮA KÌ I  •  2026–2027")
        canvas.drawRightString(width - 17 * mm, height - 11.5 * mm, "ĐỀ CƯƠNG CHUYÊN SÂU")
        canvas.line(17 * mm, 14 * mm, width - 17 * mm, 14 * mm)
        canvas.drawString(17 * mm, 10.3 * mm, "Bám sát ma trận nguồn  •  Bản học tập")
        canvas.setFont("DVSB", 7.5)
        canvas.setFillColor(NAVY)
        canvas.drawRightString(width - 17 * mm, 10.3 * mm, f"Trang {doc.page}")
    canvas.restoreState()


def cover_story(styles, question_count: int, checklist_count: int) -> list:
    story = [Spacer(1, 17 * mm)]
    story.append(Paragraph("TÀI LIỆU ÔN TẬP CHUYÊN SÂU", styles["CoverKicker"]))
    story.append(Paragraph("ĐỀ CƯƠNG<br/>GIỮA KÌ I", styles["CoverTitle"]))
    story.append(Paragraph("VẬT LÍ 10  •  2026–2027", styles["CoverSub"]))

    cards = [
        [Paragraph("<b>50 PHÚT</b>", styles["CoverBody"]), Paragraph("<b>70% TN + 30% TL</b>", styles["CoverBody"]), Paragraph("<b>10 ĐƠN VỊ</b>", styles["CoverBody"])],
    ]
    card_table = Table(cards, colWidths=[55 * mm, 55 * mm, 55 * mm], rowHeights=[20 * mm])
    card_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), PALE_TEAL),
        ("BACKGROUND", (1, 0), (1, 0), PALE_BLUE),
        ("BACKGROUND", (2, 0), (2, 0), PALE_ORANGE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BOX", (0, 0), (0, 0), 0.8, TEAL),
        ("BOX", (1, 0), (1, 0), 0.8, BLUE),
        ("BOX", (2, 0), (2, 0), 0.8, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(card_table)
    story.append(Spacer(1, 12 * mm))
    story.append(Paragraph(
        "Bám sát toàn bộ ma trận và đặc tả • Lý thuyết dễ nhớ • Ví dụ từng bước<br/>"
        f"<b>{question_count} thẻ Hỏi–Đáp • {checklist_count} mục checklist • Đề minh họa và lời giải chi tiết</b>",
        styles["CoverBody"],
    ))
    story.append(Spacer(1, 5 * mm))
    note = Table([[Paragraph(
        "<b>LƯU Ý VỀ NGUỒN</b><br/>Tệp nguồn là ma trận–đặc tả, không kèm đề thi/đáp án chính thức. "
        "Các câu hỏi luyện tập và đề minh họa trong tài liệu được biên soạn mới để phủ đúng phạm vi.",
        styles["Callout"],
    )]], colWidths=[160 * mm])
    note.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE_ORANGE),
        ("LINEBEFORE", (0, 0), (0, -1), 3, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(note)
    story.append(Spacer(1, 13 * mm))
    story.append(Paragraph(
        "Nguồn phạm vi: <i>MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx</i><br/>"
        "Phiên bản biên soạn: 23/10/2026 • Có mục lục và bookmark PDF",
        styles["CoverBody"],
    ))
    return story


def make_toc(styles) -> list:
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC1", fontName="DVSB", fontSize=9.4, leading=14,
            leftIndent=0, firstLineIndent=0, textColor=NAVY, spaceBefore=4,
        ),
        ParagraphStyle(
            "TOC2", fontName="DVS", fontSize=8.4, leading=12,
            leftIndent=14, firstLineIndent=0, textColor=INK, spaceBefore=1,
        ),
    ]
    toc.dotsMinLevel = 0
    return [
        Paragraph("MỤC LỤC", styles["TOCHeader"]),
        Paragraph("Nhấn vào mục trong danh sách hoặc bookmark để đi tới nội dung.", styles["Caption"]),
        toc,
        PageBreak(),
    ]


def callout_flowable(lines: list[str], styles, width: float):
    rendered = []
    for line in lines:
        content = line[1:].strip() if line.startswith(">") else line.strip()
        if not content:
            rendered.append("<br/>")
        else:
            rendered.append(inline_markup(content))
    first = plain_text(lines[0]).lower() if lines else ""
    background, accent = PALE, TEAL
    if first.startswith("bẫy") or first.startswith("lưu ý") or first.startswith("bốn"):
        background, accent = PALE_ORANGE, ORANGE
    elif first.startswith("chốt") or first.startswith("mẹo") or first.startswith("ưu tiên"):
        background, accent = PALE_BLUE, BLUE
    elif first.startswith("phạm vi") or first.startswith("làm rõ"):
        background, accent = PALE_TEAL, TEAL
    elif first.startswith("hỏi"):
        background, accent = PALE, colors.HexColor("#6A8CA3")
    paragraph = Paragraph("<br/>".join(rendered), styles["Callout"])
    table = Table([[paragraph]], colWidths=[width])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return [table, Spacer(1, 6)]


def build_table(headers, rows, styles, width):
    ncols = len(headers)
    compact = ncols >= 8
    body_style = styles["Table"]
    head_style = styles["TableHead"]
    if compact:
        body_style = ParagraphStyle("TableCompact", parent=styles["Table"], fontSize=6.65, leading=8.7)
        head_style = ParagraphStyle("TableCompactHead", parent=styles["TableHead"], fontSize=6.5, leading=8.4)
    data = [[Paragraph(inline_markup(cell), head_style) for cell in headers]]
    for row in rows:
        padded = row + [""] * (ncols - len(row))
        data.append([Paragraph(inline_markup(cell), body_style) for cell in padded[:ncols]])
    col_widths = table_widths(headers, rows, width)
    table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 if not compact else 2.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 if not compact else 2.5),
        ("TOPPADDING", (0, 0), (-1, -1), 4 if not compact else 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4 if not compact else 3),
    ]
    for row_index in range(1, len(data)):
        if row_index % 2 == 0:
            commands.append(("BACKGROUND", (0, row_index), (-1, row_index), PALE))
    if plain_text(headers[0]).lower() in ("câu", "ý", "stt") and ncols >= 2:
        commands.append(("ALIGN", (0, 1), (1, -1), "CENTER"))
    table.setStyle(TableStyle(commands))
    return [table, Spacer(1, 8)]


def parse_markdown(source: str, styles, root: Path, width: float) -> list:
    lines = source.splitlines()
    story = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        if not line:
            i += 1
            continue
        if line == "<!-- PAGEBREAK -->":
            story.append(PageBreak())
            i += 1
            continue
        if line.startswith("<!--"):
            i += 1
            continue
        if line.startswith(">"):
            group = []
            # Mỗi blockquote là một thẻ riêng; dòng trắng ngoài dấu > kết thúc thẻ.
            # Các dòng trắng nằm trong cùng thẻ vẫn được biểu diễn bằng một dòng chỉ có >.
            while i < len(lines) and lines[i].strip().startswith(">"):
                group.append(lines[i].strip())
                i += 1
            story.extend(callout_flowable(group, styles, width))
            continue
        if line.startswith("|") and i + 1 < len(lines) and is_table_separator(lines[i + 1]):
            headers = split_table_row(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            story.extend(build_table(headers, rows, styles, width))
            continue
        mcq = re.match(r"^\*\*Câu\s+(?:[1-9]|1[0-8])\b", line)
        if mcq:
            group = [Paragraph(inline_markup(line), styles["Body"])]
            i += 1
            option_count = 0
            while i < len(lines) and option_count < 4:
                option_line = lines[i].strip()
                if not option_line:
                    i += 1
                    continue
                if re.match(r"^[A-D]\.\s+", option_line):
                    group.append(Paragraph(inline_markup(option_line), styles["Option"]))
                    option_count += 1
                    i += 1
                    continue
                break
            if option_count != 4:
                raise ValueError(f"Câu trắc nghiệm không đủ 4 lựa chọn gần dòng: {line}")
            story.append(KeepTogether(group))
            story.append(Spacer(1, 3))
            continue
        image_match = re.fullmatch(r"!\[([^]]*)\]\(([^)]+)\)", line)
        if image_match:
            image_path = (root / image_match.group(2)).resolve()
            image = Image(str(image_path))
            max_width, max_height = 155 * mm, 92 * mm
            scale = min(max_width / image.imageWidth, max_height / image.imageHeight)
            image.drawWidth = image.imageWidth * scale
            image.drawHeight = image.imageHeight * scale
            image.hAlign = "CENTER"
            story.extend([image, Spacer(1, 3)])
            i += 1
            continue
        heading = re.match(r"^(#{1,4})\s+(.+)$", line)
        if heading:
            level = min(len(heading.group(1)), 3)
            story.append(Paragraph(inline_markup(heading.group(2)), styles[f"H{level}"]))
            i += 1
            continue
        bullet = re.match(r"^[-*]\s+(.+)$", line)
        if bullet:
            content = bullet.group(1)
            if content.startswith("☐"):
                story.append(Paragraph(inline_markup(content), styles["Bullet"]))
            else:
                story.append(Paragraph(inline_markup(content), styles["Bullet"], bulletText="•"))
            i += 1
            continue
        numbered = re.match(r"^(\d+\.)\s+(.+)$", line)
        if numbered:
            story.append(Paragraph(inline_markup(numbered.group(2)), styles["Bullet"], bulletText=numbered.group(1)))
            i += 1
            continue
        if re.match(r"^[A-D]\.\s+", line) or re.match(r"^[a-d]\)\s+", line):
            story.append(Paragraph(inline_markup(line), styles["Option"]))
            i += 1
            continue
        if re.fullmatch(r"-{3,}", line):
            story.append(Spacer(1, 5))
            i += 1
            continue
        # Ghép các dòng văn bản liên tiếp thành một đoạn, trừ khi gặp cấu trúc khác.
        paragraph_lines = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt:
                break
            if (
                nxt.startswith(("#", ">", "|", "<!--", "- "))
                or re.fullmatch(r"!\[([^]]*)\]\(([^)]+)\)", nxt)
                or re.match(r"^(\d+\.)\s+", nxt)
                or re.match(r"^[A-D]\.\s+", nxt)
                or re.match(r"^[a-d]\)\s+", nxt)
            ):
                break
            paragraph_lines.append(nxt)
            i += 1
        style = styles["Caption"] if paragraph_lines[0].startswith("*Hình") else styles["Body"]
        story.append(Paragraph(inline_markup(" ".join(paragraph_lines)), style))
    return story


def build_pdf(source_path: Path, output_path: Path) -> None:
    register_fonts()
    styles = make_styles()
    source = source_path.read_text(encoding="utf-8")
    question_count = source.count("**Hỏi ")
    checklist_count = source.count("☐")

    doc = ReviewDocTemplate(
        str(output_path),
        styles,
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=19 * mm,
        bottomMargin=18 * mm,
        title="Đề cương ôn tập giữa kì I — Vật lí 10",
        author="Tài liệu học tập biên soạn từ ma trận nguồn",
    )
    cover_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="cover-frame")
    normal_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal-frame")
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=draw_page),
        PageTemplate(id="normal", frames=[normal_frame], onPage=draw_page),
    ])

    story = cover_story(styles, question_count, checklist_count)
    story.extend([NextPageTemplate("normal"), PageBreak()])
    story.extend(make_toc(styles))
    story.extend(parse_markdown(source, styles, source_path.parent, doc.width))
    doc.multiBuild(story, maxPasses=10)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build_pdf(args.source.resolve(), args.output.resolve())
    print(args.output.resolve())
