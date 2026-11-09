"""Block 12, reading and linking: the centre and a point of a circle, its equation."""
import math
from fig import Fig, Plot

DATA = {'a': 2, 'b': 3, 'mx': 5, 'my': 7}
TEXT = {
    'uk': ('Коло з центром у точці C і точка M на колі. Від точок до осей проведено пунктир: центр C має координати (2; 3), точка M - (5; 7). На осях підписано 2, 5 і 3, 7.',
           'До задачі: коло, його центр і точка на колі.'),
    'ru': ('Окружность с центром в точке C и точка M на окружности. От точек к осям проведён пунктир: центр C имеет координаты (2; 3), точка M - (5; 7). На осях подписаны 2, 5 и 3, 7.',
           'К задаче: окружность, её центр и точка на окружности.'),
    'en': ('A circle with centre at point C and a point M on the circle. Dashed lines run from the points to the axes: the centre C has coordinates (2; 3), the point M (5; 7). The axes are labelled 2, 5 and 3, 7.',
           'For the task: a circle, its centre and a point on the circle.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    d = DATA
    s = 21  # px per unit on both axes, so the circle is round
    f = Fig(262)
    p = Plot(f, 22, 8, s * 13, s * 11.6, -4, 9, -2.6, 9)
    p.axes(ticks_x=(d['a'], d['mx']), ticks_y=(d['b'], d['my']))
    C, M = (d['a'], d['b']), (d['mx'], d['my'])
    r = math.hypot(M[0] - C[0], M[1] - C[1])
    f.circle(*p.pt(*C), r * s, w=1.8, fill_op=0.04, accent=True)
    for q in (C, M):
        f.line(*p.pt(q[0], 0), *p.pt(*q), w=1, dash='4 3', op=0.7)
        f.line(*p.pt(0, q[1]), *p.pt(*q), w=1, dash='4 3', op=0.7)
        f.circle(*p.pt(*q), 4, dot=True, accent=True)
    f.text(p.px(C[0]) + 8, p.py(C[1]) - 8, 'C', size=14, italic=True, bold=True)
    f.text(p.px(M[0]) + 8, p.py(M[1]) - 6, 'M', size=14, italic=True, bold=True)
    return f, label, caption
