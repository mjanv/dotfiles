---
description: Add something to the current daily note
argument-hint: [content]
---

Quickly add content to today's daily note.

Content to add: $ARGUMENTS

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for:
   - Daily note location and template
   - Section mappings (content type → section)

2. Find today's daily note (or create from template in CLAUDE.md)

3. Read current content to understand structure

4. Determine content type:
   - Task: `- [ ]` → ## Tasks
   - Event (with time): `## HH:MM` → ## Events
   - Idea: → ## Ideas
   - Note/thought: → ## Notes or append

5. Format and place in appropriate section

6. Add with Edit tool, preserve existing formatting

Use `[[wikilinks]]` for references. Add timestamp if appending. Match existing style.
