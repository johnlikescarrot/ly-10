#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh tệp PDF đề cương ôn tập Vật lí 10 – Kiểm tra giữa kỳ I (2026–2027).

Nguồn: ``MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx``
Chạy:  python tools/build_de_cuong.py [đường/dẫn/đầu-ra.pdf]
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                NextPageTemplate, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

import fonts_lib
from fonts_lib import mk

from content_units import UNITS, THUC_HANH_TOC_DO
from content_questions import MC, PHAN_II, PHAN_III, PHAN_IV

fonts_lib.register_fonts()

# --------------------------------------------------------------------------
# Bảng màu & kích thước
# --------------------------------------------------------------------------
INK = colors.HexColor('#1B2430')
NAVY = colors.HexColor('#123A6B')
BLUE = colors.HexColor('#2F6FB0')
TEAL = colors.HexColor('#0F766E')
AMBER = colors.HexColor('#B45309')
AMBER_BG = colors.HexColor('#FDF6E7')
GREEN = colors.HexColor('#15803D')
GREEN_BG = colors.HexColor('#EEFBF2')
RED = colors.HexColor('#B91C1C')
RED_BG = colors.HexColor('#FDF1F1')
SLATE = colors.HexColor('#4A5568')
LINE = colors.HexColor('#C9D6E4')
PANEL = colors.HexColor('#F4F7FB')
PANEL2 = colors.HexColor('#EDF3FA')
WHITE = colors.white

PW, PH = A4
LM = RM = 46
TM = 58
BM = 46
CW = PW - LM - RM

DOC_TITLE = 'ĐỀ CƯƠNG ÔN TẬP VẬT LÝ 10 · KIỂM TRA GIỮA KỲ I'
SOURCE_FILE = 'MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx'

# --------------------------------------------------------------------------
# Kiểu chữ
# --------------------------------------------------------------------------
S = {}
S['body'] = ParagraphStyle('body', fontName='BVP', fontSize=10.2, leading=15.4,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5)
S['body_l'] = ParagraphStyle('body_l', parent=S['body'], alignment=TA_LEFT)
S['h1'] = ParagraphStyle('h1', fontName='BVP-ExtraBold', fontSize=17.5, leading=23,
                         textColor=NAVY, spaceBefore=4, spaceAfter=3,
                         outlineLevel=0, keepWithNext=1)
S['h1sub'] = ParagraphStyle('h1sub', fontName='BVP', fontSize=10.4, leading=14,
                            textColor=SLATE, spaceAfter=9)
S['h2'] = ParagraphStyle('h2', fontName='BVP-Bold', fontSize=13, leading=17.5,
                         textColor=NAVY, spaceBefore=13, spaceAfter=5,
                         outlineLevel=1, keepWithNext=1)
S['h3'] = ParagraphStyle('h3', fontName='BVP-SemiBold', fontSize=10.6, leading=14.5,
                         textColor=TEAL, spaceBefore=8, spaceAfter=3, keepWithNext=1)
S['h4'] = ParagraphStyle('h4', fontName='BVP-SemiBold', fontSize=9.9, leading=13.6,
                         textColor=NAVY, spaceBefore=6, spaceAfter=2, keepWithNext=1)
S['bullet'] = ParagraphStyle('bullet', parent=S['body'], leftIndent=14,
                             bulletIndent=3, spaceAfter=3.2)
S['small'] = ParagraphStyle('small', fontName='BVP', fontSize=8.7, leading=12.4,
                             textColor=SLATE)
S['smallc'] = ParagraphStyle('smallc', parent=S['small'], alignment=TA_CENTER)
S['cap'] = ParagraphStyle('cap', fontName='BVP-SemiBold', fontSize=9.3, leading=12.6,
                           textColor=SLATE, spaceBefore=2, spaceAfter=4)
S['tab'] = ParagraphStyle('tab', fontName='BVP', fontSize=8.7, leading=11.8,
                           textColor=INK)
S['tabh'] = ParagraphStyle('tabh', fontName='BVP-Bold', fontSize=8.7, leading=11.8,
                            textColor=WHITE)
S['tabhc'] = ParagraphStyle('tabhc', parent=S['tabh'], alignment=TA_CENTER)
S['tabc'] = ParagraphStyle('tabc', parent=S['tab'], alignment=TA_CENTER)
S['spec'] = ParagraphStyle('spec', fontName='BVP', fontSize=8.6, leading=11.9,
                            textColor=INK)
S['spech'] = ParagraphStyle('spech', fontName='BVP-Bold', fontSize=8.8, leading=12,
                             textColor=NAVY)
S['formula'] = ParagraphStyle('formula', fontName='BVP-Medium', fontSize=11.4,
                               leading=16, textColor=NAVY, alignment=TA_CENTER)
S['qstem'] = ParagraphStyle('qstem', fontName='BVP-SemiBold', fontSize=10.3,
                             leading=15, textColor=INK, alignment=TA_JUSTIFY,
                             spaceAfter=3)
S['qopt'] = ParagraphStyle('qopt', fontName='BVP', fontSize=9.5, leading=13.2,
                            textColor=INK)
S['qans'] = ParagraphStyle('qans', fontName='BVP-Bold', fontSize=9.9, leading=13.8,
                            textColor=GREEN)
S['qexp'] = ParagraphStyle('qexp', fontName='BVP', fontSize=9.3, leading=13.4,
                            textColor=INK, alignment=TA_JUSTIFY)
S['sol'] = ParagraphStyle('sol', fontName='BVP', fontSize=9.6, leading=13.8,
                           textColor=INK, alignment=TA_JUSTIFY, leftIndent=12,
                           spaceAfter=2.6)
S['cover_t'] = ParagraphStyle('cover_t', fontName='BVP-ExtraBold', fontSize=31,
                              leading=36, textColor=WHITE, alignment=TA_LEFT)
S['cover_s'] = ParagraphStyle('cover_s', fontName='BVP-Medium', fontSize=15.5,
                              leading=21, textColor=colors.HexColor('#CFE3F7'),
                              alignment=TA_LEFT)
S['cover_k'] = ParagraphStyle('cover_k', fontName='BVP-SemiBold', fontSize=9.2,
                              leading=12, textColor=NAVY, alignment=TA_CENTER)
S['cover_v'] = ParagraphStyle('cover_v', fontName='BVP-Bold', fontSize=11.6,
                              leading=15, textColor=INK, alignment=TA_CENTER)
S['cover_note'] = ParagraphStyle('cover_note', fontName='BVP', fontSize=9.2,
                                 leading=13.4, textColor=colors.HexColor('#D7E6F5'),
                                 alignment=TA_LEFT)


def P(text, style='body'):
    return Paragraph(mk(text), S[style])


def bullet(text, style='bullet'):
    return Paragraph(mk('•&nbsp;&nbsp;' + text), S[style])


def panel(flowables, bg=PANEL, border=LINE, border_w=0.7, pad=8, width=None):
    """Khung màu một cột chứa nhiều flowable."""
    t = Table([[flowables]], colWidths=[width or CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), border_w, border),
        ('LEFTPADDING', (0, 0), (-1, -1), pad),
        ('RIGHTPADDING', (0, 0), (-1, -1), pad),
        ('TOPPADDING', (0, 0), (-1, -1), pad - 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), pad - 1),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def note_box(title, items, bg, border, title_color, icon='●'):
    hstyle = ParagraphStyle('h4box', parent=S['h4'], textColor=title_color)
    head = Paragraph(mk('<b>%s %s</b>' % (icon, title)), hstyle)
    rows = [head]
    for it in items:
        rows.append(Paragraph(mk(it), S['body']))
    return panel(rows, bg=bg, border=border, pad=9)


