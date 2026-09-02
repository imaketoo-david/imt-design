# -*- coding: utf-8 -*-
"""가이드 문서 생성 — src/pages/*.py 를 읽어 guide/*.html 을 만든다.

한 페이지가 한 파일이다. HIG 처럼 '주제 하나 = 문서 하나' 구조라야
찾아 읽을 수 있고, 고칠 때 그 파일만 열면 된다.
"""
import os, sys, importlib.util, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "src", "pages")
OUT  = os.path.join(ROOT, "guide")
sys.path.insert(0, os.path.join(ROOT, "src"))
os.makedirs(OUT, exist_ok=True)

VER = os.environ.get("IMT_V", "dev")

def load_pages():
    pages = []
    for f in sorted(os.listdir(SRC)):
        if not f.endswith(".py") or f.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f[:-3], os.path.join(SRC, f))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        pages.append(m.PAGE)
    return pages


def render_blocks(blocks):
    out = []
    for b in blocks:
        k = b[0]
        if   k == "h2":   out.append(f'<h2 class="g-h2" id="{b[2] if len(b)>2 else ""}">{b[1]}</h2>')
        elif k == "h3":   out.append(f'<h3 class="g-h3">{b[1]}</h3>')
        elif k == "p":    out.append(f'<p class="g-p">{b[1]}</p>')
        elif k == "rule": out.append(f'<div class="g-rule"><b>{b[1]}</b><span>{b[2]}</span></div>')
        elif k == "raw":  out.append(b[1])
        else: raise ValueError(f"모르는 블록: {k}")
    return "\n".join(out)


def toc(page):
    items = [(b[1], b[2]) for b in page["blocks"] if b[0] == "h2" and len(b) > 2 and b[2]]
    if not items: return ""
    return ('<nav class="g-toc"><b>이 문서</b>'
            + "".join(f'<a href="#{i}">{t}</a>' for t, i in items) + "</nav>")


def sidebar(pages, cur):
    groups = {}
    for p in pages:
        groups.setdefault(p["group"], []).append(p)
    out = []
    for g, ps in groups.items():
        out.append(f"<b>{g}</b>")
        for p in ps:
            a = ' class="on"' if p["slug"] == cur else ""
            out.append(f'<a href="{p["slug"]}.html"{a}>{p["title"]}</a>')
    return "".join(out)


SHELL = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — IMT Design Guide</title>
<link rel="icon" href="../favicon.svg?v={v}" type="image/svg+xml">
<link rel="icon" href="../favicon-32.png?v={v}" sizes="32x32">
<link rel="apple-touch-icon" href="../apple-touch-icon.png?v={v}">
<meta name="theme-color" content="#1d1d1f">
<link rel="stylesheet" href="../tokens.css?v={v}">
<link rel="stylesheet" href="../components.css?v={v}">
<link rel="stylesheet" href="../patterns.css?v={v}">
<link rel="stylesheet" href="../site.css?v={v}">
<link rel="stylesheet" href="../guide.css?v={v}">
<style>
  .g-toc{{display:flex;flex-wrap:wrap;gap:var(--sp-2);align-items:center;
    padding:var(--sp-4);background:var(--inset);border-radius:var(--r);
    margin:0 0 var(--sp-8);font-size:var(--fs-md)}}
  .g-toc b{{color:var(--sub2);font:var(--fw-sb) var(--fs-tag) var(--font);
    text-transform:uppercase;letter-spacing:.06em;margin-right:var(--sp-2)}}
  .g-toc a{{color:var(--brand);text-decoration:none}}
  .g-toc a:hover{{text-decoration:underline}}
  .g-next{{display:flex;gap:var(--sp-3);margin-top:var(--sp-16);
    padding-top:var(--sp-6);border-top:var(--hairline) solid var(--line)}}
  .g-next a{{flex:1;padding:var(--sp-4);background:var(--card);border-radius:var(--r);
    box-shadow:var(--edge);text-decoration:none}}
  .g-next span{{display:block;font-size:var(--fs-tag);color:var(--sub2);
    text-transform:uppercase;letter-spacing:.06em;margin-bottom:3px}}
  .g-next b{{color:var(--ink);font-weight:var(--fw-sb);font-size:var(--fs-base)}}
  @media(max-width:900px){{.gs{{grid-template-columns:1fr}}.gs__nav{{display:none}}}}
