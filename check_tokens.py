# -*- coding: utf-8 -*-
"""정의되지 않은 토큰을 쓰고 있지 않은지 검사한다.

var(--없는이름) 하나면 그 선언 '전체'가 무효가 된다 — padding 이 통째로
사라지는 식이다. 브라우저는 아무 말도 하지 않는다.
2026-09-02 에 --sp-7 (없는 단계) 때문에 리소스 카드의 안여백이 0이 됐다.
"""
import re, sys, glob, os

ROOT = os.path.dirname(os.path.abspath(__file__))
tok = set(re.findall(r'(--[a-z0-9-]+)\s*:', open(os.path.join(ROOT, "tokens.css"), encoding="utf-8").read()))

bad = 0
for f in sorted(glob.glob(os.path.join(ROOT, "*.css"))):
    if f.endswith("tokens.css"): continue
    s = open(f, encoding="utf-8").read()
    own = set(re.findall(r'(--[a-z0-9-]+)\s*:', s))
    miss = sorted(set(re.findall(r'var\((--[a-z0-9-]+)', s)) - tok - own)
    if s.count("{") != s.count("}"):
        print(f"✗ {os.path.basename(f)} 중괄호 불균형 {s.count('{')}/{s.count('}')}"); bad += 1
    if miss:
        print(f"✗ {os.path.basename(f)} 미정의 토큰: {' '.join(miss)}"); bad += 1

print("✓ 토큰 참조 정상" if not bad else "", end="" if bad else "\n")
sys.exit(1 if bad else 0)
