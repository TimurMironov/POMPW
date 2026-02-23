import pytest
from loguru import logger

from api_tests.src.services.users.user_client import UserClient


class TestGetUsers:

    @pytest.mark.api_tests
    def test_get_user(self):
        user_client = UserClient()
        users = user_client.get_user(1)
        assert users.personal_info.first_name == "Алексей"