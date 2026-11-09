"""Block 13, hook: a cube with a doubled edge holds 2 · 2 · 2 = 8 unit cubes."""
from fig import Fig

TEXT = {
    'uk': ('Ліворуч одиничний кубик. Праворуч куб з ребром 2, складений з восьми таких кубиків: два шари по чотири. Ребро подвоїлося, об\'єм зріс у 8 разів.',
           'Ребро вдвічі - об\'єм у 2³ = 8 разів.', 'V = 1', 'V = 8'),
    'ru': ('Слева единичный кубик. Справа куб с ребром 2, сложенный из восьми таких кубиков: два слоя по четыре. Ребро удвоилось, объём вырос в 8 раз.',
           'Ребро вдвое - объём в 2³ = 8 раз.', 'V = 1', 'V = 8'),
    'en': ('On the left, a unit cube. On the right, a cube with edge 2, made of eight such cubes: two layers of four. The edge doubled, the volume grew 8 times.',
           'Twice the edge - 2³ = 8 times the volume.',
           'V = 1',
           'V = 8'),
}

DX, DY = 0.5, 0.35  # oblique projection of the depth axis


def cube(f, x, y, z, s, ox, oy, accent=False):
    def P(a, b, c):
        return (ox + (a + c * DX) * s, oy - (b + c * DY) * s)
    front = [P(x, y, z), P(x + 1, y, z), P(x + 1, y + 1, z), P(x, y + 1, z)]
    top = [P(x, y + 1, z), P(x + 1, y + 1, z), P(x + 1, y + 1, z + 1), P(x, y + 1, z + 1)]
    side = [P(x + 1, y, z), P(x + 1, y, z + 1), P(x + 1, y + 1, z + 1), P(x + 1, y + 1, z)]
    for face, tone in ((side, 0.22), (top, 0.12), (front, 0.06)):
        # An opaque base in the page colour first: edges behind must not show through.
        f.add('<polygon points="%s" style="fill:var(--bg)" stroke="none"/>' % ' '.join('%.1f,%.1f' % q for q in face))
        f.poly(face, close=True, w=1, fill_op=tone, accent=accent)


def figure(lang):
    label, caption, v1, v8 = TEXT[lang]
    f = Fig(190)
    cube(f, 0, 0, 0, 40, 30, 130, accent=True)
    f.text(60, 160, v1, size=13, anchor='middle')
    order = [(x, y, z) for z in (1, 0) for y in (0, 1) for x in (0, 1)]
    for (x, y, z) in order:
        cube(f, x, y, z, 40, 150, 150)
    f.text(210, 178, v8, size=13, anchor='middle')
    return f, label, caption
