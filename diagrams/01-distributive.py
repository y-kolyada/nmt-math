"""Block 01, why: a(b + c) = ab + ac as the area of one rectangle cut in two."""
from fig import Fig

TEXT = {
    'uk': ('Прямокутник висотою a і шириною b + c розрізано на два прямокутники: ab і ac. Площа цілого a(b + c) дорівнює сумі площ ab + ac.',
           'Розподільний закон як площа: a(b + c) = ab + ac.'),
    'ru': ('Прямоугольник высотой a и шириной b + c разрезан на два прямоугольника: ab и ac. Площадь целого a(b + c) равна сумме площадей ab + ac.',
           'Распределительный закон как площадь: a(b + c) = ab + ac.'),
    'en': ('A rectangle of height a and width b + c is cut into two rectangles: ab and ac. The area of the whole, a(b + c), equals the sum of the areas ab + ac.',
           'The distributive law as area: a(b + c) = ab + ac.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(176)
    x0, y0, a, b, c = 40, 20, 90, 150, 100
    f.rect(x0, y0, b, a, rx=0, fill_op=0.08)
    f.rect(x0 + b, y0, c, a, rx=0, fill_op=0.16, accent=True)
    f.text(x0 + b / 2, y0 + a / 2 + 5, 'ab', size=16, anchor='middle', italic=True)
    f.text(x0 + b + c / 2, y0 + a / 2 + 5, 'ac', size=16, anchor='middle', italic=True)
    f.text(x0 - 10, y0 + a / 2 + 5, 'a', size=15, anchor='end', italic=True)
    f.text(x0 + b / 2, y0 + a + 20, 'b', size=15, anchor='middle', italic=True)
    f.text(x0 + b + c / 2, y0 + a + 20, 'c', size=15, anchor='middle', italic=True)
    f.line(x0, y0 + a + 32, x0 + b + c - 2, y0 + a + 32, w=1, op=0.6)
    f.text(x0 + (b + c) / 2, y0 + a + 46, 'b + c', size=13, anchor='middle', italic=True, op=0.8)
    return f, label, caption
