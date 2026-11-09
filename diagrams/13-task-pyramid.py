"""Block 13, task: regular quadrilateral pyramid with base side 6 and height 4, its volume."""
from fig import Fig

TEXT = {
    'uk': ('Правильна чотирикутна піраміда SABCD: в основі квадрат ABCD зі стороною 6, вершина S стоїть над центром O квадрата, висота SO = 4. Невидимі ребра - пунктиром.',
           'До задачі: правильна чотирикутна піраміда і її висота.'),
    'ru': ('Правильная четырёхугольная пирамида SABCD: в основании квадрат ABCD со стороной 6, вершина S стоит над центром O квадрата, высота SO = 4. Невидимые рёбра - пунктиром.',
           'К задаче: правильная четырёхугольная пирамида и её высота.'),
    'en': ('A regular square pyramid SABCD: the base is the square ABCD with side 6, the apex S stands above the centre O of the square, height SO = 4. Hidden edges are dashed.',
           'For the task: a regular square pyramid and its height.'),
    'de': ('Eine regelmäßige quadratische Pyramide SABCD: die Grundfläche ist das Quadrat ABCD mit der Seite 6, die Spitze S steht über dem Mittelpunkt O des Quadrats, Höhe SO = 4. Verdeckte Kanten sind gestrichelt.',
           'Zur Aufgabe: eine regelmäßige quadratische Pyramide und ihre Höhe.'),
}
SIDE, HEIGHT = 6, 4


def figure(lang):
    label, caption = TEXT[lang]
    s = 28.0
    f = Fig(230)
    dx, dy = 0.5 * SIDE * s * 0.7, -0.5 * SIDE * s * 0.5
    A = (60, 200)
    B = (A[0] + SIDE * s, A[1])
    C = (B[0] + dx, B[1] + dy)
    D = (A[0] + dx, A[1] + dy)
    O = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    S = (O[0], O[1] - HEIGHT * s)
    for p, q in ((A, D), (D, C), (D, S), (A, C), (B, D)):
        f.line(*p, *q, w=1.2, dash='5 4', op=0.7)
    for p, q in ((A, B), (B, C), (S, A), (S, B), (S, C)):
        f.line(*p, *q, w=1.8)
    f.line(*S, *O, w=2, dash='5 3', accent=True)
    f.circle(*O, 3, dot=True)
    for name, p, dxy in (('A', A, (-14, 12)), ('B', B, (4, 14)), ('C', C, (8, 4)), ('D', D, (-16, -2)),
                         ('S', S, (-4, -8)), ('O', O, (6, 14))):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, italic=True)
    f.text((A[0] + B[0]) / 2, A[1] + 18, '6', size=13, anchor='middle')
    f.text(S[0] + 8, (S[1] + O[1]) / 2, '4', size=13, accent=True)
    return f, label, caption
