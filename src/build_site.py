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

CATS = [("layers",     "가이드",  "guide/index.html"),
        ("doc",        "랭귀지",  "language.html"),
        ("brush",      "토큰",    "index-full.html"),
        ("sparkle",    "아이콘",  "/icons/catalog.html"),
        ("download",   "리소스",  "resources.html")]

LNAV = [("개요", "index.html", True), ("가이드", "guide/index.html", False),
        ("랭귀지", "language.html", False), ("토큰", "index-full.html", False),
        ("아이콘", "/icons/catalog.html", False),
        ("리소스", "resources.html", False)]

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
  <a href="/icons/catalog.html">아이콘 334</a>
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
    return ('<div style="display:flex;gap:8px">' + "".join(
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
    return ('<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;color:var(--ink2)">'
      + "".join(ic(n, "imt-i--scale-l") for n in
        ["bell","star","search","doc","lock","camera","trend-up","check-circle"])
      + '</div>')

def art_grid():
    return ('<div style="display:flex;gap:8px;align-items:flex-end">' + "".join(
      f'<div style="width:16px;height:{h}px;border-radius:4px;background:var(--c1);opacity:{o}"></div>'
      for h, o in [(28,.35),(44,.5),(36,.65),(58,.8),(70,1),(52,.8)]) + '</div>')

def art_btn():
    return ('<div style="display:flex;flex-direction:column;gap:8px;align-items:center">'
      '<button class="imt-btn imt-btn--primary">기본 동작</button>'
      '<button class="imt-btn imt-btn--soft">보조</button>'
      '<span class="imt-badge" style="color:var(--ok);background:var(--green-soft)">정상</span></div>')

ART = {"기초": art_layers, "패턴": art_grid, "컴포넌트": art_btn}

def art_space():
    return ('<div style="display:flex;flex-direction:column;gap:8px;align-items:flex-start">'
      + "".join(f'<div style="height:10px;width:{w}px;border-radius:3px;'
                f'background:var(--c1);opacity:{o}"></div>'
                for w, o in [(20,.30),(32,.45),(52,.6),(84,.78),(132,1)])
      + '<div style="margin-top:8px;font:var(--fw-r) var(--fs-xs) var(--font-num);'
        'color:var(--flat)">4 · 8 · 12 · 20 · 32</div></div>')

def art_lang():
    return ('<div style="width:150px;display:flex;flex-direction:column;gap:8px">'
      + "".join(f'<div style="height:7px;width:{w}%;border-radius:4px;background:var(--fill2)"></div>'
                for w in (100, 92, 74))
      + '<div style="margin-top:8px;height:7px;width:46%;border-radius:4px;background:var(--c1)"></div>'
      '</div>')

ART = {"기초": art_layers, "패턴": art_grid, "컴포넌트": art_btn}


# ── 리소스 카드 ──────────────────────────────────────────────────
def rcard(grad, glyph, title, meta, desc, dl, dl_label, more, more_label):
    return f"""<article class="rcard">
  <div class="rcard__art"><div class="rcard__sq" style="background:{grad}">{ic(glyph)}</div></div>
  <h3>{title}</h3>
  <p class="rcard__m">{meta}</p>
  <p>{desc}</p>
  <div class="rcard__foot">
    <a href="{dl}" download>{ic("download")}{dl_label}</a>
    <a href="{more}">{ic("doc")}{more_label}</a>
  </div>
</article>"""

def kb(n): return f"{n // 1024}KB" if n >= 1024 else f"{n}B"

def res_cards():
    import json
    f = os.path.join(ROOT, "dl", "_sizes.json")
    z = json.load(open(f)) if os.path.exists(f) else {}
    g1 = "linear-gradient(140deg,#0a84ff,#5e5ce6)"
    g2 = "linear-gradient(140deg,#30d158,#0a84ff)"
    g3 = "linear-gradient(140deg,#5e5ce6,#bf5af2)"
    g4 = "linear-gradient(140deg,#ff9f0a,#ff375f)"
    return "".join([
      rcard(g1, "brush", "IMT 디자인 리소스",
            f"ZIP · {kb(z.get('tokens',0))}",
            "토큰·컴포넌트·짜임새 스타일시트와 최소 화면 하나. 값을 직접 쓰지 않고 "
            "의미 이름만 부르는 방식이 그대로 들어 있다.",
            "dl/imt-tokens.zip", "다운로드", "guide/color.html", "더 알아보기"),
      rcard(g2, "sparkle", "아이콘 세트",
            f"ZIP · {kb(z.get('icons',0))} · SVG {z.get('n_svg',334)}개",
            "낱개 SVG와 스프라이트, 웹폰트까지. 굵기 9단·크기 3단이 CSS 변수 두 개로 "
            "움직인다 — 그림을 아홉 벌 그려두지 않았다.",
            "dl/imt-icons.zip", "다운로드", "/icons/catalog.html", "카탈로그 보기"),
      rcard(g3, "rounded-square", "앱 아이콘 템플릿",
            f"SVG · {kb(z.get('appicon',0))} · 1024pt",
            "1024 캔버스에 배경·중간·전경 세 겹, 안전 원 지름 512. 레이어를 위아래 "
            "155씩 어긋나게 두어 깊이를 확인한다. 참고선은 내보내기 전에 지운다.",
            "dl/imt-appicon-template.svg", "다운로드", "guide/icons.html", "아이콘 지침"),
      rcard(g4, "box", "UI 키트",
            f"ZIP · {kb(z.get('uikit',0))}",
            "버튼·카드·입력·배지가 실제로 도는 HTML 한 벌. 화면을 새로 짤 때 "
            "여기서 잘라다 쓰면 값이 어긋날 일이 없다.",
            "dl/imt-ui-kit.zip", "다운로드", "index-full.html", "컴포넌트 보기"),
    ])


# ── 표지 ─────────────────────────────────────────────────────────
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

    tiles = "".join(
        f'<a class="tile" href="guide/{ps[0]["slug"]}.html">'
        f'<div class="tile__art">{ART.get(g, art_layers)()}</div>'
        f'<div class="tile__t">{g} · {len(ps)}쪽</div>'
        f'<div class="tile__d">{" · ".join(q["title"] for q in ps)}</div></a>'
        for g, ps in groups.items())

    body = f"""
<header class="hero">
  <h1>애플 스타일을,<br>값으로 고정한다</h1>
  <p>말로 전하던 기준을 토큰·규칙·도해로 바꿨다. 이 사이트의 모든 색과 크기는
     <code>tokens.css</code> 를 실제로 읽어 그린 것이라, 문서와 코드가 어긋날 수 없다.</p>
</header>

<nav class="cats">{cats}</nav>

<section class="band band--tint" id="guide">
  <div class="wrap">
    <h2>가이드</h2>
    <p class="lead">주제 하나가 문서 하나다. 굵은 한 줄이 지침이고 그 아래가 이유이며,
       모든 지침에 도해가 붙는다 — 잘된 예와 잘못된 예를 나란히 놓는 방식이다.</p>
    <div class="tiles">{tiles}</div>
    <p class="lead" style="margin:var(--sp-6) 0 0">
      <a class="more" href="guide/index.html">가이드 {len(pages)-1}쪽 전체 보기 →</a></p>
  </div>
</section>

<section class="band" id="language">
  <div class="wrap">
    <h2>랭귀지</h2>
    <p class="lead">가이드가 <b>무엇을 하라</b>면, 랭귀지는 <b>왜 그렇게 정했나</b>이다.
       19개 절 121개 규칙이 한 문서에 있고, 애플에서 그대로 받은 것과 우리가 정한 것을
       구분해 적어둔다.</p>
    <div class="links">
      <a href="language.html"><b>디자인 랭귀지 전문</b>
        <span>19절 121규칙 — 결정과 근거를 한 곳에</span></a>
      <a href="language.html#legal"><b>무엇을 배우고 무엇을 받지 않는가</b>
        <span>HIG 문서는 읽고, 애플 에셋은 받지 않는다</span></a>
      <a href="language.html#diverge"><b>겉보기에 달라 보이는 것들</b>
        <span>승계 · 미규정 · 구현 제약 — 이견은 0건</span></a>
    </div>
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
      <a class="tile" href="guide/layout.html"><div class="tile__art">{art_space()}</div>
        <div class="tile__t">간격과 라운드</div><div class="tile__d">4의 배수 · 손끝 44pt · 포인터 28pt</div></a>
    </div>
    <p class="lead" style="margin:var(--sp-6) 0 0">
      <a class="more" href="index-full.html">토큰 값 전체와 컴포넌트 보기 →</a></p>
  </div>
</section>

<section class="band" id="icons">
  <div class="wrap">
    <h2>아이콘</h2>
    <p class="lead">334개를 좌표로 직접 그렸다. 굵기 9단·크기 3단이 CSS 변수 두 개로 움직인다 —
       애플이 아홉 벌을 그려 넣는 자리를, 우리는 한 벌로 해결한다.</p>
    <div class="tiles">
      <a class="tile" href="/icons/catalog.html"><div class="tile__art">{art_icons()}</div>
        <div class="tile__t">아이콘 카탈로그</div><div class="tile__d">334개 · 이름으로 검색 · 클릭하면 코드 복사</div></a>
      <a class="tile" href="guide/icons.html"><div class="tile__art">{art_lang()}</div>
        <div class="tile__t">아이콘 지침</div><div class="tile__d">굵기를 옆 글자에 맞춘다 · 뜻이 겹치면 하나만 쓴다</div></a>
    </div>
  </div>
</section>

<section class="band band--tint" id="resources">
  <div class="wrap">
    <h2>리소스</h2>
    <p class="lead">쓰던 그대로 내려받는다. 문서에 그려둔 값과 내려받은 파일의 값이 같다 —
       빌드할 때 같은 파일을 담기 때문이다.</p>
    <div class="res">{res_cards()}</div>
    <p class="lead" style="margin:var(--sp-8) 0 0">
      <a class="more" href="resources.html">리소스 전체 보기 →</a></p>
  </div>
</section>

<footer class="foot"><div class="wrap">
  IMT Design System · 가이드 {len(pages)-1}쪽 · 아이콘 334 ·
  <a href="https://github.com/imaketoo-david/imt-design">GitHub</a> ·
  <a href="/icons/catalog.html">design.imaketoo.com/icons</a>
</div></footer>
"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
        shell("IMT Design System", body, sprite, "개요"))

    # ── 리소스 페이지 ────────────────────────────────────────────
    rbody = f"""
<div class="wrap">
  <header class="phead">
    <p class="phead__k">리소스</p>
    <h1>다운로드</h1>
    <p>토큰·아이콘·템플릿을 파일로 받는다. 이 사이트가 실제로 쓰는 파일과 같은 것이라,
       문서에 적힌 값과 내려받은 값이 어긋나지 않는다.</p>
  </header>
  <div class="res">{res_cards()}</div>

  <section style="margin-top:var(--sp-16)">
    <h2 class="band-h" style="margin:0 0 var(--sp-4);font:var(--fw-sb) var(--fs-title2)/1.25 var(--font);
        letter-spacing:var(--tr-xl);color:var(--ink)">애플 에셋은 담지 않는다</h2>
    <p style="margin:0;max-width:64ch;font-size:var(--fs-base);line-height:var(--lh-base);color:var(--sub)">
      SF Symbols 아트워크·San Francisco 서체·Sketch/Figma 템플릿은 여기 없다.
      규격만 읽고 우리 좌표로 다시 그렸다. 앱 아이콘 템플릿의 1024 캔버스·3레이어·
      지름 512 안전 원은 애플이 공개한 <b>수치</b>이고, 그 안에 그려 넣은 것은 우리 것이다.
      <a class="more" href="language.html#legal">기준 보기 →</a>
    </p>
  </section>
</div>

<footer class="foot" style="margin-top:var(--sp-16)"><div class="wrap">
  IMT Design System ·
  <a href="index.html">개요</a> ·
  <a href="https://github.com/imaketoo-david/imt-design">GitHub</a>
</div></footer>
"""
    open(os.path.join(ROOT, "resources.html"), "w", encoding="utf-8").write(
        shell("리소스 — IMT Design System", rbody, sprite, "리소스"))

    print(f"▸ 표지·리소스 생성 · 가이드 {len(pages)-1}쪽 · 영역 {len(CATS)}")


if __name__ == "__main__":
    build()
