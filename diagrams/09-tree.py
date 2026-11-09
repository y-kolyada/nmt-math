"""Block 09, why: two coin tosses as a tree, 2 · 2 = 4 equally likely outcomes (from 09-tree.mmd)."""
from fig import Fig

TEXT = {
    'uk': ('Дерево двох кидків монети: з початку дві гілки, герб і цифра, з кожної ще дві. Листків 2 · 2 = 4: ГГ, ГЦ, ЦГ, ЦЦ. Усі чотири рівноможливі, і лише один з них - два герби.',
           'Правило добутку як дерево: 2 · 2 = 4 рівноможливі наслідки.', 'Г', 'Ц', ['1-й кидок', '2-й кидок']),
    'ru': ('Дерево двух бросков монеты: из начала две ветви, герб и цифра, из каждой ещё две. Листьев 2 · 2 = 4: ГГ, ГЦ, ЦГ, ЦЦ. Все четыре равновозможны, и только один из них - два герба.',
           'Правило произведения как дерево: 2 · 2 = 4 равновозможных исхода.', 'Г', 'Ц', ['1-й бросок', '2-й бросок']),
    'en': ('A tree of two coin tosses: from the start, two branches, heads and tails, and two more from each. There are 2 · 2 = 4 leaves: HH, HT, TH, TT. All four are equally likely, and only one of them is two heads.',
           'The product rule as a tree: 2 · 2 = 4 equally likely outcomes.',
           'H',
           'T',
           ['1st toss', '2nd toss']),
    'de': ('Ein Baum für zwei Münzwürfe: vom Start zwei Äste, Kopf und Zahl, und von jedem noch zwei. Es gibt 2 · 2 = 4 Blätter: KK, KZ, ZK, ZZ. Alle vier sind gleich wahrscheinlich, und nur eines davon ist zweimal Kopf.',
           'Die Produktregel als Baum: 2 · 2 = 4 gleich wahrscheinliche Ausgänge.',
           'K',
           'Z',
           ['1. Wurf', '2. Wurf']),
}


def figure(lang):
    label, caption, g, c, steps = TEXT[lang]
    f = Fig(196)
    f.circle(24, 98, 5, dot=True)
    mids = [(120, 50, g), (120, 146, c)]
    leaves = [(236, 24, g + g), (236, 76, g + c), (236, 120, c + g), (236, 172, c + c)]
    for (x, y, t) in mids:
        f.line(29, 98, x - 18, y, w=1.2)
        f.rect(x - 18, y - 14, 36, 28, fill_op=0.06)
        f.text(x, y + 5, t, size=14, anchor='middle', bold=True)
    for i, (x, y, t) in enumerate(leaves):
        mx, my, _ = mids[i // 2]
        f.line(mx + 18, my, x - 22, y, w=1.2)
        f.rect(x - 22, y - 14, 44, 28, fill_op=0.25 if i == 0 else 0.06, accent=(i == 0))
        f.text(x, y + 5, t, size=14, anchor='middle', bold=(i == 0))
    f.text(70, 192, steps[0], size=12, anchor='middle', op=0.7)
    f.text(186, 192, steps[1], size=12, anchor='middle', op=0.7)
    return f, label, caption
