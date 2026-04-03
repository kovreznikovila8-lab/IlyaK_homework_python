from api_client import update_project, get_project, generate_unique_title


class TestPutProjectsPositive:

    def test_update_project_title(
        self,
        headers,
        created_project_id
    ) -> None:
        new_title = generate_unique_title("Updated Title")
        response = update_project(
            headers,
            created_project_id,
            title=new_title
        )

        assert response.status_code == 200, \
            f"Ошибка обновления: {response.status_code}, {response.text}"

        get_response = get_project(headers, created_project_id)
        assert get_response.status_code == 200
        assert get_response.json().get("title") == new_title, \
            "Название не обновилось"
