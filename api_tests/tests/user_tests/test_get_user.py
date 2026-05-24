import pytest


class TestGetUsers:
    @pytest.mark.api_tests
    def test_get_user(self, user_client):
        users = user_client.get_user(1)
        assert users.personal_info.first_name == "Дмитрий"
