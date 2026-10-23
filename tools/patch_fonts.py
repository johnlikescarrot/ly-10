#!/usr/bin/env python3
"""Patch the primary fonts so combining macron (U+0304) over-lays the base letter.

ReportLab does not apply GPOS mark-to-base positioning, so a combining macron
drawn after 'x' would float to the right of the letter.  TTF advance widths
cannot be negative, so instead we translate the macron's outline horizontally
so the bar lands centred on top of the preceding letter.  The mark keeps its
zero advance width, so the metrics of the surrounding text stay correct.
"""
import json
import os

from fontTools.ttLib import TTFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
TARGETS = [
    'BeVietnamPro-Regular.ttf',
    'BeVietnamPro-Bold.ttf',
    'BeVietnamPro-Italic.ttf',
    'BeVietnamPro-BoldItalic.ttf',
    'BeVietnamPro-SemiBold.ttf',
    'BeVietnamPro-Medium.ttf',
]
MACRON = 0x0304
MARKER = os.path.join(FONT_DIR, '.macron_patched')


def _done():
    if os.path.exists(MARKER):
        return set(json.load(open(MARKER, encoding='utf-8')))
    return set()


def patch(path):
    f = TTFont(path)
    upm = f['head'].unitsPerEm
    cmap = {}
    for t in f['cmap'].tables:
        cmap.update(t.cmap)
    if MACRON not in cmap:
        print('skip (no macron):', os.path.basename(path))
        return
    mac_name = cmap[MACRON]
    x_name = cmap.get(ord('x'))
    x_adv = f['hmtx'].metrics[x_name][0]

    glyf = f['glyf']
    g = glyf[mac_name]
    g.expand(glyf)
    coords = g.coordinates
    dx = -int(x_adv * 0.5)
    for i in range(len(coords)):
        x, y = coords[i]
        coords[i] = (x + dx, y)
    f.save(path)
    print(f'patched {os.path.basename(path)}: macron shifted {dx} units '
          f'(x advance {x_adv}, upm {upm})')


if __name__ == '__main__':
    done = _done()
    changed = False
    for name in TARGETS:
        p = os.path.join(FONT_DIR, name)
        if os.path.exists(p) and name not in done:
            patch(p)
            done.add(name)
            changed = True
    if changed:
        json.dump(sorted(done), open(MARKER, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('marker updated:', MARKER)
    else:
        print('nothing to do (already patched)')
