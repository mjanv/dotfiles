---
description: Read all notes with a search term to gather context about something
argument-hint: [term]
---

Search the vault to gather comprehensive context about a topic.

Search term: $ARGUMENTS

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for search patterns and prioritization

2. Search vault with Grep:
   - Content search (case-insensitive)
   - Wikilinks: `\[\[.*term.*\]\]`
   - Tags: `#term`
   - Headers: `^#{1,6}.*term`

3. Prioritize: title matches, multiple mentions, recent notes, index/MOC notes

4. Read top 10-15 most relevant notes

5. Synthesize into structured summary:
   - Overview
   - Key information
   - Main findings by topic area
   - Referenced notes list
   - Related topics
   - Timeline (if relevant)
   - Open tasks

Use `[[wikilinks]]` for references. Exclude `.obsidian/` directory.
