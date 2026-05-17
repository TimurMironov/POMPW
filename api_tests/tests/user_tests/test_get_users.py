import pytest


class TestGetUsers:
    @pytest.mark.api_tests
    def test_get_users(self, user_client):
        users = user_client.get_users()
        assert users[0].personal_info.first_name == "Алексей"
