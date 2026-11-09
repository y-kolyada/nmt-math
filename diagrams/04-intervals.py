"""Block 04, limits: signs of (x − 3)(x + 3) between its zeros."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Числова пряма з нулями множників −3 і 3. Ліворуч від −3 і праворуч від 3 добуток (x − 3)(x + 3) додатний, між ними - від\'ємний. Тому x² > 9 при x < −3 або x > 3, а x² < 9 між −3 і 3.',
           'Метод інтервалів для (x − 3)(x + 3): знак змінюється лише в нулях множників.', ['x² > 9', 'x² < 9', 'x² > 9']),
    'ru': ('Числовая прямая с нулями множителей −3 и 3. Слева от −3 и справа от 3 произведение (x − 3)(x + 3) положительно, между ними - отрицательно. Поэтому x² > 9 при x < −3 или x > 3, а x² < 9 между −3 и 3.',
           'Метод интервалов для (x − 3)(x + 3): знак меняется только в нулях множителей.', ['x² > 9', 'x² < 9', 'x² > 9']),
}


def figure(lang):
    label, caption, words = TEXT[lang]
    f = Fig(120)
    p = Plot(f, 14, 20, 292, 60, -6, 6, -1, 1)
    y = 60
    f.arrow(14, y, 306, y, w=1.2)
    f.text(300, y + 18, 'x', size=13, anchor='end', italic=True)
    for k in (-3, 3):
        f.circle(p.px(k), y, 5, w=1.6)
        f.text(p.px(k), y + 20, ('%d' % k).replace('-', '−'), size=13, anchor='middle')
    for x, sign, w in ((-4.7, '+', words[0]), (0, '−', words[1]), (4.7, '+', words[2])):
        f.text(p.px(x), y - 14, sign, size=20, anchor='middle', bold=True, accent=(sign == '−'))
        f.text(p.px(x), y + 44, w, size=12, anchor='middle', op=0.8)
    pts = [p.pt(-6 + 12 * i / 60, 0) for i in range(0)]
    return f, label, caption
