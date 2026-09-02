# -*- coding: utf-8 -*-
from figures import cmp2, seq, spec, fig, ic

def ball(dur, ease, label):
    return (f'<div style="text-align:center"><div style="width:100%;height:44px;background:var(--card);'
            f'border-radius:var(--r-in);box-shadow:var(--edge);position:relative;overflow:hidden">'
            f'<span style="position:absolute;top:12px;left:8px;width:20px;height:20px;border-radius:50%;'
            f'background:var(--brand);animation:mv {dur} var({ease}) infinite alternate"></span></div>'
            f'<div style="margin-top:7px;font:var(--fw-m) var(--fs-sm) var(--font);color:var(--ink2)">{label}</div>'
            f'</div>')

anim_css = ('<style>@keyframes mv{from{left:8px}to{left:calc(100% - 28px)}}'
            '@media (prefers-reduced-motion: reduce){[style*="animation"]{animation:none!important}}</style>')

def state(bg, fg, label, extra=""):
    return (f'<div style="background:{bg};color:{fg};border-radius:var(--r);padding:10px 16px;'
            f'font:var(--fw-m) var(--fs-md) var(--font);display:inline-block;{extra}">저장</div>')

PAGE = {
 "slug": "motion", "group": "기초", "kicker": "기초",
 "title": "모션",
 "abstract": "움직임은 어디서 와서 어디로 갔는지 알려주는 도구다. 예쁘라고 넣는 순간 지연이 된다.",
 "blocks": [

  ("raw", anim_css),

  ("h2", "목적이 있을 때만 움직인다", "purpose"),
  ("rule", "자주 일어나는 조작에는 모션을 넣지 않는다",
   "하루에 200번 누르는 버튼의 0.3초 애니메이션은 200번의 지연이다. 처음 볼 때 근사한 것과 200번째에 견딜 만한 것은 다르다."),
  ("p", "모션이 하는 일은 셋 중 하나다. 이 셋에 해당하지 않으면 넣지 않는다."),
  ("raw", spec(["역할", "예", "길이"], [
     ["<b>연결</b> — 어디서 왔는지 알려준다", "카드를 눌러 상세로 들어갈 때", "<code>--dur-3</code> .32s"],
     ["<b>반응</b> — 눌렸다는 것을 알려준다", "버튼 누름, 토글 전환", "<code>--dur-1</code> .12s"],
     ["<b>주의</b> — 바뀐 것을 알려준다", "새 알림, 값 갱신", "<code>--dur-2</code> .2s"],
   ])),

  ("h2", "세 단계뿐", "duration"),
  ("raw", fig('<div style="display:grid;gap:var(--sp-3);grid-template-columns:repeat(auto-fit,minmax(150px,1fr))">'
     + ball(".12s","--ease","--dur-1 · 상태 전환")
     + ball(".2s","--ease","--dur-2 · 펼침")
     + ball(".32s","--ease","--dur-3 · 화면 전환") + '</div>',
     "길이를 자유롭게 고르기 시작하면 같은 종류의 동작이 화면마다 다른 속도로 돈다.")),
  ("raw", spec(["토큰", "곡선", "쓰는 곳"], [
     ["<code>--ease</code>", "<code>cubic-bezier(.4,0,.2,1)</code>", "기본. 거의 전부 여기에 해당한다"],
     ["<code>--spring</code>", "<code>cubic-bezier(.34,1.4,.5,1)</code>", "튕김이 뜻을 지는 자리에만 — 토스트 등장, 성공 표시"],
   ], "선형(<code>linear</code>)은 쓰지 않는다. 현실의 물체는 등속으로 움직이지 않아서, 눈이 기계적이라고 읽는다.")),

  ("h2", "가속과 감속의 방향", "easing"),
  ("rule", "들어올 때는 빠르게 시작해 부드럽게 멈추고, 나갈 때는 반대다",
   "들어오는 것은 곧 볼 것이므로 빨리 자리 잡아야 하고, 나가는 것은 이미 다 본 것이므로 시선을 붙잡을 필요가 없다."),

  ("h2", "상태는 반드시 보인다", "states"),
  ("rule", "눌러도 아무 변화가 없으면 사람들은 눌렸는지 의심한다",
   "그리고 한 번 더 누른다. 주문이 두 번 나가는 사고는 대개 여기서 시작된다."),
  ("raw", seq([
     (state("var(--brand)", "#fff", "기본"), "기본"),
     (state("var(--brand-hover)", "#fff", "hover"), "hover"),
     (state("var(--brand)", "#fff", "active", "transform:scale(.97);opacity:.9"), "active"),
     (state("var(--brand)", "#fff", "focus", "box-shadow:var(--ring)"), "focus-visible"),
     (state("var(--fill2)", "var(--sub2)", "비활성"), "비활성"),
   ], "다섯 상태를 다 만들지 않은 컴포넌트는 미완성이다.")),

  ("h2", "모션은 선택이다", "reduce"),
  ("rule", "<code>prefers-reduced-motion</code> 에서 전부 멈춘다",
   "전정기관이 예민한 사람에게 화면의 움직임은 실제로 멀미를 일으킨다. 이 설정은 취향이 아니라 증상에 대한 요청이다."),
  ("p", "이미 <code>tokens.css</code> 에 들어 있어 따로 신경 쓸 일이 없다. 다만 <b>애니메이션에 의존해서만 전달되는 정보를 만들지 않는 것</b>은 우리 몫이다 — 움직임이 멈춰도 뜻이 남아야 한다."),
  ("rule", "움직임을 줄일 때는 이동 대신 페이드",
   "위치를 옮기는 대신 흐려지며 바뀌게 한다. 튕김은 줄이고, 흐림에서 흐림으로 가는 전환은 피한다."),

  ("h2", "하지 않는 것", "avoid"),
  ("raw", spec(["금지", "이유"], [
     ["끝없이 반복되는 애니메이션", "시선을 계속 뺏는다. 로딩 표시만 예외다"],
     ["여러 요소가 동시에 다르게 움직이기", "어디를 봐야 할지 알 수 없다"],
     ["0.4초를 넘는 전환", "기다리는 것으로 느껴진다"],
     ["스크롤에 연동된 큰 움직임", "스크롤은 사용자의 것이지 우리 것이 아니다"],
     ["의미 없는 등장 애니메이션", "목록 20개가 차례로 나타나는 화면은 20번 기다리게 한다"],
   ])),
 ],
}
