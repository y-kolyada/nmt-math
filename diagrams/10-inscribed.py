"""Block 10, why: the inscribed angle is half the central angle on the same arc."""
import math
from fig import Fig

TEXT = {
    'uk': ('Коло з центром O. Центральний кут AOB дорівнює 100°, вписаний кут ACB спирається на ту саму дугу AB і дорівнює 50° - удвічі менше.',
           'Вписаний кут - половина центрального на тій самій дузі: 100° і 50°.'),
    'ru': ('Окружность с центром O. Центральный угол AOB равен 100°, вписанный угол ACB опирается на ту же дугу AB и равен 50° - вдвое меньше.',
           'Вписанный угол - половина центрального на той же дуге: 100° и 50°.'),
    'en': ('A circle with centre O. The central angle AOB is 100°; the inscribed angle ACB stands on the same arc AB and is 50°, half as large.',
           'An inscribed angle is half the central angle on the same arc: 100° and 50°.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(230)
    cx, cy, r = 160, 112, 92
    f.circle(cx, cy, r, w=1.4)
    pt = lambda deg: (cx + r * math.cos(math.radians(deg)), cy - r * math.sin(math.radians(deg)))
    A, B, C = pt(220), pt(320), pt(100)
    f.poly([A, (cx, cy), B], w=1.8, accent=True)
    f.poly([A, C, B], w=1.6)
    for p in (A, B, C):
        f.circle(*p, 3.5, dot=True)
    f.circle(cx, cy, 3.5, dot=True, accent=True)
    f.text(A[0] - 8, A[1] + 14, 'A', size=14, anchor='end', bold=True)
    f.text(B[0] + 8, B[1] + 14, 'B', size=14, bold=True)
    f.text(C[0], C[1] - 8, 'C', size=14, anchor='middle', bold=True)
    f.text(cx + 8, cy - 4, 'O', size=14, bold=True)
    f.text(cx, cy + 30, '100°', size=13, anchor='middle', accent=True)
    f.text(C[0] + 2, C[1] + 34, '50°', size=13, anchor='middle')
    return f, label, caption
