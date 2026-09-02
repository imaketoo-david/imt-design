# -*- coding: utf-8 -*-
from figures import cmp2, anatomy, spec, fig, ic

def chart(y0, pts, label, bars=False, grid_from=0):
    marks = ("".join(f'<rect x="{8+i*34}" y="{100-v}" width="22" height="{v}" rx="4" fill="var(--c1)"/>'
                     for i, v in enumerate(pts))
             if bars else
             f'<polyline fill="none" stroke="var(--c1)" stroke-width="2" stroke-linecap="round" '
             f'stroke-linejoin="round" points="{" ".join(f"{8+i*34},{100-v}" for i,v in enumerate(pts))}"/>')
    return ('<svg viewBox="0 0 250 118" style="width:100%;max-width:250px">'
      + "".join(f'<line x1="0" y1="{y}" x2="250" y2="{y}" stroke="var(--grid)" stroke-width="1"/>'
                for y in (20,45,70,95))
      + marks
      + f'<line x1="0" y1="100" x2="250" y2="100" stroke="var(--line)" stroke-width="1"/>'
      + f'<text x="4" y="114" font-size="9" fill="var(--sub)" font-family="var(--font-num)">{y0}</text>'
      + '</svg>')

bar0  = chart("0",  [42,50,46,58,64,70,76], "", bars=True)
barX  = chart("40", [12,20,16,28,34,40,46], "", bars=True)

legend = ('<div style="display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:8px">'
  + "".join(f'<span style="display:inline-flex;align-items:center;gap:5px;font-size:var(--fs-sm);'
            f'color:var(--sub)"><span style="width:12px;height:2.5px;border-radius:2px;'
            f'background:var(--c{i})"></span>{t}</span>' for i, t in [(1,"삼성전자"),(2,"SK하이닉스")]) + '</div>')

multi = ('<svg viewBox="0 0 250 110" style="width:100%;max-width:250px">'
  + "".join(f'<line x1="0" y1="{y}" x2="250" y2="{y}" stroke="var(--grid)" stroke-width="1"/>' for y in (18,44,70,96))
  + '<polyline fill="none" stroke="var(--c1)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" points="8,86 48,72 88,76 128,54 168,44 208,30 242,22"/>'
  + '<polyline fill="none" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4" points="8,96 48,90 88,80 128,82 168,68 208,64 242,52"/>'
  + '</svg>')

def table(align_right):
    a = "right" if align_right else "left"
    f = "var(--font-num)" if align_right else "var(--font)"
    rows = [("삼성전자","71,200","+2.4%"),("SK하이닉스","184,500","−0.8%"),("현대차","238,000","+11.2%")]
    return ('<table style="width:100%;border-collapse:collapse;font-size:var(--fs-sm)">'
      '<thead><tr>'
      '<th style="text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);color:var(--ink)">종목</th>'
      f'<th style="text-align:{a};padding:6px 8px;border-bottom:1px solid var(--line);color:var(--ink)">현재가</th>'
      f'<th style="text-align:{a};padding:6px 8px;border-bottom:1px solid var(--line);color:var(--ink)">등락</th>'
      '</tr></thead><tbody>' + "".join(
      f'<tr><td style="padding:6px 8px;color:var(--ink2)">{n}</td>'
      f'<td style="text-align:{a};padding:6px 8px;font-family:{f};color:var(--ink2)">{p}</td>'
      f'<td style="text-align:{a};padding:6px 8px;font-family:{f};'
      f'color:var({"--up" if c.startswith("+") else "--down"})">{c}</td></tr>' for n,p,c in rows)
      + '</tbody></table>')

