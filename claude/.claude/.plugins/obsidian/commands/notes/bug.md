---
description: Create structured bug note and link to relevant project
argument-hint: [description]
---

Create a structured bug report note in the vault.

Bug description: $ARGUMENTS

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for:
   - Bug note template
   - Bugs folder location
   - Project linking conventions

2. Get additional details from conversation if needed (project, steps to reproduce, expected vs actual behavior)

3. Generate unique bug identifier (e.g., `BUG-YYYY-MM-DD-<short-title>`)

4. Create structured bug note:
   ```markdown
   ---
   type: bug
   status: open
   project: [[Project Name]]
   created: YYYY-MM-DD
   tags: [bug, <project-tag>]
   ---

   # Bug: <Description>

   ## Description
   <User input>

   ## Context
   - Project: [[Project Name]]
   - Discovered: YYYY-MM-DD
   - Environment: <if provided>

   ## Steps to Reproduce
   1. <if provided>

   ## Expected Behavior
   <if provided>

   ## Actual Behavior
   <if provided>

   ## Investigation
   <Space for notes>

   ## Solution
   <Space for resolution>

   ## Related
   - Links to code, commits, or other notes
   ```

5. Save to configured bugs location (e.g., `Bugs/`, `Projects/<project>/Bugs/`)

6. Add reference to today's daily note

Link to relevant project note. Add appropriate tags. Use status: open/investigating/fixed/closed.
