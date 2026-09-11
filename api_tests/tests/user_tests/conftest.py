import pytest

from api_tests.src.services.auth.auth_client import AuthClient
from api_tests.src.services.users.user_client import UserClient
from api_tests.src.services.users.user_factory import UserFactory
from api_tests.src.services.users.user_helpers import UserHelper
from backend_services.services.auth_service.models.auth import Auth
from backend_services.services.auth_service.models.register_response import RegisterResponse


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


@pytest.fixture
def auth_user() -> Auth:
    return Auth(
        email="test_auth_user@example.com",
        password="TestPassword123!",
    )


@pytest.fixture
def register_user(
    auth_user: Auth,
    auth_client: AuthClient,
    user_client: UserClient,
):
    response = auth_client.register(auth_user.model_dump(by_alias=True))
    assert response.status_code == 200
    registered_user = RegisterResponse.model_validate(response.json())

    yield auth_user

    response = user_client.delete_user(user_id=registered_user.id)
    assert response.status_code == 200


@pytest.fixture
def login_user(
    register_user,
    auth_client: AuthClient,
) -> str:
    response = auth_client.login(register_user.model_dump(by_alias=True))
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.fixture
def authorized_user_client(
    login_user: str,
    user_client: UserClient,
) -> UserClient:
    user_client.session.headers.update({"Authorization": f"Bearer {login_user}"})
    return user_client
