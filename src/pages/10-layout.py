# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, scale, spec, grid, fig, ic

CARD = lambda inner, st="": f'<div class="imt-card" style="width:100%;{st}">{inner}</div>'
TXT  = lambda t, c="var(--ink)", s="var(--fs-md)": f'<div style="color:{c};font-size:{s};line-height:1.5">{t}</div>'

# ── 면 나누기 ────────────────────────────────────────────────────
good_surface = (
  '<div style="width:100%;background:var(--bg);padding:var(--sp-4);border-radius:var(--r-in)">'
  + CARD(TXT("<b>삼성전자</b>") + TXT("71,200원 · +2.4%", "var(--sub)", "var(--fs-sm)"))
  + '<div style="height:8px"></div>'
  + CARD(TXT("<b>SK하이닉스</b>") + TXT("184,500원 · −0.8%", "var(--sub)", "var(--fs-sm)"))
  + '</div>')
bad_surface = (
  '<div style="width:100%;background:#fff;padding:var(--sp-4);border-radius:var(--r-in)">'
  + CARD(TXT("<b>삼성전자</b>") + TXT("71,200원 · +2.4%", "var(--sub)", "var(--fs-sm)"), "box-shadow:0 2px 8px rgba(0,0,0,.10)")
  + '<div style="height:8px"></div>'
  + CARD(TXT("<b>SK하이닉스</b>") + TXT("184,500원 · −0.8%", "var(--sub)", "var(--fs-sm)"), "box-shadow:0 2px 8px rgba(0,0,0,.10)")
  + '</div>')

# ── 세 층 ───────────────────────────────────────────────────────
layer_stage = ('<div style="position:relative;width:100%;max-width:260px">'
  '<div style="background:var(--bg);border-radius:var(--r-in);padding:34px 12px 12px;'
  'box-shadow:var(--edge);min-height:180px">'
  + CARD(TXT("표 · 차트 · 본문", "var(--sub)", "var(--fs-sm)"), "min-height:74px;display:grid;place-items:center")
  + '<div style="height:8px"></div>'
  + CARD(TXT("카드", "var(--sub)", "var(--fs-sm)"), "min-height:52px;display:grid;place-items:center")
  + '</div>'
  '<div style="position:absolute;left:8px;right:8px;top:8px;height:34px;border-radius:12px;'
  'background:var(--glass);backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);'
  'border:1px solid var(--glass-line);box-shadow:var(--glass-sh);display:flex;align-items:center;'
  'justify-content:center;font:var(--fw-m) var(--fs-sm) var(--font);color:var(--ink)">상단바</div>'
  '<div style="position:absolute;left:26px;right:26px;bottom:26px;border-radius:12px;'
  'background:var(--card);box-shadow:var(--sh-lift);padding:10px 14px;'
  'font:var(--fw-m) var(--fs-sm) var(--font);color:var(--ink)">저장했습니다</div>'
  '<span class="g-pin g-pin--abs" style="left:-6px;top:14px">2</span>'
  '<span class="g-pin g-pin--abs" style="left:-6px;top:78px">1</span>'
  '<span class="g-pin g-pin--abs" style="left:-6px;bottom:32px">3</span>'
  '</div>')

# ── 간격 ────────────────────────────────────────────────────────
sp_items = [(f'<div style="width:var(--sp-{n});height:26px;background:var(--brand);'
             f'border-radius:3px"></div>', f"--sp-{n}", f"{v}px")
            for n, v in [(1,4),(2,8),(3,12),(4,16),(5,20),(6,24),(8,32),(10,40),(12,48),(16,64)]]

# ── 정렬 ────────────────────────────────────────────────────────
def rows(offsets):
    return ('<div style="width:100%;display:flex;flex-direction:column;gap:8px">' + "".join(
        f'<div style="margin-left:{o}px;background:var(--card);box-shadow:var(--edge);'
        f'border-radius:var(--r-xs);padding:8px 12px;font-size:var(--fs-sm);color:var(--ink2)">{t}</div>'
        for o, t in zip(offsets, ["매수 계획", "매도 계획", "시나리오"])) + '</div>')