PAGE = {
 "slug": "data", "group": "패턴", "kicker": "패턴",
 "title": "데이터 표현",
 "abstract": "차트는 예뻐지려고 그리는 것이 아니라 판단하게 하려고 그린다. 무엇을 말할지 정하지 못했으면 아직 표로 두는 편이 낫다.",
 "blocks": [

  ("h2", "차트를 그릴지 표로 둘지", "which"),
  ("rule", "말할 것이 없으면 표로 둔다",
   "차트는 <b>추세·비교·분포</b> 중 하나를 말할 때 쓴다. 숫자 세 개는 표가 더 정확하고 더 빨리 읽힌다."),
  ("raw", spec(["말하려는 것", "형태"], [
     ["시간에 따른 변화", "선 — 변화의 모양이 값이다"],
     ["항목 사이 크기 비교", "막대 — 길이가 값이다"],
     ["전체 중 비중", "누적 막대. 파이는 3조각 이하에서만"],
     ["두 값의 관계", "산점"],
     ["정확한 값 확인", "표"],
     ["값 하나", "큰 숫자 하나. 차트로 만들지 않는다"],
   ])),

  ("h2", "축의 하한은 유형이 정한다", "axis"),
  ("rule", "막대는 반드시 0에서 시작한다",
   "막대는 <b>길이</b>가 값이다. 0에서 시작하지 않으면 길이 비율이 실제 값 비율과 달라진다. 선은 <b>변화</b>가 값이므로 0에서 시작하지 않아도 된다."),
  ("raw", cmp2([
     ("do", bar0, "0 에서 시작 — 길이 비율이 값 비율과 같다"),
     ("no", barX, "40 에서 시작 — 차이가 세 배로 부풀어 보인다"),
   ], "같은 데이터다. 오른쪽은 거짓말을 하고 있다.")),
  ("rule", "눈금은 익숙한 간격으로",
   "0 · 25 · 50 · 75 · 100. 0 · 33 · 66 · 99 는 계산이 맞아도 읽는 사람이 암산을 해야 한다."),
  ("rule", "격자선은 데이터보다 진하면 안 된다",
   "<code>--grid</code> 는 라이트에서 검정 6%다. 눈금은 값을 <b>가늠하게</b> 돕는 것이지 그 자체가 정보가 아니다."),

  ("h2", "색만으로 시리즈를 구분하지 않는다", "series"),
  ("rule", "시리즈가 둘 이상이면 범례를 항상 넣는다",
   "그리고 색 외에 <b>선 모양</b>이나 <b>마크</b>로도 구분되게 한다. 흑백 인쇄와 색각 이상에서 동시에 해결된다."),
  ("raw", fig(multi + legend, "실선과 파선으로도 나뉜다. 색은 빠르게 찾게 돕는 보조 수단이다.")),
  ("rule", "8슬롯을 넘기지 않는다",
   "9번째 시리즈는 색을 재사용하지 말고 '기타' 로 접는다. 애초에 여덟 개를 넘는 시리즈는 사람이 한눈에 읽을 수 없다."),

  ("h2", "마크 규격", "marks"),
  ("raw", spec(["요소", "값", "이유"], [
     ["선 굵기", "2px", "1px 은 고해상도에서 사라지고 3px 은 데이터를 뭉갠다"],
     ["점 반지름", "4px", "마지막 값·변곡점에만 찍는다"],
     ["막대 라운드", "4px (<code>--r-xs</code> 보다 작게)", "막대는 값이므로 모서리가 길이를 먹으면 안 된다"],
     ["막대 사이 간격", "막대 폭의 40% 안팎", "붙으면 히스토그램으로 읽힌다"],
     ["색면 사이 간격", "1~2px 배경색 선", "맞닿으면 경계가 사라진다"],
   ])),

  ("h2", "차트에 한 문장을 붙인다", "caption"),
  ("rule", "'3분기부터 상승 전환' 한 줄이 이해 속도를 바꾼다",
   "그리고 스크린리더 사용자에게는 <b>그 문장이 차트 전부</b>다. 축 눈금은 보조기술에서 숨기고, 요약 문장을 대체 텍스트로 준다."),

  ("h2", "표", "table"),
  ("rule", "숫자는 오른쪽 정렬 · 등폭 폰트",
   "자릿수가 세로로 맞아야 위아래를 비교할 수 있다. 가변폭 폰트에서는 1과 8의 너비가 달라 줄이 어긋난다."),
  ("raw", cmp2([
     ("do", table(True),  "오른쪽 정렬 · <code>--font-num</code>"),
     ("no", table(False), "왼쪽 정렬 · 가변폭 — 자릿수가 어긋난다"),
   ])),
  ("raw", spec(["규칙", "이유"], [
     ["열 제목을 축약하지 않는다", "'전일比' 보다 '전일 대비' 가 한 번에 읽힌다"],
     ["행이 20개를 넘으면 검색이나 필터를 붙인다", "스크롤로 찾게 하지 않는다"],
     ["정렬 가능한 열은 눌러서 정렬되게", "머리를 누르는 것은 이미 학습된 동작이다"],
     ["빈 칸은 <code>—</code> 로 채운다", "빈칸이 '0' 인지 '없음' 인지 구분되지 않는다"],
   ])),

  ("h2", "상호작용은 덤이다", "interaction"),
  ("rule", "호버해야만 보이는 정보에 핵심을 두지 않는다",
   "모바일에는 호버가 없고 키보드 사용자에게도 없다. 툴팁은 <b>더 자세한 값</b>을 위한 것이지 <b>유일한 값</b>을 위한 것이 아니다."),
 ],
}
