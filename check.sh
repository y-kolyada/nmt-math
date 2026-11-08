#!/usr/bin/env bash
# Проверка сайта. Одна команда - один ответ.
#
#     ./check.sh
#
# ПОЧЕМУ ОДНА КОМАНДА, А НЕ ЧЕТЫРЕ. Проверка, которую нужно вспоминать по
# частям, не запускается перед публикацией - запускается та, что одна и
# отвечает ЗЕЛЁНОЕ или КРАСНОЕ. Сами проверки лежат в tools/ и запускаются
# по отдельности, когда нужно понять причину:
#
#     tools/check-page.sh ru/01.html      страница существует и у неё свой заголовок
#     tools/check-claims.sh               утверждения сайта выполняются в терминале
#     tools/check-examples.sh             примеры со страниц 10-12 запускаются
#     python3 tools/check-links.py        внутренние ссылки и якоря
#     python3 tools/check-text.py         длинное тире на страницах
#     python3 tools/build-search.py       пересобрать индекс поиска
#     python3 tools/build-meta.py         голова страницы, объём в словах, соседние темы, карта сайта
#     node tools/check-pages.mjs          телефон 390px и липкая панель, все страницы
#     python3 tools/build-math.py --check  формулы: напечатаны и совпадают с источником
#     node tools/check-diagrams.mjs       схемы: холст, подписи, исходники, перевод
#     python3 tools/check-navigator.py    девять линз и выход из каждой
#     node tools/shot.mjs ru/01.html       снимок одной страницы, чтобы посмотреть глазами
#
# Браузерная проверка требует playwright (npm i playwright). Если его нет,
# она честно говорит об этом и считается КРАСНОЙ: зелёный ответ без браузера
# означал бы, что страницы никто не смотрел.

set -uo pipefail
cd "$(dirname "$0")" || exit 2

if [ "${1:-}" = "--fast" ]; then
  shift
  exec ./tools/check-fast.sh "$@"
fi

FAIL=0
NAMES=()
CODES=()
DURS=()
TOTAL_US=0

g() { printf '\033[32m%s\033[0m' "$1"; }
r() { printf '\033[31m%s\033[0m' "$1"; }

# ДЛИТЕЛЬНОСТЬ КАЖДОЙ ПРОВЕРКИ. Прогон, который не говорит, сколько он шёл,
# нельзя ускорить: на вопрос «что съело минуты» отвечает оценка, а не машина.
# Замер идёт в микросекундах по EPOCHREALTIME (bash 5.0 и новее). Где его нет
# (macOS штатно несёт bash 3.2), замер падает на SECONDS и печатает целые
# секунды - хуже разрешением, но не ломается. Разделитель дробной части берётся
# из локали, поэтому запятая приводится к точке.
now() {
  local t=${EPOCHREALTIME:-}
  if [ -n "$t" ]; then
    t=${t/,/.}
    printf '%s' "${t%.*}${t#*.}"
  else
    printf '%s' "$((SECONDS * 1000000))"
  fi
}

# Микросекунды -> секунды с одним знаком, с округлением.
secs() {
  local d=$(((${1} + 50000) / 100000))
  printf '%d.%d' "$((d / 10))" "$((d % 10))"
}

# Отступ до колонки длительностей. Имена разделов русские, а printf '%-24s'
# считает БАЙТЫ: кириллица идёт по два байта на знак, и колонка уехала бы на
# пять знаков. ${#name} под UTF-8 считает знаки, поэтому отступ собирается сам.
pad() {
  local n=${#1}
  [ "$n" -ge 24 ] && { printf ' '; return; }
  printf '%*s' "$((24 - n))" ''
}

run() {
  local name=$1
  shift
  local t0
  t0=$(now)
  "$@"
  local code=$?
  local t1
  t1=$(now)
  NAMES+=("$name")
  CODES+=("$code")
  DURS+=("$(secs "$((t1 - t0))")")
  TOTAL_US=$((TOTAL_US + t1 - t0))
  [ "$code" -eq 0 ] || FAIL=$((FAIL + 1))
}

SOURCE=$(python3 tools/siteconf.py --get source) || exit 2

run "страница и заголовок" ./tools/check-page.sh "$SOURCE/index.html"
run "оболочка и навигация" python3 tools/build-nav.py --check
run "утверждения сайта"    ./tools/check-claims.sh
run "примеры запускаются"  ./tools/check-examples.sh
run "ссылки и якоря"       python3 tools/check-links.py
run "термины и словарь"    python3 tools/check-terms.py
run "пунктуация"          python3 tools/check-text.py
run "индекс поиска"        python3 tools/build-search.py --check
run "данные страниц"       python3 tools/build-meta.py --check
run "телефон и панель"     node tools/check-pages.mjs
run "формулы"             python3 tools/build-math.py --check
run "схемы страниц"        node tools/check-diagrams.mjs
run "линзы навигатора"     python3 tools/check-navigator.py
run "перевод и заглушки"  python3 tools/check-struct.py

echo
echo "  Итог проверки сайта"
echo "  ----------------------------------------------"
for i in "${!NAMES[@]}"; do
  if [ "${CODES[$i]}" -eq 0 ]; then
    printf '  [ %s ] %s%s%6s с\n' "$(g 'ДА ')" "${NAMES[$i]}" "$(pad "${NAMES[$i]}")" "${DURS[$i]}"
  else
    printf '  [ %s ] %s%s%6s с\n' "$(r 'НЕТ')" "${NAMES[$i]}" "$(pad "${NAMES[$i]}")" "${DURS[$i]}"
  fi
done
echo "  ----------------------------------------------"
TOTAL_S=$((TOTAL_US / 1000000))
if [ "$TOTAL_S" -ge 60 ]; then
  printf '  всего %d м %s с\n' "$((TOTAL_S / 60))" "$(secs "$((TOTAL_US - (TOTAL_S / 60) * 60000000))")"
else
  printf '  всего %s с\n' "$(secs "$TOTAL_US")"
fi
if [ "$FAIL" -eq 0 ]; then
  printf '  %s\n\n' "$(g 'ЗЕЛЁНОЕ')"
else
  printf '  %s  - проверок со словом НЕТ: %s\n\n' "$(r 'КРАСНОЕ')" "$FAIL"
fi

[ "$FAIL" -eq 0 ]