# --------------------------------------------------------------------------
# Tài liệu
# --------------------------------------------------------------------------
class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        frame = Frame(LM, BM, CW, PH - TM - BM, id='main',
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='cover', frames=[frame], onPage=self.on_cover),
            PageTemplate(id='body', frames=[frame], onPage=self.on_body),
        ])
        self.section = ''
        self._page_sections = {}

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name in ('h1', 'h2'):
            txt = flowable.getPlainText()
            level = 0 if flowable.style.name == 'h1' else 1
            self.notify('TOCEntry', (level, txt, self.page))
            if level == 0:
                self.section = txt
                self._page_sections[self.page] = txt

    def on_cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, PH - 46, PW, 46, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor('#CFE3F7'))
        canv.setFont('BVP-Medium', 9.4)
        canv.drawString(LM, PH - 29, 'VẬT LÝ 10 · NĂM HỌC 2026–2027')
        canv.drawRightString(PW - RM, PH - 29, 'TÀI LIỆU ÔN TẬP')
        canv.setFillColor(colors.HexColor('#E8EFF7'))
        canv.rect(0, 0, PW, BM, stroke=0, fill=1)
        canv.restoreState()

    def on_body(self, canv, doc):
        canv.saveState()
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.6)
        canv.line(LM, PH - TM + 16, PW - RM, PH - TM + 16)
        canv.setFont('BVP-Medium', 8.2)
        canv.setFillColor(SLATE)
        canv.drawString(LM, PH - TM + 22, DOC_TITLE)
        canv.setFont('BVP', 8.2)
        head = doc._page_sections.get(doc.page, doc.section)
        if head:
            canv.drawRightString(PW - RM, PH - TM + 22, head[:64])
        canv.setStrokeColor(LINE)
        canv.line(LM, BM - 12, PW - RM, BM - 12)
        canv.setFont('BVP', 8.2)
        canv.setFillColor(SLATE)
        canv.drawString(LM, BM - 24, 'Nguồn: %s' % SOURCE_FILE)
        canv.restoreState()


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self._footer(total)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def _footer(self, total):
        self.saveState()
        self.setFont('BVP-Bold', 8.6)
        self.setFillColor(NAVY)
        self.drawRightString(PW - RM, BM - 24, 'Trang %d / %d' % (self._pageNumber, total))
        self.restoreState()


# --------------------------------------------------------------------------
# 1. TRANG BÌA
# --------------------------------------------------------------------------
def build_cover():
    st = []
    band = Table([[[P('ĐỀ CƯƠNG ÔN TẬP', 'cover_t'),
                    Spacer(1, 2),
                    P('VẬT LÝ 10', 'cover_t'),
                    Spacer(1, 6),
                    P('KIỂM TRA GIỮA KỲ I &nbsp;·&nbsp; NĂM HỌC 2026–2027', 'cover_s'),
                    Spacer(1, 12),
                    P('Tài liệu ôn tập đầy đủ theo **MA TRẬN ĐẶC TẢ** – kèm **toàn bộ câu hỏi '
                      'và đáp án** của bài kiểm tra giữa kỳ I.', 'cover_note')]]],
                  colWidths=[CW])
    band.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ('TOPPADDING', (0, 0), (-1, -1), 22),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
    ]))
    st.append(band)
    st.append(Spacer(1, 16))

    info = [
        ('HÌNH THỨC', '70% trắc nghiệm<br/>+ 30% tự luận'),
        ('THỜI GIAN', '50 phút'),
        ('SỐ CÂU', '25 câu<br/>(18 TN + 7 tự luận)'),
        ('ĐƠN VỊ KIẾN THỨC', '10 nội dung<br/>chương trình'),
    ]
    cells = []
    for k, v in info:
        cells.append([P(k, 'cover_k'), Spacer(1, 3), P(v, 'cover_v')])
    grid2 = Table([[P(info[0][0], 'cover_k'), P(info[1][0], 'cover_k'),
                    P(info[2][0], 'cover_k'), P(info[3][0], 'cover_k')],
                   [P(info[0][1], 'cover_v'), P(info[1][1], 'cover_v'),
                    P(info[2][1], 'cover_v'), P(info[3][1], 'cover_v')]],
                  colWidths=[CW / 4] * 4)
    grid2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PANEL2),
        ('BOX', (0, 0), (-1, -1), 0.8, LINE),
        ('INNERGRID', (0, 0), (-1, -1), 0.8, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, 1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 1),
    ]))
    st.append(grid2)
    st.append(Spacer(1, 14))

    st.append(P('Tài liệu này được biên soạn từ tài liệu nguồn **%s** của trường. '
                'Toàn bộ kiến thức trong ma trận đặc tả được chuyển thành đề cương ôn tập '
                'theo từng đơn vị kiến thức, kèm bộ câu hỏi – đáp án **hiện thực hoá 100%% '
                'các ô của ma trận**.' % SOURCE_FILE, 'body'))
    st.append(Spacer(1, 4))

    st.append(note_box(
        'Cách dùng tài liệu này',
        ['**① Phần 0** – Cấu trúc đề thi và bảng ma trận đặc tả gốc (để đối chiếu).',
         '**② Phần 1** – Đề cương ôn tập chi tiết cho 10 đơn vị kiến thức: kiến thức cần đạt, '
         'nội dung trọng tâm, công thức, “ghi nhớ nhanh”, bài tập mẫu có lời giải, lỗi thường gặp.',
         '**③ Phần 2** – **Toàn bộ câu hỏi và đáp án** của bài kiểm tra giữa kỳ I: '
         '18 câu trắc nghiệm, 2 câu tự luận × 4 ý, 2 câu Phần III, 3 câu Phần IV.',
         '**④ Phần 3** – Bảng đối chiếu: mỗi ô của ma trận đều có câu hỏi cụ thể tương ứng.',
         '**⑤ Phụ lục** – Bảng công thức tra nhanh, đơn vị SI, quy đổi và checklist tự ôn.'],
        colors.HexColor('#EAF2FB'), BLUE, NAVY, '▶'))

    st.append(Spacer(1, 12))
    st.append(P('Nội dung gồm 10 đơn vị kiến thức', 'h3'))
    units_line = []
    for u in UNITS:
        units_line.append('<b>%s</b>&nbsp; %s' % (u['id'], u['title']))
    units_line.append('<b>2.2b</b> Thực hành: Đo tốc độ của vật chuyển động')
    units_cell = [[Paragraph(mk('&nbsp;&nbsp;' + u), S['small']) for u in units_line[:5]],
                  [Paragraph(mk('&nbsp;&nbsp;' + u), S['small']) for u in units_line[5:]]]
    ut = Table(units_cell, colWidths=[CW / 5.0] * 5)
    ut.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
    ]))
    st.append(ut)
    st.append(Spacer(1, 14))
    tips = [
        ('Ôn theo vòng', 'Đi theo thứ tự **Biết → Hiểu → Vận dụng** cho mỗi đơn vị kiến thức, '
                          'đúng theo bố cục ma trận đề thi.'),
        ('Làm lại đề', 'Làm lại 18 câu trắc nghiệm **ba lần**, mỗi lần ghi lại những câu sai và '
                       'tìm nguyên nhân trong phần “Lỗi thường gặp”.'),
        ('Ôn liên kết', 'Ghép các mảnh kiến thức: **2.4 (gia tốc) ↔ 2.5 (CĐTBĐĐ) ↔ 2.6 (rơi tự do)**; '
                        '**2.2 (tốc độ) ↔ 2.3 (đồ thị)**.'),
    ]
    tip_cells = [[Paragraph(mk('<b>%s</b>' % t[0]), S['h4']),
                   Paragraph(mk(t[1]), S['small'])] for t in tips]
    tt = Table([tip_cells], colWidths=[CW / 3.0] * 3)
    tt.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F7FAFD')),
        ('BOX', (0, 0), (-1, -1), 0.7, LINE),
        ('INNERGRID', (0, 0), (-1, -1), 0.7, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    st.append(tt)
    st.append(Spacer(1, 12))
    st.append(P('Nguồn tài liệu: **%s** &nbsp;·&nbsp; Tài liệu ôn tập phát triển từ ma trận '
                'đặc tả của nhà trường, dùng để tự học và tự kiểm tra trước khi thi.' % SOURCE_FILE,
                'small'))
    return st


# --------------------------------------------------------------------------
# 2. MỤC LỤC
# --------------------------------------------------------------------------
def build_toc():
    ttl = ParagraphStyle('toctitle', parent=S['h1'], outlineLevel=None)
    st = [Paragraph('MỤC LỤC', ttl),
          P('Bấm vào mục lục để chuyển nhanh tới từng phần của tài liệu.', 'h1sub')]
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle('toc0', fontName='BVP-Bold', fontSize=10.4, leading=17,
                       textColor=NAVY, leftIndent=0, firstLineIndent=0,
                       spaceBefore=5, spaceAfter=1),
        ParagraphStyle('toc1', fontName='BVP', fontSize=9.5, leading=14.6,
                       textColor=INK, leftIndent=18, firstLineIndent=0,
                       spaceBefore=0.5, spaceAfter=0.5),
    ]
    st.append(toc)
    return st


