#!/usr/bin/env python3
"""Links to the exam tasks behind each block, one switchable block per year.

    python3 tools/build-sources.py           write the sections into the pages
    python3 tools/build-sources.py --check   red if a page drifted from the slice

Study profile only, and only when site.conf names a `slice` (tools/examslice.py).
For every block this prints, before "Що в тебе є після цієї сторінки", a numbered
section "Посилання на завдання із зовнішніх джерел": a block per source with its
own heading and lead, and inside it a block per year:

    <div class="ext-source" data-ext-source="nmt-ua" id="ext-nmt-ua">
      <div class="ext" data-ext="nmt-ua:2026" id="ext-nmt-ua-2026"> ... </div>

Each year is its own block, so the reader switches a source or a single year
off in the settings (assets/sources.js) and the search offers it as a filter of
its own (assets/search.js). Every page also carries
`<meta name="swa-sources" content="nmt-ua:2024 nmt-ua:2025 nmt-ua:2026">`, the
catalogue the settings panel is built from on pages without a section.

The tasks themselves are not copied: a link, the session, the number, and the
names of our laws the task leans on.

Output is Russian: it speaks to the person who accepts the work.
"""

import html
import pathlib
import re
import sys

import examslice
import siteconf

CONF = siteconf.conf()
PROFILE = siteconf.profile(CONF)
SOURCE = CONF.get('slice_source', 'nmt-ua')
# The section speaks of external sources in general: there may be several
# (another exam-preparation platform beside ZNO-ONLINE). What belongs to one
# source - its heading and its lead - lives in its own block and leaves the
# page with it when the reader switches the source off.
SAY = {
    'uk': {'head': 'Посилання на завдання із зовнішніх джерел',
           'intro': 'Реальні завдання з інших сайтів підготовки до НМТ, які спираються на закони цього блоку. '
                    'Умову читай на сайті джерела за посиланням, розмітка законами - наша. Джерела й роки вмикаються '
                    'і вимикаються в налаштуваннях (шестерня вгорі).',
           'off': 'Усі зовнішні джерела вимкнені в налаштуваннях.',
           'item': '%s сесія, завдання %s', 'fig': 'з рисунком',
           'sources': {'nmt-ua': {'head': 'НМТ на сайті ЗНО-ОНЛАЙН (zno.osvita.ua)', 'year': 'НМТ %s',
                                  'lead': 'Завдання основних сесій НМТ %s з сайту ЗНО-ОНЛАЙН, по роках. '
                                          'Кожен рік вмикається окремо.'}}},
    'ru': {'head': 'Ссылки на задания из внешних источников',
           'intro': 'Реальные задания с других сайтов подготовки к НМТ, которые опираются на законы этого блока. '
                    'Условие читай на сайте источника по ссылке, разметка законами - наша. Источники и годы включаются '
                    'и выключаются в настройках (шестерёнка вверху).',
           'off': 'Все внешние источники выключены в настройках.',
           'item': '%s сессия, задание %s', 'fig': 'с рисунком',
           'sources': {'nmt-ua': {'head': 'НМТ на сайте ЗНО-ОНЛАЙН (zno.osvita.ua)', 'year': 'НМТ %s',
                                  'lead': 'Задания основных сессий НМТ %s с сайта ЗНО-ОНЛАЙН, по годам. '
                                          'Каждый год включается отдельно.'}}},
}
SECTION = re.compile(r'\n?\s*<!-- sources -->.*?<!-- /sources -->', re.S)
META = re.compile(r'\n?<meta name="swa-sources" content="[^"]*">')
H2NUM = re.compile(r'<h2 id="[^"]+">(\d+)\s*·')


