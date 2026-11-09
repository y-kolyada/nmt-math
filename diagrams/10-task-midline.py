"""Block 10, task: triangle with sides 8, 10 and 12, the triangle of its midlines."""
import math
from fig import Fig

TEXT = {
    'uk': ('Трикутник ABC зі сторонами AB = 8, BC = 10, AC = 12. Точки M, N і K - середини сторін AB, BC і AC; трикутник MNK виділено кольором.',
           'До задачі: трикутник, вершини якого - середини сторін трикутника ABC.'),
    'ru': ('Треугольник ABC со сторонами AB = 8, BC = 10, AC = 12. Точки M, N и K - середины сторон AB, BC и AC; треугольник MNK выделен цветом.',
           'К задаче: треугольник, вершины которого - середины сторон треугольника ABC.'),
    'en': ('Triangle ABC with sides AB = 8, BC = 10, AC = 12. The points M, N and K are the midpoints of AB, BC and AC; triangle MNK is coloured.',
           'For the task: a triangle whose vertices are the midpoints of the sides of triangle ABC.'),
}
AB, BC, AC = 8, 10, 12


def figure(lang):
    label, caption = TEXT[lang]
    s = 21.0
    bx = (AB ** 2 - BC ** 2 + AC ** 2) / (2 * AC)
    by = math.sqrt(AB ** 2 - bx ** 2)
    A = (34, 170)
    C = (A[0] + AC * s, A[1])
    B = (A[0] + bx * s, A[1] - by * s)
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    M, N, K = mid(A, B), mid(B, C), mid(A, C)
    f = Fig(196)
    f.poly([A, B, C], close=True, w=1.8, fill_op=0.05)
    f.poly([M, N, K], close=True, w=1.8, fill_op=0.2, accent=True)
    f.text(A[0] - 6, A[1] + 5, 'A', size=14, anchor='end', italic=True)
    f.text(B[0], B[1] - 8, 'B', size=14, anchor='middle', italic=True)
    f.text(C[0] + 6, C[1] + 5, 'C', size=14, italic=True)
    f.text(M[0] - 8, M[1], 'M', size=14, anchor='end', italic=True)
    f.text(N[0] + 8, N[1], 'N', size=14, italic=True)
    f.text(K[0], K[1] + 18, 'K', size=14, anchor='middle', italic=True)
    f.text((A[0] + M[0]) / 2 - 8, (A[1] + M[1]) / 2 + 4, '8', size=13, anchor='end')
    f.text((N[0] + C[0]) / 2 + 8, (N[1] + C[1]) / 2 + 4, '10', size=13)
    f.text((A[0] + K[0]) / 2, A[1] + 18, '12', size=13, anchor='middle')
    return f, label, caption
