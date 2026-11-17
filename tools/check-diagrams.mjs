// check-diagrams.mjs - every diagram of the site in one browser run.
//
//     node tools/check-diagrams.mjs
//
// Guards AGENTS.md section 5 rule 18. Six things a file cannot show:
//
//   1. the canvas is 320 units wide and capped at 320px, so one unit is one
//      pixel on a 390px phone and the budget below is honest;
//   2. no label is smaller than 12 units;
//   3. every label clears the right wall of its box by at least 6 units -
//      measured with getBBox, because the width of a string depends on the
//      page font and cannot be computed from the markup;
//   4. every diagram has a non-empty aria-label, which rots silently because
//      nobody looks at it;
//   5. captions are numbered sequentially across the language folder in
//      reading order (landing page first, navigator last), and
//      every diagram answers a source in diagrams/ and every source a diagram;
//   6. a translated page carries a translated diagram: its aria-label differs
//      from the base one and it keeps the same number of labels.
//
// A site without diagrams is the cheap case: no browser is started at all.
// Exits 1 if any diagram is faulty. Output is Russian: it speaks to the person
// who accepts the work.

import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';

// Languages and the source language are the site's profile (tools/siteconf.py).
const PROFILE = JSON.parse(execFileSync('python3', ['tools/siteconf.py', '--json'], { encoding: 'utf8' }));
const LANGS = PROFILE.langs;
const BASE = PROFILE.source; // the language the site is written in; the others translate it
const CANVAS = 320; // units, equal to pixels on the 390px phone
const MIN_LABEL = 12; // units
const MIN_GAP = 6; // units from the end of a label to the wall of its box

const bad = [];
const has = /<svg[^>]*\brole="img"/;

// Pages that actually hold a diagram. Reading the file is free; starting a
// browser is not.
// Reading order, not the alphabet: the landing page first, the navigator
// last, the rest by name. With sort() alone index.html came after block 15
// and a diagram on the landing page could never be number 1; aws-s3 had
// fixed this in its own copy, where a fix to the engine does not travel.
const byReading = (a, b) => {
  if (a === 'index.html') return -1;
  if (b === 'index.html') return 1;
  if (a === 'navigator.html') return 1;
  if (b === 'navigator.html') return -1;
  return a.localeCompare(b);
};
const pages = {};
for (const lang of LANGS) {
  if (!existsSync(lang)) continue;
  pages[lang] = readdirSync(lang).sort(byReading)
    .filter((n) => n.endsWith('.html'))
    .filter((n) => has.test(readFileSync(join(lang, n), 'utf8').split('<main')[1] || ''));
}
const sources = existsSync('diagrams')
  // A Mermaid source for schemes; on study sites also a generator (.py) for
  // mathematical figures that Mermaid cannot draw (profiles/study.md).
  ? readdirSync('diagrams').sort().filter((n) => n.endsWith('.mmd') || /^\d\d-.*\.py$/.test(n))
  : [];
const total = Object.values(pages).reduce((n, list) => n + list.length, 0);

if (!total && !sources.length) {
  console.log();
  console.log('  Проверка схем');
  console.log('  ' + '-'.repeat(46));
  console.log('  схем на сайте нет, проверять нечего');
  console.log('  ' + '-'.repeat(46));
  console.log('  ЗЕЛЁНОЕ');
  console.log();
  process.exit(0);
}

let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch {
  console.error('playwright не найден. Поставьте его в этой папке:');
  console.error('    npm i playwright');
  console.error('    npx playwright install chromium chromium-headless-shell');
  process.exit(2);
}

let browser;
try {
  browser = await chromium.launch();
} catch (e) {
  console.error('браузер не запустился: ' + String(e.message).split('\n')[0]);
  console.error('    npx playwright install chromium chromium-headless-shell');
  process.exit(2);
}
const page = await browser.newPage({ viewport: { width: 390, height: 900 } });

