# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, scale, spec, fig, ic

W = [("ultralight",100),("thin",200),("light",300),("regular",400),("medium",500),
     ("semibold",600),("bold",700),("heavy",800),("black",900)]
wfig = fig('<div style="display:flex;flex-direction:column;gap:9px">' + "".join(
  f'<div style="display:flex;align-items:center;gap:14px;font-weight:{fw};font-size:var(--fs-lg);'
  f'letter-spacing:var(--tr-xl);color:var(--ink)">'
  f'<span style="width:104px;font:var(--fw-r) var(--fs-xs) var(--font-num);color:var(--sub)">--{n}</span>'
  f'{ic("bell","imt-i--"+n)} 알림 Notification</div>' for n, fw in W) + '</div>',
  "그림은 한 벌이다. <code>stroke-width</code> 만 바뀐다 — 원전은 같은 것을 9벌 그려서 만든다.")

sfig = fig('<div style="display:flex;gap:var(--sp-6);align-items:center;flex-wrap:wrap">' + "".join(
  f'<span style="font-size:var(--fs-xl);color:var(--ink);display:inline-flex;align-items:center;gap:8px">'
  f'{ic("star","imt-i--scale-"+k)}<span style="font:var(--fw-r) var(--fs-xs) var(--font-num);'
  f'color:var(--sub)">--scale-{k} · {v}</span></span>' for k, v in [("s",".87"),("m","1"),("l","1.13")]) + '</div>',
  "크기를 키워도 <b>획 굵기는 그대로</b>다. 크기는 강조를 조절하는 축이지 굵기를 바꾸는 축이 아니다.")

sizes = fig('<div style="display:flex;align-items:baseline;gap:var(--sp-6);flex-wrap:wrap">' + "".join(
  f'<span style="font-size:{px}px;color:var(--ink);display:inline-flex;align-items:center;gap:6px">'
  f'{ic("search")}검색 {px}px</span>' for px in [11,13,17,26,34]) + '</div>',
  "크기를 따로 정하지 않는다. <code>1em</code> 이라 옆 글자를 그대로 따라간다.")

grid_stage = ('<svg viewBox="0 0 120 120" style="width:200px;height:200px">'
  '<defs><pattern id="p" width="5" height="5" patternUnits="userSpaceOnUse">'
  '<path d="M5 0H0V5" fill="none" stroke="var(--line-soft)" stroke-width=".5"/></pattern></defs>'
  '<rect width="120" height="120" fill="url(#p)"/>'
  '<rect x="16" y="21" width="88" height="78" fill="none" stroke="var(--brand)" '
  'stroke-width=".8" stroke-dasharray="3 2" opacity=".7"/>'
  '<g transform="translate(0,0) scale(5)" fill="none" stroke="var(--ink)" stroke-width="1.6" '
  'stroke-linecap="round" stroke-linejoin="round">'
  '<use href="#i-bell"/></g></svg>')

def emoji_row(t):
    return f'<div style="font-size:var(--fs-base);color:var(--ink);line-height:1.9">{t}</div>'

