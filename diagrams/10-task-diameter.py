"""Block 10, task: AB is a diameter, angle ABC = 35°, the angle BAC."""
import math
from fig import Fig

TEXT = {
    'uk': ('Коло з центром O і діаметром AB. Точка C лежить на колі, кут ABC дорівнює 35°, кут BAC позначено знаком питання; кут ACB спирається на діаметр.',
           'До задачі: трикутник, вписаний у коло, одна сторона якого - діаметр.'),
    'ru': ('Окружность с центром O и диаметром AB. Точка C лежит на окружности, угол ABC равен 35°, угол BAC отмечен знаком вопроса; угол ACB опирается на диаметр.',
           'К задаче: треугольник, вписанный в окружность, одна сторона которого - диаметр.'),
}
ANG_B = 35


def figure(lang):
    label, caption = TEXT[lang]
    O, R = (160, 110), 92
    A = (O[0] - R, O[1])
    B = (O[0] + R, O[1])
    phi = math.radians(180 - 2 * ANG_B)  # the central angle of C, arc AC = 2 * angle B
    C = (O[0] + R * math.cos(phi), O[1] - R * math.sin(phi))
    f = Fig(214)
    f.circle(*O, R, w=1.4, fill_op=0.04)
    f.poly([A, B, C], close=True, w=1.8)
    f.circle(*O, 3, dot=True)
    # the right angle at C
    u = [(A[0] - C[0]), (A[1] - C[1])]
    v = [(B[0] - C[0]), (B[1] - C[1])]
    nu, nv = math.hypot(*u), math.hypot(*v)
    p1 = (C[0] + u[0] / nu * 11, C[1] + u[1] / nu * 11)
    p3 = (C[0] + v[0] / nv * 11, C[1] + v[1] / nv * 11)
    p2 = (p1[0] + v[0] / nv * 11, p1[1] + v[1] / nv * 11)
    f.poly([p1, p2, p3], w=1.2)
    f.text(A[0] - 6, A[1] + 5, 'A', size=14, anchor='end', italic=True)
    f.text(B[0] + 6, B[1] + 5, 'B', size=14, italic=True)
    f.text(C[0] - 4, C[1] - 8, 'C', size=14, anchor='middle', italic=True)
    f.text(O[0], O[1] + 18, 'O', size=14, anchor='middle', italic=True)
    f.text(B[0] - 34, B[1] - 6, '35°', size=13, anchor='end')
    f.text(A[0] + 30, A[1] - 8, '?', size=15, bold=True, accent=True)
    return f, label, caption
