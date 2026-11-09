"""Block 02, hook: +20 % then −20 % does not return the price."""
from fig import Fig

TEXT = {
    'uk': ('Три стовпчики: 100 гривень, після підвищення на 20 % від 100 - 120 гривень, після зниження на 20 % від 120 - 96 гривень. Пунктир показує рівень 100, до якого ціна не повернулася.',
           'Два кроки по 20 % від різних цілих: 100 → 120 → 96.', ['+20 % від 100', '−20 % від 120'], 'грн'),
    'ru': ('Три столбика: 100 гривен, после повышения на 20 % от 100 - 120 гривен, после снижения на 20 % от 120 - 96 гривен. Пунктир показывает уровень 100, к которому цена не вернулась.',
           'Два шага по 20 % от разных целых: 100 → 120 → 96.', ['+20 % от 100', '−20 % от 120'], 'грн'),
}


def figure(lang):
    label, caption, steps, cur = TEXT[lang]
    f = Fig(200)
    base, k = 170, 1.15  # baseline y, px per hryvnia
    vals = [100, 120, 96]
    xs = [30, 130, 230]
    for i, (x, v) in enumerate(zip(xs, vals)):
        h = v * k
        f.rect(x, base - h, 60, h, rx=3, fill_op=0.12 if i != 2 else 0.22, accent=(i == 2))
        f.text(x + 30, base - h - 6, '%d %s' % (v, cur), size=13, anchor='middle', bold=True)
    f.line(14, base - 100 * k, 306, base - 100 * k, w=1, dash='4 3', op=0.7)
    f.line(14, base, 306, base, w=1.2)
    f.text(xs[0] + 60 + 20, base + 22, steps[0], size=12, anchor='middle', op=0.8)
    f.text(xs[1] + 60 + 20, base + 22, steps[1], size=12, anchor='middle', op=0.8)
    f.arrow(xs[0] + 62, base - 60, xs[1] - 2, base - 60, w=1)
    f.arrow(xs[1] + 62, base - 60, xs[2] - 2, base - 60, w=1)
    return f, label, caption
