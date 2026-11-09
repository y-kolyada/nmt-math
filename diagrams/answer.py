#!/usr/bin/env python3
"""Recompute the answer of a trainer task from the numbers of its condition.

    python3 diagrams/answer.py ID 'EXPR'

A task with a figure carries data-claim="ID". EXPR is the computation its
condition allows (Python, with math imported). The script prints the computed
answer when the task agrees with it on every language page: the data-answer of
a short task, or the text of the chosen option of a choice task. Otherwise it
prints the disagreement. tools/claims.tsv calls it, one line per task, so a
task whose answer cannot be computed from its own text turns the check red.
"""
import math
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ('uk', 'ru')


def fmt(v):
    if isinstance(v, str):
        return v
    s = '%g' % round(v, 6)
    return s.replace('.', ',')


def task(lang, tid):
    for page in sorted((ROOT / lang).glob('*.html')):
        text = page.read_text(encoding='utf-8')
        m = re.search(r'<div class="task" data-kind="(\w+)" data-answer="([^"]*)"[^>]*data-claim="%s"' % re.escape(tid), text)
        if m:
            end = text.find('<p class="law-ref">', m.end())
            return m.group(1), m.group(2), text[m.end():end]
    return None


def main():
    tid, expr = sys.argv[1], sys.argv[2]
    value = fmt(eval(expr, {'math': math}))
    bad = []
    for lang in LANGS:
        found = task(lang, tid)
        if not found:
            bad.append('%s: нет задачи' % lang)
            continue
        kind, answer, body = found
        if kind == 'choice':
            m = re.search(r'data-opt="%s">%s · ([^<]*)</button>' % (answer, answer), body)
            got = m.group(1).split(' ')[0].rstrip('°') if m else '?'
        else:
            got = answer
        if got != value:
            bad.append('%s: на странице %s' % (lang, got))
    print(value if not bad else 'вычислено %s, %s' % (value, '; '.join(bad)))


if __name__ == '__main__':
    main()
