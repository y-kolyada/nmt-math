"""Block 11, reading with an extra number: an isosceles trapezoid, its area."""
from fig import Fig

DATA = {'a': 6, 'b': 12, 'h': 4, 'c': 5}
TEXT = {
    'uk': ('Рівнобічна трапеція ABCD. На рисунку підписано: верхня основа BC = 6 см, нижня основа AD = 12 см, висота BH = 4 см (пунктиром), бічна сторона CD = 5 см.',
           'До задачі: трапеція, на якій підписано чотири довжини.'),
    'ru': ('Равнобокая трапеция ABCD. На рисунке подписаны: верхнее основание BC = 6 см, нижнее основание AD = 12 см, высота BH = 4 см (пунктиром), боковая сторона CD = 5 см.',
           'К задаче: трапеция, на которой подписаны четыре длины.'),
    'en': ('Isosceles trapezium ABCD. The figure labels: upper base BC = 6 cm, lower base AD = 12 cm, height BH = 4 cm (dashed), leg CD = 5 cm.',
           'For the task: a trapezium with four lengths labelled.'),
}

# The unit is a word of the page language: a figure in English says cm.
CM = {'uk': 'см', 'ru': 'см', 'en': 'cm'}


def figure(lang):
    label, caption = TEXT[lang]
    s = 20
    off = (DATA['b'] - DATA['a']) / 2
    A = (40, 160)
    D = (A[0] + DATA['b'] * s, A[1])
    B = (A[0] + off * s, A[1] - DATA['h'] * s)
    C = (B[0] + DATA['a'] * s, B[1])
    H = (B[0], A[1])
    f = Fig(196)
    f.poly([A, B, C, D], close=True, w=1.8, fill_op=0.04)
    f.line(*B, *H, w=1.4, dash='5 4', accent=True)
    f.poly([(H[0], H[1] - 9), (H[0] + 9, H[1] - 9), (H[0] + 9, H[1])], w=1)
    f.text((B[0] + C[0]) / 2, B[1] - 8, '6 ' + CM[lang], size=13, anchor='middle')
    f.text((A[0] + D[0]) / 2, A[1] + 20, '12 ' + CM[lang], size=13, anchor='middle')
    f.text(B[0] + 6, (B[1] + H[1]) / 2 + 5, '4 ' + CM[lang], size=13, accent=True)
    f.text((C[0] + D[0]) / 2 + 10, (C[1] + D[1]) / 2 + 2, '5 ' + CM[lang], size=13)
    for name, p, dxy, anc in (('A', A, (-6, 16), 'end'), ('B', B, (-6, -4), 'end'), ('C', C, (6, -4), 'start'),
                              ('D', D, (6, 16), 'start'), ('H', H, (0, 18), 'middle')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    return f, label, caption
