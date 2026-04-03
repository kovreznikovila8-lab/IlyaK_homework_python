import os
import pytest
from typing import Dict

from api_client import (
    create_project,
    archive_project,
    cleanup_test_projects,
    generate_unique_title
)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_required_env(var_name: str) -> str:
    value = os.environ.get(var_name)
    if not value:
        pytest.fail(
            f"Переменная окружения {var_name} не установлена.\n"
            f"Установите её командой:\n"
            f"export {var_name}='значение'\n"
            f"Или создайте файл .env в корне проекта"
        )
    return value


@pytest.fixture(scope="session")
def api_key() -> str:
    return get_required_env("YOUGILE_API_KEY")


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")


@pytest.fixture(scope="session")
def headers(api_key: str) -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


@pytest.fixture(autouse=True)
def auto_cleanup(request, headers):
    def cleanup():
        # Очищаем все тестовые проекты
        count = cleanup_test_projects(headers)
        if count > 0:
            print(f"\n🧹 Очищено {count} тестовых проектов")

    request.addfinalizer(cleanup)


@pytest.fixture
def created_project_id(headers: Dict[str, str]) -> str:
    title = generate_unique_title("Test Project")
    response = create_project(headers, title)
    assert response.status_code == 201, \
        f"Не удалось создать проект: {response.text}"
    project_id = response.json()["id"]

    yield project_id

    try:
        archive_project(headers, project_id)
    except Exception as e:
        print(f"Warning: Не удалось архивировать {project_id}: {e}")


@pytest.fixture
def clean_environment(headers):
    # Очищаем перед тестом
    cleanup_test_projects(headers)

    yield

    # Очищаем после теста
    cleanup_test_projects(headers)
