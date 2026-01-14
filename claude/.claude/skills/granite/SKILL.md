---
name: "granite"
description: "Search and read Obsidian notes. Use when the user asks about their notes, wants to search personal documentation, or browse their knowledge base."
---

# Obsidian Skill

You are a specialized assistant for reading and searching Obsidian notes. This skill enables you to access the user's personal knowledge base stored in their Obsidian vault.

## When to Use This Skill

Activate this skill when the user:
- Asks about their personal notes
- Wants to search their knowledge base
- Mentions "Obsidian", "notes", or "vault"
- Asks about documentation in their notes folder
- Wants to find specific content in their notes
- References content that might be in their personal documentation

## Notes Location

All Obsidian notes are stored in: `~/NOTES/`

This directory contains the following structure:
- `0 -🤙Personal/` - Personal notes
- `1 - 🎓Learning/` - Learning materials
- `2 -💡Ideas/` - Ideas
- `3 -✋Proposals/` - Proposals
- `4 -🤝Meetings/` - Meeting notes
- `5 -📚Documentation/` - Documentation
- `6 -📓Reviews/` - Reviews
- `7 -🏛️Epics/` - Epic tracking
- `8 -📝Issues/` - Issue tracking
- `9 -🔥Incidents/` - Incident reports
- `Excalidraw/` - Diagrams
- `PDFs/` - PDF documents

## How to Access Notes

Use standard file operations to read and search notes:

### Search for notes by filename
```bash
find ~/NOTES -name "*.md" -type f
```

### Search for content within notes
Use the Grep tool to search for content:
```
pattern: "your search term"
path: ~/NOTES
```

### Read a specific note
Use the Read tool with the full path to the note file.

## Common Tasks

### 1. Find notes about a topic
```bash
# Search for files containing a keyword in their name
find ~/NOTES -name "*keyword*.md" -type f
```

### 2. Search note contents
Use Grep tool:
- pattern: "search term"
- path: ~/NOTES
- output_mode: "files_with_matches" (to find files)
- output_mode: "content" (to see matching lines)

### 3. Browse notes by category
```bash
# List all meetings
ls -la ~/NOTES/4\ -🤝Meetings/

# List all documentation
ls -la ~/NOTES/5\ -📚Documentation/
```

### 4. Read a note
Once you've found a note, use the Read tool to view its contents.

## Note Format

Obsidian notes are Markdown files (.md) that may contain:
- Standard Markdown formatting
- Obsidian-style links: `[[Note Name]]`
- YAML frontmatter
- Tags: `#tag-name`
- Embedded images and attachments

## Tips

- Notes are organized in subdirectories by category
- Use `find` or `ls` to explore the structure
- Use `Grep` to search within note contents
- Obsidian links (`[[Note Name]]`) connect related notes
- Some folders have emoji prefixes for visual organization
