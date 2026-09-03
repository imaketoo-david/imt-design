# -*- coding: utf-8 -*-
"""가이드에서 쓰는 아이콘만 뽑아 guide/_sprite.svg 를 만든다.

334개를 통째로 넣으면 문서마다 104KB 가 붙는다. 쓰는 것만 넣는다.
아이콘을 새로 쓰기 시작하면 아래 NEED 에 이름을 더한다.
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "..", "imt-icons", "sprite.svg")
SRCD = os.path.join(ROOT, "..", "imt-icons", "sprite-derived.svg")   # 파생 4축

NEED = ['check-circle','x-circle','arrow-right','arrow-up','arrow-down','check','close',
        'warning','info','bell','star','edit','search','plus','trash','more','filter',
        'lock','layers','doc','trend-up','trend-down','person','sparkle','camera',
        'repeat','wallet','stethoscope','chart-line','box','brush','chart-bar','arrow-left','download','link','ruler','contrast',
        'rounded-square','book-open','palette' if False else 'dots-grid',
        # 파생 축 예시 — 문서에서 원본과 나란히 보여 준다
        'bell.fill','bell.circle','bell.square','bell.slash',
        'star.fill','person.fill','folder.fill','heart.fill','gear.fill']

src = open(SRC, encoding="utf-8").read()
if os.path.exists(SRCD):
    src += open(SRCD, encoding="utf-8").read()
syms = {m.group(1): f'<symbol id="i-{m.group(1)}"{m.group(2)}</symbol>'
        for m in re.finditer(r'<symbol id="i-([a-z0-9.-]+)"(.*?)</symbol>', src, re.S)}
miss = [n for n in NEED if n not in syms]
if miss:
    raise SystemExit(f"아이콘 없음: {', '.join(miss)} — imt-icons 에 먼저 추가한다")
out = ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">'
       + "".join(syms[n] for n in NEED) + '</svg>')
open(os.path.join(ROOT, "guide", "_sprite.svg"), "w", encoding="utf-8").write(out)
print(f"▸ 스프라이트 {len(NEED)}개 · {len(out)} 바이트")
