"""Block 2, reading and linking: prices by month, the percentage change."""
from fig import Fig
from bars import bars

DATA = {'jan': 40, 'mar': 50}
MONTHS = {'uk': ['січ', 'лют', 'бер', 'кві'], 'ru': ['янв', 'фев', 'мар', 'апр']}
TEXT = {
    'uk': ('Стовпчикова діаграма: ціна кілограма яблук, грн, за чотири місяці. Шкала від 0 до 60 з кроком 10. Січень - 40, лютий - 30, березень - 50, квітень - 60.',
           'До задачі: ціна яблук за чотири місяці.'),
    'ru': ('Столбчатая диаграмма: цена килограмма яблок, грн, за четыре месяца. Шкала от 0 до 60 с шагом 10. Январь - 40, февраль - 30, март - 50, апрель - 60.',
           'К задаче: цена яблок за четыре месяца.'),
}


def figure(lang):
    label, caption = TEXT[lang]
    f = Fig(200)
    bars(f, MONTHS[lang], [DATA['jan'], 30, DATA['mar'], 60], 0, 60, 10)
    return f, label, caption
