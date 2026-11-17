#!/usr/bin/env python3
"""Build terms: normalize and synchronize 'Где встретилось:' cross-references in glossary.html.

Replaces legacy 'Где встретилось впервые:' with the canonical multi-page label
'Где встретилось:', and synchronizes page references based on actual in-page .term
usage across chapters (01-15), the navigator, and landing pages.

    python3 tools/build-terms.py
    python3 tools/build-terms.py --check
"""

import glob
import os
import re
import sys

import siteconf

SOURCE = siteconf.profile()['source']
GLOSSARY_PATH = os.path.join(SOURCE, 'glossary.html')
# Link names in the 'where it appears' line, in the source language.
WHERE = {'ru': {'index': 'Посадочная страница', 'navigator': 'Навигатор'},
         'uk': {'index': 'Посадкова сторінка', 'navigator': 'Навігатор'}}.get(SOURCE, {'index': 'Landing page', 'navigator': 'Navigator'})


def collect_term_pages():
    """Scans ru/*.html and returns term_id -> set of filenames where it appears."""
    pages_by_term = {}
    html_files = sorted(glob.glob(os.path.join(SOURCE, '*.html')))

    for fpath in html_files:
        fname = os.path.basename(fpath)
        if fname == 'glossary.html':
            continue

        with open(fpath, encoding='utf-8') as f:
            html = f.read()

        for m in re.finditer(r'<span class="term">.*?href="[^"]*#([^"]+)"', html, re.DOTALL):
            tid = m.group(1)
            pages_by_term.setdefault(tid, set()).add(fname)

    return pages_by_term


def main():
    check_mode = '--check' in sys.argv

    if not os.path.isfile(GLOSSARY_PATH):
        print()
        print('  Синхронизация сносок словаря («Где встретилось:»)')
        print('  ' + '-' * 46)
        print('  словарь ещё не создан')
        print('  ----------------------------------------------')
        print('  ЗЕЛЁНОЕ')
        print()
        return 0

    with open(GLOSSARY_PATH, encoding='utf-8') as f:
        content = f.read()

    term_blocks = re.findall(r'<div class="glossary-term"\s+id="([^"]+)">', content)
    if not term_blocks:
        print()
        print('  Синхронизация сносок словаря («Где встретилось:»)')
        print('  ' + '-' * 46)
        print('  словарь пуст: 0 терминов')
        print('  ----------------------------------------------')
        print('  ЗЕЛЁНОЕ')
        print()
        return 0

    legacy_count = len(re.findall(r'Где встретилось впервые:', content))
    pages_by_term = collect_term_pages()

    new_content = content
    # 1. Normalize legacy label
    if legacy_count > 0:
        new_content = re.sub(r'<strong>Где встретилось впервые:</strong>', '<strong>Где встретилось:</strong>', new_content)

    # 2. Check if missing page links should be appended to each term
    meta_pattern = re.compile(
        r'(<div class="glossary-term"\s+id="([^"]+)">.*?'
        r'<div class="glossary-meta">\s*.*?'
        r'<strong>Где встретилось:</strong>\s*)(.*?)(</div>)',
        re.DOTALL
    )

    enriched_terms = 0

    def enrich_meta(match):
        nonlocal enriched_terms
        prefix = match.group(1)
        term_id = match.group(2)
        existing_links_str = match.group(3).strip()
        suffix = match.group(4)

        needed_pages = pages_by_term.get(term_id, set())
        # Find which pages are already linked
        linked_pages = set(re.findall(r'href="([^"#]+)(?:#[^"]*)?"', existing_links_str))

        missing_pages = sorted(p for p in needed_pages if p not in linked_pages)
        if not missing_pages:
            return match.group(0)

        enriched_terms += 1
        new_links = []
        for p in missing_pages:
            if p == 'index.html':
                new_links.append('<a href="index.html">%s</a>' % WHERE['index'])
            elif p == 'navigator.html':
                new_links.append('<a href="navigator.html">%s</a>' % WHERE['navigator'])
            elif re.match(r'^\d{2}\.html$', p):
                new_links.append(f'<a href="{p}">Глава {p[:2]}</a>')
            else:
                new_links.append(f'<a href="{p}">{p}</a>')

        added_str = ', '.join(new_links)
        updated_links_str = existing_links_str
        if updated_links_str and not updated_links_str.endswith(','):
            updated_links_str += ', ' + added_str
        else:
            updated_links_str += ' ' + added_str

        return f"{prefix}{updated_links_str} {suffix}"

    new_content = meta_pattern.sub(enrich_meta, new_content)

    # 3. Synchronize chip counters in <nav class="chips">
    chips_match = re.search(r'(<nav class="chips"[^>]*>)(.*?)(</nav>)', new_content, re.DOTALL)
    chip_updates = 0
    if chips_match:
        chips_prefix = chips_match.group(1)
        chips_inner = chips_match.group(2)
        chips_suffix = chips_match.group(3)

        sections = re.split(r'(<h2 id="(?:ch-\d\d|block-[a-z0-9_-]+)">)', new_content)
        sec_counts = {}
        for i in range(1, len(sections), 2):
            tag = sections[i]
            sec_content = sections[i + 1]
            ch_id = re.search(r'id="((?:ch-\d\d|block-[a-z0-9_-]+))"', tag).group(1)
            cnt = len(re.findall(r'<div class="glossary-term"', sec_content))
            sec_counts[ch_id] = cnt

        def update_chip(m):
            nonlocal chip_updates
            c_prefix = m.group(1)
            ch_id = m.group(2)
            old_label = m.group(3).strip()
            c_suffix = m.group(4)
            base_title = re.sub(r'\s*\(\d+\)$', '', old_label)
            actual = sec_counts.get(ch_id, 0)
            new_label = f"{base_title} ({actual})"
            if new_label != old_label:
                chip_updates += 1
                return f"{c_prefix}{new_label}{c_suffix}"
            return m.group(0)

        new_chips_inner = re.sub(
            r'(<a href="#((?:ch-\d\d|block-[a-z0-9_-]+))">)(.*?)(</a>)',
            update_chip,
            chips_inner
        )
        if chip_updates > 0:
            new_content = new_content[:chips_match.start()] + chips_prefix + new_chips_inner + chips_suffix + new_content[chips_match.end():]

    changes_needed = legacy_count + enriched_terms + chip_updates

    print()
    print('  Синхронизация сносок словаря («Где встретилось:»)')
    print('  ' + '-' * 46)
    print(f'  терминов в словаре:               {len(term_blocks)}')
    print(f'  устаревших сносок «впервые:»:      {legacy_count}')
    print(f'  терминов с дополненными ссылками: {enriched_terms}')
    if chips_match:
        print(f'  чипов со скорректированным счетом: {chip_updates}')
    print('  ' + '-' * 46)

    if check_mode:
        if changes_needed > 0:
            print('  КРАСНОЕ  - запустите python3 tools/build-terms.py для синхронизации')
            print()
            return 1
        else:
            print('  ЗЕЛЁНОЕ')
            print()
            return 0
    else:
        if changes_needed > 0:
            with open(GLOSSARY_PATH, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'  успешно обновлено сносок и чипов: {changes_needed}')
        else:
            print('  все сноски и чипы каноничны и актуальны')
        print('  ЗЕЛЁНОЕ')
        print()
        return 0


if __name__ == '__main__':
    sys.exit(main())
