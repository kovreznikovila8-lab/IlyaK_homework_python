import uuid
from api_client import get_project


class TestGetProjectsNegative:

    def test_get_nonexistent_project(
        self,
        headers
    ) -> None:
        fake_id = str(uuid.uuid4())
        response = get_project(headers, fake_id)

        assert response.status_code == 200, \
            f"Ожидался 200, получен {response.status_code}"

        data = response.json()
        is_empty = not data or "id" not in data
        assert is_empty, \
            f"Для несуществующего ID {fake_id} вернулись данные: {data}"

        assert "error" not in data, \
            f"Ответ содержит ошибку: {data}"

    def test_get_project_invalid_id_format(
        self,
        headers
    ) -> None:
        response = get_project(headers, "invalid-format")

        assert response.status_code == 400, \
            f"Ожидался 400, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "uuid", "format", "invalid", "формат", "идентификатор"
        ]), f"Сообщение об ошибке не связано с форматом ID: {error_data}"

    def test_get_project_empty_id(
        self,
        headers,
        base_url
    ) -> None:
        """Негативный: пустой ID."""
        response = get_project(headers, "")

        assert response.status_code in (400, 404), \
            f"Ожидался 400 или 404, получен {response.status_code}"

        if response.status_code != 404:
            error_data = response.json()
            assert "message" in error_data or "error" in error_data, \
                "Ответ не содержит сообщения об ошибке"