const seen = {}; // lang -> file -> [diagram, ...]
for (const lang of Object.keys(pages)) {
  seen[lang] = {};
  for (const name of pages[lang]) {
    await page.goto('file://' + join(process.cwd(), lang, name));
    seen[lang][name] = await page.evaluate(({ MIN_GAP }) => {
      return [...document.querySelectorAll('main svg[role="img"]')].map((svg) => {
        const vb = svg.viewBox.baseVal;
        const drawn = svg.getBoundingClientRect().width;
        const scale = drawn / vb.width || 1;
        const rects = [...svg.querySelectorAll('rect')].map((e) => ({
          x: +e.getAttribute('x'), y: +e.getAttribute('y'),
          w: +e.getAttribute('width'), h: +e.getAttribute('height'),
          rx: +(e.getAttribute('rx') || 0),
        })).filter((e) => Number.isFinite(e.x + e.y + e.w + e.h));
        let min = Infinity;
        const tight = [];
        const texts = [...svg.querySelectorAll('text')];
        for (const t of texts) {
          min = Math.min(min, parseFloat(getComputedStyle(t).fontSize) / scale);
          if (t.getAttribute('transform')) continue; // rotated: measured along its own axis
          const b = t.getBBox();
          const box = rects
            .filter((e) => b.x >= e.x && b.y >= e.y && b.y <= e.y + e.h && b.x <= e.x + e.w)
            .sort((a, c) => a.w * a.h - c.w * c.h)[0];
          const wall = box ? box.x + box.w : vb.width;
          const gap = wall - (b.x + b.width);
          if (gap < MIN_GAP) {
            tight.push('«' + t.textContent.trim().slice(0, 30) + '» зазор ' + gap.toFixed(0)
              + (box ? ' до стенки рамки' : ' до края холста'));
          }
        }
        const cap = svg.closest('.box') && svg.closest('.box').querySelector('p.dim');

        // Geometry check: fork clearance and arrow shafts
        const cramped = [];
        // Rule 26 is the geometry of block diagrams: arrows join rounded boxes
        // that carry a label. A plot or a figure of geometry has no such box -
        // its axis arrows point into the plane by design, its rectangles are
        // areas with square corners - and held to the rule it reddened every
        // plot of the math sites (nmt-math: 661 findings, math: 18).
        const blockDiagram = rects.some((r) => r.rx > 0 && [...svg.querySelectorAll('text')].some((t) => {
          const tx = +t.getAttribute('x'), ty = +t.getAttribute('y');
          return tx >= r.x && tx <= r.x + r.w && ty >= r.y && ty <= r.y + r.h;
        }));
        const paths = [...svg.querySelectorAll('path')];
        const polys = [...svg.querySelectorAll('polygon')].map((p) => {
          const pts = (p.getAttribute('points') || '').trim().split(/\s+/).map((pt) => pt.split(',').map(Number));
          const ys = pts.map((pt) => pt[1]);
          const xs = pts.map((pt) => pt[0]);
          return { pts, xs, ys, apexX: pts[0][0], apexY: pts[0][1], baseY: ys[1], baseX: xs[1] };
        });

        for (const p of paths) {
          const d = p.getAttribute('d') || '';
          const m = d.match(/M\s*(\d+)\s+(\d+)\s+L\s*\1\s+(\d+)\s+L\s*(\d+)\s+\3\s+L\s*\4\s+(\d+)/);
          if (m) {
            const barY = +m[3];
            const targetX = +m[4];
            const matchingPoly = polys.find((poly) => Math.abs(poly.apexX - targetX) <= 6);
            if (matchingPoly) {
              const shaft = Math.abs(matchingPoly.baseY - barY);
              if (shaft < 7) {
                cramped.push(`стрелка развилки упирается в перекладину: ножка ${shaft}px < 7px (x=${targetX})`);
              }
            }
          }
        }

        const lines = [...svg.querySelectorAll('line')].map((l) => ({
          x1: +l.getAttribute('x1'), y1: +l.getAttribute('y1'),
          x2: +l.getAttribute('x2'), y2: +l.getAttribute('y2'),
        }));
        for (const l of lines) {
          if (l.x1 === l.x2) {
            const isDown = l.y2 > l.y1;
            const matchingPoly = polys.find((p) => Math.abs(p.apexX - l.x2) <= 5 && (isDown ? (p.apexY >= l.y1 && p.apexY <= l.y2 + 8) : (p.apexY <= l.y1 && p.apexY >= l.y2 - 8)));
            if (matchingPoly) {
              const shaft = isDown ? (matchingPoly.baseY - l.y1) : (l.y1 - matchingPoly.baseY);
              if (shaft < 6) {
                cramped.push(`слишком короткая ножка вертикальной стрелки: ${shaft}px < 6px (x=${l.x1})`);
              }
              const touchesRect = rects.some((r) => l.x1 >= r.x - 6 && l.x1 <= r.x + r.w + 6 && Math.abs(l.y1 - (isDown ? r.y + r.h : r.y)) <= 6);
              if (!touchesRect) {
                cramped.push(`стрелка идет ниоткуда: начало (${l.x1}, ${l.y1}) не касается границы блока`);
              }
            }
          } else if (l.y1 === l.y2) {
            const isRight = l.x2 > l.x1;
            const matchingPoly = polys.find((p) => Math.abs(p.apexY - l.y1) <= 5 && (isRight ? (p.apexX >= l.x1 && p.apexX <= l.x2 + 8) : (p.apexX <= l.x1 && p.apexX >= l.x2 - 8)));
            if (matchingPoly) {
              const shaft = isRight ? (matchingPoly.baseX - l.x1) : (l.x1 - matchingPoly.baseX);
              if (shaft < 6) {
                cramped.push(`слишком короткая ножка горизонтальной стрелки: ${shaft}px < 6px (y=${l.y1})`);
              }
              const touchesRect = rects.some((r) => l.y1 >= r.y - 6 && l.y1 <= r.y + r.h + 6 && Math.abs(l.x1 - (isRight ? r.x + r.w : r.x)) <= 6);
              if (!touchesRect) {
                cramped.push(`горизонтальная стрелка идет ниоткуда: начало (${l.x1}, ${l.y1}) не касается границы блока`);
              }
            }
          }
        }

        // Arrowhead apex must touch a target block boundary
        for (const p of polys) {
          const pts = p.pts;
          if (pts.length !== 3) continue;
          let apex = null, dir = null;
          if (pts[1][1] === pts[2][1]) {
            apex = pts[0]; dir = pts[0][1] > pts[1][1] ? 'down' : 'up';
          } else if (pts[0][1] === pts[1][1]) {
            apex = pts[2]; dir = pts[2][1] > pts[0][1] ? 'down' : 'up';
          } else if (pts[0][1] === pts[2][1]) {
            apex = pts[1]; dir = pts[1][1] > pts[0][1] ? 'down' : 'up';
          } else if (pts[1][0] === pts[2][0]) {
            apex = pts[0]; dir = pts[0][0] > pts[1][0] ? 'right' : 'left';
          } else if (pts[0][0] === pts[1][0]) {
            apex = pts[2]; dir = pts[2][0] > pts[0][0] ? 'right' : 'left';
          } else if (pts[0][0] === pts[2][0]) {
            apex = pts[1]; dir = pts[1][0] > pts[0][0] ? 'right' : 'left';
          }
          if (!apex) continue;

          const touches = rects.some((r) => {
            if (dir === 'down') return apex[0] >= r.x - 6 && apex[0] <= r.x + r.w + 6 && Math.abs(apex[1] - r.y) <= 6;
            if (dir === 'up') return apex[0] >= r.x - 6 && apex[0] <= r.x + r.w + 6 && Math.abs(apex[1] - (r.y + r.h)) <= 6;
            if (dir === 'right') return apex[1] >= r.y - 6 && apex[1] <= r.y + r.h + 6 && Math.abs(apex[0] - r.x) <= 6;
            if (dir === 'left') return apex[1] >= r.y - 6 && apex[1] <= r.y + r.h + 6 && Math.abs(apex[0] - (r.x + r.w)) <= 6;
            return false;
          });
          if (!touches) {
            cramped.push(`наконечник стрелки указывает в пустоту: точка (${apex[0]}, ${apex[1]}) не касается границы блока`);
          }
        }

        // All non-banner rects must have at least one connection
        if (lines.length > 0 || paths.length > 0) {
          for (const r of rects) {
            if (r.w >= 260) continue; // ignore full-width banner containers
            let connected = false;
            for (const l of lines) {
              const p1 = l.x1 >= r.x - 6 && l.x1 <= r.x + r.w + 6 && l.y1 >= r.y - 6 && l.y1 <= r.y + r.h + 6;
              const p2 = l.x2 >= r.x - 6 && l.x2 <= r.x + r.w + 6 && l.y2 >= r.y - 6 && l.y2 <= r.y + r.h + 6;
              if (p1 || p2) { connected = true; break; }
            }
            if (!connected) {
              for (const p of polys) {
                for (const pt of p.pts) {
                  if (pt[0] >= r.x - 6 && pt[0] <= r.x + r.w + 6 && pt[1] >= r.y - 6 && pt[1] <= r.y + r.h + 6) {
                    connected = true; break;
                  }
                }
                if (connected) break;
              }
            }
            if (!connected) {
              for (const p of paths) {
                const mStart = (p.getAttribute('d') || '').match(/M\s*(\d+)\s+(\d+)/);
                const mEnd = (p.getAttribute('d') || '').match(/L\s*(\d+)\s+(\d+)\s*$/);
                if (mStart) {
                  const x = +mStart[1], y = +mStart[2];
                  if (x >= r.x - 6 && x <= r.x + r.w + 6 && y >= r.y - 6 && y <= r.y + r.h + 6) { connected = true; break; }
                }
                if (mEnd) {
                  const x = +mEnd[1], y = +mEnd[2];
                  if (x >= r.x - 6 && x <= r.x + r.w + 6 && y >= r.y - 6 && y <= r.y + r.h + 6) { connected = true; break; }
                }
              }
            }
            if (!connected) {
              cramped.push(`изолированный блок без связей: [x=${r.x}, y=${r.y}, w=${r.w}, h=${r.h}] не соединен со схемой`);
            }
          }
        }

        return {
          width: vb.width,
          capped: getComputedStyle(svg).maxWidth,
          label: (svg.getAttribute('aria-label') || '').trim(),
          labels: texts.length,
          smallest: Number.isFinite(min) ? +min.toFixed(1) : null,
          tight,
          cramped: blockDiagram ? cramped : [],
          caption: cap ? cap.textContent.trim() : null,
        };
      });
    }, { MIN_GAP });
  }
}
await browser.close();

