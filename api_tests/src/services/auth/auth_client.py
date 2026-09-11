from requests import Response

from api_tests.src.config.headers import Headers
from api_tests.src.config.logger import logger
from api_tests.src.services.auth.endpoints import AuthEndpoints
from api_tests.src.services.base_client import BaseClient


class AuthClient(BaseClient):
    def __init__(self, settings):
        super().__init__(settings)
        self.headers = Headers()

    def register(self, user_data, **kwargs) -> Response:
        logger.info("Register user")
        response = self.request(
            method="POST",
            endpoint=AuthEndpoints.register(),
            json=user_data,
            **kwargs,
        )
        return response

    def login(self, user_data, **kwargs) -> Response:
        logger.info("Login user")
        response = self.request(
            method="POST",
            endpoint=AuthEndpoints.login(),
            data={
                "username": user_data["email"],
                "password": user_data["password"],
            },
            **kwargs,
        )
        return response
