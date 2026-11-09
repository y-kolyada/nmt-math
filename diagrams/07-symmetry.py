"""Block 07, why: α and π − α are mirror images in the y-axis."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Точки кола для кутів α і π − α симетричні відносно осі Oy: ординати однакові, абсциси протилежні. Звідси sin(π − α) = sin α і cos(π − α) = −cos α.',
           'Формула зведення як симетрія кола: sin(π − α) = sin α.'),
    'ru': ('Точки окружности для углов α и π − α симметричны относительно оси Oy: ординаты одинаковы, абсциссы противоположны. Отсюда sin(π − α) = sin α и cos(π − α) = −cos α.',
           'Формула приведения как симметрия окружности: sin(π − α) = sin α.'),
    'en': ('The points of the circle for the angles α and π − α are symmetric about the Oy axis: the ordinates are equal, the abscissas are opposite. Hence sin(π − α) = sin α and cos(π − α) = −cos α.',
           'A reduction formula as a symmetry of the circle: sin(π − α) = sin α.'),
    'de': ('Die Kreispunkte zu den Winkeln α und π − α liegen symmetrisch zur Oy-Achse: die Ordinaten sind gleich, die Abszissen entgegengesetzt. Daher sin(π − α) = sin α und cos(π − α) = −cos α.',
           'Eine Reduktionsformel als Symmetrie des Kreises: sin(π − α) = sin α.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(230)
    p = Plot(f, 40, 14, 230, 200, -1.3, 1.3, -0.9, 1.35)
    p.axes()
    cx, cy = p.pt(0, 0)
    r = p.px(1) - cx
    f.circle(cx, cy, r, w=1.2)
    a = math.radians(35)
    for sx, acc, name in ((1, True, 'α'), (-1, False, 'π − α')):
        x, y = sx * math.cos(a), math.sin(a)
        f.line(cx, cy, *p.pt(x, y), w=1.8, accent=acc)
        f.circle(*p.pt(x, y), 4.5, dot=True, accent=acc)
        f.line(*p.pt(x, y), *p.pt(x, 0), w=1, dash='3 3', op=0.7)
        f.text(p.px(x) + (8 if sx > 0 else -8), p.py(y) - 8, name, size=13, anchor='start' if sx > 0 else 'end', italic=True, accent=acc)
    f.line(*p.pt(-math.cos(a), math.sin(a)), *p.pt(math.cos(a), math.sin(a)), w=1, dash='2 4', op=0.6)
    f.text(cx + 6, p.py(math.sin(a)) - 6, 'sin', size=12, op=0.8)
    return f, label, caption
