"""Block 02, why: inverse proportion keeps the product (the area) constant."""
from fig import Fig

TEXT = {
    'uk': ('Два прямокутники однакової площі 12: зі сторонами 2 на 6 і 3 на 4. Швидкість - висота, час - ширина, шлях - площа. Збільшили висоту в 1,5 раза - ширина зменшилася в 1,5 раза.',
           'Обернена пропорційність: добуток v · t сталий, як площа прямокутника.', 'S = 12'),
    'ru': ('Два прямоугольника одинаковой площади 12: со сторонами 2 на 6 и 3 на 4. Скорость - высота, время - ширина, путь - площадь. Увеличили высоту в 1,5 раза - ширина уменьшилась в 1,5 раза.',
           'Обратная пропорциональность: произведение v · t постоянно, как площадь прямоугольника.', 'S = 12'),
}


def figure(lang):
    label, caption, s = TEXT[lang]
    f = Fig(150)
    u = 20
    # left: v=2, t=6
    x0, base = 20, 120
    f.rect(x0, base - 2 * u, 6 * u, 2 * u, rx=0, fill_op=0.10)
    f.text(x0 + 3 * u, base - u + 5, s, size=13, anchor='middle')
    f.text(x0 + 3 * u, base + 18, 't = 6', size=13, anchor='middle', italic=True)
    f.text(x0 + 6 * u + 6, base - u + 5, 'v = 2', size=13, italic=True)
    # right: v=3, t=4
    x1 = 200
    f.rect(x1, base - 3 * u, 4 * u, 3 * u, rx=0, fill_op=0.18, accent=True)
    f.text(x1 + 2 * u, base - 1.5 * u + 5, s, size=13, anchor='middle')
    f.text(x1 + 2 * u, base + 18, 't = 4', size=13, anchor='middle', italic=True)
    f.text(x1 - 6, base - 3 * u - 8, 'v = 3', size=13, italic=True)
    return f, label, caption