PAGE = {
 "slug": "icons", "group": "기초", "kicker": "기초",
 "title": "아이콘",
 "abstract": "334개를 좌표로 직접 그렸다. 심볼 아트워크는 쓸 수 없지만 규격은 전부 승계했고, 몇 가지는 더 싼 방법으로 만들었다.",
 "blocks": [

  ("h2", "한 세트는 다섯 가지가 같아야 한다", "consistency"),
  ("p", "크기·획·시점·디테일·여백. 하나라도 어긋나면 그 아이콘만 튄다. 이 다섯이 우리 세트의 정체성이다."),
  ("raw", anatomy(grid_stage, [
     (1, "24 × 24 격자", "모든 아이콘이 같은 캔버스 위에 있다."),
     (2, "광학 영역 17.6 × 15.6", "가로로 넓고 낮게. 정사각형으로 꽉 채우면 옆 글자보다 커 보인다."),
     (3, "획 1.6 · round cap/join", "굵기 변조 없음. 끝은 둥글게."),
     (4, "패스 2~3개", "더 필요하면 아이콘이 복잡한 것이다. 개념을 다시 본다."),
   ], "점선이 광학 영역이다. 격자를 꽉 채우지 않는 것이 핵심이다.")),

  ("h2", "굵기는 옆 글자를 따라간다", "weight"),
  ("rule", "본문 옆 아이콘이 혼자 굵으면 그것만 튄다",
   "아이콘과 글자는 한 덩어리로 읽혀야 한다. 강조하고 싶을 때만 <b>일부러</b> 어긋나게 한다."),
  ("raw", wfig),
  ("p", "우리 아이콘은 채워진 외곽선이 아니라 <b>획</b>이다. 그래서 경로 하나에 <code>stroke-width</code> 만 바꾸면 우리 세트 전부가 9단을 갖는다. 같은 규격을 더 싼 방법으로 만든 지점이다."),

  ("h2", "크기는 두 가지로 조절한다", "size"),
  ("h3", "글자를 따라가는 크기"),
  ("raw", sizes),
  ("h3", "강조를 조절하는 크기"),
  ("raw", sfig),
  ("h3", "큰 아이콘은 획을 조금 얇게 — 계산이 아니라 눈으로"),
  ("rule", "화면상 굵기를 «고정» 하면 큰 아이콘이 오히려 굵어 보인다",
   "24px 에서 1.6 인 획은 64px 에서 4.3px 이 된다. 비율은 같아도 절대 두께가 커지면 눈은 «더 굵다» 로 읽는다. "
   "그래서 커질수록 <code>--imt-w</code> 를 낮춰 화면상 굵기가 <b>완만하게</b> 자라게 한다."),
  ("raw", spec(["크기", "--imt-w", "화면상 획"], [
     ["16px", "1.73", "1.15px"], ["20px", "1.62", "1.35px"],
     ["<b>24px</b>", "<b>1.60</b>", "<b>1.60px</b> — 기준"],
     ["32px", "1.46", "1.95px"], ["40px", "1.35", "2.25px"],
     ["48px", "1.25", "2.50px"], ["64px", "1.13", "3.00px"],
   ], "<code>.imt-i--px16</code> … <code>--px64</code> 를 쓰면 크기와 보정이 함께 걸린다. "
      "작은 쪽은 반대로 살짝 굵혀 획이 사라지지 않게 한다. 기본값 1.6 은 그대로다(L-9.1). "
      "규칙은 랭귀지 L-9.11.")),

  ("h2", "흔한 동작은 흔한 모양을 쓴다", "convention"),
  ("rule", "여기서 창의성을 발휘하면 사용자가 못 알아본다",
   "잘라내기는 가위, 공유는 상자에서 나가는 화살표, 검색은 돋보기, 더보기는 말줄임표. 사람들이 이미 아는 모양을 쓰는 것이 친절이다."),
  ("raw", fig('<div style="display:grid;gap:var(--sp-3);'
     'grid-template-columns:repeat(auto-fill,minmax(120px,1fr))">' + "".join(
     f'<div style="display:flex;align-items:center;gap:8px;background:var(--card);'
     f'border-radius:var(--r-in);box-shadow:var(--edge);padding:10px 12px;'
     f'font-size:var(--fs-sm);color:var(--ink2)">{ic(n)}{t}</div>'
     for n, t in [("search","검색"),("filter","필터"),("more","더보기"),("edit","편집"),
                  ("trash","삭제"),("close","닫기"),("plus","추가"),("check","완료"),
                  ("star","중요"),("bell","알림"),("lock","잠금"),("doc","문서")]) + '</div>')),

  ("h2", "이모지를 쓰지 않는다", "no-emoji"),
  ("rule", "이모지는 기기마다 다른 그림이 나온다",
   "같은 글자가 아이폰·안드로이드·윈도우에서 서로 다르게 그려지고, 굵기도 색도 우리가 통제하지 못한다. 화면에 뜻을 지고 있는 자리라면 아이콘으로 바꾼다."),
  ("raw", cmp2([
     ("do", emoji_row(f'{ic("warning")} 손절 임박<br>{ic("bell")} 계획 조건 도달<br>{ic("lock")} 새로 사지 않는 종목'),
      "굵기·색이 옆 글자를 따라간다"),
     ("no", emoji_row('⚠️ 손절 임박<br>🔔 계획 조건 도달<br>🔒 새로 사지 않는 종목'),
      "기기마다 다른 그림 · 색 통제 불가"),
   ], "다만 <b>문장 속 화살표</b>(→ ↑ ↓)와 <b>주석 안의 기호</b>는 그대로 둔다. 그건 UI가 아니라 글이다.")),

  ("h2", "아이콘만 있는 버튼에는 이름을 단다", "a11y"),
  ("rule", "<code>aria-label</code> 없는 아이콘 버튼은 스크린리더에게 존재하지 않는다",
   "눈으로 보면 명백한 ✕ 버튼이, 소리로 들으면 '버튼' 이라고만 읽힌다. 무엇을 하는 버튼인지 알 방법이 없다."),
  ("raw", fig('<div style="display:flex;gap:var(--sp-3);align-items:center;flex-wrap:wrap">'
     '<button class="imt-btn imt-btn--icon" aria-label="닫기">' + ic("close") + '</button>'
     '<code style="font:var(--fw-r) var(--fs-sm) var(--font-num);color:var(--sub)">'
     '&lt;button aria-label="닫기"&gt;</code></div>')),

  ("h2", "전달 방식", "delivery"),
  ("raw", spec(["방법", "쓸 때", "주의"], [
     ["인라인 스프라이트",
      "아이콘 20개 이하 · 같은 페이지에서 반복",
      "가장 안전하다. 필요한 것만 뽑아 <code>&lt;body&gt;</code> 바로 뒤에 넣는다"],
     ["웹폰트",
      "많은 아이콘을 쓰는 앱",
      "<code>font/imt-icons.woff2</code> · 60KB"],
     ["단독 SVG 파일",
      "한두 개만 쓰는 정적 페이지",
      "<code>icons/glyph/*.svg</code>"],
     ["외부 <code>&lt;use&gt;</code>",
      "<b>쓰지 않는다</b>",
      "브라우저가 교차 출처 <code>&lt;use&gt;</code>를 막고, 같은 출처라도 Safari 가 제대로 못 다룬다"],
   ], "네 번째 줄이 실제로 겪은 사고다. CDN 에서 <code>&lt;use&gt;</code>로 불러오면 데스크톱에서는 보이는데 아이폰에서 아이콘이 통째로 사라진다.")),
 ],
}
