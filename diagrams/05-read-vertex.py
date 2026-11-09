"""Block 5, reading: the vertex of a parabola on a grid."""
from fig import Fig, Plot

DATA = {'m': 2, 'n': 3}
TEXT = {
    'uk': ('Парабола у координатах, гілки вгору. Її вершина - точка (2; 3): від вершини до осей проведено пунктир, на осі x позначено 2, на осі y - 3.',
           'До задачі: парабола з позначеною вершиною.'),
    'ru': ('Парабола в координатах, ветви вверх. Её вершина - точка (2; 3): от вершины к осям проведён пунктир, на оси x отмечено 2, на оси y - 3.',
           'К задаче: парабола с отмеченной вершиной.'),
    'en': ('A parabola on coordinate axes, opening upwards. Its vertex is the point (2; 3): dashed lines run from the vertex to the axes, 2 is marked on the x-axis and 3 on the y-axis.',
           'For the task: a parabola with a marked vertex.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    m, n = DATA['m'], DATA['n']
    f = Fig(220)
    p = Plot(f, 24, 10, 270, 190, -1.5, 5.5, -1, 9.5)
    p.axes(ticks_x=(m,), ticks_y=(n,))
    p.curve(lambda x: (x - m) ** 2 + n, -1.5, 5.5, w=2.2, accent=True)
    f.line(*p.pt(m, 0), *p.pt(m, n), w=1, dash='4 3', op=0.8)
    f.line(*p.pt(0, n), *p.pt(m, n), w=1, dash='4 3', op=0.8)
    f.circle(*p.pt(m, n), 3.5, dot=True, accent=True)
    return f, label, caption
