"""Block 12, task: parallelogram ABCD with A(1; 1), B(4; 2), C(5; 5), the vertex D."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Координатна площина з вершинами паралелограма A(1; 1), B(4; 2), C(5; 5). Четверту вершину D позначено без координат; сторони CD і DA - пунктиром.',
           'До задачі: паралелограм ABCD, у якого невідома вершина D.'),
    'ru': ('Координатная плоскость с вершинами параллелограмма A(1; 1), B(4; 2), C(5; 5). Четвёртая вершина D отмечена без координат; стороны CD и DA - пунктиром.',
           'К задаче: параллелограмм ABCD, у которого неизвестна вершина D.'),
    'en': ('A coordinate plane with the vertices of a parallelogram A(1; 1), B(4; 2), C(5; 5). The fourth vertex D is marked without coordinates; the sides CD and DA are dashed.',
           'For the task: parallelogram ABCD with an unknown vertex D.'),
}
A, B, C = (1, 1), (4, 2), (5, 5)


def figure(lang):
    label, caption = TEXT[lang]
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    f = Fig(220)
    p = Plot(f, 24, 10, 270, 192, -0.5, 6.5, -0.5, 6.2)
    p.axes(ticks_x=(1, 4, 5), ticks_y=(1, 2, 5))
    f.poly([p.pt(*D), p.pt(*A), p.pt(*B), p.pt(*C)], w=2)
    f.poly([p.pt(*C), p.pt(*D), p.pt(*A)], w=2, dash='6 4', accent=True)
    for name, q, dxy in (('A(1; 1)', A, (6, 16)), ('B(4; 2)', B, (8, 14)), ('C(5; 5)', C, (-10, -10)), ('D', D, (-16, -6))):
        f.circle(*p.pt(*q), 4, dot=True, accent=(name == 'D'))
        f.text(p.px(q[0]) + dxy[0], p.py(q[1]) + dxy[1], name, size=13, anchor='end' if name.startswith('C') else 'start', bold=(name == 'D'))
    return f, label, caption
