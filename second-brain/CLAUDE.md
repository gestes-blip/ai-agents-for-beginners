# CLAUDE.md

This folder is my second brain: an Obsidian vault that Claude Code maintains as a linked wiki
(the LLM Wiki pattern). Read this file first in every session.

<!-- SETUP: the four sections below marked TODO are empty on purpose. On first run, paste the
interview prompt from README.md and let Claude fill them in from your answers. -->

## About me

TODO: who I am and what I do.

## Current projects

TODO: what I'm building this year, one line each.

## How to talk to me

TODO: tone, length, format preferences.

## What this brain should help me produce

TODO: the outputs I want (posts, decisions, research briefs, ...).

## How this folder works

- `raw/` holds sources: articles, transcripts, notes. **Read it, never edit, move, rename or delete
  anything in it.** This is enforced by `.claude/settings.json` and a hook, not only by this rule.
- `wiki/` holds pages you write and keep linked. I read it, you write it.
- `output/` holds finished work built from `wiki/`, not from general knowledge.
- `wiki/index.md` lists every wiki page with a one-line description.
- `wiki/log.md` records every ingest: date, source file in `raw/`, pages created or changed.
  A file in `raw/` is "not yet ingested" when it does not appear in `wiki/log.md`.

## Wiki rules

- One idea per page. File names are lowercase-with-dashes, e.g. `wiki/spaced-repetition.md`.
- Page types: `source-` summaries (one per raw file), concept pages, person pages, project pages.
- Link with `[[double brackets]]` using the page name without `.md`.
- Every claim on a concept page cites the source summary it came from, e.g. `(from [[source-karpathy-llm-wiki]])`.
- Update an existing page before creating a near-duplicate. If two sources disagree, keep both
  claims and mark the conflict with `> [!warning] Conflict`.
- Every new page goes into `wiki/index.md` in the same session.

## Answering questions

- Answer from `wiki/` only, and name the pages you used. If the wiki doesn't cover part of the
  question, say so instead of filling the gap from general knowledge.
- When I say an answer is good, save it as a wiki page, link the pages it used and add it to the index.

## Procedures

Multi-step workflows live in `.claude/skills/`, not here: `ingest`, `query`, `weekly-review`,
`new-project`. Project rooms under `wiki/<project>/` have their own `CLAUDE.md`.
