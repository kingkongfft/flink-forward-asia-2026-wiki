# AGENTS.md

## What This Repo Is

Conference wiki for **Flink Forward Asia 2026** (Shenzhen, June 26–27). 54 photos from the conference were OCR'd into 12 markdown docs covering Flink + AI Agent topics. A static web app serves them.

## Quick Commands

```bash
# Local dev server
python app.py
# → http://localhost:8080

# Build static site for Cloudflare Pages
python build.py
# → output in public/

# Deploy to Cloudflare Pages (production)
python build.py && npx wrangler pages deploy public --project-name flink-forward-asia-2026-wiki --branch main
```

## Architecture

- `docs/*.md` — source markdown files (edit these)
- `Weixin Image_*.jpg` — 54 conference photos in repo root
- `app.py` — Python stdlib HTTP server for local dev
- `build.py` — generates `public/` static site: copies docs with fixed image paths, copies images, generates `index.html` with embedded docs JSON
- `public/` — Cloudflare Pages deploy target (do not edit directly)

## Gotchas

- **Image paths**: Markdown uses `../Weixin Image_*.jpg` relative paths. `build.py` rewrites these to `/images/*.jpg` for the static site. If you add images, update both `docs/` references AND the gallery map in `app.py` and `build.py`.
- **Cloudflare Pages production branch**: Must deploy with `--branch main`. Without it, deployment goes to preview environment and the production URL shows "Nothing is here yet".
- **Filenames have spaces**: All JPG files have spaces in names (WeChat exports). Use quoted paths everywhere.
- **No dependencies**: `app.py` and `build.py` use only Python stdlib. No pip install needed.

## Deployment Stack

- **GitHub**: `kingkongfft/flink-forward-asia-2026-wiki` (public)
- **Cloudflare Pages**: `flink-forward-asia-2026-wiki` project, production branch = `main`
- **Production URL**: https://flink-forward-asia-2026-wiki.pages.dev
