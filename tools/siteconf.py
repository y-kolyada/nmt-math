"""The site's own facts, read from site.conf, and the profile of its skeleton.

Every tool in tools/ is identical on every site of the series. What differs -
the name, the live address, the topic word on the amber chip, the storage key
and the release number - lives in one file, site.conf, next to the pages.

PROFILE. The series carries three families of sites with different skeletons.
`assess` is the engineering assessment track: four languages written from
Russian, fifteen sections (topics 01-09, examples 10-12, question banks 13-15)
and a navigator of nine engineering lenses. `study` is the school study track:
Ukrainian source, Russian second, thirteen blocks of laws and a navigator of
seven subject lenses. `practice` is the conductor's own practice with AI agents
and factories: Russian source, then Ukrainian and English, fifteen blocks of
laws under menu groups and eight lenses of practice (profiles/practice.md).
A site names its profile in site.conf (`profile = study`);
a site that names none is `assess`, so every site made before profiles existed
keeps exactly the numbers it was checked against. Any single key of a profile
can still be overridden in site.conf (`langs = uk ru en`).

The engine stays one: a fix to a tool reaches both families through sync.sh.
Only the numbers and names below differ, and they live here once instead of
as constants copied into ten tools. Two of them are switches rather than
numbers, so that a tool asks what a site has instead of what it is called:
`blocks` - the skeleton is blocks of laws with the trainer (study, practice),
and `exam` - the blocks are measured against an exam slice (study only).

    python3 tools/siteconf.py --json         the profile, for the node checks
    python3 tools/siteconf.py --get source   one key, for the bash checks
"""

import json
import pathlib
import sys

PROFILES = {
    'assess': {
        'langs': ['ru', 'en', 'uk', 'de'],
        'source': 'ru',
        'sections': 15,
        # Pages whose substantive h2 carry "N · Title".
        'topics': ['%02d' % n for n in range(1, 13)],
        # Question banks: fifty questions, FAQPage markup.
        'questions': ['13', '14', '15'],
        'lenses': ['lens-components', 'lens-code', 'lens-strength', 'lens-weaknesses',
                   'lens-ecosystem', 'lens-ai', 'lens-cloud', 'lens-devops', 'lens-sre'],
        'related': 'Связанные главы курса:',
        'blocks': False,
        'exam': False,
        'groups': {},
        'kinds': [['разбор темы (01-09)', ['%02d' % n for n in range(1, 10)]],
                  ['примеры (10-12)', ['10', '11', '12']],
                  ['банк вопросов (13-15)', ['13', '14', '15']],
                  ['словарь', ['glossary']],
                  ['посадочная', ['index']]],
    },
    'study': {
        'langs': ['uk', 'ru'],
        'source': 'uk',
        'sections': 13,
        'topics': ['%02d' % n for n in range(1, 14)],
        'questions': [],
        'lenses': ['lens-language', 'lens-laws', 'lens-proof', 'lens-scope',
                   'lens-limits', 'lens-links', 'lens-traps'],
        'related': "Пов'язані блоки курсу:",
        'blocks': True,
        'exam': True,
        'groups': {},
        'kinds': [['блок (01-13)', ['%02d' % n for n in range(1, 14)]],
                  ['словник', ['glossary']],
                  ['навігатор', ['navigator']],
                  ['посадкова', ['index']]],
    },
    'practice': {
        'langs': ['ru', 'uk', 'en'],
        'source': 'ru',
        'sections': 15,
        'topics': ['%02d' % n for n in range(1, 16)],
        'questions': [],
        'lenses': ['lens-failure', 'lens-record', 'lens-check', 'lens-roles',
                   'lens-perimeter', 'lens-cost', 'lens-scale', 'lens-tomorrow'],
        'related': 'Связанные блоки курса:',
        'blocks': True,
        'exam': False,
        # Menu captions: the first block of each group and its caption per
        # language. A caption is not an item, so the checks count only items.
        'groups': {
            'starts': [1, 3, 4, 7, 10, 13, 15],
            'ru': ['Проблема', 'Люди', 'Память', 'Работа', 'Оркестр', 'Цена', 'Фабрики'],
            'uk': ['Проблема', 'Люди', "Пам'ять", 'Робота', 'Оркестр', 'Ціна', 'Фабрики'],
            'en': ['Problem', 'People', 'Memory', 'Work', 'Orchestra', 'Cost', 'Factories'],
        },
        'kinds': [['блок (01-15)', ['%02d' % n for n in range(1, 16)]],
                  ['словарь', ['glossary']],
                  ['навигатор', ['navigator']],
                  ['посадочная', ['index']]],
    },
}

# Keys a site may override one by one, and how a site.conf line reads.
LISTS = ('langs', 'lenses', 'topics', 'questions')


def conf(path='site.conf'):
    out = {}
    text = pathlib.Path(path).read_text(encoding='utf-8')
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        name, _, value = line.partition('=')
        out[name.strip()] = value.strip()
    missing = [k for k in ('name', 'url', 'topic', 'key', 'version') if k not in out]
    if missing:
        raise SystemExit('site.conf: не хватает полей %s' % ', '.join(missing))
    return out


def profile(site=None):
    """The skeleton of this site: the profile it names, with its own overrides."""
    site = site if site is not None else conf()
    name = site.get('profile', 'assess')
    if name not in PROFILES:
        raise SystemExit('site.conf: профиль «%s» неизвестен, есть: %s'
                         % (name, ', '.join(sorted(PROFILES))))
    out = json.loads(json.dumps(PROFILES[name]))
    out['name'] = name
    for key in LISTS:
        if key in site:
            out[key] = site[key].replace(',', ' ').split()
    # A blocks profile that overrides its topics (nmt-uahist: twelve blocks, not
    # thirteen) must report those pages, not the profile's own: the first kind
    # is the block list, and a page missing from it crashed build-meta.
    if 'topics' in site and out['blocks']:
        t = out['topics']
        word = out['kinds'][0][0].split(' (')[0]
        out['kinds'][0] = ['%s (%s-%s)' % (word, t[0], t[-1]), t]
    if 'source' in site:
        out['source'] = site['source']
    if 'sections' in site:
        out['sections'] = int(site['sections'])
    if 'related' in site:
        out['related'] = site['related']
    if out['source'] not in out['langs']:
        raise SystemExit('site.conf: исходный язык %s не входит в langs' % out['source'])
    return out


if __name__ == '__main__':
    if '--get' in sys.argv:
        value = profile()[sys.argv[sys.argv.index('--get') + 1]]
        print(' '.join(value) if isinstance(value, list) else value)
    elif '--json' in sys.argv:
        print(json.dumps(profile(), ensure_ascii=False))
    else:
        print(json.dumps(profile(), ensure_ascii=False, indent=2))
