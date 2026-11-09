"""Block 10, corollary: the angles of a parallelogram."""
import math
from fig import Fig

TEXT = {
    'uk': ('Паралелограм ABCD. Кути A і C позначено α, кути B і D позначено 180° − α: сусідні кути разом дають 180°, протилежні рівні.',
           'Наслідок: сусідні кути паралелограма в сумі 180°, протилежні рівні.'),
    'ru': ('Параллелограмм ABCD. Углы A и C отмечены α, углы B и D отмечены 180° − α: соседние углы вместе дают 180°, противоположные равны.',
           'Следствие: соседние углы параллелограмма в сумме 180°, противоположные равны.'),
    'en': ('Parallelogram ABCD. Angles A and C are marked α, angles B and D are marked 180° − α: adjacent angles add up to 180°, opposite angles are equal.',
           'Corollary: adjacent angles of a parallelogram add up to 180°, opposite angles are equal.'),
}
ALPHA = 60


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(190)
    a = math.radians(ALPHA)
    A = (40, 160)
    B = (A[0] + 170, A[1])
    D = (A[0] + 120 * math.cos(a), A[1] - 120 * math.sin(a))
    C = (B[0] + D[0] - A[0], D[1])
    f.poly([A, B, C, D], close=True, w=1.8, fill_op=0.04)
    for name, p, dxy, anc in (('A', A, (-6, 14), 'end'), ('B', B, (4, 14), 'start'), ('C', C, (6, -2), 'start'), ('D', D, (-6, -4), 'end')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    f.text(A[0] + 26, A[1] - 8, 'α', size=14, accent=True)
    f.text(C[0] - 26, C[1] + 20, 'α', size=14, anchor='end', accent=True)
    f.text(B[0] - 10, B[1] - 10, '180° − α', size=13, anchor='end')
    f.text(D[0] + 12, D[1] + 22, '180° − α', size=13)
    return f, label, caption