# --------------------------------------------------------------------------
# 3. PHẦN 0 – CẤU TRÚC ĐỀ & MA TRẬN
# --------------------------------------------------------------------------
MATRIX_ROWS = [
    ('1.1. Làm quen với Vật lí', '1', '', '', '', '', '', '', ''),
    ('1.2. Các quy tắc an toàn trong phòng thực hành Vật lí', '1', '1', '', '', '', '', '', ''),
    ('1.3 Thực hành tính sai số trong phép đo. Ghi kết quả đo', '1', '', '', '', '', '', '', ''),
    ('2.1. Độ dịch chuyển và quãng đường đi được', '1', '2', '', '', '', '', '', ''),
    ('2.2 Tốc độ và vận tốc', '1', '', '2-I', '', '1', '', '1', ''),
    ('2.3 Đồ thị độ dịch chuyển – thời gian', '1', '1', '2-I', '', '', '', '', ''),
    ('2.4 Chuyển động biến đổi. Gia tốc', '1', '1', '', '', '', '', '', ''),
    ('2.5 Chuyển động thẳng biến đổi đều', '2', '1', '2-II', '2-II', '', '', '', '2'),
    ('2.6 Sự rơi tự do', '1', '2', '', '', '', '1', '', ''),
]
MATRIX_TOTAL = ('Tổng', '10', '8', '6', '2', '1', '1', '1', '2')

SPEC_ROWS = [
    ('1', 'Làm quen với Vật lí',
     [('Nhận biết', ['Nêu được đối tượng nghiên cứu chủ yếu của vật lí.',
                     'Biết được các thành tựu nghiên cứu của vật lí tương ứng với các cuộc cách mạng công nghiệp.',
                     'Nêu được các quá trình phát triển của vật lí.',
                     'Nêu được phương pháp nghiên cứu vật lí.']),
      ('Thông hiểu', ['Hiểu được quá trình nghiên cứu của vật lí.'])]),
    ('2', 'Các quy tắc an toàn trong phòng thực hành Vật lí',
     [('Nhận biết', ['Nêu được các nguy cơ mất an toàn trong sử dụng thiết bị thí nghiệm vật lí.',
                     'Nêu được các quy tắc an toàn trong phòng thực hành.']),
      ('Thông hiểu', ['Hiểu và sử dụng được các thiết bị thí nghiệm.',
                      'Hiểu và sử dụng các biển báo.'])]),
    ('3', 'Thực hành tính sai số trong phép đo. Ghi kết quả đo',
     [('Nhận biết', ['Nêu được phép đo trực tiếp và phép đo gián tiếp.',
                     'Biết được các loại sai số của phép đo.',
                     'Nêu được một số nguyên nhân gây ra sai số khi tiến hành thí nghiệm vật lí.',
                     'Biết được công thức giá trị trung bình, sai số tỉ đối, sai số tuyệt đối.']),
      ('Thông hiểu', ['Cách ghi đúng kết quả phép đo và sai số phép đo.',
                      'Tính được sai số tuyệt đối và sai số tỉ đối của phép đo.']),
      ('Vận dụng', ['Tính giá trị đo.', 'Tính sai số của phép đo.'])]),
    ('4', 'Độ dịch chuyển và quãng đường đi được',
     [('Nhận biết', ['Nêu được độ dịch chuyển là gì?',
                     'So sánh được độ dịch chuyển và quãng đường đi được.']),
      ('Thông hiểu', ['Xác định được độ dịch chuyển và quãng đường đi được.']),
      ('Vận dụng', ['Tính độ dịch chuyển.']),
      ('Vận dụng cao', ['Tính được độ dịch chuyển và quãng đường trong các bài toán.'])]),
    ('5', 'Tốc độ và vận tốc',
     [('Nhận biết', ['Biết được ý nghĩa và công thức của tốc độ trung bình.',
                     'Biết tốc độ tức thời.',
                     'Biết cách đo tốc độ trong cuộc sống và trong phòng thí nghiệm.',
                     'Nêu được định nghĩa vận tốc và viết được công thức tính vận tốc.',
                     'Biết được công thức cộng vận tốc.']),
      ('Thông hiểu', ['Tính được tốc độ trung bình.',
                      'Phân biệt được tốc độ và vận tốc.',
                      'Xác định được vectơ vận tốc.']),
      ('Vận dụng', ['Giải được các bài toán về tổng hợp hai vận tốc cùng phương và hai vận tốc '
                     'vuông góc với nhau.'])]),
    ('6', 'Thực hành: Đo tốc độ của vật chuyển động',
     [('Nhận biết', ['Nêu được ưu điểm và nhược điểm khi sử dụng đồng hồ đo thời gian hiện số '
                     'và cổng quang điện.',
                     'Cách sử dụng đồng hồ đo thời gian hiện số.',
                     'Ý nghĩa của việc sử dụng hai cổng quang điện.']),
      ('Thông hiểu', ['Đo được tốc độ bằng dụng cụ thực hành.'])]),
    ('7', 'Đồ thị độ dịch chuyển – thời gian',
     [('Nhận biết', ['Mô tả được chuyển động của vật dựa vào đồ thị dịch chuyển – thời gian.']),
      ('Thông hiểu', ['Tính được tốc độ từ độ dốc của đồ thị độ dịch chuyển – thời gian.',
                      'Xác định được vị trí và vận tốc của vật ở bất kì thời điểm nào dựa vào đồ thị.']),
      ('Vận dụng', ['Vẽ được đồ thị độ dịch chuyển – thời gian trong chuyển động thẳng.',
                     'Xác định được quãng đường đi được và độ dịch chuyển của vật.'])]),
    ('8', 'Chuyển động biến đổi. Gia tốc',
     [('Nhận biết', ['Biết được thế nào là chuyển động biến đổi.',
                     'Biết được quan hệ về phương và chiều của gia tốc với vận tốc.',
                     'Biết được khái niệm gia tốc, công thức tính gia tốc và đơn vị của gia tốc.']),
      ('Thông hiểu', ['Tính được độ biến thiên vận tốc, gia tốc của chuyển động.',
                      'Phân biệt được chuyển động nhanh dần và chậm dần dựa vào vận tốc và gia tốc.'])]),
    ('9', 'Chuyển động thẳng biến đổi đều',
     [('Nhận biết', ['Biết được định nghĩa của chuyển động thẳng biến đổi đều.',
                     'Biết được định nghĩa chuyển động nhanh dần đều và chuyển động chậm dần đều.',
                     'Biết được các công thức của chuyển động thẳng biến đổi đều.']),
      ('Thông hiểu', ['Sử dụng được các công thức để tính được vận tốc, gia tốc, độ dịch chuyển của vật.']),
      ('Vận dụng', ['Vận dụng giải các bài toán cơ bản về chuyển động thẳng biến đổi đều.']),
      ('Vận dụng cao', ['Vận dụng giải các bài toán nâng cao về chuyển động thẳng biến đổi đều.'])]),
    ('10', 'Rơi tự do',
     [('Nhận biết', ['Biết được định nghĩa rơi tự do.',
                     'Biết được đặc điểm của chuyển động rơi trong không khí.',
                     'Biết được các công thức của rơi tự do.']),
      ('Thông hiểu', ['Phân biệt được vật rơi gần đúng tự do và không phải rơi tự do.',
                      'Áp dụng các công thức rơi tự do tính toán các bài đơn giản.']),
      ('Vận dụng', ['Vận dụng giải quyết các bài toán về rơi tự do.'])]),
]


