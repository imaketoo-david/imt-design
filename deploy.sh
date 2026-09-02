#!/usr/bin/env bash
# IMT Design System 배포
#   1) 대비 검증  2) CSS 버전 스탬프(캐시 우회)  3) 커밋·푸시  4) 맥미니 전송  5) 라이브 확인
# 사용: ./deploy.sh ["커밋 메시지"]
set -euo pipefail
cd "$(dirname "$0")"

HOST="${IMT_HOST:-mini-ts}"
DEST="/Users/songsmac-mini/Documents/Project/imt-design/"
SITE="https://design.imaketoo.com"

echo "▸ 1. 대비 검증"
python3 check_contrast.py | tail -2

python3 check_tokens.py || exit 1
python3 check_rules.py  || exit 1

echo "▸ 2. 가이드 빌드 · CSS 버전 스탬프"
# sed 를 안 쓴다: macOS 의 -i 는 빈 인자를 요구하고 GNU 는 그걸 파일명으로 읽는다.
# 두 곳 다 도는 한 줄이 없어서, 이미 쓰고 있는 python3 에 맡긴다.
# (stock-sim/build.sh 가 같은 이유로 같은 선택을 했다)
V="$(date +%Y%m%d-%H%M)"
IMT_V="$V" ./build.sh
V="$V" python3 - <<'PYX'
"""모든 HTML 의 모든 CSS 링크에 버전을 찍는다 (L-0.5).
   하나라도 빠뜨리면 그 파일만 CDN 캐시에 얼어붙는다 — 실제로 site.css 가 그랬다."""
import os, re, glob
v = os.environ["V"]
files = ["index.html", "resources.html", "language.html", "index-full.html"] \
        + sorted(glob.glob("guide/*.html"))
n = 0
for f in files:
    if not os.path.exists(f): continue
    s = open(f, encoding="utf-8").read()
    s2 = re.sub(r'href="((?:\.\./)?)(tokens|components|patterns|site|guide)\.css(?:\?v=[^"]*)?"',
                lambda m: f'href="{m.group(1)}{m.group(2)}.css?v={v}"', s)
    # 다른 사이트로 나가는 링크에도 버전을 붙인다.
    # 서버가 Cache-Control 을 안 내리면 브라우저는 같은 URL 을 재검증 없이 캐시에서 준다 —
    # 2026-09-02 에 아이콘 카탈로그가 배포 뒤에도 하루 종일 옛 화면으로 보였다.
    s2 = re.sub(r'https://icons\.imaketoo\.com(?:/catalog\.html)?(?:\?v=[^"\']*)?(?=["\'])',
                f'https://icons.imaketoo.com/catalog.html?v={v}', s2)
    if s2 != s:
        open(f, "w", encoding="utf-8").write(s2); n += 1
print(f"  CSS 버전 스탬프 {n}개 파일")
PYX
echo "  v=${V}"

echo "▸ 3. 커밋·푸시"
if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -q -m "${1:-배포 $(date '+%Y-%m-%d %H:%M')}"
fi
git push -q origin main 2>/dev/null || echo "  (푸시 건너뜀 — 인증 없음)"
echo "  $(git log --oneline -1)"

echo "▸ 4. 맥미니 전송 (${HOST})"
rsync -a --delete \
  --exclude '.git' --exclude '*.bak_v1_*' --exclude '__pycache__' --exclude 'deploy.sh' \
  ./ "${HOST}:${DEST}"

echo "▸ 5. 라이브 확인"
B="$(date +%s)"
printf "  language.html  -> %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "${SITE}/language.html?b=${B}")"
printf "  index.html     -> %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "${SITE}/index.html?b=${B}")"
printf "  가이드 쪽수     -> %s\n" "$(ls guide/*.html | wc -l | tr -d ' ')"
printf "  guide/layout    -> %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "${SITE}/guide/layout.html?b=${B}")"
printf "  CSS 버전 일치   -> %s\n" "$(curl -s "${SITE}/language.html?b=${B}" | grep -c "components.css?v=${V}")"
printf "  prefers-contrast-> %s\n" "$(curl -s "${SITE}/tokens.css?v=${V}" | grep -c 'prefers-contrast' || true)"
echo "완료."
