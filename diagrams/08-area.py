"""Block 08, why: the area under y = f(x) grows by a strip f(x) · h."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Площа під графіком y = 0,5x² + 0,5 від a до x зафарбована. Якщо x зрушити на маленьке h, площа виросте на вузьку смужку заввишки f(x): тому швидкість зростання площі дорівнює f(x), і площа - первісна.',
           'Ньютон - Лейбніц: площа росте на смужку f(x) · h, отже площа - первісна функції.', 'смужка f(x) · h'),
    'ru': ('Площадь под графиком y = 0,5x² + 0,5 от a до x закрашена. Если x сдвинуть на малое h, площадь вырастет на узкую полоску высотой f(x): поэтому скорость роста площади равна f(x), и площадь - первообразная.',
           'Ньютон - Лейбниц: площадь растёт на полоску f(x) · h, значит площадь - первообразная функции.', 'полоска f(x) · h'),
    'en': ('The area under the graph of y = 0.5x² + 0.5 from a to x is shaded. If x is moved by a small h, the area grows by a narrow strip of height f(x): so the rate at which the area grows equals f(x), and the area is an antiderivative.',
           'Newton - Leibniz: the area grows by a strip f(x) · h, so the area is an antiderivative of the function.',
           'strip f(x) · h'),
    'de': ('Die Fläche unter dem Graphen von y = 0,5x² + 0,5 von a bis x ist schraffiert. Verschiebt man x um ein kleines h, wächst die Fläche um einen schmalen Streifen der Höhe f(x): die Fläche wächst also mit der Rate f(x), und die Fläche ist eine Stammfunktion.',
           'Newton - Leibniz: die Fläche wächst um einen Streifen f(x) · h, also ist die Fläche eine Stammfunktion der Funktion.',
           'Streifen f(x) · h'),
}


def figure(lang):
    label, caption, strip = TEXT[lang]
    fn = lambda x: 0.5 * x * x + 0.5
    f = Fig(220)
    p = Plot(f, 20, 12, 280, 176, -0.3, 3.2, -0.3, 5.2)
    a, x, h = 0.4, 2.2, 0.28
    pts = [p.pt(a, 0)] + [p.pt(a + (x - a) * i / 40, fn(a + (x - a) * i / 40)) for i in range(41)] + [p.pt(x, 0)]
    f.poly(pts, close=True, w=0.8, fill_op=0.12)
    f.poly([p.pt(x, 0), p.pt(x, fn(x)), p.pt(x + h, fn(x)), p.pt(x + h, 0)], close=True, w=1.2, fill_op=0.35, accent=True)
    p.axes(xlabel='x', ylabel='y')
    p.curve(fn, -0.2, 3.1, w=2)
    f.text(p.px(a), p.py(0) + 16, 'a', size=13, anchor='middle', italic=True)
    f.text(p.px(x), p.py(0) + 16, 'x', size=13, anchor='middle', italic=True)
    f.text(p.px(x + h) + 6, p.py(0) + 16, 'x + h', size=12, italic=True)
    f.text(*p.pt(0.2, 4.3), strip, size=12, accent=True)
    f.arrow(p.px(1.6), p.py(4.15), p.px(x + h / 2), p.py(fn(x)) - 4, w=1.2, accent=True)
    f.text(p.px(1.2), p.py(0.6), 'S(x)', size=13, anchor='middle', italic=True)
    return f, label, caption
