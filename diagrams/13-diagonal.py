"""Block 13, why: the diagonal of a box is Pythagoras applied twice."""
from fig import Fig

TEXT = {
    'uk': ('Прямокутний паралелепіпед з ребрами a, b, c. Пунктиром - діагональ основи √(a² + b²). Вона разом з бічним ребром c утворює прямокутний трикутник, гіпотенуза якого - діагональ паралелепіпеда d, тому d² = a² + b² + c².',
           'Діагональ паралелепіпеда: Піфагор двічі, d² = a² + b² + c².'),
    'ru': ('Прямоугольный параллелепипед с рёбрами a, b, c. Пунктиром - диагональ основания √(a² + b²). Она вместе с боковым ребром c образует прямоугольный треугольник, гипотенуза которого - диагональ параллелепипеда d, поэтому d² = a² + b² + c².',
           'Диагональ параллелепипеда: Пифагор дважды, d² = a² + b² + c².'),
    'en': ('A cuboid with edges a, b, c. Dashed: the diagonal of the base, √(a² + b²). Together with the side edge c it forms a right triangle whose hypotenuse is the diagonal of the cuboid d, so d² = a² + b² + c².',
           'The diagonal of a cuboid: Pythagoras twice, d² = a² + b² + c².'),
    'de': ('Ein Quader mit den Kanten a, b, c. Gestrichelt: die Diagonale der Grundfläche, √(a² + b²). Zusammen mit der Seitenkante c bildet sie ein rechtwinkliges Dreieck, dessen Hypotenuse die Raumdiagonale d ist, also d² = a² + b² + c².',
           'Die Raumdiagonale eines Quaders: zweimal Pythagoras, d² = a² + b² + c².'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(200)
    a, b, c = 150, 90, 100
    ox, oy, k = 40, 176, 0.5

    def P(x, y, z):  # x along a, y up (c), z depth (b)
        return (ox + x + z * k, oy - y - z * k * 0.7)
    V = {n: P(*v) for n, v in {
        'A': (0, 0, 0), 'B': (a, 0, 0), 'C': (a, 0, b), 'D': (0, 0, b),
        'E': (0, c, 0), 'F': (a, c, 0), 'G': (a, c, b), 'H': (0, c, b)}.items()}
    for u, v in (('A', 'B'), ('B', 'F'), ('F', 'E'), ('E', 'A'), ('B', 'C'), ('C', 'G'), ('G', 'F'), ('E', 'H'), ('H', 'G')):
        f.line(*V[u], *V[v], w=1.4)
    for u, v in (('A', 'D'), ('D', 'C'), ('D', 'H')):
        f.line(*V[u], *V[v], w=1, dash='3 3', op=0.6)
    f.line(*V['A'], *V['C'], w=1.6, dash='5 3', accent=True)
    f.line(*V['A'], *V['G'], w=2.4, accent=True)
    f.text((V['A'][0] + V['B'][0]) / 2, V['A'][1] + 18, 'a', size=14, anchor='middle', italic=True)
    f.text((V['B'][0] + V['C'][0]) / 2 + 10, (V['B'][1] + V['C'][1]) / 2 + 12, 'b', size=14, italic=True)
    f.text(V['C'][0] + 8, (V['C'][1] + V['G'][1]) / 2, 'c', size=14, italic=True)
    f.text((V['A'][0] + V['G'][0]) / 2 - 6, (V['A'][1] + V['G'][1]) / 2 - 6, 'd', size=15, anchor='end', italic=True, bold=True, accent=True)
    return f, label, caption
