import pytest

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

    @pytest.mark.api_tests
    def test_get_users(self, user_client):
        users = user_client.get_users()
        assert users[0].first_name == "Дмитрий"
