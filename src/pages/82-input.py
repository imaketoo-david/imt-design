# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, spec, fig, ic

def field(label, val="", ph="", hint="", err="", w="100%"):
    e = (f'<div style="margin-top:5px;font-size:var(--fs-sm);color:var(--danger);'
         f'display:flex;align-items:center;gap:5px">{ic("warning")}{err}</div>') if err else ""
    h = f'<div style="margin-top:5px;font-size:var(--fs-sm);color:var(--sub)">{hint}</div>' if hint else ""
    l = (f'<div style="font-size:var(--fs-sm);color:var(--sub);margin-bottom:5px">{label}</div>'
         if label else "")
    style = "border-color:var(--danger)" if err else ""
    return (f'<div style="width:{w}">{l}<input class="imt-input" style="{style}" '
            f'value="{val}" placeholder="{ph}">{e}{h}</div>')

anat = ('<div style="width:100%;max-width:260px;position:relative">'
  + field("매수 목표가", "68,500", hint="현재가 71,200원")
  + '<span class="g-pin g-pin--abs" style="left:-26px;top:-2px">1</span>'
  + '<span class="g-pin g-pin--abs" style="left:-26px;top:26px">2</span>'
  + '<span class="g-pin g-pin--abs" style="left:-26px;bottom:-2px">3</span>'
  + '</div>')

lbl_good = field("생년월일", "", "2026-09-02", "YYYY-MM-DD")
lbl_bad  = field("", "", "생년월일")

sz_good = ('<div style="display:flex;gap:10px;width:100%">'
  + field("수량", "10", w="72px") + field("종목", "삼성전자") + '</div>')
sz_bad = ('<div style="display:flex;flex-direction:column;gap:10px;width:100%">'
  + field("수량", "10") + field("종목", "삼성전자") + '</div>')

err_field = field("매수 목표가", "abc", err="숫자만 입력할 수 있습니다")

choice_good = ('<div style="display:flex;gap:8px;flex-wrap:wrap">'
  + "".join(f'<button class="imt-chip{" on" if i==1 else ""}">{t}</button>'
            for i, t in enumerate(["1주","10주","100주"])) + '</div>')
choice_bad = field("수량", "", "몇 주를 사시겠습니까?")

