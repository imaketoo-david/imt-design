# IMT Design System v1

"고요한 정밀" 을 말이 아니라 **값**으로 고정한다. imaketoo 의 모든 사이트가 이 파일을 기준으로 만들어진다.

**레퍼런스: https://design.imaketoo.com**

## 왜 만들었나
5개 사이트의 토큰을 조사하니 이름도 값도 갈라져 있었다.

| | 배경 | 본문 | 보조 | 테두리 |
|---|---|---|---|---|
| sim / marketing | `#f2f2f7` | `--ink` | `--sub` | `--line #dcdce2` |
| plan | `#fbfbfd` | `--fg` | `--muted` | `--border #d2d2d7` |
| speak | — | `--label` | `--label2` | `--sep` |
| chess | 토큰 없음 | | | |

회색 3종, 파랑 2종, 이름 3세트. 세션마다 "고요한 정밀" 을 말로 전달한 결과다.

## 구성
```
tokens.css       색·타이포·간격·라운드·그림자·모션·레이어  ← 단일 진실
components.css   버튼·카드·세그먼트·칩·배지·목록·표·입력·모달·토스트
patterns.css     페이지 셸·대시보드 그리드·통계 타일·차트 프레임·카드뉴스 캔버스
index.html       레퍼런스 사이트 (스와치를 런타임에 읽어 그림 → 문서·코드 불일치 불가능)
```

## 원칙 여섯
1. **면은 그림자가 아니라 배경 대비로 나눈다** — 배경 회색조, 카드 순백
2. **라운드는 하나만** (`--r` 16px). 예외 셋: 세그먼트 안쪽 · 배지 · 시트
3. **글자 크기는 정해진 9단계만** — 중간값 금지
4. **간격은 4의 배수** — 6·10·14px 금지
5. **큰 글자일수록 자간을 좁힌다** — 34px에 −.024em, 13px에 −.008em
6. **색만으로 뜻을 전하지 않는다** — 상태·등락은 아이콘·라벨과 함께

## 차트 팔레트
8슬롯 고정 순서, 순환 금지. 명도대비·색각(CVD)·채도 검사를 **라이트/다크 양쪽에서 전 항목 통과**.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| `#2C6BED` | `#D9631F` | `#159B90` | `#B8811F` | `#C43A80` | `#0F8FC4` | `#7F55D4` | `#1F8A48` |

금지: 이중 y축 · 색 순환 · 순위로 색 배정 · 무지개 그라디언트

## 가져다 쓰기
```html
<link rel="stylesheet" href="https://design.imaketoo.com/tokens.css">
<link rel="stylesheet" href="https://design.imaketoo.com/components.css">
<link rel="stylesheet" href="https://design.imaketoo.com/patterns.css">
```
아이콘은 [IMT Icons](/icons/catalog.html) 334종. 2026-09-03 에 `design.imaketoo.com/icons/` 로 합쳤다 — 같은 도메인이라 `<use>` 가 그냥 되고, 옛 `icons.imaketoo.com` 은 301 로 넘어온다.

**사이트가 덮어쓸 수 있는 건 `--brand` 세 개뿐이다.**
```css
:root{ --brand:#1E37F6; --brand-hover:#4459FF; --brand-soft:rgba(30,55,246,.10) }
```
중립색·간격·타이포·라운드를 덮어쓰는 순간 다시 갈라진다.

## 기존 사이트 이관
`tokens.css` 는 기존 이름을 전부 별칭으로 갖고 있다 (`--fg`→`--ink`, `--muted`→`--sub`, `--border`→`--line`, `--label`→`--ink`, `--sep`→`--line`).
→ **link 세 줄만 넣으면 기존 CSS 를 고치지 않아도 동작한다.**
