"""Block 07, why: sin x = 1/2 is the line y = 1/2 crossing the circle twice."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Пряма y = 1/2 перетинає одиничне коло у двох точках: при x = π/6 і x = 5π/6. Кожна з них повторюється через повний оберт 2π, звідси дві серії коренів рівняння sin x = 1/2.',
           'sin x = 1/2: дві точки на одному оберті, далі - повторення через 2π.'),
    'ru': ('Прямая y = 1/2 пересекает единичную окружность в двух точках: при x = π/6 и x = 5π/6. Каждая из них повторяется через полный оборот 2π, отсюда две серии корней уравнения sin x = 1/2.',
           'sin x = 1/2: две точки на одном обороте, дальше - повторение через 2π.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(240)
    p = Plot(f, 40, 12, 230, 210, -1.3, 1.3, -1.25, 1.25)
    p.axes(ticks_y=(1,))
    cx, cy = p.pt(0, 0)
    r = p.px(1) - cx
    f.circle(cx, cy, r, w=1.2)
    f.line(p.px(-1.3), p.py(0.5), p.px(1.3), p.py(0.5), w=1.6, accent=True)
    f.text(p.px(1.28), p.py(0.5) + 18, 'y = 1/2', size=12, anchor='end', accent=True)
    for ang, name, anchor, dx in ((30, 'π/6', 'start', 8), (150, '5π/6', 'end', -8)):
        a = math.radians(ang)
        pt = p.pt(math.cos(a), math.sin(a))
        f.line(cx, cy, *pt, w=1.2, op=0.8)
        f.circle(*pt, 4.5, dot=True, accent=True)
        f.text(pt[0] + dx, pt[1] - 10, name, size=13, anchor=anchor)
    return f, label, caption
