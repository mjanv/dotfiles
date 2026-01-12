#!/usr/bin/env python3
"""
GitLab Helper
High-level operations for managing GitLab repositories and CI/CD.
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

from gitlab_client import GitLabClient, GitLabConfig


@dataclass
class Project:
    """Structured project data."""
    id: int
    name: str
    path: str
    path_with_namespace: str
    description: str = ""
    default_branch: str = "main"
    visibility: str = "private"
    web_url: str = ""
    ssh_url: str = ""
    http_url: str = ""
    created_at: Optional[str] = None
    last_activity_at: Optional[str] = None
    namespace: str = ""
    archived: bool = False
    star_count: int = 0
    forks_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "path": self.path,
            "path_with_namespace": self.path_with_namespace,
            "description": self.description,
            "default_branch": self.default_branch,
            "visibility": self.visibility,
            "web_url": self.web_url,
            "ssh_url": self.ssh_url,
            "http_url": self.http_url,
            "created_at": self.created_at,
            "last_activity_at": self.last_activity_at,
            "namespace": self.namespace,
            "archived": self.archived,
            "star_count": self.star_count,
            "forks_count": self.forks_count
        }


@dataclass
class MergeRequest:
    """Structured merge request data."""
    id: int
    iid: int
    title: str
    state: str
    source_branch: str
    target_branch: str
    project_id: int
    author: str = ""
    assignee: Optional[str] = None
    description: str = ""
    web_url: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    merged_at: Optional[str] = None
    labels: List[str] = field(default_factory=list)
    draft: bool = False
    merge_status: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "iid": self.iid,
            "title": self.title,
            "state": self.state,
            "source_branch": self.source_branch,
            "target_branch": self.target_branch,
            "project_id": self.project_id,
            "author": self.author,
            "assignee": self.assignee,
            "description": self.description,
            "web_url": self.web_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "merged_at": self.merged_at,
            "labels": self.labels,
            "draft": self.draft,
            "merge_status": self.merge_status
        }


@dataclass
class Pipeline:
    """Structured pipeline data."""
    id: int
    status: str
    ref: str
    sha: str
    project_id: int
    web_url: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    started_at: Optional[str] = None
    finished_at: Optional[str] = None
    duration: Optional[int] = None
    source: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "status": self.status,
            "ref": self.ref,
            "sha": self.sha,
            "project_id": self.project_id,
            "web_url": self.web_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "duration": self.duration,
            "source": self.source
        }


class GitLabHelper:
    """
    High-level helper for managing GitLab repositories and CI/CD.

    Provides convenience methods for common GitLab operations.
    """

    def __init__(self, config: Optional[GitLabConfig] = None):
        """Initialize the helper."""
        self.client = GitLabClient(config)
        self.connected = False

    def connect(self, token: Optional[str] = None) -> bool:
        """
        Connect to GitLab.

        Args:
            token: Personal Access Token (optional, reads from .env if not provided)

        Returns:
            True if connected successfully
        """
        self.client.authenticate(token)
        self.connected = True
        return True

    def _parse_project(self, proj: Dict[str, Any]) -> Project:
        """Parse GitLab project into Project."""
        namespace = proj.get("namespace", {})
        return Project(
            id=proj.get("id", 0),
            name=proj.get("name", ""),
            path=proj.get("path", ""),
            path_with_namespace=proj.get("path_with_namespace", ""),
            description=proj.get("description", "") or "",
            default_branch=proj.get("default_branch", "main") or "main",
            visibility=proj.get("visibility", "private"),
            web_url=proj.get("web_url", ""),
            ssh_url=proj.get("ssh_url_to_repo", ""),
            http_url=proj.get("http_url_to_repo", ""),
            created_at=proj.get("created_at"),
            last_activity_at=proj.get("last_activity_at"),
            namespace=namespace.get("full_path", "") if isinstance(namespace, dict) else "",
            archived=proj.get("archived", False),
            star_count=proj.get("star_count", 0),
            forks_count=proj.get("forks_count", 0)
        )

    def _parse_merge_request(self, mr: Dict[str, Any]) -> MergeRequest:
        """Parse GitLab MR into MergeRequest."""
        author = mr.get("author", {})
        assignee = mr.get("assignee", {})

        return MergeRequest(
            id=mr.get("id", 0),
            iid=mr.get("iid", 0),
            title=mr.get("title", ""),
            state=mr.get("state", ""),
            source_branch=mr.get("source_branch", ""),
            target_branch=mr.get("target_branch", ""),
            project_id=mr.get("project_id", 0),
            author=author.get("username", "") if author else "",
            assignee=assignee.get("username", "") if assignee else None,
            description=mr.get("description", "") or "",
            web_url=mr.get("web_url", ""),
            created_at=mr.get("created_at"),
            updated_at=mr.get("updated_at"),
            merged_at=mr.get("merged_at"),
            labels=mr.get("labels", []),
            draft=mr.get("draft", False) or mr.get("work_in_progress", False),
            merge_status=mr.get("merge_status", "")
        )

    def _parse_pipeline(self, pipe: Dict[str, Any]) -> Pipeline:
        """Parse GitLab pipeline into Pipeline."""
        return Pipeline(
            id=pipe.get("id", 0),
            status=pipe.get("status", ""),
            ref=pipe.get("ref", ""),
            sha=pipe.get("sha", ""),
            project_id=pipe.get("project_id", 0),
            web_url=pipe.get("web_url", ""),
            created_at=pipe.get("created_at"),
            updated_at=pipe.get("updated_at"),
            started_at=pipe.get("started_at"),
            finished_at=pipe.get("finished_at"),
            duration=pipe.get("duration"),
            source=pipe.get("source", "")
        )

    # Project Operations

    def list_projects(
        self,
        search: Optional[str] = None,
        owned: bool = False,
        membership: bool = True,
        starred: bool = False,
        limit: int = 20
    ) -> List[Project]:
        """
        List projects.

        Args:
            search: Search query
            owned: Only owned projects
            membership: Only projects user is member of
            starred: Only starred projects
            limit: Maximum results

        Returns:
            List of Project objects
        """
        projects = self.client.get_projects(
            search=search,
            owned=owned,
            membership=membership,
            starred=starred,
            per_page=limit
        )
        return [self._parse_project(p) for p in projects]

    def get_project(self, project_path: str) -> Project:
        """
        Get project by path.

        Args:
            project_path: Project path (e.g., "group/project")

        Returns:
            Project object
        """
        proj = self.client.get_project_by_path(project_path)
        return self._parse_project(proj)

    def search_projects(self, query: str, limit: int = 20) -> List[Project]:
        """
        Search for projects.

        Args:
            query: Search query
            limit: Maximum results

        Returns:
            List of matching Project objects
        """
        results = self.client.search(query, scope="projects", per_page=limit)
        return [self._parse_project(p) for p in results]

    # Repository Operations

    def get_file_content(
        self,
        project_path: str,
        file_path: str,
        ref: str = "main"
    ) -> str:
        """
        Get file content from repository.

        Args:
            project_path: Project path
            file_path: Path to file in repository
            ref: Branch, tag, or commit

        Returns:
            File content as string
        """
        return self.client.get_file_content(project_path, file_path, ref)

    def list_files(
        self,
        project_path: str,
        path: str = "",
        ref: str = "main",
        recursive: bool = False
    ) -> List[Dict[str, Any]]:
        """
        List files in repository.

        Args:
            project_path: Project path
            path: Directory path
            ref: Branch, tag, or commit
            recursive: Include subdirectories

        Returns:
            List of files and directories
        """
        tree = self.client.get_tree(project_path, path=path, ref=ref, recursive=recursive)
        return [{"name": item["name"], "path": item["path"], "type": item["type"]} for item in tree]

    def get_branches(self, project_path: str, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Get project branches.

        Args:
            project_path: Project path
            limit: Maximum results

        Returns:
            List of branches
        """
        branches = self.client.get_branches(project_path, per_page=limit)
        return [{"name": b["name"], "protected": b.get("protected", False), "default": b.get("default", False)} for b in branches]

    def get_tags(self, project_path: str, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Get project tags.

        Args:
            project_path: Project path
            limit: Maximum results

        Returns:
            List of tags
        """
        tags = self.client.get_tags(project_path, per_page=limit)
        return [{"name": t["name"], "message": t.get("message", ""), "commit": t.get("commit", {}).get("short_id", "")} for t in tags]

    def get_commits(
        self,
        project_path: str,
        branch: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Get recent commits.

        Args:
            project_path: Project path
            branch: Branch name
            limit: Maximum results

        Returns:
            List of commits
        """
        commits = self.client.get_commits(project_path, ref_name=branch, per_page=limit)
        return [{
            "id": c["short_id"],
            "title": c["title"],
            "author": c["author_name"],
            "date": c["committed_date"],
            "message": c["message"]
        } for c in commits]

    # Merge Request Operations

    def list_merge_requests(
        self,
        project_path: Optional[str] = None,
        state: str = "opened",
        limit: int = 20
    ) -> List[MergeRequest]:
        """
        List merge requests.

        Args:
            project_path: Project path (None for all accessible MRs)
            state: MR state (opened, closed, merged, all)
            limit: Maximum results

        Returns:
            List of MergeRequest objects
        """
        mrs = self.client.get_merge_requests(project_id=project_path, state=state, per_page=limit)
        return [self._parse_merge_request(mr) for mr in mrs]

    def get_merge_request(self, project_path: str, mr_iid: int) -> MergeRequest:
        """
        Get single merge request.

        Args:
            project_path: Project path
            mr_iid: MR internal ID

        Returns:
            MergeRequest object
        """
        mr = self.client.get_merge_request(project_path, mr_iid)
        return self._parse_merge_request(mr)

    def get_my_merge_requests(self, state: str = "opened", limit: int = 20) -> List[MergeRequest]:
        """
        Get merge requests authored by current user.

        Args:
            state: MR state
            limit: Maximum results

        Returns:
            List of MergeRequest objects
        """
        mrs = self.client.get_merge_requests(state=state, scope="created_by_me", per_page=limit)
        return [self._parse_merge_request(mr) for mr in mrs]

    def get_assigned_merge_requests(self, state: str = "opened", limit: int = 20) -> List[MergeRequest]:
        """
        Get merge requests assigned to current user.

        Args:
            state: MR state
            limit: Maximum results

        Returns:
            List of MergeRequest objects
        """
        mrs = self.client.get_merge_requests(state=state, scope="assigned_to_me", per_page=limit)
        return [self._parse_merge_request(mr) for mr in mrs]

    # Pipeline Operations

    def list_pipelines(
        self,
        project_path: str,
        status: Optional[str] = None,
        ref: Optional[str] = None,
        limit: int = 20
    ) -> List[Pipeline]:
        """
        List pipelines.

        Args:
            project_path: Project path
            status: Filter by status
            ref: Filter by branch/tag
            limit: Maximum results

        Returns:
            List of Pipeline objects
        """
        pipelines = self.client.get_pipelines(project_path, status=status, ref=ref, per_page=limit)
        return [self._parse_pipeline(p) for p in pipelines]

    def get_pipeline(self, project_path: str, pipeline_id: int) -> Pipeline:
        """
        Get single pipeline.

        Args:
            project_path: Project path
            pipeline_id: Pipeline ID

        Returns:
            Pipeline object
        """
        pipe = self.client.get_pipeline(project_path, pipeline_id)
        return self._parse_pipeline(pipe)

    def get_pipeline_jobs(
        self,
        project_path: str,
        pipeline_id: int
    ) -> List[Dict[str, Any]]:
        """
        Get pipeline jobs.

        Args:
            project_path: Project path
            pipeline_id: Pipeline ID

        Returns:
            List of jobs
        """
        jobs = self.client.get_pipeline_jobs(project_path, pipeline_id)
        return [{
            "id": j["id"],
            "name": j["name"],
            "stage": j["stage"],
            "status": j["status"],
            "duration": j.get("duration"),
            "web_url": j.get("web_url", "")
        } for j in jobs]

    def get_job_log(self, project_path: str, job_id: int) -> str:
        """
        Get job log.

        Args:
            project_path: Project path
            job_id: Job ID

        Returns:
            Job log as string
        """
        return self.client.get_job_log(project_path, job_id)

    def get_latest_pipeline(self, project_path: str, ref: Optional[str] = None) -> Optional[Pipeline]:
        """
        Get latest pipeline.

        Args:
            project_path: Project path
            ref: Branch/tag filter

        Returns:
            Latest Pipeline or None
        """
        pipelines = self.list_pipelines(project_path, ref=ref, limit=1)
        return pipelines[0] if pipelines else None

    # Issue Operations

    def list_issues(
        self,
        project_path: Optional[str] = None,
        state: str = "opened",
        labels: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        List issues.

        Args:
            project_path: Project path
            state: Issue state
            labels: Label filter
            limit: Maximum results

        Returns:
            List of issues
        """
        issues = self.client.get_issues(project_id=project_path, state=state, labels=labels, per_page=limit)
        return [{
            "id": i["id"],
            "iid": i["iid"],
            "title": i["title"],
            "state": i["state"],
            "author": i.get("author", {}).get("username", ""),
            "labels": i.get("labels", []),
            "web_url": i.get("web_url", ""),
            "created_at": i.get("created_at")
        } for i in issues]

    # Search

    def search_code(
        self,
        query: str,
        project_path: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Search code (blobs).

        Args:
            query: Search query
            project_path: Limit to project
            limit: Maximum results

        Returns:
            Search results
        """
        results = self.client.search(query, scope="blobs", project_id=project_path, per_page=limit)
        return [{
            "path": r.get("path", ""),
            "filename": r.get("filename", ""),
            "project_id": r.get("project_id"),
            "data": r.get("data", "")[:200]  # First 200 chars
        } for r in results]


def main():
    """Example usage."""
    helper = GitLabHelper()

    try:
        helper.connect()
        print("Connected to GitLab!")

        # Get current user
        user = helper.client.get_current_user()
        print(f"Logged in as: {user.get('name')} (@{user.get('username')})")

        # List projects
        print("\nRecent projects:")
        projects = helper.list_projects(limit=5)
        for proj in projects:
            print(f"  {proj.path_with_namespace} - {proj.description[:50] if proj.description else 'No description'}...")

        # List open MRs
        print("\nOpen merge requests:")
        mrs = helper.list_merge_requests(state="opened", limit=5)
        for mr in mrs:
            print(f"  !{mr.iid}: {mr.title} ({mr.source_branch} -> {mr.target_branch})")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()