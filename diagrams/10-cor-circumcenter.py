"""Block 10, corollary: the perpendicular bisectors meet at the circumcenter."""
import math
from fig import Fig

TEXT = {
    'uk': ('Трикутник ABC і серединні перпендикуляри до трьох його сторін, пунктиром. Вони перетинаються в одній точці O - центрі кола, яке проходить через A, B і C.',
           'Наслідок: серединні перпендикуляри до сторін трикутника перетинаються в центрі описаного кола.'),
    'ru': ('Треугольник ABC и серединные перпендикуляры к трём его сторонам, пунктиром. Они пересекаются в одной точке O - центре окружности, которая проходит через A, B и C.',
           'Следствие: серединные перпендикуляры к сторонам треугольника пересекаются в центре описанной окружности.'),
}
A, B, C = (66, 178), (254, 178), (130, 46)


def figure(lang):
    label, caption = TEXT[lang]
    ax, ay = A
    bx, by = B
    cx, cy = C
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ox = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    oy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    R = math.hypot(ax - ox, ay - oy)
    f = Fig(int(oy + R + 14) if oy + R + 14 > 190 else 190)
    f.circle(ox, oy, R, w=1.2, fill_op=0.03, dash='4 4')
    f.poly([A, B, C], close=True, w=1.8)
    for p, q in ((A, B), (B, C), (C, A)):
        m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        ux, uy = ox - m[0], oy - m[1]
        n = math.hypot(ux, uy) or 1
        # along the perpendicular, from beyond the side to beyond O
        nx, ny = -(q[1] - p[1]), q[0] - p[0]
        k = math.hypot(nx, ny)
        nx, ny = nx / k, ny / k
        if nx * ux + ny * uy < 0:
            nx, ny = -nx, -ny
        f.line(m[0] - nx * 14, m[1] - ny * 14, m[0] + nx * (n + 18), m[1] + ny * (n + 18), w=1.3, dash='5 4', accent=True)
        f.circle(*m, 3, dot=True)
    f.circle(ox, oy, 3.5, dot=True, accent=True)
    f.text(ox + 10, oy + 5, 'O', size=14, italic=True, accent=True)
    for name, p, dxy, anc in (('A', A, (-6, 14), 'end'), ('B', B, (6, 14), 'start'), ('C', C, (0, -10), 'middle')):
        f.text(p[0] + dxy[0], p[1] + dxy[1], name, size=14, anchor=anc, italic=True)
    return f, label, caption
