# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, scale, spec, fig, ic

def sw(var, name, sub=""):
    return (f'<div class="g-scale__i"><div class="g-scale__v">'
            f'<div style="width:100%;height:46px;border-radius:var(--r-in);background:var({var});'
            f'box-shadow:var(--edge)"></div></div>'
            f'<div class="g-scale__n">{name}</div><div class="g-scale__u">{sub or var}</div></div>')

def swrow(items):
    return fig('<div class="g-scale">' + "".join(sw(*i) for i in items) + '</div>')

TXT = lambda t, c: f'<div style="color:var({c});font-size:var(--fs-base);line-height:1.6">{t}</div>'

label_stack = ('<div style="width:100%;display:flex;flex-direction:column;gap:2px">'
  + TXT("<b>삼성전자</b>", "--ink")
  + TXT("반도체 · 코스피", "--ink2")
  + TXT("최근 3개월 +12.4%", "--sub")
  + TXT("데이터 없음", "--sub2") + '</div>')

# 색만으로 / 색+모양
only_color = ('<div style="display:flex;flex-direction:column;gap:10px;width:100%">'
  '<div style="display:flex;align-items:center;gap:8px;font-size:var(--fs-md);color:var(--up)">'
  '<span style="width:9px;height:9px;border-radius:50%;background:var(--up)"></span>삼성전자 +2.4%</div>'
  '<div style="display:flex;align-items:center;gap:8px;font-size:var(--fs-md);color:var(--down)">'
  '<span style="width:9px;height:9px;border-radius:50%;background:var(--down)"></span>SK하이닉스 −0.8%</div></div>')
color_plus = ('<div style="display:flex;flex-direction:column;gap:10px;width:100%">'
  '<div style="display:flex;align-items:center;gap:8px;font-size:var(--fs-md);color:var(--up)">'
  + ic("trend-up") + '삼성전자 +2.4%</div>'
  '<div style="display:flex;align-items:center;gap:8px;font-size:var(--fs-md);color:var(--down)">'
  + ic("trend-down") + 'SK하이닉스 −0.8%</div></div>')

badge = lambda t, fg, bg: (f'<span class="imt-badge" style="color:var({fg});background:var({bg})">{t}</span>')
badges = ('<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">'
  + badge("정상", "--ok", "--green-soft") + badge("확인", "--warn", "--orange-soft")
  + badge("문제", "--danger", "--red-soft") + badge("참고", "--info", "--blue-soft") + '</div>')

chart = ('<svg viewBox="0 0 260 110" style="width:100%;max-width:260px">'
  + "".join(f'<line x1="0" y1="{y}" x2="260" y2="{y}" stroke="var(--grid)" stroke-width="1"/>'
            for y in (10, 35, 60, 85))
  + "".join(f'<polyline fill="none" stroke="var(--c{i})" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" points="{pts}"/>'
            for i, pts in enumerate(
              ["8,86 50,72 92,76 134,54 176,44 218,30 252,22",
               "8,96 50,90 92,80 134,82 176,68 218,64 252,52",
               "8,60 50,66 92,58 134,66 176,60 218,72 252,66"], 1))
  + '</svg>')