def section(lang, stem, rows, pages, missing, span):
    say = SAY.get(lang, SAY['uk'])
    src = say['sources'].get(SOURCE, {'head': SOURCE, 'year': '%s', 'lead': '%s'})
    by_year = {}
    for r in rows:
        mine = [t for t in r['tags'] if t.split(':')[0] == stem]
        if mine:
            by_year.setdefault(r['year'], []).append((r, mine))
    if not by_year:
        return ''
    text = pages[stem]
    before = text.split('id="artifacts"')[0]
    num = max([int(n) for n in H2NUM.findall(before)] or [0]) + 1
    out = ['', '    <!-- sources -->',
           '    <h2 id="external">%d · %s <a class="anchor-link" href="#external">#</a></h2>' % (num, say['head']),
           '    <p class="dim">%s</p>' % say['intro'],
           '    <p class="dim ext-off" hidden>%s</p>' % say['off'],
           '    <div class="ext-source" data-ext-source="%s" id="ext-%s">' % (SOURCE, SOURCE),
           '      <h3 class="ext-head">%s</h3>' % src['head'],
           '      <p class="dim ext-lead">%s</p>' % (src['lead'] % span)]
    for year in sorted(by_year, reverse=True):
        out += ['      <div class="ext" data-ext="%s:%s" id="ext-%s-%s">' % (SOURCE, year, SOURCE, year),
                '        <h4>%s</h4>' % (src['year'] % year), '        <ul>']
        for r, mine in sorted(by_year[year], key=lambda x: (x[0]['session'], int(x[0]['n']))):
            names = ', '.join(examslice.name_of(t, pages, lang, missing) for t in mine)
            fig = ' (%s)' % say['fig'] if r.get('figure') == 'yes' else ''
            out.append('          <li><a href="%s" rel="noopener" target="_blank">%s</a>%s - %s</li>'
                       % (html.escape(r['url'], quote=True), say['item'] % (r['session'], r['n']), fig, html.escape(names, quote=False)))
        out += ['        </ul>', '      </div>']
    out += ['    </div>', '    <!-- /sources -->']
    return '\n'.join(out)


def main(argv):
    check = '--check' in argv
    print()
    print('  Ссылки на задания экзамена по блокам')
    print('  ' + '-' * 46)
    rows, missing = examslice.load(CONF) if PROFILE['name'] == 'study' else (None, {})
    if not rows:
        print('  среза экзамена нет (site.conf: slice), печатать нечего')
        print('  ЗЕЛЁНОЕ')
        print()
        return 0
    all_years = sorted({r['year'] for r in rows})
    catalogue = ' '.join('%s:%s' % (SOURCE, y) for y in all_years)
    span = all_years[0] if len(all_years) == 1 else '%s-%s' % (all_years[0], all_years[-1])
    changed = []
    for lang in PROFILE['langs']:
        if not pathlib.Path(lang).is_dir():
            continue
        pages = {p.stem: p.read_text(encoding='utf-8') for p in sorted(pathlib.Path(lang).glob('*.html'))}
        for stem, text in pages.items():
            new = META.sub('', text)
            new = new.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="swa-sources" content="%s">' % catalogue, 1)
            if stem in PROFILE['topics'] and 'stub-card' not in new:
                new = SECTION.sub('', new)
                block = section(lang, stem, rows, {**pages, stem: new}, missing, span)
                at = new.find('<h2 id="artifacts">')
                if block and at >= 0:
                    new = new[:at].rstrip() + block + '\n\n    ' + new[at:]
            if new != text:
                changed.append('%s/%s.html' % (lang, stem))
                if not check:
                    pathlib.Path(lang, stem + '.html').write_text(new, encoding='utf-8')
    if check and changed:
        for c in changed:
            print('        -> раздел ссылок разошёлся со срезом: %s' % c)
    else:
        print('  заданий в срезе: %d, источник %s, годы: %s' % (len(rows), SOURCE, catalogue))
        print('  переписано страниц: %d' % len(changed))
    print('  ' + '-' * 46)
    print('  ' + ('КРАСНОЕ' if check and changed else 'ЗЕЛЁНОЕ'))
    print()
    return 1 if check and changed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
