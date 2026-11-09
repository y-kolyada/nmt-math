"""Block 12, why: the distance between points is the hypotenuse of a right triangle."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Точки A(1; 2) і B(4; 6). Різниці координат 3 і 4 - катети прямокутного трикутника, відрізок AB - гіпотенуза: AB = √(3² + 4²) = 5.',
           'Відстань між точками - теорема Піфагора: √(3² + 4²) = 5.'),
    'ru': ('Точки A(1; 2) и B(4; 6). Разности координат 3 и 4 - катеты прямоугольного треугольника, отрезок AB - гипотенуза: AB = √(3² + 4²) = 5.',
           'Расстояние между точками - теорема Пифагора: √(3² + 4²) = 5.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    p = Plot(f, 24, 10, 260, 190, -0.5, 5.5, -0.5, 7)
    p.axes(ticks_x=(1, 4), ticks_y=(2, 6))
    f.poly([p.pt(1, 2), p.pt(4, 2), p.pt(4, 6)], close=True, w=1.2, fill_op=0.08, dash='4 3')
    f.line(*p.pt(1, 2), *p.pt(4, 6), w=2.2, accent=True)
    for pt in ((1, 2), (4, 6)):
        f.circle(*p.pt(*pt), 4, dot=True)
    f.text(p.px(1) - 4, p.py(2) + 18, 'A', size=13, bold=True)
    f.text(p.px(4) + 8, p.py(6) + 4, 'B', size=13, bold=True)
    f.text(p.px(2.5), p.py(2) + 16, '3', size=13, anchor='middle', bold=True)
    f.text(p.px(4) + 8, p.py(4) + 4, '4', size=13, bold=True)
    f.text(p.px(2.2), p.py(4.4), '5', size=14, anchor='middle', bold=True, accent=True)
    return f, label, caption
