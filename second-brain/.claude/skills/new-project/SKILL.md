---
name: new-project
description: Create a project room under wiki/<project>/ with its own CLAUDE.md. Use when the user wants to focus on one project or says "create a project for ...".
---

# New project room

1. Ask the user, one question at a time, only for what you don't know yet:
   what the project is, its one goal, how you should help, and which existing wiki pages matter most.
2. Create `wiki/<project-name>/CLAUDE.md` (lowercase-with-dashes name) with sections:
   What this project is, The one goal, How to help, Key pages (as `[[links]]`). Under 60 lines.
3. Create `wiki/<project-name>/<project-name>.md` as the project's hub page linking the key pages.
4. Add the hub page to `wiki/index.md` under "Projects" and to "Current projects" in the root
   `CLAUDE.md` only if the user agrees.
