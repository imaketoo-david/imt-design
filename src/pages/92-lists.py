# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, spec, fig, ic

def row(title, sub, right, chev=True):
    c = (f'<span style="color:var(--sub2);margin-left:6px">{ic("arrow-right")}</span>') if chev else ""
    return (f'<div class="imt-row" style="width:100%">'
            f'<div style="min-width:0"><div style="font-size:var(--fs-md);color:var(--ink);'
            f'white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{title}</div>'
            f'<div style="font-size:var(--fs-sm);color:var(--sub);margin-top:2px">{sub}</div></div>'
            f'<div style="margin-left:auto;display:flex;align-items:center;'
            f'font-family:var(--font-num);font-size:var(--fs-md);color:var(--ink2)">{right}{c}</div></div>')

lst = ('<div class="imt-list" style="width:100%;max-width:290px">'
  + row("삼성전자", "10주 · 매수가 68,500", "71,200")
  + row("SK하이닉스", "4주 · 매수가 186,000", "184,500")
  + row("현대차", "3주 · 매수가 214,000", "238,000") + '</div>')

anat = (f'<div style="position:relative">{lst}'
  '<span class="g-pin g-pin--abs" style="left:-26px;top:12px">1</span>'
  '<span class="g-pin g-pin--abs" style="left:-26px;top:34px">2</span>'
  '<span class="g-pin g-pin--abs" style="right:-26px;top:20px">3</span></div>')

def tbl(num_right):
    a = "right" if num_right else "left"
    f = "var(--font-num)" if num_right else "var(--font)"
    return ('<table class="imt-table" style="width:100%"><thead><tr>'
      '<th>종목</th>' + f'<th style="text-align:{a}">수량</th><th style="text-align:{a}">평가손익</th>'
      '</tr></thead><tbody>' + "".join(
      f'<tr><td>{n}</td><td style="text-align:{a};font-family:{f}">{q}</td>'
      f'<td style="text-align:{a};font-family:{f};color:var({c})">{p}</td></tr>'
      for n,q,p,c in [("삼성전자","10","+27,000","--up"),("SK하이닉스","4","−6,000","--down"),
                      ("현대차","3","+72,000","--up")]) + '</tbody></table>')

PAGE = {
 "slug": "lists", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "목록과 표",
 "abstract": "많은 것을 한 번에 보여주는 두 가지 방법이다. 훑어보게 할 것인지 비교하게 할 것인지가 갈림길이다.",
 "blocks": [

  ("h2", "목록인가 표인가", "which"),
  ("raw", spec(["", "목록", "표"], [
     ["쓸 때", "항목을 찾아 들어간다", "값을 비교한다"],
     ["열", "1~2개 (제목 + 값)", "3개 이상"],
     ["행 높이", "48px 이상 · 두 줄 가능", "낮게 · 한 줄"],
     ["모바일", "그대로 쓴다", "가로 스크롤하거나 카드로 접는다"],
   ], "표를 모바일에서 그대로 밀어 넣으면 페이지 전체가 가로로 스크롤된다. 표는 자기 컨테이너 안에서만 스크롤해야 한다.")),

  ("h2", "목록 행의 생김새", "anatomy"),
  ("raw", anatomy(anat, [
     (1, "제목", "찾을 때 눈이 닿는 곳. <code>--ink</code>."),
     (2, "보조", "구분에 필요한 최소한. <code>--fs-sm</code> · <code>--sub</code>."),
     (3, "값과 화살표", "오른쪽 끝. 화살표는 들어갈 수 있다는 신호다."),
   ])),
  ("raw", spec(["속성", "값"], [
     ["행 높이", "최소 48px · 터치에서 <code>--tap</code> 44px 이상"],
     ["구분선", "<code>--hairline</code> 0.5px · <code>--line-soft</code>"],
     ["구분선 시작 위치", "제목 왼쪽에 맞춘다 — 아이콘이 있으면 그 뒤부터"],
     ["누름 상태", "<code>--fill4</code> 배경"],
   ])),

  ("h2", "긴 글자를 다루는 법", "truncate"),
  ("rule", "잘리는 것은 제목이 아니라 보조 정보여야 한다",
   "제목이 잘리면 무엇인지 알 수 없다. 제목은 두 줄까지 허용하고, 보조 정보를 줄인다."),
  ("rule", "가운데를 잘라야 하는 것도 있다",
   "파일명·경로처럼 <b>끝이 중요한</b> 문자열은 끝을 남기고 가운데를 자른다."),

  ("h2", "표", "table"),
  ("rule", "숫자는 오른쪽 정렬 · 등폭 폰트",
   "자릿수가 세로로 맞아야 위아래를 비교할 수 있다. 이것 하나로 표의 쓸모가 갈린다."),
  ("raw", cmp2([
     ("do", tbl(True),  "오른쪽 정렬 · <code>--font-num</code>"),
     ("no", tbl(False), "왼쪽 정렬 · 가변폭"),
   ])),
  ("raw", spec(["규칙", "이유"], [
     ["열 제목을 축약하지 않는다", "'전일比' 보다 '전일 대비'"],
     ["빈 칸은 <code>—</code>", "0 인지 없음인지 구분된다"],
     ["단위는 열 제목에 한 번만", "칸마다 '원' 을 붙이면 숫자가 안 보인다"],
     ["행이 20개를 넘으면 검색·필터", "스크롤로 찾게 하지 않는다"],
     ["정렬 가능한 열은 머리를 눌러서", "이미 학습된 동작이다"],
     ["줄무늬 배경은 열이 4개 이상일 때만", "적은 열에서는 소음이다"],
   ])),

  ("h2", "좁은 화면", "narrow"),
  ("rule", "페이지 본문은 절대 가로로 스크롤되지 않는다",
   "넘치는 것은 <b>표 자신</b>이다. 표를 <code>overflow-x:auto</code> 컨테이너에 넣고, 격자 칸에는 <code>min-width:0</code> 을 준다 — 기본값 <code>auto</code> 는 내용보다 작아지지 않는다. 좁은 화면 깨짐의 가장 흔한 원인이다."),
  ("rule", "열이 다섯을 넘으면 카드로 접는 편이 낫다",
   "가로 스크롤은 어느 열을 보고 있는지 잃게 한다. 행 하나를 카드 하나로 바꾸면 세로로 읽힌다."),

  ("h2", "선택과 편집", "select"),
  ("raw", spec(["동작", "규칙"], [
     ["선택", "행 전체가 선택 영역이다. 체크박스만 눌리게 하지 않는다"],
     ["여러 개 선택", "선택 개수와 동작을 <b>하단 고정 바</b>에 모은다"],
     ["삭제", "되돌리기를 준다. 확인창보다 낫다"],
     ["순서 바꾸기", "드래그 손잡이를 명시한다. 아무 데나 잡히면 스크롤과 충돌한다"],
   ])),

  ("h2", "빈 목록", "empty"),
  ("p", "왜 비었는지와 무엇을 하면 채워지는지를 쓴다. 자세한 것은 <a href='feedback.html#empty'>피드백</a>에 있다."),
 ],
}
