# -*- coding: utf-8 -*-
from figures import cmp2, spec, fig, ic

def sheet(title, body, actions):
    return (f'<div style="width:100%;max-width:280px;background:var(--sheet);'
      f'border-radius:var(--r-sheet);box-shadow:var(--sh-lift);padding:var(--sp-5);text-align:center">'
      f'<div style="font:var(--fw-sb) var(--fs-lg)/1.4 var(--font);letter-spacing:var(--tr-xl);'
      f'color:var(--ink)">{title}</div>'
      f'<div style="font-size:var(--fs-md);color:var(--sub);margin-top:6px;line-height:1.55">{body}</div>'
      f'<div style="display:flex;gap:8px;margin-top:var(--sp-4)">{actions}</div></div>')

B = lambda cls, t: f'<button class="imt-btn {cls}" style="flex:1">{t}</button>'

alert_good = sheet("기록 3건을 삭제할까요?", "되돌릴 수 없습니다.",
                   B("imt-btn--soft","취소") + B("imt-btn--danger","삭제"))
alert_bad  = sheet("알림", "저장이 완료되었습니다.", B("imt-btn--primary","확인"))

pop = ('<div style="width:100%;max-width:220px;background:var(--card);border-radius:var(--r);'
  'box-shadow:var(--sh-lift);padding:var(--sp-3)">'
  + "".join(f'<div style="display:flex;align-items:center;gap:9px;padding:7px 8px;border-radius:8px;'
            f'font-size:var(--fs-md);color:var(--ink2)">{ic(i)}{t}</div>'
            for i, t in [("edit","수정"),("doc","복제"),("trash","삭제")]) + '</div>')

toast = ('<div style="display:flex;align-items:center;gap:10px;background:var(--card);'
  'border-radius:var(--r);box-shadow:var(--sh-lift);padding:11px 14px;width:100%;max-width:300px;'
  'font-size:var(--fs-md);color:var(--ink)">' + ic("check-circle")
  + '계획을 저장했습니다<button class="imt-btn imt-btn--ghost imt-btn--sm" '
    'style="margin-left:auto">되돌리기</button></div>')

PAGE = {
 "slug": "overlay", "group": "패턴", "kicker": "패턴",
 "title": "겹침",
 "abstract": "무엇을 띄울지 매번 즉흥으로 고르면 앱이 산만해진다. 상황별로 답을 고정해 둔다.",
 "blocks": [

  ("h2", "무엇을 띄울 것인가", "which"),
  ("raw", spec(["상황", "쓸 것", "이유"], [
     ["사용자가 의도한 동작의 선택지", "액션시트 · 메뉴", "중단이 아니라 이어짐이다"],
     ["되돌릴 수 없는 파괴적 동작", "경고(alert)", "여기서만 멈춰 세운다"],
     ["짧은 보조 정보 · 소수의 컨트롤", "팝오버", "맥락을 유지한다"],
     ["여러 단계가 있는 독립 작업", "시트", "단, 앱 안의 앱이 되면 실패다"],
     ["결과 알림", "토스트 3~5초", "조작을 막지 않는다"],
     ["단순 정보 전달", "화면 안에 인라인", "띄우지 않는다"],
   ])),

  ("h2", "경고는 아껴 쓴다", "alert"),
  ("rule", "정보 전달용 경고를 만들지 않는다",
   "경고는 사용자를 멈춰 세우는 도구다. 세 번째부터는 읽지 않고 누르고, 그때부터는 진짜 위험한 경고도 통과한다."),
  ("raw", cmp2([
     ("do", alert_good, "되돌릴 수 없는 일 · 결과를 말한다"),
     ("no", alert_bad,  "이미 끝난 일을 알리려 멈춰 세운다"),
   ], "오른쪽은 토스트면 충분하다.")),
  ("raw", spec(["규칙", "내용"], [
     ["제목이 질문이나 결과를 말한다", "'알림' 이 아니라 '기록 3건을 삭제할까요?'"],
     ["버튼은 동사", "'확인' 이 아니라 '삭제'"],
     ["파괴적 동작에는 취소를 반드시", "그리고 파괴 쪽을 기본값으로 두지 않는다"],
     ["Esc · 바깥 클릭으로 닫힌다", "닫는 방법이 하나뿐이면 갇힌 느낌이 난다"],
     ["앱을 켜자마자 띄우지 않는다", "무엇을 하려던 것도 아닌데 멈춰 세운다"],
   ])),

  ("h2", "되돌리기가 확인창보다 낫다", "undo"),
  ("rule", "먼저 실행하고 되돌릴 수 있게 한다",
   "확인창은 <b>모든 사람에게 매번</b> 비용을 물린다. 되돌리기는 <b>실수한 사람에게 한 번만</b> 비용을 물린다. 정말 되돌릴 수 없는 일에만 확인창을 쓴다."),
  ("raw", fig(toast, "3~5초. 그 안에 되돌릴 수 있게 한다. 파괴적 동작이라면 실제 삭제를 그 시간만큼 미룬다.")),

  ("h2", "팝오버", "popover"),
  ("rule", "누른 자리 근처에 띄운다",
   "어디서 나왔는지 보이지 않으면 무엇에 대한 것인지 알 수 없다. 화면 가운데 띄우는 순간 그건 팝오버가 아니라 모달이다."),
  ("raw", fig(pop, "항목 수를 적게 유지한다. 자주 쓰는 것을 위에 두되, <b>파괴적 동작은 맨 아래에 떼어</b> 놓는다.")),
  ("rule", "팝오버 위에 다른 것을 올리지 않는다",
   "겹침은 한 겹까지다. 두 겹부터는 어느 것을 닫아야 하는지 알 수 없다."),

  ("h2", "시트", "sheet"),
  ("rule", "앱 안의 앱이 되면 실패다",
   "시트 안에서 또 다른 흐름이 시작되고, 그 안에서 또 시트가 열리면 사용자는 자기가 어디 있는지 잃는다. 그 정도 분량이면 화면을 하나 만든다."),
  ("raw", spec(["규칙", "내용"], [
     ["닫는 방법이 항상 명확하다", "Esc · 바깥 클릭 · 닫기 버튼"],
     ["내려서 닫기만으로 닫히게 하지 않는다", "모바일에서 잡을 손잡이(grabber)를 보인다"],
     ["작업 중 닫으면 확인한다", "입력한 내용이 사라지는 경우에만"],
     ["한 번에 하나", "먼저 닫고 다음을 연다"],
   ])),

  ("h2", "층", "layer"),
  ("p", "겹침은 <a href='layout.html#layers'>세 층</a> 중 가장 위다. 나머지 둘을 덮으므로 <b>덮을 만한 이유</b>가 있어야 한다."),
  ("raw", spec(["<code>--z-nav</code>", "100"], [
     ["<code>--z-sticky</code>", "200"],
     ["<code>--z-drop</code>", "300"],
     ["<code>--z-modal</code>", "400"],
     ["<code>--z-toast</code>", "500"],
   ], "z-index 를 임의로 쓰지 않는다. 999999 가 등장하는 순간 그 파일부터 시스템 밖이다.")),
 ],
}
