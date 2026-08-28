from api_tests.src.config.headers import Headers
from api_tests.src.config.logger import logger
from api_tests.src.services.base_client import BaseClient
from api_tests.src.services.users.endpoints import Endpoints
from api_tests.src.services.users.user_model import User


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.headers = Headers()

    def get_users(self, **kwargs):
        logger.info("Getting all users")
        response = self.request(
            method="GET",
            endpoint=Endpoints.get_users(),
            **kwargs,
        )
        assert response.status_code == 200
        users = [User.model_validate(user) for user in response.json()]
        return users

    def get_user(self, user_id: int, **kwargs) -> User:
        logger.info("Getting user with id=%s", user_id)
        response = self.request(
            method="GET",
            endpoint=Endpoints.get_user(user_id),
            **kwargs,
        )
        assert response.status_code == 200
        return User.model_validate(response.json())

    def create_user(self, user_data, **kwargs):
        logger.info("Creating user")
        response = self.request(
            method="POST",
            endpoint=Endpoints.create_user(),
            json=user_data,
            **kwargs,
        )
        assert response.status_code == 200
        return response

    def delete_user(self, user_id: int, **kwargs):
        logger.info("Deleting user with id=%s", user_id)
        response = self.request(
            method="DELETE",
            endpoint=Endpoints.delete_user(user_id),
            **kwargs,
        )
        assert response.status_code == 200
        return response

    def search_user_by_email(self, email: str, **kwargs):
        logger.info("Searching user with email=%s", email)
        response = self.request(
            method="GET",
            endpoint=Endpoints.get_by_email(email),
            **kwargs,
        )
        return response
