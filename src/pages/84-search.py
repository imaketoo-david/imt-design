# -*- coding: utf-8 -*-
from figures import cmp2, spec, fig, ic

sf = ('<label class="imt-search" style="width:100%;max-width:280px">' + ic("search")
      + '<input placeholder="종목명 · 종목코드">' + '</label>')

sugg = ('<div style="width:100%;max-width:280px">'
  '<label class="imt-search" style="width:100%">' + ic("search")
  + '<input value="삼성"></label>'
  '<div style="margin-top:6px;background:var(--card);border-radius:var(--r);box-shadow:var(--sh);'
  'overflow:hidden">' + "".join(
     f'<div style="display:flex;align-items:center;gap:9px;padding:9px 12px;font-size:var(--fs-md);'
     f'color:var(--ink2);border-bottom:var(--hairline) solid var(--line-soft)">'
     f'<b style="color:var(--ink)">삼성</b>{t}<span style="margin-left:auto;'
     f'font:var(--fw-r) var(--fs-xs) var(--font-num);color:var(--sub2)">{c}</span></div>'
     for t, c in [("전자","005930"),("SDI","006400"),("바이오로직스","207940")]) + '</div></div>')

scope = ('<div style="width:100%;max-width:300px">'
  '<label class="imt-search" style="width:100%">' + ic("search") + '<input value="반도체"></label>'
  '<div class="imt-seg" style="margin-top:8px">'
  + "".join(f'<button{" class=on" if i==0 else ""}>{t}</button>'
            for i, t in enumerate(["전체","보유","관심","기록"])) + '</div></div>')

noresult = ('<div class="imt-empty" style="width:100%;max-width:300px">' + ic("search","imt-i--scale-l")
  + '<div style="font:var(--fw-sb) var(--fs-base) var(--font);color:var(--ink);margin-top:6px">'
    '&ldquo;삼성전자우B&rdquo; 결과 없음</div>'
  '<div style="font-size:var(--fs-sm);color:var(--sub);margin-top:4px;line-height:1.55">'
  '보유 종목에서만 찾고 있습니다.<br>전체로 넓혀 보시겠어요?</div>'
  '<button class="imt-btn imt-btn--soft imt-btn--sm" style="margin-top:12px">전체에서 다시 찾기</button></div>')

PAGE = {
 "slug": "search", "group": "패턴", "kicker": "패턴",
 "title": "검색",
 "abstract": "찾는 것이 목록보다 빠를 때만 검색이 의미가 있다. 그러려면 즉시 반응하고, 무엇을 찾고 있는지 계속 보여야 한다.",
 "blocks": [

  ("h2", "한 곳에서 전부 찾게 한다", "single"),
  ("rule", "검색창이 여러 개면 어디서 찾을지부터 골라야 한다",
   "탭마다 검색이 따로 있으면, 사용자는 못 찾을 때마다 '다른 탭에서 찾아야 하나' 를 의심한다. 하나로 모으고 <b>범위</b>로 좁힌다."),
  ("raw", fig(sf, "힌트에 <b>무엇으로 찾을 수 있는지</b>를 적는다. '검색' 만 있으면 종목코드로도 되는지 알 수 없다.")),

  ("h2", "치는 즉시 반응한다", "instant"),
  ("rule", "Enter 를 눌러야 결과가 나오면 탐색이 아니라 조회가 된다",
   "즉시 반응하면 사람들은 두 글자만 치고 결과를 보며 좁혀 간다. 검색어를 완성하는 부담이 사라진다."),
  ("raw", fig(sugg, "일치한 부분을 굵게 표시한다. 종목코드처럼 <b>식별에 필요한 값</b>을 함께 보여준다.")),
  ("raw", spec(["규칙", "이유"], [
     ["입력이 멈춘 뒤 150~250ms 에 요청", "글자마다 요청하면 서버도 화면도 흔들린다"],
     ["이전 요청은 취소한다", "늦게 온 옛 결과가 새 결과를 덮는 사고가 흔하다"],
     ["결과가 바뀌어도 입력 포커스는 유지", "계속 칠 수 있어야 한다"],
     ["로딩 중에도 이전 결과를 남긴다", "화면이 비면 '없다' 로 읽힌다"],
   ])),

  ("h2", "범위를 항상 보여준다", "scope"),
  ("rule", "지금 어디에서 찾고 있는지 화면에 있어야 한다",
   "'없다' 는 결과의 절반은 <b>범위가 좁아서</b>다. 범위가 보이지 않으면 사용자는 데이터가 없다고 결론 내린다."),
  ("raw", fig(scope, "범위는 넓은 쪽을 기본으로 두고 좁히게 한다. 좁은 쪽이 기본이면 못 찾는 경험이 먼저 온다.")),

  ("h2", "결과가 없을 때", "empty"),
  ("rule", "검색어를 다시 보여주고, 넓힐 방법을 준다",
   "오타였는지 확인할 수 있어야 하고, 한 번 눌러서 범위를 넓힐 수 있어야 한다."),
  ("raw", fig(noresult)),

  ("h2", "기록과 프라이버시", "history"),
  ("rule", "검색 기록을 보여주기 전에 한 번 생각한다",
   "누가 화면을 같이 볼 수 있는 상황이 있다. 지우는 방법을 항상 함께 둔다."),

  ("h2", "결과 화면", "results"),
  ("raw", spec(["규칙", "내용"], [
     ["검색어를 결과에 강조 표시", "왜 이게 나왔는지 보인다"],
     ["개수를 알려준다", "'12건' — 더 좁혀야 하는지 판단하게 한다"],
     ["정렬 기준을 밝힌다", "관련도순인지 최신순인지"],
     ["결과가 많으면 필터를 붙인다", "다시 치게 하지 않는다"],
   ])),
 ],
}
