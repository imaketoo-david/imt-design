# -*- coding: utf-8 -*-
"""사이트 표지(index.html) 생성 — 애플 개발자 사이트의 2단 내비 구조를 승계한다.

가이드 쪽수·제목·요약은 src/pages/*.py 에서 읽어온다.
문서를 추가하면 표지가 저절로 따라온다 — 손으로 목록을 고칠 일이 없다.
"""
import os, sys, importlib.util, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
VER = os.environ.get("IMT_V", "dev")

def load_pages():
    d = os.path.join(ROOT, "src", "pages"); out = []
    for f in sorted(os.listdir(d)):
        if not f.endswith(".py") or f.startswith("_"): continue
        sp = importlib.util.spec_from_file_location(f[:-3], os.path.join(d, f))
        m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        out.append(m.PAGE)
    return out

def ic(n, cls=""):
    c = f" {cls}" if cls else ""
    return f'<svg class="imt-i{c}" aria-hidden="true"><use href="#i-{n}"/></svg>'

CATS = [("layers", "기초", "guide/layout.html"),
        ("chart-line", "패턴", "guide/data.html"),
        ("box", "컴포넌트", "guide/buttons.html"),
        ("sparkle", "아이콘", "https://icons.imaketoo.com"),
        ("doc", "랭귀지", "language.html"),
        ("brush", "토큰", "#tokens")]

LNAV = [("개요", "index.html", True), ("가이드", "guide/index.html", False),
        ("랭귀지", "language.html", False), ("토큰", "#tokens", False),
        ("아이콘", "https://icons.imaketoo.com", False)]

def shell(title, body, sprite, lnav_on="개요", extra_css=""):
    nav = "".join(f'<a href="{h}"{" class=on" if t == lnav_on else ""}>{t}</a>' for t, h, _ in LNAV)
    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="tokens.css?v={VER}">
<link rel="stylesheet" href="components.css?v={VER}">
<link rel="stylesheet" href="patterns.css?v={VER}">
<link rel="stylesheet" href="site.css?v={VER}">
<link rel="stylesheet" href="guide.css?v={VER}">
{extra_css}</head><body>
<nav class="gnav">
  <a class="gnav__b" href="index.html">{ic("layers")}IMT Design</a>
  <span class="gnav__sp"></span>
  <a href="https://icons.imaketoo.com">아이콘 334</a>
  <a href="https://github.com/imaketoo-david/imt-design">GitHub</a>
  <button class="gnav__t" id="theme">다크</button>
</nav>
<nav class="lnav">
  <a class="lnav__t" href="index.html">디자인 시스템</a>
  <div class="lnav__i">{nav}</div>
</nav>
{sprite}
{body}
<script>
const T=document.getElementById("theme");
const ap=d=>{{document.documentElement.setAttribute("data-theme",d?"dark":"light");T.textContent=d?"라이트":"다크";}};
let d=matchMedia("(prefers-color-scheme: dark)").matches;
try{{const s=localStorage.getItem("imt-theme"); if(s) d=s==="dark";}}catch(e){{}}
ap(d);
T.onclick=()=>{{d=!d;ap(d);try{{localStorage.setItem("imt-theme",d?"dark":"light")}}catch(e){{}}}};
</script>
</body></html>"""


# ── 표지 본문 ────────────────────────────────────────────────────
def art_color():
    return ('<div style="display:flex;gap:6px">' + "".join(
        f'<div style="width:26px;height:64px;border-radius:7px;background:var(--c{i})"></div>'
        for i in range(1, 7)) + '</div>')

def art_type():
    return ('<div style="text-align:center;line-height:1">'
      '<div style="font:var(--fw-sb) 44px var(--font);letter-spacing:var(--tr-3xl);color:var(--ink)">Aa</div>'
      '<div style="margin-top:8px;font:var(--fw-r) var(--fs-sm) var(--font-num);color:var(--sub)">'
      '34 · 28 · 22 · 17 · 13</div></div>')

def art_layers():
    return ('<div style="position:relative;width:136px;height:88px">'
      '<div style="position:absolute;inset:18px 0 0;border-radius:12px;'
      'background:linear-gradient(140deg,var(--c1),var(--c6));opacity:.9"></div>'
      '<div style="position:absolute;left:12px;right:12px;top:8px;height:26px;border-radius:9px;'
      'background:rgba(255,255,255,.62);backdrop-filter:blur(10px);'
      '-webkit-backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.7)"></div>'
      '<div style="position:absolute;left:30px;right:30px;bottom:8px;height:24px;border-radius:9px;'
      'background:var(--card);box-shadow:var(--sh-lift)"></div></div>')

def art_icons():
    return ('<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;color:var(--ink2)">'
      + "".join(ic(n, "imt-i--scale-l") for n in
        ["bell","star","search","doc","lock","camera","trend-up","check-circle"])
      + '</div>')

def art_grid():
    return ('<div style="display:flex;gap:8px;align-items:flex-end">' + "".join(
      f'<div style="width:16px;height:{h}px;border-radius:4px;background:var(--c1);opacity:{o}"></div>'
      for h, o in [(28,.35),(44,.5),(36,.65),(58,.8),(70,1),(52,.8)]) + '</div>')

def art_btn():
    return ('<div style="display:flex;flex-direction:column;gap:9px;align-items:center">'
      '<button class="imt-btn imt-btn--primary">기본 동작</button>'
      '<button class="imt-btn imt-btn--soft">보조</button>'
      '<span class="imt-badge" style="color:var(--ok);background:var(--green-soft)">정상</span></div>')

ART = {"기초": art_layers, "패턴": art_grid, "컴포넌트": art_btn}

def build():
    pages = load_pages()
    sp = os.path.join(ROOT, "guide", "_sprite.svg")
    sprite = open(sp, encoding="utf-8").read() if os.path.exists(sp) else ""

    cats = "".join(
        f'<a href="{h}"><span class="cats__i">{ic(n)}</span><span>{t}</span></a>'
        for n, t, h in CATS)

    groups = {}
    for p in pages:
        if p["slug"] == "index": continue
        groups.setdefault(p["group"], []).append(p)

    tiles = []
    for g, ps in groups.items():
        art = ART.get(g, art_layers)()
        tiles.append(
            f'<a class="tile" href="guide/{ps[0]["slug"]}.html">'
            f'<div class="tile__art">{art}</div>'
            f'<div class="tile__t">{g} · {len(ps)}쪽</div>'
            f'<div class="tile__d">{" · ".join(q["title"] for q in ps)}</div></a>')

    def plain(t, n=64):
        """요약에서 태그를 걷어내고 자른다. 태그 한가운데를 자르면 마크업이 샌다."""
        t = re.sub(r"<[^>]+>", "", t).strip()
        return t if len(t) <= n else t[:n].rstrip() + "…"

    doclinks = "".join(
        f'<a href="guide/{q["slug"]}.html"><b>{q["title"]}</b>'
        f'<span>{plain(q["abstract"])}</span></a>' for g in groups for q in groups[g])

    body = f"""