def build_matrix_table():
    n = 9
    w0 = 152.0
    w = (CW - w0) / 8.0
    data = [
        [P('ĐƠN VỊ KIẾN THỨC', 'tabh'), P('TRẮC NGHIỆM', 'tabhc'),
         P('', 'tabhc'), P('', 'tabhc'), P('TỰ LUẬN', 'tabhc'), P('', 'tabhc'),
         P('', 'tabhc'), P('', 'tabhc'), P('', 'tabhc')],
        [P('', 'tabh'), P('PHẦN I (18 câu)', 'tabhc'), P('', 'tabhc'),
         P('PHẦN II (2 câu, mỗi câu 4 ý)', 'tabhc'), P('', 'tabhc'),
         P('PHẦN III (2 câu)', 'tabhc'), P('', 'tabhc'), P('PHẦN IV', 'tabhc'),
         P('', 'tabhc')],
        [P('', 'tabh'), P('Biết', 'tabhc'), P('Hiểu', 'tabhc'), P('Biết', 'tabhc'),
         P('Hiểu', 'tabhc'), P('Biết', 'tabhc'), P('Hiểu', 'tabhc'),
         P('Hiểu', 'tabhc'), P('Vận dụng', 'tabhc')],
    ]
    for row in MATRIX_ROWS:
        data.append([P(row[0], 'tab')] + [P(c, 'tabc') for c in row[1:]])
    data.append([P(MATRIX_TOTAL[0], 'tabh')] + [P(c, 'tabhc') for c in MATRIX_TOTAL[1:]])

    t = Table(data, colWidths=[w0] + [w] * 8, repeatRows=3)
    style = [
        ('BACKGROUND', (0, 0), (-1, 2), NAVY),
        ('BACKGROUND', (0, 3), (-1, -2), WHITE),
        ('BACKGROUND', (0, -1), (-1, -1), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.6),
        ('SPAN', (0, 0), (0, 2)),
        ('SPAN', (1, 0), (4, 0)),
        ('SPAN', (5, 0), (8, 0)),
        ('SPAN', (1, 1), (2, 1)),
        ('SPAN', (3, 1), (4, 1)),
        ('SPAN', (5, 1), (6, 1)),
        ('SPAN', (7, 1), (8, 1)),
    ]
    t.setStyle(TableStyle(style))
    return t


SPEC_COUNTS = {
    '1': ('1 câu trắc nghiệm\n(Câu 1)', '–', '–'),
    '2': ('1 câu trắc nghiệm\n(Câu 2)', '1 câu trắc nghiệm\n(Câu 11)', '–'),
    '3': ('1 câu trắc nghiệm\n(Câu 3)', '–', '–'),
    '4': ('1 câu trắc nghiệm\n(Câu 4)', '2 câu trắc nghiệm\n(Câu 12, 13)', '–'),
    '5': ('1 câu trắc nghiệm (Câu 5)\n+ 1 câu (Phần III – Câu 1)\n+ 2 ý tự luận',
          '1 câu (Phần IV – Câu 1)', '–'),
    '6': ('Gộp vào mục 2.2', 'Gộp vào mục 2.2', 'Gộp vào mục 2.2'),
    '7': ('1 câu trắc nghiệm\n(Câu 6)', '1 câu trắc nghiệm\n(Câu 14)',
          '2 ý tự luận\n(Phần II – Câu 1)'),
    '8': ('1 câu trắc nghiệm\n(Câu 7)', '1 câu trắc nghiệm\n(Câu 15)', '–'),
    '9': ('2 câu trắc nghiệm (Câu 8, 9)\n+ 2 ý tự luận',
          '1 câu trắc nghiệm (Câu 16)\n+ 2 ý tự luận',
          '2 câu (Phần IV – Câu 2, 3)'),
    '10': ('1 câu trắc nghiệm\n(Câu 10)',
           '2 câu trắc nghiệm (Câu 17, 18)\n+ 1 câu (Phần III – Câu 2)', '–'),
}


