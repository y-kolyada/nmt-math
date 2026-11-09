"""Block 04, limits: squaring √(x + 2) = x adds the extraneous root −1."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Графіки y = √(x + 2) і y = x перетинаються лише в точці x = 2. При x = −1 корінь дорівнює 1, а пряма дає −1: значення протилежні, тому після піднесення до квадрата −1 з\'являється як сторонній корінь.',
           'Сторонній корінь: при x = −1 обидві частини мають однаковий квадрат, але різні знаки.'),
    'ru': ('Графики y = √(x + 2) и y = x пересекаются только в точке x = 2. При x = −1 корень равен 1, а прямая даёт −1: значения противоположны, поэтому после возведения в квадрат −1 появляется как посторонний корень.',
           'Посторонний корень: при x = −1 обе части имеют одинаковый квадрат, но разные знаки.'),
    'en': ('The graphs y = √(x + 2) and y = x meet only at x = 2. At x = −1 the root equals 1 and the line gives −1: the values are opposite, so after squaring, −1 appears as an extraneous root.',
           'An extraneous root: at x = −1 both sides have the same square but different signs.'),
    'de': ('Die Graphen y = √(x + 2) und y = x treffen sich nur bei x = 2. Bei x = −1 ist die Wurzel 1 und die Gerade gibt −1: die Werte sind entgegengesetzt, also erscheint nach dem Quadrieren −1 als Scheinlösung.',
           'Eine Scheinlösung: bei x = −1 haben beide Seiten dasselbe Quadrat, aber verschiedene Vorzeichen.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(230)
    p = Plot(f, 30, 14, 260, 190, -2.5, 3.5, -2, 3)
    p.axes(ticks_x=(-1, 2), ticks_y=(-1, 1, 2))
    p.curve(lambda x: math.sqrt(x + 2) if x >= -2 else None, -2, 3.5, w=2, accent=True)
    p.curve(lambda x: x, -2, 3, w=1.6)
    f.circle(*p.pt(2, 2), 4.5, dot=True, accent=True)
    f.circle(*p.pt(-1, 1), 4, w=1.6)
    f.circle(*p.pt(-1, -1), 4, w=1.6)
    f.line(*p.pt(-1, 1), *p.pt(-1, -1), w=1, dash='3 3', op=0.7)
    f.text(p.px(3.4), p.py(math.sqrt(5.4)) - 8, 'y = √(x + 2)', size=12, anchor='end', accent=True)
    f.text(*p.pt(2.45, 1.25), 'y = x', size=12)
    return f, label, caption
