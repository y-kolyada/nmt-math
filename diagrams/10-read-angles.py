"""Block 10, reading: two angles of a triangle are marked, the third is asked."""
import math
from fig import Fig

DATA = {'a': 48, 'b': 67}
TEXT = {
    'uk': ('Трикутник ABC. На рисунку позначено кути: ∠A = 48°, ∠B = 67°. Кут C позначено знаком питання.',
           'До задачі: трикутник із двома позначеними кутами.'),
    'ru': ('Треугольник ABC. На рисунке отмечены углы: ∠A = 48°, ∠B = 67°. Угол C отмечен знаком вопроса.',
           'К задаче: треугольник с двумя отмеченными углами.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    A, B = (60, 200), (260, 200)
    ta, tb = math.tan(math.radians(DATA['a'])), math.tan(math.radians(DATA['b']))
    x = (B[0] - A[0]) * tb / (ta + tb)
    C = (A[0] + x, A[1] - x * ta)
    f = Fig(226)
    f.poly([A, B, C], close=True, w=1.8, fill_op=0.04)
    for p, a0, a1 in ((A, 0, DATA['a']), (B, 180 - DATA['b'], 180)):
        r = 26
        q0 = (p[0] + r * math.cos(math.radians(a0)), p[1] - r * math.sin(math.radians(a0)))
        q1 = (p[0] + r * math.cos(math.radians(a1)), p[1] - r * math.sin(math.radians(a1)))
        f.add('<path d="M %.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" stroke="currentColor" stroke-width="1.2"/>' % (q0[0], q0[1], r, r, q1[0], q1[1]))
    f.text(A[0] + 32, A[1] - 8, '48°', size=13, accent=True)
    f.text(B[0] - 32, B[1] - 8, '67°', size=13, anchor='end', accent=True)
    f.text(C[0], C[1] + 28, '?', size=15, anchor='middle', bold=True, accent=True)
    for name, p, dxy, anc in (('A', A, (-6, 16), 'end'), ('B', B, (6, 16), 'start'), ('C', C, (0, -8), 'middle')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    return f, label, caption
