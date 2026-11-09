"""Block 9, task: a spinner of 8 equal sectors numbered 1 to 8, the chance of a prime."""
import math
from fig import Fig

TEXT = {
    'uk': ('Круг-рулетка, поділений на 8 однакових секторів з номерами від 1 до 8. Стрілка в центрі зупиняється навмання на одному із секторів.',
           'До задачі: рулетка з восьми рівних секторів.'),
    'ru': ('Круг-рулетка, разделённый на 8 одинаковых секторов с номерами от 1 до 8. Стрелка в центре останавливается наугад на одном из секторов.',
           'К задаче: рулетка из восьми равных секторов.'),
    'en': ('A spinner divided into 8 equal sectors numbered 1 to 8. The arrow in the centre stops at random on one of the sectors.',
           'For the task: a spinner of eight equal sectors.'),
    'de': ('Ein Glücksrad, in 8 gleiche Sektoren mit den Nummern 1 bis 8 geteilt. Der Pfeil in der Mitte bleibt zufällig auf einem der Sektoren stehen.',
           'Zur Aufgabe: ein Glücksrad aus acht gleichen Sektoren.'),
}
N = 8


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(210)
    c, r = (160, 105), 92
    f.circle(*c, r, w=1.8, fill_op=0.05)
    for k in range(N):
        a = math.radians(90 - 360 / N * k)
        f.line(c[0], c[1], c[0] + r * math.cos(a), c[1] - r * math.sin(a), w=1.2)
        m = math.radians(90 - 360 / N * (k + 0.5))
        f.text(c[0] + 66 * math.cos(m), c[1] - 66 * math.sin(m) + 5, str(k + 1), size=15, anchor='middle', bold=True)
    tip = math.radians(90 - 360 / N * 2.3)
    f.arrow(c[0], c[1], c[0] + 44 * math.cos(tip), c[1] - 44 * math.sin(tip), w=2.6, accent=True, head=9)
    f.circle(*c, 5, dot=True, accent=True)
    return f, label, caption