<header class="hero">
  <h1>애플 스타일을,<br>값으로 고정한다</h1>
  <p>말로 전하던 기준을 토큰·규칙·도해로 바꿨다. 이 사이트의 모든 색과 크기는
     <code>tokens.css</code> 를 실제로 읽어 그린 것이라, 문서와 코드가 어긋날 수 없다.</p>
</header>

<nav class="cats">{cats}</nav>

<section class="band band--tint">
  <div class="wrap">
    <h2>가이드</h2>
    <p class="lead">주제 하나가 문서 하나다. 굵은 한 줄이 지침이고 그 아래가 이유이며,
       모든 지침에 도해가 붙는다 — 잘된 예와 잘못된 예를 나란히 놓는 방식이다.</p>
    <div class="tiles">{"".join(tiles)}</div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2>전체 문서</h2>
    <div class="links">{doclinks}</div>
  </div>
</section>

<section class="band band--tint" id="tokens">
  <div class="wrap">
    <h2>토큰</h2>
    <p class="lead">값은 이 한 파일 안에만 있다. 코드에서는 <code>--sub</code>·<code>--warn</code>
       같은 <b>의미 이름</b>만 부른다. 값이 바뀌어도 코드는 바뀌지 않는다.</p>
    <div class="tiles">
      <a class="tile" href="guide/color.html"><div class="tile__art">{art_color()}</div>
        <div class="tile__t">색</div><div class="tile__d">면 3단 · 글자 4단 · 상태 4색 · 차트 8슬롯</div></a>
      <a class="tile" href="guide/typography.html"><div class="tile__art">{art_type()}</div>
        <div class="tile__t">타이포그래피</div><div class="tile__d">12단계 · 애플 텍스트 스타일 대응</div></a>
      <a class="tile" href="https://icons.imaketoo.com"><div class="tile__art">{art_icons()}</div>
        <div class="tile__t">아이콘 334</div><div class="tile__d">굵기 9단 · 크기 3단 · 좌표로 직접 그린 세트</div></a>
    </div>
    <p class="lead" style="margin-top:var(--sp-6)">
      <a href="index-full.html" style="color:var(--brand);text-decoration:none">
        토큰 값 전체와 컴포넌트 보기 →</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap wrap--narrow">
    <h2>애플과의 관계</h2>
    <p class="lead"><b>디자인 가이드는 100% 승계한다.</b> 버튼·글자·위치·색·라운드에 대해
      애플이 정해둔 것을 다시 고민하지 않는다. 쓸 수 없는 것은 가이드가 아니라
      <b>산출물</b>(심볼 아트워크·폰트 파일·템플릿)이고, 그건 규격만 읽고 우리 방식으로 다시 만든다.</p>
    <div class="links">
      <a href="language.html#legal"><b>무엇을 배우고 무엇을 받지 않는가</b>
        <span>HIG 문서는 읽고, 애플 에셋은 받지 않는다</span></a>
      <a href="language.html#diverge"><b>겉보기에 달라 보이는 것들</b>
        <span>승계 · 미규정 · 구현 제약 — 이견은 0건</span></a>
    </div>
  </div>
</section>

<footer class="foot"><div class="wrap">
  IMT Design System · 가이드 {len(pages)-1}쪽 · 아이콘 334 ·
  <a href="https://github.com/imaketoo-david/imt-design">GitHub</a> ·
  <a href="https://icons.imaketoo.com">icons.imaketoo.com</a>
</div></footer>
"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
        shell("IMT Design System", body, sprite, "개요"))
    print(f"▸ 표지 생성 · 가이드 {len(pages)-1}쪽 · 카테고리 {len(CATS)}")


if __name__ == "__main__":
    build()
