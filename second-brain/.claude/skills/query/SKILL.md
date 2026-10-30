---
name: query
description: Answer a question from the wiki only, citing pages, and optionally save the answer as a new page. Use when the user asks what they know, have collected, or have read about something.
---

# Query

1. Start from `wiki/index.md` to find candidate pages, then read them and follow their links.
2. Answer using only `wiki/`. After each point, name the page it came from as `[[page]]`.
3. End with a "Not covered" line listing any part of the question the wiki doesn't answer.
   Never fill those gaps from general knowledge.
4. If the user says to keep the answer: save it as `wiki/answer-<short-topic>.md` with the
   question at the top, link every page it used, and add it to `wiki/index.md` under
   "Saved answers".
