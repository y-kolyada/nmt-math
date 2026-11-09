"""Block 11, task: isosceles trapezoid with bases 4 and 16 and leg 10, its height."""
import math
from fig import Fig

TEXT = {
    'uk': ('Рівнобічна трапеція ABCD: нижня основа AD = 16, верхня основа BC = 4, бічна сторона AB = 10. З вершини B на основу AD опущено висоту h.',
           'До задачі: висота рівнобічної трапеції, опущена з вершини меншої основи.'),
    'ru': ('Равнобокая трапеция ABCD: нижнее основание AD = 16, верхнее основание BC = 4, боковая сторона AB = 10. Из вершины B на основание AD опущена высота h.',
           'К задаче: высота равнобокой трапеции, опущенная из вершины меньшего основания.'),
    'en': ('Isosceles trapezium ABCD: lower base AD = 16, upper base BC = 4, leg AB = 10. From vertex B the height h is dropped to the base AD.',
           'For the task: the height of an isosceles trapezium, dropped from a vertex of the shorter base.'),
    'de': ('Das gleichschenklige Trapez ABCD: untere Grundseite AD = 16, obere Grundseite BC = 4, Schenkel AB = 10. Von der Ecke B ist die Höhe h auf die Grundseite AD gefällt.',
           'Zur Aufgabe: die Höhe eines gleichschenkligen Trapezes, von einer Ecke der kürzeren Grundseite gefällt.'),
}
BIG, SMALL, LEG = 16, 4, 10


def figure(lang):
    label, caption = TEXT[lang]
    s = 15.0
    h = math.sqrt(LEG ** 2 - ((BIG - SMALL) / 2) ** 2)
    f = Fig(180)
    A = (40, 150)
    D = (A[0] + BIG * s, A[1])
    B = (A[0] + (BIG - SMALL) / 2 * s, A[1] - h * s)
    C = (B[0] + SMALL * s, B[1])
    f.poly([A, B, C, D], close=True, w=1.8, fill_op=0.06)
    f.line(B[0], B[1], B[0], A[1], w=1.8, dash='5 3', accent=True)
    f.poly([(B[0], A[1] - 10), (B[0] + 10, A[1] - 10), (B[0] + 10, A[1])], w=1.2)
    f.text(A[0] - 6, A[1] + 5, 'A', size=14, anchor='end', italic=True)
    f.text(B[0] - 6, B[1] - 4, 'B', size=14, anchor='end', italic=True)
    f.text(C[0] + 6, C[1] - 4, 'C', size=14, italic=True)
    f.text(D[0] + 6, D[1] + 5, 'D', size=14, italic=True)
    f.text((A[0] + D[0]) / 2 + 30, A[1] + 18, '16', size=13, anchor='middle')
    f.text((B[0] + C[0]) / 2, B[1] - 8, '4', size=13, anchor='middle')
    f.text((A[0] + B[0]) / 2 - 8, (A[1] + B[1]) / 2, '10', size=13, anchor='end')
    f.text(B[0] + 8, (A[1] + B[1]) / 2 + 5, 'h', size=14, italic=True, accent=True)
    return f, label, caption
