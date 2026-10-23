#!/usr/bin/env python3
"""Render selected PDF pages to PNG for visual inspection."""
import sys

import pymupdf

pdf = sys.argv[1]
outdir = sys.argv[2] if len(sys.argv) > 2 else '/tmp/preview'
pages = sys.argv[3] if len(sys.argv) > 3 else 'all'
dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 110

import os
os.makedirs(outdir, exist_ok=True)
d = pymupdf.open(pdf)
print('pages:', d.page_count)
if pages == 'all':
    idx = range(d.page_count)
else:
    idx = [int(x) - 1 for x in pages.split(',')]
for i in idx:
    if i < 0 or i >= d.page_count:
        continue
    d[i].get_pixmap(dpi=dpi).save(os.path.join(outdir, 'p%02d.png' % (i + 1)))
print('saved to', outdir)
