"""Block 10, task: triangle with angles A = 50° and B = 70°, the exterior angle at C."""
import math
from fig import Fig

TEXT = {
    'uk': ('Трикутник ABC з кутами A = 50° і B = 70°. Сторону AC продовжено за вершину C; зовнішній кут при вершині C, між продовженням і стороною CB, позначено знаком питання.',
           'До задачі: зовнішній кут трикутника при вершині C.'),
    'ru': ('Треугольник ABC с углами A = 50° и B = 70°. Сторона AC продолжена за вершину C; внешний угол при вершине C, между продолжением и стороной CB, отмечен знаком вопроса.',
           'К задаче: внешний угол треугольника при вершине C.'),
    'en': ('Triangle ABC with angles A = 50° and B = 70°. Side AC is extended beyond vertex C; the exterior angle at vertex C, between the extension and side CB, is marked with a question mark.',
           'For the task: the exterior angle of a triangle at vertex C.'),
    'de': ('Das Dreieck ABC mit den Winkeln A = 50° und B = 70°. Die Seite AC ist über die Ecke C hinaus verlängert; der Außenwinkel an der Ecke C, zwischen der Verlängerung und der Seite CB, ist mit einem Fragezeichen markiert.',
           'Zur Aufgabe: der Außenwinkel eines Dreiecks an der Ecke C.'),
}
ANG_A, ANG_B = 50, 70


def arc(f, c, r, a1, a2, accent=False):
    """Arc of radius r around c from angle a1 to a2 (degrees, counter-clockwise on screen up)."""
    x1, y1 = c[0] + r * math.cos(math.radians(a1)), c[1] - r * math.sin(math.radians(a1))
    x2, y2 = c[0] + r * math.cos(math.radians(a2)), c[1] - r * math.sin(math.radians(a2))
    st = ' style="stroke:var(--acc)"' if accent else ''
    f.add('<path d="M %.1f %.1f A %.1f %.1f 0 0 0 %.1f %.1f" fill="none" stroke="currentColor" stroke-width="1.4"%s/>' % (x1, y1, r, r, x2, y2, st))


def figure(lang):
    label, caption = TEXT[lang]
    ang_c = 180 - ANG_A - ANG_B
    sa, sb, sc = (math.sin(math.radians(a)) for a in (ANG_A, ANG_B, ang_c))
    k = 200 / sb  # AC = b is drawn 200 units long
    A = (24, 166)
    C = (A[0] + sb * k, A[1])
    B = (A[0] + sc * k * math.cos(math.radians(ANG_A)), A[1] - sc * k * math.sin(math.radians(ANG_A)))
    f = Fig(190)
    f.poly([A, B, C], close=True, w=1.8, fill_op=0.05)
    f.line(C[0], C[1], 300, C[1], w=1.8)
    arc(f, A, 26, 0, ANG_A)
    ext = 180 - ang_c  # direction of CB seen from C
    arc(f, C, 22, 0, ext, accent=True)
    f.text(A[0] - 2, A[1] + 18, 'A', size=14, italic=True)
    f.text(B[0], B[1] - 8, 'B', size=14, anchor='middle', italic=True)
    f.text(C[0] - 4, C[1] + 18, 'C', size=14, anchor='middle', italic=True)
    f.text(A[0] + 32, A[1] - 8, '50°', size=13)
    bdir = math.atan2(A[1] - B[1], A[0] - B[0]) + math.atan2(C[1] - B[1], C[0] - B[0])
    f.text(B[0] + 22 * math.cos(bdir / 2), B[1] + 22 * math.sin(bdir / 2) + 10, '70°', size=13, anchor='middle')
    mid = math.radians(ext / 2)
    f.text(C[0] + 38 * math.cos(mid), C[1] - 38 * math.sin(mid) + 5, '?', size=15, anchor='middle', bold=True, accent=True)
    return f, label, caption
