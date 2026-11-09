"""Block 13, why: the lateral surface of a right prism unfolds into a rectangle P · h."""
from fig import Fig

TEXT = {
    'uk': ('Розгортка бічної поверхні прямої чотирикутної призми: чотири бічні грані стали в ряд і утворили прямокутник. Його ширина - периметр основи a + b + a + b, висота - висота призми h, тому бічна поверхня дорівнює P · h.',
           'Бічна поверхня прямої призми - прямокутник зі сторонами P і h.', 'P = a + b + a + b'),
    'ru': ('Развёртка боковой поверхности прямой четырёхугольной призмы: четыре боковые грани встали в ряд и образовали прямоугольник. Его ширина - периметр основания a + b + a + b, высота - высота призмы h, поэтому боковая поверхность равна P · h.',
           'Боковая поверхность прямой призмы - прямоугольник со сторонами P и h.', 'P = a + b + a + b'),
    'en': ('The net of the lateral surface of a right square prism: the four side faces stand in a row and form a rectangle. Its width is the perimeter of the base a + b + a + b, its height is the height of the prism h, so the lateral surface equals P · h.',
           'The lateral surface of a right prism is a rectangle with sides P and h.',
           'P = a + b + a + b'),
    'de': ('Das Netz der Mantelfläche eines geraden Prismas mit viereckiger Grundfläche: die vier Seitenflächen stehen in einer Reihe und bilden ein Rechteck. Seine Breite ist der Umfang der Grundfläche a + b + a + b, seine Höhe die Höhe des Prismas h, also ist die Mantelfläche P · h.',
           'Die Mantelfläche eines geraden Prismas ist ein Rechteck mit den Seiten P und h.',
           'P = a + b + a + b'),
}


def figure(lang):
    label, caption, per = TEXT[lang]
    f = Fig(150)
    x0, y0, h = 20, 20, 80
    ws = [80, 50, 80, 50]
    x = x0
    for i, w in enumerate(ws):
        f.rect(x, y0, w, h, rx=0, fill_op=0.16 if i % 2 else 0.08, accent=(i == 0))
        f.text(x + w / 2, y0 + h / 2 + 5, 'ab'[i % 2], size=14, anchor='middle', italic=True)
        x += w
    f.text(x + 6, y0 + h / 2 + 5, 'h', size=14, italic=True)
    f.line(x0, y0 + h + 14, x0 + sum(ws), y0 + h + 14, w=1, op=0.6)
    f.text(x0 + sum(ws) / 2, y0 + h + 34, per, size=13, anchor='middle', italic=True)
    return f, label, caption
