# -*- coding: utf-8 -*-
"""도해 어휘 — 애플 문서의 그림 유형을 함수로 고정한다.

도해는 그림 파일이 아니라 살아 있는 컴포넌트다. tokens.css 가 바뀌면
도해도 같이 바뀐다 — 문서와 코드가 어긋날 수 없다는 것이 이 시스템의 전제고,
그 전제는 도해에도 똑같이 적용된다.
"""

def ic(name, cls=""):
    c = f" {cls}" if cls else ""
    return f'<svg class="imt-i{c}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def fig(body, cap="", plain=False):
    inner = body if plain else f'<div class="g-fig__body">{body}</div>'
    c = f'<p class="g-cap">{cap}</p>' if cap else ""
    return f'<figure class="g-fig">{inner}{c}</figure>'


def cmp2(items, cap=""):
    """비교 — 잘된 예 / 잘못된 예. items = [(kind, stage_html, label)]
    kind: 'do' | 'no'. 애플 문서에서 가장 많이 쓰이는 형태다."""
    out = []
    LABEL = {"do": "이렇게", "no": "이렇게 하지 않는다"}
    for it in items:
        kind, stage = it[0], it[1]
        label = it[2] if len(it) > 2 else LABEL[kind]
        mark = ic("check-circle") if kind == "do" else ic("x-circle")
        out.append(
            f'<div class="g-cmp__i g-cmp__i--{kind}">'
            f'<div class="g-cmp__stage">{stage}</div>'
            f'<div class="g-cmp__tag">{mark}{label}</div></div>')
    return fig(f'<div class="g-cmp">{"".join(out)}</div>', cap)


def anatomy(stage, items, cap=""):
    """해부 — 부품에 번호를 달아 지목한다. items = [(번호, 이름, 설명)]"""
    lis = "".join(
        f'<li><span class="g-pin">{n}</span><div><b>{t}</b><br>{d}</div></li>'
        for n, t, d in items)
    return fig(
        f'<div class="g-ana"><div class="g-ana__stage">{stage}</div>'
        f'<ul class="g-ana__list">{lis}</ul></div>', cap)


def scale(items, cap=""):
    """단계 — 축을 나열한다. items = [(시각 html, 이름, 단위)]"""
    out = "".join(
        f'<div class="g-scale__i"><div class="g-scale__v">{v}</div>'
        f'<div class="g-scale__n">{n}</div><div class="g-scale__u">{u}</div></div>'
        for v, n, u in items)
    return fig(f'<div class="g-scale">{out}</div>', cap)


def spec(headers, rows, cap=""):
    """사양표 — 수치는 글이 아니라 표로 준다."""
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return fig(
        f'<div class="g-spec__wrap"><table class="g-spec">'
        f'<thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>', cap, plain=True)


def grid(inner, cap=""):
    """격자 — 8px 눈금 위에 얹어 치수를 눈으로 재게 한다."""
    return fig(f'<div class="g-grid">{inner}</div>', cap, plain=True)


def seq(items, cap=""):
    """상태 순서 — items = [(시각 html, 이름)]"""
    arrow = f'<span class="g-seq__arrow">{ic("arrow-right")}</span>'
    cells = [f'<div class="g-seq__i">{v}<div class="g-seq__n">{n}</div></div>'
             for v, n in items]
    return fig(f'<div class="g-seq">{arrow.join(cells)}</div>', cap)


def dim(inner, label):
    """치수 표시 — 요소 아래에 눈금선과 값을 단다."""
    return f'<span class="g-dim" data-dim="{label}">{inner}</span>'
