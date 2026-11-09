#!/usr/bin/env python3
"""Law frequency: how many trainer tasks lean on each law, printed into the pages.

    python3 tools/build-frequency.py           write the lines into the pages
    python3 tools/build-frequency.py --check   red if a printed number drifted

Study profile only (profiles/study.md). Every task of the trainer names its law
in `<p class="law-ref">` with a link to the law's frame, its limit or its
concept. This tool counts those links and prints, between markers it owns:

  * in each block, inside "Що в тебе є після цієї сторінки", one line: how many
    tasks the page holds and which laws they lean on, most used first;
  * on the landing page, a summary by block and the laws used most across the
    site, if the page carries `<!-- freq-summary --><!-- /freq-summary -->`.

WHY A GENERATOR. A count written by hand becomes a lie with the first new task.
WHY THE CAPTION SAYS "ON THIS SITE". The numbers say how the site trains, not
what the exam asks; the exam slice (real NMT variants) is a separate source,
and until it exists the line must not read as "what matters on the NMT".

Output is Russian: it speaks to the person who accepts the work.
"""

import html
import pathlib
import re
import sys

import siteconf

PROFILE = siteconf.profile()
SAY = {
    'uk': {'line': 'Частота на цьому сайті, а не на НМТ: на цій сторінці %d %s тренажера, і вони спираються на такі закони: %s.',
           'none': 'На цій сторінці задач тренажера немає.',
           'tasks': ('задача', 'задачі', 'задач'),
           'head': 'Частота законів на сайті',
           'intro': 'Скільки задач тренажера спирається на кожен закон. Це частота <strong>на цьому сайті</strong>, а не на НМТ: '
                    'вона показує, як сайт тренує, а не що питає екзамен. Зріз реальних варіантів НМТ 2024-2026 стане поруч, коли буде зроблений.',
           'total': 'Усього задач тренажера: %d, законів, на які вони спираються: %d.',
           'blocks': 'За блоками',
           'top': 'Закони, на які спирається найбільше задач',
           'block': '%s: %d %s, найчастіше - %s',
           'even': 'кожен закон по одній задачі', 'and': ' та '},
    'ru': {'line': 'Частота на этом сайте, а не на НМТ: на этой странице %d %s тренажёра, и они опираются на такие законы: %s.',
           'none': 'На этой странице задач тренажёра нет.',
           'tasks': ('задача', 'задачи', 'задач'),
           'head': 'Частота законов на сайте',
           'intro': 'Сколько задач тренажёра опирается на каждый закон. Это частота <strong>на этом сайте</strong>, а не на НМТ: '
                    'она показывает, как сайт тренирует, а не что спрашивает экзамен. Срез реальных вариантов НМТ 2024-2026 встанет рядом, когда будет сделан.',
           'total': 'Всего задач тренажёра: %d, законов, на которые они опираются: %d.',
           'blocks': 'По блокам',
           'top': 'Законы, на которые опирается больше всего задач',
           'block': '%s: %d %s, чаще всего - %s',
           'even': 'каждый закон по одной задаче', 'and': ' и '},
}
TASK = re.compile(r'<div class="task"[^>]*>(.*?)<div class="solution">', re.S)
LAW_REF = re.compile(r'<p class="law-ref">(.*?)</p>', re.S)
LINK = re.compile(r'<a\b[^>]*href="([^"#]*)#([^"]+)"[^>]*>(.*?)</a>', re.S)
# A tag may hold '>' inside a quoted attribute (data-tex="a > 0").
TAG = re.compile(r'<(?:[^>"]|"[^"]*")*>')
FREQ = re.compile(r'\n?\s*<!-- freq -->.*?<!-- /freq -->', re.S)
SUMMARY = re.compile(r'(<!-- freq-summary -->).*?(<!-- /freq-summary -->)', re.S)


def plain(s):
    s = re.sub(r'<annotation[^>]*>.*?</annotation>', '', s, flags=re.S)
    s = re.sub(r'<span class="term-card".*?</span></span></span>', '', s, flags=re.S)
    return ' '.join(html.unescape(TAG.sub(' ', s)).split()).replace(' .', '.').replace(' ,', ',')


def plural(n, forms):
    if n % 10 == 1 and n % 100 != 11:
        return forms[0]
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return forms[1]
    return forms[2]


def name_of(text, anchor, said):
    """A law frame names itself; any other target (a limit, a concept) is named
    by the words of the link, which say what exactly the task leans on there."""
    m = re.search(r'id="%s"' % re.escape(anchor), text)
    if not m:
        return None
    start = text.rfind('<', 0, m.start())
    chunk = text[start:start + 4000]
    law = re.search(r'<p class="law-name">(.*?)</p>', chunk, re.S)
    if chunk.startswith('<div class="law"') and law:
        return plain(law.group(1))
    words = plain(said)
    return words[:1].upper() + words[1:] if words else None


