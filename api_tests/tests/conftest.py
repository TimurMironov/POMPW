import pytest

from api_tests.src.config.settings import base_settings
from api_tests.src.services.auth.auth_client import AuthClient
from api_tests.src.services.users.user_client import UserClient


@pytest.fixture(scope="session")
def user_client():
    return UserClient(base_settings)


@pytest.fixture(scope="session")
def auth_client():
    return AuthClient(base_settings)
