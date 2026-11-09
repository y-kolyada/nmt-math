"""Block 05, why: y = (x + 2)² is y = x² moved two units to the LEFT."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Парабола y = x² з вершиною в нулі і парабола y = (x + 2)² з вершиною в точці −2. Стрілка показує зсув на 2 ліворуч, хоча в дужках стоїть плюс.',
           'f(x + 2): вершина переїхала з 0 у −2, тобто ліворуч.', 'ліворуч на 2'),
    'ru': ('Парабола y = x² с вершиной в нуле и парабола y = (x + 2)² с вершиной в точке −2. Стрелка показывает сдвиг на 2 влево, хотя в скобках стоит плюс.',
           'f(x + 2): вершина переехала из 0 в −2, то есть влево.', 'влево на 2'),
    'en': ('The parabola y = x² with vertex at zero and the parabola y = (x + 2)² with vertex at −2. The arrow shows a shift of 2 to the left, although the brackets hold a plus.',
           'f(x + 2): the vertex moved from 0 to −2, that is, to the left.',
           'left by 2'),
}


def figure(lang):
    label, caption, left = TEXT[lang]
    f = Fig(210)
    p = Plot(f, 14, 14, 292, 168, -5, 3, -1.7, 5)
    p.axes(ticks_x=(-2, 2), ticks_y=(2, 4))
    p.curve(lambda x: x * x, -2.3, 2.3, w=1.4, op=0.6)
    p.curve(lambda x: (x + 2) ** 2, -4.3, 0.3, w=2, accent=True)
    f.circle(*p.pt(0, 0), 4, dot=True)
    f.circle(*p.pt(-2, 0), 4.5, dot=True, accent=True)
    f.arrow(p.px(-0.2), p.py(-0.55), p.px(-1.8), p.py(-0.55), w=1.6, accent=True)
    f.text(p.px(-1), p.py(-0.55) + 17, left, size=12, anchor='middle', accent=True)
    f.text(p.px(-4.2), p.py(4.6), 'y = (x + 2)²', size=12, accent=True)
    f.text(p.px(1.2), p.py(4.6), 'y = x²', size=12, op=0.8)
    return f, label, caption
