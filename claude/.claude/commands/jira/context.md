---
description: Get full context from a Jira issue including related tickets
---

Load full context for Jira issue **$ARGUMENTS** using the Jira skill.

## Gather

1. Main issue: key, summary, type, status, priority, assignee, description
2. Linked issues (issuelinks field): key, summary, status, link type
3. If Epic: child issues via JQL `"Epic Link" = $ARGUMENTS OR parent = $ARGUMENTS`
4. If child: parent issue
5. Subtasks if any
6. Last 3 comments

## Then

Proceed with the user's original request using this context.
