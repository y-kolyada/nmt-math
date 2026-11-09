"""Block 11, hook: doubling the side of a square makes the area four times larger."""
from fig import Fig

TEXT = {
    'uk': ('Ліворуч квадрат зі стороною 3 і площею 9. Праворуч квадрат зі стороною 6: він складається з чотирьох таких самих квадратів, тому його площа 36, учетверо більша.',
           'Сторона подвоїлася - площа зросла вчетверо: 3² = 9, 6² = 36.'),
    'ru': ('Слева квадрат со стороной 3 и площадью 9. Справа квадрат со стороной 6: он складывается из четырёх таких же квадратов, поэтому его площадь 36, вчетверо больше.',
           'Сторона удвоилась - площадь выросла вчетверо: 3² = 9, 6² = 36.'),
    'en': ('On the left, a square with side 3 and area 9. On the right, a square with side 6: it is made of four such squares, so its area is 36, four times as large.',
           'The side doubled, so the area grew fourfold: 3² = 9, 6² = 36.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(176)
    u = 22
    f.rect(20, 80, 3 * u, 3 * u, rx=0, fill_op=0.12)
    f.text(20 + 1.5 * u, 80 + 1.5 * u + 5, 'S = 9', size=13, anchor='middle')
    f.text(20 + 1.5 * u, 80 + 3 * u + 18, '3', size=13, anchor='middle', italic=True)
    x1, y1 = 150, 14
    for i in range(2):
        for j in range(2):
            f.rect(x1 + j * 3 * u, y1 + i * 3 * u, 3 * u, 3 * u, rx=0, fill_op=0.12, accent=(i + j == 0))
            f.text(x1 + j * 3 * u + 1.5 * u, y1 + i * 3 * u + 1.5 * u + 5, '9', size=13, anchor='middle')
    f.text(x1 + 3 * u, y1 + 6 * u + 18, '6  ·  S = 36', size=13, anchor='middle', italic=True)
    f.arrow(96, 110, 140, 90, w=1.2)
    return f, label, caption
