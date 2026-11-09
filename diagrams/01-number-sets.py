"""Block 01, concept: nested number sets, drawn from 01-number-sets.mmd."""
from fig import Fig

TEXT = {
    'uk': (['ℝ дійсні: додано √2, π', 'ℚ раціональні: дроби p/q', 'ℤ цілі: нуль і від\'ємні', 'ℕ натуральні: 1, 2, 3, …'],
           ['дозволив корінь', 'дозволило ділення', 'дозволило віднімання'],
           'Вкладені множини чисел: натуральні всередині цілих, цілі всередині раціональних, раціональні всередині дійсних. Кожне розширення дозволило дію, якої не було: віднімання, ділення, добування кореня.',
           'Кожна множина чисел лежить усередині наступної, і кожне розширення з\'явилося заради нової дії.'),
    'ru': (['ℝ действительные: + √2, π', 'ℚ рациональные: дроби p/q', 'ℤ целые: ноль и отрицательные', 'ℕ натуральные: 1, 2, 3, …'],
           ['позволил корень', 'позволило деление', 'позволило вычитание'],
           'Вложенные множества чисел: натуральные внутри целых, целые внутри рациональных, рациональные внутри действительных. Каждое расширение позволило действие, которого не было: вычитание, деление, извлечение корня.',
           'Каждое множество чисел лежит внутри следующего, и каждое расширение появилось ради нового действия.'),
    'en': (['ℝ real: √2, π added', 'ℚ rational: fractions p/q', 'ℤ integers: zero and negatives', 'ℕ natural: 1, 2, 3, …'],
           ['allowed roots', 'allowed division', 'allowed subtraction'],
           'Nested sets of numbers: natural numbers inside the integers, integers inside the rationals, rationals inside the reals. Each extension allowed an operation that was not there before: subtraction, division, taking a root.',
           'Each set of numbers lies inside the next one, and each extension came for the sake of a new operation.'),
}


def figure(lang):
    names, why, label, caption = TEXT[lang]
    f = Fig(214)
    boxes = [(4, 4, 312, 206), (16, 50, 288, 156), (28, 96, 264, 106), (40, 142, 240, 56)]
    for i, (x, y, w, h) in enumerate(boxes):
        f.rect(x, y, w, h, fill_op=0.035, accent=(i == 3))
        f.text(x + 10, y + 20, names[i], size=13, bold=(i == 3))
        if i < 3:
            f.text(x + 10, y + 38, why[i], size=12, op=0.7, italic=True)
    return f, label, caption
