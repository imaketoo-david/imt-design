# -*- coding: utf-8 -*-
from figures import cmp2, spec, fig, ic

seg = lambda items, on=0: ('<div class="imt-seg" style="width:100%;max-width:270px">'
  + "".join(f'<button{" class=on" if i==on else ""}>{t}</button>' for i, t in enumerate(items)) + '</div>')
chips = lambda items, on=(0,): ('<div style="display:flex;gap:8px;flex-wrap:wrap">'
  + "".join(f'<button class="imt-chip{" on" if i in on else ""}">{t}</button>'
            for i, t in enumerate(items)) + '</div>')
badge = lambda t, fg, bg, icn=None: (
  f'<span class="imt-badge" style="color:var({fg});background:var({bg});display:inline-flex;'
  f'align-items:center;gap:4px">{ic(icn) if icn else ""}{t}</span>')

PAGE = {
 "slug": "selection", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "세그먼트 · 칩 · 배지",
 "abstract": "셋 다 작고 둥글어서 헷갈리기 쉽지만 하는 일이 다르다. 화면을 바꾸는 것, 조건을 좁히는 것, 상태를 알리는 것.",
 "blocks": [

  ("h2", "셋의 차이", "diff"),
  ("raw", spec(["", "세그먼트", "칩", "배지"], [
     ["하는 일", "<b>화면 내용을 바꾼다</b>", "<b>조건을 좁힌다</b>", "<b>상태를 알린다</b>"],
     ["누를 수 있나", "예 — 하나만 선택", "예 — 여러 개 선택 가능", "<b>아니오</b>"],
     ["예", "일 / 주 / 월", "보유 · 관심 · 급등", "정상 · 확인 · 문제"],
     ["모양", "한 덩어리 안에 붙어 있다", "낱개로 떨어져 있다", "낱개 · 더 작다"],
   ], "배지를 누를 수 있게 만들면 칩이 된다. 누를 수 없는 것을 누를 수 있어 보이게 만들지 않는다.")),

  ("h2", "세그먼트", "segment"),
  ("raw", fig(seg(["일","주","월","연"]), "선택된 것 하나가 항상 있다. '아무것도 선택 안 됨' 상태를 만들지 않는다.")),
  ("raw", spec(["규칙", "이유"], [
     ["다섯 개까지", "그 이상은 글자가 잘리거나 누르기 어려워진다 — 드롭다운으로"],
     ["텍스트든 아이콘이든 하나로 통일", "섞으면 어느 쪽이 기준인지 알 수 없다"],
     ["칸 너비를 같게", "글자 길이가 달라도 균등 분할한다"],
     ["안쪽 라운드는 <code>--r-in</code>", "바깥 라운드 − 패딩 = 안쪽 라운드. 동심원을 맞춘다"],
     ["누르면 즉시 바뀐다", "적용 버튼을 따로 두지 않는다"],
   ])),
  ("rule", "이름은 명사로",
   "세그먼트는 <b>무엇을 보는지</b>를 고르는 것이지 동작이 아니다. '보기' 가 아니라 '차트'."),

  ("h2", "칩", "chip"),
  ("raw", fig(chips(["전체","보유","관심","급등","배당"], on=(1,3)),
     "여러 개를 켤 수 있다. 켜진 것과 꺼진 것이 <b>면색</b>으로 확실히 갈려야 한다.")),
  ("raw", spec(["규칙", "이유"], [
     ["라운드는 캡슐(<code>--r-cap</code>)", "여기가 캡슐을 쓰는 자리다 — 버튼과 구분된다"],
     ["'전체' 를 맨 앞에", "초기화 수단이 항상 보인다"],
     ["개수가 많으면 가로 스크롤", "줄바꿈으로 화면 절반을 먹지 않게"],
     ["몇 개가 켜졌는지 알린다", "'3개 조건' — 스크롤 밖의 칩을 잊지 않게"],
     ["결과가 0이면 어느 조건 때문인지 말한다", "하나씩 꺼 보게 하지 않는다"],
   ])),

  ("h2", "배지", "badge"),
  ("raw", fig('<div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center">'
     + badge("정상","--ok","--green-soft","check-circle")
     + badge("확인","--warn","--orange-soft","warning")
     + badge("문제","--danger","--red-soft","x-circle")
     + badge("참고","--info","--blue-soft","info") + '</div>',
     "색 면만 있는 배지는 만들지 않는다. 글자가 뜻을 지고 색은 빠르게 찾게 돕는다.")),
  ("raw", spec(["속성", "값"], [
     ["글자 크기", "<code>--fs-tag</code> 10px 또는 <code>--fs-xs</code> 11px"],
     ["라운드", "<code>--r-xs</code> 6px — 16px 이면 뭉개진다"],
     ["안쪽 여백", "가로 8px · 세로 3px"],
     ["색", "전경 <code>--ok</code> 계열 · 배경 <code>-soft</code> 계열"],
   ], "배지 색 조합은 <code>check_contrast.py</code> 가 <b>-soft 배경 위에서</b> 검사한다 — 흰 배경에서만 통과하는 조합은 실제로 쓰이는 자리에서 미달일 수 있다.")),
  ("rule", "숫자 배지는 읽지 않은 개수에만",
   "그리고 반드시 최신 상태를 유지한다. 안 지워지는 배지가 신뢰를 가장 빨리 무너뜨린다."),
  ("rule", "배지만으로 전달되는 정보를 만들지 않는다",
   "배지는 <b>이미 아는 것을 빨리 찾게</b> 하는 표식이다. 그것만 봐야 알 수 있는 정보를 담지 않는다."),

  ("h2", "함께 쓸 때", "together"),
  ("rule", "한 줄에 세 가지를 다 넣지 않는다",
   "세그먼트로 화면을 고르고, 그 아래 칩으로 좁히고, 결과 안에 배지가 있다. 층이 다르므로 줄도 나눈다."),
  ("raw", fig('<div style="display:flex;flex-direction:column;gap:10px;width:100%;max-width:290px">'
     + seg(["보유","관심","기록"])
     + chips(["전체","급등","배당"], on=(0,))
     + '<div class="imt-row" style="width:100%">삼성전자'
       '<span style="margin-left:auto">' + badge("정상","--ok","--green-soft") + '</span></div>'
     + '</div>', "위에서 아래로 좁혀진다. 각 층이 하는 일이 다르다.")),
 ],
}
