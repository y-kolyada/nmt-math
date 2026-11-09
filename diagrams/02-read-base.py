"""Block 2, reading with a trap: the value axis starts at 40, not at zero."""
from fig import Fig
from bars import bars

DATA = {'tue': 50, 'sat': 80}
DAYS = {'uk': ['Пн', 'Вт', 'Пт', 'Сб'], 'ru': ['Пн', 'Вт', 'Пт', 'Сб'], 'en': ['Mon', 'Tue', 'Fri', 'Sat'], 'de': ['Mo', 'Di', 'Fr', 'Sa']}
TEXT = {
    'uk': ('Стовпчикова діаграма відвідувачів музею. Шкала починається не з нуля, а з 40 (злам на осі), крок 10, до 90. Понеділок - 60, вівторок - 50, пʼятниця - 70, субота - 80. Стовпчик суботи на вигляд у 4 рази вищий за стовпчик вівторка.',
           'До задачі: діаграма, шкала якої починається не з нуля.'),
    'ru': ('Столбчатая диаграмма посетителей музея. Шкала начинается не с нуля, а с 40 (излом на оси), шаг 10, до 90. Понедельник - 60, вторник - 50, пятница - 70, суббота - 80. Столбик субботы на вид в 4 раза выше столбика вторника.',
           'К задаче: диаграмма, шкала которой начинается не с нуля.'),
    'en': ('A bar chart of museum visitors. The scale starts not at zero but at 40 (a break on the axis), step 10, up to 90. Monday 60, Tuesday 50, Friday 70, Saturday 80. The Saturday bar looks 4 times as tall as the Tuesday bar.',
           'For the task: a chart whose scale does not start at zero.'),
    'de': ('Ein Säulendiagramm der Museumsbesucher. Die Skala beginnt nicht bei null, sondern bei 40 (ein Bruch auf der Achse), Schritt 10, bis 90. Montag 60, Dienstag 50, Freitag 70, Samstag 80. Die Säule für Samstag sieht 4-mal so hoch aus wie die für Dienstag.',
           'Zur Aufgabe: ein Diagramm, dessen Skala nicht bei null beginnt.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(214)
    bars(f, DAYS[lang], [60, DATA['tue'], 70, DATA['sat']], 40, 90, 10, broken=True)
    return f, label, caption
