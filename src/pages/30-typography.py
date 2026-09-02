# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, scale, spec, fig, ic

S = lambda t, sz, w="--fw-r", tr="--tr-base", lh="1.3": (
    f'<div style="font:var({w}) var({sz})/{lh} var(--font);letter-spacing:var({tr});color:var(--ink)">{t}</div>')

steps = [("--fs-3xl","--tr-3xl"),("--fs-title1","--tr-2xl"),("--fs-2xl","--tr-2xl"),
         ("--fs-title2","--tr-2xl"),("--fs-xl","--tr-xl"),("--fs-lg","--tr-xl"),
         ("--fs-callout","--tr-base"),("--fs-base","--tr-base"),("--fs-md","--tr-base"),
         ("--fs-sm","--tr-sm"),("--fs-xs","--tr-sm"),("--fs-tag","--tr-sm")]
scale_fig = fig('<div style="display:flex;flex-direction:column;gap:var(--sp-3)">' + "".join(
    f'<div style="display:flex;align-items:baseline;gap:var(--sp-4);'
    f'border-bottom:var(--hairline) solid var(--line-soft);padding-bottom:var(--sp-2)">'
    f'<code style="flex:none;width:104px;font:var(--fw-r) var(--fs-xs) var(--font-num);color:var(--sub)">{f}</code>'
    f'{S("애플 스타일 Apple 2026", f, "--fw-sb", t)}</div>' for f, t in steps) + '</div>',
    "이 열두 단계 안에서만 고른다.")

# 자간
tr_good = ('<div style="font:var(--fw-sb) 34px/1.2 var(--font);letter-spacing:-.024em;color:var(--ink)">'
           '오늘의 수익률</div>')
tr_bad  = ('<div style="font:var(--fw-sb) 34px/1.2 var(--font);letter-spacing:0;color:var(--ink)">'
           '오늘의 수익률</div>')

# 굵기
w_fig = fig('<div style="display:flex;flex-direction:column;gap:10px">' + "".join(
   f'<div style="display:flex;align-items:baseline;gap:16px">'
   f'<code style="width:74px;font:var(--fw-r) var(--fs-xs) var(--font-num);color:var(--sub)">{c}</code>'
   f'<span style="font:{w} var(--fs-xl)/1.3 var(--font);letter-spacing:var(--tr-xl);color:var(--ink)">'
   f'수익률 Portfolio 24.8%</span></div>'
   for c, w in [("--fw-r · 400","400"),("--fw-m · 500","500"),("--fw-sb · 600","600")]) + '</div>',
   "셋뿐이다. Thin·Light 는 토큰에 아예 없다 — 작은 글자에서 읽히지 않는다.")

# 행간
lh_ko = ('<p style="margin:0;font:var(--fw-r) var(--fs-md)/1.55 var(--font);letter-spacing:var(--tr-base);'
  'color:var(--ink2);max-width:30ch">받침이 있는 글자가 이어지면 줄과 줄이 서로 밀착해 보인다. '
  '한글 본문은 행간을 넓혀야 읽힌다.</p>')
lh_apple = ('<p style="margin:0;font:var(--fw-r) var(--fs-md)/1.29 var(--font);letter-spacing:var(--tr-base);'
  'color:var(--ink2);max-width:30ch">받침이 있는 글자가 이어지면 줄과 줄이 서로 밀착해 보인다. '
  '한글 본문은 행간을 넓혀야 읽힌다.</p>')

# 잘림
trunc_bad = ('<div style="width:100%;max-width:220px;background:var(--card);border-radius:var(--r-in);'
  'box-shadow:var(--edge);padding:12px"><div style="font-size:var(--fs-md);color:var(--ink);'
  'white-space:nowrap;overflow:hidden;text-overflow:ellipsis">삼성전자 우선주 배당락일 안내</div></div>')
trunc_good = ('<div style="width:100%;max-width:220px;background:var(--card);border-radius:var(--r-in);'
  'box-shadow:var(--edge);padding:12px"><div style="font-size:var(--fs-md);color:var(--ink);'
  'line-height:1.45">삼성전자 우선주<br>배당락일 안내</div></div>')

