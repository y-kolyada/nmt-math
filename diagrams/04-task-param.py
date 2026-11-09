"""Block 4, task: for which a the equation x² − 4x = a has no roots."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Парабола y = x² − 4x з вершиною в точці (2; −4) і горизонтальна пряма y = a, проведена нижче вершини. Пряма, що лежить нижче вершини, не має з параболою спільних точок.',
           'До задачі: число коренів рівняння x² − 4x = a як число спільних точок параболи і прямої y = a.'),
    'ru': ('Парабола y = x² − 4x с вершиной в точке (2; −4) и горизонтальная прямая y = a, проведённая ниже вершины. Прямая, лежащая ниже вершины, не имеет с параболой общих точек.',
           'К задаче: число корней уравнения x² − 4x = a как число общих точек параболы и прямой y = a.'),
    'en': ('The parabola y = x² − 4x with vertex at (2; −4) and the horizontal line y = a drawn below the vertex. A line lying below the vertex has no common points with the parabola.',
           'For the task: the number of roots of x² − 4x = a as the number of common points of the parabola and the line y = a.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(230)
    p = Plot(f, 20, 10, 280, 206, -1.5, 5.8, -6.2, 5.5)
    p.axes(ticks_x=(2, 4), ticks_y=(-4,))
    p.curve(lambda x: x * x - 4 * x, -1.2, 5.2, w=2.2)
    f.line(p.px(0), p.py(-4), p.px(2), p.py(-4), w=1, dash='3 3', op=0.6)
    f.circle(*p.pt(2, -4), 3.5, dot=True)
    f.line(p.px(-1.4), p.py(-5.3), p.px(5.6), p.py(-5.3), w=2, dash='6 4', accent=True)
    f.text(p.px(5.6), p.py(-5.3) - 6, 'y = a', size=13, italic=True, anchor='end', accent=True)
    f.text(p.px(4.6), p.py(1.3), 'y = x² − 4x', size=13, italic=True, anchor='end')
    return f, label, caption
