# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, spec, fig, ic

def card(inner, st=""):
    return f'<div class="imt-card" style="width:100%;max-width:270px;{st}">{inner}</div>'

head = ('<div style="display:flex;align-items:baseline;justify-content:space-between;gap:8px">'
  '<div style="font:var(--fw-sb) var(--fs-base) var(--font);letter-spacing:var(--tr-base);'
  'color:var(--ink)">보유 종목</div>'
  '<div style="font-size:var(--fs-sm);color:var(--sub)">12개</div></div>')
body = ('<div style="margin-top:var(--sp-3);display:flex;flex-direction:column;gap:7px">'
  + "".join(f'<div style="display:flex;justify-content:space-between;font-size:var(--fs-md)">'
            f'<span style="color:var(--ink2)">{n}</span>'
            f'<span style="font-family:var(--font-num);color:var({c})">{v}</span></div>'
            for n, v, c in [("삼성전자","+2.4%","--up"),("SK하이닉스","−0.8%","--down"),
                            ("현대차","+11.2%","--up")]) + '</div>')
foot = ('<div style="margin-top:var(--sp-4);padding-top:var(--sp-3);'
  'border-top:var(--hairline) solid var(--line-soft)">'
  '<button class="imt-btn imt-btn--ghost imt-btn--sm">전체 보기</button></div>')

anat = (f'<div style="position:relative">{card(head + body + foot)}'
  '<span class="g-pin g-pin--abs" style="left:-26px;top:14px">1</span>'
  '<span class="g-pin g-pin--abs" style="left:-26px;top:60px">2</span>'
  '<span class="g-pin g-pin--abs" style="left:-26px;bottom:20px">3</span></div>')

stat = ('<div class="imt-stat" style="width:100%;max-width:180px">'
  '<div class="imt-stat__k">평가손익</div>'
  '<div class="imt-stat__v" style="color:var(--up)">+3,240,800</div>'
  '<div class="imt-stat__d">+7.2% · 어제보다 +0.4%p</div></div>')

nest_bad = card(head + '<div style="margin-top:10px">' + card(body, "max-width:100%;box-shadow:var(--edge)") + '</div>')
nest_good = card(head + '<div style="margin-top:10px;background:var(--inset);border-radius:var(--r-in);'
                        'padding:var(--sp-3)">' + body + '</div>')

PAGE = {
 "slug": "cards", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "카드",
 "abstract": "관련된 것을 한 덩어리로 묶는 가장 기본적인 도구다. 무엇을 한 카드에 넣을지가 곧 정보 설계다.",
 "blocks": [

  ("h2", "생김새", "anatomy"),
  ("raw", anatomy(anat, [
     (1, "제목 줄", "무엇에 대한 카드인지. 오른쪽에 요약값(개수·기간)을 둘 수 있다."),
     (2, "본문", "카드의 이유. 여기가 비면 카드를 만들 이유가 없다."),
     (3, "동작", "있으면 아래에, 구분선으로 떼어 놓는다. 없어도 된다."),
   ], "제목은 생략할 수 있다. 무엇인지 본문만으로 명백하면 굳이 붙이지 않는다.")),
  ("raw", spec(["속성", "값"], [
     ["배경", "<code>--card</code> · 배경(<code>--bg</code>)과 대비로 떠오른다"],
     ["라운드", "<code>--r</code> 16px"],
     ["안쪽 여백", "<code>--sp-4</code> 16px · 좁은 화면 <code>--sp-3</code> 12px"],
     ["그림자", "<code>--edge</code> 1px 테두리. <code>--sh</code> 는 떠 있는 카드에만"],
     ["카드 사이 간격", "<code>--sp-2</code>~<code>--sp-3</code>"],
   ])),

  ("h2", "카드를 카드 안에 넣지 않는다", "nest"),
  ("rule", "두 겹째부터는 위계가 아니라 소음이다",
   "안쪽에 구역을 나눠야 하면 카드가 아니라 <b>배경 한 단</b>(<code>--inset</code>)이나 구분선을 쓴다. 그림자 위에 그림자를 얹으면 어느 쪽이 위인지 눈이 판단하지 못한다."),
  ("raw", cmp2([
     ("do", nest_good, "안쪽은 <code>--inset</code> 면으로"),
     ("no", nest_bad,  "카드 안에 카드"),
   ])),

  ("h2", "무엇을 한 카드에 넣는가", "grouping"),
  ("rule", "'이 카드를 지우면 같이 사라져도 되는가' 로 판단한다",
   "같이 사라져도 되면 한 덩어리다. 하나만 남아야 하면 다른 카드다."),
  ("raw", spec(["잘못된 묶음", "왜"], [
     ["'기타' 카드", "무엇이 들어 있는지 열어봐야 안다"],
     ["설정 전부를 한 카드에", "관련 없는 것이 나란히 있으면 찾는 데 시간이 든다"],
     ["카드 하나에 항목 하나", "카드일 필요가 없다 — 목록 행이면 된다"],
     ["스크롤해야 다 보이는 카드", "덩어리로 안 보인다. 나누거나 접는다"],
   ])),

  ("h2", "수치 카드", "stat"),
  ("raw", fig(stat, "값이 주인공이다. 라벨은 작게 위에, 변화는 작게 아래에. <b>값 크기는 <code>--fs-2xl</code> 이상</b>으로 잡아 한눈에 들어오게 한다.")),
  ("rule", "숫자 하나를 차트로 만들지 않는다",
   "값 하나는 큰 글자가 가장 빠르다. 옆에 작은 스파크라인을 붙이는 정도가 적당하다."),
  ("rule", "변화량에는 기준을 밝힌다",
   "'+7.2%' 만으로는 무엇 대비인지 모른다. '어제보다' · '매수가 대비' 를 함께 쓴다."),

  ("h2", "누를 수 있는 카드", "tappable"),
  ("raw", spec(["규칙", "내용"], [
     ["카드 전체가 눌리게 한다", "안의 작은 링크만 눌리면 어디를 눌러야 할지 찾아야 한다"],
     ["누름 상태를 만든다", "<code>:active</code> 에서 살짝 눌리거나 면색이 바뀐다"],
     ["카드 안에 또 다른 버튼을 넣으면", "그 버튼은 카드 이동을 막아야 한다 (<code>stopPropagation</code>)"],
     ["화살표를 오른쪽 끝에", "누를 수 있다는 신호. <code>chevron-right</code>"],
   ])),

  ("h2", "격자", "grid"),
  ("p", "카드를 여러 개 늘어놓을 때는 중단점 대신 <code>.imt-grid</code> 를 쓴다 — <code>repeat(auto-fill, minmax(240px, 1fr))</code>. 자세한 것은 <a href='layout.html#adapt'>레이아웃</a>에 있다."),
  ("rule", "한 줄 안의 카드는 높이를 맞춘다",
   "내용 길이가 달라 높이가 들쭉날쭉하면 줄로 안 읽힌다. 격자는 기본적으로 높이를 맞춰 준다."),
 ],
}
