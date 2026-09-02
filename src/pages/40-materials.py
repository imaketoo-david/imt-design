# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, scale, spec, fig, ic

RICH = ("background:radial-gradient(circle at 20% 30%,#ffd60a 0 14%,transparent 14.5%),"
        "radial-gradient(circle at 74% 66%,#ff2d55 0 18%,transparent 18.5%),"
        "linear-gradient(140deg,#1d1d1f,#0071e3 55%,#5856d6)")

def chip(bg, blur, label, extra=""):
    return (f'<div style="flex:1 1 110px;min-height:74px;border-radius:var(--r-in);'
            f'padding:var(--sp-3);display:flex;flex-direction:column;justify-content:center;'
            f'background:var({bg});backdrop-filter:var({blur});-webkit-backdrop-filter:var({blur});{extra}">'
            f'<b style="font:var(--fw-sb) var(--fs-base) var(--font);letter-spacing:var(--tr-base)">{label}</b></div>')

mats = fig('<div style="display:flex;gap:var(--sp-3);flex-wrap:wrap;padding:var(--sp-5);'
  'border-radius:var(--r);background:linear-gradient(120deg,#0071e3,#30b0c7 38%,#ff9500 70%,#ff2d55)">'
  + chip("--mat-ultrathin","--mat-blur","ultraThin")
  + chip("--mat-thin","--mat-blur","thin")
  + chip("--mat","--mat-blur","regular")
  + chip("--mat-thick","--mat-blur","thick") + '</div>',
  "두꺼울수록 대비가 좋고, 얇을수록 뒤 맥락이 남는다. <b>얇은 재질 위에 <code>--sub2</code>(비활성) 단계 글자를 올리지 않는다</b> — 대비가 모자란다.")

glass = fig(f'<div style="display:flex;gap:var(--sp-3);flex-wrap:wrap;padding:var(--sp-5);'
  f'border-radius:var(--r);{RICH}">'
  + chip("--glass","--glass-blur","regular",
         "border:1px solid var(--glass-line);box-shadow:var(--glass-sh);border-radius:var(--r-cap)")
  + chip("--glass-clear","--glass-blur","clear",
         "border:1px solid var(--glass-line);border-radius:var(--r-cap);color:#fff") + '</div>',
  "regular 은 배경 휘도를 조정해 가독성을 확보한다. clear 는 사진·영상 위에서만 쓴다.")

# 콘텐츠 층에 유리를 쓴 경우
def panel(bg, blur, label, note):
    return (f'<div style="width:100%;padding:var(--sp-4);border-radius:var(--r-in);'
            f'background:var({bg});backdrop-filter:var({blur});-webkit-backdrop-filter:var({blur});'
            f'box-shadow:var(--edge)">'
            f'<div style="font:var(--fw-sb) var(--fs-base) var(--font);color:var(--ink)">{label}</div>'
            f'<div style="font-size:var(--fs-sm);color:var(--sub);margin-top:3px">{note}</div></div>')

content_good = (f'<div style="width:100%;{RICH};padding:var(--sp-4);border-radius:var(--r-in)">'
  + panel("--card","--mat-blur","보유 종목", "12개 · 평가 4,820만원") + '</div>')
content_bad = (f'<div style="width:100%;{RICH};padding:var(--sp-4);border-radius:var(--r-in)">'
  + panel("--glass-clear","--glass-blur","보유 종목", "12개 · 평가 4,820만원") + '</div>')

dim_no = (f'<div style="width:100%;height:96px;border-radius:var(--r-in);position:relative;'
  f'background:linear-gradient(120deg,#ffe08a,#fff3c4)">'
  f'<div style="position:absolute;inset:14px;border-radius:12px;background:var(--glass-clear);'
  f'backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);'
  f'display:grid;place-items:center;color:#fff;font:var(--fw-sb) var(--fs-base) var(--font)">재생</div></div>')
dim_yes = (f'<div style="width:100%;height:96px;border-radius:var(--r-in);position:relative;'
  f'background:linear-gradient(120deg,#ffe08a,#fff3c4)">'
  f'<div style="position:absolute;inset:14px;border-radius:12px;background:var(--glass-dim);'
  f'display:grid;place-items:center;color:#fff;font:var(--fw-sb) var(--fs-base) var(--font)">재생</div></div>')

