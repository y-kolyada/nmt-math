# Profile `practice`: the sites of the conductor's practice

This file is part of the charter for every site whose `site.conf` says `profile = practice`. Where it differs from `AGENTS.md`, this file wins; where it is silent, `AGENTS.md` holds. It reaches the sites through `sync.sh` like the charter.

Born on `agent-os` (2026-11-10, ordered by the conductor through `Step 3 (talkaos)` of the factory plan). The numbers below live in `tools/siteconf.py`; this file says why they are what they are.

## 1. What the subject is

The subject is a practice, not a tool and not an exam: how a person and several AI agents run projects for months across machines without losing the context. There is no exam to measure the blocks against, so the profile keeps the law chain of `study` and drops everything that points at an exam.

## 2. Skeleton

1. **Languages.** Russian is the source (`ru/`), then Ukrainian (`uk/`) and English (`en/`), the order of the talk's decks. The stubs of `uk` and `en` point at the Russian page.
2. **Fifteen blocks, not fifteen sections.** Pages `01`-`15` are blocks of laws in the order the practice grew. There are no example chapters and no question banks: practice lives inside every block, bound to its law. A block exists only if it has a law that does not follow from the laws of its neighbours.
3. **Menu groups.** The menu carries seven captions before their first block: Проблема (01), Люди (03), Память (04), Работа (07), Оркестр (10), Цена (13), Фабрики (15), with Ukrainian and English captions beside them in `tools/siteconf.py`. A caption is `<li class="group">`, not an item, and the checks count only items. Twenty-two rows do not fit the visible panel of an 860px window at the series size, so the stamp marks the menu `data-dense` and `assets/study.css` tightens its rows on a wide screen only. **Menu titles must stay one line:** the dense menu fits with about 20px to spare, and a title that wraps takes that back. A long block title gets a short form in the menu.
4. **Navigator: eight lenses of practice**, the questions a conductor asks of any practice: `lens-failure` (как ломается), `lens-record` (что записано), `lens-check` (чем проверено), `lens-roles` (кто отвечает), `lens-perimeter` (границы дозволенного), `lens-cost` (сколько стоит), `lens-scale` (что меняет масштаб), `lens-tomorrow` (что взять завтра). Each written lens ends with `<p><strong>Связанные блоки курса:</strong> ...</p>`.
5. **No exam.** `site.conf` names no `slice`; `tools/build-frequency.py` and `tools/build-sources.py` do nothing (`exam = False` in the profile), and `./check.sh` has no rows for them, as on `assess`.
6. The glossary, the navigator, the term cards and every series rule about them hold as in `AGENTS.md`.

## 3. The unit is a law

A block holds one or a few laws. Each law follows the chain of `profiles/study.md` §2, with the content of the steps changed:

| Step | Here |
| :-- | :-- |
| 0 · Зацепка | **a real incident from the factory's records** in which the habitual move gave a wrong result; cited by its step, commit or register line |
| 1 · Понятие | the object in the language of the practice: session, work order, gate, key |
| 2 · Закон | the principle in a frame, `<div class="law" id="law-...">` |
| 3 · Почему так | the mechanism, not the slogan |
| 4 · Границы | `<div class="limit" id="limit-...">`: where the law does not hold and what it costs |
| 5 · Применение | a scenario from the repository: a command, a document, a commit |
| 6 · Обратный ход | someone else's failure described without a hint: the reader names the law |

**Three predicates close every block:** I name the law behind someone else's failure; I explain why it holds; I find the error in someone else's setup (a work order, an acceptance, a session).

**Every claim about a record is a claim about a file.** A step 0 incident names where it is written; a number names the command that measured it. What cannot be pointed at does not go on the page.

## 4. The trainer: one form, the same contract

**Proposal of the executor, 2026-11-10, for the conductor to confirm.** Every block carries one "find the error" item, and it uses the trainer contract of `profiles/study.md` §3 unchanged, in one form only:

- `<div class="task" data-kind="choice" data-answer="..." data-limit="limit-...">`, whose options are the lines of someone else's artifact (a work order, an acceptance, a session plan) and whose answer is the wrong line;
- `<p class="law-ref">` names the law with a link to its frame; `<div class="solution">` says why the line is wrong and what the right line is;
- `data-mode="reverse"` when the block's step 6 asks the reader to name the law as well.

**Why the full contract and not a lighter one.** What makes a "find the error" item teach is exactly what the contract already enforces: the answer stays closed until the reader commits, and a wrong pick leads back to the law and its limit rather than to the answer. A lighter form (a `<details>` with the answer) shows the answer to anyone who clicks first. The contract also costs nothing new: `assets/trainer.js` already speaks `ru`, `uk` and `en`, and the page checks already run it. The forms `short` and `match` are not used: the subject has no numbers to type and no exam format to imitate.

## 5. Figures

Schemes only (`diagrams/NN-name.mmd`), under the rules of `profiles/study.md` §6, points 1, 2 and 4: a figure complements the text and never replaces it, it lives inside the step it explains, and its caption reads `Рисунок N.` There are no generated mathematical figures.
