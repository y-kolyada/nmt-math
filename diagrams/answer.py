#!/usr/bin/env python3
"""Recompute the answer of a trainer task from the numbers of its condition.

    python3 diagrams/answer.py ID 'EXPR'

A task with a figure carries data-claim="ID". EXPR is the computation its
condition allows (Python, with math imported). The script prints the computed
answer when the task agrees with it on every language page: the data-answer of
a short task, or the text of the chosen option of a choice task. Otherwise it
prints the disagreement. tools/claims.tsv calls it, one line per task, so a
task whose answer cannot be computed from its own text turns the check red.

    python3 diagrams/answer.py --figure ID 'EXPR'

A task of the class "data on the figure" gives its numbers only on the figure.
EXPR is computed over the names of DATA in the generator diagrams/ID.py. The
script also checks that every number of DATA is a label of the baked figure and
is named in its aria-label, and that it is absent from the condition text. A
choice whose options are formulas compares the whole option text when EXPR
gives a string.
"""
import importlib.util
import math
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
LANGS = ('uk', 'ru', 'en', 'de')
# English writes a decimal point where Ukrainian, Russian and German write a comma.
POINT = {'uk': ',', 'ru': ',', 'en': '.', 'de': ','}


def fmt(v, lang='uk'):
    if isinstance(v, str):
        return v
    s = '%g' % round(v, 6)
    return s.replace('.', POINT[lang])


def translated(lang, tid):
    """The block of the task exists in this language and is not a stub."""
    page = ROOT / lang / (tid[:2] + '.html')
    return page.is_file() and 'stub-card' not in page.read_text(encoding='utf-8')


def task(lang, tid):
    for page in sorted((ROOT / lang).glob('*.html')):
        text = page.read_text(encoding='utf-8')
        m = re.search(r'<div class="task" data-kind="(\w+)" data-answer="([^"]*)"[^>]*data-claim="%s"' % re.escape(tid), text)
        if m:
            end = text.find('<p class="law-ref">', m.end())
            return m.group(1), m.group(2), text[m.end():end]
    return None


def numbers(s, lang='uk'):
    """The unsigned numbers written in a piece of text, decimal separator kept."""
    return set(re.findall(r'\d+(?:%s\d+)?' % re.escape(POINT[lang]), s))


def data(tid):
    sys.path.insert(0, str(HERE))
    spec = importlib.util.spec_from_file_location(tid.replace('-', '_'), HERE / (tid + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DATA


def figure_faults(lang, tid, body, values):
    """Where a number of DATA is missing from the figure or leaks into the condition."""
    m = re.search(r'<!-- fig:%s -->(.*?)<!-- /fig:%s -->' % (tid, tid), body, re.S)
    if not m:
        return ['%s: рисунок не запечён' % lang]
    svg = m.group(1)
    labels = numbers(' '.join(re.findall(r'<text[^>]*>([^<]*)</text>', svg)), lang)
    aria = numbers(' '.join(re.findall(r'aria-label="([^"]*)"', svg)), lang)
    head = body[:m.start()]
    head = re.sub(r'<p class="task-(?:kind|class)">.*?</p>', '', head, flags=re.S)
    cond = numbers(re.sub(r'<[^>]+>', ' ', head), lang)
    bad = []
    for name, v in values.items():
        s = fmt(abs(v), lang)
        if s not in labels:
            bad.append('%s: %s = %s нет подписью на рисунке' % (lang, name, s))
        if s not in aria:
            bad.append('%s: %s = %s нет в aria-label' % (lang, name, s))
        if s in cond:
            bad.append('%s: %s = %s есть в условии' % (lang, name, s))
    return bad


def main():
    figure = sys.argv[1] == '--figure'
    tid, expr = sys.argv[1 + figure], sys.argv[2 + figure]
    names = {'math': math}
    if figure:
        values = data(tid)
        names.update(values)
    raw = eval(expr, names)
    value = fmt(raw)
    bad = []
    for lang in LANGS:
        # A language whose block is still a stub has no task to check yet.
        if lang != 'uk' and not translated(lang, tid):
            continue
        found = task(lang, tid)
        if not found:
            bad.append('%s: нет задачи' % lang)
            continue
        kind, answer, body = found
        if kind == 'choice':
            m = re.search(r'data-opt="%s">%s · ([^<]*)</button>' % (answer, answer), body)
            got = m.group(1) if m else '?'
            if not isinstance(raw, str):
                got = got.split(' ')[0].rstrip('°').replace('−', '-')
        else:
            got = answer
        if got != fmt(raw, lang):
            bad.append('%s: на странице %s' % (lang, got))
        if figure:
            bad += figure_faults(lang, tid, body, values)
    print(value if not bad else 'вычислено %s, %s' % (value, '; '.join(bad)))


if __name__ == '__main__':
    main()