def build_spec_table():
    data = [[P('TT', 'tabhc'), P('Nội dung đơn vị kiến thức / kỹ năng', 'tabh'),
             P('Mức độ kiến thức, kỹ năng cần kiểm tra, đánh giá', 'tabh'),
             P('Số câu hỏi theo mức độ nhận thức\n(đã hiện thực hoá)', 'tabhc')]]
    for tt, name, spec in SPEC_ROWS:
        cell = []
        for level, items in spec:
            cell.append(Paragraph(mk('<b>%s:</b>' % level), S['spech']))
            for it in items:
                cell.append(Paragraph(mk('– ' + it), S['spec']))
            cell.append(Spacer(1, 2))
        nb, th, vd = SPEC_COUNTS[tt]
        cnt = [Paragraph(mk('<b>Nhận biết</b>\n' + nb), S['tabc']),
               Paragraph(mk('<b>Thông hiểu</b>\n' + th), S['tabc']),
               Paragraph(mk('<b>Vận dụng</b>\n' + vd), S['tabc'])]
        data.append([P(tt, 'tabc'), P(name, 'tab'), cell, cnt])
    t = Table(data, colWidths=[24, 104, 281, CW - 24 - 104 - 281], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('SPAN', (2, 0), (3, 0)),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (3, 0), (3, 0), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    return t


def build_part0():
    st = [P('PHẦN 0 · CẤU TRÚC ĐỀ THI VÀ MA TRẬN ĐẶC TẢ', 'h1'),
          P('Phần này trích nguyên văn từ tài liệu nguồn, làm cơ sở để đối chiếu với '
            'đề cương ôn tập (Phần 1) và bộ câu hỏi – đáp án (Phần 2).', 'h1sub')]

    st.append(P('0.1. Thông tin chung về đề kiểm tra giữa kỳ I', 'h2'))
    info = [
        ('Môn học', 'Vật lí 10'),
        ('Năm học', '2026–2027'),
        ('Hình thức kiểm tra', '70% trắc nghiệm + 30% tự luận'),
        ('Thời gian làm bài', '50 phút'),
        ('Phần I', 'Trắc nghiệm – 18 câu (10 “Biết” + 8 “Hiểu”)'),
        ('Phần II', 'Tự luận – 2 câu, mỗi câu 4 ý (6 ý “Biết” + 2 ý “Hiểu”)'),
        ('Phần III', '2 câu (1 “Biết” + 1 “Hiểu”)'),
        ('Phần IV', '3 câu (1 “Hiểu” + 2 “Vận dụng”)'),
        ('Tổng số câu', '25 câu trên 10 đơn vị kiến thức'),
    ]
    rows = [[P(k, 'tab'), P(v, 'tab')] for k, v in info]
    t = Table(rows, colWidths=[132, CW - 132])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), PANEL2),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.4),
    ]))
    st.append(t)

    st.append(P('0.2. Ma trận đề thi (ma trận đặc tả)', 'h2'))
    st.append(P('Bảng dưới đây được trích nguyên văn từ tài liệu nguồn. Các ký hiệu '
                '**2-I** và **2-II** trong cột “Tự luận – Phần II” chỉ số **ý** thuộc câu I và '
                'câu II của Phần II (mỗi câu gồm 4 ý).', 'body'))
    st.append(Spacer(1, 4))
    st.append(build_matrix_table())
    st.append(Spacer(1, 6))
    st.append(note_box(
        'Cách đọc ma trận',
        ['**Tổng cột “Biết” của Phần I = 10**, **“Hiểu” = 8** ⇒ đúng **18 câu** trắc nghiệm '
         'như đề đã ghi ở hàng tiêu đề.',
         '**Tổng cột của Phần II = 6 + 2 = 8 ý** ⇒ đúng **2 câu × 4 ý = 8 ý**.',
         '**Phần III = 1 + 1 = 2 câu**; **Phần IV = 1 + 2 = 3 câu** ⇒ tổng cộng **25 câu**.',
         'Lưu ý: trong tệp nguồn, hàng tiêu đề gộp “TRẮC NGHIỆM” trên 6 cột đầu và “TỰ LUẬN” '
         'trên 2 cột cuối. Cách hiểu nhất quán với các con số ghi trong ma trận là: **Phần I** '
         '(18 câu) là trắc nghiệm; **Phần II** (2 câu × 4 ý) là tự luận; **Phần III** (2 câu) '
         'và **Phần IV** (3 câu) là các phần bài toán. Bộ câu hỏi trong Phần 2 của tài liệu này '
         'được xây dựng theo đúng cách hiểu đó.'],
        colors.HexColor('#EAF2FB'), BLUE, NAVY, 'ℹ'))

    st.append(P('0.3. Đặc tả nội dung kiến thức – kỹ năng và mức độ nhận thức', 'h2'))
    st.append(P('Cột 2 và cột 3 trích nguyên văn theo bảng “ĐẶC TẢ ĐỀ KIỂM TRA GIỮA HKI '
                'VẬT LÝ 10” trong tài liệu nguồn. Cột 4 được **bổ sung** để chỉ rõ mỗi yêu cầu '
                'đã được kiểm tra ở câu nào trong bộ đề của Phần 2.', 'body'))
    st.append(Spacer(1, 4))
    st.append(build_spec_table())
    st.append(Spacer(1, 4))
    st.append(P('*Ghi chú về bản gốc:* ở mục 1.3, tài liệu nguồn ghi “sai số **tỉ đổi**”; '
                'đó là cách viết của “sai số **tỉ đối**” và được giữ nguyên khi trích dẫn.', 'small'))

    st.append(P('0.4. Phân bổ điểm dự kiến của đề', 'h2'))
    dist = [
        ['Phần', 'Dạng câu hỏi', 'Số câu', 'Mức độ', 'Điểm (dự kiến)', 'Nội dung trọng tâm'],
        ['I', 'Trắc nghiệm', '18', 'Biết 10 – Hiểu 8', '18 × 0,35 = 6,3', 'Mục 1.1 → 2.6'],
        ['II', 'Tự luận (4 ý/câu)', '2', 'Biết 6 ý – Hiểu 2 ý', '2 × 0,75 = 1,5',
         '2.2 (2 ý) + 2.3 (2 ý) ; 2.5 (4 ý)'],
        ['III', 'Bài toán ngắn', '2', 'Biết 1 – Hiểu 1', '2 × 0,5 = 1,0', '2.2 ; 2.6'],
        ['IV', 'Bài toán tổng hợp', '3', 'Hiểu 1 – Vận dụng 2', '3 × 0,5 = 1,5', '2.2 ; 2.5 (2 câu)'],
        ['', 'Tổng', '25', '', '10,0', ''],
    ]
    data = [[P(c, 'tabh' if i in (0, len(dist) - 1) else 'tab') for c in r]
            for i, r in enumerate(dist)]
    t = Table(data, colWidths=[34, 86, 38, 108, 78, CW - 344], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, -1), (-1, -1), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (2, 1), (4, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.6),
    ]))
    st.append(t)
    st.append(Spacer(1, 6))
    st.append(P('Cách phân bổ điểm trên là **dự kiến theo thể lệ 70% trắc nghiệm + 30% tự luận** '
                'ghi trong tài liệu nguồn, nhằm đối chiếu với tổng số câu và mức độ trong ma trận. '
                'Thang điểm chi tiết do giáo viên xác định.', 'small'))
    return st


# --------------------------------------------------------------------------
# 4. PHẦN 1 – ĐỀ CƯƠNG ÔN TẬP
# --------------------------------------------------------------------------
def build_unit(unit):
    st = []
    ubox = ParagraphStyle('h2box', parent=S['h2'], outlineLevel=None,
                          spaceBefore=0, spaceAfter=0)
    ubox2 = ParagraphStyle('h2box2', parent=ubox, fontSize=12.2, leading=16.5)
    head = Table([[Paragraph(mk('<b>%s</b>' % unit['id']), ubox),
                   Paragraph(mk(unit['title']), ubox2),
                   Paragraph(mk(unit['badge']), S['small'])]],
                 colWidths=[36, CW - 36 - 118, 118])
    head.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PANEL2),
        ('LINEBEFORE', (0, 0), (0, -1), 3.2, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    st.append(head)
    st.append(Spacer(1, 7))

    # 1) Kiến thức cần đạt theo đặc tả
    st.append(P('Kiến thức cần đạt (theo đặc tả)', 'h3'))
    spec_cell = []
    for level, items in unit['spec']:
        spec_cell.append(Paragraph(mk('<b>%s:</b>' % level), S['spech']))
        for it in items:
            spec_cell.append(Paragraph(mk('– ' + it), S['spec']))
        spec_cell.append(Spacer(1, 1))
    st.append(panel(spec_cell, bg=colors.HexColor('#FAFCFE'), border=LINE, pad=8))
    st.append(Spacer(1, 7))

    # 2) Mục tiêu ôn tập
    st.append(P('Mục tiêu ôn tập', 'h3'))
    for o in unit['objectives']:
        st.append(bullet(o))
    st.append(Spacer(1, 3))

    # 3) Nội dung trọng tâm
    st.append(P('Nội dung trọng tâm', 'h3'))
    for topic, text in unit['knowledge']:
        st.append(P(topic, 'h4'))
        st.append(P(text, 'body'))
    st.append(Spacer(1, 2))

    # 4) Ghi nhớ nhanh
    st.append(note_box('Ghi nhớ nhanh', unit['memory'], AMBER_BG, AMBER, AMBER, '★'))

    # 5) Bài tập mẫu
    ex = unit['example']
    if ex:
        st.append(Spacer(1, 6))
        st.append(P('Bài tập vận dụng mẫu', 'h3'))
        body = [Paragraph(mk('<b>Đề bài:</b> ' + ex['problem']), S['body'])]
        for i, sline in enumerate(ex['solution']):
            body.append(Paragraph(mk(sline), S['sol']))
        body.append(Spacer(1, 2))
        body.append(Paragraph(mk('<b>Đáp án:</b> ' + ex['answer']), S['qans']))
        st.append(panel(body, bg=colors.HexColor('#F7FAFD'), border=LINE, pad=9))

    # 6) Lỗi thường gặp
    st.append(Spacer(1, 6))
    st.append(note_box('Lỗi thường gặp – cần tránh', unit['pitfalls'], RED_BG, RED, RED, '✖'))

    # 7) Liên hệ với đề thi
    st.append(Spacer(1, 5))
    st.append(note_box('Câu hỏi tương ứng trong đề kiểm tra', unit['links'],
                        GREEN_BG, GREEN, GREEN, '✔'))
    return st


def build_part1():
    st = [P('PHẦN 1 · ĐỀ CƯƠNG ÔN TẬP CHI TIẾT THEO 10 ĐƠN VỊ KIẾN THỨC', 'h1'),
          P('Mỗi đơn vị kiến thức được trình bày theo cùng một cấu trúc: kiến thức cần đạt '
            '(theo đặc tả) → mục tiêu ôn tập → nội dung trọng tâm → “ghi nhớ nhanh” → '
            'bài tập mẫu có lời giải → lỗi thường gặp → câu hỏi tương ứng trong đề.', 'h1sub')]
    for u in UNITS:
        st += build_unit(u)
    st += build_unit(THUC_HANH_TOC_DO)
    return st


# --------------------------------------------------------------------------
# 5. PHẦN 2 – BỘ CÂU HỎI VÀ ĐÁP ÁN
# --------------------------------------------------------------------------
def mc_block(q):
    st = []
    head = Table([[Paragraph(mk('<b>Câu %d.</b>' % q['no']), S['qstem']),
                   Paragraph(mk('<font color="#5A6472">(%s – %s)</font>' % (q['unit'], q['level'])),
                             S['small'])]],
                 colWidths=[CW - 190, 190])
    head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    st.append(head)
    st.append(Paragraph(mk(q['stem']), S['qstem']))

    letters = ['A', 'B', 'C', 'D']
    opt_cells = []
    for i, opt in enumerate(q['options']):
        opt_cells.append(Paragraph(mk('<b>%s.</b> %s' % (letters[i], opt)), S['qopt']))
    t = Table([[opt_cells[0], opt_cells[1]], [opt_cells[2], opt_cells[3]]],
              colWidths=[CW / 2, CW / 2])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 1.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.4),
    ]))
    st.append(t)

    ans = [Paragraph(mk('✔ <b>Đáp án: %s</b>' % q['answer']), S['qans']),
           Paragraph(mk('<b>Giải thích:</b> ' + q['explain']), S['qexp'])]
    st.append(panel(ans, bg=GREEN_BG, border=GREEN, border_w=0.7, pad=7))
    st.append(Spacer(1, 6))
    return st


