import pytest

from api_tests.src.services.users.user_model import User
from api_tests.tests.user_tests.payloads.user_payloads import (
    CreateUserTestType,
    UserPayloads,
)


class TestUsers:
    @pytest.mark.api_tests
    def test_user_creation(self, user_client):
        user_payload = UserPayloads.create_user_payload(
            user_type=CreateUserTestType.valid
        )
        User.model_validate(user_payload)
        user_client.create_user(user_data=user_payload)

    @pytest.mark.api_tests
    def test_get_user(self, user_client):
        users = user_client.get_user(1)
        assert users.first_name == "Дмитрий"

    @pytest.mark.api_tests
    def test_get_users(self, user_client):
        users = user_client.get_users()
        assert users[0].first_name == "Дмитрий"
