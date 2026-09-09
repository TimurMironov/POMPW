from api_tests.src.services.users.user_responce import UserResponse


class UserHelper:
    @staticmethod
    def to_response_model(
        user_data: dict,
        user_id: int,
    ) -> UserResponse:
        response_data = user_data.copy()

        response_data["id"] = user_id
        response_data.pop("password", None)

        return UserResponse.model_validate(response_data)

    @staticmethod
    def compare_users(expected_user: UserResponse, actual_user: UserResponse) -> list[str]:
        actual_data = actual_user.model_dump()
        expected_user = expected_user.model_dump()
        different_fields = []
        for key in expected_user:
            if expected_user.get(key) != actual_data.get(key):
                different_fields.append(key)
        return different_fields
