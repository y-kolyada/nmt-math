"""Block 8, task: the area under y = x² from 0 to 3."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Графік y = x² для x від 0 і далі. Фігуру під графіком між віссю Ox і прямою x = 3 зафарбовано: її обмежують парабола зверху, вісь Ox знизу і вертикальна пряма x = 3 праворуч.',
           'До задачі: криволінійна трапеція під параболою.'),
    'ru': ('График y = x² для x от 0 и дальше. Фигура под графиком между осью Ox и прямой x = 3 закрашена: её ограничивают парабола сверху, ось Ox снизу и вертикальная прямая x = 3 справа.',
           'К задаче: криволинейная трапеция под параболой.'),
    'en': ('The graph of y = x² for x from 0 onwards. The figure under the graph between the Ox axis and the line x = 3 is shaded: it is bounded by the parabola above, the Ox axis below and the vertical line x = 3 on the right.',
           'For the task: a curvilinear trapezium under a parabola.'),
    'de': ('Der Graph von y = x² für x ab 0. Die Figur unter dem Graphen zwischen der Ox-Achse und der Geraden x = 3 ist schraffiert: oben begrenzt sie die Parabel, unten die Ox-Achse, rechts die senkrechte Gerade x = 3.',
           'Zur Aufgabe: ein krummliniges Trapez unter einer Parabel.'),
}
B = 3


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    p = Plot(f, 20, 10, 280, 196, -0.6, 3.8, -1, 11)
    p.axes(ticks_x=(B,))
    pts = [p.pt(B * i / 60, (B * i / 60) ** 2) for i in range(61)] + [p.pt(B, 0), p.pt(0, 0)]
    f.poly(pts, close=True, w=0, fill_op=0.3, accent=True)
    p.curve(lambda x: x * x, -0.6, 3.3, w=2.2)
    f.line(p.px(B), p.py(0), p.px(B), p.py(B * B), w=1.6, dash='5 3')
    f.text(p.px(1.3), p.py(8.2), 'y = x²', size=13, italic=True)
    f.text(p.px(2.1), p.py(1.6), 'S', size=16, anchor='middle', italic=True, bold=True)
    return f, label, caption
