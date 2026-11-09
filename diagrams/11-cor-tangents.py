"""Block 11, corollary: the two tangent segments from one point are equal."""
import math
from fig import Fig

TEXT = {
    'uk': ('Коло з центром O і точка P поза ним. З P проведено дві дотичні, точки дотику T₁ і T₂; обидва відрізки дотичних позначено t. Радіуси OT₁ і OT₂ перпендикулярні до дотичних.',
           'Наслідок: відрізки дотичних, проведених до кола з однієї точки, рівні.'),
    'ru': ('Окружность с центром O и точка P вне её. Из P проведены две касательные, точки касания T₁ и T₂; оба отрезка касательных отмечены t. Радиусы OT₁ и OT₂ перпендикулярны касательным.',
           'Следствие: отрезки касательных, проведённых к окружности из одной точки, равны.'),
    'en': ('A circle with centre O and a point P outside it. Two tangents are drawn from P, touching at T₁ and T₂; both tangent segments are marked t. The radii OT₁ and OT₂ are perpendicular to the tangents.',
           'Corollary: the tangent segments drawn to a circle from one point are equal.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    O, R = (90, 100), 58
    P = (280, 100)
    d = P[0] - O[0]
    phi = math.acos(R / d)
    T = [(O[0] + R * math.cos(s * phi), O[1] - R * math.sin(s * phi)) for s in (1, -1)]
    f = Fig(200)
    f.circle(*O, R, w=1.4, fill_op=0.04)
    for t in T:
        f.line(*P, *t, w=2.2, accent=True)
        f.line(*O, *t, w=1.2, dash='4 3')
        f.circle(*t, 3.5, dot=True)
        # the right angle at the touching point
        u = ((O[0] - t[0]) / R, (O[1] - t[1]) / R)
        L = math.hypot(P[0] - t[0], P[1] - t[1])
        v = ((P[0] - t[0]) / L, (P[1] - t[1]) / L)
        a = (t[0] + u[0] * 9, t[1] + u[1] * 9)
        f.poly([a, (a[0] + v[0] * 9, a[1] + v[1] * 9), (t[0] + v[0] * 9, t[1] + v[1] * 9)], w=1)
        m = ((P[0] + t[0]) / 2, (P[1] + t[1]) / 2)
        f.text(m[0] + 2, m[1] + (-8 if t[1] < O[1] else 20), 't', size=14, italic=True, accent=True)
    f.circle(*O, 3, dot=True)
    f.circle(*P, 3.5, dot=True)
    f.text(O[0] - 8, O[1] + 5, 'O', size=14, anchor='end', italic=True)
    f.text(P[0] + 4, P[1] + 20, 'P', size=14, anchor='middle', italic=True)
    f.text(T[0][0] - 2, T[0][1] - 10, 'T₁', size=14, anchor='middle', italic=True)
    f.text(T[1][0] - 2, T[1][1] + 22, 'T₂', size=14, anchor='middle', italic=True)
    return f, label, caption
