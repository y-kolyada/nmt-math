#!/usr/bin/env python3
"""The menu: one list of titles per language folder, and no placeholder left.

    python3 tools/check-menu.py

The menu is copied into every page. A translation order translates the copy on
its own pages while later pages are still stubs, so a folder can end up with
the block titles on some pages and «Розділ 6» on others; nothing else compares
the copies, and a reader sees it at once. Two things are checked per folder:

1. every page gives each numbered page of the menu the same title;
2. no title is a stub's placeholder (Раздел N, Розділ N, Блок N, Section N,
   Block N, Abschnitt N) once that page has a title of its own - a freshly
   stamped site, where the page is still the stub, stays green.

Exits 1 on any finding. Output is Russian: it speaks to the person who accepts
the work.
"""

import html
import os
import re
import sys

import siteconf

LANGS = siteconf.profile()['langs']
NAV = re.compile(r'<nav class="contents".*?</nav>', re.S)
ITEM = re.compile(r'<a href="(\d\d)\.html"[^>]*><span class="num">\d+</span>([^<]*)</a>')
H1 = re.compile(r'<h1[^>]*>(.*?)</h1>', re.S)
STUB = re.compile(r'^(Раздел|Розділ|Блок|Section|Block|Abschnitt) \d+$')

bad = []
checked = 0
for lang in LANGS:
    if not os.path.isdir(lang):
        continue
    titles = {}  # NN -> {title: [pages]}
    for name in sorted(os.listdir(lang)):
        if not name.endswith('.html'):
            continue
        nav = NAV.search(open(os.path.join(lang, name), encoding='utf-8').read())
        if not nav:
            bad.append('%s/%s: отсутствует обязательное главное меню <nav class="contents">' % (lang, name))
            continue
        checked += 1
        for num, title in ITEM.findall(nav.group(0)):
            titles.setdefault(num, {}).setdefault(html.unescape(title).strip(), []).append(name)
    for num, seen in sorted(titles.items()):
        if len(seen) > 1:
            parts = ['«%s» на %d' % (t, len(p)) for t, p in sorted(seen.items(), key=lambda x: -len(x[1]))]
            bad.append('%s: пункт %s назван по-разному: %s' % (lang, num, ', '.join(parts)))
        page = os.path.join(lang, num + '.html')
        h1 = H1.search(open(page, encoding='utf-8').read()) if os.path.exists(page) else None
        own = html.unescape(re.sub(r'<[^>]+>', '', h1.group(1))).strip() if h1 else ''
        for title, pages in seen.items():
            if STUB.match(title) and own and not STUB.match(own):
                bad.append('%s: пункт %s - заглушка «%s» на %d стр., а у страницы уже есть заголовок «%s»'
                           % (lang, num, title, len(pages), own))

print()
print('  Проверка меню: одни названия, без заглушек')
print('  ' + '-' * 46)
print('  страниц с меню: %d' % checked)
print('  в браке:        %d' % len(bad))
for line in bad[:20]:
    print('        -> ' + line)
print('  ' + '-' * 46)
print('  ' + ('КРАСНОЕ' if bad else 'ЗЕЛЁНОЕ'))
print()
sys.exit(1 if bad else 0)
