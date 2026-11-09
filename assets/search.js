// search.js - the search panel. Loaded on demand by swa.js, together with the
// index for the language of the page, so nothing of this reaches a reader who
// never opens it.
(function () {
  const SAY = {
    ru: { place: 'Искать по разделам, словарю и вопросам', none: 'Ничего не найдено',
          empty: 'Для этого языка содержание ещё не переведено', close: 'Закрыть поиск',
          clear: 'Очистить строку поиска',
          hint: 'Esc - закрыть, стрелки - выбор, Enter - перейти, PgUp/PgDn - страницы' ,
          only: 'Искать только по темам или снова везде', found: 'Найдено',
          shown: 'показаны', pages: 'Страницы результатов',
          prev: 'Предыдущая страница результатов', next: 'Следующая страница результатов',
          first: 'Первая страница результатов', last: 'Последняя страница результатов',
          kinds: { t: 'Темы', e: 'Примеры', q: 'Вопросы', n: 'Навигатор', g: 'Словарь', i: 'Витрина' } },
    en: { place: 'Search sections, glossary, and questions', none: 'Nothing found',
          empty: 'This language has no content yet', close: 'Close search',
          clear: 'Clear search query',
          hint: 'Esc to close, arrows to move, Enter to open, PgUp/PgDn to turn pages' ,
          only: 'Search topics only, or everywhere again', found: 'Found',
          shown: 'shown', pages: 'Result pages',
          prev: 'Previous page of results', next: 'Next page of results',
          first: 'First page of results', last: 'Last page of results',
          kinds: { t: 'Topics', e: 'Examples', q: 'Questions', n: 'Navigator', g: 'Glossary', i: 'Landing' } },
    uk: { place: 'Шукати в розділах, словнику й питаннях', none: 'Нічого не знайдено',
          empty: 'Для цієї мови зміст ще не перекладено', close: 'Закрити пошук',
          clear: 'Очистити рядок пошуку',
          hint: 'Esc - закрити, стрілки - вибір, Enter - перейти, PgUp/PgDn - сторінки' ,
          only: 'Шукати лише в темах або знову скрізь', found: 'Знайдено',
          shown: 'показано', pages: 'Сторінки результатів',
          prev: 'Попередня сторінка результатів', next: 'Наступна сторінка результатів',
          first: 'Перша сторінка результатів', last: 'Остання сторінка результатів',
          kinds: { t: 'Теми', e: 'Приклади', q: 'Питання', n: 'Навігатор', g: 'Словник', i: 'Вітрина' } },
    de: { place: 'Abschnitte, Glossar und Fragen durchsuchen', none: 'Nichts gefunden',
          empty: 'Für diese Sprache gibt es noch keine Inhalte', close: 'Suche schließen',
          clear: 'Suchfeld leeren',
          hint: 'Esc schließt, Pfeile wählen, Enter öffnet, Bild↑/Bild↓ blättern' ,
          only: 'Nur in Themen suchen oder wieder überall', found: 'Gefunden',
          shown: 'angezeigt', pages: 'Ergebnisseiten',
          prev: 'Vorherige Ergebnisseite', next: 'Nächste Ergebnisseite',
          first: 'Erste Ergebnisseite', last: 'Letzte Ergebnisseite',
          kinds: { t: 'Themen', e: 'Beispiele', q: 'Fragen', n: 'Navigator', g: 'Glossar', i: 'Startseite' } },
  };

  const lang = document.documentElement.lang || 'ru';
  const say = SAY[lang] || SAY.ru;
  const raw = (window.SEARCH && window.SEARCH.i) || [];
  const SITE = document.documentElement.dataset.site || 'swa';
  const key = (name) => 'swa-' + SITE + '-' + name;

  // ё and е are one letter for a reader looking for a word.
  const norm = (s) => s.toLowerCase().replace(/ё/g, 'е');
  const items = raw.map((e) => ({ url: e[0], title: e[1], page: e[2], body: e[3],
    kind: e[4] || 't', t: norm(e[1]), b: norm(e[3]) }));

  // Виды страниц, которые в этом индексе вообще есть. Один вид - отбирать
  // не из чего, и ряда переключателей не появляется вовсе: на языке, где
  // переведена только витрина, он был бы одной кнопкой «Витрина».
  const kinds = ((window.SEARCH && window.SEARCH.k) || []).filter((k) => say.kinds[k]);
  // Внешние источники учебного профиля (assets/sources.js): у каждого года
  // свой вид x:<источник>:<год> и своя подпись. Выключенный в настройках год
  // не ищется и не показывает переключателя; настройки читаются заново при
  // каждом открытии окна, потому что меняются в другом окне.
  const xlabels = (window.SEARCH && window.SEARCH.x) || {};
  const xkinds = Object.keys(xlabels);
  const EXT_KEY = key('ext-off');
  function xOff() {
    try {
      const list = JSON.parse(localStorage.getItem(EXT_KEY) || '[]');
      return new Set(Array.isArray(list) ? list : []);
    } catch (_) { return new Set(); }
  }
  let extOff = xOff();
  const xHidden = (k) => {
    const id = k.slice(2);
    return extOff.has(id) || extOff.has(id.split(':')[0]);
  };
  const live = () => kinds.concat(xkinds.filter((k) => !xHidden(k)));
  const faceted = kinds.length + xkinds.length > 1;
  const off = new Set();

  const panel = document.createElement('div');
  panel.className = 'search-panel';
  panel.hidden = true;
  panel.innerHTML =
    '<div class="search-box" role="dialog" aria-modal="true" aria-label="' + say.place + '">'
    + '<div class="search-head">'
    + '<svg class="icon search-lead-icon" viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8.6" cy="8.6" r="5.4"/><path d="M12.6 12.6l4 4"/></svg>'
    + '<input type="search" class="search-input" placeholder="' + say.place + '" aria-label="' + say.place + '">'
    + '<button type="button" class="search-clear" hidden aria-label="' + say.clear + '" title="' + say.clear + '">'
    + '<svg class="icon" data-icon="clear-mark" viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    + '<path d="M12.5 3.5l4 4L8 16H4v-4L12.5 3.5z"/><path d="M3 18h14"/><path d="M14.5 11.5l3.5 3.5M18 11.5l-3.5 3.5"/></svg>'
    + '</button>'
    + (faceted ? '<button type="button" class="search-only" aria-pressed="false" aria-label="'
        + say.only + '" title="' + say.only + '">'
        + '<svg class="icon" data-icon="funnel" viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        + '<path d="M3 4.5h14l-5.4 6.2v4.6l-3.2 1.8v-6.4z"/></svg>'
        + '</button>' : '')
    + '<span class="search-lang">' + lang.toUpperCase() + '</span>'
    + '<button type="button" class="search-close" aria-label="' + say.close + '">&times;</button>'
    + '</div>'
    + (faceted ? '<div class="search-facets" role="group">'
        + kinds.map((k) => '<button type="button" class="search-facet" data-kind="' + k
          + '" aria-pressed="true">' + say.kinds[k] + '</button>').join('')
        + xkinds.map((k) => '<button type="button" class="search-facet search-facet-ext" data-kind="' + k
          + '" aria-pressed="true"></button>').join('')
        + '</div>' : '')
    + '<div class="search-meta" hidden><p class="search-count"></p>'
    + '<div class="search-pager" role="group" aria-label="' + say.pages + '" hidden></div></div>'
    + '<ul class="search-results"></ul>'
    + '<div class="search-hint">' + say.hint + '</div>'
    + '</div>';
  document.body.appendChild(panel);

  const input = panel.querySelector('.search-input');
  const facets = [...panel.querySelectorAll('.search-facet')];
  facets.forEach((b) => { if (xlabels[b.dataset.kind]) b.textContent = xlabels[b.dataset.kind]; });
  const onlyBtn = panel.querySelector('.search-only');
  const meta = panel.querySelector('.search-meta');
  const count = panel.querySelector('.search-count');
  const pager = panel.querySelector('.search-pager');
  const clearBtn = panel.querySelector('.search-clear');
  const list = panel.querySelector('.search-results');
  let picked = -1;
  // Выдача идёт страницами по сорок мест: сорок - прежний потолок списка, и
  // пейджер открывает то, что раньше за ним пропадало. Номер страницы
  // считается с нуля и живёт рядом с запросом, чтобы возврат со страницы
  // темы открывал окно там же, откуда читатель ушёл.
  const PAGE = 40;
  let pageNo = 0;
  let pages = 1;

  try {
    const saved = JSON.parse(sessionStorage.getItem(key('search')) || 'null');
    if (saved && saved.q) {
      input.value = saved.q;
      picked = typeof saved.idx === 'number' ? saved.idx : -1;
      pageNo = typeof saved.page === 'number' && saved.page > 0 ? saved.page : 0;
    }
    if (saved && Array.isArray(saved.off)) {
      saved.off.forEach((k) => off.add(k));
    }
  } catch (_) {}

  paintFacets();

  // Выключить все виды - то же, что не искать вовсе, поэтому последний
  // включённый не выключается: пустая выдача без причины читается как
  // поломка поиска, а не как собственный выбор.
  // Объявления, а не стрелки: paintFacets зовётся выше по тексту, ещё при загрузке.
  function offLive() { return live().filter((k) => off.has(k)).length; }
  function onlyTopics() { return offLive() === live().length - 1 && !off.has('t'); }

  function paintFacets() {
    facets.forEach((b) => {
      b.setAttribute('aria-pressed', String(!off.has(b.dataset.kind)));
      if (xlabels[b.dataset.kind]) b.hidden = xHidden(b.dataset.kind);
    });
    if (onlyBtn) onlyBtn.setAttribute('aria-pressed', String(onlyTopics()));
  }

  // Один щелчок вместо пяти: предмет сайта или весь сайт. Первое открытие
  // окна ищет везде - читатель, который ещё не знает, что здесь есть,
  // не должен сначала включать то, о чём не спрашивал.
  if (onlyBtn) {
    onlyBtn.addEventListener('click', () => {
      const was = onlyTopics();
      off.clear();
      if (!was) live().forEach((k) => { if (k !== 't') off.add(k); });
      paintFacets();
      render(input.value, false);
      saveState(picked, '', false);
    });
  }

  facets.forEach((btn) => btn.addEventListener('click', () => {
    const k = btn.dataset.kind;
    if (off.has(k)) off.delete(k);
    else if (offLive() < live().length - 1) off.add(k);
    else return;
    paintFacets();
    render(input.value, false);
    saveState(picked, '', false);
  }));

  function saveState(idx, url, active) {
    try {
      if (!input.value.trim() && !off.size) {
        sessionStorage.removeItem(key('search'));
        return;
      }
      sessionStorage.setItem(key('search'), JSON.stringify({
        q: input.value,
        idx,
        url: url || '',
        active: Boolean(active),
        off: [...off],
        page: pageNo,
      }));
    } catch (_) {}
  }

  function snippet(entry, needle) {
    const at = entry.b.indexOf(needle);
    if (at < 0) return entry.body.slice(0, 120);
    const from = Math.max(0, at - 40);
    return (from ? '… ' : '') + entry.body.slice(from, from + 150);
  }

  function find(query) {
    const needle = norm(query.trim());
    // Пустой и односимвольный запрос тоже возвращает форму {total, all}: раньше здесь
    // стоял пустой массив, и render падал на got.all при каждом открытии окна.
    if (needle.length < 2) return { total: 0, all: [] };
    const hits = [];
    for (const entry of items) {
      if (off.has(entry.kind) || (entry.kind.charAt(1) === ':' && xHidden(entry.kind))) continue;
      const inTitle = entry.t.indexOf(needle);
      const inBody = inTitle < 0 ? entry.b.indexOf(needle) : -1;
      if (inTitle < 0 && inBody < 0) continue;
      hits.push({ entry, rank: inTitle >= 0 ? inTitle : 1000 + inBody });
    }
    hits.sort((a, b) => a.rank - b.rank);
    return { total: hits.length, all: hits.map((h) => h.entry) };
  }

  // Номера страниц для пейджера: до семи страниц - все, дальше - первая,
  // последняя и соседи текущей, а пропуски между ними - многоточие (null).
  function pageList(n, cur) {
    if (n <= 7) return [...Array(n).keys()];
    let lo = Math.max(1, cur - 1);
    let hi = Math.min(n - 2, cur + 1);
    if (cur <= 3) { lo = 1; hi = 4; }
    if (cur >= n - 4) { lo = n - 5; hi = n - 2; }
    const out = [0];
    if (lo > 1) out.push(null);
    for (let i = lo; i <= hi; i += 1) out.push(i);
    if (hi < n - 2) out.push(null);
    out.push(n - 1);
    return out;
  }

  function pgButton(label, to, aria, current, disabled) {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'search-pg';
    b.textContent = label;
    b.dataset.page = String(to);
    if (aria) b.setAttribute('aria-label', aria);
    if (current) b.setAttribute('aria-current', 'page');
    if (disabled) b.disabled = true;
    return b;
  }

  function paintPager() {
    pager.innerHTML = '';
    pager.hidden = pages < 2;
    if (pages < 2) return;
    // Края « и » - стандарт пейджера: в начало и в конец одним щелчком,
    // даже когда номер нужной страницы спрятан за многоточием.
    pager.appendChild(pgButton('«', 0, say.first, false, pageNo === 0));
    pager.appendChild(pgButton('‹', pageNo - 1, say.prev, false, pageNo === 0));
    pageList(pages, pageNo).forEach((n) => {
      if (n === null) {
        const gap = document.createElement('span');
        gap.className = 'search-pg-gap';
        gap.textContent = '…';
        pager.appendChild(gap);
      } else {
        pager.appendChild(pgButton(String(n + 1), n, '', n === pageNo, false));
      }
    });
    pager.appendChild(pgButton('›', pageNo + 1, say.next, false, pageNo === pages - 1));
    pager.appendChild(pgButton('»', pages - 1, say.last, false, pageNo === pages - 1));
  }

  function turn(to) {
    if (to < 0 || to >= pages || to === pageNo) return;
    pageNo = to;
    picked = -1;
    render(input.value, true);
    list.scrollTop = 0;
    saveState(-1, '', false);
  }

  function render(query, keepPicked) {
    clearBtn.hidden = !query.length;
    const got = items.length ? find(query) : { total: 0, all: [] };
    // Новый запрос или другая область - снова первая страница; открытие
    // окна и листание страницу сохраняют, но не дальше последней: область
    // могла сузиться в другом окне.
    if (!keepPicked) { picked = -1; pageNo = 0; }
    pages = Math.max(1, Math.ceil(got.total / PAGE));
    if (pageNo > pages - 1) { pageNo = pages - 1; picked = -1; }
    const found = got.all.slice(pageNo * PAGE, (pageNo + 1) * PAGE);
    list.innerHTML = '';
    // Счётчик говорит, сколько нашлось на самом деле, а не сколько влезло,
    // и какой кусок списка сейчас на экране.
    meta.hidden = !got.total;
    count.textContent = got.total
      ? say.found + ': ' + got.total
        + (pages > 1 ? ', ' + say.shown + ' ' + (pageNo * PAGE + 1) + '-' + (pageNo * PAGE + found.length) : '')
      : '';
    paintPager();
    if (!items.length) {
      list.innerHTML = '<li class="search-empty">' + say.empty + '</li>';
      return;
    }
    if (!found.length) {
      if (query.trim().length >= 2) list.innerHTML = '<li class="search-empty">' + say.none + '</li>';
      return;
    }
    const needle = norm(query.trim());
    found.forEach((entry, idx) => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = entry.url;
      a.dataset.idx = String(idx);
      if (idx === picked) a.classList.add('picked');
      a.innerHTML = '<span class="search-title"></span>'
        + '<span class="search-where"><span class="search-badge">' + lang.toUpperCase() + '</span>'
        + '<span class="search-page"></span></span>'
        + '<span class="search-snip"></span>';
      a.querySelector('.search-title').textContent = entry.title;
      a.querySelector('.search-page').textContent = entry.page;
      a.querySelector('.search-snip').textContent = snippet(entry, needle);
      li.appendChild(a);
      list.appendChild(li);
    });
    if (picked >= 0) {
      const activeLink = list.querySelectorAll('a')[picked];
      if (activeLink) activeLink.scrollIntoView({ block: 'nearest' });
    }
  }

  function move(step) {
    const links = [...list.querySelectorAll('a')];
    if (!links.length) return;
    picked = (picked + step + links.length) % links.length;
    links.forEach((a, n) => a.classList.toggle('picked', n === picked));
    links[picked].scrollIntoView({ block: 'nearest' });
  }

  function chooseLink(a) {
    const links = [...list.querySelectorAll('a')];
    const idx = links.indexOf(a);
    if (idx >= 0) {
      picked = idx;
      links.forEach((el, n) => el.classList.toggle('picked', n === picked));
    }
    const href = a.getAttribute('href') || '';
    saveState(picked, href, true);
    const [targetPage, anchor] = href.split('#');
    const curPage = location.pathname.split('/').pop() || 'index.html';
    if (anchor && (!targetPage || targetPage === curPage) && window.applySearchHighlight) {
      window.applySearchHighlight(anchor, input.value);
    }
    close();
  }

  function open() {
    extOff = xOff();
    paintFacets();
    panel.hidden = false;
    render(input.value, true);
    input.focus();
    input.select();
  }

  function close() {
    panel.hidden = true;
  }

  input.addEventListener('input', () => {
    saveState(-1, '', false);
    render(input.value, false);
  });
  clearBtn.addEventListener('click', () => {
    input.value = '';
    picked = -1;
    saveState(-1, '', false);
    if (window.clearSearchHighlight) window.clearSearchHighlight(false);
    render('', false);
    input.focus();
  });
  panel.querySelector('.search-close').addEventListener('click', close);
  panel.addEventListener('click', (e) => { if (e.target === panel) close(); });
  pager.addEventListener('click', (e) => {
    const b = e.target.closest('.search-pg');
    if (b && !b.disabled) turn(Number(b.dataset.page));
  });
  list.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (a) chooseLink(a);
  });
  document.addEventListener('keydown', (e) => {
    if (panel.hidden) return;
    if (e.key === 'Escape') { e.preventDefault(); close(); return; }
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); return; }
    if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); return; }
    if (e.key === 'PageDown' && pages > 1) { e.preventDefault(); turn(pageNo + 1); return; }
    if (e.key === 'PageUp' && pages > 1) { e.preventDefault(); turn(pageNo - 1); return; }
    // Enter на кнопке окна (пейджер, области) нажимает саму кнопку, а не
    // уводит читателя по первому найденному месту.
    if (e.key === 'Enter' && e.target.tagName === 'BUTTON') return;
    if (e.key === 'Enter') {
      const links = [...list.querySelectorAll('a')];
      const target = links[picked >= 0 ? picked : 0];
      if (target) { e.preventDefault(); target.click(); }
    }
  });

  window.openSearch = open;
  open();
})();
