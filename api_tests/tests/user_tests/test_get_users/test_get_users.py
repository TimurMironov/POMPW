import pytest


class TestGetUsers:
    @pytest.mark.api_tests
    def test_get_users(self, authorized_user_client):
        response = authorized_user_client.get_users()
        assert response.status_code == 200
