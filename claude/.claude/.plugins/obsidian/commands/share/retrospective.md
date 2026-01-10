---
description: Create project retrospective from related notes
argument-hint: [project]
---

Generate a project retrospective by analyzing all related notes.

Project name: $ARGUMENTS

## Steps

1. Read `/home/maxime/NOTES/CLAUDE.md` for:
   - Projects location
   - Retrospective template structure

3. Search for all notes related to project:
   - Grep for project name and `[[Project Name]]` links
   - Check for `#project-name` tags
   - Find project folder in Projects/

4. Read relevant notes (project notes, daily notes mentioning project, decisions)

5. Extract and categorize:
   - **Goals**: What we set out to achieve
   - **Outcomes**: What was actually accomplished
   - **Went Well**: Successes and wins
   - **Challenges**: Problems encountered
   - **Learnings**: Key takeaways
   - **Timeline**: Major milestones
   - **Decisions**: Architecture/technical decisions made
   - **Metrics**: Time spent, tasks completed, if tracked

6. Generate structured retrospective document

7. Offer to save to `Projects/<project-name>/Retrospective.md` or `Retrospectives/YYYY-MM-<project>.md`

Use standard retrospective format. Link all referenced notes. Include both technical and process insights.
