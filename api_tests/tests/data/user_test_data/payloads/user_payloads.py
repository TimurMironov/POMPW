import json
from pathlib import Path

from api_tests.tests.data.user_test_data.constants import CreateUserTestType


class UserPayloads:

    @staticmethod
    def create_user_payload(user_type: CreateUserTestType) -> dict:
        path = Path(__file__).parent
        if user_type == CreateUserTestType.valid:
            path = path / "valid_user.json"
        elif user_type == CreateUserTestType.invalid:
            path = path / "invalid_user.json"
        else:
            raise ValueError(f"Unknown user type: {user_type}")

        with open(path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data
