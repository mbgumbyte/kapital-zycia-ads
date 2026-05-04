#!/usr/bin/env python3
"""Extract Atria ad thumbnails — crop the grid area from rendered PDF pages."""

from PIL import Image
from pathlib import Path

HERE = Path(__file__).parent

# At 300dpi (2479x3508), the ad grid sits roughly:
# x: 940..2280 (skip left sidebar + brand header column)
# page 1 y: 470..3370 (skip top brand header, footer)
# page 2 y: 70..2870 (continues from top)
GRID_X = (940, 2280)

CROPS = [
    ("page-1-grid.png", "atria-page-1.png", GRID_X, (470, 3370)),
    ("page-2-grid.png", "atria-page-2.png", GRID_X, (70, 2870)),
]

for out, src, (x0, x1), (y0, y1) in CROPS:
    img = Image.open(HERE / src)
    img.crop((x0, y0, x1, y1)).save(HERE / out, optimize=True)
    print(f"saved {out} {x1-x0}x{y1-y0}")

# Also create a 5-column slice for each page (each col shows a vertical thumbnail strip)
COL_WIDTH = (GRID_X[1] - GRID_X[0]) // 5

for page_idx, (src, y0, y1) in enumerate([
    ("atria-page-1.png", 470, 3370),
    ("atria-page-2.png", 70, 2870),
], start=1):
    img = Image.open(HERE / src)
    for col in range(5):
        x0 = GRID_X[0] + col * COL_WIDTH
        x1 = x0 + COL_WIDTH
        out = f"page-{page_idx}-col-{col+1}.png"
        img.crop((x0, y0, x1, y1)).save(HERE / out, optimize=True)
    print(f"saved 5 columns for page {page_idx}")