def written_block(q, part_label):
    st = []
    head = Table([[Paragraph(mk('<b>%s · Câu %d.</b>' % (part_label, q['no'])), S['qstem']),
                   Paragraph(mk('<font color="#5A6472">(%s – %s)</font>'
                                % (q['unit'], q.get('level', 'Tự luận'))), S['small'])]],
                 colWidths=[CW - 190, 190])
    head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    st.append(head)
    st.append(Paragraph(mk(q['topic']), S['h4']))
    st.append(Paragraph(mk(q['stem']), S['qstem']))
    st.append(Spacer(1, 2))
    for tag, ask, steps in q['parts']:
        st.append(Paragraph(mk('<b>%s</b> %s' % (tag, ask)), S['qstem']))
        body = [Paragraph(mk('<b>Lời giải:</b>'), S['h4'])]
        for sline in steps:
            body.append(Paragraph(mk(sline), S['sol']))
        st.append(panel(body, bg=colors.HexColor('#F7FAFD'), border=LINE, pad=8))
        st.append(Spacer(1, 4))
    st.append(Spacer(1, 4))
    return st


def build_part2():
    st = [P('PHẦN 2 · TOÀN BỘ CÂU HỎI VÀ ĐÁP ÁN CỦA BÀI KIỂM TRA GIỮA KỲ I', 'h1'),
          P('Bộ câu hỏi dưới đây được xây dựng từ ma trận đặc tả để **hiện thực hoá 100% các ô '
            'của ma trận**: mỗi ô đều có câu hỏi cụ thể tương ứng, kèm đáp án và lời giải. '
            'Đáp án trắc nghiệm được in ngay dưới từng câu để học sinh tự kiểm tra.', 'h1sub')]

    st.append(note_box(
        'Cấu trúc bộ câu hỏi',
        ['**Phần I – Trắc nghiệm:** 18 câu, trắc nghiệm 4 lựa chọn A–B–C–D '
         '(10 câu “Biết”, 8 câu “Hiểu”).',
         '**Phần II – Tự luận:** 2 câu, mỗi câu 4 ý (ý a, b, c, d), có lời giải chi tiết từng ý.',
         '**Phần III:** 2 câu (1 câu “Biết” về 2.2, 1 câu “Hiểu” về 2.6).',
         '**Phần IV:** 3 câu (1 câu “Hiểu” về 2.2, 2 câu “Vận dụng” về 2.5).'],
        colors.HexColor('#EAF2FB'), BLUE, NAVY, '▶'))

    st.append(P('2.1. PHẦN I – TRẮC NGHIỆM (18 câu)', 'h2'))
    st.append(P('Chọn một phương án đúng nhất.', 'small'))
    st.append(Spacer(1, 4))
    for q in MC:
        st += mc_block(q)

    # bảng đáp án Phần I
    st.append(P('Bảng đáp án Phần I – Trắc nghiệm', 'h3'))
    st.append(build_mc_answer_table())
    st.append(Spacer(1, 8))

    st.append(P('2.2. PHẦN II – TỰ LUẬN (2 câu, mỗi câu 4 ý)', 'h2'))
    for q in PHAN_II:
        st += written_block(q, 'Phần II')

    st.append(P('2.3. PHẦN III (2 câu)', 'h2'))
    for q in PHAN_III:
        st += written_block(q, 'Phần III')

    st.append(P('2.4. PHẦN IV (3 câu)', 'h2'))
    for q in PHAN_IV:
        st += written_block(q, 'Phần IV')

    st.append(P('2.5. Bảng tổng hợp đáp án toàn bộ đề', 'h2'))
    st.append(build_full_answer_table())
    return st


def build_mc_answer_table():
    letters = ['A', 'B', 'C', 'D']
    rows = []
    for i in range(0, 18, 9):
        r1 = [P('<b>Câu</b>', 'tabhc')]
        r2 = [P('<b>ĐA</b>', 'tabhc')]
        for q in MC[i:i + 9]:
            r1.append(P(str(q['no']), 'tabc'))
            r2.append(P('<b>%s</b>' % q['answer'], 'tabc'))
        rows.append(r1)
        rows.append(r2)
    w = [46] + [(CW - 46) / 9.0] * 9
    t = Table(rows, colWidths=w)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, 1), (-1, 1), GREEN_BG),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.4),
    ]))
    return t


def build_full_answer_table():
    rows = [[P('Câu', 'tabhc'), P('Nội dung', 'tabh'), P('Mức độ', 'tabhc'),
             P('Đáp án', 'tabhc'), P('Câu', 'tabhc'), P('Nội dung', 'tabh'),
             P('Mức độ', 'tabhc'), P('Đáp án', 'tabhc')]]
    mc_ans = {q['no']: (q['unit'], q['level'], q['answer']) for q in MC}
    entries = []
    for q in MC:
        entries.append((str(q['no']), 'Trắc nghiệm', q['unit'], q['level'], q['answer']))
    for q in PHAN_II:
        entries.append(('II.%d' % q['no'], 'Tự luận', q['unit'], '4 ý', 'Có lời giải'))
    for q in PHAN_III:
        entries.append(('III.%d' % q['no'], 'Bài toán', q['unit'], q['level'], 'Có lời giải'))
    for q in PHAN_IV:
        entries.append(('IV.%d' % q['no'], 'Bài toán', q['unit'], q['level'], 'Có lời giải'))
    half = (len(entries) + 1) // 2
    left, right = entries[:half], entries[half:]
    for i in range(half):
        l = left[i]
        r = right[i] if i < len(right) else ('', '', '', '', '')
        rows.append([P(l[0], 'tabc'), P(l[1] + ' – ' + l[2], 'tab'), P(l[3], 'tabc'),
                     P(l[4], 'tabc'),
                     P(r[0], 'tabc'), P(r[1] + ' – ' + r[2], 'tab'), P(r[3], 'tabc'),
                     P(r[4], 'tabc')])
    t = Table(rows, colWidths=[30, 120, 52, 34, 30, 120, 52, CW - 438], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.2),
    ]))
    return t


