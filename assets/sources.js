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
  document.querySelectorAll('[data-kind="illustration"][data-line]').forEach((el) => {
    const id = el.dataset.line;
    if (!(id in lineName)) { lines.push(id); lineName[id] = el.dataset.lineName || id; }
  });
  if (!catalogue.length && lines.length < 2) return;

  const SAY = {
    uk: { open: 'Налаштування', title: 'Налаштування', close: 'Закрити налаштування',
          group: 'Зовнішні джерела',
          lead: 'Посилання на реальні завдання, що спираються на закони блоку. Вимкнений рік зникає зі сторінок і з пошуку.',
          sources: { 'nmt-ua': 'Показувати посилання на завдання НМТ із сайту ЗНО-ОНЛАЙН (zno.osvita.ua)',
                     'nmt-demo': 'Показувати демоваріанти НМТ із сайту ЗНО-ОНЛАЙН',
                     'zno-ua': 'Показувати завдання ЗНО минулих років із сайту ЗНО-ОНЛАЙН' },
          year: { 'nmt-ua': 'НМТ %s', 'nmt-demo': 'Демо НМТ %s', 'zno-ua': 'ЗНО %s' },
          artGroup: 'Ілюстрації',
          artLead: 'Ті самі сюжети в різних лініях. Вибір діє на всіх сторінках сайту.' },
    ru: { open: 'Настройки', title: 'Настройки', close: 'Закрыть настройки',
          group: 'Внешние источники',
          lead: 'Ссылки на реальные задания, которые опираются на законы блока. Выключенный год пропадает со страниц и из поиска.',
          sources: { 'nmt-ua': 'Показывать ссылки на задания НМТ с сайта ЗНО-ОНЛАЙН (zno.osvita.ua)',
                     'nmt-demo': 'Показывать демоварианты НМТ с сайта ЗНО-ОНЛАЙН',
                     'zno-ua': 'Показывать задания ВНО прошлых лет с сайта ЗНО-ОНЛАЙН' },
          year: { 'nmt-ua': 'НМТ %s', 'nmt-demo': 'Демо НМТ %s', 'zno-ua': 'ВНО %s' },
          artGroup: 'Иллюстрации',
          artLead: 'Те же сюжеты в разных линиях. Выбор действует на всех страницах сайта.' },
    en: { open: 'Settings', title: 'Settings', close: 'Close settings',
          group: 'External sources',
          lead: 'Links to real exam tasks that rest on the laws of a block. A year switched off leaves the pages and the search.',
          sources: { 'nmt-ua': 'Show links to NMT tasks on the ZNO-ONLINE site (zno.osvita.ua)',
                     'nmt-demo': 'Show the NMT demo variants from the ZNO-ONLINE site',
                     'zno-ua': 'Show the ZNO tests of past years from the ZNO-ONLINE site' },
          year: { 'nmt-ua': 'NMT %s', 'nmt-demo': 'NMT demo %s', 'zno-ua': 'ZNO %s' },
          artGroup: 'Illustrations',
          artLead: 'The same scenes in different lines. The choice holds on every page of the site.' },
    de: { open: 'Einstellungen', title: 'Einstellungen', close: 'Einstellungen schließen',
          group: 'Externe Quellen',
          lead: 'Links zu echten Prüfungsaufgaben, die auf den Gesetzen eines Blocks beruhen. Ein ausgeschaltetes Jahr verschwindet von den Seiten und aus der Suche.',
          sources: { 'nmt-ua': 'Links zu NMT-Aufgaben auf der Seite ZNO-ONLINE (zno.osvita.ua) zeigen',
                     'nmt-demo': 'NMT-Demovarianten von der Seite ZNO-ONLINE zeigen',
                     'zno-ua': 'ZNO-Tests früherer Jahre von der Seite ZNO-ONLINE zeigen' },
          year: { 'nmt-ua': 'NMT %s', 'nmt-demo': 'NMT-Demo %s', 'zno-ua': 'ZNO %s' },
          artGroup: 'Illustrationen',
          artLead: 'Dieselben Motive in verschiedenen Linien. Die Wahl gilt auf allen Seiten der Website.' },
  };
  const lang = document.documentElement.lang || 'uk';
  const say = SAY[lang] || SAY.uk;
  const SITE = document.documentElement.dataset.site || 'swa';
  const KEY = 'swa-' + SITE + '-ext-off';
  const LINE_KEY = 'swa-' + SITE + '-art-line';

  function readLine() {
    let id = null;
    try { id = localStorage.getItem(LINE_KEY); } catch (_) {}
    return lines.includes(id) ? id : lines[0];
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
      document.querySelectorAll('[data-kind="illustration"][data-line]').forEach((el) => {
        el.hidden = el.dataset.line !== line;
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
  dlg.innerHTML = '<div class="settings-head"><h2 id="settings-title">' + say.title + '</h2>'
    + '<button type="button" class="settings-close" aria-label="' + say.close + '">&times;</button></div>'
    + (lines.length > 1 ? '<fieldset class="settings-group"><legend>' + (say.artGroup || SAY.uk.artGroup) + '</legend>'
      + '<p class="dim">' + (say.artLead || SAY.uk.artLead) + '</p>'
      + lines.map((id) => '<label class="settings-row"><input type="radio" name="art-line" data-line="' + id + '"> '
        + lineName[id] + '</label>').join('')
      + '</fieldset>' : '')
    + (catalogue.length ? '<fieldset class="settings-group"><legend>' + say.group + '</legend>'
    + '<p class="dim">' + say.lead + '</p>'
    + sources.map((src) => '<div class="settings-source">'
      + '<label class="settings-row"><input type="checkbox" data-src="' + src + '"> '
      + (say.sources[src] || src) + '</label>'
      + '<div class="settings-years">'
      + years[src].map((id) => '<label class="settings-row"><input type="checkbox" data-id="' + id + '"> '
        + fmt(src, id) + '</label>').join('')
      + '</div></div>').join('')
    + '</fieldset>' : '');
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
