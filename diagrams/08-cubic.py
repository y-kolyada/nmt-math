"""Block 08, limits: f = x³ − 3x² has a maximum at 0 and a minimum at 2."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Графік f(x) = x³ − 3x². Похідна 3x(x − 2) змінює знак з плюса на мінус у точці 0 - там максимум, і з мінуса на плюс у точці 2 - там мінімум. Знаки похідної підписано під віссю.',
           'Екстремум там, де похідна змінює знак: максимум у 0, мінімум у 2.', ['max', 'min'], "f′:"),
    'ru': ('График f(x) = x³ − 3x². Производная 3x(x − 2) меняет знак с плюса на минус в точке 0 - там максимум, и с минуса на плюс в точке 2 - там минимум. Знаки производной подписаны под осью.',
           'Экстремум там, где производная меняет знак: максимум в 0, минимум в 2.', ['max', 'min'], "f′:"),
    'en': ('The graph of f(x) = x³ − 3x². The derivative 3x(x − 2) changes sign from plus to minus at 0, where there is a maximum, and from minus to plus at 2, where there is a minimum. The signs of the derivative are written below the axis.',
           'An extremum is where the derivative changes sign: a maximum at 0, a minimum at 2.',
           ['max', 'min'],
           'f′:'),
}


def figure(lang):
    label, caption, mm, fd = TEXT[lang]
    f = Fig(230)
    p = Plot(f, 30, 12, 260, 170, -1.3, 3.4, -4.6, 1.5)
    p.axes(ticks_x=(2,), ticks_y=(-4,))
    p.curve(lambda x: x ** 3 - 3 * x * x, -1.2, 3.35, w=2, accent=True)
    f.circle(*p.pt(0, 0), 4.5, dot=True)
    f.circle(*p.pt(2, -4), 4.5, dot=True)
    f.text(p.px(0), p.py(0) - 10, mm[0], size=12, anchor='middle', bold=True)
    f.text(p.px(2), p.py(-4) + 20, mm[1], size=12, anchor='middle', bold=True)
    y = 214
    f.text(18, y, fd, size=12, op=0.8)
    for x, s in ((-0.7, '+'), (1, '−'), (2.8, '+')):
        f.text(p.px(x), y, s, size=16, anchor='middle', bold=True)
    for x in (0, 2):
        f.line(p.px(x), y - 14, p.px(x), y + 4, w=1, op=0.6)
    return f, label, caption
