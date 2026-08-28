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
        logger.info("/GET %s", Endpoints.get_users())
        response = self.get(
            endpoint=Endpoints.get_users(),
            **kwargs,
        )
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.json())
        assert response.status_code == 200
        users = [User.model_validate(user) for user in response.json()]
        return users

    def get_user(self, user_id: int, **kwargs) -> User:
        logger.info("/GET %s", Endpoints.get_user(user_id))
        response = self.get(
            endpoint=Endpoints.get_user(user_id),
            **kwargs,
        )
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.json())
        assert response.status_code == 200
        return User.model_validate(response.json())

    def create_user(self, user_data, **kwargs):
        logger.info("/POST %s", Endpoints.create_user())
        logger.debug("Request body: %s", user_data)
        response = self.post(
            endpoint=Endpoints.create_user(),
            json=user_data,
            **kwargs,
        )
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.json())
        assert response.status_code == 200
        return response

    def delete_user(self, user_id: int, **kwargs):
        logger.info("/DELETE %s", Endpoints.delete_user(user_id))
        response = self.delete(
            endpoint=Endpoints.delete_user(user_id),
            **kwargs,
        )
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.json())
        assert response.status_code == 200
        return response

    def search_user_by_email(self, email: str, **kwargs):
        logger.info("/GET %s", Endpoints.get_by_email(email))
        response = self.get(
            endpoint=Endpoints.get_by_email(email),
            **kwargs,
        )
        logger.debug("Response status: %s", response.status_code)
        logger.debug("Response body: %s", response.json())
        return response
