"""Block 10, corollary: a quadrilateral inscribed in a circle."""
import math
from fig import Fig

TEXT = {
    'uk': ('Чотирикутник ABCD, вписаний у коло. Кут A позначено α, протилежний кут C - 180° − α; кут B позначено β, протилежний кут D - 180° − β.',
           'Наслідок: у вписаному чотирикутнику сума протилежних кутів дорівнює 180°.'),
    'ru': ('Четырёхугольник ABCD, вписанный в окружность. Угол A отмечен α, противоположный угол C - 180° − α; угол B отмечен β, противоположный угол D - 180° − β.',
           'Следствие: во вписанном четырёхугольнике сумма противоположных углов равна 180°.'),
}
# the positions of A, B, C, D on the circle, degrees counter-clockwise from the right
AT = {'A': 200, 'B': 290, 'C': 10, 'D': 110}


def figure(lang):
    label, caption = TEXT[lang]
    O, R = (160, 112), 96
    pt = {k: (O[0] + R * math.cos(math.radians(v)), O[1] - R * math.sin(math.radians(v))) for k, v in AT.items()}
    f = Fig(230)
    f.circle(*O, R, w=1.4, fill_op=0.03)
    f.poly([pt['A'], pt['B'], pt['C'], pt['D']], close=True, w=1.8)
    for k in 'ABCD':
        x, y = pt[k]
        ux, uy = (x - O[0]) / R, (y - O[1]) / R
        f.text(x + ux * 14, y + uy * 14 + 5, k, size=14, anchor='middle', italic=True)
    inside = lambda k, d: (pt[k][0] + (O[0] - pt[k][0]) * d, pt[k][1] + (O[1] - pt[k][1]) * d)
    for k, s, acc in (('A', 'α', True), ('C', '180° − α', True), ('B', 'β', False), ('D', '180° − β', False)):
        x, y = inside(k, {'A': 0.26, 'B': 0.3, 'C': 0.5, 'D': 0.42}[k])
        f.text(x, y + 5, s, size=13, anchor='middle', accent=acc)
    return f, label, caption
