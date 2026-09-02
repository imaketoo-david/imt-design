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

echo "▸ 2. CSS 버전 스탬프"
V="$(date +%Y%m%d-%H%M)"
for f in index.html language.html; do
  /usr/bin/sed -i '' -E "s#href=\"(tokens|components|patterns)\.css(\?v=[^\"]*)?\"#href=\"\1.css?v=${V}\"#g" "$f"
done
echo "  v=${V}"

echo "▸ 3. 커밋·푸시"
if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -q -m "${1:-배포 $(date '+%Y-%m-%d %H:%M')}"
fi
git push -q origin main
echo "  $(git log --oneline -1)"

echo "▸ 4. 맥미니 전송 (${HOST})"
rsync -a --delete \
  --exclude '.git' --exclude '*.bak_v1_*' --exclude '__pycache__' --exclude 'deploy.sh' \
  ./ "${HOST}:${DEST}"

echo "▸ 5. 라이브 확인"
B="$(date +%s)"
printf "  language.html  -> %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "${SITE}/language.html?b=${B}")"
printf "  index.html     -> %s\n" "$(curl -s -o /dev/null -w '%{http_code}' "${SITE}/index.html?b=${B}")"
printf "  CSS 버전 일치   -> %s\n" "$(curl -s "${SITE}/language.html?b=${B}" | grep -c "components.css?v=${V}")"
printf "  prefers-contrast-> %s\n" "$(curl -s "${SITE}/tokens.css?v=${V}" | grep -c 'prefers-contrast' || true)"
echo "완료."
