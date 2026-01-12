#!/usr/bin/env python3
"""
GitLab REST API Client
Core client for interacting with GitLab REST API.
"""

import json
import os
import urllib.request
import urllib.error
import urllib.parse
import ssl
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class GitLabConfig:
    """GitLab API configuration."""
    base_url: str = "https://gitlab.lan.athonet.com"
    api_path: str = "/api/v4"
    timeout: int = 30
    verify_ssl: bool = False  # Self-signed certificate


class GitLabClient:
    """
    GitLab REST API client for repository and CI/CD management.

    Supports Personal Access Token authentication.
    """

    def __init__(self, config: Optional[GitLabConfig] = None):
        """Initialize the GitLab client."""
        self.config = config or GitLabConfig()
        self.token: Optional[str] = None
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

    def authenticate(self, token: Optional[str] = None) -> bool:
        """
        Authenticate with GitLab.

        Args:
            token: Personal Access Token

        Returns:
            True if authentication successful
        """
        if not token:
            creds = self.load_credentials()
            token = creds.get('GITLAB_API_TOKEN')

            if not token:
                raise ValueError("GITLAB_API_TOKEN not found in .env file")

        self.token = token
        self.auth_header = token

        # Verify authentication
        try:
            self._request("GET", "/user")
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
    ) -> Optional[Any]:
        """
        Make HTTP request to GitLab API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
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
            "PRIVATE-TOKEN": self.auth_header,
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
                if response.status == 204:
                    return None
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else ""
            raise Exception(f"HTTP {e.code}: {e.reason} - {error_body}")
        except urllib.error.URLError as e:
            raise Exception(f"Connection error: {e.reason}")

    # User Operations

    def get_current_user(self) -> Dict[str, Any]:
        """Get current authenticated user."""
        return self._request("GET", "/user")

    # Project Operations

    def get_projects(
        self,
        search: Optional[str] = None,
        owned: bool = False,
        membership: bool = False,
        starred: bool = False,
        order_by: str = "last_activity_at",
        sort: str = "desc",
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get projects.

        Args:
            search: Search query
            owned: Only owned projects
            membership: Only projects user is member of
            starred: Only starred projects
            order_by: Order field (id, name, path, created_at, updated_at, last_activity_at)
            sort: Sort direction (asc, desc)
            per_page: Results per page
            page: Page number

        Returns:
            List of projects
        """
        params = {
            "order_by": order_by,
            "sort": sort,
            "per_page": per_page,
            "page": page
        }

        if search:
            params["search"] = search
        if owned:
            params["owned"] = "true"
        if membership:
            params["membership"] = "true"
        if starred:
            params["starred"] = "true"

        return self._request("GET", "/projects", params=params)

    def get_project(self, project_id: str) -> Dict[str, Any]:
        """
        Get project by ID or path.

        Args:
            project_id: Project ID or URL-encoded path (e.g., "group%2Fproject")

        Returns:
            Project details
        """
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        return self._request("GET", f"/projects/{encoded_id}")

    def get_project_by_path(self, path: str) -> Dict[str, Any]:
        """
        Get project by path.

        Args:
            path: Project path (e.g., "group/project")

        Returns:
            Project details
        """
        encoded_path = urllib.parse.quote(path, safe='')
        return self._request("GET", f"/projects/{encoded_path}")

    # Repository Operations

    def get_branches(
        self,
        project_id: str,
        search: Optional[str] = None,
        per_page: int = 20
    ) -> List[Dict[str, Any]]:
        """Get project branches."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        params = {"per_page": per_page}
        if search:
            params["search"] = search
        return self._request("GET", f"/projects/{encoded_id}/repository/branches", params=params)

    def get_branch(self, project_id: str, branch: str) -> Dict[str, Any]:
        """Get single branch."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        encoded_branch = urllib.parse.quote(branch, safe='')
        return self._request("GET", f"/projects/{encoded_id}/repository/branches/{encoded_branch}")

    def get_tags(
        self,
        project_id: str,
        search: Optional[str] = None,
        per_page: int = 20
    ) -> List[Dict[str, Any]]:
        """Get project tags."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        params = {"per_page": per_page}
        if search:
            params["search"] = search
        return self._request("GET", f"/projects/{encoded_id}/repository/tags", params=params)

    def get_commits(
        self,
        project_id: str,
        ref_name: Optional[str] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        path: Optional[str] = None,
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get project commits.

        Args:
            project_id: Project ID or path
            ref_name: Branch or tag name
            since: Only commits after this date (ISO 8601)
            until: Only commits before this date (ISO 8601)
            path: Only commits affecting this path
            per_page: Results per page
            page: Page number

        Returns:
            List of commits
        """
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        params = {"per_page": per_page, "page": page}

        if ref_name:
            params["ref_name"] = ref_name
        if since:
            params["since"] = since
        if until:
            params["until"] = until
        if path:
            params["path"] = path

        return self._request("GET", f"/projects/{encoded_id}/repository/commits", params=params)

    def get_commit(self, project_id: str, sha: str) -> Dict[str, Any]:
        """Get single commit."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        return self._request("GET", f"/projects/{encoded_id}/repository/commits/{sha}")

    def get_file(
        self,
        project_id: str,
        file_path: str,
        ref: str = "main"
    ) -> Dict[str, Any]:
        """
        Get file from repository.

        Args:
            project_id: Project ID or path
            file_path: Path to file
            ref: Branch, tag, or commit SHA

        Returns:
            File info with content (base64 encoded)
        """
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        encoded_path = urllib.parse.quote(file_path, safe='')
        params = {"ref": ref}
        return self._request("GET", f"/projects/{encoded_id}/repository/files/{encoded_path}", params=params)

    def get_file_content(
        self,
        project_id: str,
        file_path: str,
        ref: str = "main"
    ) -> str:
        """
        Get raw file content.

        Args:
            project_id: Project ID or path
            file_path: Path to file
            ref: Branch, tag, or commit SHA

        Returns:
            File content as string
        """
        import base64
        file_info = self.get_file(project_id, file_path, ref)
        content = file_info.get("content", "")
        return base64.b64decode(content).decode('utf-8')

    def get_tree(
        self,
        project_id: str,
        path: str = "",
        ref: str = "main",
        recursive: bool = False,
        per_page: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Get repository tree (file listing).

        Args:
            project_id: Project ID or path
            path: Path inside repository
            ref: Branch, tag, or commit SHA
            recursive: Include subdirectories
            per_page: Results per page

        Returns:
            List of tree items (files and directories)
        """
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        params = {"ref": ref, "per_page": per_page}
        if path:
            params["path"] = path
        if recursive:
            params["recursive"] = "true"

        return self._request("GET", f"/projects/{encoded_id}/repository/tree", params=params)

    # Merge Request Operations

    def get_merge_requests(
        self,
        project_id: Optional[str] = None,
        state: str = "opened",
        scope: str = "all",
        author_id: Optional[int] = None,
        assignee_id: Optional[int] = None,
        search: Optional[str] = None,
        order_by: str = "created_at",
        sort: str = "desc",
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get merge requests.

        Args:
            project_id: Project ID (None for all accessible MRs)
            state: MR state (opened, closed, merged, all)
            scope: Scope (created_by_me, assigned_to_me, all)
            author_id: Filter by author
            assignee_id: Filter by assignee
            search: Search in title and description
            order_by: Order field
            sort: Sort direction
            per_page: Results per page
            page: Page number

        Returns:
            List of merge requests
        """
        params = {
            "state": state,
            "scope": scope,
            "order_by": order_by,
            "sort": sort,
            "per_page": per_page,
            "page": page
        }

        if author_id:
            params["author_id"] = author_id
        if assignee_id:
            params["assignee_id"] = assignee_id
        if search:
            params["search"] = search

        if project_id:
            encoded_id = urllib.parse.quote(str(project_id), safe='')
            return self._request("GET", f"/projects/{encoded_id}/merge_requests", params=params)
        else:
            return self._request("GET", "/merge_requests", params=params)

    def get_merge_request(self, project_id: str, mr_iid: int) -> Dict[str, Any]:
        """Get single merge request."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        return self._request("GET", f"/projects/{encoded_id}/merge_requests/{mr_iid}")

    def get_merge_request_changes(self, project_id: str, mr_iid: int) -> Dict[str, Any]:
        """Get merge request changes (diff)."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        return self._request("GET", f"/projects/{encoded_id}/merge_requests/{mr_iid}/changes")

    # Issue Operations

    def get_issues(
        self,
        project_id: Optional[str] = None,
        state: str = "opened",
        scope: str = "all",
        labels: Optional[str] = None,
        milestone: Optional[str] = None,
        search: Optional[str] = None,
        order_by: str = "created_at",
        sort: str = "desc",
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get issues.

        Args:
            project_id: Project ID (None for all accessible issues)
            state: Issue state (opened, closed, all)
            scope: Scope (created_by_me, assigned_to_me, all)
            labels: Comma-separated label names
            milestone: Milestone title
            search: Search in title and description
            order_by: Order field
            sort: Sort direction
            per_page: Results per page
            page: Page number

        Returns:
            List of issues
        """
        params = {
            "state": state,
            "scope": scope,
            "order_by": order_by,
            "sort": sort,
            "per_page": per_page,
            "page": page
        }

        if labels:
            params["labels"] = labels
        if milestone:
            params["milestone"] = milestone
        if search:
            params["search"] = search

        if project_id:
            encoded_id = urllib.parse.quote(str(project_id), safe='')
            return self._request("GET", f"/projects/{encoded_id}/issues", params=params)
        else:
            return self._request("GET", "/issues", params=params)

    def get_issue(self, project_id: str, issue_iid: int) -> Dict[str, Any]:
        """Get single issue."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        return self._request("GET", f"/projects/{encoded_id}/issues/{issue_iid}")

    # Pipeline Operations

    def get_pipelines(
        self,
        project_id: str,
        status: Optional[str] = None,
        ref: Optional[str] = None,
        sha: Optional[str] = None,
        order_by: str = "id",
        sort: str = "desc",
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Get project pipelines.

        Args:
            project_id: Project ID or path
            status: Filter by status (running, pending, success, failed, canceled, skipped, manual)
            ref: Filter by ref (branch or tag)
            sha: Filter by commit SHA
            order_by: Order field (id, status, ref, updated_at, user_id)
            sort: Sort direction
            per_page: Results per page
            page: Page number

        Returns:
            List of pipelines
        """
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        params = {
            "order_by": order_by,
            "sort": sort,
            "per_page": per_page,
            "page": page
        }

        if status:
            params["status"] = status
        if ref:
            params["ref"] = ref
        if sha:
            params["sha"] = sha

        return self._request("GET", f"/projects/{encoded_id}/pipelines", params=params)

    def get_pipeline(self, project_id: str, pipeline_id: int) -> Dict[str, Any]:
        """Get single pipeline."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        return self._request("GET", f"/projects/{encoded_id}/pipelines/{pipeline_id}")

    def get_pipeline_jobs(
        self,
        project_id: str,
        pipeline_id: int,
        scope: Optional[str] = None,
        per_page: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Get pipeline jobs.

        Args:
            project_id: Project ID
            pipeline_id: Pipeline ID
            scope: Job scope (created, pending, running, failed, success, canceled, skipped, manual)
            per_page: Results per page

        Returns:
            List of jobs
        """
        encoded_id = urllib.parse.quote(str(project_id), safe='')
        params = {"per_page": per_page}
        if scope:
            params["scope"] = scope

        return self._request("GET", f"/projects/{encoded_id}/pipelines/{pipeline_id}/jobs", params=params)

    def get_job_log(self, project_id: str, job_id: int) -> str:
        """Get job log/trace."""
        encoded_id = urllib.parse.quote(str(project_id), safe='')

        url = f"{self.api_url}/projects/{encoded_id}/jobs/{job_id}/trace"
        headers = {"PRIVATE-TOKEN": self.auth_header}

        req = urllib.request.Request(url, headers=headers, method="GET")

        try:
            with urllib.request.urlopen(
                req,
                timeout=self.config.timeout,
                context=self.ssl_context
            ) as response:
                return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else ""
            raise Exception(f"HTTP {e.code}: {e.reason} - {error_body}")

    # Group Operations

    def get_groups(
        self,
        search: Optional[str] = None,
        owned: bool = False,
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """Get groups."""
        params = {"per_page": per_page, "page": page}
        if search:
            params["search"] = search
        if owned:
            params["owned"] = "true"

        return self._request("GET", "/groups", params=params)

    def get_group(self, group_id: str) -> Dict[str, Any]:
        """Get single group."""
        encoded_id = urllib.parse.quote(str(group_id), safe='')
        return self._request("GET", f"/groups/{encoded_id}")

    def get_group_projects(
        self,
        group_id: str,
        include_subgroups: bool = False,
        per_page: int = 20,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """Get group projects."""
        encoded_id = urllib.parse.quote(str(group_id), safe='')
        params = {"per_page": per_page, "page": page}
        if include_subgroups:
            params["include_subgroups"] = "true"

        return self._request("GET", f"/groups/{encoded_id}/projects", params=params)

    # Search

    def search(
        self,
        query: str,
        scope: str = "projects",
        project_id: Optional[str] = None,
        group_id: Optional[str] = None,
        per_page: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Global search.

        Args:
            query: Search query
            scope: Search scope (projects, issues, merge_requests, milestones, users, blobs, commits, notes, wiki_blobs)
            project_id: Limit to project
            group_id: Limit to group
            per_page: Results per page

        Returns:
            Search results
        """
        params = {"search": query, "scope": scope, "per_page": per_page}

        if project_id:
            encoded_id = urllib.parse.quote(str(project_id), safe='')
            return self._request("GET", f"/projects/{encoded_id}/search", params=params)
        elif group_id:
            encoded_id = urllib.parse.quote(str(group_id), safe='')
            return self._request("GET", f"/groups/{encoded_id}/search", params=params)
        else:
            return self._request("GET", "/search", params=params)


def main():
    """Example usage."""
    import sys

    client = GitLabClient()

    try:
        client.authenticate()
        print("Authentication successful!")

        user = client.get_current_user()
        print(f"Logged in as: {user.get('name')} (@{user.get('username')})")

        # Get projects
        print("\nRecent projects:")
        projects = client.get_projects(membership=True, per_page=5)
        for proj in projects:
            print(f"  [{proj.get('id')}] {proj.get('path_with_namespace')}")

        if len(sys.argv) > 2 and sys.argv[1] == "--search":
            query = sys.argv[2]
            print(f"\nSearching for: {query}")
            results = client.search(query, scope="projects", per_page=10)
            for result in results:
                print(f"  {result.get('path_with_namespace')}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
