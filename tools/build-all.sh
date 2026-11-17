#!/usr/bin/env bash
# The generators of a site in their one order. Each one rewrites pages that the
# next one reads, so the order is part of the result:
#   build-nav        the shell: menu, switcher, labels, asset versions
#   build-math       formulas
#   build-frequency  the frequency line on block pages (study, with a slice)
#   build-sources    the exam links section on block pages (study, with a slice)
#   build-meta       the head block and the page data, counted from the body
#                    the generators above have finished writing
#   build-search     the search index, read from the finished pages
# build-meta before build-frequency left the page data stale and red
# (nmt-enlang, 2026-11-17). build-terms is not here: term cards are placed by
# the author of a page, not regenerated on every build.
#     ./tools/build-all.sh
set -euo pipefail
cd "$(dirname "$0")/.."
for g in build-nav build-math build-frequency build-sources build-meta build-search; do
  python3 tools/$g.py | grep -E 'ЗЕЛЁНОЕ|КРАСНОЕ|изменено|переписано|ошиб|не найден|нет ' || true
done
