"""Block 11, corollary: a chord is twice the radius times the sine of the inscribed angle."""
import math
from fig import Fig

TEXT = {
    'uk': ('Коло з центром O і радіусом R. Хорда AB виділена, вписаний кут ACB, що на неї спирається, позначено γ. Пунктиром - діаметр, найбільша хорда. Підпис: AB = 2R · sin γ.',
           'Наслідок: хорда дорівнює подвоєному радіусу, помноженому на синус вписаного кута.'),
    'ru': ('Окружность с центром O и радиусом R. Хорда AB выделена, вписанный угол ACB, опирающийся на неё, отмечен γ. Пунктиром - диаметр, наибольшая хорда. Подпись: AB = 2R · sin γ.',
           'Следствие: хорда равна удвоенному радиусу, умноженному на синус вписанного угла.'),
    'en': ('A circle with centre O and radius R. Chord AB is highlighted, and the inscribed angle ACB standing on it is marked γ. Dashed: a diameter, the longest chord. Label: AB = 2R · sin γ.',
           'Corollary: a chord equals twice the radius times the sine of the inscribed angle.'),
}
AT = {'A': 215, 'B': 325, 'C': 95}


def figure(lang):
    label, caption = TEXT[lang]
    O, R = (112, 120), 88
    pt = {k: (O[0] + R * math.cos(math.radians(v)), O[1] - R * math.sin(math.radians(v))) for k, v in AT.items()}
    f = Fig(228)
    f.circle(*O, R, w=1.4, fill_op=0.03)
    f.line(O[0] - R, O[1], O[0] + R, O[1], w=1.2, dash='5 4')
    f.line(*pt['A'], *pt['B'], w=2.4, accent=True)
    f.line(*pt['C'], *pt['A'], w=1.4)
    f.line(*pt['C'], *pt['B'], w=1.4)
    f.line(*O, *pt['B'], w=1.1, op=0.7)
    f.circle(*O, 3, dot=True)
    f.text(O[0] - 4, O[1] - 7, 'O', size=13, anchor='end', italic=True)
    rb = ((O[0] + pt['B'][0]) / 2 + 8, (O[1] + pt['B'][1]) / 2 - 2)
    f.text(*rb, 'R', size=13, italic=True)
    for k in 'ABC':
        x, y = pt[k]
        ux, uy = (x - O[0]) / R, (y - O[1]) / R
        f.text(x + ux * 14, y + uy * 14 + 5, k, size=14, anchor='middle', italic=True)
    f.text(pt['C'][0], pt['C'][1] + 30, 'γ', size=14, anchor='middle', accent=True)
    f.text(206, 70, 'AB = 2R · sin γ', size=13, accent=True)
    return f, label, caption
