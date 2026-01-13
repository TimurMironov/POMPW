from api_tests.src.config.headers import Headers
from api_tests.src.services.base_client import BaseClient
from api_tests.src.services.users.endpoints import Endpoints


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def get_users(self):
        response = self.get(
            endpoint=self.endpoints.get_users,
        )
        # assert response.status_code == 200
        return response