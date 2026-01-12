---
name: "jira"
description: "Interact with Jira for ticket management. Use when the user asks about Jira tickets, wants to create/update issues, search with JQL, track workflows, or manage Jira-related tasks."
---

# Jira Skill

You are a specialized assistant for managing tickets in Jira. This skill enables querying, creating, updating, and tracking issues across projects.

## When to Use This Skill

Activate this skill when the user:
- Asks about Jira tickets or issues
- Wants to create a new Jira issue
- Needs to update ticket status or details
- Wants to search for tickets using JQL
- Asks about project workflows or statuses
- Mentions "Jira", "ticket", or "issue"

## Prerequisites

Before using this skill, ensure:
1. The `~/.claude/.env` file exists with `JIRA_API_TOKEN` and `EMAIL`
2. Python 3.x is installed
3. Network access to Jira instance

## Skill Structure

```
.claude/skills/jira/
├── SKILL.md                    # This file
├── requirements.txt            # Python dependencies
└── scripts/
    ├── jira_client.py          # Core Jira REST API client
    └── jira_helper.py          # High-level ticket operations
```

Project root contains:
- `~/.claude/.env` - API credentials (JIRA_API_TOKEN, EMAIL)
- `output/` - Generated reports directory

## Quick Start

### Using JiraHelper (Recommended)

```python
import sys
sys.path.insert(0, '.claude/skills/jira/scripts')

from jira_helper import JiraHelper

helper = JiraHelper()
helper.connect()

# Search for tickets
tickets = helper.search_tickets(project="MYPROJECT", status="Open")

# Get ticket details
ticket = helper.get_ticket("PROJ-123")

# Create a new ticket
ticket = helper.create_ticket(
    project="MYPROJECT",
    summary="Implement new feature",
    description="Detailed description of the feature...",
    issue_type="Story",
    priority="High",
    components=["Backend"],
    labels=["feature", "q1"]
)

# Update ticket status
helper.transition_ticket(ticket_key="PROJ-123", status="In Progress")

# Add a comment
helper.add_comment(ticket_key="PROJ-123", comment="Started working on this")

# Link tickets
helper.link_tickets("PROJ-123", "PROJ-456", link_type="relates to")

# Get ticket metrics
metrics = helper.get_metrics(project="MYPROJECT")
```

### Using JiraClient Directly

```python
import sys
sys.path.insert(0, '.claude/skills/jira/scripts')

from jira_client import JiraClient

client = JiraClient()
client.authenticate()

# Search with JQL
issues = client.search_issues('project = MYPROJECT AND status = Open')

# Get single issue
issue = client.get_issue("PROJ-123")

# Create issue
new_issue = client.create_issue({
    "project": {"key": "MYPROJECT"},
    "summary": "New feature request",
    "issuetype": {"name": "Story"},
    "priority": {"name": "High"},
    "description": "Full description here..."
})

# Update issue
client.update_issue("PROJ-123", {"description": "Updated description"})

# Add comment
client.add_comment("PROJ-123", "Investigation complete")

# Transition issue
client.transition_issue("PROJ-123", "In Progress")

# Get transitions
transitions = client.get_transitions("PROJ-123")
```

## Available Operations

### JiraHelper Methods

| Method | Description |
|--------|-------------|
| `connect()` | Initialize Jira API client with credentials |
| `search_tickets(project, status, ...)` | Search for tickets with filters |
| `get_open_tickets(project, days)` | Get open tickets, optionally filtered by age |
| `get_ticket(ticket_key)` | Get full ticket details |
| `create_ticket(project, summary, ...)` | Create a new ticket |
| `update_ticket(ticket_key, fields)` | Update ticket fields |
| `transition_ticket(ticket_key, status)` | Change ticket status |
| `add_comment(ticket_key, comment)` | Add comment to ticket |
| `link_tickets(from_key, to_key, type)` | Create link between tickets |
| `get_metrics(project)` | Get ticket statistics |
| `export_report(project, format)` | Export tickets report |

### JiraClient Methods