// 1-4: the budget, the label and the caption of every diagram.
const CAPTION = /^(\S+)\s+(\d+)\./u;
let drawn = 0;
for (const lang of Object.keys(seen)) {
  let n = 0;
  let word = null;
  for (const [name, list] of Object.entries(seen[lang])) {
    for (const d of list) {
      const where = lang + '/' + name;
      if (d.width !== CANVAS) bad.push([where, 'холст шириной ' + d.width + ' единиц вместо ' + CANVAS]);
      if (d.capped !== CANVAS + 'px') bad.push([where, 'нет ограничения max-width:' + CANVAS + 'px, сейчас ' + d.capped]);
      if (!d.label) bad.push([where, 'пустой aria-label: читалке схема не достанется']);
      if (d.smallest !== null && d.smallest < MIN_LABEL) bad.push([where, 'наименьшая подпись ' + d.smallest + ' единиц вместо ' + MIN_LABEL]);
      for (const t of d.tight) bad.push([where, 'подпись не помещается: ' + t]);
      for (const c of d.cramped) bad.push([where, 'дефект геометрии стрелки: ' + c]);
      n += 1;
      drawn += 1;
      if (!d.caption) {
        bad.push([where, 'у схемы нет подписи <p class="dim">']);
        continue;
      }
      const m = CAPTION.exec(d.caption);
      if (!m) {
        bad.push([where, 'подпись не начинается со слова и номера: «' + d.caption.slice(0, 40) + '»']);
        continue;
      }
      if (word === null) word = m[1];
      else if (m[1] !== word) bad.push([where, 'подписи названы по-разному: «' + m[1] + '» против «' + word + '»']);
      if (+m[2] !== n) bad.push([where, 'номер подписи ' + m[2] + ', а по порядку ' + n]);
    }
  }
}

