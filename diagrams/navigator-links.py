"""Navigator, lens "links": the graph of the thirteen blocks, drawn from navigator-links.mmd."""
import math
from fig import Fig

NAMES = {
    'uk': {1: 'Число', 2: 'Відсоток', 3: 'Вирази', 4: 'Рівняння', 5: 'Функція', 6: 'Степінь', 7: 'sin, cos',
           8: 'Похідна', 9: 'Лічба', 10: 'Фігури', 11: 'Виміри', 12: 'Вектори', 13: 'Простір'},
    'ru': {1: 'Число', 2: 'Процент', 3: 'Алгебра', 4: 'Корни', 5: 'Функция', 6: 'Степень', 7: 'sin, cos',
           8: 'Скорость', 9: 'Счёт', 10: 'Фигуры', 11: 'Площади', 12: 'Векторы', 13: 'Объёмы'},
    'en': {1: 'Number', 2: 'Percent', 3: 'Algebra', 4: 'Equations', 5: 'Function', 6: 'Power', 7: 'sin, cos', 8: 'Derivative', 9: 'Counting', 10: 'Figures', 11: 'Measure', 12: 'Vectors', 13: 'Space'},
    'de': {1: 'Zahl', 2: 'Prozent', 3: 'Algebra', 4: 'Gleichung', 5: 'Funktion', 6: 'Potenz', 7: 'sin, cos', 8: 'Ableitung', 9: 'Zählen', 10: 'Figuren', 11: 'Messen', 12: 'Vektoren', 13: 'Raum'},
}
TEXT = {
    'uk': ('Граф тринадцяти блоків: стрілка веде від блоку до того, що з нього виростає. Число веде до відсотка, виразів, рівнянь, функції і похідної; вирази і функція - до степеня й логарифма; число - до лічби варіантів. Фігури ведуть до тригонометрії, вимірювань, простору, а вимірювання і рівняння - до координат і векторів.',
           'Як блоки виростають один з одного: алгебра зверху, геометрія знизу.'),
    'ru': ('Граф тринадцати блоков: стрелка ведёт от блока к тому, что из него вырастает. Число ведёт к проценту, выражениям, уравнениям, функции и производной; выражения и функция - к степени и логарифму; число - к счёту вариантов. Фигуры ведут к тригонометрии, измерениям, пространству, а измерения и уравнения - к координатам и векторам.',
           'Как блоки вырастают друг из друга: алгебра сверху, геометрия снизу.'),
    'en': ('A graph of the thirteen blocks: an arrow leads from a block to the one that grows out of it. Number leads to percent, expressions, equations, function and derivative; expressions and function lead to power and logarithm; number leads to counting. Figures lead to trigonometry, measurement and space, and measurement and equations lead to coordinates and vectors.',
           'How the blocks grow out of one another: algebra above, geometry below.'),
    'de': ('Ein Graph der dreizehn Blöcke: ein Pfeil führt von einem Block zu dem, der aus ihm herauswächst. Die Zahl führt zu Prozent, Termen, Gleichungen, Funktion und Ableitung; Terme und Funktion führen zu Potenz und Logarithmus; die Zahl führt zum Zählen. Die Figuren führen zu Trigonometrie, Messen und Raum, und Messen und Gleichungen führen zu Koordinaten und Vektoren.',
           'Wie die Blöcke auseinander herauswachsen: Algebra oben, Geometrie unten.'),
}
# Three columns, so an arrow has room between the boxes: 30 units across and
# 24 down (four columns left 6 and 12, and the head of an arrow did not fit).
# Algebra in rows 0-2, geometry in rows 3-4, with a wider gap between them.
# 4 -> 12 runs down the empty cell under block 4: the equation of a circle is
# an equation of block 4 (lessons/map.md section 5, the lens "links").
POS = {1: (0, 0), 2: (1, 0), 3: (2, 0),
       9: (0, 1), 6: (1, 1), 4: (2, 1),
       8: (0, 2), 5: (1, 2),
       10: (0, 3), 11: (1, 3), 12: (2, 3),
       7: (0, 4), 13: (1, 4)}
EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 8), (3, 6), (5, 6), (1, 9),
         (10, 7), (10, 11), (11, 12), (11, 13), (4, 12)]
BW, BH = 84, 36
STEP_X, STEP_Y, SPLIT = 114, 60, 10
HEIGHT = 8 + 4 * STEP_Y + SPLIT + BH + 8


def corner(n):
    c, r = POS[n]
    return 4 + c * STEP_X, 8 + r * STEP_Y + (SPLIT if r >= 3 else 0)


def centre(n):
    x, y = corner(n)
    return (x + BW / 2, y + BH / 2)


def edge_point(a, b):
    (x1, y1), (x2, y2) = centre(a), centre(b)
    dx, dy = x2 - x1, y2 - y1
    t = min((BW / 2 + 2) / abs(dx) if dx else 9e9, (BH / 2 + 2) / abs(dy) if dy else 9e9)
    return (x1 + dx * t, y1 + dy * t), (x2 - dx * t, y2 - dy * t)


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(HEIGHT)
    for a, b in EDGES:
        p, q = edge_point(a, b)
        f.arrow(*p, *q, w=1.1, head=6)
    for n in POS:
        x, y = corner(n)
        f.rect(x, y, BW, BH, fill_op=0.14 if n >= 10 else 0.05, accent=(n >= 10))
        f.text(x + 6, y + 15, str(n), size=12, bold=True)
        f.text(x + 6, y + 30, NAMES[lang][n], size=12)
    return f, label, caption
