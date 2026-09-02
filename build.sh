#!/usr/bin/env bash
# IMT Design — 가이드 문서 생성
#   src/pages/*.py  →  guide/*.html
# 도해는 그림 파일이 아니라 tokens.css 로 그려지는 살아 있는 컴포넌트다.
# 그래서 토큰을 고치면 이 빌드만 다시 돌리면 문서가 따라온다.
set -euo pipefail
cd "$(dirname "$0")"

# 아이콘 스프라이트 — 가이드에서 쓰는 것만 뽑는다
if [ -f ../imt-icons/sprite.svg ]; then
  python3 src/build_sprite.py
else
  echo "▸ imt-icons 없음 — 스프라이트 갱신 건너뜀"
fi

IMT_V="${IMT_V:-dev}" python3 src/build_guide.py
IMT_V="${IMT_V:-dev}" python3 src/build_site.py
