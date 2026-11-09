"""Block 12, corollary: the line y = kx + b, b on the y axis and k the rise per unit step."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Пряма y = kx + b у координатах. Вона перетинає вісь y у точці, позначеній b. Сходинка під прямою: крок 1 праворуч - підйом k угору.',
           'Наслідок: b - точка перетину з віссю y, k - підйом прямої на один крок праворуч.'),
    'ru': ('Прямая y = kx + b в координатах. Она пересекает ось y в точке, отмеченной b. Ступенька под прямой: шаг 1 вправо - подъём k вверх.',
           'Следствие: b - точка пересечения с осью y, k - подъём прямой на один шаг вправо.'),
    'en': ('The line y = kx + b on coordinate axes. It crosses the y-axis at the point marked b. A step under the line: 1 to the right, k up.',
           'Corollary: b is where the line crosses the y-axis, k is how far the line rises for one step to the right.'),
    'de': ('Die Gerade y = kx + b im Koordinatensystem. Sie schneidet die y-Achse in dem mit b markierten Punkt. Ein Schritt unter der Geraden: 1 nach rechts, k nach oben.',
           'Folgerung: b ist der Schnittpunkt der Geraden mit der y-Achse, k ist, wie weit die Gerade bei einem Schritt nach rechts steigt.'),
}
K, B0 = 0.5, 1.5


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(210)
    p = Plot(f, 20, 12, 286, 182, -1.2, 5.2, -0.8, 4.4)
    p.axes()
    p.curve(lambda x: K * x + B0, -1.2, 5.2, w=2, accent=True)
    f.circle(*p.pt(0, B0), 3.5, dot=True, accent=True)
    f.text(p.px(0) - 8, p.py(B0) - 6, 'b', size=14, anchor='end', italic=True, accent=True)
    x0 = 2.4
    y0 = K * x0 + B0
    f.line(*p.pt(x0, y0), *p.pt(x0 + 1, y0), w=1.4)
    f.line(*p.pt(x0 + 1, y0), *p.pt(x0 + 1, y0 + K), w=1.4)
    f.text((p.px(x0) + p.px(x0 + 1)) / 2, p.py(y0) + 17, '1', size=13, anchor='middle')
    f.text(p.px(x0 + 1) + 7, (p.py(y0) + p.py(y0 + K)) / 2 + 5, 'k', size=14, italic=True)
    f.text(p.px(0.4), p.py(4.0), 'y = kx + b', size=13, italic=True, accent=True)
    return f, label, caption
