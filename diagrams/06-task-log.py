"""Block 6, task: the graph of y = log₂ x passes through a point with ordinate 3."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Графік функції y = log₂ x: проходить через точку (1; 0) і повільно росте праворуч. На висоті y = 3 проведено горизонтальну пунктирну лінію до графіка; точку перетину позначено, її абсциса невідома.',
           'До задачі: точка графіка логарифма з ординатою 3.'),
    'ru': ('График функции y = log₂ x: проходит через точку (1; 0) и медленно растёт вправо. На высоте y = 3 проведена горизонтальная пунктирная линия до графика; точка пересечения отмечена, её абсцисса неизвестна.',
           'К задаче: точка графика логарифма с ординатой 3.'),
}
Y = 3


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(210)
    p = Plot(f, 20, 10, 280, 186, -0.8, 10, -2.5, 4.2)
    p.axes(ticks_x=(1,), ticks_y=(Y,))
    p.curve(lambda x: math.log2(x) if x > 0 else None, 0.18, 9.8, n=200, w=2.2, accent=True)
    x = 2 ** Y
    f.line(p.px(0), p.py(Y), p.px(x), p.py(Y), w=1.2, dash='4 3', op=0.8)
    f.line(p.px(x), p.py(Y), p.px(x), p.py(0), w=1.2, dash='4 3', op=0.8)
    f.circle(*p.pt(x, Y), 4.5, dot=True, accent=True)
    f.text(p.px(x), p.py(0) + 16, '?', size=15, anchor='middle', bold=True)
    f.text(p.px(3.2), p.py(2.2), 'y = log₂ x', size=13, italic=True, accent=True, anchor='end')
    return f, label, caption
