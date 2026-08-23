from api_tests.src.services.users.user_model import User


class UserHelper:
    @staticmethod
    def compare_users(expected_user: dict, actual_user: User) -> list[str]:
        actual_data = actual_user.model_dump()
        different_fields = []
        for key in expected_user:
            if expected_user.get(key) != actual_data.get(key):
                different_fields.append(key)
        return different_fields
