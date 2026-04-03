import uuid
import requests
from typing import Dict, List, Optional


def create_project(
    headers: Dict[str, str],
    title: str,
    users: Optional[Dict[str, str]] = None
) -> requests.Response:
    payload = {"title": title}
    if users:
        payload["users"] = users
    return requests.post(
        "https://ru.yougile.com/api-v2/projects",
        headers=headers,
        json=payload
    )


def update_project(
    headers: Dict[str, str],
    project_id: str,
    title: Optional[str] = None,
    users: Optional[Dict[str, str]] = None
) -> requests.Response:
    payload = {}
    if title is not None:
        payload["title"] = title
    if users is not None:
        payload["users"] = users
    return requests.put(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        headers=headers,
        json=payload
    )


def get_project(
    headers: Dict[str, str],
    project_id: str
) -> requests.Response:
    return requests.get(
        f"https://ru.yougile.com/api-v2/projects/{project_id}",
        headers=headers
    )


def get_all_projects(headers: Dict[str, str]) -> List[Dict]:
    response = requests.get(
        "https://ru.yougile.com/api-v2/projects",
        headers=headers
    )
    if response.status_code != 200:
        return []

    data = response.json()
    if "content" in data:
        return data["content"]
    return []


def archive_project(
    headers: Dict[str, str],
    project_id: str
) -> requests.Response:
    return update_project(
        headers,
        project_id,
        title=f"[ARCHIVED_{uuid.uuid4().hex[:6]}]"
    )


def cleanup_test_projects(
    headers: Dict[str, str],
    test_prefix: str = "Test Project"
) -> int:
    projects = get_all_projects(headers)
    cleaned_count = 0

    for project in projects:
        title = project.get("title", "")
        if title.startswith(test_prefix) or "[ARCHIVED]" in title:
            archive_project(headers, project["id"])
            cleaned_count += 1

    return cleaned_count


def generate_unique_title(prefix: str = "Test Project") -> str:
    return f"{prefix} {uuid.uuid4().hex[:8]}"
