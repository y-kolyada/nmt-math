"""Block 13, reading: the edges of a box are on the figure, the diagonal is asked."""
from fig import Fig
from box import box

DATA = {'a': 12, 'b': 4, 'c': 3}
TEXT = {
    'uk': ('Прямокутний паралелепіпед ABCDA₁B₁C₁D₁. На рисунку підписано ребра: AB = 12 см, AD = 4 см, AA₁ = 3 см. Діагональ AC₁ - пунктиром, позначена знаком питання.',
           'До задачі: прямокутний паралелепіпед із підписаними ребрами і його діагональ.'),
    'ru': ('Прямоугольный параллелепипед ABCDA₁B₁C₁D₁. На рисунке подписаны рёбра: AB = 12 см, AD = 4 см, AA₁ = 3 см. Диагональ AC₁ - пунктиром, отмечена знаком вопроса.',
           'К задаче: прямоугольный параллелепипед с подписанными рёбрами и его диагональ.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(190)
    v = box(f, DATA['a'], DATA['b'], DATA['c'], A=(50, 160), s=14, depth=1.0)
    A, B, D, A1, C1 = v['A'], v['B'], v['D'], v['A₁'], v['C₁']
    f.line(*A, *C1, w=1.6, dash='6 4', accent=True)
    f.text((A[0] + C1[0]) / 2 - 4, (A[1] + C1[1]) / 2 + 18, '?', size=15, bold=True, accent=True)
    f.text((A[0] + B[0]) / 2, A[1] + 20, '12 см', size=13, anchor='middle')
    f.text(B[0] + 22, B[1] - 4, '4 см', size=13)
    f.text(A[0] - 6, (A[1] + A1[1]) / 2 + 12, '3 см', size=13, anchor='end')
    return f, label, caption
