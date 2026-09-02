# -*- coding: utf-8 -*-
"""기술 절에서 건너온 것 — HIG Technologies 29쪽을 전수로 읽고 남은 것.

애플 프레임워크(HealthKit·CarPlay·Wallet…)를 쓰지 않아도, 그 문서 안에는
'화면을 어떻게 만들라'는 지침이 섞여 있다. 그것만 골라낸 쪽이다.
출처는 HIG-COVERAGE.md 에 쪽 단위로 적어두었다.
"""
from figures import cmp2, spec, fig, ic

# 신뢰도 — 숫자 대신 말로
CONF_BAD = ('<div style="width:100%;display:flex;flex-direction:column;gap:7px">'
  + "".join(f'<div style="display:flex;justify-content:space-between;font-size:var(--fs-md);'
            f'color:var(--ink2)"><span>{n}</span>'
            f'<span style="font-family:var(--font-num);color:var(--sub)">{v}</span></div>'
            for n, v in [("다음 분기 매출", "0.7213"), ("이탈 위험", "0.5104"),
                         ("재구매 확률", "0.3388")]) + '</div>')
CONF_OK = ('<div style="width:100%;display:flex;flex-direction:column;gap:7px">'
  + "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;'
            f'font-size:var(--fs-md);color:var(--ink2)"><span>{n}</span>'
            f'<span class="imt-badge" style="color:var({c});background:var({b})">{t}</span></div>'
            for n, t, c, b in [("다음 분기 매출", "가능성 높음", "--ok", "--green-soft"),
                               ("이탈 위험", "가능성 있음", "--warn", "--amber-soft")])
  + '<div style="display:flex;justify-content:space-between;font-size:var(--fs-md);'
    'color:var(--flat)"><span>재구매 확률</span><span>—</span></div></div>')

# 상호작용 색 분리
HIT_BAD = ('<div style="width:100%;display:flex;flex-direction:column;gap:8px;font-size:var(--fs-md)">'
  '<div style="color:var(--brand)">전체 기간</div>'
  '<div style="color:var(--brand)">2026년 3분기 실적 요약</div>'
  '<div style="color:var(--brand)">자세히 보기</div></div>')
HIT_OK = ('<div style="width:100%;display:flex;flex-direction:column;gap:8px;font-size:var(--fs-md)">'
  '<div style="color:var(--sub)">전체 기간</div>'
  '<div style="color:var(--ink)">2026년 3분기 실적 요약</div>'
  '<div style="color:var(--brand)">자세히 보기</div></div>')

# 유휴 디밍
def _row(op, w):
    return (f'<div style="display:flex;align-items:center;gap:9px;opacity:{op}">'
            f'<div style="width:7px;height:7px;border-radius:99px;background:var(--c1)"></div>'
            f'<div style="height:8px;width:{w}px;border-radius:4px;background:var(--fill2)"></div></div>')
DIM_OK = ('<div style="width:100%;display:flex;flex-direction:column;gap:9px">'
  '<div style="font:var(--fw-sb) var(--fs-lg) var(--font-num);color:var(--ink)">₩ 4,182만</div>'
  + _row(.62, 96) + _row(.38, 132) + _row(.38, 78)
  + '<button class="imt-btn imt-btn--sm" disabled style="margin-top:6px;opacity:.5">새로고침</button></div>')
DIM_BAD = ('<div style="width:100%;display:flex;flex-direction:column;gap:9px">'
  '<div style="font:var(--fw-sb) var(--fs-lg) var(--font-num);color:var(--ink)">₩ 4,182만</div>'
  '<div style="font-size:var(--fs-sm);color:var(--flat)">— 나머지 줄이 사라졌다 —</div></div>')

# 차트 각주
NOTE = ('<div style="width:100%;max-width:300px;background:var(--card);border-radius:var(--r);'
  'box-shadow:var(--edge);padding:var(--sp-4)">'
  '<div style="display:flex;gap:5px;align-items:flex-end;height:56px">'
  + "".join(f'<div style="flex:1;height:{h}%;border-radius:3px 3px 0 0;background:var(--c1);'
            f'opacity:{o}"></div>' for h, o in [(42,.45),(66,.6),(54,.72),(88,.86),(100,1)])
  + '</div><div style="margin-top:10px;padding:var(--note-pad-y) var(--note-pad-x) 0;'
    'border-top:var(--hairline) solid var(--line-soft);font-size:var(--fs-xs);color:var(--flat)">'
    '출처 통신사 공시 · 2026-08-31 기준</div></div>')