# --------------------------------------------------------------------------
# 6. PHẦN 3 – ĐỐI CHIẾU MA TRẬN ↔ CÂU HỎI
# --------------------------------------------------------------------------
MAPPING = [
    # (đơn vị kiến thức, P1 Biết, P1 Hiểu, P2 Biết, P2 Hiểu, P3 Biết, P3 Hiểu, P4 Hiểu, P4 VDN)
    ('1.1. Làm quen với Vật lí', 'Câu 1', '', '', '', '', '', '', ''),
    ('1.2. Các quy tắc an toàn', 'Câu 2', 'Câu 11', '', '', '', '', '', ''),
    ('1.3. Sai số trong phép đo', 'Câu 3', '', '', '', '', '', '', ''),
    ('2.1. Độ dịch chuyển – quãng đường', 'Câu 4', 'Câu 12, 13', '', '', '', '', '', ''),
    ('2.2. Tốc độ và vận tốc', 'Câu 5', '', 'Câu 1 (ý a, b)', '', 'Câu 1', '', 'Câu 1', ''),
    ('2.3. Đồ thị độ dịch chuyển – thời gian', 'Câu 6', 'Câu 14', 'Câu 1 (ý c, d)',
     '', '', '', '', ''),
    ('2.4. Chuyển động biến đổi. Gia tốc', 'Câu 7', 'Câu 15', '', '', '', '', '', ''),
    ('2.5. Chuyển động thẳng biến đổi đều', 'Câu 8, 9', 'Câu 16', 'Câu 2 (ý a, b)',
     'Câu 2 (ý c, d)', '', '', '', 'Câu 2, 3'),
    ('2.6. Sự rơi tự do', 'Câu 10', 'Câu 17, 18', '', '', '', 'Câu 2', '', ''),
]


def build_part3():
    st = [P('PHẦN 3 · ĐỐI CHIẾU MA TRẬN ĐỀ VỚI CÂU HỎI', 'h1'),
          P('Bảng dưới đây chứng minh rằng **mọi ô của ma trận đặc tả đều được hiện thực hoá** '
            'bằng câu hỏi cụ thể trong bộ đề của Phần 2.', 'h1sub')]
    rows = [[P('Đơn vị kiến thức', 'tabh'), P('P1 – Biết', 'tabhc'), P('P1 – Hiểu', 'tabhc'),
             P('P2 – Biết', 'tabhc'), P('P2 – Hiểu', 'tabhc'), P('P3 – Biết', 'tabhc'),
             P('P3 – Hiểu', 'tabhc'), P('P4 – Hiểu', 'tabhc'), P('P4 – Vận dụng', 'tabhc')]]
    for r in MAPPING:
        rows.append([P(r[0], 'tab')] + [P(c, 'tabc') for c in r[1:]])
    rows.append([P('Tổng', 'tabh'), P('10 câu', 'tabhc'), P('8 câu', 'tabhc'),
                 P('6 ý', 'tabhc'), P('2 ý', 'tabhc'), P('1 câu', 'tabhc'),
                 P('1 câu', 'tabhc'), P('1 câu', 'tabhc'), P('2 câu', 'tabhc')])
    w0 = 138.0
    t = Table(rows, colWidths=[w0] + [(CW - w0) / 8.0] * 8, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, -1), (-1, -1), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.6),
    ]))
    st.append(t)
    st.append(Spacer(1, 8))

    st.append(P('Kiểm tra độ đầy đủ của ma trận', 'h3'))
    checks = [
        'Phần I: 10 câu “Biết” (câu 1–10) và 8 câu “Hiểu” (câu 11–18) → **đúng 18 câu**.',
        'Phần II: câu 1 gồm 2 ý “Biết” về 2.2 và 2 ý “Biết” về 2.3; câu 2 gồm 2 ý “Biết” và '
        '2 ý “Hiểu” về 2.5 → **đúng 2 câu × 4 ý**.',
        'Phần III: câu 1 “Biết” về 2.2, câu 2 “Hiểu” về 2.6 → **đúng 2 câu**.',
        'Phần IV: câu 1 “Hiểu” về 2.2, câu 2 và câu 3 “Vận dụng” về 2.5 → **đúng 3 câu**.',
        'Tổng cộng **25 câu** với đầy đủ đáp án và lời giải.',
    ]
    for c in checks:
        st.append(bullet(c))
    return st


