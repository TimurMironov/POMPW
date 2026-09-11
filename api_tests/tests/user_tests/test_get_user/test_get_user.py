import pytest

from api_tests.src.services.users.user_helpers import UserHelper
from api_tests.src.services.users.user_responce import UserResponse


class TestGetUser:
    @pytest.mark.api_tests
    def test_get_user(self, authorized_user_client, prepare_user):
        expected_user = prepare_user
        response = authorized_user_client.get_user(expected_user.id)
        assert response.status_code == 200
        actual_user = UserResponse.model_validate(response.json())
        different_fields = UserHelper.compare_users(
            expected_user=expected_user,
            actual_user=actual_user,
        )
        assert not different_fields, f"Данные в полях {different_fields} разные"
