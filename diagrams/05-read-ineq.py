"""Block 5, reading and linking: the zeros of a parabola, the integer solutions of f(x) < 0."""
from fig import Fig, Plot, fmt

DATA = {'x1': -1, 'x2': 3}
TEXT = {
    'uk': ('Графік функції y = f(x) - парабола, гілки вгору. Вона перетинає вісь x у точках −1 і 3 (позначені), вершина - у точці (1; −4). Частина графіка під віссю x виділена.',
           'До задачі: парабола, яка перетинає вісь x у двох позначених точках.'),
    'ru': ('График функции y = f(x) - парабола, ветви вверх. Она пересекает ось x в точках −1 и 3 (отмечены), вершина - в точке (1; −4). Часть графика под осью x выделена.',
           'К задаче: парабола, которая пересекает ось x в двух отмеченных точках.'),
    'en': ('The graph of y = f(x) is a parabola opening upwards. It crosses the x-axis at −1 and 3 (marked), and its vertex is at (1; −4). The part of the graph below the x-axis is highlighted.',
           'For the task: a parabola that crosses the x-axis at two marked points.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    x1, x2 = DATA['x1'], DATA['x2']
    fn = lambda x: (x - x1) * (x - x2)
    f = Fig(230)
    p = Plot(f, 24, 10, 270, 204, -3, 5, -5, 6)
    p.axes(ticks_x=(1,), ticks_y=(-4,))
    for x, dx, anc in ((x1, -6, 'end'), (x2, 6, 'start')):
        f.line(p.px(x), p.py(0) - 3, p.px(x), p.py(0) + 3, w=1)
        f.text(p.px(x) + dx, p.py(0) + 16, fmt(x), size=12, anchor=anc, op=0.8)
    p.curve(fn, -3, 5, w=1.6)
    p.curve(lambda x: fn(x) if x1 <= x <= x2 else None, x1, x2, w=2.6, accent=True)
    for x in (x1, x2):
        f.circle(*p.pt(x, 0), 3.5, dot=True, accent=True)
    f.line(*p.pt(1, 0), *p.pt(1, -4), w=1, dash='4 3', op=0.7)
    f.line(*p.pt(0, -4), *p.pt(1, -4), w=1, dash='4 3', op=0.7)
    return f, label, caption
