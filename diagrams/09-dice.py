"""Block 09, limits: 36 equally likely pairs of two dice; the sum 7 takes six of them."""
from fig import Fig

TEXT = {
    'uk': ('Таблиця 6 на 6: рядок - перший кубик, стовпчик - другий, у клітинці сума. Шість клітинок із сумою 7 лежать на діагоналі і виділені. Сума 2 трапляється лише в одній клітинці, тому суми не рівноможливі, а пари граней - рівноможливі.',
           'Рівноможливі - 36 пар граней, а не 11 сум: сума 7 займає 6 клітинок з 36.', ['1-й', '2-й']),
    'ru': ('Таблица 6 на 6: строка - первый кубик, столбец - второй, в клетке сумма. Шесть клеток с суммой 7 лежат на диагонали и выделены. Сумма 2 встречается только в одной клетке, поэтому суммы не равновозможны, а пары граней - равновозможны.',
           'Равновозможны 36 пар граней, а не 11 сумм: сумма 7 занимает 6 клеток из 36.', ['1-й', '2-й']),
    'en': ('A 6 by 6 table: the row is the first die, the column is the second, the cell holds the sum. The six cells with sum 7 lie on a diagonal and are highlighted. The sum 2 occurs in only one cell, so the sums are not equally likely, while the pairs of faces are.',
           'Equally likely are the 36 pairs of faces, not the 11 sums: the sum 7 takes 6 cells of 36.',
           ['1st', '2nd']),
}


def figure(lang):
    label, caption, heads = TEXT[lang]
    f = Fig(250)
    x0, y0, s = 74, 34, 32
    for k in range(6):
        f.text(x0 + s * k + s / 2, y0 - 8, str(k + 1), size=12, anchor='middle', bold=True, op=0.8)
        f.text(x0 - 10, y0 + s * k + s / 2 + 4, str(k + 1), size=12, anchor='end', bold=True, op=0.8)
    for i in range(6):
        for j in range(6):
            hit = i + j + 2 == 7
            f.rect(x0 + s * j, y0 + s * i, s, s, rx=0, fill_op=0.3 if hit else 0.03, accent=hit, sw=0.8)
            f.text(x0 + s * j + s / 2, y0 + s * i + s / 2 + 4, str(i + j + 2), size=12, anchor='middle', bold=hit)
    f.text(x0 + 3 * s, 14, heads[1], size=12, anchor='middle', op=0.7)
    f.text(14, y0 + 3 * s, heads[0], size=12, op=0.7)
    return f, label, caption
