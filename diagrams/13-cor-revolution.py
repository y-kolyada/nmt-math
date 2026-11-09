"""Block 13, corollary: a cone is a right triangle turned about a leg."""
from fig import Fig

TEXT = {
    'uk': ('Конус. Прямокутний трикутник виділено: його катет h лежить на осі обертання, пунктиром; другий катет r - радіус основи; гіпотенуза l - твірна конуса. Обертання трикутника навколо h дає конус.',
           'Наслідок: конус утворюється обертанням прямокутного трикутника навколо катета; гіпотенуза стає твірною.'),
    'ru': ('Конус. Прямоугольный треугольник выделен: его катет h лежит на оси вращения, пунктиром; второй катет r - радиус основания; гипотенуза l - образующая конуса. Вращение треугольника вокруг h даёт конус.',
           'Следствие: конус образуется вращением прямоугольного треугольника вокруг катета; гипотенуза становится образующей.'),
    'en': ('A cone. A right triangle is highlighted: its leg h lies on the axis of rotation, dashed; the other leg r is the radius of the base; the hypotenuse l is the slant height of the cone. Rotating the triangle about h gives the cone.',
           'Corollary: a cone is formed by rotating a right triangle about a leg; the hypotenuse becomes the slant height.'),
    'de': ('Ein Kegel. Ein rechtwinkliges Dreieck ist hervorgehoben: seine Kathete h liegt auf der Drehachse, gestrichelt; die andere Kathete r ist der Radius der Grundfläche; die Hypotenuse l ist die Mantellinie des Kegels. Dreht man das Dreieck um h, entsteht der Kegel.',
           'Folgerung: ein Kegel entsteht durch Drehung eines rechtwinkligen Dreiecks um eine Kathete; die Hypotenuse wird zur Mantellinie.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    S = (160, 24)
    O = (160, 176)
    rx, ry = 96, 24
    L, Rr = (O[0] - rx, O[1]), (O[0] + rx, O[1])
    f.add('<path d="M %.1f %.1f A %d %d 0 0 1 %.1f %.1f" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="5 4" opacity="0.8"/>'
          % (L[0], L[1], rx, ry, Rr[0], Rr[1]))
    f.add('<path d="M %.1f %.1f A %d %d 0 0 0 %.1f %.1f" fill="none" stroke="currentColor" stroke-width="1.6"/>'
          % (L[0], L[1], rx, ry, Rr[0], Rr[1]))
    f.line(*S, *L, w=1.6)
    f.poly([S, O, Rr], close=True, w=2.2, fill_op=0.12, accent=True)
    f.line(S[0], S[1] - 8, O[0], O[1] + 30, w=1.1, dash='3 4', op=0.8)
    f.poly([(O[0], O[1] - 10), (O[0] + 10, O[1] - 10), (O[0] + 10, O[1])], w=1)
    f.text(O[0] - 8, (S[1] + O[1]) / 2 + 5, 'h', size=14, anchor='end', italic=True)
    f.text((O[0] + Rr[0]) / 2, O[1] - 6, 'r', size=14, anchor='middle', italic=True)
    f.text((S[0] + Rr[0]) / 2 + 10, (S[1] + Rr[1]) / 2, 'l', size=14, italic=True, accent=True)
    return f, label, caption
