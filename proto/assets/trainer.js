// trainer.js - прототип тренажёра: задача знает свой закон.
// Три формы НМТ: выбор одного из пяти (data-kind="choice"), соответствие (match),
// короткий ответ (short). Разбор задачи (.solution) закрыт, пока ученик не ответил
// верно: ответ, увиденный раньше попытки, учит читать ответы, а не закон.
// При ошибке задача ведёт к закону и его границам, а не к правильному ответу.
// После второй ошибки появляется кнопка «Показати розбір»: застрять навсегда
// на одной задаче хуже, чем увидеть разбор.
(function () {
  const norm = (s) => s.trim().replace(',', '.').replace(/[\u2212\u2013]/g, '-').replace(/\s+/g, '');

  function verdict(task, ok) {
    let v = task.querySelector('.verdict');
    if (!v) { v = document.createElement('p'); v.className = 'verdict'; task.querySelector('.law-ref').before(v); }
    v.className = 'verdict ' + (ok ? 'right' : 'wrong');
    if (ok) { v.textContent = 'Правильно.'; task.classList.add('solved'); return; }
    const tries = (Number(task.dataset.tries) || 0) + 1;
    task.dataset.tries = String(tries);
    const limit = task.dataset.limit;
    const law = task.querySelector('.law-ref a');
    v.innerHTML = 'Ні. Перечитай ' + (law ? '<a href="' + law.getAttribute('href') + '">закон</a>' : 'закон') +
      (limit ? ' і його <a href="#' + limit + '">межі</a>' : '') + ', потім спробуй ще раз.';
    if (tries >= 2) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'reveal'; b.textContent = 'Показати розбір';
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
