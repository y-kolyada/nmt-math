# Profile `study`: the school study sites

This file is part of the charter for every site whose `site.conf` says
`profile = study`. Where it differs from `AGENTS.md`, this file wins; where it is
silent, `AGENTS.md` holds. It reaches the sites through `sync.sh` like the charter.

Born on `nmt-math` (2026-11-08, accepted by the Conductor 2026-11-09). The
numbers below live in `tools/siteconf.py`; this file says why they are what
they are.

## 1. Skeleton

1. **Languages.** Ukrainian is the source (`uk/`), Russian is the second
   language (`ru/`), translated at the very end. English, if it ever comes, is
   one `langs` override in `site.conf`, not a new profile.
2. **Thirteen blocks, not fifteen sections.** Pages `01`-`13` are blocks of the
   subject in the order the subject grew, each built from the previous ones.
   There are no example chapters and no question banks: practice lives inside
   every block, bound to its law. The menu may group the blocks with
   `<li class="group">Алгебра і початки аналізу</li>`: a group is a caption,
   not an item, and the checks count only items.
3. **Navigator: seven subject lenses** instead of the nine engineering ones:
   `lens-language` (мова і запис), `lens-laws` (закони), `lens-proof`
   (доведення), `lens-scope` (застосовність), `lens-limits` (межі),
   `lens-links` (зв'язки між розділами), `lens-traps` (пастки формулювань
   НМТ). Each written lens ends with `<p><strong>Пов'язані блоки курсу:</strong> ...</p>`.
4. The glossary, the navigator, the term cards and every series rule about
   them hold as in `AGENTS.md`, read for the Ukrainian source.

## 2. The unit is a law, not a task type

A block holds several laws. Each law follows the chain that the prototype
proved, in this order, with the step label above the heading:

| Step | What | Why |
| --- | --- | --- |
| 0 · Зачіпка | a case where the habitual blind move gives a wrong answer | a habit is changed only by its own failure |
| 1 · Поняття | what the object is, in the language of mathematics | without the object a law is a string of signs |
| 2 · Закон | the formula in a frame, `<div class="law" id="law-...">` | what must be recognised in seconds |
| 3 · Чому так | a proof or a clear intuition, for the age | a law without "why" never binds to an example |
| 4 · Межі | `<div class="limit" id="limit-...">`: where the law breaks | half of exam errors are a law used outside its domain |
| 5 · Застосування | tasks in the exam's forms, each naming its law | the law and the task are tied explicitly |
| 6 · Зворотний хід | a task without the hint: the reader names the law | stripping the plot off a task is the exam's main skill |

A block may run the chain once per law or gather steps 5 and 6 for several
laws at the end; the order of steps inside one law does not change.

**No inflation.** A worked task names as many laws as actually work in it,
usually one or two. A story about a video sped up 1.5 times is `t = S / k`,
not three "laws".

**Three levels of foundation** (Conductor, 2026-11-09). If an exam task has a
solution, the site holds what it rests on, at one of three levels:

1. **Law** - the frame `.law`. Few of them: a new law appears only when the
   topic cannot be derived from the laws already on the site.
2. **Corollary** - a theorem derived from a law of the block, standing under
   its law: `<div class="corollary" id="cor-..." data-law="law-...">` with
   `<p class="corollary-of">` (a link to the law), `<p class="corollary-name">`
   and a derivation of two to five lines. It counts for its law in the
   frequency and the exam slice (`tools/examslice.py` parent()), so laws do not
   multiply while every task has a foundation.
3. **Method** - not a new statement but a scheme of applying laws, in step 5:
   `<div class="method">` with `<h3 id="method-...">` and a trainer task tied
   to the laws it uses.

The exam slice tags a task `NN:law-...`, `NN:cor-...` or `NN:method-...`;
`tools/build-frequency.py` is red on a tag that names nothing on its page.

**Three predicates close every block**: I solve 8 of 10 tasks of this kind
without a hint; I explain aloud why the formula works; I find the error in
someone else's solution. Every block carries one "find the error" item.

## 3. The trainer contract (`assets/trainer.js`)

