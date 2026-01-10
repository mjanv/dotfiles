# Obsidian Plugin for Claude Code

Claude Code integration with Obsidian for note management, context retrieval, and knowledge base interaction.

**Vault**: `/home/maxime/NOTES/`

## Setup

1. Copy `CLAUDE.md.template` to `/home/maxime/NOTES/CLAUDE.md`
2. Customize the vault configuration in that file
3. All commands and skills will read from it
4. (Optional) Install git hooks for automation

## Skill: `obsidian`

Makes Claude Code aware of your Obsidian vault structure and conventions. Automatically available to all sessions.

## Commands

### Daily & Time-Based

**`/obsidian:session`**
Add a summary of the current Claude Code session to today's daily note.

**`/obsidian:today`**
Generate a prioritized todo list from vault notes (today's daily, yesterday's, project notes).

**`/obsidian:daily`**
Generate end-of-day summary from today's daily note (accomplishments, time spent, carry-over tasks).

**`/obsidian:weekly`**
Create a summary of the current week from daily notes (Monday-Sunday).

**`/obsidian:monthly`**
Generate monthly summary from weekly summaries with themes, trends, and insights.

**`/obsidian:yearly`**
Generate annual review from monthly summaries (year overview, accomplishments, growth, year-over-year).

**`/obsidian:note <content>`**
Quickly add content to today's daily note (tasks, events, ideas, notes).

Examples:
```bash
/obsidian:note task: Review pull request
/obsidian:note 15:00 meeting with design team
/obsidian:note idea: automate deployment
```

### Knowledge & Context

**`/obsidian:context <term>`**
Search the vault and gather comprehensive context about a topic.

**`/obsidian:chat <query>`**
Answer a question using vault knowledge, formatted for sharing with colleagues (Slack/Teams ready).

**`/obsidian:learn`**
Extract all learning points from recent notes (last 30 days), organized by topic.

**`/obsidian:summarize <note>`**
Create concise summary of a long note (TL;DR, key points, actionables).

### Project Management

**`/obsidian:retrospective <project>`**
Create project retrospective from related notes (goals, wins, challenges, learnings).

**`/obsidian:decision <topic>`**
Create Architecture Decision Record (ADR) with standard format.

**`/obsidian:bug <description>`**
Create structured bug note with reproduction steps, investigation, and solution tracking.

## Hooks

### post-commit

Automatically logs git commits to today's daily note.

**Installation**:
```bash
# Option 1: Symlink to specific repo
cd your-repo
ln -s ~/.dotfiles/claude/.claude/.plugins/obsidian/hooks/post-commit .git/hooks/post-commit

# Option 2: Use globally (all repos)
git config --global core.hooksPath ~/.dotfiles/claude/.claude/.plugins/obsidian/hooks
```

**Configuration**:
Set environment variables (optional):
```bash
export OBSIDIAN_VAULT="$HOME/NOTES"
export OBSIDIAN_DAILY="Daily"
```

**Output format**:
```markdown
## Commits
- 14:30 [project-name] `abc123` commit message
```

## Configuration

All configuration is in `/home/maxime/NOTES/CLAUDE.md`:
- Vault structure (daily notes, projects, decisions, bugs, learning, retrospectives)
- Templates (daily note, ADR, bug report)
- Priority rules for `/obsidian:today`
- Summary sections for weekly/monthly
- Search patterns and categorization
- Learning categories
- ADR numbering scheme
ntions

- Wikilinks: `[[Note Name]]`
- Tags: `#tag-name`
- Tasks: `- [ ]` or `- [x]`
- Dates: YYYY-MM-DD
- Time: HH:MM (24-hour)
- Week: YYYY-WXX (ISO)
- ADR: ADR-NNN-title

## Workflows

### Daily Workflow
1. **Morning**: `/obsidian:today` - Review priorities for the day
2. **During day**: `/obsidian:note` - Capture thoughts, tasks, events
3. **Evening**: `/obsidian:daily` - Reflect on accomplishments

### Development Session
1. Code and commit (auto-logged via post-commit hook)
2. `/obsidian:session` - Log session summary
3. `/obsidian:decision` - Document architectural decisions
4. `/obsidian:bug` - Track bugs discovered

### Weekly Review
1. `/obsidian:weekly` - Generate week summary
2. `/obsidian:learn` - Extract learning points
3. `/obsidian:today` - Plan next week's priorities

### Project Completion
1. `/obsidian:retrospective <project>` - Create retrospective
2. `/obsidian:monthly` - Include in monthly summary
3. Archive or mark project as complete

### Yearly Review
1. `/obsidian:yearly` - Generate annual review from monthly summaries
2. Review completed projects and major decisions
3. Identify growth themes and set direction for next year

**Version**: 0.3.0
**Author**: Maxime Janvier
**Updated**: 2026-01-10
