import pytest

from api_tests.src.services.users.endpoints import Endpoints

# from api_tests.src.services.users.user_model import User
from api_tests.src.services.users.user_helpers import UserHelper


class TestUsers:
    # @pytest.mark.api_tests
    # def test_user_creation(self, user_client, user):
    #     User.model_validate(user)
    #     user_client.create_user(user_data=user)

    @pytest.mark.api_tests
    def test_get_user(self, user_client, created_user):
        user_id, expected_user = created_user
        actual_user = user_client.get_user(user_id)
        different_fields = UserHelper.compare_users(
            expected_user=expected_user,
            actual_user=actual_user,
        )
        assert not different_fields, f"Данные в полях {different_fields} разные"

    @pytest.mark.parametrize(
        "field, value, expected_status, expected_error",
        [
            pytest.param(
                "first_name",
                "",
                422,
                "String should have at least 1 character",
                id="Empty name",
            ),
            pytest.param(
                "age",
                "abc",
                422,
                "Input should be a valid integer, unable to parse string as an integer",
                id="Invalid age type",
            ),
            pytest.param(
                "gender",
                "Unknown",
                422,
                "Input should be 'male' or 'female'",
                id="Invalid gender value",
            ),
        ],
    )
    def test_create_user_invalid_data(
        self, generated_user, user_client, field, value, expected_status, expected_error
    ):
        generated_user[field] = value
        response = user_client.post(
            endpoint=Endpoints.create_user(),
            json=generated_user,
        )
        assert response.status_code == expected_status
        assert response.json()["detail"][0]["msg"] == expected_error

    @pytest.mark.api_tests
    def test_get_users(self, user_client):
        users = user_client.get_users()
        assert users[0].first_name == "Дмитрий"
