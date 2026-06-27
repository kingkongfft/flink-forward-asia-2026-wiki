# Deployment Guide — Flink Forward Asia 2026 Wiki

## Live URLs

| Service | URL |
|---------|-----|
| **Cloudflare Pages (Production)** | https://flink-forward-asia-2026-wiki.pages.dev |
| **GitHub Repository** | https://github.com/kingkongfft/flink-forward-asia-2026-wiki |
| **Local Development** | http://localhost:8080 |

---

## Project Structure

```
flink-ai-agent-wiki/
├── app.py                    # Local Python dev server
├── build.py                  # Static site builder for Cloudflare Pages
├── docs/                     # Source markdown files
│   ├── 00-conference-overview.md
│   ├── 01-keynote-agenda.md
│   ├── 02-track-agendas.md
│   ├── 03-flink-agents-streaming-agent-os.md
│   ├── 04-fluss-gateway-agent-data-layer.md
│   ├── 05-milvus-flink-agents.md
│   ├── 06-llamafactory-training-platform.md
│   ├── 07-flink-llm-post-training.md
│   ├── 08-nvidia-flink-multimodal.md
│   ├── 09-alibaba-cloud-agentic-cloud.md
│   ├── 10-flink-autopilot-agent.md
│   ├── 11-tencent-flink-ai-engine.md
│   └── README.md
├── public/                   # Static build output (Cloudflare Pages)
│   ├── index.html
│   ├── docs/
│   └── images/
├── Weixin Image_*.jpg        # 54 conference photos (source)
├── DEPLOY.md                 # This file
└── .gitignore
```

---

## Local Development

```bash
python app.py
# Open http://localhost:8080
```

---

## Build for Cloudflare Pages

```bash
python build.py
# Output: public/ directory
```

The build script:
1. Copies markdown files to `public/docs/` with fixed image paths
2. Copies all JPG images to `public/images/`
3. Generates `public/index.html` with embedded docs list

---

## Deploy to Cloudflare Pages

```bash
# First time: create project
npx wrangler pages project create flink-forward-asia-2026-wiki --production-branch main

# Deploy to production
python build.py
npx wrangler pages deploy public --project-name flink-forward-asia-2026-wiki --branch main
```

### Deployment Notes
- The production branch must be `main` (not `master`)
- Deploy with `--branch main` to publish to production
- Without `--branch`, deployment goes to preview environment
- Preview URL format: `https://<hash>.flink-forward-asia-2026-wiki.pages.dev`
- Production URL: `https://flink-forward-asia-2026-wiki.pages.dev`

---

## GitHub Push

```bash
git add -A
git commit -m "your message"
git push origin master
```

---

## Tech Stack

- **Markdown rendering**: marked.js (CDN)
- **Local server**: Python http.server (stdlib)
- **Static build**: Python build.py
- **Hosting**: Cloudflare Pages
- **Source control**: GitHub (kingkongfft/flink-forward-asia-2026-wiki)
