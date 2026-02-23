from api_tests.src.services.users.user_client import UserClient
from api_tests.src.services.users.user_model import User
from api_tests.tests.data.user_test_data.constants import CreateUserTestType
from api_tests.tests.data.user_test_data.payloads.user_payloads import UserPayloads


class TestCreateUser:

    def test_user_creation(self):
        user_payload = UserPayloads.create_user_payload(user_type=CreateUserTestType.valid)
        User.model_validate(user_payload)
        user_client = UserClient()
        user_client.create_user(user_data=user_payload)

