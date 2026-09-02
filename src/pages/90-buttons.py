# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, seq, spec, fig, ic

B = lambda cls, t, extra="": f'<button class="imt-btn {cls}" style="{extra}">{t}</button>'
ROW = lambda inner, gap="var(--gap-ctl)": f'<div style="display:flex;gap:{gap};align-items:center;flex-wrap:wrap">{inner}</div>'

anat = ('<div style="position:relative">'
  + B("imt-btn--primary", ic("plus") + "계획 추가")
  + '<span class="g-pin g-pin--abs" style="left:-4px;top:-14px">1</span>'
  + '<span class="g-pin g-pin--abs" style="right:-4px;top:-14px">2</span>'
  + '<span class="g-pin g-pin--abs" style="left:26px;bottom:-16px">3</span>'
  + '</div>')

hier_good = ROW(B("imt-btn--primary","저장") + B("imt-btn--soft","취소"))
hier_bad  = ROW(B("imt-btn--primary","저장") + B("imt-btn--primary","취소") + B("imt-btn--primary","삭제"))

size_good = ROW(B("imt-btn--primary","저장") + B("imt-btn--soft","취소"))
size_bad  = ROW(B("imt-btn--primary","저장", "height:48px;font-size:var(--fs-lg)") + B("imt-btn--soft","취소","height:30px"))

label_good = ROW(B("imt-btn--danger","삭제") + B("imt-btn--soft","취소"))
label_bad  = ROW(B("imt-btn--primary","확인") + B("imt-btn--soft","취소"))

