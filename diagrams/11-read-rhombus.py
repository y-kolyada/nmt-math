"""Block 11, reading and linking: the diagonals of a rhombus, its perimeter."""
from fig import Fig

DATA = {'d1': 10, 'd2': 24}
TEXT = {
    'uk': ('Ромб ABCD з діагоналями, що перетинаються в точці O під прямим кутом. На рисунку підписано діагоналі: AC = 24 см, BD = 10 см.',
           'До задачі: ромб і дві його діагоналі.'),
    'ru': ('Ромб ABCD с диагоналями, пересекающимися в точке O под прямым углом. На рисунке подписаны диагонали: AC = 24 см, BD = 10 см.',
           'К задаче: ромб и две его диагонали.'),
    'en': ('Rhombus ABCD with diagonals meeting at point O at a right angle. The figure labels the diagonals: AC = 24 cm, BD = 10 cm.',
           'For the task: a rhombus and its two diagonals.'),
}

# The unit is a word of the page language: a figure in English says cm.
CM = {'uk': 'см', 'ru': 'см', 'en': 'cm'}


def figure(lang):
    label, caption = TEXT[lang]
    s = 10
    O = (160, 92)
    A = (O[0] - DATA['d2'] / 2 * s, O[1])
    C = (O[0] + DATA['d2'] / 2 * s, O[1])
    B = (O[0], O[1] - DATA['d1'] / 2 * s * 1.3)
    D = (O[0], O[1] + DATA['d1'] / 2 * s * 1.3)
    f = Fig(186)
    f.poly([A, B, C, D], close=True, w=1.8, fill_op=0.04)
    f.line(*A, *C, w=1.3, dash='5 4', accent=True)
    f.line(*B, *D, w=1.3, dash='5 4', accent=True)
    f.poly([(O[0], O[1] - 9), (O[0] + 9, O[1] - 9), (O[0] + 9, O[1])], w=1)
    f.text((A[0] + O[0]) / 2, O[1] + 18, 'AC = 24 ' + CM[lang], size=13, anchor='middle', accent=True)
    f.text(O[0] + 8, (B[1] + O[1]) / 2 - 2, 'BD = 10 ' + CM[lang], size=13, accent=True)
    for name, p, dxy, anc in (('A', A, (-8, 5), 'end'), ('B', B, (0, -8), 'middle'), ('C', C, (8, 5), 'start'),
                              ('D', D, (0, 18), 'middle'), ('O', O, (-6, -6), 'end')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    return f, label, caption
