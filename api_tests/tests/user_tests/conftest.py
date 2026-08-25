import pytest

from api_tests.src.services.users.user_client import UserClient
from api_tests.src.services.users.user_factory import UserFactory
from api_tests.src.services.users.user_model import User


@pytest.fixture
def user_client():
    return UserClient()


@pytest.fixture
def generated_user():
    return UserFactory().create_user()


@pytest.fixture
def created_user(user_client, generated_user):
    User.model_validate(generated_user)
    user = user_client.create_user(user_data=generated_user)
    user_id = user.json().get("user_id")

    yield user_id, generated_user

    user_client.delete_user(user_id=user_id)
