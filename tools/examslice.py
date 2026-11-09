"""The exam slice of a study site: real exam tasks tagged with the site's laws.

A study site may keep, in a file named by `slice =` in site.conf, a table of
real exam tasks (one row per task) tagged with its own laws:

    year  session  test  n  form  figure  laws  url
    2026  1        846   8  choice  yes   12:law-vector  https://...

A tag is `NN:law-id` (a law frame on block NN), `NN:concept` (the concept
section of block NN) or `missing:topic` (the site has no law for it yet). Lines
`#missing<TAB>topic<TAB>uk name<TAB>ru name` give the topics their names.

The slice adds to the site and never overwrites it: the tools that read it
print a second number beside the site's own, and links to the originals in a
section of their own that the reader can switch off (assets/sources.js).
"""

import html
import pathlib
import re

import siteconf

TAG = re.compile(r'<(?:[^>"]|"[^"]*")*>')


def plain(s):
    s = re.sub(r'<annotation[^>]*>.*?</annotation>', '', s, flags=re.S)
    s = re.sub(r'<span class="term-card".*?</span></span></span>', '', s, flags=re.S)
    return ' '.join(html.unescape(TAG.sub(' ', s)).split()).replace(' .', '.').replace(' ,', ',')


def load(conf=None):
    """Rows of the slice and the names of missing topics, or (None, {}) without a slice."""
    conf = conf if conf is not None else siteconf.conf()
    path = conf.get('slice')
    if not path or not pathlib.Path(path).is_file():
        return None, {}
    rows, missing, head = [], {}, None
    for line in pathlib.Path(path).read_text(encoding='utf-8').splitlines():
        if line.startswith('#missing\t'):
            _, tag, uk, ru = (line.split('\t') + ['', ''])[:4]
            missing[tag] = {'uk': uk, 'ru': ru}
            continue
        if not line.strip() or line.startswith('#'):
            continue
        cells = line.split('\t')
        if head is None:
            head = cells
            continue
        row = dict(zip(head, cells))
        row['tags'] = row.get('laws', '').split()
        rows.append(row)
    return rows, missing


def name_of(tag, pages, lang, missing):
    """What a tag is called on this site, in the language of the pages."""
    where, _, what = tag.partition(':')
    if where == 'missing':
        return (missing.get(what, {}).get(lang) or what.replace('_', ' '))
    text = pages.get(where, '')
    if what == 'concept':
        m = re.search(r'<h2 id="concept">(.*?)</h2>', text, re.S)
        return re.sub(r'^\d+\s*·\s*', '', plain(m.group(1))).rstrip('#').strip() if m else tag
    m = re.search(r'<div class="law" id="%s">\s*<p class="law-name">(.*?)</p>' % re.escape(what), text, re.S)
    return plain(m.group(1)) if m else tag


def years(rows):
    ys = sorted({r['year'] for r in rows})
    return '%s-%s' % (ys[0], ys[-1]) if len(ys) > 1 else ys[0]