PAGE = {
 "slug": "materials", "group": "기초", "kicker": "기초",
 "title": "머티리얼",
 "abstract": "재질은 앞과 뒤를 나누는 도구다. 무엇을 얼마나 비칠지 정하는 일이지, 예쁜 흐림 효과를 얹는 일이 아니다.",
 "blocks": [

  ("h2", "재질은 두 벌이다", "two"),
  ("p", "이걸 나누지 않으면 화면이 통째로 반투명해진다. <b>표준 머티리얼</b>은 콘텐츠 층 안에서 구조를 만들고, <b>Liquid Glass</b>는 그 위에 뜨는 컨트롤·내비게이션 전용이다."),
  ("raw", spec(["", "표준 머티리얼", "Liquid Glass"], [
     ["쓰는 층", "콘텐츠", "컨트롤 · 내비게이션"],
     ["예", "카드 배경, 구역 나누기", "상단바, 탭바, 사이드바, 툴바"],
     ["토큰", "<code>--mat-ultrathin</code> ~ <code>--mat-thick</code>", "<code>--glass</code> · <code>--glass-clear</code>"],
     ["개수 제한", "없음", "화면당 하나에서 둘"],
   ])),

  ("h2", "표준 머티리얼 네 단", "standard"),
  ("raw", mats),

  ("h2", "Liquid Glass 두 종", "glass"),
  ("raw", glass),
  ("rule", "콘텐츠 층에 유리를 쓰지 않는다",
   "유리는 시선을 <b>아래 콘텐츠로</b> 보내려는 재질이다. 콘텐츠 자체에 씌우면 목적이 뒤집혀서, 읽어야 할 것이 배경과 뒤섞인다."),
  ("raw", cmp2([
     ("do", content_good, "콘텐츠는 불투명한 <code>--card</code>"),
     ("no", content_bad,  "콘텐츠에 유리 — 글자가 배경과 싸운다"),
   ])),
  ("rule", "아껴 쓴다",
   "애플 문서의 표현 그대로다. 커스텀 컨트롤마다 유리를 얹으면 화면이 통째로 흐릿해지고, 정작 강조하려던 것이 묻힌다."),

  ("h2", "clear 를 밝은 콘텐츠 위에 얹을 때", "dim"),
  ("rule", "35% 어두운 층을 먼저 깐다",
   "애플이 수치까지 명시한 몇 안 되는 항목이다. 아래가 충분히 어두우면 생략한다."),
  ("raw", cmp2([
     ("do", dim_yes, "<code>--glass-dim</code> 35% 를 깐다"),
     ("no", dim_no,  "밝은 배경 위 clear — 글자가 사라진다"),
   ])),

  ("h2", "경계는 선이 아니라 스크롤 엣지로", "edge"),
  ("p", "컨트롤 층 아래로 콘텐츠가 지나갈 때, 1px 선을 긋는 대신 콘텐츠가 흐릿하게 사라지게 한다. <code>--scroll-edge</code>. 뷰당 하나만 쓴다."),

  ("h2", "재질은 시스템 설정에 진다", "settings"),
  ("raw", spec(["설정", "일어나는 일", "우리 대응"], [
     ["<code>prefers-reduced-transparency</code>",
      "투명 효과를 줄여 달라는 요청", "머티리얼·유리가 전부 <code>--card</code> 불투명 면으로 바뀐다"],
     ["<code>prefers-contrast: more</code>",
      "대비를 높여 달라는 요청", "글자·선·상태색이 고대비 변형으로 교체된다"],
     ["<code>prefers-reduced-motion</code>",
      "움직임을 줄여 달라는 요청", "모든 전환이 0.01ms 로 눌린다"],
   ], "세 가지 모두 <code>tokens.css</code> 에 이미 들어 있다. 컴포넌트를 만들 때 따로 신경 쓸 일이 없다 — 그게 토큰에 넣어둔 이유다.")),
 ],
}
