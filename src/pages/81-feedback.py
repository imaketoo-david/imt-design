# -*- coding: utf-8 -*-
from figures import cmp2, spec, seq, fig, ic

SKEL = ('<div style="width:100%;display:flex;flex-direction:column;gap:8px">'
  + "".join(f'<div class="imt-skel" style="height:{h}px;border-radius:8px"></div>'
            for h in (14, 14, 14)) + '</div>')
SPIN = ('<div style="display:grid;place-items:center;width:100%;min-height:64px;color:var(--sub)">'
  '<svg viewBox="0 0 24 24" style="width:26px;height:26px;fill:none;stroke:currentColor;'
  'stroke-width:2;stroke-linecap:round"><path d="M12 3.5a8.5 8.5 0 1 1-6 2.5" opacity=".9"/></svg></div>')
BAR = ('<div style="width:100%"><div style="height:6px;border-radius:99px;background:var(--fill3);'
  'overflow:hidden"><div style="width:64%;height:100%;background:var(--brand)"></div></div>'
  '<div style="margin-top:8px;font-size:var(--fs-sm);color:var(--sub)">1,280 / 2,000 건 · 약 40초 남음</div></div>')

def toast(icon, color, msg, action=""):
    a = (f'<button class="imt-btn imt-btn--ghost imt-btn--sm" style="margin-left:auto">{action}</button>'
         if action else "")
    return (f'<div style="display:flex;align-items:center;gap:10px;background:var(--card);'
            f'border-radius:var(--r);box-shadow:var(--sh-lift);padding:11px 14px;width:100%;'
            f'font-size:var(--fs-md);color:var(--ink)"><span style="color:var({color})">{icon}</span>{msg}{a}</div>')

err_good = (f'<div style="width:100%;background:var(--red-soft);border-radius:var(--r-in);'
  f'padding:12px 14px;font-size:var(--fs-md);color:var(--ink2);line-height:1.55">'
  f'<b style="color:var(--danger);display:flex;align-items:center;gap:6px">{ic("x-circle")}저장하지 못했습니다</b>'
  f'<div style="margin-top:4px">네트워크가 끊겼습니다. 연결을 확인한 뒤 다시 시도해 주세요 — '
  f'입력한 내용은 그대로 남아 있습니다.</div></div>')
err_bad = (f'<div style="width:100%;background:var(--red-soft);border-radius:var(--r-in);'
  f'padding:12px 14px;font-size:var(--fs-md);color:var(--danger)">오류가 발생했습니다 (E_UNKNOWN)</div>')

empty = (f'<div class="imt-empty" style="width:100%">{ic("doc","imt-i--scale-l")}'
  f'<div style="font:var(--fw-sb) var(--fs-base) var(--font);color:var(--ink);margin-top:6px">'
  f'아직 계획이 없습니다</div>'
  f'<div style="font-size:var(--fs-sm);color:var(--sub);margin-top:4px">'
  f'목표가와 수량을 정해두면 조건에 닿았을 때 알려드립니다</div>'
  f'<button class="imt-btn imt-btn--primary imt-btn--sm" style="margin-top:12px">첫 계획 만들기</button></div>')

