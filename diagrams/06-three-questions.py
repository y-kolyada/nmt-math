"""Block 06, concept: one equality 2³ = 8 and three questions to it (from 06-three-questions.mmd)."""
from fig import Fig

TEXT = {
    'uk': ('У центрі рівність 2³ = 8. Три стрілки ведуть до трьох запитань: невідомий результат - степінь, невідома основа - корінь, невідомий показник - логарифм.',
           'Одна рівність, три запитання: степінь, корінь, логарифм.',
           ['степінь', 'корінь', 'логарифм'], ['шукаємо 8', 'шукаємо 2', 'шукаємо 3']),
    'ru': ('В центре равенство 2³ = 8. Три стрелки ведут к трём вопросам: неизвестный результат - степень, неизвестное основание - корень, неизвестный показатель - логарифм.',
           'Одно равенство, три вопроса: степень, корень, логарифм.',
           ['степень', 'корень', 'логарифм'], ['ищем 8', 'ищем 2', 'ищем 3']),
    'en': ('In the centre is the equality 2³ = 8. Three arrows lead to three questions: unknown result - a power, unknown base - a root, unknown exponent - a logarithm.',
           'One equality, three questions: power, root, logarithm.',
           ['power', 'root', 'logarithm'],
           ['we seek 8', 'we seek 2', 'we seek 3']),
    'de': ('In der Mitte steht die Gleichung 2³ = 8. Drei Pfeile führen zu drei Fragen: Ergebnis unbekannt - eine Potenz, Basis unbekannt - eine Wurzel, Exponent unbekannt - ein Logarithmus.',
           'Eine Gleichung, drei Fragen: Potenz, Wurzel, Logarithmus.',
           ['Potenz', 'Wurzel', 'Logarithmus'],
           ['gesucht 8', 'gesucht 2', 'gesucht 3']),
}


def figure(lang):
    label, caption, names, seek = TEXT[lang]
    f = Fig(200)
    f.rect(110, 12, 100, 40, fill_op=0.12, accent=True)
    f.text(160, 39, '2³ = 8', size=17, anchor='middle', bold=True)
    forms = ['2³ = ?', '∛8 = ?', 'log₂ 8 = ?']
    xs = [6, 112, 218]
    for x, n, s, fm in zip(xs, names, seek, forms):
        f.arrow(160, 52, x + 48, 120, w=1.2)
        f.rect(x, 122, 96, 66, fill_op=0.05)
        f.text(x + 48, 144, n, size=13, anchor='middle', bold=True)
        f.text(x + 48, 163, fm, size=13, anchor='middle')
        f.text(x + 48, 181, s, size=12, anchor='middle', op=0.7, italic=True)
    return f, label, caption