PAGE = {
 "slug": "input", "group": "패턴", "kicker": "패턴",
 "title": "입력 받기",
 "abstract": "가장 좋은 입력은 입력하지 않는 것이다. 타이핑은 마지막 수단이고, 그 전에 시스템이 알아내거나 고르게 할 방법을 먼저 찾는다.",
 "blocks": [

  ("h2", "입력을 시키지 않는 순서", "avoid"),
  ("raw", spec(["순서", "방법", "예"], [
     ["1", "시스템에서 얻는다", "오늘 날짜, 현재가, 마지막에 쓴 계좌"],
     ["2", "고르게 한다", "칩·세그먼트·드롭다운"],
     ["3", "붙여넣기·끌어놓기로 받는다", "거래내역 파일, 캡처 이미지"],
     ["4", "타이핑", "위 셋으로 안 되는 것만"],
   ])),
  ("raw", cmp2([
     ("do", choice_good, "자주 쓰는 값은 고르게 한다"),
     ("no", choice_bad,  "매번 타이핑하게 한다"),
   ], "'기타' 를 두면 자유 입력도 남는다. 흔한 경우를 빠르게, 드문 경우를 가능하게.")),

  ("h2", "생김새", "anatomy"),
  ("raw", anatomy(anat, [
     (1, "라벨", "입력 중에도 남아 있어야 한다. <code>--fs-sm</code> · <code>--sub</code>."),
     (2, "필드", "높이 38px, 터치에서 44px. 라운드 <code>--r</code>."),
     (3, "도움말", "형식 예시나 참고값. 오류가 나면 이 자리가 오류 문구로 바뀐다."),
   ])),

  ("h2", "힌트는 라벨을 대신하지 못한다", "label"),
  ("rule", "플레이스홀더는 타이핑을 시작하면 사라진다",
   "라벨을 힌트로 대신하면, 입력을 마친 뒤 그 칸이 무엇이었는지 확인할 방법이 없다. 특히 여러 칸을 채운 뒤 검토할 때 문제가 된다."),
  ("raw", cmp2([
     ("do", lbl_good, "라벨은 남고, 힌트는 <b>형식</b>을 보여준다"),
     ("no", lbl_bad,  "라벨을 힌트로 대신 — 입력하면 사라진다"),
   ])),
  ("rule", "힌트 색은 비활성 색이 아니다",
   "힌트는 실제로 읽어야 하는 글자다. <code>--placeholder</code> 를 쓴다. 비활성 색(<code>--sub2</code>)으로 칠하면 대비가 모자란다."),

  ("h2", "칸 크기가 곧 기대치다", "size"),
  ("rule", "예상 길이에 맞춘다",
   "우편번호 칸이 화면 너비면 무엇을 얼마나 넣으라는 건지 알 수 없다. 반대로 주소 칸이 짧으면 다 안 들어갈 것처럼 보인다."),
  ("raw", cmp2([
     ("do", sz_good, "수량은 짧게, 종목은 길게"),
     ("no", sz_bad,  "전부 같은 폭 — 무엇을 넣을지 안 보인다"),
   ])),

  ("h2", "검증은 입력 중에", "validate"),
  ("rule", "제출을 눌러야 오류를 알려주는 것은 늦다",
   "다만 첫 글자부터 빨갛게 만들지는 않는다 — 아직 다 안 쳤을 뿐이다. <b>칸을 벗어날 때</b>가 적당하다."),
  ("raw", fig(err_field, "오류 문구는 필드 <b>바로 아래</b>에 둔다. 화면 위쪽에 모아두면 어느 칸인지 찾아야 한다.")),
  ("raw", spec(["규칙", "이유"], [
     ["오류가 난 칸에 포커스를 옮긴다", "찾게 하지 않는다"],
     ["입력한 값은 지우지 않는다", "다시 치게 하는 것이 가장 흔한 분노 지점이다"],
     ["숫자 칸에는 숫자 키패드를 띄운다", "<code>inputmode=\"numeric\"</code> 한 줄이다"],
     ["필수 항목을 <b>미리</b> 표시한다", "제출 후에 알려주면 되돌아가야 한다"],
   ])),

  ("h2", "비밀번호와 민감 정보", "secure"),
  ("rule", "비밀번호를 미리 채우지 않는다. 평문으로 저장하지 않는다",
   "예외 없다. 보여주기/숨기기 토글은 제공하되, 기본값은 숨김이다."),

  ("h2", "토글·체크박스·라디오", "choice"),
  ("raw", spec(["컨트롤", "쓸 때", "특징"], [
     ["토글(스위치)", "즉시 반영되는 켜기/끄기", "누르는 순간 적용된다 — 저장 버튼이 없다"],
     ["체크박스", "여러 개를 고르거나 하위 설정이 딸릴 때", "저장을 눌러야 반영된다"],
     ["라디오", "셋 이상 중 하나", "둘뿐이면 체크박스나 세그먼트가 낫다"],
     ["세그먼트", "화면 내용을 바꾸는 전환", "다섯 개까지. 그 이상은 드롭다운"],
   ], "스위치를 체크박스 대신 쓰지 않는다. 스위치는 '지금 적용', 체크박스는 '나중에 저장' 이라는 약속이 이미 학습돼 있다.")),

  ("h2", "키보드", "keyboard"),
  ("raw", spec(["키", "동작"], [
     ["Tab", "다음 칸. 시각 순서와 같아야 한다"],
     ["Enter", "폼 제출 — 단, 여러 줄 입력에서는 줄바꿈"],
     ["Esc", "취소 · 모달 닫기"],
     ["⌘Z", "되돌리기. 재정의하지 않는다"],
   ])),
 ],
}
