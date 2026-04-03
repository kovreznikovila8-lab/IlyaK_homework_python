from api_client import create_project, archive_project, generate_unique_title


class TestPostProjectsPositive:

    def test_create_project_with_required_fields_only(
        self,
        headers
    ) -> None:
        unique_title = generate_unique_title("Positive Create")
        response = create_project(headers, unique_title)

        assert response.status_code == 201, \
            f"Статус не 201: {response.status_code}, тело: {response.text}"
        assert "id" in response.json(), "Ответ не содержит id проекта"

        project_id = response.json()["id"]
        archive_project(headers, project_id)
