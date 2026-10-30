---
name: ingest
description: Ingest new sources from raw/ into the wiki. Use when the user says "ingest", adds a file to raw/, or a scheduled run asks to file new material.
---

# Ingest

1. List files in `raw/` and compare against `wiki/log.md`. Every raw file not in the log is new.
   If the user named a specific file, ingest only that one. If nothing is new, say so and stop.
2. For each new file, in order:
   1. Read it fully. Never edit, move, rename or delete it.
   2. Write `wiki/source-<short-name>.md`: title, author and date if known, a link back to the raw
      file (`raw/<file>`), a one-page summary, and the key claims as bullets.
   3. For every concept, person and project the source touches: update the existing page if one
      exists (check `wiki/index.md` first), otherwise create it. Each added claim cites
      `[[source-<short-name>]]`. If it contradicts an existing claim, keep both and add a
      `> [!warning] Conflict` callout.
   4. Link everything with `[[double brackets]]`, both from the summary to the pages and back.
   5. Add every new page to `wiki/index.md` under the right heading, one line each.
   6. Append a row to `wiki/log.md`: date, raw file, pages created, pages updated.
3. Report what you created and changed, grouped by source.

Keep one idea per page. Prefer updating a page over creating a near-duplicate.
