# -*- coding: utf-8 -*-
"""CSS 가 우리 규칙을 지키는지 검사한다 (L-0.3 — 규칙은 기계가 검사할 수 있어야 한다).

검사 항목
  L-5.1  간격은 4의 배수만
  L-6.1  라운드는 --r 계열만 (도해 안은 L-6.7 로 면제)
  L-7.1  글자 크기는 --fs-* 단계만
  L-7.2  가는 굵기(400 미만)를 쓰지 않는다
"""
import re, sys, glob, os

ROOT = os.path.dirname(os.path.abspath(__file__))
tok  = open(os.path.join(ROOT, "tokens.css"), encoding="utf-8").read()
FS   = {int(v) for v in re.findall(r'--fs-[a-z0-9]+:\s*(\d+)px', tok)}
R    = {int(v) for v in re.findall(r'--r[a-z-]*:\s*(\d+)px', tok)} | {0, 999}
# 도해 컨테이너 — 여기 안은 축소 비율을 쓴다 (L-6.7)
FIG  = ("tile__art", "rcard__art", "g-fig", "g-cmp", "g-ana", "g-scale", "g-seq", "imt-canvas")

SPACE = re.compile(r'\b(?:margin|padding|gap|row-gap|column-gap)(?:-[a-z]+)?:\s*([^;{}]+)')
PX    = re.compile(r'(?<![\w.-])(\d+(?:\.\d+)?)px')

bad = []
for f in sorted(glob.glob(os.path.join(ROOT, "*.css"))):
    name = os.path.basename(f)
    if name == "tokens.css": continue
    for i, ln in enumerate(open(f, encoding="utf-8"), 1):
        t = ln.strip()
        if t.startswith(("/*", "*")) or any(k in ln for k in FIG): continue

        for decl in SPACE.findall(ln):
            for v in PX.findall(decl):
                n = float(v)
                if n % 4 and 2 < n < 80:
                    bad.append(f"{name}:{i}  L-5.1 간격 {v}px — 4의 배수가 아니다"); break

        for m in re.finditer(r'border-radius:\s*([^;{}]+)', ln):
            for v in PX.findall(m.group(1)):
                if int(float(v)) not in R:
                    bad.append(f"{name}:{i}  L-6.1 라운드 {v}px — 토큰에 없는 값")

        for m in re.finditer(r'font-size:\s*(\d+(?:\.\d+)?)px', ln):
            if int(float(m.group(1))) not in FS:
                bad.append(f"{name}:{i}  L-7.1 글자 {m.group(1)}px — 단계에 없다")

        for m in re.finditer(r'font-weight:\s*(\d{3})', ln):
            if int(m.group(1)) < 400:
                bad.append(f"{name}:{i}  L-7.2 굵기 {m.group(1)} — 400 미만은 쓰지 않는다")

if bad:
    print(f"✗ 규칙 위반 {len(bad)}건")
    for b in bad[:30]: print("   " + b)
    sys.exit(1)
print("✓ 규칙 위반 없음 (L-5.1 · L-6.1 · L-7.1 · L-7.2)")
