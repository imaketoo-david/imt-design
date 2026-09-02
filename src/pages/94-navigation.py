# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, spec, fig, ic

topbar = ('<div style="width:100%;max-width:290px;border-radius:var(--r);overflow:hidden;'
  'box-shadow:var(--edge);background:var(--bg)">'
  '<div style="display:flex;align-items:center;gap:10px;padding:10px 14px;background:var(--glass);'
  'backdrop-filter:var(--glass-blur);-webkit-backdrop-filter:var(--glass-blur);'
  'border-bottom:1px solid var(--glass-line)">'
  + ic("arrow-left") if False else '')

def bar(inner, glass=True):
    g = ('background:var(--glass);backdrop-filter:var(--glass-blur);'
         '-webkit-backdrop-filter:var(--glass-blur);border-bottom:1px solid var(--glass-line)'
         if glass else 'background:var(--card);border-bottom:1px solid var(--line)')
    return (f'<div style="width:100%;max-width:290px;border-radius:var(--r);overflow:hidden;'
      f'box-shadow:var(--edge);background:var(--bg)">'
      f'<div style="display:flex;align-items:center;gap:10px;padding:10px 14px;{g}">{inner}</div>'
      f'<div style="padding:14px;font-size:var(--fs-md);color:var(--sub);line-height:1.6">'
      f'표·차트·본문이 이 아래로 지나간다</div></div>')

top_good = bar('<span style="font:var(--fw-sb) var(--fs-base) var(--font);color:var(--ink)">보유</span>'
  '<span style="margin-left:auto;display:flex;gap:12px;color:var(--ink2)">'
  + ic("search") + ic("more") + '</span>')
top_bad = bar('<span style="font:var(--fw-sb) var(--fs-base) var(--font);color:var(--ink)">보유</span>'
  '<span style="margin-left:auto;display:flex;gap:9px;color:var(--ink2)">'
  + ic("search") + ic("filter") + ic("edit") + ic("star") + ic("bell") + ic("more") + '</span>')

tabbar = ('<div style="width:100%;max-width:290px;border-radius:var(--r);overflow:hidden;'
  'box-shadow:var(--edge);background:var(--bg)">'
  '<div style="padding:16px 14px;font-size:var(--fs-md);color:var(--sub)">콘텐츠</div>'
  '<div style="display:flex;background:var(--glass);backdrop-filter:var(--glass-blur);'
  '-webkit-backdrop-filter:var(--glass-blur);border-top:1px solid var(--glass-line)">'
  + "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;'
            f'padding:8px 0;color:var({"--brand" if i==0 else "--sub"})">{ic(n)}'
            f'<span style="font-size:var(--fs-tag)">{t}</span></div>'
            for i, (n, t) in enumerate([("wallet","보유"),("trend-up","시장"),
                                        ("doc","계획"),("person","내정보")])) + '</div></div>')

PAGE = {
 "slug": "navigation", "group": "컴포넌트", "kicker": "컴포넌트",
 "title": "내비게이션",
 "abstract": "지금 어디에 있고 어디로 갈 수 있는지를 항상 보이게 한다. 길을 잃는 화면은 대개 여기가 비어 있다.",
 "blocks": [

  ("h2", "내비게이션은 컨트롤 층이다", "layer"),
  ("p", "상단바·탭바·사이드바는 콘텐츠와 <b>같은 평면에 있지 않다</b>. 콘텐츠 위에 떠 있고 그 아래로 콘텐츠가 지나간다. <code>--glass</code> 를 쓰는 자리는 여기뿐이다."),
  ("raw", fig(top_good, "경계는 선이 아니라 재질로 만든다. 아래로 지나가는 콘텐츠가 살짝 비친다.")),

  ("h2", "상단바", "top"),
  ("rule", "제목 · 뒤로 · 주요 동작 하나. 그 이상은 넘친다",
   "아이콘을 계속 더하면 각각이 무엇인지 알 수 없게 되고, 결국 전부 눌러 보게 된다. 넘치는 것은 <b>더보기</b>로 접는다."),
  ("raw", cmp2([
     ("do", top_good, "제목 + 검색 + 더보기"),
     ("no", top_bad,  "아이콘 여섯 — 무엇이 중요한지 없다"),
   ])),
  ("raw", spec(["규칙", "내용"], [
     ["제목은 지금 화면을 말한다", "앱 이름을 제목으로 쓰지 않는다"],
     ["뒤로 버튼은 왼쪽 끝", "표준 위치를 옮기지 않는다"],
     ["아이콘에는 <code>aria-label</code>", "없으면 스크린리더에게 '버튼' 으로만 읽힌다"],
     ["스크롤해도 사라지지 않는다", "숨기려면 <b>내려갈 때만</b> 숨기고 올릴 때 즉시 되돌린다"],
   ])),

  ("h2", "탭바", "tab"),
  ("rule", "탭바는 이동이지 동작이 아니다",
   "'추가' 같은 동작을 탭에 넣지 않는다. 탭은 <b>장소</b>이고, 눌렀을 때 다른 장소로 가야 한다."),
  ("raw", fig(tabbar, "선택된 탭은 색과 <b>채움</b>으로 구분한다. 색만으로는 색각 이상에서 구분되지 않는다.")),
  ("raw", spec(["규칙", "이유"], [
     ["3~5개", "둘이면 세그먼트가 낫고, 여섯이면 들어갈 자리가 없다"],
     ["라벨을 항상 보인다", "아이콘만으로는 뜻이 갈린다"],
     ["비활성화하거나 감추지 않는다", "장소가 사라지면 앱 구조가 바뀐 것처럼 보인다"],
     ["어느 탭에서든 같은 자리", "위치가 바뀌면 근육 기억이 무너진다"],
   ])),

  ("h2", "사이드바", "side"),
  ("raw", spec(["규칙", "내용"], [
     ["위계는 두 단까지", "세 단째부터는 접어야 보이고, 접히면 안 찾는다"],
     ["현재 위치를 항상 강조", "면색으로. 글자 굵기만으로는 약하다"],
     ["접을 수 있게", "좁은 화면에서는 기본으로 접힌다"],
     ["아이콘은 익숙한 것만", "사이드바 아이콘은 라벨의 보조다"],
   ])),

  ("h2", "지금 어디인지 말한다", "current"),
  ("rule", "선택 상태를 색만으로 표시하지 않는다",
   "면색·굵기·채움 아이콘 중 <b>둘 이상</b>을 함께 쓴다. <code>aria-current=\"page\"</code> 도 같이 단다."),

  ("h2", "돌아왔을 때", "restore"),
  ("rule", "스크롤 위치·선택·필터는 그대로여야 한다",
   "목록에서 상세로 들어갔다 나왔는데 맨 위로 올라가 있으면, 사용자는 보던 자리를 다시 찾아야 한다. 이게 '맥락을 보존한다' 의 가장 흔한 실패다."),
 ],
}
