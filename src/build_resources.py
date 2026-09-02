# -*- coding: utf-8 -*-
"""리소스(다운로드) 페이지와 실제 내려받을 산출물을 만든다.

애플 다운로드 페이지의 '구성'만 승계한다 — 카드 격자, 아트 정사각, 제목,
설명, 구분선 아래 다운로드/더 알아보기 두 줄. 애플 파일은 하나도 쓰지 않는다.
앱 아이콘 템플릿은 애플이 공개한 규격(1024 캔버스 · 3레이어 · 지름 512 원 ·
y오프셋 ±155)만 읽고 우리 좌표로 다시 그린다.
"""
import os, zipfile, shutil, json

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS = os.path.join(os.path.dirname(ROOT), "imt-icons")
DL    = os.path.join(ROOT, "dl")

# ── 앱 아이콘 템플릿 (우리가 그린다) ─────────────────────────────
APPICON = """<?xml version="1.0" encoding="UTF-8"?>
<!-- IMT 앱 아이콘 템플릿 · 1024 캔버스 · 3레이어 · 안전 원 지름 512
     레이어 y중심 357 / 512 / 667 — 위아래 155px 시차로 깊이를 만든다.
     각 레이어의 <g>를 열어 그 안에만 그린다. 원 밖으로 나가면 잘린다. -->
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <clipPath id="safe"><circle cx="512" cy="512" r="256"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0a84ff"/><stop offset="1" stop-color="#5e5ce6"/>
    </linearGradient>
  </defs>

  <!-- 배경 레이어 — 캔버스를 꽉 채운다 -->
  <g id="layer-back">
    <rect width="1024" height="1024" rx="230" fill="url(#bg)"/>
  </g>

  <!-- 중간 레이어 — 안전 원 안 -->
  <g id="layer-mid" clip-path="url(#safe)">
    <circle cx="512" cy="512" r="256" fill="#fff" opacity=".14"/>
  </g>

  <!-- 전경 레이어 — 안전 원 안, 여기에 기호를 그린다 -->
  <g id="layer-fore" clip-path="url(#safe)" fill="none" stroke="#fff"
     stroke-width="34" stroke-linecap="round" stroke-linejoin="round">
    <path d="M400 560 L480 640 L624 424"/>
  </g>

  <!-- 참고선 — 내보내기 전에 이 그룹을 지운다 -->
  <g id="guides" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2">
    <circle cx="512" cy="512" r="256"/>
    <circle cx="512" cy="357" r="256" stroke-dasharray="8 8"/>
    <circle cx="512" cy="667" r="256" stroke-dasharray="8 8"/>
    <line x1="512" y1="0" x2="512" y2="1024"/><line x1="0" y1="512" x2="1024" y2="512"/>
  </g>
</svg>
"""

STARTER = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>IMT 스타터</title>
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components.css">
<link rel="stylesheet" href="patterns.css">
</head><body>
<!-- 값은 하나도 직접 쓰지 않는다. 토큰 이름만 부른다. -->
<div class="imt-page">
  <h1 class="imt-h1">제목</h1>
  <p class="imt-sub">부제목 한 줄.</p>

  <div class="imt-card" style="margin-top:var(--sp-6)">
    <div class="imt-card__h">카드</div>
    <div class="imt-card__b">
      <p>본문. 색은 <code>--ink</code>, 여백은 <code>--sp-*</code>.</p>
      <div style="display:flex;gap:var(--gap-ctl);margin-top:var(--sp-5)">
        <button class="imt-btn imt-btn--primary">기본 동작</button>
        <button class="imt-btn">취소</button>
      </div>
    </div>
  </div>
</div>
</body></html>
"""

README = """IMT Design — 토큰 꾸러미
=========================

파일
  tokens.css      값의 단일 출처. 색·크기·간격·라운드·그림자·모션.
  components.css  버튼·카드·배지·입력·아이콘 등 기본 부품.
  patterns.css    표·대시보드 같은 짜임새.
  guide.css       문서용 도해 스타일. 앱에는 필요 없다.
  starter.html    위 셋만으로 만든 최소 화면.

쓰는 법
  <link rel="stylesheet" href="tokens.css">
  <link rel="stylesheet" href="components.css">

규칙
  1. 값을 직접 쓰지 않는다. #6e6e74 가 아니라 var(--sub) 이라고 쓴다.
  2. 사이트가 덮어써도 되는 토큰은 --brand / --brand-hover / --brand-soft 셋뿐이다.
  3. 다크 모드는 :root[data-theme=dark] 에서 저절로 바뀐다. 따로 쓸 것이 없다.

문서  https://design.imaketoo.com
아이콘 https://icons.imaketoo.com
"""


def zip_add(z, src, arc):
    if os.path.exists(src): z.write(src, arc)


def build_downloads():
    os.makedirs(DL, exist_ok=True)
    out = {}

    # ① 토큰 꾸러미
    p = os.path.join(DL, "imt-tokens.zip")
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        for f in ("tokens.css", "components.css", "patterns.css", "guide.css"):
            zip_add(z, os.path.join(ROOT, f), f"imt-tokens/{f}")
        z.writestr("imt-tokens/starter.html", STARTER)
        z.writestr("imt-tokens/README.txt", README)
    out["tokens"] = os.path.getsize(p)

    # ② 아이콘 꾸러미
    p = os.path.join(DL, "imt-icons.zip")
    n_svg = 0
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        d = os.path.join(ICONS, "icons")
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".svg"):
                    z.write(os.path.join(d, f), f"imt-icons/svg/{f}"); n_svg += 1
        zip_add(z, os.path.join(ICONS, "sprite.svg"),     "imt-icons/sprite.svg")
        zip_add(z, os.path.join(ICONS, "imt-icons.css"),  "imt-icons/imt-icons.css")
        zip_add(z, os.path.join(ICONS, "icons.json"),     "imt-icons/icons.json")
        fd = os.path.join(ICONS, "font")
        if os.path.isdir(fd):
            for f in sorted(os.listdir(fd)):
                z.write(os.path.join(fd, f), f"imt-icons/font/{f}")
    out["icons"] = os.path.getsize(p); out["n_svg"] = n_svg

    # ③ 앱 아이콘 템플릿
    p = os.path.join(DL, "imt-appicon-template.svg")
    open(p, "w", encoding="utf-8").write(APPICON)
    out["appicon"] = os.path.getsize(p)

    # ④ 화면 템플릿 — 스타터 + 토큰 3종을 한 폴더로
    p = os.path.join(DL, "imt-ui-kit.zip")
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        for f in ("tokens.css", "components.css", "patterns.css"):
            zip_add(z, os.path.join(ROOT, f), f"imt-ui-kit/{f}")
        z.writestr("imt-ui-kit/starter.html", STARTER)
        zip_add(z, os.path.join(ROOT, "index-full.html"), "imt-ui-kit/component-gallery.html")
    out["uikit"] = os.path.getsize(p)

    json.dump(out, open(os.path.join(DL, "_sizes.json"), "w"))
    return out


if __name__ == "__main__":
    o = build_downloads()
    print("▸ 다운로드 산출물 " + " · ".join(
        f"{k} {v//1024}KB" for k, v in o.items() if k != "n_svg"))