PAGE = {
 "slug": "feedback", "group": "패턴", "kicker": "패턴",
 "title": "피드백",
 "abstract": "지금 무슨 일이 일어나고 있는지, 끝났는지, 잘못됐다면 무엇을 하면 되는지. 이 셋을 화면이 먼저 말하게 한다.",
 "blocks": [

  ("h2", "기다리게 하는 법", "loading"),
  ("rule", "가장 먼저 할 일은 무언가를 보여주는 것이다",
   "빈 화면은 '느리다' 가 아니라 '고장났다' 로 읽힌다. 뼈대라도 먼저 그리면 사람들은 기다린다."),
  ("raw", cmp2([
     ("do", SKEL, "뼈대를 먼저 그린다 — 곧 올 모양을 예고한다"),
     ("no", SPIN, "돌아가는 표시만 — 무엇을 기다리는지 모른다"),
   ], "뼈대는 최종 레이아웃과 <b>같은 모양</b>이어야 한다. 다르면 값이 들어올 때 화면이 튄다.")),
  ("rule", "알 수 있으면 진행률을 알려준다",
   "비결정 스피너는 마지막 수단이다. 알게 되는 순간 결정형 막대로 바꾼다 — 반대 방향(막대 → 스피너)으로는 바꾸지 않는다."),
  ("raw", fig(BAR, "남은 개수와 예상 시간이 있으면 기다리는 느낌이 절반으로 준다.")),
  ("raw", spec(["기다리는 시간", "표시"], [
     ["0.1초 미만", "아무것도 안 한다 — 표시가 오히려 깜박임이 된다"],
     ["0.1 ~ 1초", "커서·버튼 상태만"],
     ["1 ~ 10초", "뼈대 또는 진행 막대"],
     ["10초 이상", "진행률 + 남은 시간 + 중단 수단"],
   ])),

  ("h2", "끝났다고 말한다", "done"),
  ("rule", "결과가 화면에 안 보이는 일만 알린다",
   "목록에 항목이 추가되는 것이 보이면 '추가했습니다' 토스트는 소음이다. 뒤에서 일어난 일, 오래 걸린 일, 되돌릴 수 없는 일만 알린다."),
  ("raw", fig('<div style="display:flex;flex-direction:column;gap:8px;width:100%;max-width:380px">'
     + toast(ic("check-circle"), "--ok", "계획을 저장했습니다")
     + toast(ic("trash"), "--danger", "기록 3건을 삭제했습니다", "되돌리기")
     + '</div>',
     "파괴적 동작에는 <b>되돌리기</b>를 붙인다. 확인창으로 미리 막는 것보다 낫다 — 확인창은 세 번째부터 읽히지 않는다.")),

  ("h2", "안 되는 이유를 말한다", "error"),
  ("rule", "'오류가 발생했습니다' 는 정보가 아니다",
   "무엇이 · 왜 안 됐고 · 다음에 뭘 하면 되는지. 셋을 다 말한다. 그리고 <b>입력한 내용이 남아 있는지</b>를 반드시 알려준다 — 그게 가장 궁금한 것이다."),
  ("raw", cmp2([
     ("do", err_good, "무엇이 · 왜 · 다음에 무엇을"),
     ("no", err_bad,  "코드만 — 사용자가 할 수 있는 일이 없다"),
   ])),
  ("rule", "사람을 주어로 쓰지 않는다",
   "'잘못 입력하셨습니다' 가 아니라 '날짜 형식이 맞지 않습니다'. 오류는 대개 설계의 결과이지 사용자의 잘못이 아니다."),

  ("h2", "빈 화면은 실패가 아니라 시작점이다", "empty"),
  ("rule", "왜 비었는지와 무엇을 하면 채워지는지를 쓴다",
   "빈 목록에 아무 말도 없으면 사용자는 '불러오기에 실패했나' 를 먼저 의심한다."),
  ("raw", fig(empty, "검색 결과가 없는 경우라면 <b>검색어를 다시 보여주고</b> 조건을 넓힐 방법을 제안한다.")),

  ("h2", "네 단계", "levels"),
  ("raw", spec(["단계", "색", "아이콘", "쓸 때"], [
     ["오류", "<code>--danger</code>", "<code>x-circle</code>", "사용자가 하려던 일이 실패했다"],
     ["확인", "<code>--warn</code>", "<code>warning</code>", "됐지만 봐야 할 것이 있다"],
     ["참고", "<code>--info</code>", "<code>info</code>", "알아두면 좋은 것"],
     ["정상", "<code>--ok</code>", "<code>check-circle</code>", "이상 없음"],
   ], "네 단계 모두 <b>색과 아이콘을 같이</b> 쓴다. 색만으로는 흑백과 색각 이상에서 구분되지 않는다.")),

  ("h2", "무엇으로 알릴 것인가", "channel"),
  ("raw", spec(["상황", "수단", "이유"], [
     ["그 자리에서 알 수 있는 것", "인라인", "중단하지 않는다"],
     ["짧은 결과 알림", "토스트 3~5초", "조작을 막지 않는다"],
     ["되돌릴 수 없는 파괴적 동작", "경고(alert)", "여기서만 멈춰 세운다"],
     ["의도한 동작의 선택지", "액션시트 · 메뉴", "중단이 아니라 이어짐이다"],
   ], "경고는 아껴 쓴다. 앱을 켜자마자 뜨는 경고, 정보 전달용 경고는 만들지 않는다.")),
 ],
}
