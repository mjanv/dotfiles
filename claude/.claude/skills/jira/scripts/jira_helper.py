#!/usr/bin/env python3
"""
Jira Helper
High-level operations for managing Jira tickets.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

from jira_client import JiraClient, JiraConfig


@dataclass
class Ticket:
    """Structured ticket data."""
    key: str
    summary: str
    status: str
    priority: str
    issue_type: str = ""
    assignee: Optional[str] = None
    reporter: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None
    resolution: Optional[str] = None
    fix_versions: List[str] = field(default_factory=list)
    components: List[str] = field(default_factory=list)
    labels: List[str] = field(default_factory=list)
    description: str = ""
    comments_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "key": self.key,
            "summary": self.summary,
            "status": self.status,
            "priority": self.priority,
            "issue_type": self.issue_type,
            "assignee": self.assignee,
            "reporter": self.reporter,
            "created": self.created,
            "updated": self.updated,
            "resolution": self.resolution,
            "fix_versions": self.fix_versions,
            "components": self.components,
            "labels": self.labels,
            "description": self.description,
            "comments_count": self.comments_count
        }


@dataclass
class Metrics:
    """Ticket metrics."""
    total: int = 0
    by_status: Dict[str, int] = field(default_factory=dict)
    by_priority: Dict[str, int] = field(default_factory=dict)
    by_type: Dict[str, int] = field(default_factory=dict)
    avg_age_days: float = 0.0
    oldest_ticket: Optional[str] = None
    newest_ticket: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "total": self.total,
            "by_status": self.by_status,
            "by_priority": self.by_priority,
            "by_type": self.by_type,
            "avg_age_days": self.avg_age_days,
            "oldest_ticket": self.oldest_ticket,
            "newest_ticket": self.newest_ticket
        }


class JiraHelper:
    """
    High-level helper for managing Jira tickets.

    Provides convenience methods for common ticket operations.
    """

    def __init__(self, config: Optional[JiraConfig] = None):
        """Initialize the helper."""
        self.client = JiraClient(config)
        self.connected = False

    def connect(self, token: Optional[str] = None, email: Optional[str] = None) -> bool:
        """
        Connect to Jira.

        Args:
            token: API token (optional, reads from .env if not provided)
            email: User email (optional)

        Returns:
            True if connected successfully
        """
        self.client.authenticate(token, email)
        self.connected = True
        return True

    def _parse_issue(self, issue: Dict[str, Any]) -> Ticket:
        """Parse Jira issue into Ticket."""
        fields = issue.get("fields", {})

        # Extract components
        components = [c.get("name", "") for c in fields.get("components", [])]

        # Extract fix versions
        fix_versions = [v.get("name", "") for v in fields.get("fixVersions", [])]

        # Extract assignee
        assignee = None
        if fields.get("assignee"):
            assignee = fields["assignee"].get("displayName") or fields["assignee"].get("name")

        # Extract reporter
        reporter = None
        if fields.get("reporter"):
            reporter = fields["reporter"].get("displayName") or fields["reporter"].get("name")

        return Ticket(
            key=issue.get("key", ""),
            summary=fields.get("summary", ""),
            status=fields.get("status", {}).get("name", ""),
            priority=fields.get("priority", {}).get("name", ""),
            issue_type=fields.get("issuetype", {}).get("name", ""),
            assignee=assignee,
            reporter=reporter,
            created=fields.get("created"),
            updated=fields.get("updated"),
            resolution=fields.get("resolution", {}).get("name") if fields.get("resolution") else None,
            fix_versions=fix_versions,
            components=components,
            labels=fields.get("labels", []),
            description=fields.get("description", "") or "",
            comments_count=fields.get("comment", {}).get("total", 0) if isinstance(fields.get("comment"), dict) else 0
        )

    def search_tickets(
        self,
        project: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        issue_type: Optional[str] = None,
        assignee: Optional[str] = None,
        labels: Optional[List[str]] = None,
        jql_extra: Optional[str] = None,
        max_results: int = 50
    ) -> List[Ticket]:
        """
        Search for tickets with filters.

        Args:
            project: Project key to filter by
            status: Status to filter by
            priority: Priority to filter by
            issue_type: Issue type to filter by
            assignee: Assignee username
            labels: Labels to filter by
            jql_extra: Additional JQL conditions
            max_results: Maximum results to return

        Returns:
            List of Ticket objects
        """
        jql_parts = []

        if project:
            jql_parts.append(f'project = {project}')

        if status:
            jql_parts.append(f'status = "{status}"')

        if priority:
            jql_parts.append(f'priority = {priority}')

        if issue_type:
            jql_parts.append(f'issuetype = "{issue_type}"')

        if assignee:
            if assignee.lower() == "currentuser":
                jql_parts.append('assignee = currentUser()')
            else:
                jql_parts.append(f'assignee = "{assignee}"')

        if labels:
            for label in labels:
                jql_parts.append(f'labels = "{label}"')

        if jql_extra:
            jql_parts.append(jql_extra)

        jql = " AND ".join(jql_parts) if jql_parts else "ORDER BY created DESC"
        if jql_parts:
            jql += " ORDER BY created DESC"

        results = self.client.search_issues(
            jql,
            fields=["summary", "status", "priority", "issuetype", "assignee", "reporter",
                    "created", "updated", "resolution", "fixVersions",
                    "components", "labels", "description", "comment"],
            max_results=max_results
        )

        return [self._parse_issue(issue) for issue in results.get("issues", [])]

    def get_open_tickets(
        self,
        project: Optional[str] = None,
        min_age_days: Optional[int] = None
    ) -> List[Ticket]:
        """
        Get open tickets.

        Args:
            project: Project key to filter by
            min_age_days: Minimum age in days

        Returns:
            List of open Ticket objects
        """
        jql_parts = [
            'status NOT IN (Resolved, Closed, Done, "Won\'t Fix", "Won\'t Do")'
        ]

        if project:
            jql_parts.append(f'project = {project}')

        if min_age_days:
            jql_parts.append(f'created <= -{min_age_days}d')

        jql = " AND ".join(jql_parts) + " ORDER BY priority DESC, created ASC"

        results = self.client.search_issues(
            jql,
            fields=["summary", "status", "priority", "issuetype", "assignee", "reporter",
                    "created", "updated", "resolution", "fixVersions",
                    "components", "labels", "description"],
            max_results=100
        )

        return [self._parse_issue(issue) for issue in results.get("issues", [])]

    def get_ticket(self, ticket_key: str) -> Ticket:
        """
        Get full ticket details.

        Args:
            ticket_key: Jira issue key (e.g., "PROJ-123")

        Returns:
            Ticket with full details
        """
        issue = self.client.get_issue(ticket_key, expand=["changelog"])
        return self._parse_issue(issue)

    def create_ticket(
        self,
        project: str,
        summary: str,
        description: str = "",
        issue_type: str = "Task",
        priority: str = "Medium",
        components: Optional[List[str]] = None,
        labels: Optional[List[str]] = None,
        assignee: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new ticket.

        Args:
            project: Project key
            summary: Issue summary/title
            description: Full description
            issue_type: Issue type name (Task, Bug, Story, etc.)
            priority: Priority name
            components: List of component names
            labels: List of labels
            assignee: Assignee username

        Returns:
            Created issue info with key and id
        """
        fields = {
            "project": {"key": project},
            "summary": summary,
            "issuetype": {"name": issue_type},
            "priority": {"name": priority},
            "description": description
        }

        if components:
            fields["components"] = [{"name": c} for c in components]

        if labels:
            fields["labels"] = labels

        if assignee:
            fields["assignee"] = {"name": assignee}

        return self.client.create_issue(fields)

    def update_ticket(
        self,
        ticket_key: str,
        fields: Dict[str, Any],
        notify: bool = True
    ) -> None:
        """
        Update ticket fields.

        Args:
            ticket_key: Issue key
            fields: Fields to update
            notify: Whether to notify watchers
        """
        self.client.update_issue(ticket_key, fields, notify_users=notify)

    def transition_ticket(
        self,
        ticket_key: str,
        status: str,
        comment: Optional[str] = None
    ) -> None:
        """
        Transition ticket to new status.

        Args:
            ticket_key: Issue key
            status: Target status name
            comment: Optional comment to add with transition
        """
        self.client.transition_issue(ticket_key, status, comment=comment)

    def add_comment(self, ticket_key: str, comment: str) -> Dict[str, Any]:
        """
        Add comment to ticket.

        Args:
            ticket_key: Issue key
            comment: Comment text

        Returns:
            Created comment info
        """
        return self.client.add_comment(ticket_key, comment)

    def get_comments(self, ticket_key: str) -> List[Dict[str, Any]]:
        """
        Get all comments on a ticket.

        Args:
            ticket_key: Issue key

        Returns:
            List of comments
        """
        result = self.client.get_comments(ticket_key)
        return result.get("comments", [])

    def link_tickets(
        self,
        from_key: str,
        to_key: str,
        link_type: str = "Relates"
    ) -> None:
        """
        Create link between tickets.

        Args:
            from_key: Source issue key
            to_key: Target issue key
            link_type: Link type (Relates, Blocks, Duplicates, etc.)
        """
        self.client.link_issues(from_key, to_key, link_type)

    def get_metrics(self, project: Optional[str] = None) -> Metrics:
        """
        Get ticket metrics.

        Args:
            project: Project key to filter by

        Returns:
            Metrics with statistics
        """
        jql_parts = []
        if project:
            jql_parts.append(f'project = {project}')

        jql = " AND ".join(jql_parts) if jql_parts else ""

        results = self.client.search_issues(
            jql,
            fields=["summary", "status", "priority", "issuetype", "created"],
            max_results=100
        )

        issues = results.get("issues", [])
        metrics = Metrics()
        metrics.total = results.get("total", len(issues))

        if not issues:
            return metrics

        ages = []
        oldest_date = None
        newest_date = None

        for issue in issues:
            fields = issue.get("fields", {})

            # Count by status
            status = fields.get("status", {}).get("name", "Unknown")
            metrics.by_status[status] = metrics.by_status.get(status, 0) + 1

            # Count by priority
            priority = fields.get("priority", {}).get("name", "Unknown")
            metrics.by_priority[priority] = metrics.by_priority.get(priority, 0) + 1

            # Count by type
            issue_type = fields.get("issuetype", {}).get("name", "Unknown")
            metrics.by_type[issue_type] = metrics.by_type.get(issue_type, 0) + 1

            # Calculate age
            created = fields.get("created")
            if created:
                try:
                    # Parse ISO date
                    created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
                    age = (datetime.now(created_dt.tzinfo) - created_dt).days
                    ages.append(age)

                    if oldest_date is None or created_dt < oldest_date:
                        oldest_date = created_dt
                        metrics.oldest_ticket = issue.get("key")

                    if newest_date is None or created_dt > newest_date:
                        newest_date = created_dt
                        metrics.newest_ticket = issue.get("key")
                except (ValueError, TypeError):
                    pass

        if ages:
            metrics.avg_age_days = sum(ages) / len(ages)

        return metrics

    def export_report(
        self,
        project: Optional[str] = None,
        filename: Optional[str] = None,
        output_dir: str = "output"
    ) -> Dict[str, Any]:
        """
        Export tickets report to JSON.

        Args:
            project: Project key to filter by
            filename: Output filename (auto-generated if not provided)
            output_dir: Output directory

        Returns:
            Report data
        """
        tickets = self.search_tickets(project=project, max_results=100)
        metrics = self.get_metrics(project)

        report = {
            "generated_at": datetime.now().isoformat(),
            "project": project or "all",
            "metrics": metrics.to_dict(),
            "tickets": [t.to_dict() for t in tickets]
        }

        # Save to file
        os.makedirs(output_dir, exist_ok=True)

        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            project_suffix = f"_{project}" if project else ""
            filename = f"jira_report{project_suffix}_{timestamp}.json"

        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"Report saved to: {filepath}")
        return report


def main():
    """Example usage."""
    helper = JiraHelper()

    try:
        helper.connect()
        print("Connected to Jira!")

        # Get current user info
        user = helper.client.get_current_user()
        print(f"Logged in as: {user.get('displayName')}")

        # Get metrics
        metrics = helper.get_metrics()
        print(f"\nTicket Metrics:")
        print(f"  Total: {metrics.total}")
        print(f"  By Status: {metrics.by_status}")
        print(f"  By Priority: {metrics.by_priority}")
        print(f"  By Type: {metrics.by_type}")
        print(f"  Avg Age: {metrics.avg_age_days:.1f} days")

        # Search for recent tickets
        print("\nRecent Tickets:")
        tickets = helper.search_tickets(max_results=5)
        for ticket in tickets:
            print(f"  {ticket.key}: {ticket.summary[:50]}... [{ticket.status}]")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
