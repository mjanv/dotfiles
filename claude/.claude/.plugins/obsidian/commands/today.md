---
description: Read relevant files to generate today's todo list
---

Generate a prioritized todo list for today from vault notes.

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for configuration:
   - Which files to scan
   - Priority rules
   - Category mappings
   - Filters

2. Find and read relevant files (today's daily, yesterday's, INDEX, project notes)

3. Extract unchecked tasks `- [ ]`

4. Prioritize and categorize based on CLAUDE.md rules

5. Output structured list grouped by category

Show high priority first, include source notes as `([[Note]])`, aggregate time estimates if present.
