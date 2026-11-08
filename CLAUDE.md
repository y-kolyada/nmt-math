# Claude Code

Read `AGENTS.md`: the rules and the order of work live there.

The engine (`assets/`) and the checks (`tools/`) are shared across the series and are **not edited here**. A defect in them is one line in `lessons/notes-N.md`, fixed once in the seed.

**Three files are the exception and are the site's own** (`AGENTS.md` §1): `tools/check-examples.sh` runs the code the pages show, `tools/check-claims.sh` executes what the pages state, and `tools/claims.tsv` holds those statements. `sync.sh` creates them when they are absent and never overwrites them, so they cannot drift and they are written, measured and fixed here, on the site. This paragraph exists because its absence had a price: this file is the first one a pilot reads, it said «not edited here» without the exception, and `devops-helm` carried 24 synchronous namespace deletions through three shifts that had already measured what they cost.

