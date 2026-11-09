"""Block 12, reading with a trap: the grid cells are 2 wide and 1 tall, the slope of a line."""
from fig import Fig, Plot

DATA = {'x1': 2, 'y1': 1, 'x2': 6, 'y2': 3}
TEXT = {
    'uk': ('Пряма проходить через точки P і Q. Клітинки сітки квадратні на вигляд, але по осі x одна клітинка - 2 одиниці (підписано 2, 4, 6, 8), а по осі y - 1 одиниця (підписано 1, 2, 3, 4). Точка P має координати (2; 1), точка Q - (6; 3).',
           'До задачі: пряма на сітці, у якої крок по осях різний.'),
    'ru': ('Прямая проходит через точки P и Q. Клетки сетки квадратные на вид, но по оси x одна клетка - 2 единицы (подписано 2, 4, 6, 8), а по оси y - 1 единица (подписано 1, 2, 3, 4). Точка P имеет координаты (2; 1), точка Q - (6; 3).',
           'К задаче: прямая на сетке, у которой шаг по осям разный.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    d = DATA
    f = Fig(244)
    # 40 px per cell on both axes: 2 units of x, 1 unit of y
    p = Plot(f, 30, 8, 20 * 11, 40 * 5.2, -1, 10, -0.8, 4.4)
    for x in (2, 4, 6, 8):
        f.line(*p.pt(x, -0.8), *p.pt(x, 4.4), w=0.8, op=0.25)
    for y in (1, 2, 3, 4):
        f.line(*p.pt(-1, y), *p.pt(10, y), w=0.8, op=0.25)
    p.axes(ticks_x=(2, 4, 6, 8), ticks_y=(1, 2, 3, 4))
    k = (d['y2'] - d['y1']) / (d['x2'] - d['x1'])
    p.curve(lambda x: d['y1'] + k * (x - d['x1']), -1, 8.6, w=2, accent=True)
    for name, x, y in (('P', d['x1'], d['y1']), ('Q', d['x2'], d['y2'])):
        f.circle(*p.pt(x, y), 4, dot=True, accent=True)
        f.text(p.px(x) - 4, p.py(y) - 10, name, size=14, anchor='end', italic=True, bold=True)
    return f, label, caption
