"""Block 10, reading with an extra number: a parallelogram, an angle and a side."""
import math
from fig import Fig

DATA = {'a': 58, 'ab': 7}
TEXT = {
    'uk': ('Паралелограм ABCD. На рисунку позначено кут A = 58° і підписано сторону AB = 7 см. Кут B позначено знаком питання.',
           'До задачі: паралелограм із позначеним кутом і підписаною стороною.'),
    'ru': ('Параллелограмм ABCD. На рисунке отмечен угол A = 58° и подписана сторона AB = 7 см. Угол B отмечен знаком вопроса.',
           'К задаче: параллелограмм с отмеченным углом и подписанной стороной.'),
    'en': ('Parallelogram ABCD. The figure marks angle A = 58° and labels side AB = 7 cm. Angle B is marked with a question mark.',
           'For the task: a parallelogram with a marked angle and a labelled side.'),
    'de': ('Das Parallelogramm ABCD. Auf der Abbildung ist der Winkel A = 58° markiert und die Seite AB = 7 cm beschriftet. Der Winkel B ist mit einem Fragezeichen markiert.',
           'Zur Aufgabe: ein Parallelogramm mit einem markierten Winkel und einer beschrifteten Seite.'),
}

# The unit is a word of the page language: a figure in English says cm.
CM = {'uk': 'см', 'ru': 'см', 'en': 'cm', 'de': 'cm'}


def figure(lang):
    label, caption = TEXT[lang]
    a = math.radians(DATA['a'])
    A = (40, 160)
    B = (A[0] + DATA['ab'] * 24, A[1])
    D = (A[0] + 125 * math.cos(a), A[1] - 125 * math.sin(a))
    C = (B[0] + D[0] - A[0], D[1])
    f = Fig(192)
    f.poly([A, B, C, D], close=True, w=1.8, fill_op=0.04)
    r = 24
    q1 = (A[0] + r * math.cos(a), A[1] - r * math.sin(a))
    f.add('<path d="M %.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" stroke="currentColor" stroke-width="1.2"/>' % (A[0] + r, A[1], r, r, q1[0], q1[1]))
    f.text(A[0] + 30, A[1] - 8, '58°', size=13, accent=True)
    f.text((A[0] + B[0]) / 2, A[1] + 20, '7 ' + CM[lang], size=13, anchor='middle')
    f.text(B[0] - 14, B[1] - 10, '?', size=15, anchor='end', bold=True, accent=True)
    for name, p, dxy, anc in (('A', A, (-6, 16), 'end'), ('B', B, (6, 16), 'start'), ('C', C, (6, -4), 'start'), ('D', D, (-6, -4), 'end')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    return f, label, caption
