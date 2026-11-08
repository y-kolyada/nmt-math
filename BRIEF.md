# Brief for a new site of the series

Paste this into a fresh session, with the row of your site filled in.

| Repo (dir) | Site name | Topic chip | Storage key | Search word |
| :-- | :-- | :-- | :-- | :-- |
| `git` | `devops-git` | `Git` | `git` | `rebase` |
| `github-actions` | `devops-github-actions` | `GitHub Actions` | `gha` | `workflow` |
| `terraform` | `devops-terraform` | `Terraform` | `terraform` | `state` |
| `aws-iam` | `devops-aws-iam` | `AWS IAM` | `aws-iam` | `policy` |
| `newrelic` | `sre-newrelic` | `New Relic` | `newrelic` | `NRQL` |

## 1. Stamp the site (one command, from the seed)

```
cd <factory root>/seed/swa
./bootstrap.sh ../../courses/<repo> <site name> "<topic chip>" <storage key> <search word>
```

It copies the seed, writes `site.conf`, stamps the pages (Russian skeletons, three languages as stubs), links the factory's `node_modules`, runs the three generators and removes its own scaffolding. How many pages it stamped is printed by the stamp itself. Then:

```
cd <factory root>/courses/<repo>
./check.sh
```

The check must be green before any content is written, and it is green on a freshly stamped site. How many lines its summary holds is printed by the check itself: a number written here rots the moment the engine grows a check, and then a pilot looks for a line that does not exist.

The symlink to the factory's `node_modules` is made by the stamp, not by hand. Without it the site's own checks go red: they resolve `js-yaml` at the literal path `node_modules/js-yaml` inside the site. A freshly stamped site hides that, because it declares nothing and both checks pass on an empty manifest; it would surface one shift later, on the first page of content.

## 1a. The first commit, and the branches

Two starting points, and the stamp is the same in both.

**The repository already exists** with a one-line `chore(init)` commit and the branches `main`, `dev` and `prod` on `origin`. This is the usual case. Work on `dev`, create no branches. The `README.md` of the empty repository is removed, because no site of the series carries one:

```
git rm -q README.md
git add -A && git commit -m "chore(seed): stamp the site from seed/swa"
```

**There is no repository yet.** `scripts/src/bash/cources/init-course.sh` stamps, runs `git init -b main`, makes the first commit and the branches `prod` and `dev`, and runs the check.

`.gitignore` comes from the seed and keeps the `node_modules` symlink, `__pycache__` and the harness's session analytics (`docs/codemie/`, `.codemie/`) out of that commit. The analytics file name carries a work email slug, so `git add -A` must never be the thing that finds it.

## 2. Read the rules

`AGENTS.md` in the site, all of it. Section 1 is the one that matters most: **this repository does not edit `assets/` or `tools/`.** A defect there is one line in `lessons/notes-1.md` and a fix in the seed, once, for every site.

## 3. Write the task before any page

`lessons/step-1.md`: the goal, **exactly three predicates**, the boundaries. Show the predicates to the Conductor and stop. The work starts on the word "делаем".

## 4. The first delivery, when it is approved

Russian only, two pages of real text:

- `ru/index.html` - the landing page: what the site is, who it is for, what the reader leaves with. It holds the reader, so it is not a table of contents in prose.
- `ru/01.html` - the first topic: the mechanisms the rest of the site builds on.
- The fifteen navigation titles and the glossary stay as they are until the Architect approves the plan of sections. Do not invent fifteen names in passing.
- Every claim about the tool is executed before it is published. If the examples cannot be run in this session, the claim does not go on the page.
- Run `python3 tools/build-meta.py`, `python3 tools/build-search.py`, then `./check.sh`.

## 5. Report back

Commit locally, never push. In the report: what the predicates say, the output of `./check.sh`, the word count of the two pages, and anything that belongs in the seed rather than in this site.