PAGE = {
 "slug": "typography", "group": "기초", "kicker": "기초",
 "title": "타이포그래피",
 "abstract": "글자는 화면의 대부분을 차지한다. 크기·굵기·자간·행간 네 가지만 정해두면 나머지는 저절로 정해진다.",
 "blocks": [

  ("h2", "정해진 단계만 쓴다", "scale"),
  ("rule", "11.5px 를 한 번 허용하면 위계가 사라진다",
   "눈은 0.5px 차이를 '더 중요함' 으로 읽지 못한다. 얻는 것 없이 단계만 늘어나고, 그다음부터는 무엇이 무엇보다 큰지 아무도 모른다."),
  ("raw", scale_fig),
  ("p", "각 단계는 애플 텍스트 스타일에 대응한다. 우리가 임의로 만든 숫자가 아니다."),
  ("raw", spec(["토큰", "px", "애플 스타일 (iOS Large)", "쓰는 곳"], [
     ["<code>--fs-3xl</code>", "34", "Large Title", "히어로"],
     ["<code>--fs-title1</code>", "28", "Title 1", "페이지 제목"],
     ["<code>--fs-2xl</code>", "26", "macOS Large Title", "요약 숫자"],
     ["<code>--fs-title2</code>", "22", "Title 2", "큰 섹션"],
     ["<code>--fs-xl</code>", "20", "Title 3", "섹션 제목"],
     ["<code>--fs-lg</code>", "17", "Body · Headline", "강조 값"],
     ["<code>--fs-callout</code>", "16", "Callout", "버튼"],
     ["<code>--fs-base</code>", "15", "Subhead", "값"],
     ["<code>--fs-md</code>", "13", "Footnote · macOS Body", "본문"],
     ["<code>--fs-sm</code>", "12", "Caption 1", "라벨"],
     ["<code>--fs-xs</code>", "11", "Caption 2 (iOS 최소)", "보조 설명"],
     ["<code>--fs-tag</code>", "10", "macOS 최소", "배지"],
   ], "모바일에서 뜻이 있는 글자에는 11px 이상을 쓴다. 10px 는 배지처럼 부수적인 표식에만 쓴다.")),

  ("h2", "큰 글자일수록 자간을 좁힌다", "tracking"),
  ("rule", "이 하나가 '애플처럼 보이는가' 를 가장 크게 좌우한다",
   "시스템 폰트는 크기마다 자간을 스스로 조정한다. 웹에서는 그 일이 자동으로 일어나지 않으므로 우리가 대신해야 한다. 34px 제목에 <code>-0.024em</code>, 13px 본문에 <code>-0.008em</code>."),
  ("raw", cmp2([
     ("do", tr_good, "<code>letter-spacing: -.024em</code>"),
     ("no", tr_bad,  "기본값 — 글자 사이가 벌어져 흩어진다"),
   ], "작은 차이 같지만, 제목이 있는 모든 화면에서 매번 나타난다.")),

  ("h2", "굵기는 셋", "weight"),
  ("raw", w_fig),
  ("rule", "굵기로 강조할 자리는 한 화면에 몇 곳뿐이다",
   "전부 굵게 하면 아무것도 굵지 않다. 강조가 필요하면 굵기보다 <b>색의 진하기</b>나 <b>공간</b>을 먼저 쓴다."),

  ("h2", "한글 본문은 행간을 넓힌다", "leading"),
  ("p", "애플 실측은 본문 17/22 = 1.29다. 그 값은 라틴 문자 기준이다. 한글은 받침 때문에 글자 하나의 세로 밀도가 높아 같은 비율이면 줄이 서로 붙어 보인다."),
  ("raw", cmp2([
     ("do", lh_ko,    "<code>--lh-base</code> 1.55 — 한글 본문"),
     ("no", lh_apple, "1.29 — 라틴 기준 그대로"),
   ], "본문만 넓힌다. 제목과 수치는 애플 비율(<code>--lh-title</code> 1.21, <code>--lh-head</code> 1.29)을 그대로 쓴다 — 큰 글자는 원래 행간이 좁아야 덩어리로 읽힌다.")),

  ("h2", "잘라내기보다 접는다", "truncate"),
  ("rule", "말줄임은 마지막 수단이다",
   "잘린 글자는 정보가 아니라 '더 있다' 는 신호일 뿐이다. 줄 수를 늘리거나, 세로로 쌓거나, 열을 줄인다."),
  ("raw", cmp2([
     ("do", trunc_good, "두 줄로 접는다"),
     ("no", trunc_bad,  "한 줄에 욱여넣고 자른다"),
   ])),

  ("h2", "서체", "font"),
  ("raw", spec(["토큰", "값", "이유"], [
     ["<code>--font</code>",
      "<code>-apple-system</code> → Pretendard → Apple SD Gothic Neo",
      "맥·아이폰에서는 시스템 서체가 그대로 나온다. SF Pro 를 웹폰트로 배포하는 것은 라이선스 범위 밖이다."],
     ["<code>--font-num</code>",
      "<code>ui-monospace</code> → SF Mono → Menlo",
      "표에서 자릿수가 흔들리면 위아래 비교가 안 된다. 숫자·코드·토큰명에만 쓴다."],
   ])),
  ("rule", "읽으라고 쓴 글자는 선택할 수 있어야 한다",
   "값·종목코드·오류 메시지는 복사해서 검색하게 된다. <code>user-select:none</code> 은 버튼·탭 같은 컨트롤에만 건다."),
 ],
}
