"""Block 13, reading with an extra number: a box, its volume; the diagonal of the base is not needed."""
from fig import Fig
from box import box

DATA = {'a': 5, 'b': 2, 'c': 4, 'd': 29}
TEXT = {
    'uk': ('Прямокутний паралелепіпед ABCDA₁B₁C₁D₁. На рисунку підписано ребра AB = 5 см, AD = 2 см, AA₁ = 4 см і діагональ основи AC = √29 см (пунктиром).',
           'До задачі: прямокутний паралелепіпед, на якому підписано три ребра і діагональ основи.'),
    'ru': ('Прямоугольный параллелепипед ABCDA₁B₁C₁D₁. На рисунке подписаны рёбра AB = 5 см, AD = 2 см, AA₁ = 4 см и диагональ основания AC = √29 см (пунктиром).',
           'К задаче: прямоугольный параллелепипед, на котором подписаны три ребра и диагональ основания.'),
    'en': ('Cuboid ABCDA₁B₁C₁D₁. The figure labels the edges AB = 5 cm, AD = 2 cm, AA₁ = 4 cm and the diagonal of the base AC = √29 cm (dashed).',
           'For the task: a cuboid with three edges and the diagonal of the base labelled.'),
    'de': ('Der Quader ABCDA₁B₁C₁D₁. Auf der Abbildung sind die Kanten AB = 5 cm, AD = 2 cm, AA₁ = 4 cm und die Diagonale der Grundfläche AC = √29 cm (gestrichelt) beschriftet.',
           'Zur Aufgabe: ein Quader mit drei beschrifteten Kanten und der Diagonalen der Grundfläche.'),
}

# The unit is a word of the page language: a figure in English says cm.
CM = {'uk': 'см', 'ru': 'см', 'en': 'cm', 'de': 'cm'}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(232)
    v = box(f, DATA['a'], DATA['b'], DATA['c'], A=(52, 208), s=30, depth=1.6)
    A, B, C, A1 = v['A'], v['B'], v['C'], v['A₁']
    f.line(*A, *C, w=1.4, dash='6 4', accent=True)
    f.text((A[0] + C[0]) / 2 + 4, (A[1] + C[1]) / 2 - 12, '√29 ' + CM[lang], size=13, accent=True)
    f.text((A[0] + B[0]) / 2, A[1] + 20, '5 ' + CM[lang], size=13, anchor='middle')
    f.text((B[0] + C[0]) / 2 + 12, (B[1] + C[1]) / 2 + 12, '2 ' + CM[lang], size=13)
    f.text(A[0] - 6, (A[1] + A1[1]) / 2 + 12, '4 ' + CM[lang], size=13, anchor='end')
    return f, label, caption