</style></head><body>
<nav class="gnav">
  <a class="gnav__b" href="../index.html"><svg class="imt-i" aria-hidden="true"><use href="#i-layers"/></svg>IMT Design</a>
  <div class="gnav__i">
    <a href="../index.html">개요</a>
    <a href="index.html" class="on">가이드</a>
    <a href="../language.html">랭귀지</a>
    <a href="../index-full.html">토큰</a>
    <a href="/icons/catalog.html">아이콘</a>
    <a href="../resources.html">리소스</a>
  </div>
  <span class="gnav__sp"></span>
  <a class="gnav__x" href="https://github.com/imaketoo-david/imt-design">GitHub</a>
  <button class="gnav__t" id="theme">다크</button>
</nav>
{sprite}
<div class="wrap">
  <header class="phead">
    <p class="phead__k">{kicker}</p>
    <h1>{title}</h1>
    <p>{abstract}</p>
  </header>
  <div class="cols">
    <aside class="side">{side}</aside>
    <main>
      {toc}
      {body}
      {next}
    </main>
  </div>
</div>
<script>
const T=document.getElementById("theme");
const ap=d=>{{document.documentElement.setAttribute("data-theme",d?"dark":"light");T.textContent=d?"라이트":"다크";}};
let d=matchMedia("(prefers-color-scheme: dark)").matches;
try{{const s=localStorage.getItem("imt-theme"); if(s) d=s==="dark";}}catch(e){{}}
ap(d);
T.onclick=()=>{{d=!d;ap(d);try{{localStorage.setItem("imt-theme",d?"dark":"light")}}catch(e){{}}}};
</script>
</body></html>"""


def main():
    pages = load_pages()
    sprite_path = os.path.join(ROOT, "guide", "_sprite.svg")
    sprite = open(sprite_path, encoding="utf-8").read() if os.path.exists(sprite_path) else ""
    for i, p in enumerate(pages):
        nxt = ""
        prev_p = pages[i-1] if i else None
        next_p = pages[i+1] if i+1 < len(pages) else None
        cells = []
        if prev_p: cells.append(f'<a href="{prev_p["slug"]}.html"><span>이전</span><b>{prev_p["title"]}</b></a>')
        if next_p: cells.append(f'<a href="{next_p["slug"]}.html"><span>다음</span><b>{next_p["title"]}</b></a>')
        if cells: nxt = f'<div class="g-next">{"".join(cells)}</div>'
        body = render_blocks(p["blocks"])
        if "@@TOC@@" in body:
            groups = {}
            for q in pages:
                if q["slug"] == "index":
                    continue
                groups.setdefault(q["group"], []).append(q)
            cards = []
            for g, qs in groups.items():
                items = "".join(
                    f'<a href="{q["slug"]}.html" style="display:block;padding:9px 0;'
                    f'border-bottom:var(--hairline) solid var(--line-soft);text-decoration:none">'
                    f'<b style="color:var(--ink);font-weight:var(--fw-m);font-size:var(--fs-base)">'
                    f'{q["title"]}</b>'
                    f'<span style="display:block;color:var(--sub);font-size:var(--fs-sm);'
                    f'margin-top:2px;line-height:1.5">{q["abstract"]}</span></a>' for q in qs)
                cards.append(
                    f'<div class="imt-card" style="margin-bottom:var(--sp-4)">'
                    f'<h3 style="margin:0 0 var(--sp-2);font:var(--fw-sb) var(--fs-base) var(--font);'
                    f'color:var(--sub2);text-transform:uppercase;letter-spacing:.06em">{g}</h3>'
                    f'{items}</div>')
            body = body.replace("@@TOC@@", "".join(cards))
        html = SHELL.format(
            title=p["title"], kicker=p["kicker"], abstract=p["abstract"],
            body=body, toc=toc(p),
            side=sidebar(pages, p["slug"]), next=nxt, sprite=sprite, v=VER)
        open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8").write(html)
    print(f"가이드 {len(pages)}쪽 생성:", ", ".join(p["slug"] for p in pages))


if __name__ == "__main__":
    main()
