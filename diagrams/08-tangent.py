"""Block 08, why: the derivative is the slope of the tangent; y = x², x₀ = 1, slope 2."""
from fig import Fig, Plot

TEXT = {
    'uk': ('Парабола y = x² і дотична до неї в точці x₀ = 1. Дотична піднімається на 2 одиниці на кожну одиницю праворуч: її кутовий коефіцієнт 2 дорівнює похідній 2x у точці 1.',
           'Похідна як нахил дотичної: для y = x² у точці 1 нахил дорівнює 2.', 'нахил 2'),
    'ru': ('Парабола y = x² и касательная к ней в точке x₀ = 1. Касательная поднимается на 2 единицы на каждую единицу вправо: её угловой коэффициент 2 равен производной 2x в точке 1.',
           'Производная как наклон касательной: для y = x² в точке 1 наклон равен 2.', 'наклон 2'),
    'en': ('The parabola y = x² and its tangent at x₀ = 1. The tangent rises 2 units for each unit to the right: its gradient 2 equals the derivative 2x at the point 1.',
           'The derivative as the slope of the tangent: for y = x² at the point 1 the slope is 2.',
           'slope 2'),
}


def figure(lang):
    label, caption, slope = TEXT[lang]
    f = Fig(220)
    p = Plot(f, 20, 12, 280, 180, -1.5, 3, -1.5, 4.5)
    p.axes(ticks_x=(1, 2), ticks_y=(1, 3))
    p.curve(lambda x: x * x, -1.5, 2.1, w=2)
    p.curve(lambda x: 2 * x - 1, -0.2, 2.7, w=1.6, accent=True)
    f.circle(*p.pt(1, 1), 4.5, dot=True, accent=True)
    f.line(*p.pt(1, 1), *p.pt(2, 1), w=1.2, dash='3 3')
    f.line(*p.pt(2, 1), *p.pt(2, 3), w=1.2, dash='3 3')
    f.text(p.px(2) + 6, p.py(2) + 4, slope, size=12, accent=True)
    f.text(p.px(1.5), p.py(1) + 16, '1', size=12, anchor='middle')
    f.text(p.px(-1.4), p.py(3.9), 'y = x²', size=12)
    return f, label, caption
