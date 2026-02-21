from api_tests.src.config.headers import Headers
from api_tests.src.services.base_client import BaseClient
from api_tests.src.services.users.endpoints import Endpoints
from api_tests.src.services.users.model import User


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def get_users(self):
        response = self.get(
            endpoint=self.endpoints.get_users,
        )
        assert response.status_code == 200
        users = [User.model_validate(user) for user in response.json()]
        return users

    def get_user(self, user_id: int):
        response = self.get(
            endpoint=self.endpoints.get_user(user_id)
        )
        assert response.status_code == 200
        return User.model_validate(response.json())