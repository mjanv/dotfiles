# Future Ideas for Obsidian Plugin

## Knowledge Base Enhancement

### `/obsidian:links` - Vault health checker
- Find broken wikilinks
- Identify orphaned notes (no incoming links)
- Suggest connections between related notes
- Show most/least connected notes

### `/obsidian:graph [topic]` - Knowledge graph
- Generate text-based map of note connections
- Show how topics relate to each other
- Identify knowledge clusters
- Find bridge notes connecting different areas

### `/obsidian:similar <note>` - Find related notes
- Use tags, links, and content similarity
- Suggest notes to link together
- Discover forgotten related content

### `/obsidian:random` - Serendipity command
- Show random note from vault
- Great for rediscovering old notes
- Optional: filter by tag or date range

### `/obsidian:stats` - Vault statistics
- Most referenced notes
- Tag usage distribution
- Note creation trends
- Writing patterns (when you write most)
- Vault growth over time

## Productivity & Habits

### `/obsidian:habit [habit-name]` - Habit tracking
- Track daily habits in daily notes
- Show streak information
- Generate habit consistency reports
- Visual patterns in weekly/monthly reviews

### `/obsidian:goals` - Goal management
- Track quarterly/yearly goals
- Show progress toward goals
- Link goals to daily work
- Generate goal progress reports

### `/obsidian:time [duration] [task]` - Time tracking
- Log time spent on tasks
- Aggregate time by project/category
- Show time allocation in reviews
- Pomodoro timer integration

### `/obsidian:standup` - Daily standup generator
- What I did yesterday (from yesterday's note)
- What I'll do today (from today's tasks)
- Blockers (from notes tagged #blocker)
- Formatted for posting in team chat

## Development Workflow

### `/obsidian:til [learning]` - Structured TIL
- Create formatted Today I Learned entry
- Auto-tag by technology/domain
- Link to related concepts
- Aggregate TILs in learning reviews

### `/obsidian:deploy [environment]` - Deployment log
- Log deployments to production/staging
- Track what was deployed, when, by whom
- Link to commits or PRs
- Useful for incident investigation

### `/obsidian:incident [description]` - Incident tracker
- Create incident post-mortem template
- Timeline tracking
- Root cause analysis structure
- Action items and learnings

### `/obsidian:review-checklist` - Code review helper
- Generate code review checklist
- Track review points
- Link to PR/commit
- Document review feedback

### `/obsidian:performance [metric]` - Performance notes
- Log performance metrics
- Track optimization work
- Before/after comparisons
- Link to benchmarking data

### `/obsidian:debt [description]` - Technical debt tracking
- Create technical debt entries
- Priority and effort estimation
- Link to code locations
- Track debt paydown

## Communication & Meetings

### `/obsidian:meeting [title]` - Meeting notes
- Structured meeting template
- Attendees, agenda, decisions, action items
- Link to related projects
- Auto-create follow-up tasks

### `/obsidian:oneonone [person]` - 1-on-1 tracker
- Track 1-on-1 meetings over time
- Action items from previous meetings
- Topics to discuss
- Relationship building notes

### `/obsidian:rfc [topic]` - Request for Comments
- Create RFC template
- Problem, proposal, alternatives
- Decision process tracking
- Link to related ADRs

## Templates & Structure

### `/obsidian:template [type]` - Create from template
- Apply templates for common note types
- Meeting, project, book, course, person, etc.
- Customizable template library

### `/obsidian:project [name]` - Initialize project
- Create standard project structure
- README, decisions, retrospective folders
- Link to index
- Set up tracking

## Automation & Integration

### `/obsidian:bookmark [url]` - Save bookmark
- Capture URL with description
- Fetch page title/summary
- Tag and categorize
- Link to projects if relevant

### `/obsidian:reading [book/article]` - Reading tracker
- Track books/articles in progress
- Reading notes
- Key takeaways
- Status: reading/completed/abandoned

## Hooks

### `pre-push` - Work session reminder
- Prompt to log work session before pushing

### `post-merge` - Merge logging
- Log merges to daily note

### `daily-reminder` - Daily review reminder
- Cron job to remind about daily review

### `weekly-reminder` - Weekly review reminder
- Remind to run weekly review

## Maintenance & Health

### `/obsidian:archive [project]` - Archive project
- Move completed project to archive
- Update links
- Create final retrospective
- Mark as complete in index

### `/obsidian:cleanup` - Vault maintenance
- Find notes without tags
- Identify very short notes
- Suggest notes to merge
- Find duplicate content

### `/obsidian:age` - Find stale content
- Notes not modified in X months
- Uncompleted tasks over X days old
- Projects without recent activity

## Priority Recommendations

High value for Elixir/Phoenix TDD workflow:

1. **`/obsidian:til`** - Structured learning capture (high value for daily learning)
2. **`/obsidian:standup`** - Generate team updates (saves time daily)
3. **`/obsidian:links`** - Vault health (maintain knowledge base quality)
4. **`/obsidian:deploy`** - Track production changes (important for senior dev)
5. **`/obsidian:incident`** - Post-mortem structure (critical for production issues)
6. **`/obsidian:stats`** - Understand your productivity patterns
7. **`/obsidian:habit`** - Track TDD practice, exercise, etc.
8. **`/obsidian:random`** - Rediscover old learnings
9. **`/obsidian:meeting`** - Structured meeting capture
10. **`/obsidian:review-checklist`** - Standardize code reviews
