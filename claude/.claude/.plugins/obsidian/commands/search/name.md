---
description: Search and load Obsidian notes by name
---

## Search Results

Notes matching "$ARGUMENTS":

$```find ~/NOTES/ -type f -name "*$ARGUMENTS*" -name "*.md" 2>/dev/null | head -50```

## Your Task

Read the content of the notes found above. If no notes were found, inform the user that no notes match their search term "$ARGUMENTS".
