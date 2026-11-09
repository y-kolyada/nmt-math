"""Block 01, concept: the modulus is a distance to zero on the number line."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Числова пряма від −5 до 5. Точки −3 і 3 стоять на однаковій відстані 3 від нуля, тому |−3| = |3| = 3.',
           'Модуль - відстань до нуля: |−3| = |3| = 3.', 'відстань 3'),
    'ru': ('Числовая прямая от −5 до 5. Точки −3 и 3 стоят на одинаковом расстоянии 3 от нуля, поэтому |−3| = |3| = 3.',
           'Модуль - расстояние до нуля: |−3| = |3| = 3.', 'расстояние 3'),
}


def figure(lang):
    label, caption, dist = TEXT[lang]
    f = Fig(110)
    p = Plot(f, 14, 20, 292, 60, -5.5, 5.5, -1, 1)
    y = p.py(0)
    f.arrow(14, y, 306, y, w=1.2)
    for k in range(-5, 6):
        f.line(p.px(k), y - 4, p.px(k), y + 4, w=1)
        f.text(p.px(k), y + 20, ('%d' % k).replace('-', '−'), size=12, anchor='middle', op=0.8)
    for k in (-3, 3):
        f.circle(p.px(k), y, 4.5, dot=True, accent=True)
    f.line(p.px(-3), y - 18, p.px(0), y - 18, w=2, accent=True)
    f.line(p.px(0), y - 18, p.px(3), y - 18, w=2, accent=True)
    for k in (-3, 0, 3):
        f.line(p.px(k), y - 23, p.px(k), y - 13, w=1.4, accent=True)
    f.text(p.px(-1.5), y - 26, dist, size=12, anchor='middle')
    f.text(p.px(1.5), y - 26, dist, size=12, anchor='middle')
    return f, label, caption