| Method | Description |
|--------|-------------|
| `authenticate()` | Load credentials and verify API access |
| `search_issues(jql, fields, max_results)` | Search issues with JQL |
| `get_issue(issue_key, fields)` | Get single issue details |
| `create_issue(fields)` | Create new issue |
| `update_issue(issue_key, fields)` | Update issue fields |
| `delete_issue(issue_key)` | Delete issue (use with caution) |
| `add_comment(issue_key, body)` | Add comment |
| `get_comments(issue_key)` | Get all comments |
| `get_transitions(issue_key)` | Get available transitions |
| `transition_issue(issue_key, transition)` | Perform transition |
| `link_issues(inward_key, outward_key, type)` | Link two issues |
| `get_project(project_key)` | Get project details |
| `get_issue_types(project_key)` | Get available issue types |

## JQL Query Examples

```python
# All tickets in a project
'project = MYPROJECT'

# Open tickets
'project = MYPROJECT AND status in (Open, "In Progress", "To Do")'

# High priority tickets
'project = MYPROJECT AND priority in (High, Critical)'

# Tickets created in last 30 days
'project = MYPROJECT AND created >= -30d'

# Tickets assigned to current user
'project = MYPROJECT AND assignee = currentUser()'

# Tickets with specific label
'project = MYPROJECT AND labels = backend'

# Recently updated tickets
'project = MYPROJECT AND updated >= -7d ORDER BY updated DESC'

# Unassigned tickets
'project = MYPROJECT AND assignee is EMPTY'

# Tickets by issue type
'project = MYPROJECT AND issuetype = Bug'

# Tickets in specific sprint
'project = MYPROJECT AND sprint = "Sprint 5"'

# Overdue tickets
'project = MYPROJECT AND duedate < now() AND status != Done'
```

## Common Tasks

### 1. Find All Open Tickets

```python
open_tickets = helper.get_open_tickets(project="MYPROJECT")
for ticket in open_tickets:
    print(f"{ticket['key']}: {ticket['summary']} - {ticket['status']}")
```

### 2. Create a Bug Ticket

```python
ticket = helper.create_ticket(
    project="MYPROJECT",
    summary="Login button not working on mobile",
    description="""
    ## Steps to Reproduce
    1. Open app on mobile device
    2. Navigate to login page
    3. Tap login button

    ## Expected Behavior
    User should be logged in

    ## Actual Behavior
    Nothing happens when tapping the button
    """,
    issue_type="Bug",
    priority="High",
    components=["Mobile", "Authentication"],
    labels=["bug", "mobile", "urgent"]
)
print(f"Created: {ticket['key']}")
```

### 3. Track Progress

```python
# Get ticket
ticket = helper.get_ticket("PROJ-123")
print(f"Status: {ticket['status']}")
print(f"Assignee: {ticket['assignee']}")

# Update with fix version
helper.update_ticket("PROJ-123", {
    "fixVersions": [{"name": "2.0.1"}]
})

# Transition to done
helper.transition_ticket("PROJ-123", "Done")
helper.add_comment("PROJ-123", "Fixed in release 2.0.1")
```

### 4. Generate Metrics Report

```python
metrics = helper.get_metrics(project="MYPROJECT")
print(f"Total Tickets: {metrics['total']}")
print(f"Open: {metrics['by_status'].get('Open', 0)}")
print(f"High Priority: {metrics['by_priority'].get('High', 0)}")
print(f"Average Age: {metrics['avg_age_days']:.1f} days")
```

### 5. Link Related Tickets

```python
# Link duplicate tickets
helper.link_tickets("PROJ-123", "PROJ-456", link_type="duplicates")

# Link related issues
helper.link_tickets("PROJ-123", "PROJ-789", link_type="relates to")

# Link blocker
helper.link_tickets("PROJ-123", "PROJ-100", link_type="blocks")
```

## Error Handling

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API token | Check JIRA_API_TOKEN in .env |
| 403 Forbidden | No project access | Request project permissions |
| 404 Not Found | Issue doesn't exist | Verify issue key |
| 400 Bad Request | Invalid field value | Check field names and values |

## Running Scripts

```bash
# Run the helper example
python .claude/skills/jira/scripts/jira_helper.py

# Run client directly
python .claude/skills/jira/scripts/jira_client.py --search "feature"
```

## Configuration

The client reads settings from environment:

- `JIRA_API_TOKEN` - API token (required)
- `EMAIL` - User email for Basic auth (required for Atlassian Cloud)
- `JIRA_BASE_URL` - Jira instance URL (default: https://hpe.atlassian.net)

## API Limits

- Maximum 100 results per search (paginate for more)
- Rate limits apply per Jira instance configuration
- Bulk operations should be batched
