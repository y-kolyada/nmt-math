"""Block 11, task: a quadrilateral circumscribed about a circle, AB = 7, BC = 9, CD = 12.

The drawing is exact: the tangent segments from the vertices are 3, 4, 5 and 7
(AB = 3 + 4, BC = 4 + 5, CD = 5 + 7, DA = 7 + 3 = 10), and the radius is the
one for which the four central angles close the full turn.
"""
import math
from fig import Fig

TEXT = {
    'uk': ('Чотирикутник ABCD, описаний навколо кола: кожна сторона дотикається до кола. Підписано сторони AB = 7, BC = 9, CD = 12; сторона AD позначена знаком питання.',
           'До задачі: чотирикутник, описаний навколо кола.'),
    'ru': ('Четырёхугольник ABCD, описанный около окружности: каждая сторона касается окружности. Подписаны стороны AB = 7, BC = 9, CD = 12; сторона AD отмечена знаком вопроса.',
           'К задаче: четырёхугольник, описанный около окружности.'),
    'en': ('Quadrilateral ABCD circumscribed about a circle: each side touches the circle. The sides AB = 7, BC = 9, CD = 12 are labelled; side AD is marked with a question mark.',
           'For the task: a quadrilateral circumscribed about a circle.'),
    'de': ('Das Viereck ABCD ist einem Kreis umbeschrieben: jede Seite berührt den Kreis. Die Seiten AB = 7, BC = 9, CD = 12 sind beschriftet; die Seite AD ist mit einem Fragezeichen markiert.',
           'Zur Aufgabe: ein einem Kreis umbeschriebenes Viereck.'),
}
T = (3, 4, 5, 7)  # tangent segments from A, B, C, D


def radius():
    lo, hi = 0.1, 50.0
    for _ in range(80):
        r = (lo + hi) / 2
        if sum(math.atan(t / r) for t in T) > math.pi:
            lo = r
        else:
            hi = r
    return r


def figure(lang):
    label, caption = TEXT[lang]
    r = radius()
    pts, ang = [], math.pi * 0.95
    for t in T:
        half = math.atan(t / r)
        mid = ang + half
        d = math.hypot(r, t)
        pts.append((d * math.cos(mid), d * math.sin(mid)))
        ang += 2 * half
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    s = min(250 / (max(xs) - min(xs)), 190 / (max(ys) - min(ys)))
    ox = 160 - (max(xs) + min(xs)) / 2 * s
    oy = 115 + (max(ys) + min(ys)) / 2 * s
    P = [(ox + x * s, oy - y * s) for x, y in pts]
    O = (ox, oy)
    f = Fig(230)
    f.circle(*O, r * s, w=1.4, fill_op=0.06, accent=True)
    f.poly(P, close=True, w=1.8)
    for name, p in zip('ABCD', P):
        dx, dy = p[0] - O[0], p[1] - O[1]
        k = 14 / math.hypot(dx, dy)
        f.text(p[0] + dx * k, p[1] + dy * k + 5, name, size=14, anchor='middle', italic=True)
    for (i, j), txt in zip(((0, 1), (1, 2), (2, 3), (3, 0)), ('7', '9', '12', '?')):
        mx, my = (P[i][0] + P[j][0]) / 2, (P[i][1] + P[j][1]) / 2
        dx, dy = mx - O[0], my - O[1]
        k = 14 / math.hypot(dx, dy)
        f.text(mx + dx * k, my + dy * k + 5, txt, size=13, anchor='middle', bold=(txt == '?'))
    return f, label, caption
