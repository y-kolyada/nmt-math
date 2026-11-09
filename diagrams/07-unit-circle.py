"""Block 07, why: (cos α; sin α) on the unit circle, and Pythagoras in it."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Одиничне коло з центром у початку координат. Точка на колі під кутом α має координати (cos α; sin α). Катети прямокутного трикутника - cos α і sin α, гіпотенуза - радіус 1, тому cos²α + sin²α = 1.',
           'Синус і косинус - координати точки одиничного кола; тотожність - теорема Піфагора.'),
    'ru': ('Единичная окружность с центром в начале координат. Точка на окружности под углом α имеет координаты (cos α; sin α). Катеты прямоугольного треугольника - cos α и sin α, гипотенуза - радиус 1, поэтому cos²α + sin²α = 1.',
           'Синус и косинус - координаты точки единичной окружности; тождество - теорема Пифагора.'),
    'en': ('The unit circle centred at the origin. The point on the circle at angle α has coordinates (cos α; sin α). The legs of the right triangle are cos α and sin α, the hypotenuse is the radius 1, so cos²α + sin²α = 1.',
           "Sine and cosine are the coordinates of a point of the unit circle; the identity is Pythagoras' theorem."),
    'de': ('Der Einheitskreis mit dem Mittelpunkt im Ursprung. Der Kreispunkt zum Winkel α hat die Koordinaten (cos α; sin α). Die Katheten des rechtwinkligen Dreiecks sind cos α und sin α, die Hypotenuse ist der Radius 1, also cos²α + sin²α = 1.',
           'Sinus und Kosinus sind die Koordinaten eines Punktes des Einheitskreises; die Identität ist der Satz des Pythagoras.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(250)
    p = Plot(f, 40, 10, 230, 230, -1.3, 1.3, -1.3, 1.3)
    p.axes(ticks_x=(-1, 1), ticks_y=(-1, 1))
    cx, cy = p.pt(0, 0)
    r = p.px(1) - cx
    f.circle(cx, cy, r, w=1.4)
    a = math.radians(50)
    x, y = math.cos(a), math.sin(a)
    f.line(cx, cy, *p.pt(x, y), w=1.8, accent=True)
    f.line(*p.pt(x, 0), *p.pt(x, y), w=2, accent=True)
    f.line(cx, cy, *p.pt(x, 0), w=2, accent=True)
    f.circle(*p.pt(x, y), 4.5, dot=True, accent=True)
    f.text(p.px(x) + 8, p.py(y) - 6, '(cos α; sin α)', size=12)
    f.text(p.px(x / 2), p.py(0) + 16, 'cos α', size=12, anchor='middle')
    f.text(p.px(x) + 6, p.py(y / 2) + 4, 'sin α', size=12)
    f.text(p.px(0.2), p.py(0.12), 'α', size=13, italic=True)
    f.text(p.px(x / 2) - 12, p.py(y / 2) - 4, '1', size=13, anchor='end')
    return f, label, caption
