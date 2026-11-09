"""Block 12, reading: two points on a grid, the distance between them."""
from fig import Fig, Plot

DATA = {'x1': 1, 'y1': 2, 'x2': 7, 'y2': 10}
TEXT = {
    'uk': ('Координатна площина з точками A і B. Від точок до осей проведено пунктир: точка A має абсцису 1 і ординату 2, точка B - абсцису 7 і ординату 10. На осях підписано 1, 7 і 2, 10.',
           'До задачі: дві точки, координати яких видно на осях.'),
    'ru': ('Координатная плоскость с точками A и B. От точек к осям проведён пунктир: точка A имеет абсциссу 1 и ординату 2, точка B - абсциссу 7 и ординату 10. На осях подписаны 1, 7 и 2, 10.',
           'К задаче: две точки, координаты которых видны на осях.'),
    'en': ('A coordinate plane with points A and B. Dashed lines run from the points to the axes: point A has abscissa 1 and ordinate 2, point B has abscissa 7 and ordinate 10. The axes are labelled 1, 7 and 2, 10.',
           'For the task: two points whose coordinates can be seen on the axes.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    d = DATA
    f = Fig(230)
    p = Plot(f, 30, 10, 260, 200, -1, 9, -1, 11.5)
    p.axes(ticks_x=(d['x1'], d['x2']), ticks_y=(d['y1'], d['y2']))
    A, B = (d['x1'], d['y1']), (d['x2'], d['y2'])
    for q in (A, B):
        f.line(*p.pt(q[0], 0), *p.pt(*q), w=1, dash='4 3', op=0.7)
        f.line(*p.pt(0, q[1]), *p.pt(*q), w=1, dash='4 3', op=0.7)
    f.line(*p.pt(*A), *p.pt(*B), w=2, accent=True)
    for name, q, dxy in (('A', A, (10, 4)), ('B', B, (10, 4))):
        f.circle(*p.pt(*q), 4, dot=True, accent=True)
        f.text(p.px(q[0]) + dxy[0], p.py(q[1]) + dxy[1], name, size=14, italic=True, bold=True)
    return f, label, caption
