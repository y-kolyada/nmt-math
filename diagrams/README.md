# Diagram sources

A figure on a page is **inline SVG**, not an image file (AGENTS.md section 5 rule 18; `node tools/check-diagrams.mjs`
guards it). On this study site a figure **complements the text and never replaces it** (`profiles/study.md` section 6):
the step reads in full without the figure, and every figure carries an `aria-label` that says what it shows.

## Two kinds of source

- **Mathematical figures** (graphs, circles, triangles, solids): `NN-name.py`. The generator computes the coordinates
  from the same formula the page states and returns the SVG with its Ukrainian and Russian text.
- **Schemes** (sets, trees, the graph of blocks): `NN-name.mmd` holds the structure in Mermaid, and `NN-name.py` beside
  it draws that structure. **The truth about the renderer:** no Mermaid renderer is installed in this factory, so the
  SVG on the page is drawn by the generator from the `.mmd`, not exported from it. If the `.mmd` changes, the `.py`
  is changed with it.

## How a figure reaches the page

A page marks the place with an empty pair `<!-- fig:05-shift --><!-- /fig:05-shift -->`, and

```bash
python3 diagrams/build.py          # bake every figure, number the captions through the folder
python3 diagrams/build.py --check  # red if a baked figure drifted from its source
```

`fig.py` holds the shared helpers (canvas 320, axes, curves from functions, the accent colour `--acc`).

## Figures in tasks

A task of the trainer may carry a figure: `NN-task-name.py`, baked inside the `div.task` the same way. The rule is strict (`lessons/step-05-figures.md`): every number the task needs stands in its text, and the figure only shows it. The task carries `data-claim="NN-task-name"`, and a line of `tools/claims.tsv` runs

```bash
python3 diagrams/answer.py 11-task-height '15*20/math.hypot(15, 20)'
```

which computes the answer from the numbers of the condition and compares it with the answer of the task on every language page: a task whose answer cannot be computed from its own text turns the claim check red.

## Data on the figure

The class «Дані на рисунку» / «Данные на рисунке» (`lessons/step-06-reading.md`) turns the rule of the section above around: the numbers the task needs stand only on the figure, and reading them is the skill. Such a task is `NN-read-name.py`, carries the line `p.task-class` with its role (read and apply, choose what is needed, read and link) and keeps its numbers in a dictionary `DATA` of the generator; the figure is drawn from it and its `aria-label` names every number, so a screen reader user solves the task too. A line of `tools/claims.tsv` runs

```bash
python3 diagrams/answer.py --figure 12-read-dist 'math.hypot(x2 - x1, y2 - y1)'
```

which computes the answer over the names of `DATA`, compares it with the task on every language page, and checks that every number of `DATA` is a label of the baked figure, is named in its `aria-label` and is absent from the condition. A number written into the condition turns the line red. `box.py` (a rectangular box) and `bars.py` (a bar chart) are shared drawing helpers, not figures.

## Figures

