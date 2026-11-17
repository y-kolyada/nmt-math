// sources.js - the settings window and the external sources it switches.
//
// A study site may point beyond itself: to the real exam tasks that lean on a
// block's laws. Each source and each year of it is a block of its own,
// <div class="ext" data-ext="nmt-ua:2026">, which the reader switches on or off
// here. The catalogue comes from <meta name="swa-sources" content="nmt-ua:2024 ...">
// (tools/build-sources.py writes it on every page), so the panel lists the same
// years on a page without a section. A page without that meta gets nothing from
// this file: no gear, no panel.
//
// The choice lives in localStorage swa-<site>-ext-off as a list: "nmt-ua" is the
// whole source off, "nmt-ua:2026" one year off. assets/search.js reads the same
// list, so a switched-off year is not searched either.
//
// The same window switches the line of illustrations. A site may draw the same
// picture in several lines (a village and a modern one, say): each drawing is
// <div class="box" data-kind="illustration" data-line="modern"
// data-line-name="Сучасна Україна">, the alternatives stand side by side, and
// all but the default carry `hidden` in the markup, so a reader without
// JavaScript and the first paint see the default only. The lines are read from
// the page itself, in the order they first appear: the first is the default, so
// a site lists its default line first on every page. The choice lives in
// localStorage swa-<site>-art-line; a choice the page does not draw falls back
// to the default. A drawing without data-line belongs to no line and always
// shows. The group appears only where a page has two lines or more.
(function () {
  const meta = document.querySelector('meta[name="swa-sources"]');
  const tray = document.querySelector('.utility-tray');
  if (!tray) return;
  const catalogue = meta ? meta.content.split(/\s+/).filter(Boolean) : [];
  const lines = [];
  const lineName = {};
  // The site's lines come first, from <meta name="swa-art-lines"> that
  // tools/build-sources.py writes on every page from site.conf `art_lines`, so a
  // page without pictures shows the same tab; the drawings on the page add any
  // line the meta does not name.
  const artMeta = document.querySelector('meta[name="swa-art-lines"]');
  (artMeta ? artMeta.content.split(';') : []).forEach((pair) => {
    const at = pair.indexOf(':');
    const id = (at < 0 ? pair : pair.slice(0, at)).trim();
    if (id && !(id in lineName)) { lines.push(id); lineName[id] = at < 0 ? '' : pair.slice(at + 1).trim(); }
  });
  document.querySelectorAll('[data-kind="illustration"][data-line]').forEach((el) => {
    const id = el.dataset.line;
    if (!(id in lineName)) { lines.push(id); lineName[id] = el.dataset.lineName || ''; }
  });
  if (!catalogue.length && !lines.length) return;

  const SAY = {
    uk: { open: 'Налаштування', title: 'Налаштування', close: 'Закрити налаштування',
          group: 'Зовнішні джерела',
          lead: 'Посилання на реальні завдання, що спираються на закони блоку. Вимкнений рік зникає зі сторінок і з пошуку.',
          sources: { 'nmt-ua': 'Показувати посилання на завдання НМТ із сайту ЗНО-ОНЛАЙН (zno.osvita.ua)',
                     'nmt-demo': 'Показувати демоваріанти НМТ із сайту ЗНО-ОНЛАЙН',
                     'zno-ua': 'Показувати завдання ЗНО минулих років із сайту ЗНО-ОНЛАЙН' },
          year: { 'nmt-ua': 'НМТ %s', 'nmt-demo': 'Демо НМТ %s', 'zno-ua': 'ЗНО %s' },
          artGroup: 'Ілюстрації',
          artLead: 'Ті самі сюжети в різних лініях. Вибір діє на всіх сторінках сайту.',
          artNone: 'Без ілюстрацій',
          artAll: 'Показувати ілюстрації', artLeadOne: 'Рисунки на сторінках сайту. Вибір діє на всіх сторінках.' },
    ru: { open: 'Настройки', title: 'Настройки', close: 'Закрыть настройки',
          group: 'Внешние источники',
          lead: 'Ссылки на реальные задания, которые опираются на законы блока. Выключенный год пропадает со страниц и из поиска.',
          sources: { 'nmt-ua': 'Показывать ссылки на задания НМТ с сайта ЗНО-ОНЛАЙН (zno.osvita.ua)',
                     'nmt-demo': 'Показывать демоварианты НМТ с сайта ЗНО-ОНЛАЙН',
                     'zno-ua': 'Показывать задания ВНО прошлых лет с сайта ЗНО-ОНЛАЙН' },
          year: { 'nmt-ua': 'НМТ %s', 'nmt-demo': 'Демо НМТ %s', 'zno-ua': 'ВНО %s' },
          artGroup: 'Иллюстрации',
          artLead: 'Те же сюжеты в разных линиях. Выбор действует на всех страницах сайта.',
          artNone: 'Без иллюстраций',
          artAll: 'Показывать иллюстрации', artLeadOne: 'Рисунки на страницах сайта. Выбор действует на всех страницах.' },
    en: { open: 'Settings', title: 'Settings', close: 'Close settings',
          group: 'External sources',
          lead: 'Links to real exam tasks that rest on the laws of a block. A year switched off leaves the pages and the search.',
          sources: { 'nmt-ua': 'Show links to NMT tasks on the ZNO-ONLINE site (zno.osvita.ua)',
                     'nmt-demo': 'Show the NMT demo variants from the ZNO-ONLINE site',
                     'zno-ua': 'Show the ZNO tests of past years from the ZNO-ONLINE site' },
          year: { 'nmt-ua': 'NMT %s', 'nmt-demo': 'NMT demo %s', 'zno-ua': 'ZNO %s' },
          artGroup: 'Illustrations',
          artLead: 'The same scenes in different lines. The choice holds on every page of the site.',
          artNone: 'No illustrations',
          artAll: 'Show illustrations', artLeadOne: 'The pictures on the pages of the site. The choice holds on every page.' },
    de: { open: 'Einstellungen', title: 'Einstellungen', close: 'Einstellungen schließen',
          group: 'Externe Quellen',
          lead: 'Links zu echten Prüfungsaufgaben, die auf den Gesetzen eines Blocks beruhen. Ein ausgeschaltetes Jahr verschwindet von den Seiten und aus der Suche.',
          sources: { 'nmt-ua': 'Links zu NMT-Aufgaben auf der Seite ZNO-ONLINE (zno.osvita.ua) zeigen',
                     'nmt-demo': 'NMT-Demovarianten von der Seite ZNO-ONLINE zeigen',
                     'zno-ua': 'ZNO-Tests früherer Jahre von der Seite ZNO-ONLINE zeigen' },
          year: { 'nmt-ua': 'NMT %s', 'nmt-demo': 'NMT-Demo %s', 'zno-ua': 'ZNO %s' },
          artGroup: 'Illustrationen',
          artLead: 'Dieselben Motive in verschiedenen Linien. Die Wahl gilt auf allen Seiten der Website.',
          artNone: 'Ohne Illustrationen',
          artAll: 'Illustrationen zeigen', artLeadOne: 'Die Bilder auf den Seiten der Website. Die Wahl gilt auf allen Seiten.' },
  };
  const lang = document.documentElement.lang || 'uk';
  const say = SAY[lang] || SAY.uk;
  const SITE = document.documentElement.dataset.site || 'swa';
  const KEY = 'swa-' + SITE + '-ext-off';
  const LINE_KEY = 'swa-' + SITE + '-art-line';

  // «Без ілюстрацій»: one more choice after the lines, which hides every raster
  // illustration on every page (the Conductor, 2026-11-18). Diagrams are not
  // illustrations and stay.
  const NONE = 'none';
  function readLine() {
    let id = null;
    try { id = localStorage.getItem(LINE_KEY); } catch (_) {}
    return lines.includes(id) || id === NONE ? id : lines[0];
  }
  function writeLine(id) {
    try {
      if (id === lines[0]) localStorage.removeItem(LINE_KEY);
      else localStorage.setItem(LINE_KEY, id);
    } catch (_) {}
  }

  function readOff() {
    try {
      const list = JSON.parse(localStorage.getItem(KEY) || '[]');
      return new Set(Array.isArray(list) ? list : []);
    } catch (_) { return new Set(); }
  }
  function writeOff(off) {
    try {
      if (off.size) localStorage.setItem(KEY, JSON.stringify([...off].sort()));
      else localStorage.removeItem(KEY);
    } catch (_) {}
  }
  const sourceOf = (id) => id.split(':')[0];
  const isOff = (off, id) => off.has(id) || off.has(sourceOf(id));

  // Sources in the order of the catalogue, each with its years.
  const sources = [];
  const years = {};
  catalogue.forEach((id) => {
    const src = sourceOf(id);
    if (!years[src]) { years[src] = []; sources.push(src); }
    if (id !== src) years[src].push(id);
  });

  // The page: a year block is hidden when it or its source is off; a source
  // block (its heading and lead) leaves with its last year; the note "all
  // sources are off" shows when no source is left in the section.
  function apply() {
    const off = readOff();
    document.querySelectorAll('.ext[data-ext]').forEach((el) => {
      el.hidden = isOff(off, el.dataset.ext);
    });
    document.querySelectorAll('.ext-source').forEach((box) => {
      box.hidden = ![...box.querySelectorAll('.ext[data-ext]')].some((el) => !el.hidden);
    });
    document.querySelectorAll('.ext-off').forEach((note) => {
      const scope = note.parentElement;
      note.hidden = [...scope.querySelectorAll('.ext-source')].some((box) => !box.hidden);
    });
    if (lines.length) {
      const line = readLine();
      document.querySelectorAll('[data-kind="illustration"]').forEach((el) => {
        el.hidden = line === NONE || (el.dataset.line !== undefined && el.dataset.line !== line);
      });
    }
  }

  const gear = document.createElement('button');
  gear.type = 'button';
  gear.className = 'settings-btn';
  gear.setAttribute('aria-label', say.open);
  gear.setAttribute('aria-haspopup', 'dialog');
  gear.title = say.open;
  // The shape follows the Conductor's sample (courses/nmt-math/gear.png): six
  // wide teeth and a hole. evenodd keeps the hole when hover fills the body.
  gear.innerHTML = '<svg class="icon" data-icon="gear" viewBox="0 0 20 20" width="16" height="16"'
    + ' fill="none" fill-rule="evenodd" stroke="currentColor" stroke-width="1.5"'
    + ' stroke-linejoin="round" aria-hidden="true"><path d="M7.9 1.9L12.1 1.9L12.6 4.6L13.4 5.1L16.0 4.1L18.1 7.7L16.0 9.5L16.0 10.5L18.1 12.3L16.0 15.9L13.4 14.9L12.6 15.4'
    + 'L12.1 18.1L7.9 18.1L7.4 15.4L6.6 14.9L4.0 15.9L1.9 12.3L4.0 10.5L4.0 9.5L1.9 7.7L4.0 4.1L6.6 5.1L7.4 4.6Z'
    + 'M10 7.7a2.3 2.3 0 1 0 0 4.6a2.3 2.3 0 1 0 0-4.6Z"/></svg>';
  tray.appendChild(gear);

  const dlg = document.createElement('dialog');
  dlg.className = 'settings-panel';
  dlg.setAttribute('aria-labelledby', 'settings-title');
  const fmt = (src, id) => (say.year[src] || '%s').replace('%s', id.slice(src.length + 1));
  // The groups of the window. With two or more, each is a tab of its own, left to
  // right, and one shows at a time: stacked one under another they made the
  // window scroll even on a large screen (the Conductor, 2026-11-18). With one
  // group the window is as before, without a tab row.
  const groups = [];
  // One line is enough for the group now: «Без ілюстрацій» makes it a choice. A
  // site with one line writes `art_lines = all` without a name, and the engine
  // names it in the page's own language (nmt-math has four).
  if (lines.length) groups.push({ id: 'art', label: say.artGroup || SAY.uk.artGroup,
    body: '<p class="dim">' + (lines.length > 1 ? say.artLead || SAY.uk.artLead : say.artLeadOne || SAY.uk.artLeadOne) + '</p>'
      + lines.concat(NONE).map((id) => '<label class="settings-row"><input type="radio" name="art-line" data-line="' + id + '"> '
        + (id === NONE ? (say.artNone || SAY.uk.artNone) : lineName[id] || say.artAll || SAY.uk.artAll) + '</label>').join('') });
  if (catalogue.length) groups.push({ id: 'ext', label: say.group,
    body: '<p class="dim">' + say.lead + '</p>'
      + sources.map((src) => '<div class="settings-source">'
        + '<label class="settings-row"><input type="checkbox" data-src="' + src + '"> '
        + (say.sources[src] || src) + '</label>'
        + '<div class="settings-years">'
        + years[src].map((id) => '<label class="settings-row"><input type="checkbox" data-id="' + id + '"> '
          + fmt(src, id) + '</label>').join('')
        + '</div></div>').join('') });
  const tabbed = groups.length > 1;
  dlg.innerHTML = '<div class="settings-head"><h2 id="settings-title">' + say.title + '</h2>'
    + '<button type="button" class="settings-close" aria-label="' + say.close + '">&times;</button></div>'
    + (tabbed ? '<div class="settings-tabs" role="tablist">' + groups.map((g, i) => '<button type="button" role="tab"'
      + ' class="settings-tab" id="settings-tab-' + g.id + '" aria-controls="settings-panel-' + g.id + '"'
      + ' aria-selected="' + (i === 0) + '" tabindex="' + (i === 0 ? 0 : -1) + '">' + g.label + '</button>').join('') + '</div>' : '')
    + groups.map((g, i) => '<fieldset class="settings-group"' + (tabbed ? ' role="tabpanel" id="settings-panel-' + g.id
      + '" aria-labelledby="settings-tab-' + g.id + '"' + (i ? ' hidden' : '') : '') + '>'
      + (tabbed ? '' : '<legend>' + g.label + '</legend>') + g.body + '</fieldset>').join('');
  if (tabbed) {
    const tabs = [...dlg.querySelectorAll('.settings-tab')];
    const show = (tab) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        dlg.querySelector('#' + t.getAttribute('aria-controls')).hidden = !on;
      });
    };
    tabs.forEach((t) => t.addEventListener('click', () => show(t)));
    dlg.querySelector('.settings-tabs').addEventListener('keydown', (e) => {
      const i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      const to = { ArrowRight: (i + 1) % tabs.length, ArrowLeft: (i - 1 + tabs.length) % tabs.length,
                   Home: 0, End: tabs.length - 1 }[e.key];
      if (to === undefined) return;
      e.preventDefault();
      tabs[to].focus();
      show(tabs[to]);
    });
  }
  document.body.appendChild(dlg);

  function paint() {
    const line = readLine();
    dlg.querySelectorAll('input[data-line]').forEach((r) => { r.checked = r.dataset.line === line; });
    const off = readOff();
    dlg.querySelectorAll('input[data-src]').forEach((box) => {
      box.checked = !off.has(box.dataset.src);
      box.closest('.settings-source').querySelectorAll('input[data-id]').forEach((y) => {
        y.checked = !off.has(y.dataset.id);
        y.disabled = !box.checked;
      });
    });
  }

  dlg.addEventListener('change', (e) => {
    const box = e.target;
    if (!(box instanceof HTMLInputElement)) return;
    if (box.dataset.line) {
      writeLine(box.dataset.line);
      paint();
      apply();
      return;
    }
    const off = readOff();
    const id = box.dataset.src || box.dataset.id;
    if (box.checked) off.delete(id); else off.add(id);
    writeOff(off);
    paint();
    apply();
  });
  dlg.querySelector('.settings-close').addEventListener('click', () => dlg.close());
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener('close', () => gear.focus());
  gear.addEventListener('click', () => {
    paint();
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
  });

  // Another tab may change the choice; this one follows it.
  window.addEventListener('storage', (e) => { if (e.key === KEY || e.key === LINE_KEY) { paint(); apply(); } });
  apply();
})();
