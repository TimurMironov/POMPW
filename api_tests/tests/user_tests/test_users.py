import pytest

# from api_tests.src.services.users.user_model import User


class TestUsers:
    # @pytest.mark.api_tests
    # def test_user_creation(self, user_client, user):
    #     User.model_validate(user)
    #     user_client.create_user(user_data=user)

    @pytest.mark.api_tests
    def test_get_user(self, user_client, created_user):
        user_client.get_user(created_user)

    @pytest.mark.api_tests
    def test_get_users(self, user_client):
        users = user_client.get_users()
        assert users[0].first_name == "Дмитрий"
