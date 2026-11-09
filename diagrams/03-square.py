"""Block 03, why: (a + b)² = a² + 2ab + b² as a square cut into four parts."""
from fig import Fig

TEXT = {
    'uk': ('Квадрат зі стороною a + b розрізано на чотири частини: квадрат a², квадрат b² і два однакові прямокутники ab. Сліпий хід «a² + b²» губить саме два прямокутники.',
           'Квадрат суми: два прямокутники ab, які губить сліпий хід.'),
    'ru': ('Квадрат со стороной a + b разрезан на четыре части: квадрат a², квадрат b² и два одинаковых прямоугольника ab. Слепой ход «a² + b²» теряет именно два прямоугольника.',
           'Квадрат суммы: два прямоугольника ab, которые теряет слепой ход.'),
    'en': ('A square with side a + b is cut into four parts: a square a², a square b² and two equal rectangles ab. The blind move «a² + b²» loses exactly the two rectangles.',
           'The square of a sum: the two rectangles ab that the blind move loses.'),
    'de': ('Ein Quadrat mit der Seite a + b ist in vier Teile geteilt: ein Quadrat a², ein Quadrat b² und zwei gleiche Rechtecke ab. Der blinde Zug «a² + b²» verliert genau die zwei Rechtecke.',
           'Das Quadrat einer Summe: die zwei Rechtecke ab, die der blinde Zug verliert.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    x0, y0, a, b = 70, 10, 110, 70
    f.rect(x0, y0, a, a, rx=0, fill_op=0.08)
    f.rect(x0 + a, y0, b, a, rx=0, fill_op=0.2, accent=True)
    f.rect(x0, y0 + a, a, b, rx=0, fill_op=0.2, accent=True)
    f.rect(x0 + a, y0 + a, b, b, rx=0, fill_op=0.08)
    f.text(x0 + a / 2, y0 + a / 2 + 6, 'a²', size=18, anchor='middle', italic=True)
    f.text(x0 + a + b / 2, y0 + a / 2 + 6, 'ab', size=16, anchor='middle', italic=True)
    f.text(x0 + a / 2, y0 + a + b / 2 + 6, 'ab', size=16, anchor='middle', italic=True)
    f.text(x0 + a + b / 2, y0 + a + b / 2 + 6, 'b²', size=16, anchor='middle', italic=True)
    f.text(x0 - 10, y0 + a / 2 + 5, 'a', size=15, anchor='end', italic=True)
    f.text(x0 - 10, y0 + a + b / 2 + 5, 'b', size=15, anchor='end', italic=True)
    f.text(x0 + a / 2, y0 + a + b + 20, 'a', size=15, anchor='middle', italic=True)
    f.text(x0 + a + b / 2, y0 + a + b + 20, 'b', size=15, anchor='middle', italic=True)
    return f, label, caption
