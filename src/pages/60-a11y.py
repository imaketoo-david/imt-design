# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, scale, spec, grid, fig, ic

def tapbox(size, ok):
    col = "--ok" if ok else "--danger"
    return (f'<div style="position:relative;display:grid;place-items:center;'
            f'width:{size}px;height:{size}px;border:1.5px dashed var({col});border-radius:10px">'
            f'<button class="imt-btn imt-btn--icon" style="height:30px;width:30px;min-height:0"'
            f' aria-label="더보기">{ic("more")}</button></div>')

def txt(c, bg, label):
    return (f'<div style="width:100%;background:{bg};border-radius:var(--r-in);padding:var(--sp-4);'
            f'box-shadow:var(--edge)"><div style="color:{c};font-size:var(--fs-md);line-height:1.6">'
            f'최근 3개월 수익률은 12.4% 입니다</div>'
            f'<div style="margin-top:6px;font:var(--fw-r) var(--fs-tag) var(--font-num);color:var(--sub)">'
            f'{label}</div></div>')

focus_on = ('<button class="imt-btn imt-btn--soft" style="box-shadow:var(--ring)">계획 추가</button>')
focus_off = ('<button class="imt-btn imt-btn--soft">계획 추가</button>')

PAGE = {
 "slug": "accessibility", "group": "기초", "kicker": "기초",
 "title": "접근성",
 "abstract": "배려가 아니라 규격이다. 수치가 정해져 있으니 눈으로 다투지 않고 기계가 판정한다.",
 "blocks": [

  ("h2", "대비", "contrast"),
  ("rule", "기본값이 못 맞추면 최소한 고대비 모드에서는 맞춘다",
   "애플이 명시한 방식이고, 애플 자신도 시스템 색에 별도 accessible 변형을 둔다. 우리 <code>@media (prefers-contrast: more)</code> 블록이 그 역할이다."),
  ("raw", spec(["글자 크기", "굵기", "최소 대비"], [
     ["17pt 이하", "전부", "<b>4.5 : 1</b>"],
     ["18pt 이상", "전부", "<b>3 : 1</b>"],
     ["전부", "Bold", "<b>3 : 1</b>"],
     ["비텍스트 (차트 마크·아이콘·경계)", "—", "<b>3 : 1</b>"],
   ])),
  ("raw", cmp2([
     ("do", txt("var(--sub)", "var(--card)", "--sub #6e6e74 · 5.07:1"),
      "라벨색이 기준을 넘는다"),
     ("no", txt("#a4a4aa", "var(--card)", "#a4a4aa · 2.48:1"),
      "흐린 회색 — 밝은 곳에서 사라진다"),
   ], "오른쪽은 실내 모니터에서는 읽히지만 햇빛 아래 아이폰에서는 사라진다. 그래서 눈이 아니라 계산이 판정한다.")),
  ("rule", "라이트·다크 양쪽에서 검사한다",
   "한쪽만 통과하는 색은 통과가 아니다. <code>python3 check_contrast.py</code> 가 라이트·다크·고대비 세 벌을 한 번에 검사한다."),
  ("rule", "비활성 글자는 기준에서 면제된다",
   "그래서 <code>--sub2</code> 는 낮은 대비를 유지한다. 대신 <b>플레이스홀더는 실제로 읽는 글자</b>이므로 <code>--placeholder</code> 로 분리해 4.5:1 을 지킨다. 이 둘을 헷갈리면 화면이 필요 이상으로 어두워진다."),

  ("h2", "컨트롤 크기", "size"),
  ("rule", "기준은 '보이는 크기' 가 아니라 '히트영역' 이다",
   "38px 버튼이라도 눌리는 범위가 44px 면 규격을 만족한다. 마우스 환경까지 44px 로 키우면 대시보드 밀도가 무너지므로, 우리는 <code>@media (pointer: coarse)</code> 에서만 확장한다."),
  ("raw", cmp2([
     ("do", tapbox(44, True),  "히트영역 44 × 44 — 보이는 건 30px"),
     ("no", tapbox(30, False), "보이는 크기 그대로 30 × 30"),
   ], "점선이 실제로 눌리는 범위다. 투명한 여백을 넓히는 것이지 버튼을 키우는 게 아니다.")),
  ("raw", spec(["플랫폼", "기본", "최소", "토큰"], [
     ["iOS · iPadOS · watchOS", "44 × 44 pt", "28 × 28 pt", "<code>--tap</code> / <code>--tap-min</code>"],
     ["macOS", "28 × 28 pt", "20 × 20 pt", "<code>--ctl</code> / <code>--ctl-min</code>"],
     ["visionOS", "60 × 60 pt", "28 × 28 pt", "<code>--tap-vision</code>"],
   ], "간격도 크기만큼 중요하다 — 테두리 있는 요소 주위 <code>--gap-ctl</code>(12px), 없는 요소 주위 <code>--gap-ctl-plain</code>(24px).")),

  ("h2", "글자 최소 크기", "fontsize"),
  ("raw", spec(["플랫폼", "기본", "최소"], [
     ["iOS · iPadOS", "17 pt", "11 pt"],
     ["macOS", "13 pt", "10 pt"],
     ["visionOS", "17 pt", "12 pt"],
   ], "<code>--fs-tag</code>(10px) 는 macOS 최소치에는 맞지만 iOS 최소치보다 작다. 모바일에서 뜻이 있는 글자에는 <code>--fs-xs</code>(11px) 이상을 쓴다.")),
  ("rule", "가는 굵기를 쓰지 않는다",
   "Ultralight·Thin·Light 는 작은 글자에서 읽히지 않는다. 우리 토큰에 아예 없다."),

  ("h2", "키보드", "keyboard"),
  ("rule", "포커스 링을 없애면 키보드 사용자는 길을 잃는다",
   "<code>outline:none</code> 만 쓰고 대체를 만들지 않는 것이 가장 흔한 실수다. 지금 어디에 있는지 보이지 않으면 Tab 을 누를 이유가 없어진다."),
  ("raw", cmp2([
     ("do", focus_on,  "<code>:focus-visible</code> 에 <code>--ring</code>"),
     ("no", focus_off, "<code>outline:none</code> 만 — 위치를 알 수 없다"),
   ])),
  ("rule", "Tab 순서가 시각 순서와 같아야 한다",
   "CSS 로 위치만 바꾸면 화면에서는 위에 있는데 Tab 은 나중에 닿는다. 갇히는 곳(포커스 트랩)이 없는지도 확인한다 — 모달은 <b>일부러</b> 가두되 Esc 로 나갈 수 있어야 한다."),

  ("h2", "색만으로 뜻을 전하지 않는다", "color"),
  ("p", "적록색각인 사람에게 빨강과 초록은 같은 색이다. 상태·등락은 반드시 아이콘이나 라벨과 함께 쓰고, 차트는 시리즈가 둘 이상이면 범례를 항상 넣는다. 자세한 것은 <a href='color.html#inclusive'>색</a> 문서에 있다."),

  ("h2", "시스템 설정을 존중한다", "prefs"),
  ("p", "사용자가 이미 정한 것을 앱이 무시하지 않는다. 세 가지 모두 <code>tokens.css</code> 에 들어 있어 컴포넌트를 만들 때 따로 신경 쓸 일이 없다."),
  ("raw", spec(["설정", "우리 대응"], [
     ["<code>prefers-reduced-motion</code>", "모든 전환 0.01ms"],
     ["<code>prefers-contrast: more</code>", "고대비 색 구성으로 교체"],
     ["<code>prefers-reduced-transparency</code>", "머티리얼·유리를 불투명 면으로"],
     ["<code>prefers-color-scheme</code>", "다크 모드 (사용자 토글이 OS 설정을 이긴다)"],
   ])),

  ("h2", "배포 전에 확인하는 다섯", "check"),
  ("raw", spec(["□", "확인"], [
     ["1", "<code>python3 check_contrast.py</code> 가 통과하는가"],
     ["2", "다크 모드에서 열어봤는가"],
     ["3", "키보드 Tab 만으로 전부 닿고 포커스가 보이는가"],
     ["4", "아이콘만 있는 버튼에 <code>aria-label</code> 이 있는가"],
     ["5", "화면을 흑백으로 만들어도 뜻이 전해지는가"],
   ])),
 ],
}
