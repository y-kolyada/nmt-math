---
name: site-bootstrap
description: Guides the initialization and bootstrapping of a brand-new course site of the AI Factory series from seed/swa, setting up git branches (main, dev, prod), verifying a green check out of the box, and preparing Batch 1 under the stop crane.
---

# Skill · Site Bootstrap and Initialization

Use this skill whenever starting a brand-new course site of the AI Factory series (e.g. `docker`, `newrelic`, or any course from `assess-tracks` or `study-tracks`) from absolute scratch. `<factory root>` below is the checkout of `ai-factory-builder` on the host in use.

## 1. Parameters of the Site

Identify the five parameters of the new site with the Conductor:
- `<target-dir>`: destination path, e.g. `../../courses/docker`
- `<site-name>`: header brand, e.g. `devops-docker`
- `<topic-chip>`: amber chip in the header, e.g. `Docker`
- `<storage-key>`: local storage and cookie key prefix, e.g. `docker`
- `[search-word]`: the smoke search term. The Architect's decision of 26.10.2026: `Раздел` for every new site, because only placeholders exist on a fresh site and the word is replaced by real content later.

## 2. Execute Bootstrap from the Seed

### Option A · No repository exists yet
From `<factory root>`:
```bash
./scripts/src/bash/cources/init-course.sh <repo-slug> [site-name] [topic-chip] [storage-key] [search-word]
# e.g.:
./scripts/src/bash/cources/init-course.sh aws-vpc devops-aws-vpc "AWS VPC" aws-vpc Раздел
```
The script stamps, links `node_modules`, runs `git init -b main`, makes the first commit and the branches `prod` and `dev`, and runs the check.

### Option B · The repository already exists (the usual case)
The repository has a `chore(init)` commit and the branches `main`, `dev`, `prod` on `origin`. Stamp from the seed:
```bash
cd <factory root>/seed/swa
./bootstrap.sh ../../courses/<repo> <site-name> "<topic-chip>" <storage-key> <search-word>
```

What the stamp does automatically:
- Copies the static SWA engine, assets, checks, and harness.
- Writes `site.conf` with site-specific metadata.
- Stamps all HTML pages (landing page `index.html`, 15 topics, `glossary.html`, `navigator.html` across `ru`, `en`, `uk`, `de`, plus the root `index.html` language door). The stamp prints how many.
- Links the factory's `node_modules` into the site. Without that link the site's own checks go red; do not make it by hand.
- Builds initial navigation (`build-nav.py`), metadata (`build-meta.py`), and search index (`build-search.py`).
- Removes seed scaffolding (`pages/`, `tools/new-site.py`).

## 3. Git setup

**Option A** did it. **Option B:** the branches exist, so create none. Work happens on `dev`. Remove the one-line `README.md` of the empty repository (no site of the series carries one, unless the Architect says otherwise), then commit:
```bash
cd <factory root>/courses/<repo>
git rm -q README.md
git add -A && git commit -m "chore(seed): stamp the site from seed/swa"
```

**Branch Architecture Invariants:**
- `main`: root baseline stamped from the seed.
- `prod`: release branch for GitHub Pages publication. Must branch strictly from `main`, NEVER directly from `dev`. Releases are merged into `prod` using `--no-ff` nodes.
- `dev`: active working branch where AI pilots and engineers build content and run checks.

`.gitignore` keeps the harness's session analytics (`docs/codemie/`) out of `git add -A`: the file name carries a work email slug.

## 4. Immediate Machine Verification

Run the full test suite before touching any file:
```bash
./check.sh
```

The check MUST print `ЗЕЛЁНОЕ` with every line of its summary saying `ДА` on the freshly stamped site. How many lines the summary holds is printed by the check itself; a number written here rots when the engine grows a check.

## 5. Remote and GitHub Pages Connection (Architect/Conductor Action)

Only the Conductor pushes. If a remote repository on GitHub (`y-kolyada/<repo>`) is created:
```bash
git remote add origin git@github.com:y-kolyada/<repo>.git
git push -u origin main
git push -u origin prod
git push -u origin dev
gh repo edit y-kolyada/<repo> --default-branch main
gh api --method POST repos/y-kolyada/<repo>/pages -f source[branch]=prod -f source[path]=/
```

## 6. Handing Off to Batch 1 and Stop Crane

Once the scaffold is green and branches are established:
1. Activate the `step` skill to formulate `lessons/step-1.md`.
2. Follow Rule §5.15 (Batched shift delivery model) - target **Batch 1 (Setup, Landing index.html, Topics 01-05)**.
3. Formulate the goal, strictly three machine-checkable predicates, and explicit boundaries.
4. Stop and await the Conductor's explicit approval word ("делаем") before authoring any content.
