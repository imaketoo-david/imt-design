# -*- coding: utf-8 -*-
from figures import cmp2, spec, fig, ic

def scene(theme):
    d = theme == "dark"
    bg   = "#000000" if d else "#f2f2f7"
    card = "#1c1c1e" if d else "#ffffff"
    ink  = "#f5f5f7" if d else "#1d1d1f"
    sub  = "#98989f" if d else "#6e6e74"
    line = "#38383a" if d else "#dcdce2"
    up   = "#ff5f52" if d else "#e0392e"
    edge = ("0 0 0 1px rgba(255,255,255,.07)" if d else "0 0 0 1px rgba(0,0,0,.045)")
    return (f'<div style="width:100%;background:{bg};border-radius:var(--r-in);padding:var(--sp-4)">'
      f'<div style="background:{card};border-radius:var(--r-in);box-shadow:{edge};padding:var(--sp-4)">'
      f'<div style="font:var(--fw-sb) var(--fs-base) var(--font);color:{ink}">삼성전자</div>'
      f'<div style="font-size:var(--fs-sm);color:{sub};margin-top:2px">10주 · 매수가 68,500</div>'
      f'<div style="margin-top:10px;padding-top:10px;border-top:.5px solid {line};'
      f'font-family:var(--font-num);font-size:var(--fs-lg);color:{up}">71,200 · +2.4%</div>'
      f'</div></div>')

def naive_dark():
    return ('<div style="width:100%;background:#000;border-radius:var(--r-in);padding:var(--sp-4)">'
      '<div style="background:#000;border-radius:var(--r-in);box-shadow:0 4px 14px rgba(0,0,0,.6);'
      'padding:var(--sp-4)">'
      '<div style="font:var(--fw-sb) var(--fs-base) var(--font);color:#fff">삼성전자</div>'
      '<div style="font-size:var(--fs-sm);color:#888;margin-top:2px">10주 · 매수가 68,500</div>'
      '<div style="margin-top:10px;padding-top:10px;border-top:.5px solid #333;'
      'font-family:var(--font-num);font-size:var(--fs-lg);color:#ff0000">71,200 · +2.4%</div>'
      '</div></div>')

PAGE = {
 "slug": "dark-mode", "group": "기초", "kicker": "기초",
 "title": "다크 모드",
 "abstract": "명도를 뒤집는 일이 아니다. 어두운 화면에서 눈이 색을 다르게 받아들이므로, 값을 따로 고른다.",
 "blocks": [

  ("h2", "반전이 아니라 별도로 고른 값이다", "not-invert"),
  ("rule", "배경은 검정이 아니라 올리고, 글자는 순백이 아니라 내린다",
   "<code>#000</code> 위의 순백 글자는 눈부시고, 어두운 배경에서는 같은 채도의 색이 더 튀어 보인다. 그래서 면은 <code>#1c1c1e</code>, 글자는 <code>#f5f5f7</code> 로 양쪽을 안으로 당긴다."),
  ("raw", cmp2([
     ("do", scene("dark"), "면을 올리고 글자를 내린다"),
     ("no", naive_dark(),  "검정 + 순백 + 원색 — 눈이 아프다"),
   ], "오른쪽은 배경과 카드가 둘 다 검정이라 경계도 사라졌다. 라이트에서 배경/카드를 나누던 규칙이 다크에서도 그대로 적용된다.")),

  ("h2", "그림자 대신 테두리", "edge"),
  ("rule", "어두운 배경 위에서는 그림자가 보이지 않는다",
   "라이트에서 <code>--edge</code> 는 검정 4.5% 테두리이고, 다크에서는 <b>흰색 7%</b> 로 바뀐다. 면을 나누는 일은 같지만 수단이 반대다."),

  ("h2", "값 대조", "values"),
  ("raw", spec(["토큰", "라이트", "다크", "왜 다른가"], [
     ["<code>--bg</code>", "#f2f2f7", "#000000", "다크는 진짜 검정이 배경일 때 OLED 에서 가장 편하다"],
     ["<code>--card</code>", "#ffffff", "#1c1c1e", "카드를 <b>올려서</b> 배경과 나눈다 — 라이트와 방향이 반대"],
     ["<code>--inset</code>", "#f5f5f8", "#2c2c2e", "한 단 더 올린다"],
     ["<code>--ink</code>", "#1d1d1f", "#f5f5f7", "순백이 아니다"],
     ["<code>--sub</code>", "#6e6e74", "#98989f", "밝기를 올려 대비를 맞춘다"],
     ["<code>--up</code>", "#e0392e", "#ff5f52", "어두운 배경에서는 밝고 채도가 낮은 빨강이 읽힌다"],
     ["<code>--edge</code>", "검정 4.5%", "흰색 7%", "그림자 → 테두리"],
   ])),

  ("h2", "차트 색은 그대로 쓴다", "chart"),
  ("p", "8슬롯(<code>--c1</code>~<code>--c8</code>)은 <b>라이트와 다크에서 같은 값</b>이다. 두 배경 모두에서 3:1 대비를 통과하도록 고른 조합이라, 모드마다 색이 바뀌면 오히려 같은 데이터가 다른 색으로 보인다."),

  ("h2", "누가 이기는가", "priority"),
  ("raw", spec(["순위", "조건", "구현"], [
     ["1", "사용자가 이 사이트에서 토글로 고른 것", "<code>:root[data-theme]</code>"],
     ["2", "OS 설정", "<code>@media (prefers-color-scheme: dark)</code>"],
     ["3", "기본값", "라이트"],
   ], "토글 선택은 <code>localStorage</code> 에 남긴다. 다만 브라우저가 그것을 비워도 화면이 정상이어야 한다 — 읽기·쓰기를 <code>try/catch</code> 로 감싼다.")),
  ("rule", "앱 전용 테마 설정을 굳이 만들지 않는다",
   "OS 설정을 따르는 것이 기본이다. 토글은 <b>편의</b>이지 필수가 아니고, 토글이 있어도 OS 를 무시하는 기본값을 두지 않는다."),

  ("h2", "확인할 것", "check"),
  ("raw", spec(["□", "확인"], [
     ["1", "배경과 카드가 구분되는가 — 둘 다 검정이 되지 않았는가"],
     ["2", "대비 검사를 <b>다크에서도</b> 돌렸는가"],
     ["3", "이미지·로고에 흰 배경이 박혀 있지 않은가"],
     ["4", "그림자에만 의존한 요소가 사라지지 않았는가"],
     ["5", "차트 격자선이 보이는가 (<code>--grid</code> 는 다크에서 흰색 8%)"],
   ])),
 ],
}
