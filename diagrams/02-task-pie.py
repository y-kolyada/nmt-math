"""Block 2, task: a pie chart of 40 pupils, the angle of one sector."""
import math
from fig import Fig

DATA = {'uk': (('футбол', 10), ('баскетбол', 14), ('волейбол', 16)),
        'ru': (('футбол', 10), ('баскетбол', 14), ('волейбол', 16)),
        'en': (('football', 10), ('basketball', 14), ('volleyball', 16)),
        'de': (('Fußball', 10), ('Basketball', 14), ('Volleyball', 16))}
TEXT = {
    'uk': ('Кругова діаграма: 40 учнів за улюбленою грою - футбол 10, баскетбол 14, волейбол 16. Сектор баскетболу виділено кольором, його кут позначено знаком питання.',
           'До задачі: кругова діаграма, у якій сектор - частка цілого.'),
    'ru': ('Круговая диаграмма: 40 учеников по любимой игре - футбол 10, баскетбол 14, волейбол 16. Сектор баскетбола выделен цветом, его угол отмечен знаком вопроса.',
           'К задаче: круговая диаграмма, в которой сектор - доля целого.'),
    'en': ('A pie chart: 40 pupils by favourite game - football 10, basketball 14, volleyball 16. The basketball sector is coloured, and its angle is marked with a question mark.',
           'For the task: a pie chart in which a sector is a share of the whole.'),
    'de': ('Ein Kreisdiagramm: 40 Schüler nach ihrem Lieblingsspiel - Fußball 10, Basketball 14, Volleyball 16. Der Sektor Basketball ist farbig, sein Winkel ist mit einem Fragezeichen markiert.',
           'Zur Aufgabe: ein Kreisdiagramm, in dem ein Sektor ein Anteil am Ganzen ist.'),
}


def sector(f, c, r, a1, a2, op, accent=False):
    x1, y1 = c[0] + r * math.cos(math.radians(a1)), c[1] - r * math.sin(math.radians(a1))
    x2, y2 = c[0] + r * math.cos(math.radians(a2)), c[1] - r * math.sin(math.radians(a2))
    big = 1 if a2 - a1 > 180 else 0
    st = ' style="fill:var(--acc)"' if accent else ''
    f.add('<path d="M %.1f %.1f L %.1f %.1f A %.1f %.1f 0 %d 0 %.1f %.1f Z" fill="currentColor" fill-opacity="%s" stroke="currentColor" stroke-width="1.4"%s/>'
          % (c[0], c[1], x1, y1, r, r, big, x2, y2, op, st))


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(190)
    c, r = (88, 95), 78
    total = sum(n for _, n in DATA[lang])
    a = 90.0
    for i, (name, n) in enumerate(DATA[lang]):
        span = n / total * 360
        sector(f, c, r, a, a + span, 0.45 if i == 1 else 0.08 + 0.1 * i, accent=(i == 1))
        if i == 1:
            m = math.radians(a + span / 2)
            f.text(c[0] + 44 * math.cos(m), c[1] - 44 * math.sin(m) + 6, '?', size=16, anchor='middle', bold=True)
        y = 62 + 30 * i
        f.rect(180, y - 11, 12, 12, rx=2, fill_op=0.45 if i == 1 else 0.08 + 0.1 * i, accent=(i == 1))
        f.text(198, y, '%s - %d' % (name, n), size=13)
        a += span
    return f, label, caption
