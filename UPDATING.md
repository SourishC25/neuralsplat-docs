# Publishing a new edition

The manual is built in the main product repository and copied here. This
repository only shows it: the README for anyone who opens the repo on GitHub,
and `index.html` for the GitHub Pages site.

1. Replace `NeuralSplat-User-Manual.pdf` with the new edition. Keep the file name,
   so links that people already have keep working.
2. Render the pages:

   ```bash
   pip install pymupdf pillow
   python tools/render_pages.py
   ```

3. If the sections, their page numbers or the page count changed, update:
   - the `PAGES` and `SECTIONS` lists near the end of `index.html`
   - the contents table and the page list in `README.md`
   - the edition date in `index.html` and `README.md`
4. Commit and push to `main`. GitHub Pages republishes the site within a minute
   or two.

## What is where

| Path | What it is |
| --- | --- |
| `NeuralSplat-User-Manual.pdf` | The manual itself, the file people download |
| `pages/` | One image per page, shown by the README and the site |
| `index.html` | The GitHub Pages site: a page-by-page reader with contents and download |
| `assets/` | Logo, favicon, the cover and the link preview card |
| `tools/render_pages.py` | Turns the PDF into the page images |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are |
