"""Block 11, task: right triangle with legs 15 and 20, the height to the hypotenuse."""
from fig import Fig

TEXT = {
    'uk': ('Прямокутний трикутник ABC з прямим кутом C: катет AC = 15 вертикальний, катет BC = 20 горизонтальний. З вершини C до гіпотенузи AB проведено висоту CH, позначену h.',
           'До задачі: висота CH прямокутного трикутника, проведена до гіпотенузи.'),
    'ru': ('Прямоугольный треугольник ABC с прямым углом C: катет AC = 15 вертикальный, катет BC = 20 горизонтальный. Из вершины C к гипотенузе AB проведена высота CH, обозначенная h.',
           'К задаче: высота CH прямоугольного треугольника, проведённая к гипотенузе.'),
    'en': ('Right triangle ABC with the right angle at C: leg AC = 15 is vertical, leg BC = 20 is horizontal. From vertex C the height CH, marked h, is drawn to the hypotenuse AB.',
           'For the task: the height CH of a right triangle, drawn to the hypotenuse.'),
}
AC, BC = 15, 20


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(200)
    s = 9.0
    C = (70, 170)
    A = (C[0], C[1] - AC * s)
    B = (C[0] + BC * s, C[1])
    # the foot of the height: projection of C onto AB
    ux, uy = B[0] - A[0], B[1] - A[1]
    t = ((C[0] - A[0]) * ux + (C[1] - A[1]) * uy) / (ux * ux + uy * uy)
    H = (A[0] + t * ux, A[1] + t * uy)
    f.poly([A, B, C], close=True, w=1.8, fill_op=0.06)
    f.line(*C, *H, w=1.8, dash='5 3', accent=True)
    f.poly([(C[0], C[1] - 12), (C[0] + 12, C[1] - 12), (C[0] + 12, C[1])], w=1.2)
    f.text(A[0] - 8, A[1] + 4, 'A', size=14, anchor='end', italic=True)
    f.text(B[0] + 6, B[1] + 5, 'B', size=14, italic=True)
    f.text(C[0] - 8, C[1] + 14, 'C', size=14, anchor='end', italic=True)
    f.text(H[0] + 6, H[1] - 6, 'H', size=14, italic=True)
    f.text(C[0] - 10, (A[1] + C[1]) / 2 + 5, '15', size=13, anchor='end')
    f.text((C[0] + B[0]) / 2, C[1] + 18, '20', size=13, anchor='middle')
    f.text((C[0] + H[0]) / 2 + 8, (C[1] + H[1]) / 2 + 14, 'h', size=14, italic=True, accent=True)
    return f, label, caption
