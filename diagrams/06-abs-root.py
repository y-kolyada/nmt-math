"""Block 06, limits: y = √(x²) is y = |x|, not y = x."""
import math
from fig import Fig, Plot

TEXT = {
    'uk': ('Графік y = √(x²) - це «галочка» y = |x|: обидві гілки вище осі Ox. Пунктиром показано y = x: ліворуч від нуля вона йде нижче осі, тому √(x²) і x там різні.',
           '√(x²) = |x|: ліворуч від нуля корінь з квадрата не дорівнює x.'),
    'ru': ('График y = √(x²) - это «галочка» y = |x|: обе ветви выше оси Ox. Пунктиром показано y = x: слева от нуля она идёт ниже оси, поэтому √(x²) и x там различны.',
           '√(x²) = |x|: слева от нуля корень из квадрата не равен x.'),
    'en': ('The graph of y = √(x²) is the «tick» y = |x|: both branches lie above the Ox axis. Dashed: y = x; to the left of zero it runs below the axis, so √(x²) and x differ there.',
           '√(x²) = |x|: to the left of zero the root of the square is not x.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(190)
    p = Plot(f, 20, 12, 280, 160, -3.5, 3.5, -3, 3.5)
    p.axes(ticks_x=(-2, 2), ticks_y=(2,))
    p.curve(lambda x: x, -3, 3.3, w=1.2, dash='4 3', op=0.7)
    p.curve(lambda x: math.sqrt(x * x), -3.4, 3.4, w=2.2, accent=True)
    f.text(*p.pt(0.9, 0.3), 'y = √(x²) = |x|', size=12, accent=True)
    f.text(*p.pt(1.2, -1.2), 'y = x', size=12, op=0.8)
    return f, label, caption
