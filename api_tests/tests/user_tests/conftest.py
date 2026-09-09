import pytest

# from _pytest.runner import CallInfo
from api_tests.src.services.users.user_client import UserClient
from api_tests.src.services.users.user_factory import UserFactory
from api_tests.src.services.users.user_helpers import UserHelper


@pytest.fixture(scope="session")
def user_client():
    return UserClient()


@pytest.fixture
def generate_user():
    return UserFactory().create_user()


@pytest.fixture
def prepare_user(user_client, generate_user):
    response = user_client.create_user(user_data=generate_user)
    assert response.status_code == 200

    user_id = response.json().get("user_id")
    expected_user = UserHelper.to_response_model(
        user_data=generate_user,
        user_id=user_id,
    )

    yield expected_user

    response = user_client.delete_user(user_id=user_id)
    assert response.status_code == 200


@pytest.fixture
def update_user():
    def update(data: dict | list, key: str, new_value):
        for key_current, value in data.items():
            if key_current == key:
                data[key_current] = new_value
            elif isinstance(value, dict):
                update(value, key, new_value)
            elif isinstance(value, list):
                for item in value:
                    update(item, key, new_value)
        return data

    return update