def collect(lang):
    pages = {p.stem: p.read_text(encoding='utf-8') for p in sorted(pathlib.Path(lang).glob('*.html'))}
    per_page, unresolved = {}, []
    for stem in PROFILE['topics']:
        text = pages.get(stem)
        if not text or 'stub-card' in text:
            continue
        counts, tasks = {}, 0
        for task in TASK.finditer(text):
            tasks += 1
            ref = LAW_REF.search(task.group(1))
            seen = set()
            for target, anchor, said in LINK.findall(ref.group(1) if ref else ''):
                page = pathlib.Path(target).stem if target else stem
                name = name_of(pages.get(page, ''), anchor, said)
                if not name:
                    unresolved.append('%s/%s.html: %s#%s' % (lang, stem, target, anchor))
                    continue
                if name not in seen:
                    seen.add(name)
                    counts[name] = counts.get(name, 0) + 1
        per_page[stem] = (tasks, counts)
    return pages, per_page, unresolved


def ranked(counts):
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


def block_line(lang, tasks, counts):
    say = SAY[lang]
    if not tasks:
        return say['none']
    laws = ', '.join('%s - %d' % (n, c) for n, c in ranked(counts))
    return say['line'] % (tasks, plural(tasks, say['tasks']), laws)


def bake(lang, check):
    pages, per_page, unresolved = collect(lang)
    say = SAY[lang]
    changed = []
    for stem, (tasks, counts) in per_page.items():
        text = pages[stem]
        new = FREQ.sub('', text)
        at = new.find('id="artifacts"')
        if at < 0:
            continue
        end = new.find('</div>', at)
        line = '\n    <!-- freq -->\n    <p class="dim law-freq" data-tasks="%d">%s</p>\n    <!-- /freq -->' % (tasks, block_line(lang, tasks, counts))
        new = new[:end + 6] + line + new[end + 6:]
        if new != text:
            changed.append('%s/%s.html' % (lang, stem))
            if not check:
                pathlib.Path(lang, stem + '.html').write_text(new, encoding='utf-8')
    landing = pages.get('index', '')
    if SUMMARY.search(landing):
        total = sum(t for t, _ in per_page.values())
        laws = {}
        for _, counts in per_page.values():
            for n, c in counts.items():
                laws[n] = laws.get(n, 0) + c
        rows = ['', '    <p>%s</p>' % say['intro'], '    <p>%s</p>' % (say['total'] % (total, len(laws))),
                '    <h3 id="freq-blocks">%s</h3>' % say['blocks'], '    <ul>']
        for stem, (tasks, counts) in per_page.items():
            title = plain(re.search(r'<h1[^>]*>(.*?)</h1>', pages[stem], re.S).group(1))
            best = max(counts.values()) if counts else 0
            leaders = [n for n, c in ranked(counts) if c == best]
            if best <= 1:
                item = '%s: %d %s, %s' % (title, tasks, plural(tasks, say['tasks']), say['even'])
            else:
                item = say['block'] % (title, tasks, plural(tasks, say['tasks']), say['and'].join(leaders[:2]))
            rows.append('      <li><a href="%s.html">%s</a></li>' % (stem, html.escape(item, quote=False)))
        rows += ['    </ul>', '    <h3 id="freq-top">%s</h3>' % say['top'], '    <ol>']
        rows += ['      <li>%s - %d</li>' % (html.escape(n, quote=False), c) for n, c in ranked(laws)[:10]]
        rows += ['    </ol>', '    ']
        new = SUMMARY.sub(lambda m: m.group(1) + '\n'.join(rows) + m.group(2), landing, count=1)
        if new != landing:
            changed.append('%s/index.html' % lang)
            if not check:
                pathlib.Path(lang, 'index.html').write_text(new, encoding='utf-8')
    return per_page, changed, unresolved


def main(argv):
    check = '--check' in argv
    print()
    print('  Частота законов в задачах тренажёра')
    print('  ' + '-' * 46)
    if PROFILE['name'] != 'study':
        print('  профиль %s: тренажёра нет, считать нечего' % PROFILE['name'])
        print('  ЗЕЛЁНОЕ')
        print()
        return 0
    bad = 0
    for lang in PROFILE['langs']:
        if not pathlib.Path(lang).is_dir():
            continue
        per_page, changed, unresolved = bake(lang, check)
        tasks = sum(t for t, _ in per_page.values())
        print('  %s: страниц с задачами %d, задач %d' % (lang, sum(1 for t, _ in per_page.values() if t), tasks))
        for u in unresolved:
            print('        -> ссылка на закон не найдена: %s' % u)
        bad += len(unresolved)
        if check and changed:
            for c in changed:
                print('        -> числа разошлись с задачами: %s' % c)
            bad += len(changed)
        elif changed:
            print('  переписано страниц: %d' % len(changed))
    print('  ' + '-' * 46)
    print('  ' + ('КРАСНОЕ' if bad else 'ЗЕЛЁНОЕ'))
    print()
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
