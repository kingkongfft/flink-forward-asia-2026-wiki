import os, json, shutil, re, sys

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Flink Forward Asia 2026 Wiki</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0f1117;--surface:#1a1d27;--border:#2a2d3a;
  --text:#e4e4e7;--text2:#a1a1aa;--accent:#7c3aed;
  --accent2:#a78bfa;--green:#22c55e;--blue:#3b82f6;
}
body{font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);display:flex;height:100vh;overflow:hidden}
#sidebar{width:280px;min-width:280px;background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}
#sidebar-header{padding:20px;border-bottom:1px solid var(--border)}
#sidebar-header h1{font-size:16px;font-weight:700;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
#sidebar-header p{font-size:12px;color:var(--text2);margin-top:4px}
#sidebar-header .tag{display:inline-block;font-size:10px;padding:2px 8px;border-radius:10px;background:rgba(124,58,237,0.15);color:var(--accent2);margin-top:8px}
#nav{flex:1;overflow-y:auto;padding:8px}
#nav::-webkit-scrollbar{width:4px}
#nav::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
.nav-item{display:block;padding:10px 12px;border-radius:8px;text-decoration:none;color:var(--text2);font-size:13px;transition:all .15s;cursor:pointer;margin-bottom:2px}
.nav-item:hover{background:rgba(124,58,237,0.08);color:var(--text)}
.nav-item.active{background:rgba(124,58,237,0.15);color:var(--accent2);font-weight:600}
#main{flex:1;display:flex;flex-direction:column;overflow:hidden}
#topbar{height:52px;border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 24px;gap:12px;flex-shrink:0}
#topbar h2{font-size:14px;font-weight:600;color:var(--text)}
#topbar .breadcrumb{font-size:12px;color:var(--text2)}
#content-wrap{flex:1;overflow-y:auto;padding:32px 48px}
#content-wrap::-webkit-scrollbar{width:6px}
#content-wrap::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
#content{max-width:860px;margin:0 auto}
.md-body h1{font-size:28px;font-weight:800;margin:0 0 16px;background:linear-gradient(135deg,var(--text),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1.3}
.md-body h2{font-size:22px;font-weight:700;margin:32px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--border);color:var(--text)}
.md-body h3{font-size:17px;font-weight:600;margin:24px 0 8px;color:var(--accent2)}
.md-body h4{font-size:14px;font-weight:600;margin:16px 0 6px;color:var(--text2)}
.md-body p{margin:8px 0;line-height:1.7;color:var(--text)}
.md-body ul,.md-body ol{margin:8px 0;padding-left:24px;line-height:1.7}
.md-body li{margin:4px 0;color:var(--text)}
.md-body a{color:var(--accent2);text-decoration:none}
.md-body a:hover{text-decoration:underline}
.md-body strong{color:#fff;font-weight:600}
.md-body code{background:rgba(124,58,237,0.12);padding:2px 6px;border-radius:4px;font-size:13px;color:var(--accent2);font-family:ui-monospace,monospace}
.md-body pre{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:16px;overflow-x:auto;margin:12px 0}
.md-body pre code{background:none;padding:0;color:var(--text)}
.md-body blockquote{border-left:3px solid var(--accent);padding:8px 16px;margin:12px 0;background:rgba(124,58,237,0.05);border-radius:0 8px 8px 0;color:var(--text2);font-style:italic}
.md-body table{width:100%;border-collapse:collapse;margin:12px 0;font-size:13px}
.md-body th{background:var(--surface);padding:10px 12px;text-align:left;font-weight:600;border:1px solid var(--border);color:var(--accent2)}
.md-body td{padding:8px 12px;border:1px solid var(--border)}
.md-body tr:nth-child(even){background:rgba(255,255,255,0.02)}
.md-body hr{border:none;border-top:1px solid var(--border);margin:24px 0}
.md-body img{max-width:100%;border-radius:8px;margin:12px 0;border:1px solid var(--border);cursor:pointer;transition:transform .2s}
.md-body img:hover{transform:scale(1.01)}
.md-body em{color:var(--text2)}
#gallery-section{margin-top:48px;padding-top:32px;border-top:1px solid var(--border)}
#gallery-section h2{font-size:22px;font-weight:700;margin-bottom:16px}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.gallery-item{border-radius:8px;overflow:hidden;border:1px solid var(--border);background:var(--surface);cursor:pointer;transition:all .2s}
.gallery-item:hover{border-color:var(--accent);transform:translateY(-2px)}
.gallery-item img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block}
.gallery-item .caption{padding:8px 12px;font-size:11px;color:var(--text2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#lightbox{display:none;position:fixed;inset:0;z-index:1000;background:rgba(0,0,0,0.92);align-items:center;justify-content:center;cursor:pointer}
#lightbox.show{display:flex}
#lightbox img{max-width:90vw;max-height:90vh;border-radius:8px;box-shadow:0 8px 32px rgba(0,0,0,0.5)}
#lightbox-close{position:absolute;top:16px;right:20px;font-size:28px;color:#fff;cursor:pointer;width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:rgba(255,255,255,0.1)}
#lightbox-close:hover{background:rgba(255,255,255,0.2)}
#loading{text-align:center;padding:60px 0;color:var(--text2)}
#loading .spinner{width:32px;height:32px;border:3px solid var(--border);border-top-color:var(--accent);border-radius:50%;animation:spin .6s linear infinite;margin:0 auto 12px}
@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:768px){
  #sidebar{display:none}
  #content-wrap{padding:16px}
}
</style>
</head>
<body>
<div id="sidebar">
  <div id="sidebar-header">
    <h1>Flink Forward Asia 2026</h1>
    <p>Shenzhen \u00b7 June 26\u201327</p>
    <span class="tag">Real-Time Data \u00b7 AI Future</span>
  </div>
  <div id="nav"></div>
</div>
<div id="main">
  <div id="topbar">
    <span class="breadcrumb" id="breadcrumb"></span>
  </div>
  <div id="content-wrap">
    <div id="content">
      <div id="loading"><div class="spinner"></div>Loading...</div>
    </div>
  </div>
</div>
<div id="lightbox" onclick="closeLightbox()">
  <div id="lightbox-close">&times;</div>
  <img id="lightbox-img" src="" onclick="event.stopPropagation()">
</div>

<script>
const docs = __DOCS_JSON__;
let currentFile = null;

function init() {
  renderNav();
  const hash = location.hash.slice(1);
  if (hash && docs.find(d => d.file === hash)) {
    loadDoc(hash);
  } else if (docs.length > 0) {
    loadDoc(docs[0].file);
  }
}

function renderNav() {
  const nav = document.getElementById("nav");
  nav.innerHTML = docs.map(d =>
    `<div class="nav-item${d.file === currentFile ? " active" : ""}" onclick="loadDoc('${d.file}')" title="${d.title}">${d.title}</div>`
  ).join("");
}

async function loadDoc(file) {
  currentFile = file;
  location.hash = file;
  renderNav();
  const doc = docs.find(d => d.file === file);
  document.getElementById("breadcrumb").textContent = doc ? doc.title : file;
  const content = document.getElementById("content");
  content.innerHTML = '<div id="loading"><div class="spinner"></div>Loading...</div>';
  try {
    const res = await fetch("/docs/" + file);
    const md = await res.text();
    const html = marked.parse(md);
    content.innerHTML = `<div class="md-body">${html}</div>`;
    addGallery(file);
    content.querySelectorAll("img").forEach(img => {
      img.addEventListener("click", (e) => { e.stopPropagation(); openLightbox(img.src); });
    });
  } catch(e) {
    content.innerHTML = '<p style="color:var(--text2)">Failed to load document.</p>';
  }
}

function addGallery(file) {
  const galleries = {
    "00-conference-overview.md": [["Weixin Image_20260627190222_5_25.jpg","Venue Signage"],["Weixin Image_20260627190228_12_25.jpg","Floor Map"],["Weixin Image_20260627190246_32_25.jpg","Main Stage"],["Weixin Image_20260627190240_25_25.jpg","Theme Banner"],["Weixin Image_20260627190308_43_25.jpg","Opening Scene"]],
    "03-flink-agents-streaming-agent-os.md": [["Weixin Image_20260627190233_17_25.jpg","Apache Flink Agents: Streaming Agent OS"],["Weixin Image_20260627190236_21_25.jpg","Agent\u65f6\u4ee3\uff1a\u8bad\u7ec3\u5bf9\u8c61\u4ece\u6a21\u578b\u8d70\u5411\u7cfb\u7edf"],["Weixin Image_20260627190242_27_25.jpg","\u4e3a\u4ec0\u4e48Flink\u662f\u5b9e\u65f6\u6570\u636e\u5e95\u5ea7"],["Weixin Image_20260627190239_24_25.jpg","Flink\u5b9e\u65f6\u8fd0\u7ef4Agent"],["Weixin Image_20260627190245_30_25.jpg","\u4ec0\u4e48\u662fAgentic"]],
    "04-fluss-gateway-agent-data-layer.md": [["Weixin Image_20260627190240_25_25.jpg","Fluss Gateway Title"],["Weixin Image_20260627190241_26_25.jpg","OpenClaw Agent Risk Control Architecture"]],
    "05-milvus-flink-agents.md": [["Weixin Image_20260627190243_28_25.jpg","Milvus + Flink-Agents"],["Weixin Image_20260627190304_41_25.jpg","\u957f\u65f6\u8fd0\u884cAgent\u7684\u4e24\u5821\u5899"],["Weixin Image_20260627190306_42_25.jpg","\u8bb0\u5fc6\u662f\u5206\u5c42\u7684"],["Weixin Image_20260627190308_43_25.jpg","\u957f\u671f\u8bb0\u5fc6\u9700\u8981\u670d\u52a1\u8fb9\u754c"],["Weixin Image_20260627190311_44_25.jpg","AMS\u662f\u4ec0\u4e48"]],
    "08-nvidia-flink-multimodal.md": [["Weixin Image_20260627190234_18_25.jpg","NVIDIA Booth"],["Weixin Image_20260627190238_23_25.jpg","Flink Multimodal Pipeline"],["Weixin Image_20260627190300_39_25.jpg","Flink Agentic Operators"],["Weixin Image_20260627190245_30_25.jpg","AI Compute Terminal"]],
    "09-alibaba-cloud-agentic-cloud.md": [["Weixin Image_20260627190232_16_25.jpg","Agentic Cloud Architecture"],["Weixin Image_20260627190246_32_25.jpg","Alibaba Cloud Exhibition"]],
    "07-flink-llm-post-training.md": [["Weixin Image_20260627190235_20_25.jpg","LLM Post-Training"]],
    "10-flink-autopilot-agent.md": [["Weixin Image_20260627190315_46_25.jpg","Flink AutoPilot"],["Weixin Image_20260627190239_24_25.jpg","Flink\u5b9e\u65f6\u8fd0\u7ef4Agent"]],
    "11-tencent-flink-ai-engine.md": [["Weixin Image_20260627190356_52_25.jpg","Tencent Flink 2.x AI Engine"],["Weixin Image_20260627190358_53_25.jpg","AI\u65f6\u4ee3\u7684\u6570\u636e\u8bc9\u6c42\u4e0eFlink\u7834\u5c40\u4e4b\u9053"],["Weixin Image_20260627190402_55_25.jpg","SQL\u5c42AI\u80fd\u529b"],["Weixin Image_20260627190404_56_25.jpg","Flink AI Ops"]],
  };
  const images = galleries[file];
  if (!images) return;
  const section = document.createElement("div");
  section.id = "gallery-section";
  section.innerHTML = `<h2>Photo Gallery (${images.length})</h2><div class="gallery">${images.map(([img,c])=>`<div class="gallery-item" onclick="openLightbox('/images/${img}')"><img src="/images/${img}" alt="${c}" loading="lazy"><div class="caption">${c}</div></div>`).join("")}</div>`;
  document.getElementById("content").appendChild(section);
}

function openLightbox(src) {
  document.getElementById("lightbox-img").src = src;
  document.getElementById("lightbox").classList.add("show");
  document.body.style.overflow = "hidden";
}
function closeLightbox() {
  document.getElementById("lightbox").classList.remove("show");
  document.body.style.overflow = "";
}
document.addEventListener("keydown", e => { if (e.key === "Escape") closeLightbox(); });
init();
</script>
</body>
</html>'''

base = os.path.dirname(os.path.abspath(__file__))
public = os.path.join(base, 'public')

os.makedirs(os.path.join(public, 'docs'), exist_ok=True)
os.makedirs(os.path.join(public, 'images'), exist_ok=True)

# Copy and fix markdown files
docs_dir = os.path.join(base, 'docs')
for f in os.listdir(docs_dir):
    if f.endswith('.md'):
        with open(os.path.join(docs_dir, f), 'r', encoding='utf-8') as fh:
            content = fh.read()
        content = re.sub(r'\.\.\/((?:Weixin)[^)\s]+\.(?:jpg|jpeg|png))', r'/images/\1', content)
        with open(os.path.join(public, 'docs', f), 'w', encoding='utf-8') as fh:
            fh.write(content)

# Copy images
for f in os.listdir(base):
    if f.startswith('Weixin') and f.endswith('.jpg'):
        shutil.copy2(os.path.join(base, f), os.path.join(public, 'images', f))

# Build docs list
files = sorted(f for f in os.listdir(os.path.join(public, 'docs')) if f.endswith('.md'))
docs = []
for f in files:
    with open(os.path.join(public, 'docs', f), 'r', encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if line.startswith('# '):
                docs.append({'file': f, 'title': line[2:]})
                break
        else:
            docs.append({'file': f, 'title': f.replace('.md', '')})

# Generate index.html
html = INDEX_HTML.replace('__DOCS_JSON__', json.dumps(docs, ensure_ascii=False))
with open(os.path.join(public, 'index.html'), 'w', encoding='utf-8') as fh:
    fh.write(html)

print(f'Built {len(files)} docs, {len(os.listdir(os.path.join(public, "images")))} images')
print(f'Output: {public}')
