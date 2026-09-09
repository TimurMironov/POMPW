from requests import Response

from api_tests.src.config.headers import Headers
from api_tests.src.config.logger import logger
from api_tests.src.config.settings import Settings, base_settings
from api_tests.src.services.base_client import BaseClient
from api_tests.src.services.users.endpoints import Endpoints


class UserClient(BaseClient):
    def __init__(self, settings: Settings = base_settings):
        super().__init__(settings=settings)
        self.headers = Headers()

    def get_users(self, **kwargs):
        logger.info("Getting all users")
        response = self.request(
            method="GET",
            endpoint=Endpoints.get_users(),
            **kwargs,
        )
        return response

    def get_user(self, user_id: int, **kwargs) -> Response:
        logger.info("Getting user with id=%s", user_id)
        response = self.request(
            method="GET",
            endpoint=Endpoints.get_user(user_id),
            **kwargs,
        )
        return response

    def create_user(self, user_data, **kwargs) -> Response:
        logger.info("Creating user")
        response = self.request(
            method="POST",
            endpoint=Endpoints.create_user(),
            json=user_data,
            **kwargs,
        )
        return response

    def delete_user(self, user_id: int, **kwargs):
        logger.info("Deleting user with id=%s", user_id)
        response = self.request(
            method="DELETE",
            endpoint=Endpoints.delete_user(user_id),
            **kwargs,
        )
        return response

    def search_user_by_email(self, email: str, **kwargs):
        logger.info("Searching user with email=%s", email)
        response = self.request(
            method="GET",
            endpoint=Endpoints.get_by_search(),
            params={"email": email},
            **kwargs,
        )
        return response