PAGE = {
 "slug": "layout", "group": "기초", "kicker": "기초",
 "title": "레이아웃",
 "abstract": "화면을 여는 순간 어디를 봐야 하는지 알게 만드는 일이다. 위치·간격·정렬은 취향이 아니라 위계를 만드는 도구다.",
 "blocks": [

  ("h2", "화면은 세 층이다", "layers"),
  ("p", "가장 먼저 정할 것은 색도 글자도 아니고 <b>층</b>이다. 콘텐츠가 맨 아래에 있고, 컨트롤이 그 위에 떠 있고, 알림이 가장 위에 있다. 이 셋을 같은 평면에 늘어놓으면 아무리 예쁘게 칠해도 화면이 납작해진다."),
  ("raw", anatomy(layer_stage, [
     (1, "콘텐츠 층", "표·차트·본문·카드. 불투명하다. 여기에는 유리를 쓰지 않는다."),
     (2, "컨트롤 층", "상단바·탭바·사이드바. 반투명하게 떠 있고 아래로 콘텐츠가 지나간다. <code>--glass</code>는 여기서만 쓴다."),
     (3, "알림 층", "모달·시트·토스트. 나머지 둘을 덮는다. 한 번에 하나만 띄운다."),
   ], "층을 나누면 스크롤할 때 무엇이 따라오고 무엇이 지나가는지가 저절로 정해진다.")),

  ("h2", "면은 배경 대비로 나눈다", "surface"),
  ("rule", "그림자를 얹기 전에 배경색을 먼저 바꾼다",
   "배경과 카드가 둘 다 흰색이면 그림자를 아무리 진하게 넣어도 경계가 흐릿하다. 배경을 회색조로 한 단 내리면 그림자 없이도 카드가 떠오른다. 그림자는 '떠 있음'을 말할 때만 쓴다."),
  ("raw", cmp2([
     ("do", good_surface, "배경 <code>--bg</code> · 카드 <code>--card</code>"),
     ("no", bad_surface,  "둘 다 흰색 — 그림자로 메우려 한다"),
   ], "오른쪽은 그림자가 더 진한데도 경계가 덜 또렷하다. 대비가 하는 일을 그림자가 대신하지 못한다.")),
  ("raw", spec(["단계", "쓰는 곳", "grouped", "system"], [
     ["1차", "화면 전체 배경", "<code>--bg</code>", "<code>--bg-sys</code>"],
     ["2차", "그 안의 묶음(카드)", "<code>--card</code>", "<code>--bg-sys-2</code>"],
     ["3차", "묶음 안의 강조 면", "<code>--inset</code>", "<code>--bg-sys-3</code>"],
   ], "배경은 3단계까지다. 4단계가 필요하면 위계 설계가 잘못된 것이다. 목록·설정처럼 묶음이 있는 화면은 grouped, 그 외 일반 화면은 system 을 쓰고 <b>한 화면에서 둘을 섞지 않는다.</b>")),

  ("h2", "간격은 4의 배수", "space"),
  ("rule", "6px·10px·14px 를 한 번 허용하면 스무 가지로 불어난다",
   "중간값은 언제나 '이번 한 번만' 으로 들어온다. 그리고 다음 사람은 그걸 근거로 또 하나를 들인다. 눈은 4px 차이를 위계로 읽지 못하므로, 얻는 것 없이 리듬만 잃는다."),
  ("raw", scale(sp_items, "이 열 개 안에서만 고른다. 화면 전체가 같은 눈금 위에 놓인다.")),
  ("rule", "컨트롤 주위 여백은 크기만큼 중요하다",
   "버튼이 아무리 커도 옆에 붙어 있으면 잘못 눌린다. 테두리가 있는 요소 주위에는 12px, 테두리 없이 글자만 있는 요소 주위에는 24px 를 둔다."),
  ("raw", grid(
     '<div style="display:flex;align-items:center;gap:var(--gap-ctl)">'
     '<button class="imt-btn imt-btn--soft">취소</button>'
     '<button class="imt-btn imt-btn--primary">저장</button></div>',
     "8px 눈금 위에 놓인 버튼 두 개. 사이 간격이 <code>--gap-ctl</code>(12px) 이다.")),

  ("h2", "정렬이 곧 조직도다", "align"),
  ("p", "왼쪽 모서리가 맞는 것들은 한 묶음으로 읽힌다. 반대로 한 줄만 어긋나면 눈이 거기서 멈춘다 — 그래서 <b>일부러 어긋나게 하는 것</b>도 도구가 된다. 문제는 의도 없이 어긋난 경우다."),
  ("raw", cmp2([
     ("do", rows([0,0,0]),    "같은 묶음이면 모서리를 맞춘다"),
     ("no", rows([0,14,6]),    "의도 없는 어긋남 — 셋이 남남으로 보인다"),
   ])),

  ("h2", "적응은 중단점이 아니라 격자로", "adapt"),
  ("rule", "미디어 쿼리를 늘리는 대신 격자가 스스로 접히게 한다",
   "<code>repeat(auto-fill, minmax(240px, 1fr))</code> 한 줄이면 폭에 따라 열 수가 저절로 바뀐다. 중단점을 세 개 네 개 늘리면 그만큼 확인할 화면이 늘어나고, 그중 하나는 반드시 잊는다."),
  ("raw", fig(
     '<div class="imt-grid">' + "".join(
       CARD(TXT(f"카드 {i}", "var(--sub)", "var(--fs-sm)"), "min-height:60px;display:grid;place-items:center")
       for i in range(1, 5)) + '</div>',
     "창을 좁히면 4열 → 2열 → 1열로 접힌다. 규칙은 한 줄뿐이다.")),
  ("rule", "글자가 커져도 위계는 유지한다",
   "사용자가 글자 크기를 키우면 본문은 커지되 탭 제목까지 같이 커질 필요는 없다. 전부 같은 비율로 키우면 화면이 깨지고, 정작 읽고 싶었던 본문은 그대로 답답하다."),

  ("h2", "사양", "spec"),
  ("raw", spec(["토큰", "값", "쓰는 곳"], [
     ["<code>--w-content</code>", "720px", "글이 주인 화면 — 한 줄이 길면 눈이 다음 줄을 놓친다"],
     ["<code>--w-wide</code>", "1120px", "표·차트가 있는 대시보드"],
     ["<code>--w-full</code>", "1440px", "최대 폭 — 그 이상은 여백만 늘어난다"],
     ["<code>--gap-ctl</code>", "12px", "테두리 있는 컨트롤 주위"],
     ["<code>--gap-ctl-plain</code>", "24px", "테두리 없는 컨트롤 주위"],
   ])),
 ],
}
