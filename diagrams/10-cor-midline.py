"""Block 10, corollary: the midline of a triangle."""
from fig import Fig

TEXT = {
    'uk': ('Трикутник ABC, M - середина AB, N - середина BC. Середня лінія MN виділена: вона паралельна AC і дорівнює її половині; AC позначено a, MN позначено a/2.',
           'Наслідок: середня лінія трикутника паралельна третій стороні і дорівнює її половині.'),
    'ru': ('Треугольник ABC, M - середина AB, N - середина BC. Средняя линия MN выделена: она параллельна AC и равна её половине; AC отмечена a, MN отмечена a/2.',
           'Следствие: средняя линия треугольника параллельна третьей стороне и равна её половине.'),
}
A, B, C = (40, 170), (150, 30), (280, 170)


def figure(lang):
    label, caption = TEXT[lang]
    M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    N = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    f = Fig(200)
    f.poly([A, B, C], close=True, w=1.8, fill_op=0.04)
    f.line(*M, *N, w=2.4, accent=True)
    for p in (M, N):
        f.circle(*p, 3.5, dot=True, accent=True)
    for name, p, dxy, anc in (('A', A, (-6, 14), 'end'), ('B', B, (0, -10), 'middle'), ('C', C, (6, 14), 'start'),
                              ('M', M, (-8, 0), 'end'), ('N', N, (8, 0), 'start')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    f.text((A[0] + C[0]) / 2, A[1] + 18, 'a', size=14, anchor='middle', italic=True)
    f.text((M[0] + N[0]) / 2, M[1] + 18, 'a/2', size=14, anchor='middle', italic=True, accent=True)
    return f, label, caption
