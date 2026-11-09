"""Block 2, reading: a bar chart of books sold, the share of two days."""
from fig import Fig
from bars import bars

DATA = {'mon': 12, 'tue': 18, 'wed': 30, 'thu': 24, 'fri': 6}
DAYS = {'uk': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт'], 'ru': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт'], 'en': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], 'de': ['Mo', 'Di', 'Mi', 'Do', 'Fr']}
TEXT = {
    'uk': ('Стовпчикова діаграма: скільки книжок продала крамниця за день. Шкала від 0 до 30 з кроком 6. Понеділок - 12, вівторок - 18, середа - 30, четвер - 24, пʼятниця - 6.',
           'До задачі: продаж книжок за п’ять днів.'),
    'ru': ('Столбчатая диаграмма: сколько книг продал магазин за день. Шкала от 0 до 30 с шагом 6. Понедельник - 12, вторник - 18, среда - 30, четверг - 24, пятница - 6.',
           'К задаче: продажа книг за пять дней.'),
    'en': ('A bar chart: how many books a shop sold in a day. The scale goes from 0 to 30 in steps of 6. Monday 12, Tuesday 18, Wednesday 30, Thursday 24, Friday 6.',
           'For the task: book sales over five days.'),
    'de': ('Ein Säulendiagramm: wie viele Bücher ein Laden an einem Tag verkaufte. Die Skala geht von 0 bis 30 in Schritten von 6. Montag 12, Dienstag 18, Mittwoch 30, Donnerstag 24, Freitag 6.',
           'Zur Aufgabe: Buchverkäufe an fünf Tagen.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(200)
    bars(f, DAYS[lang], [DATA[k] for k in ('mon', 'tue', 'wed', 'thu', 'fri')], 0, 30, 6)
    return f, label, caption
