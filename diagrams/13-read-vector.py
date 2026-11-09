"""Block 13, reading and linking: a box on the axes, the coordinates and the length of a vector."""
from fig import Fig
from box import box

DATA = {'a': 6, 'b': 2, 'c': 3}
TEXT = {
    'uk': ('Прямокутний паралелепіпед ABCDA₁B₁C₁D₁, вершина A - початок координат. Вісь x іде вздовж AB, вісь y - вздовж AD, вісь z - вздовж AA₁. На рисунку підписано ребра: AB = 6, AD = 2, AA₁ = 3. Вектор BD₁ виділено.',
           'До задачі: прямокутний паралелепіпед в осях координат і вектор BD₁.'),
    'ru': ('Прямоугольный параллелепипед ABCDA₁B₁C₁D₁, вершина A - начало координат. Ось x идёт вдоль AB, ось y - вдоль AD, ось z - вдоль AA₁. На рисунке подписаны рёбра: AB = 6, AD = 2, AA₁ = 3. Вектор BD₁ выделен.',
           'К задаче: прямоугольный параллелепипед в осях координат и вектор BD₁.'),
    'en': ('Cuboid ABCDA₁B₁C₁D₁, vertex A is the origin. The x-axis runs along AB, the y-axis along AD, the z-axis along AA₁. The figure labels the edges: AB = 6, AD = 2, AA₁ = 3. The vector BD₁ is highlighted.',
           'For the task: a cuboid on coordinate axes and the vector BD₁.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(222)
    v = box(f, DATA['a'], DATA['b'], DATA['c'], A=(40, 182), s=30, depth=1.5, names=False)
    A, B, D, A1, D1 = v['A'], v['B'], v['D'], v['A₁'], v['D₁']
    f.arrow(*B, B[0] + 26, B[1], w=1.1)
    f.text(B[0] + 28, B[1] + 16, 'x', size=13, italic=True, anchor='end')
    f.arrow(*D, D[0] + (D[0] - A[0]) * 0.6, D[1] + (D[1] - A[1]) * 0.6, w=1.1)
    f.text(D[0] + (D[0] - A[0]) * 0.6 + 6, D[1] + (D[1] - A[1]) * 0.6 + 4, 'y', size=13, italic=True)
    f.arrow(*A1, A1[0], A1[1] - 22, w=1.1)
    f.text(A1[0] - 8, A1[1] - 14, 'z', size=13, italic=True, anchor='end')
    f.arrow(*B, *D1, w=2.2, accent=True)
    f.text((A[0] + B[0]) / 2, A[1] + 20, '6', size=13, anchor='middle')
    f.text((A[0] + D[0]) / 2 - 10, (A[1] + D[1]) / 2 + 2, '2', size=13, anchor='end')
    f.text(A[0] - 8, (A[1] + A1[1]) / 2 + 5, '3', size=13, anchor='end')
    for name, dxy in (('A', (-12, 16)), ('B', (4, 18)), ('D', (6, -6)), ('A₁', (-22, -2)), ('D₁', (-6, -10))):
        p = v[name]
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, italic=True)
    return f, label, caption
