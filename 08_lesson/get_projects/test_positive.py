from api_client import get_project


class TestGetProjectsPositive:

    def test_get_existing_project(
        self,
        headers,
        created_project_id
    ) -> None:
        response = get_project(headers, created_project_id)

        assert response.status_code == 200, \
            f"Ожидался 200, получен {response.status_code}"

        data = response.json()
        assert "id" in data, "Ответ не содержит id"
        assert data["id"] == created_project_id, "ID не совпадает"
        assert "title" in data, "Ответ не содержит title"
        assert isinstance(data["title"], str)