PAGE = {
 "slug": "color", "group": "기초", "kicker": "기초",
 "title": "색",
 "abstract": "색은 장식이 아니라 의미다. 그래서 이름으로 부르고, 값은 한 파일 안에만 둔다. 값이 바뀌어도 뜻은 그대로여야 한다.",
 "blocks": [

  ("h2", "값이 아니라 의미를 부른다", "semantic"),
  ("p", "코드 어디에도 <code>#7c7c82</code> 같은 값이 나오지 않는다. <code>--sub</code>라고 부른다. 값은 <code>tokens.css</code> 한 파일 안에만 있고, 대비를 맞추려 값을 조정해도 코드는 한 줄도 바뀌지 않는다."),
  ("rule", "의미를 바꿔 쓰지 않는다",
   "구분선 색을 글자색으로, 보조 라벨색을 배경색으로 돌려쓰는 순간 시스템이 무너진다. 다크 모드로 넘어가는 순간 그 자리가 먼저 깨진다 — 각 색이 자기 역할에 맞게 따로 조정되기 때문이다. 필요한 의미가 없으면 새 토큰을 만든다."),

  ("h2", "글자는 네 단계", "label"),
  ("p", "중요도를 크기로 표현하기 전에 <b>색의 진하기</b>로 표현한다. 크기를 바꾸면 레이아웃이 흔들리지만, 진하기는 흔들리지 않는다."),
  ("raw", anatomy(label_stack, [
     (1, "<code>--ink</code>", "본문·값. 읽으라고 쓴 글자."),
     (2, "<code>--ink2</code>", "부제. 본문을 보조한다."),
     (3, "<code>--sub</code>", "라벨·설명. 항상 켜져 있지만 주인공은 아니다."),
     (4, "<code>--sub2</code>", "비활성. <b>대비 기준이 면제되는 유일한 단계</b>다."),
   ], "다섯 번째 단계가 필요하다고 느껴지면 위계 설계를 다시 본다.")),
  ("rule", "플레이스홀더는 비활성색이 아니다",
   "입력 힌트는 실제로 읽어야 하는 글자다. <code>--sub2</code>(비활성)로 칠하면 대비가 모자란다. <code>--placeholder</code>를 따로 두는 이유다. 같은 이유로 본문 링크는 <code>--link</code>를 쓴다 — <code>--brand</code>는 버튼 <b>면</b>의 색이지 글자색이 아니다."),

  ("h2", "색만으로 뜻을 전하지 않는다", "inclusive"),
  ("rule", "적록색각인 사람에게 빨강과 초록은 같은 색이다",
   "이건 배려가 아니라 정확성의 문제다. 색은 뜻을 <b>강화</b>하는 것이지 <b>전달</b>하는 것이 아니다. 아이콘이나 라벨이 뜻을 지고, 색은 그것을 빠르게 찾게 돕는다."),
  ("raw", cmp2([
     ("do", color_plus,  "방향 아이콘이 뜻을 진다"),
     ("no", only_color,  "색 점만으로는 흑백에서 사라진다"),
   ], "화면을 흑백으로 만들어 보면 바로 드러난다. 흑백에서 읽히지 않으면 색에 의존한 것이다.")),

  ("h2", "등락은 한국 관례를 따른다", "trend"),
  ("p", "상승이 빨강, 하락이 파랑이다. 애플 문서도 이걸 지지한다 — 색 문서가 주식 앱 스크린샷 두 장으로 <b>영어권은 초록이 상승, 중국어권은 빨강이 상승</b>이라고 직접 예시한다. 색의 뜻은 문화가 정한다는 것이 원래 규정이다."),
  ("raw", swrow([("--up","상승","--up"),("--down","하락","--down"),("--flat","보합","--flat")])),

  ("h2", "상태색은 넷", "status"),
  ("p", "뜻이 고정된 색이다. 차트 시리즈로 재사용하지 않는다 — '3번 시리즈가 초록'인 화면에서 초록이 '정상'으로도 읽히면 둘 다 읽히지 않는다."),
  ("raw", fig(badges, "배지는 항상 <b>글자와 함께</b> 쓴다. 색 면만 있는 배지는 만들지 않는다.")),
  ("raw", spec(["토큰", "뜻", "함께 쓰는 아이콘"], [
     ["<code>--ok</code>", "정상 · 완료", "<code>check-circle</code>"],
     ["<code>--warn</code>", "확인 필요", "<code>warning</code>"],
     ["<code>--danger</code>", "문제 · 파괴적 동작", "<code>x-circle</code>"],
     ["<code>--info</code>", "참고", "<code>info</code>"],
   ])),

  ("h2", "차트는 8슬롯 고정", "chart"),
  ("rule", "9번째 시리즈는 색을 재사용하지 말고 '기타'로 접는다",
   "같은 색 두 개는 그래프를 거짓말로 만든다. 여덟 개를 넘는 시리즈는 애초에 사람이 읽을 수 없는 양이다."),
  ("raw", fig(chart, "8슬롯은 명도대비·색각(CVD)·채도 검사를 전 항목 통과한 조합이다. 라이트·다크에서 같은 값을 쓴다.")),
  ("raw", swrow([(f"--c{i}", f"슬롯 {i}", "") for i in range(1, 9)])),

  ("h2", "다크는 반전이 아니다", "dark"),
  ("rule", "배경은 검정이 아니라 올리고, 글자는 순백이 아니라 내린다",
   "명도만 뒤집으면 채도가 튀어 보인다. 배경 <code>#000</code> 위의 순백 글자는 눈부시고, 그 위에서 브랜드색은 형광펜처럼 뜬다. 그래서 다크는 <b>따로 고른 값</b>이다 — 면은 <code>#1c1c1e</code>, 글자는 <code>#f5f5f7</code>."),
  ("rule", "그림자 대신 테두리로 면을 나눈다",
   "어두운 배경 위에서는 그림자가 보이지 않는다. 다크에서 <code>--edge</code>는 흰색 7% 테두리로 바뀐다."),

  ("h2", "대비는 눈이 아니라 계산이 판정한다", "contrast"),
  ("raw", spec(["대상", "최소 대비", "검사"], [
     ["17pt 이하 글자", "4.5 : 1", "<code>check_contrast.py</code>"],
     ["18pt 이상 · Bold", "3 : 1", "같음"],
     ["차트 마크 · 아이콘 · 경계", "3 : 1", "같음"],
     ["비활성 글자(<code>--sub2</code>)", "면제", "—"],
   ], "기본값이 이를 못 맞추면 <b>최소한 고대비 모드에서는</b> 맞춘다 — 애플이 명시한 방식이고, 애플 자신도 시스템 색에 별도 accessible 변형을 둔다. 우리 <code>@media (prefers-contrast: more)</code> 블록이 그 역할이다.")),
 ],
}
