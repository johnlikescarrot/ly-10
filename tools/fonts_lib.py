#!/usr/bin/env python3
"""Font registry + rich-text helper shared by the đề cương builder."""
import os
import re

from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')

# Be Vietnam Pro: beautiful Vietnamese grotesque (primary text font)
BVP = {
    'BVP': 'BeVietnamPro-Regular.ttf',
    'BVP-Bold': 'BeVietnamPro-Bold.ttf',
    'BVP-Italic': 'BeVietnamPro-Italic.ttf',
    'BVP-BoldItalic': 'BeVietnamPro-BoldItalic.ttf',
    'BVP-SemiBold': 'BeVietnamPro-SemiBold.ttf',
    'BVP-Medium': 'BeVietnamPro-Medium.ttf',
    'BVP-ExtraBold': 'BeVietnamPro-ExtraBold.ttf',
    # DejaVu Sans: fallback that carries Greek letters, arrows, radicals
    'Sym': 'DejaVuSans.ttf',
    'Sym-Bold': 'DejaVuSans-Bold.ttf',
    'Sym-Italic': 'DejaVuSans-Oblique.ttf',
    'Sym-BoldItalic': 'DejaVuSans-BoldOblique.ttf',
}

_registered = False
_primary_cmap = set()


def register_fonts():
    global _registered, _primary_cmap
    if _registered:
        return
    for name, fn in BVP.items():
        path = os.path.join(FONT_DIR, fn)
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        pdfmetrics.registerFont(TTFont(name, path))
    addMapping('BVP', 0, 0, 'BVP')
    addMapping('BVP', 1, 0, 'BVP-Bold')
    addMapping('BVP', 0, 1, 'BVP-Italic')
    addMapping('BVP', 1, 1, 'BVP-BoldItalic')
    addMapping('BVP', 2, 0, 'BVP-Bold')
    addMapping('BVP', 0, 2, 'BVP-Italic')
    addMapping('BVP', 1, 2, 'BVP-BoldItalic')
    addMapping('BVP', 2, 2, 'BVP-BoldItalic')

    addMapping('Sym', 0, 0, 'Sym')
    addMapping('Sym', 1, 0, 'Sym-Bold')
    addMapping('Sym', 0, 1, 'Sym-Italic')
    addMapping('Sym', 1, 1, 'Sym-BoldItalic')
    addMapping('Sym', 2, 0, 'Sym-Bold')
    addMapping('Sym', 0, 2, 'Sym-Italic')
    addMapping('Sym', 1, 2, 'Sym-BoldItalic')
    addMapping('Sym', 2, 2, 'Sym-BoldItalic')
    _registered = True

    # character coverage of the primary font
    from fontTools.ttLib import TTFont as FTFont
    f = FTFont(os.path.join(FONT_DIR, BVP['BVP']))
    for t in f['cmap'].tables:
        _primary_cmap |= set(t.cmap.keys())


# --------------------------------------------------------------------------
# Lightweight markup: **bold**, //italic//, plus raw <sub> <super> <br/>
# Characters missing from the primary font are auto-wrapped in the fallback.
# --------------------------------------------------------------------------
_TAG_RE = re.compile(r'<(/?)([a-zA-Z]+)([^<>]*?)(/?)>')
_ALLOWED_TAGS = {'sub', 'sup', 'super', 'b', 'i', 'br', 'u', 'font', 'a'}
_TAG_ALIAS = {'super': 'sup'}


_ENTITIES = {
    '&nbsp;': '\u00a0', '&middot;': '\u00b7', '&ndash;': '\u2013',
    '&mdash;': '\u2014', '&hellip;': '\u2026', '&times;': '\u00d7',
    '&rarr;': '\u2192', '&larr;': '\u2190',
}


def _esc(s):
    for k, v in _ENTITIES.items():
        s = s.replace(k, v)
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _fallback(text):
    """Wrap characters the primary font lacks in the symbol font.

    ReportLab strips whitespace that sits directly in front of a markup tag,
    so a space before a symbol would vanish.  We therefore move any trailing
    blank into the fallback span, where it keeps its width.
    """
    out = []
    buf = []

    def flush():
        nonlocal buf
        if buf:
            out.append(''.join(buf))
            buf = []

    for ch in text:
        if ord(ch) in _primary_cmap or ch in '\n\t':
            buf.append(ch)
        else:
            lead = ''
            while buf and buf[-1] == ' ':
                buf.pop()
                lead = ' ' + lead
            flush()
            out.append('<font name="Sym">%s%s</font>' % (lead, _esc(ch)))
    flush()
    return ''.join(out)


def mk(text):
    """Convert light markup to ReportLab Paragraph markup."""
    if not _primary_cmap:
        register_fonts()
    out = []
    pos = 0
    for m in _TAG_RE.finditer(text):
        out.append(_fallback(_esc(text[pos:m.start()])))
        name = m.group(2).lower()
        if name in _ALLOWED_TAGS:
            if m.group(4):          # self-closing, e.g. <br/>
                out.append('<%s%s%s/>' % (m.group(1), name, m.group(3)))
            else:
                out.append('<%s%s%s>' % (m.group(1), _TAG_ALIAS.get(name, name),
                                         m.group(3)))
        else:
            out.append(_esc(m.group(0)))
        pos = m.end()
    out.append(_fallback(_esc(text[pos:])))
    s = ''.join(out)
    # bold / italic shorthands
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s, flags=re.S)
    s = re.sub(r'(?<![*\w])\*([^*\n]+?)\*(?!\*)', r'<i>\1</i>', s)
    s = re.sub(r'//(.+?)//', r'<i>\1</i>', s, flags=re.S)
    return s
