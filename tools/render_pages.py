"""Turn the manual PDF into the images the README and the site show.

Run it after replacing NeuralSplat-User-Manual.pdf:

    python tools/render_pages.py

Needs: pip install pymupdf pillow
Writes pages/page-NN.webp (one per page) and assets/cover.png.
"""
from pathlib import Path

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "NeuralSplat-User-Manual.pdf"
PAGES = ROOT / "pages"
ASSETS = ROOT / "assets"


def main() -> None:
    PAGES.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)
    for old in PAGES.glob("page-*.webp"):
        old.unlink()

    doc = pymupdf.open(PDF)
    for i, page in enumerate(doc, 1):
        # 144 dpi: an A4 page comes out ~1190 px wide, sharp on high-density screens.
        pix = page.get_pixmap(dpi=144)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img.save(PAGES / f"page-{i:02d}.webp", "WEBP", quality=86, method=6)
        if i == 1:
            img.save(ASSETS / "cover.png", optimize=True)

    print(f"{doc.page_count} pages rendered.")
    print("If the page count or the contents changed, update the SECTIONS list in index.html")
    print("and the contents table in README.md.")


if __name__ == "__main__":
    main()
