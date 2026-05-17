import pytest

from api_tests.src.services.users.user_client import UserClient


@pytest.fixture
def user_client():
    return UserClient()