A task is `<div class="task" data-kind="choice|short|match" data-answer="..." data-limit="limit-id">`
with a `.task-kind` line (form and points), a `<p class="law-ref">` naming the law
with a link to its frame, and a `<div class="solution">` with the worked answer.

- The solution stays closed until a correct answer: an answer seen before the
  attempt teaches reading answers, not the law. After the second wrong
  attempt a "Показати розбір" button appears.
- A wrong answer leads to the law and its limit, never to the right answer.
- `data-mode="reverse"` hides the law line too until the task is solved
  (step 6).
- Choice: buttons `data-opt="А".."Д"`; wrong options are real blind moves,
  explained in the solution. Match: three `<select>`, `data-answer="В Б А"`.
  Short: one `<input>`, comma or dot accepted, Unicode minus accepted.

## 4. Sources and rights

Exam papers (zno.osvita.ua, УЦОЯО) are not copied: the tasks there are images
and the rights are not ours. Every task on a study site is our own analogue;
a link to an official task may stand next to it. Figures are our own SVG.

## 5. Formulas

TeX in `data-tex`, baked by `tools/build-math.py`. **The decimal comma is
written `0\text{,}25`**: `0{,}25` bakes into an operator comma and the reader
sees "0, 25". Every second number in Ukrainian mathematics has a comma, so
this is not a corner case.

## 6. Figures

Decided with the Conductor 2026-11-09.

1. **A figure complements the text and never replaces it.** The text of every
   step stays complete without the figure: reading and drawing figures are
   skills of their own that a pupil is still building, and a page must read in
   full to a screen reader on a phone. Every figure carries a non-empty
   `aria-label` that says what the figure shows, and a caption.
2. **Figures live inside the steps**, mostly in "Чому так" and "Межі", as many
   as the law needs (usually two to four per block). There is no separate
   "figures" axis: it would tear the picture away from the law it explains.
3. **Two kinds of source in `diagrams/`.** Schemes (links, chains of
   derivation, order of steps) have a Mermaid source `NN-name.mmd`.
   Mathematical figures (graphs, circles, triangles, solids) have a generator
   `NN-name.py` that computes exact coordinates from the same formula the page
   states and prints the SVG: a parabola drawn from its equation, not by eye.
   `tools/check-diagrams.mjs` accepts both kinds as sources.
4. Captions read `Рисунок N.`, numbered through the language folder; the
   series rules of rule 18 (canvas 320, labels of at least 12 units,
   `currentColor`) hold for both kinds.

## 7. External sources and the settings window

A study site may point beyond itself, to the real exam tasks that lean on a
block's laws. The rule is the same as in section 4: **a link, never a copy**.

1. **The slice.** `site.conf slice = lessons/<file>.tsv` holds the tagged tasks
   (year, session, number, figure, our laws, url); `tools/examslice.py` reads
   it. The frequency line prints the second number from it
   (`tools/build-frequency.py`), and `tools/build-sources.py` prints the section
   "Посилання на завдання із зовнішніх джерел" before the artifacts of each block.
   The section speaks of sources in general, because there may be several
   platforms; what belongs to one source (its heading and lead) lives in its own
   block `<div class="ext-source" data-ext-source="<source>">` and leaves the page
   with its last year.
2. **A year is a block of its own**: `<div class="ext" data-ext="<source>:<year>">`.
   The reader switches a whole source or a single year off in the settings
   (`assets/sources.js`, the gear in the tray); the choice is stored in
   `localStorage swa-<site>-ext-off`, and the search (`assets/search.js`) offers
   every year that is on as a filter of its own and does not search the years
   that are off.
3. **The look is the site's own.** The settings window repeats the search
   window (frame, head, cross, backdrop, full screen on a phone); a year block
   wears the `.box` frame; a checked box wears the accent of a pressed search
   filter. The gear follows the Conductor's sample: six wide teeth and a hole, filled on hover. A new external source adds its texts to `build-sources.py` and `sources.js`, not a new style.
4. **Polite collection.** Before any request to a source site the volume and the
   rate are agreed with the Conductor; robots.txt is read first, requests go one
   at a time, at most one per five seconds, each file once, and the run stops
   on 429, 5xx or a disallow.
