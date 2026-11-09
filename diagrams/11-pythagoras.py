"""Block 11, why: (a + b)² = 4 · ab/2 + c² proves Pythagoras."""
from fig import Fig

TEXT = {
    'uk': ('Квадрат зі стороною a + b, у кутах якого стоять чотири однакові прямокутні трикутники з катетами a і b. Усередині лишається квадрат зі стороною c - гіпотенузою. Площа: (a + b)² = 4 · ab/2 + c², звідки a² + b² = c².',
           'Доведення теореми Піфагора площею: чотири трикутники і квадрат c².'),
    'ru': ('Квадрат со стороной a + b, в углах которого стоят четыре одинаковых прямоугольных треугольника с катетами a и b. Внутри остаётся квадрат со стороной c - гипотенузой. Площадь: (a + b)² = 4 · ab/2 + c², откуда a² + b² = c².',
           'Доказательство теоремы Пифагора площадью: четыре треугольника и квадрат c².'),
    'en': ('A square with side a + b, in whose corners stand four equal right triangles with legs a and b. Inside remains a square with side c, the hypotenuse. Area: (a + b)² = 4 · ab/2 + c², hence a² + b² = c².',
           "A proof of Pythagoras' theorem by area: four triangles and a square c²."),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(236)
    x0, y0, a, b = 70, 18, 120, 60
    s = a + b
    P = [(x0 + a, y0), (x0 + s, y0 + a), (x0 + b, y0 + s), (x0, y0 + b)]
    f.rect(x0, y0, s, s, rx=0, fill_op=0.12)
    f.poly(P, close=True, w=1.8, fill_op=0.25, accent=True)
    f.text(x0 + s / 2, y0 + s / 2 + 6, 'c²', size=18, anchor='middle', italic=True, bold=True)
    f.text(x0 + a / 2, y0 - 4, 'a', size=14, anchor='middle', italic=True)
    f.text(x0 + a + b / 2, y0 - 4, 'b', size=14, anchor='middle', italic=True)
    f.text(x0 - 8, y0 + b / 2 + 5, 'b', size=14, anchor='end', italic=True)
    f.text(x0 - 8, y0 + b + a / 2 + 5, 'a', size=14, anchor='end', italic=True)
    f.text((P[0][0] + P[1][0]) / 2 + 4, (P[0][1] + P[1][1]) / 2 - 4, 'c', size=14, italic=True, accent=True)
    return f, label, caption
