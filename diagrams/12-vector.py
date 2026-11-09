"""Block 12, hook: vector AB for A(5; 1), B(2; 4) is end minus start = (−3; 3)."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Координатна сітка з точками A(5; 1) і B(2; 4). Вектор AB іде від A до B: по осі x на −3, по осі y на +3, тому AB = (−3; 3), кінець мінус початок.',
           'Координати вектора - кінець мінус початок: AB = (2 − 5; 4 − 1) = (−3; 3).'),
    'ru': ('Координатная сетка с точками A(5; 1) и B(2; 4). Вектор AB идёт от A к B: по оси x на −3, по оси y на +3, поэтому AB = (−3; 3), конец минус начало.',
           'Координаты вектора - конец минус начало: AB = (2 − 5; 4 − 1) = (−3; 3).'),
    'en': ('A coordinate grid with points A(5; 1) and B(2; 4). The vector AB goes from A to B: by −3 along the x-axis and by +3 along the y-axis, so AB = (−3; 3), end minus start.',
           'The coordinates of a vector are end minus start: AB = (2 − 5; 4 − 1) = (−3; 3).'),
    'de': ('Ein Koordinatengitter mit den Punkten A(5; 1) und B(2; 4). Der Vektor AB geht von A nach B: um −3 entlang der x-Achse und um +3 entlang der y-Achse, also AB = (−3; 3), Ende minus Anfang.',
           'Die Koordinaten eines Vektors sind Ende minus Anfang: AB = (2 − 5; 4 − 1) = (−3; 3).'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(220)
    p = Plot(f, 24, 10, 270, 190, -0.5, 6.5, -0.5, 5.2)
    for k in range(0, 7):
        f.line(p.px(k), p.py(-0.3), p.px(k), p.py(5), w=0.6, op=0.3)
    for k in range(0, 6):
        f.line(p.px(-0.3), p.py(k), p.px(6.3), p.py(k), w=0.6, op=0.3)
    p.axes(ticks_x=(2, 5), ticks_y=(1, 4))
    f.line(*p.pt(5, 1), *p.pt(2, 1), w=1.4, dash='4 3')
    f.line(*p.pt(2, 1), *p.pt(2, 4), w=1.4, dash='4 3')
    f.arrow(*p.pt(5, 1), *p.pt(2.08, 3.92), w=2.2, accent=True)
    f.circle(*p.pt(5, 1), 4, dot=True)
    f.circle(*p.pt(2, 4), 4, dot=True)
    f.text(p.px(5) + 8, p.py(1) + 4, 'A(5; 1)', size=12)
    f.text(p.px(2) + 8, p.py(4) - 6, 'B(2; 4)', size=12)
    f.text(p.px(3.5), p.py(1) + 16, '−3', size=13, anchor='middle', bold=True)
    f.text(p.px(2) - 8, p.py(2.5), '+3', size=13, anchor='end', bold=True)
    return f, label, caption
