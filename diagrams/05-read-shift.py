"""Block 5, reading with a trap: the grid step is 2, the shifted graph of |x|."""
from fig import Fig, Plot

DATA = {'h': 4, 'k': 2}
TEXT = {
    'uk': ('Координатна сітка з кроком 2: на осях підписано 2, 4, 6. Пунктиром - графік y = |x| з вершиною в початку координат. Суцільною лінією - графік-«куточок» з вершиною в точці (4; 2): дві клітинки праворуч і одна вгору.',
           'До задачі: графік y = |x| і зсунутий графік на сітці з кроком 2.'),
    'ru': ('Координатная сетка с шагом 2: на осях подписаны 2, 4, 6. Пунктиром - график y = |x| с вершиной в начале координат. Сплошной линией - график-«уголок» с вершиной в точке (4; 2): две клетки вправо и одна вверх.',
           'К задаче: график y = |x| и сдвинутый график на сетке с шагом 2.'),
    'en': ('A coordinate grid with step 2: the axes are labelled 2, 4, 6. Dashed: the graph of y = |x| with its vertex at the origin. Solid: a «V» graph with its vertex at (4; 2): two squares to the right and one up.',
           'For the task: the graph of y = |x| and a shifted graph on a grid with step 2.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    h, k = DATA['h'], DATA['k']
    f = Fig(230)
    p = Plot(f, 24, 10, 270, 200, -3, 8.6, -1, 7.6)
    for x in (-2, 2, 4, 6, 8):
        f.line(*p.pt(x, -1), *p.pt(x, 7.6), w=0.8, op=0.25)
    for y in (2, 4, 6):
        f.line(*p.pt(-3, y), *p.pt(8.6, y), w=0.8, op=0.25)
    p.axes(ticks_x=(2, 4, 6), ticks_y=(2, 4, 6))
    p.curve(lambda x: abs(x), -3, 7.6, w=1.4, dash='5 4')
    p.curve(lambda x: abs(x - h) + k, -1.5, 8.6, n=240, w=2.2, accent=True)
    f.circle(*p.pt(h, k), 3.5, dot=True, accent=True)
    return f, label, caption
