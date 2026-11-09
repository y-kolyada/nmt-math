"""Block 5, task: the common points of y = x² and y = x + 2."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Парабола y = x² і пряма y = x + 2 в одних координатах. Пряма перетинає параболу у двох точках, ліворуч і праворуч від осі Oy; обидві точки позначено.',
           'До задачі: спільні точки параболи і прямої.'),
    'ru': ('Парабола y = x² и прямая y = x + 2 в одних координатах. Прямая пересекает параболу в двух точках, слева и справа от оси Oy; обе точки отмечены.',
           'К задаче: общие точки параболы и прямой.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    p = Plot(f, 20, 10, 280, 196, -3, 3.5, -1, 6)
    p.axes()
    p.curve(lambda x: x * x, -2.5, 2.5, w=2)
    p.curve(lambda x: x + 2, -3, 3.5, w=2, accent=True)
    for x in ((1 - 3) / 2, (1 + 3) / 2):  # roots of x² − x − 2 = 0, D = 9
        f.circle(*p.pt(x, x * x), 4.5, dot=True, accent=True)
    f.text(p.px(-2.3) + 2, p.py(5.3), 'y = x²', size=13, italic=True)
    f.text(p.px(2.9), p.py(5.3) - 2, 'y = x + 2', size=13, italic=True, accent=True, anchor='end')
    return f, label, caption
