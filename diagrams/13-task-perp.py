"""Block 13, task: which line is perpendicular to the plane ABCD of a box."""
from fig import Fig

TEXT = {
    'uk': ('Прямокутний паралелепіпед ABCDA₁B₁C₁D₁ у косокутній проєкції: ABCD - нижня основа, A₁B₁C₁D₁ - верхня, AA₁, BB₁, CC₁, DD₁ - бічні ребра. Невидимі ребра - пунктиром.',
           'До задачі: прямокутний паралелепіпед і площина його нижньої основи.'),
    'ru': ('Прямоугольный параллелепипед ABCDA₁B₁C₁D₁ в косоугольной проекции: ABCD - нижнее основание, A₁B₁C₁D₁ - верхнее, AA₁, BB₁, CC₁, DD₁ - боковые рёбра. Невидимые рёбра - пунктиром.',
           'К задаче: прямоугольный параллелепипед и плоскость его нижнего основания.'),
    'en': ('Cuboid ABCDA₁B₁C₁D₁ in oblique projection: ABCD is the lower base, A₁B₁C₁D₁ the upper one, AA₁, BB₁, CC₁, DD₁ are the side edges. Hidden edges are dashed.',
           'For the task: a cuboid and the plane of its lower base.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    a, h, dx, dy = 170, 120, 70, -48
    A = (50, 190)
    B = (A[0] + a, A[1])
    C = (B[0] + dx, B[1] + dy)
    D = (A[0] + dx, A[1] + dy)
    up = lambda p: (p[0], p[1] - h)
    A1, B1, C1, D1 = up(A), up(B), up(C), up(D)
    f.poly([A, B, C, D], close=True, w=0, fill_op=0.1, accent=True)
    for p, q in ((A, D), (D, C), (D, D1)):
        f.line(*p, *q, w=1.3, dash='5 4', op=0.8)
    for p, q in ((A, B), (B, C), (A, A1), (B, B1), (C, C1), (A1, B1), (B1, C1), (C1, D1), (D1, A1)):
        f.line(*p, *q, w=1.8)
    for name, p, dxy in (('A', A, (-14, 14)), ('B', B, (4, 16)), ('C', C, (8, 6)), ('D', D, (-16, -4)),
                         ('A₁', A1, (-22, 0)), ('B₁', B1, (-6, -8)), ('C₁', C1, (8, -2)), ('D₁', D1, (-8, -8))):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, italic=True)
    return f, label, caption
