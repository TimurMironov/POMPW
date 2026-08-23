import pytest

from api_tests.src.services.users.user_client import UserClient
from api_tests.src.services.users.user_factory import UserFactory
from api_tests.src.services.users.user_model import User


@pytest.fixture
def user_client():
    return UserClient()


@pytest.fixture
def created_user(user_client):
    user_data = UserFactory().create_user()
    User.model_validate(user_data)
    user = user_client.create_user(user_data=user_data)
    user_id = user.json().get("user_id")

    yield user_id, user

    user_client.delete_user(user_id=user_id)
