"""Block 2, reading: a bar chart of books sold, the share of two days."""
from fig import Fig
from bars import bars

DATA = {'mon': 12, 'tue': 18, 'wed': 30, 'thu': 24, 'fri': 6}
DAYS = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
TEXT = {
    'uk': ('Стовпчикова діаграма: скільки книжок продала крамниця за день. Шкала від 0 до 30 з кроком 6. Понеділок - 12, вівторок - 18, середа - 30, четвер - 24, пʼятниця - 6.',
           'До задачі: продаж книжок за п’ять днів.'),
    'ru': ('Столбчатая диаграмма: сколько книг продал магазин за день. Шкала от 0 до 30 с шагом 6. Понедельник - 12, вторник - 18, среда - 30, четверг - 24, пятница - 6.',
           'К задаче: продажа книг за пять дней.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(200)
    bars(f, DAYS, [DATA[k] for k in ('mon', 'tue', 'wed', 'thu', 'fri')], 0, 30, 6)
    return f, label, caption
