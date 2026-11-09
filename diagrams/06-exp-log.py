"""Block 06, limits: y = 2^x and y = log₂ x mirror each other in y = x."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Графіки y = 2ˣ і y = log₂ x симетричні відносно прямої y = x. Показникова функція завжди додатна, тому логарифм існує лише для додатних чисел: його графік не заходить ліворуч від осі Oy.',
           'Логарифм - дзеркало степеня: 2ˣ > 0 завжди, тому log₂ x існує лише при x > 0.'),
    'ru': ('Графики y = 2ˣ и y = log₂ x симметричны относительно прямой y = x. Показательная функция всегда положительна, поэтому логарифм существует только для положительных чисел: его график не заходит левее оси Oy.',
           'Логарифм - зеркало степени: 2ˣ > 0 всегда, поэтому log₂ x существует только при x > 0.'),
    'en': ('The graphs y = 2ˣ and y = log₂ x are symmetric about the line y = x. The exponential function is always positive, so the logarithm exists only for positive numbers: its graph never goes to the left of the Oy axis.',
           'The logarithm mirrors the power: 2ˣ > 0 always, so log₂ x exists only for x > 0.'),
    'de': ('Die Graphen y = 2ˣ und y = log₂ x sind symmetrisch zur Geraden y = x. Die Exponentialfunktion ist immer positiv, also existiert der Logarithmus nur für positive Zahlen: sein Graph geht nie links von der Oy-Achse.',
           'Der Logarithmus spiegelt die Potenz: 2ˣ > 0 immer, also existiert log₂ x nur für x > 0.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(250)
    p = Plot(f, 30, 12, 260, 220, -3, 4.5, -3, 4.5)
    p.axes(ticks_x=(1, 2, 4), ticks_y=(1, 2, 4))
    p.curve(lambda x: x, -3, 4.5, w=1, dash='4 3', op=0.6)
    p.curve(lambda x: 2 ** x, -3, 2.17, w=2, accent=True)
    p.curve(lambda x: math.log2(x) if x > 0 else None, 0.13, 4.5, w=2)
    f.text(*p.pt(-2.9, 0.75), 'y = 2ˣ', size=12, accent=True)
    f.text(*p.pt(2.6, 0.55), 'y = log₂ x', size=12)
    f.text(*p.pt(3.3, 3.75), 'y = x', size=12, op=0.7)
    return f, label, caption