PAGE = {
 "slug": "buttons", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "버튼",
 "abstract": "누르면 무슨 일이 일어나는지, 그리고 그중 무엇이 가장 중요한지를 모양으로 말한다.",
 "blocks": [

  ("h2", "생김새", "anatomy"),
  ("raw", anatomy(anat, [
     (1, "면", "라운드 <code>--r</code> 16px, 높이 38px. 강조 단계에 따라 면색이 바뀐다."),
     (2, "히트영역", "터치 환경에서 44px 로 넓어진다. 보이는 높이는 그대로다."),
     (3, "이름", "동사. <code>--fs-callout</code> 16px · <code>--fw-m</code> 500."),
   ], "아이콘을 함께 쓸 때는 이름 <b>앞</b>에 둔다 — 눈이 왼쪽에서 오른쪽으로 훑기 때문이다.")),

  ("h2", "강조는 네 단계", "hierarchy"),
  ("raw", fig(ROW(
     B("imt-btn--primary","기본 동작") + B("imt-btn--soft","보조") +
     B("imt-btn--ghost","약함") + B("imt-btn--danger","파괴적")), "")),
  ("raw", spec(["단계", "클래스", "쓸 때", "화면당"], [
     ["기본", "<code>--primary</code>", "이 화면에서 가장 하고 싶어 할 일", "하나에서 둘"],
     ["보조", "<code>--soft</code>", "함께 놓이는 대안 (취소·나중에)", "제한 없음"],
     ["약함", "<code>--ghost</code>", "툴바·목록 안의 잦은 동작", "제한 없음"],
     ["파괴적", "<code>--danger</code>", "되돌릴 수 없는 삭제", "기본값으로 두지 않는다"],
   ])),
  ("rule", "강조 버튼이 셋이면 아무것도 강조되지 않는다",
   "무엇을 눌러야 할지 고르는 데 시간이 걸리고, 그 시간은 화면을 볼 때마다 든다."),
  ("raw", cmp2([
     ("do", hier_good, "하나만 강조한다"),
     ("no", hier_bad,  "전부 강조 — 고르는 데 시간이 든다"),
   ])),

  ("h2", "크기가 아니라 스타일로 구분한다", "size"),
  ("rule", "같은 줄의 버튼은 높이를 맞춘다",
   "크기가 다르면 한 세트로 보이지 않는다. 어느 쪽이 더 중요한지는 <b>면색</b>이 말한다."),
  ("raw", cmp2([
     ("do", size_good, "높이는 같게, 면색으로 구분"),
     ("no", size_bad,  "크기로 구분 — 짝이 아닌 것처럼 보인다"),
   ])),

  ("h2", "이름은 동작을 말한다", "label"),
  ("rule", "'확인' 은 무엇을 확인하는지 말하지 않는다",
   "특히 파괴적 동작에서 위험하다. 버튼만 읽고 누르는 사람이 대부분이라, 버튼이 곧 마지막 설명이다."),
  ("raw", cmp2([
     ("do", label_good, "삭제 — 무슨 일이 일어나는지 말한다"),
     ("no", label_bad,  "확인 — 무엇을 확인하는지 모른다"),
   ], "순수한 정보 알림이 아니면 '확인/OK' 를 쓰지 않는다.")),
  ("raw", spec(["규칙", "예"], [
     ["동사로", "저장 · 삭제 · 계획 추가 · 파일로 채우기"],
     ["더 입력이 필요하면 말줄임표", "이름 변경… · 내보내기…"],
     ["한글 조사를 생략하지 않는다", "종목 추가 ○ / 종목추가 ✕"],
     ["같은 동작은 같은 말로", "한 화면에서 '저장' 과 '보관' 을 섞지 않는다"],
   ])),

  ("h2", "상태 다섯", "states"),
  ("raw", seq([
     (B("imt-btn--primary","저장"), "기본"),
     (B("imt-btn--primary","저장","background:var(--brand-hover)"), "hover"),
     (B("imt-btn--primary","저장","transform:scale(.97);opacity:.92"), "active"),
     (B("imt-btn--primary","저장","box-shadow:var(--ring)"), "focus-visible"),
     (B("imt-btn--primary","저장","background:var(--fill2);color:var(--sub2)"), "비활성"),
   ], "다섯을 다 만들지 않은 버튼은 미완성이다. 특히 <b>active</b> 가 없으면 눌렸는지 의심해서 한 번 더 누른다.")),
  ("rule", "비활성 버튼은 이유를 알려준다",
   "왜 못 누르는지 모르면 사용자는 자기 잘못이라고 생각한다. <code>title</code> 이나 옆의 한 줄로 조건을 말한다 — 또는 아예 감춘다."),

  ("h2", "모양", "shape"),
  ("p", "애플이 주는 모양은 셋이다 — 캡슐(텍스트), 캡슐(텍스트+아이콘), 둥근 사각형. 우리는 <b>둥근 사각형</b>을 기본으로 쓴다. 표와 지표가 빽빽한 화면에서 캡슐은 좌우 여백을 많이 먹어 밀도를 깎기 때문이다."),
  ("raw", fig(ROW(
     B("imt-btn--primary","둥근 사각형") +
     B("imt-btn--soft","캡슐","border-radius:var(--r-cap)") +
     B("imt-btn--icon", ic("more")) ), "캡슐(<code>--r-cap</code>)은 칩·필터에 쓴다. 아이콘 전용 버튼은 정사각이다.")),
  ("rule", "흰 면에 검은 글자 조합은 만들지 않는다",
   "시스템이 <b>선택된 상태</b>를 나타내는 데 쓰는 조합이다. 일반 버튼에 쓰면 항상 켜져 있는 것처럼 보인다."),

  ("h2", "배치", "placement"),
  ("raw", spec(["상황", "순서"], [
     ["일반 (저장/취소)", "취소 → <b>저장</b> · 오른쪽이 기본 동작"],
     ["파괴적 (삭제/취소)", "취소를 반드시 넣고, 삭제를 기본값으로 두지 않는다"],
     ["가로 폭이 좁을 때", "세로로 쌓되 기본 동작을 위에"],
   ])),
  ("rule", "전체 폭 버튼은 피한다",
   "화면 좌우 여백 안에 들어와 있어야 화면에 속한 것으로 보인다. 꼭 써야 한다면 좌우를 안쪽으로 들인다."),
 ],
}