PAGE = {
 "slug": "technologies", "group": "패턴", "kicker": "패턴",
 "title": "기술 절에서 건너온 것",
 "abstract": "애플 기기 기능을 하나도 쓰지 않아도, 그 문서들이 말하는 화면 규칙은 웹에 그대로 선다. 29쪽을 읽고 남은 것만 모았다.",
 "blocks": [

  ("h2", "추정값은 숫자로 말하지 않는다", "confidence"),
  ("rule", "0.7213 은 판단에 아무 도움이 되지 않는다",
   "확신의 정도는 <b>말</b>로 바꿔 보여준다. 그리고 확신이 기준 아래면 값을 아예 그리지 않는다 — "
   "틀린 값을 흐리게 보여주는 것보다 없는 편이 낫다. 다만 사람들이 통계를 기대하는 자리"
   "(수익률·표본 지표)에서는 원래 수치를 그대로 준다."),
  ("raw", cmp2([
     ("do", CONF_OK, "말로 바꾸고, 기준 아래는 비운다"),
     ("no", CONF_BAD, "소수점 넷째 자리까지 — 무엇을 하라는 뜻인지 알 수 없다"),
   ], "토큰 <code>--conf-hi</code>·<code>--conf-mid</code>·<code>--conf-lo</code>, "
      "잘라내는 기준은 <code>--conf-cut</code> = 0.55.")),
  ("rule", "왜 그렇게 봤는지는 사실로만 적는다",
   "&ldquo;최근 3개월 거래 기준&rdquo; 은 되고, &ldquo;이런 걸 좋아하시니까&rdquo; 는 안 된다. "
   "취향·감정을 단정하면 틀렸을 때 되돌릴 수 없다."),

  ("h2", "누를 수 있는 색과 그냥 색", "hit"),
  ("rule", "같은 색이면 어디를 누를지 알 수 없다",
   "링크 색을 제목이나 라벨에 쓰지 않는다. <b>브랜드색은 누를 수 있는 것에만</b> 쓴다 — "
   "이 한 줄만 지켜도 화면이 읽힌다."),
  ("raw", cmp2([
     ("do", HIT_OK, "누를 수 있는 것 하나만 브랜드색"),
     ("no", HIT_BAD, "셋 다 브랜드색 — 전부 링크처럼 보인다"),
   ])),

  ("h2", "쉬는 화면", "idle"),
  ("rule", "비활성은 지우는 것이 아니라 낮추는 것이다",
   "상시 띄워두는 대시보드가 유휴로 들어갈 때 요소를 없애면 레이아웃이 흔들리고 고장으로 읽힌다. "
   "자리는 그대로 두고 <b>흐리게</b> 만든다. 버튼도 없애지 말고 사용 불가 모양으로 바꾼다."),
  ("raw", cmp2([
     ("do", DIM_OK, "핵심만 남기고 나머지를 낮춘다 — 자리는 그대로"),
     ("no", DIM_BAD, "안 쓰는 것을 지웠다 — 돌아올 때 화면이 튄다"),
   ], "보조는 <code>--dim-2</code> = .62, 넓은 색면·이미지는 <code>--dim-3</code> = .38.")),
  ("rule", "쉬는 동안에는 드물게, 그리고 조용히 갱신한다",
   "시야 가장자리에 있는 화면의 움직임은 유난히 거슬린다. 값이 실제로 바뀔 때만 갱신하고, "
   "돌던 것은 뚝 끊지 말고 하던 동작을 마치고 멈춘다."),

  ("h2", "차트에 붙는 것", "chart"),
  ("rule", "같은 색의 밝기 차이로 다른 뜻을 나누지 않는다",
   "계열 구분은 <b>색상</b>으로 한다. 명도만 다른 두 색은 인쇄·저조도·색각 차이에서 같은 색이 된다. "
   "그리고 색은 언제나 보조 단서다 — 색을 못 봐도 읽히게 라벨이나 모양을 함께 둔다."),
  ("rule", "단위는 축에 한 번만 적는다",
   "값마다 &ldquo;BPM&rdquo; 을 붙이면 눈이 그것만 읽는다. 축 라벨에 한 번 적고 값에서 뺀다. "
   "시간축은 초·분·시·일·주·월·년 중 무엇인지 반드시 드러낸다."),
  ("raw", fig(NOTE, "각주는 위 <code>--note-pad-y</code> 10px · 좌우 <code>--note-pad-x</code> 7px. "
     "차트가 <code>--note-min-w</code> 200 × <code>--note-min-h</code> 100 보다 작으면 각주를 뺀다.")),
  ("rule", "그림에 글자를 굽지 않는다",
   "이미지 안에 박힌 글자는 읽히지도, 검색되지도, 확대되지도 않는다. 차트를 PNG로 굽는 대신 "
   "글자는 글자로 그린다."),
  ("raw", spec(["표시 크기", "보여줄 것"], [
     ["작음 (요약 카드)", "큰 구획과 값 하나. 눈금·범례·개별 점은 뺀다"],
     ["보통", "축 눈금 · 범례 · 겹치는 점은 묶어서"],
     ["큼 (상세)", "개별 점 · 라벨 · 보조 눈금까지"],
   ], "한꺼번에 다 보여주면 어수선하다. 커질수록 하나씩 더한다.")),

  ("h2", "버튼의 세로 리듬", "button"),
  ("rule", "글자 크기는 버튼 높이의 43% 다",
   "뒤집으면 버튼 높이 = 글자 크기 × <b>2.33</b>. 지금까지 감으로 잡던 값에 근거가 생겼다. "
   "글자 있는 버튼은 최소 140px 폭, 글자와 오른쪽 끝 사이는 폭의 8% 이상 띄운다."),
  ("raw", spec(["글자", "버튼 높이", "쓰는 곳"], [
     ["13px", "30px", "표 안 · 도구 막대"],
     ["15px", "35px", "일반 폼"],
     ["17px", "40px", "주 동작"],
   ], "<code>--btn-ratio</code> = 2.33 으로 계산한 값. 손끝으로 누르는 자리는 "
      "여기에 관계없이 <code>--tap</code> 44px 를 지킨다 — 보이는 크기가 아니라 닿는 영역이다.")),
  ("rule", "마크와 배지 둘레는 자기 높이의 1/10 을 비운다",
   "로고·배지·브랜드 아이콘 주위에 다른 것이 붙지 않게 한다. <code>--clear</code> = .1em."),

  ("h2", "화면 폭이 바뀔 때", "responsive"),
  ("rule", "손끝 기준 크기를 포인터 화면에 그대로 쓰지 않는다",
   "같은 본문이 태블릿 17px 이면 데스크톱은 13px 다 — <b>77%</b>. 손끝에 맞춰 키운 것을 "
   "마우스 화면까지 끌고 가면 헐렁해 보인다."),
  ("rule", "아래·양옆 가장자리에 붙인 버튼은 위로 올린다",
   "화면 끝에 둔 이유는 엄지가 닿기 때문이다. 마우스에는 그 이유가 없다. 넓은 화면에서는 "
   "위쪽 도구 막대로 옮긴다 — 데스크톱은 중요한 것이 위에 있다."),

  ("h2", "읽어주는 사람", "a11y"),
  ("rule", "차트는 세 가지를 갖춰야 접근 가능하다",
   "① 무엇을 보여주는지 <b>한 문장 요약</b>, ② 마우스로만 되는 조작은 키보드로도 되게, "
   "③ 장식은 접근성 트리에서 뺀다. 이 셋이 없으면 차트는 그냥 빈 그림이다."),
  ("raw", spec(["갖출 것", "어떻게"], [
     ["요약 한 줄", "<code>&lt;figcaption&gt;</code> 또는 aria-label 에 &ldquo;최근 5개월 가입자 추이&rdquo;"],
     ["키보드", "화살표로 점 이동 · Enter 로 상세 · Esc 로 닫기"],
     ["장식 제외", "격자선·그림자·꾸밈 도형은 <code>aria-hidden</code>"],
   ])),
  ("rule", "값과 라벨은 한 덩어리로 묶는다",
   "묶지 않으면 값들을 죽 읽고 나서 라벨들을 읽는다. 짝이 맞지 않아 아무것도 알 수 없다. "
   "지표와 이름, 차트와 범례를 각각 하나의 그룹으로 만든다."),
  ("rule", "쪽마다 제목이 다르고, 그 제목이 첫 정보다",
   "화면에 들어서면 제목이 가장 먼저 읽힌다. 모든 쪽이 &ldquo;대시보드&rdquo; 면 어디에 왔는지 알 수 없다."),

  ("h2", "글자 수", "limits"),
  ("rule", "잘릴 것을 알고 쓴다",
   "길게 쓰면 시스템이 자른다. 자를 자리를 우리가 고르는 편이 낫다."),
  ("raw", spec(["자리", "상한"], [
     ["카드 제목", "30자 · 2줄"],
     ["카드 설명", "56자 · 2줄"],
     ["오류 메시지", "128자"],
     ["차트 마커 안 글자", "2~3자"],
   ], "제목은 제목형, 설명은 문장형으로 통일한다. "
      "이미지가 없을 때 나올 <b>자리표시자</b>를 반드시 함께 만든다 — 빈 칸이 나오면 고장으로 보인다.")),
 ],
}