// 5: every source answers a diagram and every diagram a source.
const keyOf = (name) => name.replace(/\.html$/, '');
const basePages = new Set((pages[BASE] || []).map(keyOf));
for (const src of sources) {
  const key = src.split('-')[0].replace(/\.(mmd|py)$/, '');
  if (!basePages.has(key)) bad.push(['diagrams/' + src, 'исходник есть, а схемы на ' + BASE + '/' + key + '.html нет']);
}
for (const key of basePages) {
  if (!sources.some((s) => s.split('-')[0].replace(/\.(mmd|py)$/, '') === key)) {
    bad.push([BASE + '/' + key + '.html', 'схема есть, а исходника diagrams/' + key + '-*.mmd нет']);
  }
}

// 6: a translated page carries a translated diagram.
for (const lang of Object.keys(seen)) {
  if (lang === BASE) continue;
  for (const [name, list] of Object.entries(seen[lang])) {
    const base = (seen[BASE] || {})[name] || [];
    list.forEach((d, i) => {
      const where = lang + '/' + name;
      if (!base[i]) {
        bad.push([where, 'схема есть, а на ' + BASE + '/' + name + ' такой схемы нет']);
        return;
      }
      if (d.label === base[i].label) bad.push([where, 'aria-label совпадает с ' + BASE + ': схема не переведена']);
      if (d.labels !== base[i].labels) bad.push([where, 'подписей ' + d.labels + ', а на ' + BASE + ' их ' + base[i].labels + ': часть потеряна при переводе']);
    });
  }
}

console.log();
console.log('  Проверка схем: холст, подписи, исходники, перевод');
console.log('  ' + '-'.repeat(46));
console.log('  схем проверено: ' + drawn + ' на ' + total + (total === 1 ? ' странице' : ' страницах'));
console.log('  в браке:        ' + bad.length);
for (const [where, why] of bad.slice(0, 20)) console.log('        -> ' + where + ': ' + why);
if (bad.length > 20) console.log('        -> ... и ещё ' + (bad.length - 20));
console.log('  ' + '-'.repeat(46));
console.log('  ' + (bad.length ? 'КРАСНОЕ' : 'ЗЕЛЁНОЕ'));
console.log();
process.exit(bad.length ? 1 : 0);
