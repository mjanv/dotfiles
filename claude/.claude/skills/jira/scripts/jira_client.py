#!/usr/bin/env python3
"""
Jira REST API Client
Core client for interacting with Jira REST API.
"""

import json
import os
import urllib.request
import urllib.error
import urllib.parse
import ssl
import base64
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class JiraConfig:
    """Jira API configuration."""
    base_url: str = "https://hpe.atlassian.net"
    api_path: str = "/rest/api/3"
    timeout: int = 30
    verify_ssl: bool = True  # Atlassian Cloud uses valid SSL


class JiraClient:
    """
    Jira REST API client for ticket management.

    Supports both Personal Access Token (PAT) and Basic Auth.
    """

    def __init__(self, config: Optional[JiraConfig] = None):
        """Initialize the Jira client."""
        self.config = config or JiraConfig()
        self.token: Optional[str] = None
        self.email: Optional[str] = None
        self.auth_header: Optional[str] = None

        # SSL context for self-signed certificates
        self.ssl_context = ssl.create_default_context()
        if not self.config.verify_ssl:
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE

    @property
    def api_url(self) -> str:
        """Get full API URL."""
        return f"{self.config.base_url}{self.config.api_path}"

    def load_credentials(self, env_file: str = os.path.expanduser("~/.claude/.env")) -> Dict[str, str]:
        """Load credentials from .env file."""
        credentials = {}

        if os.path.exists(env_file):
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        credentials[key.strip()] = value.strip()

        return credentials

    def authenticate(self, token: Optional[str] = None, email: Optional[str] = None) -> bool:
        """
        Authenticate with Jira.

        Args:
            token: API token (PAT or API key)
            email: User email (for Basic Auth)

        Returns:
            True if authentication successful
        """
        if not token:
            creds = self.load_credentials()
            token = creds.get('JIRA_API_TOKEN')
            email = creds.get('EMAIL') or creds.get('JIRA_USER_EMAIL')

            if not token:
                raise ValueError("JIRA_API_TOKEN not found in .env file")

        self.token = token
        self.email = email

        # Determine auth type
        if email:
            # Basic Auth: email:token
            auth_string = f"{email}:{token}"
            encoded = base64.b64encode(auth_string.encode()).decode()
            self.auth_header = f"Basic {encoded}"
        else:
            # Bearer token (PAT)
            self.auth_header = f"Bearer {token}"

        # Verify authentication
        try:
            self._request("GET", "/myself")
            return True
        except Exception as e:
            self.auth_header = None
            raise ConnectionError(f"Authentication failed: {e}")

    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Optional[Dict]:
        """
        Make HTTP request to Jira API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (e.g., "/issue/SEC-123")
            data: Request body for POST/PUT
            params: Query parameters

        Returns:
            JSON response or None
        """
        if not self.auth_header:
            raise ConnectionError("Not authenticated. Call authenticate() first.")

        url = f"{self.api_url}{endpoint}"

        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"

        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        body = None
        if data:
            body = json.dumps(data).encode('utf-8')

        req = urllib.request.Request(url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(
                req,
                timeout=self.config.timeout,
                context=self.ssl_context
            ) as response:
                if response.status == 204:  # No content
                    return None
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else ""
            raise Exception(f"HTTP {e.code}: {e.reason} - {error_body}")
        except urllib.error.URLError as e:
            raise Exception(f"Connection error: {e.reason}")

    # Issue Operations

    def search_issues(
        self,
        jql: str,
        fields: Optional[List[str]] = None,
        start_at: int = 0,
        max_results: int = 50
    ) -> Dict[str, Any]:
        """
        Search issues using JQL.

        Args:
            jql: JQL query string
            fields: List of fields to return
            start_at: Starting index for pagination
            max_results: Maximum results to return (max 100)

        Returns:
            Search results with issues and pagination info
        """
        # API v3 uses /search/jql endpoint with GET
        params = {
            "jql": jql,
            "startAt": start_at,
            "maxResults": min(max_results, 100)
        }

        if fields:
            params["fields"] = ",".join(fields)

        return self._request("GET", "/search/jql", params=params)

    def get_issue(
        self,
        issue_key: str,
        fields: Optional[List[str]] = None,
        expand: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Get single issue by key.

        Args:
            issue_key: Issue key (e.g., "SEC-123")
            fields: Specific fields to return
            expand: Fields to expand (e.g., ["changelog", "transitions"])

        Returns:
            Issue details
        """
        params = {}
        if fields:
            params["fields"] = ",".join(fields)
        if expand:
            params["expand"] = ",".join(expand)

        return self._request("GET", f"/issue/{issue_key}", params=params or None)

    def create_issue(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new issue.

        Args:
            fields: Issue fields dict with project, summary, issuetype, etc.

        Returns:
            Created issue with key and id

        Example:
            create_issue({
                "project": {"key": "SEC"},
                "summary": "CVE-2024-12345: Description",
                "issuetype": {"name": "Bug"},
                "priority": {"name": "High"},
                "description": "Full description..."
            })
        """
        return self._request("POST", "/issue", data={"fields": fields})

    def update_issue(
        self,
        issue_key: str,
        fields: Dict[str, Any],
        notify_users: bool = True
    ) -> None:
        """
        Update issue fields.

        Args:
            issue_key: Issue key
            fields: Fields to update
            notify_users: Whether to notify watchers
        """
        params = {"notifyUsers": str(notify_users).lower()}
        self._request("PUT", f"/issue/{issue_key}", data={"fields": fields}, params=params)

    def delete_issue(self, issue_key: str) -> None:
        """Delete an issue (use with caution)."""
        self._request("DELETE", f"/issue/{issue_key}")

    # Comments

    def add_comment(self, issue_key: str, body: str) -> Dict[str, Any]:
        """
        Add comment to issue.

        Args:
            issue_key: Issue key
            body: Comment text

        Returns:
            Created comment
        """
        return self._request("POST", f"/issue/{issue_key}/comment", data={"body": body})

    def get_comments(self, issue_key: str) -> Dict[str, Any]:
        """Get all comments on an issue."""
        return self._request("GET", f"/issue/{issue_key}/comment")

    # Transitions

    def get_transitions(self, issue_key: str) -> Dict[str, Any]:
        """
        Get available transitions for an issue.

        Returns:
            List of possible transitions with id, name, and target status
        """
        return self._request("GET", f"/issue/{issue_key}/transitions")

    def transition_issue(
        self,
        issue_key: str,
        transition_name_or_id: str,
        fields: Optional[Dict] = None,
        comment: Optional[str] = None
    ) -> None:
        """
        Perform status transition.

        Args:
            issue_key: Issue key
            transition_name_or_id: Transition name or ID
            fields: Optional fields to set during transition
            comment: Optional comment to add
        """
        # Get available transitions
        transitions = self.get_transitions(issue_key)

        # Find matching transition
        transition_id = None
        for t in transitions.get("transitions", []):
            if t["id"] == transition_name_or_id or t["name"].lower() == transition_name_or_id.lower():
                transition_id = t["id"]
                break

        if not transition_id:
            available = [t["name"] for t in transitions.get("transitions", [])]
            raise ValueError(f"Transition '{transition_name_or_id}' not found. Available: {available}")

        data = {"transition": {"id": transition_id}}

        if fields:
            data["fields"] = fields

        if comment:
            data["update"] = {
                "comment": [{"add": {"body": comment}}]
            }

        self._request("POST", f"/issue/{issue_key}/transitions", data=data)

    # Issue Links

    def link_issues(
        self,
        inward_key: str,
        outward_key: str,
        link_type: str = "Relates"
    ) -> None:
        """
        Create link between two issues.

        Args:
            inward_key: Source issue key
            outward_key: Target issue key
            link_type: Link type name (e.g., "Relates", "Blocks", "Duplicates")
        """
        data = {
            "type": {"name": link_type},
            "inwardIssue": {"key": inward_key},
            "outwardIssue": {"key": outward_key}
        }
        self._request("POST", "/issueLink", data=data)

    def get_link_types(self) -> Dict[str, Any]:
        """Get available issue link types."""
        return self._request("GET", "/issueLinkType")

    # Project Operations

    def get_project(self, project_key: str) -> Dict[str, Any]:
        """Get project details."""
        return self._request("GET", f"/project/{project_key}")

    def get_issue_types(self, project_key: str) -> List[Dict[str, Any]]:
        """Get available issue types for a project."""
        project = self.get_project(project_key)
        return project.get("issueTypes", [])

    def get_priorities(self) -> Dict[str, Any]:
        """Get available priorities."""
        return self._request("GET", "/priority")

    def get_statuses(self) -> Dict[str, Any]:
        """Get available statuses."""
        return self._request("GET", "/status")

    # User Operations

    def get_current_user(self) -> Dict[str, Any]:
        """Get current authenticated user."""
        return self._request("GET", "/myself")

    def search_users(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Search for users."""
        params = {"query": query, "maxResults": max_results}
        return self._request("GET", "/user/search", params=params)

    # Attachments

    def get_attachments(self, issue_key: str) -> List[Dict[str, Any]]:
        """Get attachments for an issue."""
        issue = self.get_issue(issue_key, fields=["attachment"])
        return issue.get("fields", {}).get("attachment", [])

    # Watchers

    def add_watcher(self, issue_key: str, username: str) -> None:
        """Add watcher to an issue."""
        self._request("POST", f"/issue/{issue_key}/watchers", data=f'"{username}"')

    def get_watchers(self, issue_key: str) -> Dict[str, Any]:
        """Get issue watchers."""
        return self._request("GET", f"/issue/{issue_key}/watchers")


def main():
    """Example usage."""
    import sys

    client = JiraClient()

    try:
        client.authenticate()
        print("Authentication successful!")

        user = client.get_current_user()
        print(f"Logged in as: {user.get('displayName')} ({user.get('emailAddress')})")

        if len(sys.argv) > 2 and sys.argv[1] == "--search":
            query = sys.argv[2]
            print(f"\nSearching for: {query}")
            results = client.search_issues(f'summary ~ "{query}"', max_results=10)

            print(f"Found {results.get('total', 0)} issues:")
            for issue in results.get("issues", []):
                key = issue["key"]
                summary = issue["fields"]["summary"]
                status = issue["fields"]["status"]["name"]
                print(f"  {key}: {summary} [{status}]")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
