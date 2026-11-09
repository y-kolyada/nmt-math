"""Block 11, reading: the sides of a rectangle are on the figure, the diagonal is asked."""
from fig import Fig

DATA = {'a': 5, 'b': 12}
TEXT = {
    'uk': ('Прямокутник ABCD. На рисунку підписано сторони: AD = 5 см, AB = 12 см. Діагональ AC - пунктиром, позначена знаком питання.',
           'До задачі: прямокутник із підписаними сторонами і діагональ.'),
    'ru': ('Прямоугольник ABCD. На рисунке подписаны стороны: AD = 5 см, AB = 12 см. Диагональ AC - пунктиром, отмечена знаком вопроса.',
           'К задаче: прямоугольник с подписанными сторонами и диагональ.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    s = 20
    A = (50, 150)
    B = (A[0] + DATA['b'] * s, A[1])
    C = (B[0], A[1] - DATA['a'] * s)
    D = (A[0], C[1])
    f = Fig(186)
    f.poly([A, B, C, D], close=True, w=1.8, fill_op=0.04)
    f.line(*A, *C, w=1.6, dash='6 4', accent=True)
    f.text((A[0] + C[0]) / 2 - 6, (A[1] + C[1]) / 2 - 8, '?', size=15, bold=True, accent=True)
    f.text((A[0] + B[0]) / 2, A[1] + 20, '12 см', size=13, anchor='middle')
    f.text(A[0] - 8, (A[1] + D[1]) / 2 + 5, '5 см', size=13, anchor='end')
    for name, p, dxy, anc in (('A', A, (-6, 16), 'end'), ('B', B, (6, 16), 'start'), ('C', C, (6, -4), 'start'), ('D', D, (-6, -4), 'end')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    return f, label, caption
