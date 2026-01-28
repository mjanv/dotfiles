---
description: Debug and fix a Jira bug ticket
argument-hint: [jira-ticket]
---

# Jira Bug Fix Workflow

You are working on fixing a bug ticket: **$ARGUMENTS**

Follow this structured workflow to investigate, analyze, and fix the bug:

## Phase 1: Ticket Analysis

1. **Create markdown file** with name pattern `[TICKET_KEY]-analysis.md` in the output directory
2. **Extract ticket information** using the jira skill:
   - Get full ticket details: key, summary, description, status, priority, assignee
   - Get ticket type, issue links, comments
   - Get any attached files, logs, or reproduction steps
3. **Summarize** all information in the markdown file in a clear format:
   ```markdown
   # [TICKET_KEY] - [Summary]

   ## Ticket details
   - Status: [status]
   - Priority: [priority]
   - Type: [type]
   - Assignee: [assignee]

   ### Description
   [Full description with reproducible steps]

   ### Behavior
   [What should happen]
   [What actually happens]

   ### Comments
   [Recent comments from team]
   ```

## Phase 2: Root Cause Analysis

1. **Analyze the codebase** to understand the bug:
   - Identify the affected components/modules
   - Trace the code path that causes the issue
   - Look for similar issues or related code
   - Identify edge cases or error handling gaps
2. **Document findings** in the markdown file under a new section:
   ```markdown
   ## Root cause analysis

   [Files affected]
   [Root cause explanation]
   ```

## Phase 3: Solution Design & Approval

1. **Design possible fixes** and document them in a `## Fixes` section
2. **Ask for approval** by presenting the root cause and possible fixes clearly

## Phase 4: Test-Driven Implementation

Once approved, implement using TDD approach:

1. **Create unit tests** that reproduce the bug and validate the expected fix behavior. Verify the created tests fail.
2. **Implement the fix**: Modify the source code to make new tests pass. Keep changes minimal and focused. Don't refactor unrelated code. Check the existing test suite run without regressions.

## Phase 5: Documentation

1. **Write implementation summary** in the markdown file in a `## Implementation summary` section
2. **Create jira comment** in the markdown file in a `## Jira comment` section

## Important Notes

- **Stay focused**: Only fix the specific bug, don't refactor unrelated code
- **Test-driven**: Always write tests that fail first, then implement
- **Document reasoning**: Explain why changes are made, not just what changed
- **Ask for approval**: Get explicit user approval before moving between phases
- **No assumptions**: If context is unclear, ask the user for clarification