# Obsidian Vault Configuration for Claude Code

Place this file at: `/home/maxime/NOTES/CLAUDE.md`

## Vault Structure

- **Vault root**: `/home/maxime/NOTES/`
- **Daily notes**: `Daily/YYYY-MM-DD.md`
- **Weekly summaries**: `Weekly/YYYY-WXX.md`
- **Monthly summaries**: `Monthly/YYYY-MM.md`
- **Yearly reviews**: `Yearly/YYYY.md`
- **Projects**: `Projects/`
- **Decisions (ADRs)**: `Decisions/` or `Projects/<project>/Decisions/`
- **Bugs**: `Bugs/` or `Projects/<project>/Bugs/`
- **Learning**: `Learning/YYYY-MM.md`
- **Retrospectives**: `Retrospectives/` or `Projects/<project>/`
- **Index**: `INDEX.md`

## Daily Note Template

```markdown
---
date: YYYY-MM-DD
tags: [daily]
---

# YYYY-MM-DD

## Tasks
- [ ]

## Events

## Notes

## Ideas
```

## Today Command Configuration

**Files to scan**:
- Daily/{{today}}.md
- Daily/{{yesterday}}.md
- INDEX.md
- Projects/Active/*.md

**Priority order**:
1. Tasks with ⭐ or #urgent
2. Tasks with #today or today's date
3. Tasks from yesterday (carry-over)
4. Other unchecked tasks

**Categories** (tag → category):
- #work → Work
- #dev, #code → Development
- #personal → Personal
- #learning → Learning

**Exclude**: #archive, #cancelled, #someday

## Weekly Command Configuration

**Week**: Monday to Sunday (ISO week format YYYY-WXX)

**Summary sections**:
1. Overview
2. Accomplishments (by category)
3. Project Progress
4. Learning & Growth
5. Challenges & Solutions
6. Next Week Priorities

**Metrics to track**:
- Tasks completed: count `- [x]`
- Time tracked: sum `⏱️ Xh` or `(Xh)`
- Notes created: count new `[[links]]`

**Tone**: Concise, celebrate wins, frame challenges as learning

## Context Command Notes

Search patterns:
- Content: case-insensitive
- Wikilinks: `\[\[.*term.*\]\]`
- Tags: `#term`
- Headers: `^#{1,6}.*term`

Prioritize: title matches, multiple mentions, recent notes

## Chat Command Configuration

**Purpose**: Answer queries with vault knowledge, formatted for colleague sharing

**Search priority**:
1. ADRs and decision records
2. Project documentation
3. Recent learnings and TILs
4. Implementation notes
5. Daily notes with relevant context

**Output format**:
- Direct answer (1-2 sentences)
- Supporting details (bullets)
- Additional context if needed
- Chat-length (3-8 lines max)
- No markdown headers, use **bold** for emphasis
- Professional, colleague-friendly tone

**Length**: Concise, ready to copy-paste to Slack/Teams/Discord

## Session Command Format

```markdown
## Claude Code Session - HH:MM

### Summary
[1-2 sentences]

### Completed
- [tasks]

### Files Modified
- `path` - description

### Next Steps
- [if any]
```

## Note Command Sections

Map content type to section:
- Task → ## Tasks
- Event (with time) → ## Events or timestamped
- Idea → ## Ideas
- General → ## Notes or append to end

## Daily Command Configuration

**Summary format**:
- Quick overview (1-2 sentences)
- Key accomplishments
- Time spent (if tracked)
- Important notes or decisions
- Incomplete tasks for tomorrow

**Placement**: Append to daily note under `## Summary` or output only

Use at end of day for reflection. Compare with morning todos.

## Monthly Command Configuration

**Location**: `Monthly/YYYY-MM.md`

**Structure**:
1. Overview and highlights
2. Major accomplishments by theme
3. Project progress summary
4. Learning themes
5. Challenges and solutions
6. Metrics and trends
7. Month-over-month comparison

## Yearly Command Configuration

**Location**: `Yearly/YYYY.md`

**Structure**:
1. Year Overview (major themes and highlights)
2. Accomplishments (by domain: work, learning, personal, projects)
3. Projects (completed, ongoing, archived)
4. Learning & Growth (skills, courses, insights)
5. Challenges (major obstacles overcome)
6. Decisions (important ADRs and strategic choices)
7. Metrics (annual totals and patterns)
8. Year-over-Year comparison
9. Looking Forward (themes for next year)

**Focus**: Big-picture themes, long-term trends, personal/professional growth, major shifts

## Retrospective Command Configuration

**Location**: `Retrospectives/YYYY-MM-<project>.md` or `Projects/<project>/Retrospective.md`

**Format**:
- Goals vs Outcomes
- What Went Well
- Challenges
- Learnings
- Timeline
- Decisions Made
- Metrics

## Learn Command Configuration

**Time range**: Last 30 days (configurable)

**Search patterns**: "learned", "TIL", "discovered", "realized", `#learning`, `## Learnings`

**Categories**:
- Technical (Elixir, Phoenix, databases)
- Tools & Workflows
- Patterns & Best Practices
- Soft Skills
- Domain Knowledge
- Mistakes & Corrections

## Bug Command Configuration

**Location**: `Bugs/<project>-BUG-YYYY-MM-DD-<title>.md`

**Template includes**:
- Description, Context, Environment
- Steps to Reproduce
- Expected vs Actual Behavior
- Investigation notes
- Solution space
- Status: open/investigating/fixed/closed

**Tags**: #bug, #<project>

## Decision Command Configuration

**Location**: `Decisions/ADR-NNN-<title>.md`

**ADR Format**: Use standard ADR template with Context, Decision, Options, Rationale, Consequences

**Numbering**: Sequential (ADR-001, ADR-002, etc.)

**Status**: proposed/accepted/deprecated/superseded

## Summarize Command Configuration

**Summary format**:
- TL;DR (1-2 sentences)
- Key Points (bullet list)
- Topics covered
- Actionables
- References

**Target length**: 10-20% of original

**Placement**: Add to note or create separate `-Summary.md` file

## Conventions

- Use `[[wikilinks]]` for internal links
- Use `#tags` (no spaces, use hyphens)
- Tasks: `- [ ]` unchecked, `- [x]` checked
- Time: 24-hour format HH:MM
- Dates: YYYY-MM-DD format
