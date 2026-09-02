# -*- coding: utf-8 -*-
from figures import cmp2, spec, seq, fig, ic

def fld(val="", ph="", st="", ic_left=None, right=None):
    l = f'<span style="color:var(--sub2);flex:none">{ic(ic_left)}</span>' if ic_left else ""
    r = f'<span style="color:var(--sub2);flex:none;margin-left:auto">{ic(right)}</span>' if right else ""
    if l or r:
        return (f'<label class="imt-search" style="width:100%;{st}">{l}'
                f'<input value="{val}" placeholder="{ph}">{r}</label>')
    return f'<input class="imt-input" style="width:100%;{st}" value="{val}" placeholder="{ph}">'

sw = lambda on: (f'<span class="imt-switch{" on" if on else ""}" role="switch" '
                 f'aria-checked="{"true" if on else "false"}"></span>')
def swrow(label, on):
    return (f'<div class="imt-row" style="width:100%">{label}'
            f'<span style="margin-left:auto">{sw(on)}</span></div>')

PAGE = {
 "slug": "fields", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "입력 필드",
 "abstract": "무엇을 넣어야 하는지, 지금 맞게 넣고 있는지, 틀렸다면 어디가 틀렸는지. 필드 하나가 이 셋을 말해야 한다.",
 "blocks": [

  ("h2", "사양", "spec"),
  ("raw", spec(["속성", "값"], [
     ["높이", "38px · 터치에서 <code>--tap</code> 44px"],
     ["라운드", "<code>--r</code> 16px"],
     ["안쪽 여백", "가로 <code>--sp-3</code> 12px"],
     ["글자", "<code>--fs-md</code> 13px · <code>--ink</code>"],
     ["힌트", "<code>--placeholder</code> — 비활성색(<code>--sub2</code>)이 아니다"],
     ["테두리", "<code>--line</code> · 포커스 시 <code>--ring</code>"],
     ["배경", "<code>--card</code> 또는 <code>--inset</code>"],
   ])),
  ("raw", fig('<div style="display:flex;flex-direction:column;gap:10px;width:100%;max-width:280px">'
     + fld("", "종목명 또는 코드", ic_left="search")
     + fld("68,500")
     + fld("", "메모 (선택)")
     + '</div>')),

  ("h2", "상태", "states"),
  ("raw", seq([
     (fld("", "값 입력", "width:110px"), "기본"),
     (fld("68,500", "", "width:110px;box-shadow:var(--ring)"), "포커스"),
     (fld("68,500", "", "width:110px"), "입력됨"),
     (fld("abc", "", "width:110px;border-color:var(--danger)"), "오류"),
     (fld("68,500", "", "width:110px;background:var(--fill4);color:var(--sub2)"), "비활성"),
   ], "오류 상태는 테두리 색만 바꾸지 않는다 — <b>아래에 무엇이 틀렸는지</b> 한 줄을 붙인다. 색만으로는 색각 이상에서 구분되지 않는다.")),

  ("h2", "지우기와 보조 버튼", "affordance"),
  ("raw", fig('<div style="display:flex;flex-direction:column;gap:10px;width:100%;max-width:280px">'
     + fld("삼성전자", "", ic_left="search", right="close")
     + fld("", "비밀번호", right="eye")
     + '</div>',
     "값이 있을 때만 지우기 버튼을 보인다. 비어 있는데 ✕ 가 있으면 무엇을 지우는 버튼인지 알 수 없다.")),
  ("rule", "보조 버튼도 44px 히트영역을 갖는다",
   "필드 안의 작은 아이콘이 가장 자주 빗맞는 자리다."),

  ("h2", "숫자 입력", "number"),
  ("raw", spec(["규칙", "이유"], [
     ["<code>inputmode=\"numeric\"</code>", "모바일에서 숫자 키패드가 뜬다 — 한 줄이면 된다"],
     ["천 단위 구분을 표시한다", "68500 보다 68,500 이 자릿수를 세지 않게 한다"],
     ["단위를 필드 밖에", "칸 안에 '원' 을 넣으면 입력값과 섞인다"],
     ["증감 버튼은 값이 작을 때만", "수량 1~10 에는 유용하고 가격에는 무의미하다"],
     ["범위를 미리 알린다", "'1 ~ 999' — 넘긴 뒤에 알려주지 않는다"],
   ])),

  ("h2", "토글 · 스위치", "switch"),
  ("raw", fig('<div style="display:flex;flex-direction:column;gap:0;width:100%;max-width:280px" class="imt-list">'
     + swrow("계획 조건 알림", True)
     + swrow("장 마감 요약", False) + '</div>',
     "스위치는 <b>누르는 순간 적용</b>된다. 저장 버튼이 없다는 약속이 이미 학습돼 있다.")),
  ("rule", "스위치를 체크박스 대신 쓰지 않는다",
   "체크박스는 '나중에 저장', 스위치는 '지금 적용'. 이 약속을 어기면 사용자는 저장을 눌러야 하는지 몰라 머뭇거린다."),
  ("raw", spec(["컨트롤", "쓸 때"], [
     ["스위치", "즉시 반영되는 켜기/끄기 · 목록 행 안에서"],
     ["체크박스", "여러 개 선택 · 하위 설정이 딸릴 때 · 저장을 눌러야 반영"],
     ["라디오", "셋 이상 중 하나. 둘뿐이면 체크박스나 세그먼트"],
   ])),

  ("h2", "폼 전체", "form"),
  ("raw", spec(["규칙", "이유"], [
     ["필수 항목을 미리 표시", "제출 후에 알려주면 되돌아가야 한다"],
     ["Tab 순서가 시각 순서와 같게", "CSS 로 위치만 바꾸면 어긋난다"],
     ["Enter 로 제출", "여러 줄 입력에서는 줄바꿈이 우선"],
     ["오류가 나면 그 칸으로 포커스", "찾게 하지 않는다"],
     ["입력값을 지우지 않는다", "다시 치게 하는 것이 가장 흔한 분노 지점이다"],
     ["긴 폼은 나눈다", "한 화면에 열 칸이 넘으면 단계로 쪼갠다"],
   ])),

  ("h2", "비밀번호", "password"),
  ("rule", "미리 채우지 않는다. 평문으로 저장하지 않는다",
   "예외 없다. 보여주기 토글은 제공하되 기본값은 숨김이다."),
 ],
}
