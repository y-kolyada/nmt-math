"""Block 5, task: y = x² moved 3 to the right and 2 down."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Дві параболи в координатах. Пунктиром - графік y = x² з вершиною в початку координат. Кольором - той самий графік, зсунутий на 3 одиниці праворуч і на 2 одиниці вниз: його вершина в точці (3; −2). Стрілка веде від старої вершини до нової.',
           'До задачі: графік y = x², зсунутий праворуч і вниз.'),
    'ru': ('Две параболы в координатах. Пунктиром - график y = x² с вершиной в начале координат. Цветом - тот же график, сдвинутый на 3 единицы вправо и на 2 единицы вниз: его вершина в точке (3; −2). Стрелка ведёт от старой вершины к новой.',
           'К задаче: график y = x², сдвинутый вправо и вниз.'),
    'en': ('Two parabolas on coordinate axes. Dashed: the graph of y = x² with its vertex at the origin. Coloured: the same graph shifted 3 units to the right and 2 units down, with its vertex at (3; −2). An arrow leads from the old vertex to the new one.',
           'For the task: the graph of y = x² shifted right and down.'),
    'de': ('Zwei Parabeln im Koordinatensystem. Gestrichelt: der Graph von y = x² mit dem Scheitel im Ursprung. Farbig: derselbe Graph um 3 Einheiten nach rechts und 2 Einheiten nach unten verschoben, mit dem Scheitel bei (3; −2). Ein Pfeil führt vom alten Scheitel zum neuen.',
           'Zur Aufgabe: der Graph von y = x², nach rechts und nach unten verschoben.'),
}
DX, DY = 3, -2


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    p = Plot(f, 20, 10, 280, 196, -2.5, 6.5, -3, 6)
    p.axes(ticks_x=(3,), ticks_y=(-2,))
    p.curve(lambda x: x * x, -2.5, 2.5, w=1.6, dash='5 4', op=0.7)
    p.curve(lambda x: (x - DX) ** 2 + DY, DX - 2.9, DX + 2.9, w=2.2, accent=True)
    f.line(p.px(DX), p.py(0), p.px(DX), p.py(DY), w=1, dash='3 3', op=0.6)
    f.arrow(*p.pt(0.15, -0.1), *p.pt(DX - 0.15, DY + 0.08), w=1.6, accent=True)
    f.circle(*p.pt(DX, DY), 3.5, dot=True, accent=True)
    return f, label, caption
