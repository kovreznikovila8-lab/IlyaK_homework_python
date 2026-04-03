import uuid
from api_client import update_project


class TestPutProjectsNegative:

    def test_update_project_invalid_id(
        self,
        headers
    ) -> None:
        fake_id = str(uuid.uuid4())
        response = update_project(headers, fake_id, title="New Title")

        assert response.status_code in (400, 404), \
            f"Ожидался 400/404, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "not found", "does not exist", "не найден", "project"
        ]) or response.status_code == 400, \
            "Сообщение об ошибке не связано с отсутствием проекта: " \
            f"{error_data}"

    def test_update_project_malformed_id(
        self,
        headers
    ) -> None:
        response = update_project(headers, "not-a-uuid", title="Bad ID")

        assert response.status_code in (400, 422), \
            f"Ожидался 400 или 422, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "uuid", "format", "invalid", "формат", "идентификатор"
        ]), f"Сообщение об ошибке не связано с форматом ID: {error_data}"

    def test_update_project_no_fields(
        self,
        headers,
        created_project_id
    ) -> None:
        response = update_project(headers, created_project_id)

        assert response.status_code == 400, \
            f"Ожидался 400, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "empty", "no fields", "nothing", "пуст", "нет данных"
        ]) or response.status_code == 400, \
            f"Сообщение об ошибке не связано с отсутствием полей: {error_data}"

    def test_update_project_with_empty_title(
        self,
        headers,
        created_project_id
    ) -> None:
        response = update_project(headers, created_project_id, title="")

        assert response.status_code == 400, \
            f"Ожидался 400, получен {response.status_code}"

        error_data = response.json()
        assert "message" in error_data or "error" in error_data, \
            "Ответ не содержит сообщения об ошибке"

        error_message = str(error_data).lower()
        assert any(keyword in error_message for keyword in [
            "empty", "blank", "title", "пуст", "заполните"
        ]), f"Сообщение об ошибке не связано с пустым title: {error_data}"