| No. | Source | Page | What the reader is meant to see |
| :-- | :-- | :-- | :-- |
| 1 | `01-number-sets.py` + `01-number-sets.mmd` | `uk/01.html` | Кожна множина чисел лежить усередині наступної, і кожне розширення з'явилося заради нової дії. |
| 2 | `01-abs-line.py` | `uk/01.html` | Модуль - відстань до нуля: |−3| = |3| = 3. |
| 3 | `01-distributive.py` | `uk/01.html` | Розподільний закон як площа: a(b + c) = ab + ac. |
| 4 | `02-chain.py` | `uk/02.html` | Два кроки по 20 % від різних цілих: 100 → 120 → 96. |
| 5 | `02-inverse.py` | `uk/02.html` | Обернена пропорційність: добуток v · t сталий, як площа прямокутника. |
| 6 | `02-task-pie.py` | `uk/02.html` | До задачі: кругова діаграма, у якій сектор - частка цілого. |
| 7 | `02-read-share.py` | `uk/02.html` | До задачі: продаж книжок за п’ять днів. |
| 8 | `02-read-base.py` | `uk/02.html` | До задачі: діаграма, шкала якої починається не з нуля. |
| 9 | `02-read-change.py` | `uk/02.html` | До задачі: ціна яблук за чотири місяці. |
| 10 | `03-square.py` | `uk/03.html` | Квадрат суми: два прямокутники ab, які губить сліпий хід. |
| 11 | `04-extraneous.py` | `uk/04.html` | Сторонній корінь: при x = −1 обидві частини мають однаковий квадрат, але різні знаки. |
| 12 | `04-intervals.py` | `uk/04.html` | Метод інтервалів для (x − 3)(x + 3): знак змінюється лише в нулях множників. |
| 13 | `04-task-param.py` | `uk/04.html` | До задачі: число коренів рівняння x² − 4x = a як число спільних точок параболи і прямої y = a. |
| 14 | `05-shift.py` | `uk/05.html` | f(x + 2): вершина переїхала з 0 у −2, тобто ліворуч. |
| 15 | `05-gauss.py` | `uk/05.html` | Сума арифметичної прогресії: сто пар по 101, поділені на два. |
| 16 | `05-task-shift.py` | `uk/05.html` | До задачі: графік y = x², зсунутий праворуч і вниз. |
| 17 | `05-task-abs.py` | `uk/05.html` | До задачі: графік y = |x|, зсунутий ліворуч. |
| 18 | `05-task-common.py` | `uk/05.html` | До задачі: спільні точки параболи і прямої. |
| 19 | `05-read-vertex.py` | `uk/05.html` | До задачі: парабола з позначеною вершиною. |
| 20 | `05-read-shift.py` | `uk/05.html` | До задачі: графік y = |x| і зсунутий графік на сітці з кроком 2. |
| 21 | `05-read-ineq.py` | `uk/05.html` | До задачі: парабола, яка перетинає вісь x у двох позначених точках. |
| 22 | `06-three-questions.py` + `06-three-questions.mmd` | `uk/06.html` | Одна рівність, три запитання: степінь, корінь, логарифм. |
| 23 | `06-exp-log.py` | `uk/06.html` | Логарифм - дзеркало степеня: 2ˣ > 0 завжди, тому log₂ x існує лише при x > 0. |
| 24 | `06-abs-root.py` | `uk/06.html` | √(x²) = |x|: ліворуч від нуля корінь з квадрата не дорівнює x. |
| 25 | `06-task-log.py` | `uk/06.html` | До задачі: точка графіка логарифма з ординатою 3. |
| 26 | `07-unit-circle.py` | `uk/07.html` | Синус і косинус - координати точки одиничного кола; тотожність - теорема Піфагора. |
| 27 | `07-symmetry.py` | `uk/07.html` | Формула зведення як симетрія кола: sin(π − α) = sin α. |
| 28 | `07-half.py` | `uk/07.html` | sin x = 1/2: дві точки на одному оберті, далі - повторення через 2π. |
| 29 | `08-tangent.py` | `uk/08.html` | Похідна як нахил дотичної: для y = x² у точці 1 нахил дорівнює 2. |
| 30 | `08-area.py` | `uk/08.html` | Ньютон - Лейбніц: площа росте на смужку f(x) · h, отже площа - первісна функції. |
| 31 | `08-cubic.py` | `uk/08.html` | Екстремум там, де похідна змінює знак: максимум у 0, мінімум у 2. |
| 32 | `08-task-area.py` | `uk/08.html` | До задачі: криволінійна трапеція під параболою. |
| 33 | `09-tree.py` + `09-tree.mmd` | `uk/09.html` | Правило добутку як дерево: 2 · 2 = 4 рівноможливі наслідки. |
| 34 | `09-dice.py` | `uk/09.html` | Рівноможливі - 36 пар граней, а не 11 сум: сума 7 займає 6 клітинок з 36. |
| 35 | `09-task-spinner.py` | `uk/09.html` | До задачі: рулетка з восьми рівних секторів. |
| 36 | `10-cor-parallelogram.py` | `uk/10.html` | Наслідок: сусідні кути паралелограма в сумі 180°, протилежні рівні. |
| 37 | `10-cor-cyclic.py` | `uk/10.html` | Наслідок: у вписаному чотирикутнику сума протилежних кутів дорівнює 180°. |
| 38 | `10-cor-circumcenter.py` | `uk/10.html` | Наслідок: серединні перпендикуляри до сторін трикутника перетинаються в центрі описаного кола. |
| 39 | `10-cor-midline.py` | `uk/10.html` | Наслідок: середня лінія трикутника паралельна третій стороні і дорівнює її половині. |
| 40 | `10-angle-sum.py` | `uk/10.html` | Сума кутів трикутника: три кути при вершині B складають пряму лінію. |
| 41 | `10-inscribed.py` | `uk/10.html` | Вписаний кут - половина центрального на тій самій дузі: 100° і 50°. |
| 42 | `10-task-midline.py` | `uk/10.html` | До задачі: трикутник, вершини якого - середини сторін трикутника ABC. |
| 43 | `10-task-exterior.py` | `uk/10.html` | До задачі: зовнішній кут трикутника при вершині C. |
| 44 | `10-task-diameter.py` | `uk/10.html` | До задачі: трикутник, вписаний у коло, одна сторона якого - діаметр. |
| 45 | `10-read-angles.py` | `uk/10.html` | До задачі: трикутник із двома позначеними кутами. |
| 46 | `10-read-par.py` | `uk/10.html` | До задачі: паралелограм із позначеним кутом і підписаною стороною. |
| 47 | `10-read-circle.py` | `uk/10.html` | До задачі: вписаний трикутник, центральний кут і вписаний кут. |
| 48 | `11-scale.py` | `uk/11.html` | Сторона подвоїлася - площа зросла вчетверо: 3² = 9, 6² = 36. |
| 49 | `11-cor-tangents.py` | `uk/11.html` | Наслідок: відрізки дотичних, проведених до кола з однієї точки, рівні. |
| 50 | `11-cor-chords.py` | `uk/11.html` | Наслідок: хорда дорівнює подвоєному радіусу, помноженому на синус вписаного кута. |
| 51 | `11-pythagoras.py` | `uk/11.html` | Доведення теореми Піфагора площею: чотири трикутники і квадрат c². |
| 52 | `11-task-height.py` | `uk/11.html` | До задачі: висота CH прямокутного трикутника, проведена до гіпотенузи. |
| 53 | `11-task-trapezoid.py` | `uk/11.html` | До задачі: висота рівнобічної трапеції, опущена з вершини меншої основи. |
| 54 | `11-task-tangential.py` | `uk/11.html` | До задачі: чотирикутник, описаний навколо кола. |
| 55 | `11-read-rect.py` | `uk/11.html` | До задачі: прямокутник із підписаними сторонами і діагональ. |
| 56 | `11-read-trap.py` | `uk/11.html` | До задачі: трапеція, на якій підписано чотири довжини. |
| 57 | `11-read-rhombus.py` | `uk/11.html` | До задачі: ромб і дві його діагоналі. |
| 58 | `12-vector.py` | `uk/12.html` | Координати вектора - кінець мінус початок: AB = (2 − 5; 4 − 1) = (−3; 3). |
| 59 | `12-cor-line.py` | `uk/12.html` | Наслідок: b - точка перетину з віссю y, k - підйом прямої на один крок праворуч. |
| 60 | `12-distance.py` | `uk/12.html` | Відстань між точками - теорема Піфагора: √(3² + 4²) = 5. |
| 61 | `12-task-parallelogram.py` | `uk/12.html` | До задачі: паралелограм ABCD, у якого невідома вершина D. |
| 62 | `12-read-dist.py` | `uk/12.html` | До задачі: дві точки, координати яких видно на осях. |
| 63 | `12-read-slope.py` | `uk/12.html` | До задачі: пряма на сітці, у якої крок по осях різний. |
| 64 | `12-read-circle.py` | `uk/12.html` | До задачі: коло, його центр і точка на колі. |
| 65 | `13-cube.py` | `uk/13.html` | Ребро вдвічі - об'єм у 2³ = 8 разів. |
| 66 | `13-cor-revolution.py` | `uk/13.html` | Наслідок: конус утворюється обертанням прямокутного трикутника навколо катета; гіпотенуза стає твірною. |
| 67 | `13-unfold.py` | `uk/13.html` | Бічна поверхня прямої призми - прямокутник зі сторонами P і h. |
| 68 | `13-diagonal.py` | `uk/13.html` | Діагональ паралелепіпеда: Піфагор двічі, d² = a² + b² + c². |
| 69 | `13-task-perp.py` | `uk/13.html` | До задачі: прямокутний паралелепіпед і площина його нижньої основи. |
| 70 | `13-task-pyramid.py` | `uk/13.html` | До задачі: правильна чотирикутна піраміда і її висота. |
| 71 | `13-read-diag.py` | `uk/13.html` | До задачі: прямокутний паралелепіпед із підписаними ребрами і його діагональ. |
| 72 | `13-read-volume.py` | `uk/13.html` | До задачі: прямокутний паралелепіпед, на якому підписано три ребра і діагональ основи. |
| 73 | `13-read-vector.py` | `uk/13.html` | До задачі: прямокутний паралелепіпед в осях координат і вектор BD₁. |
| 74 | `navigator-links.py` + `navigator-links.mmd` | `uk/navigator.html` | Як блоки виростають один з одного: алгебра зверху, геометрія знизу. |
