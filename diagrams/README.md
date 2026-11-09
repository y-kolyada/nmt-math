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

## Figures

| No. | Source | Page | What the reader is meant to see |
| :-- | :-- | :-- | :-- |
| 1 | `01-number-sets.py` + `01-number-sets.mmd` | `uk/01.html` | Кожна множина чисел лежить усередині наступної, і кожне розширення з'явилося заради нової дії. |
| 2 | `01-abs-line.py` | `uk/01.html` | Модуль - відстань до нуля: |−3| = |3| = 3. |
| 3 | `01-distributive.py` | `uk/01.html` | Розподільний закон як площа: a(b + c) = ab + ac. |
| 4 | `02-chain.py` | `uk/02.html` | Два кроки по 20 % від різних цілих: 100 → 120 → 96. |
| 5 | `02-inverse.py` | `uk/02.html` | Обернена пропорційність: добуток v · t сталий, як площа прямокутника. |
| 6 | `03-square.py` | `uk/03.html` | Квадрат суми: два прямокутники ab, які губить сліпий хід. |
| 7 | `04-extraneous.py` | `uk/04.html` | Сторонній корінь: при x = −1 обидві частини мають однаковий квадрат, але різні знаки. |
| 8 | `04-intervals.py` | `uk/04.html` | Метод інтервалів для (x − 3)(x + 3): знак змінюється лише в нулях множників. |
| 9 | `05-shift.py` | `uk/05.html` | f(x + 2): вершина переїхала з 0 у −2, тобто ліворуч. |
| 10 | `05-gauss.py` | `uk/05.html` | Сума арифметичної прогресії: сто пар по 101, поділені на два. |
| 11 | `06-three-questions.py` + `06-three-questions.mmd` | `uk/06.html` | Одна рівність, три запитання: степінь, корінь, логарифм. |
| 12 | `06-exp-log.py` | `uk/06.html` | Логарифм - дзеркало степеня: 2ˣ > 0 завжди, тому log₂ x існує лише при x > 0. |
| 13 | `06-abs-root.py` | `uk/06.html` | √(x²) = |x|: ліворуч від нуля корінь з квадрата не дорівнює x. |
| 14 | `07-unit-circle.py` | `uk/07.html` | Синус і косинус - координати точки одиничного кола; тотожність - теорема Піфагора. |
| 15 | `07-symmetry.py` | `uk/07.html` | Формула зведення як симетрія кола: sin(π − α) = sin α. |
| 16 | `07-half.py` | `uk/07.html` | sin x = 1/2: дві точки на одному оберті, далі - повторення через 2π. |
| 17 | `08-tangent.py` | `uk/08.html` | Похідна як нахил дотичної: для y = x² у точці 1 нахил дорівнює 2. |
| 18 | `08-area.py` | `uk/08.html` | Ньютон - Лейбніц: площа росте на смужку f(x) · h, отже площа - первісна функції. |
| 19 | `08-cubic.py` | `uk/08.html` | Екстремум там, де похідна змінює знак: максимум у 0, мінімум у 2. |
| 20 | `09-tree.py` + `09-tree.mmd` | `uk/09.html` | Правило добутку як дерево: 2 · 2 = 4 рівноможливі наслідки. |
| 21 | `09-dice.py` | `uk/09.html` | Рівноможливі - 36 пар граней, а не 11 сум: сума 7 займає 6 клітинок з 36. |
| 22 | `10-angle-sum.py` | `uk/10.html` | Сума кутів трикутника: три кути при вершині B складають пряму лінію. |
| 23 | `10-inscribed.py` | `uk/10.html` | Вписаний кут - половина центрального на тій самій дузі: 100° і 50°. |
| 24 | `11-scale.py` | `uk/11.html` | Сторона подвоїлася - площа зросла вчетверо: 3² = 9, 6² = 36. |
| 25 | `11-pythagoras.py` | `uk/11.html` | Доведення теореми Піфагора площею: чотири трикутники і квадрат c². |
| 26 | `12-vector.py` | `uk/12.html` | Координати вектора - кінець мінус початок: AB = (2 − 5; 4 − 1) = (−3; 3). |
| 27 | `12-distance.py` | `uk/12.html` | Відстань між точками - теорема Піфагора: √(3² + 4²) = 5. |
| 28 | `13-cube.py` | `uk/13.html` | Ребро вдвічі - об'єм у 2³ = 8 разів. |
| 29 | `13-unfold.py` | `uk/13.html` | Бічна поверхня прямої призми - прямокутник зі сторонами P і h. |
| 30 | `13-diagonal.py` | `uk/13.html` | Діагональ паралелепіпеда: Піфагор двічі, d² = a² + b² + c². |
| 31 | `navigator-links.py` + `navigator-links.mmd` | `uk/navigator.html` | Як блоки виростають один з одного: алгебра зверху, геометрія знизу. |
