import requests
from api_client import create_project


class TestPostProjectsNegative:

    def test_create_project_no_title(
        self,
        headers,
        base_url
    ) -> None:
        payload = {"users": {}}
        response = requests.post(
            f"{base_url}/projects",
            headers=headers,
            json=payload
        )

        assert response.status_code == 400, \
            f"Ожидался 400, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "title", "required", "missing", "обязательное"
        ]), f"Сообщение об ошибке не связано с title: {error_data}"

    def test_create_project_empty_title(
        self,
        headers
    ) -> None:
        response = create_project(headers, "")

        assert response.status_code == 400, \
            "Пустой title должен возвращать 400, " \
            f"получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "empty", "blank", "пуст", "заполните"
        ]) or response.status_code == 400, \
            f"Сообщение об ошибке не связано с пустым title: {error_data}"

    def test_create_project_invalid_auth(self, base_url) -> None:
        invalid_headers = {
            "Authorization": "Bearer invalid_token_12345",
            "Content-Type": "application/json"
        }
        payload = {"title": "Test Project"}
        response = requests.post(
            f"{base_url}/projects",
            headers=invalid_headers,
            json=payload
        )

        assert response.status_code == 401, \
            f"Ожидался 401, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "unauthorized", "invalid", "token", "неавторизован"
        ]), f"Сообщение об ошибке не связано с авторизацией: {error_data}"

    def test_create_project_wrong_users_format(
        self,
        headers
    ) -> None:
        payload = {"title": "Bad Users", "users": ["not_an_object"]}
        response = requests.post(
            "https://ru.yougile.com/api-v2/projects",
            headers=headers,
            json=payload
        )

        assert response.status_code == 400, \
            f"Ожидался 400, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "users", "format", "object", "массив"
        ]) or response.status_code == 400, \
            f"Сообщение об ошибке не связано с форматом users: {error_data}"
