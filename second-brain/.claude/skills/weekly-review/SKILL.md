---
name: weekly-review
description: Audit the wiki for contradictions, orphan pages, missing pages and unsourced claims, without changing anything. Use for the weekly upkeep run or when the user asks to review or lint the wiki.
---

# Weekly review

Read all of `wiki/`. Do not change any file. Report, each with a suggested fix:

1. **Contradictions**: pages that disagree with each other, including open `Conflict` callouts.
2. **Orphans**: pages with no incoming links, and pages missing from `wiki/index.md`.
3. **Missing pages**: ideas, people or projects mentioned on several pages that have no page.
4. **Unsourced claims**: claims that don't cite a `source-` page, or cite one whose raw file is gone.
5. **Merge candidates**: near-duplicate pages.
6. **Not ingested**: files in `raw/` missing from `wiki/log.md`.

Write the report to `output/weekly-review-<YYYY-MM-DD>.md` and summarize it in three lines.
