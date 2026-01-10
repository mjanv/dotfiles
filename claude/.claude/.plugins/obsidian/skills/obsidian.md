---
description: Allow other projects to search, read, and edit notes in Obsidian vaults
---

You have access to an Obsidian knowledge base.

## Vault Location

Main vault: `/home/maxime/NOTES/`

## Configuration

Read `/home/maxime/NOTES/CLAUDE.md` for:
- Vault structure and folder paths
- Daily note format and location
- Conventions (wikilinks, tags, tasks)
- Preferred formatting

## Basic Operations

**Search notes**:
```
Grep: pattern, path: /home/maxime/NOTES/, exclude .obsidian/
```

**Read notes**:
```
Read: /home/maxime/NOTES/path/to/note.md
```

**Edit notes**:
```
Edit: file_path, old_string, new_string
```

**Create notes**:
```
Write: file_path, content (with frontmatter)
```

## Conventions

- Internal links: `[[Note Name]]`
- Tags: `#tag-name`
- Tasks: `- [ ]` or `- [x]`
- Dates: YYYY-MM-DD
- Daily notes: typically `Daily/YYYY-MM-DD.md`

Always read CLAUDE.md first for specific vault configuration.
