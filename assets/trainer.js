// trainer.js - прототип тренажёра: задача знает свой закон.
// Три формы НМТ: выбор одного из пяти (data-kind="choice"), соответствие (match),
// короткий ответ (short). Разбор задачи (.solution) закрыт, пока ученик не ответил
// верно: ответ, увиденный раньше попытки, учит читать ответы, а не закон.
// При ошибке задача ведёт к закону и его границам, а не к правильному ответу.
// После второй ошибки появляется кнопка «Показати розбір»: застрять навсегда
// на одной задаче хуже, чем увидеть разбор.
(function () {
  // Messages in the language of the page: the trainer is the same file on
  // every page, the words are not.
  const SAY = {
    uk: { right: 'Правильно.', wrong: 'Ні. Перечитай', law: 'закон', and: ' і його ', limits: 'межі', again: ', потім спробуй ще раз.', reveal: 'Показати розбір' },
    ru: { right: 'Правильно.', wrong: 'Нет. Перечитай', law: 'закон', and: ' и его ', limits: 'границы', again: ', потом попробуй ещё раз.', reveal: 'Показать разбор' },
    en: { right: 'Correct.', wrong: 'No. Reread the', law: 'law', and: ' and its ', limits: 'limits', again: ', then try again.', reveal: 'Show the solution' },
  };
  const say = SAY[document.documentElement.lang] || SAY.uk;
  const norm = (s) => s.trim().replace(',', '.').replace(/[\u2212\u2013]/g, '-').replace(/\s+/g, '');

  function verdict(task, ok) {
    let v = task.querySelector('.verdict');
    if (!v) { v = document.createElement('p'); v.className = 'verdict'; task.querySelector('.law-ref').before(v); }
    v.className = 'verdict ' + (ok ? 'right' : 'wrong');
    if (ok) { v.textContent = say.right; task.classList.add('solved'); return; }
    const tries = (Number(task.dataset.tries) || 0) + 1;
    task.dataset.tries = String(tries);
    const limit = task.dataset.limit;
    const law = task.querySelector('.law-ref a');
    v.innerHTML = say.wrong + ' ' + (law ? '<a href="' + law.getAttribute('href') + '">' + say.law + '</a>' : say.law) +
      (limit ? say.and + '<a href="#' + limit + '">' + say.limits + '</a>' : '') + say.again;
    if (tries >= 2) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'reveal'; b.textContent = say.reveal;
      b.addEventListener('click', () => task.classList.add('solved'));
      v.append(b);
    }
  }

  document.querySelectorAll('.task[data-kind="choice"]').forEach((task) => {
    task.querySelectorAll('.opts button').forEach((b) => {
      b.addEventListener('click', () => {
        const ok = b.dataset.opt === task.dataset.answer;
        b.classList.add(ok ? 'right' : 'wrong');
        verdict(task, ok);
      });
    });
  });

  document.querySelectorAll('.task[data-kind="short"]').forEach((task) => {
    const input = task.querySelector('input');
    const go = () => verdict(task, norm(input.value) === norm(task.dataset.answer));
    task.querySelector('.check').addEventListener('click', go);
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter') go(); });
  });

  document.querySelectorAll('.task[data-kind="match"]').forEach((task) => {
    task.querySelector('.check').addEventListener('click', () => {
      const want = task.dataset.answer.split(' ');
      const got = [...task.querySelectorAll('select')].map((s) => s.value);
      verdict(task, want.every((w, i) => w === got[i]));
    });
  });
})();
