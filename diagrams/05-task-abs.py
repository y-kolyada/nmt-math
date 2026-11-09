"""Block 5, task: y = |x| moved 2 to the left, where it meets the axis Oy."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Два графіки-«куточки» в координатах. Пунктиром - y = |x| з вершиною в початку координат. Кольором - той самий графік, зсунутий на 2 одиниці ліворуч: його вершина в точці (−2; 0). Точку, де новий графік перетинає вісь Oy, позначено.',
           'До задачі: графік y = |x|, зсунутий ліворуч.'),
    'ru': ('Два графика-«уголка» в координатах. Пунктиром - y = |x| с вершиной в начале координат. Цветом - тот же график, сдвинутый на 2 единицы влево: его вершина в точке (−2; 0). Точка, где новый график пересекает ось Oy, отмечена.',
           'К задаче: график y = |x|, сдвинутый влево.'),
    'en': ('Two «V» graphs on coordinate axes. Dashed: y = |x| with its vertex at the origin. Coloured: the same graph shifted 2 units to the left, with its vertex at (−2; 0). The point where the new graph crosses the Oy axis is marked.',
           'For the task: the graph of y = |x| shifted to the left.'),
    'de': ('Zwei «V»-Graphen im Koordinatensystem. Gestrichelt: y = |x| mit dem Scheitel im Ursprung. Farbig: derselbe Graph um 2 Einheiten nach links verschoben, mit dem Scheitel bei (−2; 0). Der Punkt, in dem der neue Graph die Oy-Achse schneidet, ist markiert.',
           'Zur Aufgabe: der Graph von y = |x|, nach links verschoben.'),
}
DX = -2


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(200)
    p = Plot(f, 20, 10, 280, 176, -5.5, 3.5, -1, 4.6)
    p.axes(ticks_x=(DX,))
    p.curve(abs, -4.4, 3.4, w=1.6, dash='5 4', op=0.7)
    p.curve(lambda x: abs(x - DX), -5.5, 2.4, w=2.2, accent=True)
    f.arrow(*p.pt(-0.15, 0.25), *p.pt(DX + 0.2, 0.25), w=1.6, accent=True)
    f.circle(*p.pt(0, abs(-DX)), 4, dot=True, accent=True)
    return f, label, caption
