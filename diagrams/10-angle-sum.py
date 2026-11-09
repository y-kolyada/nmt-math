"""Block 10, why: a line through B parallel to AC shows the angle sum of a triangle."""
from fig import Fig

TEXT = {
    'uk': ('Трикутник ABC і пряма через вершину B, паралельна стороні AC. Кути при B, утворені цією прямою, дорівнюють кутам A і C як внутрішні різносторонні. Три кути при B разом складають розгорнутий кут 180°.',
           'Сума кутів трикутника: три кути при вершині B складають пряму лінію.'),
    'ru': ('Треугольник ABC и прямая через вершину B, параллельная стороне AC. Углы при B, образованные этой прямой, равны углам A и C как внутренние накрест лежащие. Три угла при B вместе составляют развёрнутый угол 180°.',
           'Сумма углов треугольника: три угла при вершине B составляют прямую линию.'),
    'en': ('Triangle ABC and a line through vertex B parallel to side AC. The angles at B formed by this line are equal to angles A and C as alternate angles. The three angles at B together make a straight angle, 180°.',
           'The angle sum of a triangle: the three angles at vertex B make a straight line.'),
    'de': ('Das Dreieck ABC und eine Gerade durch die Ecke B parallel zur Seite AC. Die Winkel bei B, die diese Gerade bildet, sind als Wechselwinkel gleich den Winkeln A und C. Die drei Winkel bei B ergeben zusammen einen gestreckten Winkel, 180°.',
           'Die Winkelsumme im Dreieck: die drei Winkel an der Ecke B bilden eine Gerade.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(180)
    A, B, C = (40, 150), (130, 40), (290, 150)
    f.poly([A, B, C], close=True, w=1.8, fill_op=0.05)
    f.line(14, 40, 306, 40, w=1.4, accent=True)
    f.text(A[0] - 6, A[1] + 18, 'A', size=14, anchor='middle', bold=True)
    f.text(B[0], B[1] - 10, 'B', size=14, anchor='middle', bold=True)
    f.text(C[0] + 2, C[1] + 18, 'C', size=14, anchor='middle', bold=True)
    f.text(A[0] + 26, A[1] - 6, '1', size=13, accent=True, bold=True)
    f.text(C[0] - 34, C[1] - 6, '3', size=13, accent=True, bold=True)
    f.text(B[0] - 34, B[1] + 16, '1', size=13, accent=True, bold=True)
    f.text(B[0] + 22, B[1] + 16, '3', size=13, accent=True, bold=True)
    f.text(B[0] - 2, B[1] + 30, '2', size=13, bold=True)
    return f, label, caption