# --------------------------------------------------------------------------
# 7. PHỤ LỤC
# --------------------------------------------------------------------------
def build_appendix():
    st = [P('PHỤ LỤC · BẢNG TRA NHANH', 'h1'),
          P('Các bảng dưới đây được thiết kế để in ra dán bên bàn học hoặc dùng làm “phao cứu” '
            'khi làm bài kiểm tra.', 'h1sub')]

    st.append(P('A. Bảng công thức trọng tâm', 'h2'))
    formulas = [
        ['Nội dung', 'Công thức', 'Ghi chú'],
        ['Tốc độ trung bình', 'v = s/t', 'vô hướng; 1 m/s = 3,6 km/h'],
        ['Tốc độ tức thời', 'v = Δs/Δt (Δt rất nhỏ)', 'vô hướng'],
        ['Vận tốc (vectơ)', '**v** = **Δr**/Δt', 'có hướng'],
        ['Cộng vận tốc cùng phương', 'v = v₁ + v₂ (cùng chiều) ; v = |v₁ − v₂| (ngược chiều)',
         'dùng cho bài tổng hợp'],
        ['Cộng vận tốc vuông góc', 'v = √(v₁² + v₂²)', 'định lý Pythagore'],
        ['Gia tốc (vectơ)', '**a** = **Δv**/Δt', 'đơn vị m/s²'],
        ['CĐTBĐĐ', 'v = v₀ + at ; s = v₀t + ½at² ; s = ½(v₀ + v)t ; v² − v₀² = 2as',
         'a không đổi'],
        ['Rơi tự do', 'v = gt ; s = ½gt² ; v² = 2gs', 'g = 9,8 m/s² (một số bài lấy 10 m/s²)'],
        ['Giá trị trung bình', 'x̄ = (x₁ + x₂ + … + xₙ)/n', 'n số lần đo'],
        ['Sai số tuyệt đối', 'Δx = |x̄ − x|', 'luôn không âm'],
        ['Sai số tỉ đối', 'δ = Δx/x̄ × 100%', 'không có đơn vị'],
        ['Ghi kết quả đo', 'x̄ ± Δx', 'giữ 1 chữ số đầu của Δx (2 nếu chữ số đầu là 1)'],
        ['Độ dốc đồ thị x–t', 'v = Δx/Δt', 'độ dốc = tốc độ'],
    ]
    data = [[P(c, 'tabh') for c in formulas[0]]]
    for r in formulas[1:]:
        data.append([P(r[0], 'tab'), P(r[1], 'tab'), P(r[2], 'tab')])
    t = Table(data, colWidths=[118, 214, CW - 332], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.6),
    ]))
    st.append(t)

    st.append(P('B. Đơn vị đo và quy đổi thường dùng', 'h2'))
    units = [
        ['Đại lượng', 'Kí hiệu', 'Đơn vị SI', 'Ghi chú quy đổi'],
        ['Độ dài (quãng đường, độ dịch chuyển)', 's, Δr', 'm (mét)', '1 km = 1000 m'],
        ['Thời gian', 't', 's (giây)', '1 phút = 60 s'],
        ['Tốc độ, vận tốc', 'v', 'm/s', 'v(km/h) = 3,6 × v(m/s)'],
        ['Gia tốc', 'a', 'm/s²', '–'],
        ['Khối lượng', 'm', 'kg', '1 t = 1000 kg'],
        ['Gia tốc rơi tự do', 'g', 'm/s²', 'g ≈ 9,8 m/s² (một số bài lấy 10 m/s²)'],
        ['Sai số tuyệt đối', 'Δx', 'cùng đơn vị với x', '–'],
        ['Sai số tỉ đối', 'δ', 'không có đơn vị', '–'],
    ]
    data = [[P(c, 'tabh') for c in units[0]]]
    for r in units[1:]:
        data.append([P(r[0], 'tab'), P(r[1], 'tabc'), P(r[2], 'tabc'), P(r[3], 'tab')])
    t = Table(data, colWidths=[168, 62, 92, CW - 322], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ('BOX', (0, 0), (-1, -1), 0.9, NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.6),
    ]))
    st.append(t)

    st.append(P('C. Checklist tự ôn trước khi thi', 'h2'))
    checklist = [
        ('Mức “Biết” – 10 câu trắc nghiệm', [
            'Nêu được đối tượng nghiên cứu, thành tựu, quá trình phát triển và phương pháp nghiên cứu vật lí.',
            'Nêu được nguy cơ mất an toàn và các quy tắc an toàn trong phòng thực hành.',
            'Nhớ công thức giá trị trung bình, sai số tuyệt đối, sai số tỉ đối.',
            'Phân biệt độ dịch chuyển (vectơ) và quãng đường đi được (vô hướng).',
            'Phân biệt tốc độ (vô hướng) và vận tốc (có hướng); nhớ công thức cộng vận tốc.',
            'Biết độ dốc đồ thị x–t là tốc độ.',
            'Biết gia tốc đặc trưng cho tốc độ thay đổi, đơn vị m/s².',
            'Biết định nghĩa CĐTBĐĐ và công thức v = v₀ + at.',
            'Biết vật rơi tự do có gia tốc bằng g, hướng thẳng xuống.',
        ]),
        ('Mức “Hiểu” – 8 câu trắc nghiệm', [
            'Hiểu và sử dụng được biển báo an toàn.',
            'Xác định được quãng đường đi được và độ dịch chuyển trong tình huống đi vòng.',
            'Phân biệt chuyển động thẳng và chuyển động cong đều.',
            'Đọc được đồ thị x–t: dấu của vận tốc, tính được tốc độ.',
            'Phân biệt nhanh dần – chậm dần theo quan hệ phương chiều của a và v.',
            'Nhận biết điều kiện chuyển động nhanh dần đều (a và v₀ cùng dấu).',
            'Giải thích được vì sao vật rơi gần đúng tự do, phân biệt với rơi tự do trong chân không.',
        ]),
        ('Tự luận – Phần II, III, IV', [
            'Tính tốc độ trung bình, quy đổi km/h ↔ m/s, tính tổng hợp vận tốc.',
            'Vẽ và đọc đồ thị độ dịch chuyển – thời gian.',
            'Chọn đúng công thức CĐTBĐĐ theo dữ kiện bài cho, tính v, a, s, t.',
            'Tìm thời điểm và quãng đường khi vật dừng lại (v = 0).',
            'Đo tốc độ bằng hai cổng quang điện: Δt = t₂ − t₁, v = L/Δt.',
            'Giải bài rơi tự do và so sánh rơi trong không khí với rơi trong chân không.',
        ]),
    ]
    chk = ParagraphStyle('chk', parent=S['bullet'], fontSize=9.4, leading=13.0,
                         spaceAfter=1.4, textColor=INK)
    for title, items in checklist:
        st.append(P(title, 'h3'))
        half = (len(items) + 1) // 2
        left = items[:half]
        right = items[half:]
        cells = [[Paragraph(mk('☐&nbsp;&nbsp;' + x), chk) for x in left],
                 [Paragraph(mk('☐&nbsp;&nbsp;' + x), chk) for x in right]]
        nrows = max(len(left), len(right))
        while len(cells[0]) < nrows:
            cells[0].append(Paragraph('', chk))
        while len(cells[1]) < nrows:
            cells[1].append(Paragraph('', chk))
        tb = Table([[cells[0][i], cells[1][i]] for i in range(nrows)],
                   colWidths=[CW / 2 - 4, CW / 2 - 4])
        tb.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        st.append(tb)
    st.append(Spacer(1, 6))
    st.append(note_box(
        'Cách đọc kí hiệu',
        ['**Chữ in đật** (v, Δr, a, Δv) biểu thị **đại lượng vectơ** – có hướng.',
         '**Giá trị trung bình** được kí hiệu bằng x̄ (đọc là “x trung bình”).',
         'Chỉ số dưới (v<sub>0</sub>) là **vận tốc đầu**, chỉ số trên (t<sup>2</sup>) là **bậc hai**.',
         '“TN” = trắc nghiệm; “TL” = tự luận; “NB/TH/VD” = Nhận biết / Thông hiểu / Vận dụng.',
         '**Câu hỏi trong đề** được đánh số theo Phần (I.1 → I.18, II.1 → II.2, III.1 → III.2, IV.1 → IV.3).'],
        colors.HexColor('#EAF2FB'), BLUE, NAVY, 'ℹ'))
    st.append(Spacer(1, 6))
    st.append(note_box(
        'Lời nhắc cuối bài',
        ['Đọc kỹ đề, chú ý đơn vị và dấu của các đại lượng.',
         'Câu trắc nghiệm: ưu tiên loại trừ – dùng **điều kiện đủ để loại**, rồi mới so sánh đáp án.',
         'Câu tự luận: viết **“Cho” / “Tìm”** rõ ràng, thay số và ghi đơn vị ở **mỗi kết quả**, '
         'kể cả kết quả trung gian.',
         'Kiểm tra lại: đơn vị, dấu, độ chính xác (số lẻ gần đúng), và câu nào còn bỏ trống.'],
        AMBER_BG, AMBER, AMBER, '★'))
    return st


# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------
def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(HERE),
        'ĐỀ CƯƠNG ÔN TẬP VẬT LÝ 10 - KIỂM TRA GIỮA KỲ I 2026-2027.pdf')

    doc = Doc(out, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM,
              bottomMargin=BM, title='Đề cương ôn tập Vật lí 10 – Kiểm tra giữa kỳ I 2026-2027',
              author='GV', subject='Vật lí 10 – Kiểm tra giữa kỳ I (2026–2027)',
              keywords='vật lí 10, ma trận đặc tả, kiểm tra giữa kỳ I, đề cương ôn tập')
    story = []
    story += build_cover()
    story.append(NextPageTemplate('body'))
    story.append(PageBreak())
    story += build_toc()
    story.append(PageBreak())
    story += build_part0()
    story.append(PageBreak())
    story += build_part1()
    story.append(PageBreak())
    story += build_part2()
    story.append(PageBreak())
    story += build_part3()
    story.append(PageBreak())
    story += build_appendix()

    doc.multiBuild(story, canvasmaker=NumberedCanvas)
    print('Đã tạo:', out)
    print('Dung lượng: %.1f KB' % (os.path.getsize(out) / 1024.0))


if __name__ == '__main__':
    main()
