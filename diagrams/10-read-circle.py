"""Block 10, reading and linking: a central angle and an inscribed angle, the third angle."""
import math
from fig import Fig

DATA = {'aob': 130, 'cab': 70}
TEXT = {
    'uk': ('Коло з центром O, точки A, B, C на колі, трикутник ABC вписаний. На рисунку позначено центральний кут AOB = 130° (спирається на дугу AB, що не містить C) і кут CAB = 70°. Кут ABC позначено знаком питання.',
           'До задачі: вписаний трикутник, центральний кут і вписаний кут.'),
    'ru': ('Окружность с центром O, точки A, B, C на окружности, треугольник ABC вписан. На рисунке отмечены центральный угол AOB = 130° (опирается на дугу AB, не содержащую C) и угол CAB = 70°. Угол ABC отмечен знаком вопроса.',
           'К задаче: вписанный треугольник, центральный угол и вписанный угол.'),
    'en': ('A circle with centre O, points A, B, C on the circle, triangle ABC inscribed. The figure marks the central angle AOB = 130° (on the arc AB that does not contain C) and the angle CAB = 70°. Angle ABC is marked with a question mark.',
           'For the task: an inscribed triangle, a central angle and an inscribed angle.'),
    'de': ('Ein Kreis mit dem Mittelpunkt O, die Punkte A, B, C auf dem Kreis, das Dreieck ABC einbeschrieben. Auf der Abbildung sind der Mittelpunktswinkel AOB = 130° (über dem Bogen AB, der C nicht enthält) und der Winkel CAB = 70° markiert. Der Winkel ABC ist mit einem Fragezeichen markiert.',
           'Zur Aufgabe: ein einbeschriebenes Dreieck, ein Mittelpunktswinkel und ein Umfangswinkel.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    O, R = (160, 112), 92
    ang = {'A': 200}
    ang['B'] = ang['A'] + DATA['aob']
    ang['C'] = ang['B'] + 2 * DATA['cab']
    pt = {k: (O[0] + R * math.cos(math.radians(v)), O[1] - R * math.sin(math.radians(v))) for k, v in ang.items()}
    f = Fig(228)
    f.circle(*O, R, w=1.4, fill_op=0.03)
    f.poly([pt['A'], pt['B'], pt['C']], close=True, w=1.8)
    f.line(*O, *pt['A'], w=1.3, accent=True)
    f.line(*O, *pt['B'], w=1.3, accent=True)
    f.circle(*O, 3, dot=True)
    f.text(O[0] + 2, O[1] - 8, 'O', size=13, anchor='middle', italic=True)
    f.text(O[0], O[1] + 30, '130°', size=13, anchor='middle', accent=True)
    for k in 'ABC':
        x, y = pt[k]
        ux, uy = (x - O[0]) / R, (y - O[1]) / R
        f.text(x + ux * 14, y + uy * 14 + 5, k, size=14, anchor='middle', italic=True)
    a = pt['A']
    f.text(a[0] + 22, a[1] - 14, '70°', size=13)
    b = pt['B']
    f.text(b[0] - 18, b[1] - 22, '?', size=15, anchor='end', bold=True, accent=True)
    return f, label, caption
