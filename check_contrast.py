import re,sys
src=open('tokens.css',encoding='utf-8').read()
def lin(c):
    c/=255; return c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
def L(h):
    h=h.lstrip('#'); r,g,b=(int(h[i:i+2],16) for i in (0,2,4))
    return .2126*lin(r)+.7152*lin(g)+.0722*lin(b)
def R(a,b):
    l1,l2=L(a),L(b)
    if l1<l2: l1,l2=l2,l1
    return (l1+.05)/(l2+.05)
def seg(a,b):
    i=src.index(a)+len(a); j=src.index(b,i)
    return dict(re.findall(r'(--[a-z0-9-]+):\s*(#[0-9a-fA-F]{6})',src[i:j]))
LIGHT = seg(':root {','@media (prefers-color-scheme: dark)')
CON_L = seg('@media (prefers-contrast: more) {\n  :root:not([data-theme="dark"]) {','  }')
CON_D = seg('@media (prefers-contrast: more) {','}\n}\n@media (prefers-contrast: more) and')
DARK  = seg(':root[data-theme="dark"] {\n  color-scheme: dark;','   대비 강화 — 시스템 설정')
SOFT={'up':'#fceceb','down':'#e8f1fd','ok':'#e6f4ec','warn':'#fdf1de','danger':'#fdeceb','info':'#e4f2f9'}
SOFT_D={'up':'#3a2523','down':'#123049','ok':'#1e3527','warn':'#3a3410','danger':'#3a201e','info':'#12333a'}
fails=[]
def chk(tag,fg,bg,t):
    r=R(fg,bg)
    if r<t: fails.append(tag)
    print(f"{'PASS' if r>=t else 'FAIL'}  {tag:38s} {fg} on {bg}  {r:5.2f}  (>= {t})")

print("── LIGHT 기본 (텍스트 4.5 / 그래픽 3.0) ──")
for k,bg,t in [('--ink','#f2f2f7',4.5),('--ink2','#f2f2f7',4.5),('--sub','#f2f2f7',4.5),('--sub','#ffffff',4.5),
               ('--placeholder','#ffffff',4.5),('--placeholder','#f5f5f8',4.5),
               ('--link','#f2f2f7',4.5),('--danger','#ffffff',4.5),
               ('--flat','#ffffff',3.0),('--axis','#ffffff',3.0),('--line','#ffffff',1.2)]:
    chk(k+' @'+bg, LIGHT[k], bg, t)
print("  차트 8슬롯 — 비텍스트 마크이므로 3:1 기준")
for i in range(1,9): chk(f'--c{i} @#ffffff', LIGHT[f'--c{i}'], '#ffffff', 3.0)

print("\n── LIGHT + Increase Contrast ──")
for k in ['up','down','ok','warn','danger','info']:
    chk(f'--{k} @{k}-soft', CON_L['--'+k], SOFT[k], 4.5)
for k,bg,t in [('--sub','#f2f2f7',4.5),('--sub2','#ffffff',4.5),('--placeholder','#f5f5f8',4.5),
               ('--link','#ffffff',4.5),('--flat','#ffffff',3.0),('--line','#ffffff',3.0)]:
    chk(k+' @'+bg, CON_L[k], bg, t)

D='#1c1c1e'
print("\n── DARK 기본 (@ --card #1c1c1e) ──")
for k,t in [('--ink',4.5),('--ink2',4.5),('--sub',4.5),('--placeholder',4.5),('--link',4.5),
            ('--flat',3.0),('--axis',3.0),('--up',4.5),('--down',4.5),('--ok',4.5),
            ('--warn',4.5),('--danger',4.5),('--info',4.5),('--indigo',3.0),('--line',1.2)]:
    chk(k+' (dark)', DARK.get(k) or LIGHT[k], D, t)
print("  차트 8슬롯 (다크, 라이트와 동일값)")
for i in range(1,9): chk(f'--c{i} (dark)', LIGHT[f'--c{i}'], D, 3.0)

print("\n── DARK + Increase Contrast ──")
for k,t in [('--sub',4.5),('--sub2',4.5),('--placeholder',4.5),('--link',4.5),('--indigo',4.5),('--axis',3.0)]:
    chk(k+' (dark/ic)', CON_D[k], D, t)

print("\n실패:", fails if fails else "없음")
sys.exit(1 if fails else 0)
