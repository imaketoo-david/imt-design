# -*- coding: utf-8 -*-
from figures import spec, fig, ic

def modal(title, body, actions, w="270px", r="--r-sheet"):
    return (f'<div style="width:100%;max-width:{w};background:var(--sheet);border-radius:var({r});'
      f'box-shadow:var(--sh-lift);padding:var(--sp-5)">'
      f'<div style="font:var(--fw-sb) var(--fs-lg)/1.4 var(--font);letter-spacing:var(--tr-xl);'
      f'color:var(--ink)">{title}</div>'
      f'<div style="font-size:var(--fs-md);color:var(--sub);margin-top:6px;line-height:1.55">{body}</div>'
      f'<div style="display:flex;gap:8px;margin-top:var(--sp-4)">{actions}</div></div>')

B = lambda c, t: f'<button class="imt-btn {c}" style="flex:1">{t}</button>'

sheet = ('<div style="width:100%;max-width:270px;background:var(--sheet);'
  'border-radius:var(--r-sheet) var(--r-sheet) 0 0;box-shadow:var(--sh-lift);'
  'padding:var(--sp-3) var(--sp-5) var(--sp-5)">'
  '<div style="width:36px;height:4px;border-radius:99px;background:var(--fill1);margin:0 auto 14px"></div>'
  '<div style="font:var(--fw-sb) var(--fs-lg) var(--font);color:var(--ink)">계획 만들기</div>'
  '<div style="font-size:var(--fs-md);color:var(--sub);margin-top:6px">목표가와 수량을 정합니다</div>'
  '<div style="height:52px"></div>'
  '<button class="imt-btn imt-btn--primary" style="width:100%">저장</button></div>')

toast = ('<div class="imt-toast on" style="position:static;width:100%;max-width:290px;'
  'display:flex;align-items:center;gap:10px">' + ic("check-circle")
  + '계획을 저장했습니다<button class="imt-btn imt-btn--ghost imt-btn--sm" '
    'style="margin-left:auto">되돌리기</button></div>')

PAGE = {
 "slug": "overlays", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "모달 · 시트 · 토스트",
 "abstract": "무엇을 언제 띄울지는 <a href='overlay.html'>겹침</a>에서 정한다. 여기서는 그 셋의 생김새와 사양을 정한다.",
 "blocks": [

  ("h2", "경고 (alert)", "alert"),
  ("raw", fig(modal("기록 3건을 삭제할까요?", "되돌릴 수 없습니다.",
     B("imt-btn--soft","취소") + B("imt-btn--danger","삭제")),
     "제목이 <b>질문이나 결과</b>를 말한다. 버튼은 동사다.")),
  ("raw", spec(["속성", "값"], [
     ["폭", "최대 270~320px · 가운데"],
     ["라운드", "<code>--r-sheet</code> 22px"],
     ["그림자", "<code>--sh-lift</code>"],
     ["배경 덮개", "검정 30~40% · 눌러서 닫히게"],
     ["버튼", "가로 두 개. 셋을 넘으면 세로로 쌓는다"],
     ["기본 동작", "오른쪽. 단 파괴적 동작은 기본값으로 두지 않는다"],
   ])),
  ("rule", "Esc 로 닫힌다",
   "닫는 방법이 버튼 하나뿐이면 갇힌 느낌이 난다. 포커스는 모달 안에 가두되 Esc 로 나갈 수 있어야 한다."),

  ("h2", "시트", "sheet"),
  ("raw", fig(sheet, "손잡이(grabber)가 있으면 내려서 닫을 수 있다는 뜻이다. 손잡이 없이 스와이프로만 닫히게 만들지 않는다.")),
  ("raw", spec(["속성", "값"], [
     ["라운드", "위쪽만 <code>--r-sheet</code> 22px"],
     ["높이", "내용에 맞추되 화면의 90% 를 넘지 않는다"],
     ["손잡이", "36 × 4px · <code>--fill1</code>"],
     ["주 동작", "맨 아래 전체 폭"],
     ["닫기", "Esc · 바깥 클릭 · 내려서 닫기"],
   ])),
  ("rule", "시트 안에서 또 시트를 열지 않는다",
   "두 겹째부터 사용자는 자기가 어디 있는지 잃는다. 그 정도 분량이면 화면을 하나 만든다."),

  ("h2", "토스트", "toast"),
  ("raw", fig(toast, "3~5초. 조작을 막지 않는다. 파괴적 동작에는 <b>되돌리기</b>를 붙이고, 실제 삭제를 그 시간만큼 미룬다.")),
  ("raw", spec(["속성", "값"], [
     ["위치", "화면 아래 가운데 · 모바일은 탭바 위"],
     ["폭", "내용에 맞추되 최대 <code>--w-content</code> 의 절반"],
     ["시간", "3초 · 되돌리기가 있으면 5초"],
     ["동시 개수", "하나. 새 것이 오면 이전 것을 교체한다"],
     ["층", "<code>--z-toast</code> 500 — 가장 위"],
   ])),
  ("rule", "토스트에 중요한 정보를 담지 않는다",
   "사라지는 것이 전제다. 놓치면 안 되는 것은 화면 안에 남긴다."),

  ("h2", "팝오버", "popover"),
  ("raw", spec(["속성", "값"], [
     ["위치", "누른 자리 근처. 화면 밖으로 나가면 반대편으로 뒤집는다"],
     ["폭", "180~280px"],
     ["라운드", "<code>--r</code> 16px"],
     ["그림자", "<code>--sh-lift</code>"],
     ["닫기", "바깥 클릭 · Esc · 항목 선택"],
     ["항목", "7개 이하. 파괴적 항목은 맨 아래에 떼어 놓는다"],
   ])),

  ("h2", "공통 규칙", "common"),
  ("raw", spec(["규칙", "이유"], [
     ["한 번에 하나", "먼저 닫고 다음을 연다"],
     ["열릴 때 포커스를 안으로", "키보드 사용자가 내용에 닿을 수 있어야 한다"],
     ["닫힐 때 포커스를 원래 자리로", "어디서 열었는지 잃지 않는다"],
     ["배경 스크롤을 잠근다", "뒤가 움직이면 어느 쪽이 활성인지 모른다"],
     ["<code>prefers-reduced-motion</code> 존중", "등장 애니메이션이 눌린다"],
   ])),
 ],
}
