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

import examslice
import siteconf

PROFILE = siteconf.profile()
SAY = {
    'uk': {'line': 'Частота на цьому сайті, а не на НМТ: на цій сторінці %d %s тренажера, і вони спираються на такі закони: %s.',
           'none': 'На цій сторінці задач тренажера немає.',
           'tasks': ('задача', 'задачі', 'задач'),
           'head': 'Частота законів на сайті',
           'intro': 'Скільки задач тренажера спирається на кожен закон. Це частота <strong>на цьому сайті</strong>, а не на НМТ: '
                    'вона показує, як сайт тренує, а не що питає екзамен. Що питає екзамен, показує зріз реальних варіантів НМТ нижче, якщо він є.',
           'total': 'Усього задач тренажера: %d, законів, на які вони спираються: %d.',
           'blocks': 'За блоками',
           'top': 'Закони, на які спирається найбільше задач',
           'block': '%s: %d %s, найчастіше - %s',
           'even': 'кожен закон по одній задачі', 'and': ' та ',
           'exam': 'У реальних варіантах НМТ %s цей блок потрібен у %d %s з %d: %s.',
           'exam0': 'У реальних варіантах НМТ %s цей блок не знадобився в жодному з %d завдань.',
           'xhead': 'Реальні варіанти НМТ %s', 'xintro': 'Ті самі закони, але в %d завданнях шести основних сесій НМТ %s: друга цифра поруч із першою. Розмітка наша, завдання - за посиланнями в кожному блоці.',
           'xblocks': 'Завдань НМТ за блоками', 'xtop': 'Закони, на які спирається найбільше завдань НМТ',
           'xmiss': 'Закони НМТ, яких на сайті ще немає', 'xmissintro': 'Ці теми трапилися в завданнях НМТ, а окремого закону на сайті для них поки немає. Це вхід для наступних блоків, а не готовий матеріал.',
           'xitem': '%s: %d %s', 'xtask': ('завдання', 'завдання', 'завдань'), 'xloc': ('завданні', 'завданнях', 'завданнях'),
           'xstub': 'Блоки %s ще не перекладені: їхніх законів у цих списках немає. Їхні числа - на посадковій сторінці мови-джерела.'},
    'ru': {'line': 'Частота на этом сайте, а не на НМТ: на этой странице %d %s тренажёра, и они опираются на такие законы: %s.',
           'none': 'На этой странице задач тренажёра нет.',
           'tasks': ('задача', 'задачи', 'задач'),
           'head': 'Частота законов на сайте',
           'intro': 'Сколько задач тренажёра опирается на каждый закон. Это частота <strong>на этом сайте</strong>, а не на НМТ: '
                    'она показывает, как сайт тренирует, а не что спрашивает экзамен. Что спрашивает экзамен, показывает срез реальных вариантов НМТ ниже, если он есть.',
           'total': 'Всего задач тренажёра: %d, законов, на которые они опираются: %d.',
           'blocks': 'По блокам',
           'top': 'Законы, на которые опирается больше всего задач',
           'block': '%s: %d %s, чаще всего - %s',
           'even': 'каждый закон по одной задаче', 'and': ' и ',
           'exam': 'В реальных вариантах НМТ %s этот блок нужен в %d %s из %d: %s.',
           'exam0': 'В реальных вариантах НМТ %s этот блок не понадобился ни в одном из %d заданий.',
           'xhead': 'Реальные варианты НМТ %s', 'xintro': 'Те же законы, но в %d заданиях шести основных сессий НМТ %s: вторая цифра рядом с первой. Разметка наша, задания - по ссылкам в каждом блоке.',
           'xblocks': 'Заданий НМТ по блокам', 'xtop': 'Законы, на которые опирается больше всего заданий НМТ',
           'xmiss': 'Законы НМТ, которых на сайте ещё нет', 'xmissintro': 'Эти темы встретились в заданиях НМТ, а отдельного закона на сайте для них пока нет. Это вход для следующих блоков, а не готовый материал.',
           'xitem': '%s: %d %s', 'xtask': ('задание', 'задания', 'заданий'), 'xloc': ('задании', 'заданиях', 'заданиях'),
           'xstub': 'Блоки %s ещё не переведены: их законов в этих списках нет. Их числа - на посадочной странице языка-источника.'},
    # English has two forms where Ukrainian and Russian have three: plural() reads the length.
    'en': {'line': 'Frequency on this site, not in the NMT: this page has %d trainer %s, and they lean on these laws: %s.',
           'none': 'This page has no trainer tasks.',
           'tasks': ('task', 'tasks'),
           'head': 'Frequency of laws on the site',
           'intro': 'How many trainer tasks lean on each law. This is the frequency <strong>on this site</strong>, not in the NMT: '
                    'it shows how the site trains, not what the exam asks. What the exam asks is shown by the slice of real NMT papers below, if there is one.',
           'total': 'Trainer tasks in all: %d; laws they lean on: %d.',
           'blocks': 'By block',
           'top': 'Laws that the most tasks lean on',
           'block': '%s: %d %s, most often - %s',
           'even': 'one task for each law', 'and': ' and ',
           'exam': 'In real NMT papers of %s this block is needed in %d %s out of %d: %s.',
           'exam0': 'In real NMT papers of %s this block was not needed in any of the %d tasks.',
           'xhead': 'Real NMT papers of %s', 'xintro': 'The same laws, but in %d tasks of the six main NMT sessions of %s: the second number next to the first. The tagging is ours, the tasks are behind the links in each block.',
           'xblocks': 'NMT tasks by block', 'xtop': 'Laws that the most NMT tasks lean on',
           'xmiss': 'NMT laws the site does not have yet', 'xmissintro': 'These topics came up in NMT tasks, but the site has no law of its own for them yet. This is input for the next blocks, not finished material.',
           'xitem': '%s: %d %s', 'xtask': ('task', 'tasks'), 'xloc': ('task', 'tasks'),
           'xstub': 'Blocks %s are not translated yet: their laws are not in these lists. Their counts are on the landing page of the source language.'},
    # German, like English, has two forms.
    'de': {'line': 'Häufigkeit auf dieser Seite, nicht im NMT: diese Seite hat %d %s im Trainer, und sie stützen sich auf diese Gesetze: %s.',
           'none': 'Diese Seite hat keine Aufgaben im Trainer.',
           'tasks': ('Aufgabe', 'Aufgaben'),
           'head': 'Häufigkeit der Gesetze auf der Seite',
           'intro': 'Wie viele Aufgaben im Trainer sich auf jedes Gesetz stützen. Das ist die Häufigkeit <strong>auf dieser Seite</strong>, nicht im NMT: '
                    'sie zeigt, wie die Seite trainiert, nicht, was die Prüfung fragt. Was die Prüfung fragt, zeigt der Schnitt durch echte NMT-Varianten weiter unten, falls es ihn gibt.',
           'total': 'Aufgaben im Trainer insgesamt: %d; Gesetze, auf die sie sich stützen: %d.',
           'blocks': 'Nach Blöcken',
           'top': 'Gesetze, auf die sich die meisten Aufgaben stützen',
           'block': '%s: %d %s, am häufigsten - %s',
           'even': 'jedes Gesetz mit einer Aufgabe', 'and': ' und ',
           'exam': 'In echten NMT-Varianten %s wird dieser Block in %d %s von %d gebraucht: %s.',
           'exam0': 'In echten NMT-Varianten %s wurde dieser Block in keiner der %d Aufgaben gebraucht.',
           'xhead': 'Echte NMT-Varianten %s', 'xintro': 'Dieselben Gesetze, aber in %d Aufgaben der sechs Hauptsitzungen des NMT %s: die zweite Zahl neben der ersten. Die Zuordnung ist unsere, die Aufgaben stehen hinter den Links in jedem Block.',
           'xblocks': 'NMT-Aufgaben nach Blöcken', 'xtop': 'Gesetze, auf die sich die meisten NMT-Aufgaben stützen',
           'xmiss': 'NMT-Gesetze, die die Seite noch nicht hat', 'xmissintro': 'Diese Themen kamen in NMT-Aufgaben vor, aber die Seite hat für sie noch kein eigenes Gesetz. Das ist ein Eingang für die nächsten Blöcke, kein fertiges Material.',
           'xitem': '%s: %d %s', 'xtask': ('Aufgabe', 'Aufgaben'), 'xloc': ('Aufgabe', 'Aufgaben'),
           'xstub': 'Die Blöcke %s sind noch nicht übersetzt: ihre Gesetze fehlen in diesen Listen. Ihre Zahlen stehen auf der Startseite der Ausgangssprache.'},
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
    if len(forms) == 2:
        return forms[0] if n == 1 else forms[1]
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
    # A corollary counts for its law: the same line, not a new law.
    cor = re.match(r'<div class="corollary"[^>]*data-law="([^"]+)"', chunk)
    if cor:
        return name_of(text, cor.group(1), said)
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


def exam_counts(rows, pages, lang, missing):
    """Per block: tasks of the slice that lean on it and how often each tag does.

    A corollary is counted for its law (examslice.parent); a task that leans on
    a law twice, once directly and once through its corollary, counts once.
    """
    per_block, per_tag = {}, {}
    for r in rows:
        blocks = set()
        for tag in dict.fromkeys(examslice.parent(t, pages) for t in r['tags']):
            name = examslice.name_of(tag, pages, lang, missing)
            per_tag[(tag, name)] = per_tag.get((tag, name), 0) + 1
            where = tag.split(':')[0]
            if where != 'missing':
                blocks.add(where)
                per_block.setdefault(where, {})
                per_block[where][name] = per_block[where].get(name, 0) + 1
        for b in blocks:
            per_block[b]['__tasks__'] = per_block[b].get('__tasks__', 0) + 1
    return per_block, per_tag


def bake(lang, check):
    pages, per_page, unresolved = collect(lang)
    say = SAY[lang]
    rows, missing = examslice.load()
    exam = exam_counts(rows, pages, lang, missing) if rows else None
    # A page that is still a stub in this language has no laws to name: its
    # tags are not a defect here, and the landing leaves them out and says so.
    stubs = sorted(stem for stem in PROFILE['topics'] if 'stub-card' in pages.get(stem, ''))
    for r in rows or []:
        for tag in r['tags']:
            if tag.split(':')[0] in stubs:
                continue
            if not tag.startswith('missing:') and not examslice.resolved(tag, pages, lang, missing):
                unresolved.append('срез %s/%s №%s: %s' % (r['year'], r['test'], r['n'], tag))
    changed = []
    for stem, (tasks, counts) in per_page.items():
        text = pages[stem]
        new = FREQ.sub('', text)
        at = new.find('id="artifacts"')
        if at < 0:
            continue
        end = new.find('</div>', at)
        said = block_line(lang, tasks, counts)
        if exam:
            mine = dict(exam[0].get(stem, {}))
            n = mine.pop('__tasks__', 0)
            if n:
                said += ' ' + say['exam'] % (examslice.years(rows), n, plural(n, say['xloc']), len(rows),
                                             ', '.join('%s - %d' % kv for kv in ranked(mine)))
            else:
                said += ' ' + say['exam0'] % (examslice.years(rows), len(rows))
        line = '\n    <!-- freq -->\n    <p class="dim law-freq" data-tasks="%d">%s</p>\n    <!-- /freq -->' % (tasks, said)
        new = new[:end + 6] + line + new[end + 6:]
        if new != text:
            changed.append('%s/%s.html' % (lang, stem))
            if not check:
                pathlib.Path(lang, stem + '.html').write_text(new, encoding='utf-8')
    landing = pages.get('index', '')
    exrows = rows
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
        rows += ['    </ol>']
        if exam:
            yrs = examslice.years(exrows)
            per_block, per_tag = exam
            rows += ['    <h3 id="freq-nmt">%s</h3>' % (say['xhead'] % yrs),
                     '    <p>%s</p>' % (say['xintro'] % (len(exrows), yrs)),
                     '    <h3 id="freq-nmt-blocks">%s</h3>' % say['xblocks'], '    <ul>']
            for stem in per_page:
                n = per_block.get(stem, {}).get('__tasks__', 0)
                title = plain(re.search(r'<h1[^>]*>(.*?)</h1>', pages[stem], re.S).group(1))
                rows.append('      <li><a href="%s.html">%s</a></li>' % (stem, html.escape(say['xitem'] % (title, n, plural(n, say['xtask'])), quote=False)))
            rows += ['    </ul>', '    <h3 id="freq-nmt-top">%s</h3>' % say['xtop'], '    <ol>']
            known = [(name, c) for (tag, name), c in per_tag.items()
                     if not tag.startswith('missing:') and ':method-' not in tag and tag.split(':')[0] not in stubs]
            rows += ['      <li>%s - %d</li>' % (html.escape(n, quote=False), c) for n, c in sorted(known, key=lambda kv: (-kv[1], kv[0]))[:10]]
            rows += ['    </ol>']
            if stubs:
                rows += ['    <p class="dim">%s</p>' % (say['xstub'] % ', '.join(str(int(x)) for x in stubs))]
            gaps = [(name, c) for (tag, name), c in per_tag.items() if tag.startswith('missing:')]
            # The list of gaps exists only while there are gaps.
            if gaps:
                rows += ['    <h3 id="freq-missing">%s</h3>' % say['xmiss'], '    <p>%s</p>' % say['xmissintro'], '    <ul>']
                rows += ['      <li>%s - %d</li>' % (html.escape(n, quote=False), c) for n, c in sorted(gaps, key=lambda kv: (-kv[1], kv[0]))]
                rows += ['    </ul>']
        rows += ['    ']
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
