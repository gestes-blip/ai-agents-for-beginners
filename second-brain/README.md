# Second Brain (Claude Code + Obsidian)

A ready-made vault for the LLM Wiki pattern: you save sources in `raw/`, Claude Code builds and
maintains a linked wiki in `wiki/`, and finished work goes to `output/`.

```
second-brain/
├── CLAUDE.md                 # rulebook Claude loads every session (fill in "About me" etc.)
├── raw/                      # your sources; read-only for Claude (enforced)
├── wiki/
│   ├── index.md              # every page, one line each
│   └── log.md                # what was ingested when; drives "not yet ingested"
├── output/                   # finished work and review reports
└── .claude/
    ├── settings.json         # permissions: deny edits to raw/, deny rm and git push
    ├── hooks/protect-raw.sh  # PreToolUse hook that blocks writes to raw/
    └── skills/               # ingest, query, weekly-review, new-project
```

`CLAUDE.md` only asks Claude not to touch `raw/`; the deny rule in `settings.json` and the hook
actually stop it. Delete or change them deliberately if you need to.

## Setup (about 15 minutes)

1. **Get the folder onto your computer.** Download this repository's
   `claude/article-requirements-ta1lwo` branch (Code → Download ZIP on GitHub) and copy the
   `second-brain` folder wherever you want your vault, renaming it `brain` if you like.
   Files starting with a dot (`.claude`, `.gitignore`) are hidden on Mac: press Cmd+Shift+. in
   Finder to check they came along.
2. **Install the apps.** Claude Desktop from claude.com/download (Pro or Max plan, use the Code
   tab) and Obsidian from obsidian.md. In Obsidian choose *Open folder as vault* and pick the folder.
3. **Back it up.** Run `git init && git add -A && git commit -m "Empty brain"` in the folder, or
   keep it in a synced folder, so any bad edit is one undo away.
4. **Open it in Claude.** In the Code tab pick the folder as the working folder and trust it.
   On Windows, Claude Code runs hooks through Git Bash, which it already requires.
5. **Fill in CLAUDE.md.** Paste:

   > Interview me one question at a time to fill the TODO sections of CLAUDE.md: who I am and
   > what I do, what I'm building this year, how I want you to talk to me, and what I want this
   > brain to help me produce. Wait for each answer, then replace the TODOs. Keep the file under
   > 200 lines and don't change the other sections.

6. **First ingest.** Save five to ten text or markdown files into `raw/` (nothing confidential:
   everything Claude reads is sent to the model, and usage limits are shared with Claude chat).
   Then type `/ingest` and open Obsidian's graph view.

## Daily use

| You want to | Type |
|---|---|
| File new sources | `/ingest` |
| Ask across everything | `/query what are the best arguments I've collected about X?` |
| Keep a good answer | "Save that answer" (the query skill handles it) |
| Focus on one project | `/new-project youtube-channel` |
| Check wiki health | `/weekly-review` |
| Save a routine as a skill | "Turn this workflow into a skill in .claude/skills/: [steps + example]" |

## Scheduled tasks (autopilot)

In the Code tab: **Scheduled → New task → Set up manually**. Use a **local** task (*Only on this
computer* under Advanced settings, local folder = your vault); cloud tasks can't see your files.

**nightly-brain** (Daily, a time you choose):

> Use the ingest skill on every file in raw/ that is not in wiki/log.md. Never edit raw/. Then
> write output/daily-log.md with three lines: what you added, what you changed, what needs my
> decision.

**weekly-review** (Weekly):

> Use the weekly-review skill. Do not change anything in wiki/.

Click **Run now** once for each and choose "always allow" for the prompts it raises, or the night
run will stall waiting. Local tasks only run while the app is open and the computer is awake:
turn on *Keep computer awake* in Settings → This computer → System for overnight runs.

## Optional: Google Calendar

Create a Google Cloud project, enable the Google Calendar API and create an OAuth client, then:

```bash
export GOOGLE_OAUTH_CLIENT_ID="your-client-id"
export GOOGLE_OAUTH_CLIENT_SECRET="your-client-secret"
claude mcp add google-workspace uvx workspace-mcp --tools calendar
```

Then ask: "Read my calendar for today. For each meeting, add a line to wiki/meetings.md with what
was decided or what I owe someone. Flag any meeting with no clear next step."

## Where this comes from

The structure follows Andrej Karpathy's LLM Wiki pattern as laid out in Ryven's guide
"How to Build a Second Brain With Claude and Obsidian". Prebuilt alternatives mentioned there:
`AgriciDaniel/claude-obsidian` and `eugeniughelbur/obsidian-second-brain`.
