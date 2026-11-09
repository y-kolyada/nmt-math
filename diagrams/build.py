#!/usr/bin/env python3
"""Bake the figures of nmt-math into the pages.

    python3 diagrams/build.py          every language folder
    python3 diagrams/build.py --check  say whether a baked figure drifted

A page marks a figure with an empty pair of comments:

    <!-- fig:05-shift --><!-- /fig:05-shift -->

and this script fills the space between them with the inline SVG computed by
diagrams/05-shift.py and its caption. Captions are numbered through the
language folder in the order the checks read the pages (sorted file names),
so a figure added in the middle renumbers the rest by itself.

This script belongs to the site, not to the engine: it lives in diagrams/
beside the sources, because the series forbids a site to edit tools/.
"""
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
WORD = {'uk': 'Рисунок', 'ru': 'Рисунок'}
MARK = re.compile(r'<!-- fig:((?:[0-9]{2}|navigator)-[a-z0-9-]+) -->.*?<!-- /fig:\1 -->', re.S)


def load(fid):
    spec = importlib.util.spec_from_file_location(fid.replace('-', '_'), HERE / (fid + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def bake(lang):
    changed, count = 0, 0
    for page in sorted((ROOT / lang).glob('*.html')):
        text = page.read_text(encoding='utf-8')

        def fill(m):
            nonlocal count
            fid = m.group(1)
            count += 1
            fig, label, caption = load(fid).figure(lang)
            return ('<!-- fig:%s -->\n    <div class="box figure">\n      %s\n      <p class="dim">%s %d. %s</p>\n    </div>\n    <!-- /fig:%s -->'
                    % (fid, fig.svg(label), WORD[lang], count, caption, fid))
        new = MARK.sub(fill, text)
        if new != text:
            changed += 1
            if '--check' not in sys.argv:
                page.write_text(new, encoding='utf-8')
    return changed, count


def main():
    bad = 0
    for lang in ('uk', 'ru'):
        if not (ROOT / lang).is_dir():
            continue
        changed, count = bake(lang)
        print('  %s: рисунков %d, страниц изменено %d' % (lang, count, changed))
        if '--check' in sys.argv and changed:
            bad += 1
    print('  ' + ('КРАСНОЕ: рисунки разошлись с исходниками' if bad else 'ЗЕЛЁНОЕ'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
