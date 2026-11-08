#!/usr/bin/env bash
# Быстрая проверка изменений. Проверяет только изменённые HTML-файлы и утверждения.
#
#     ./tools/check-fast.sh
#     ./tools/check-fast.sh ru/01.html ru/02.html
#
# Запускает проверки текста, навигации, клеймов и браузерного рендеринга
# только для целевых файлов, экономя время и контекст во время смены.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

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

# Определение списка проверяемых страниц
TARGETS=("$@")
if [ "${#TARGETS[@]}" -eq 0 ]; then
  # Ищем изменённые HTML-файлы в рабочей копии или индексе git
  CHANGED=$(git status --porcelain 2>/dev/null | awk '{print $NF}' | grep '\.html$' || true)
  if [ -z "$CHANGED" ]; then
    # Если рабочая копия чиста, берём файлы последнего коммита
    CHANGED=$(git diff --name-only HEAD~1 2>/dev/null | grep '\.html$' || true)
  fi
  if [ -n "$CHANGED" ]; then
    # Преобразуем строку в массив
    while IFS= read -r line; do
      [ -f "$line" ] && TARGETS+=("$line")
    done <<< "$CHANGED"
  fi
fi

if [ "${#TARGETS[@]}" -eq 0 ]; then
  SOURCE=$(python3 tools/siteconf.py --get source) || exit 2
  TARGETS=("$SOURCE/index.html" "$SOURCE/01.html")
fi

echo "  Быстрая проверка: ${TARGETS[*]}"
echo "  =============================================="

run "оболочка и навигация" python3 tools/build-nav.py --check
run "утверждения сайта"    ./tools/check-claims.sh
run "пунктуация (файлы)"   python3 tools/check-text.py "${TARGETS[@]}"
run "телефон и панель"     node tools/check-pages.mjs "${TARGETS[@]}"

echo
echo "  Итог быстрой проверки"
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
  printf '  %s\n\n' "$(g 'ЗЕЛЁНОЕ (быстрая проверка)')"
else
  printf '  %s  - проверок со словом НЕТ: %s\n\n' "$(r 'КРАСНОЕ')" "$FAIL"
fi

[ "$FAIL" -eq 0 ]
